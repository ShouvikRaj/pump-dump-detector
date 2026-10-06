import json
import math

import pytest

from pumpdump import db, text
from pumpdump.tickers import TickerExtractor

DAY = 86_400
AS_OF = 1_791_209_356.0  # 2026-10-05 14:09:16 UTC


def doc(id_, created, collected=None, kind="comment", author="alice", title=None, body="", url=None, sub="pennystocks"):
    return {"id": id_, "kind": kind, "subreddit": sub, "author": author, "created_utc": created,
            "collected_at": created + 30 if collected is None else collected, "source": "arctic_shift",
            "source_retrieved_at": created + 20, "title": title, "body": body, "link_id": None, "parent_id": None,
            "url": url, "permalink": f"/r/{sub}/{id_}", "flair": None, "score": 1, "num_comments": 0, "run_id": "r"}


def documents(*records, ticker="ABCD", as_of=AS_OF):
    conn = db.connect()
    db.insert_docs(conn, records)
    ext = TickerExtractor(universe={"ABCD", "WXYZ", "GME"}, common_words={"the"}, acronyms={"CEO"}, cashtag_block=set())
    db.extract_mentions(conn, ext, {"AutoModerator"})
    return text.flag_documents(conn, ticker, as_of)


def test_only_documents_known_at_the_flag_count():
    docs = documents(
        doc("t1_a", AS_OF - 3600, body="$ABCD looks good"),
        doc("t1_late", AS_OF - 3600, collected=AS_OF + 60, body="$ABCD archived after the flag"),
        doc("t1_old", AS_OF - DAY - 60, body="$ABCD from the day before"),
        doc("t1_after", AS_OF + 10, collected=AS_OF + 40, body="$ABCD written after the flag"),
        doc("t1_other", AS_OF - 600, body="$WXYZ only"),
        doc("t1_bot", AS_OF - 300, author="AutoModerator", body="$ABCD daily thread"),
        doc("t3_p", AS_OF - 7200, kind="post", title="ABCD DD", body="float is tiny"),
    )
    assert [d["id"] for d in docs] == ["t3_p", "t1_a"]  # oldest first
    assert docs[0]["title"] == "ABCD DD" and docs[0]["kind"] == "post"


def test_text_features_are_shares_of_the_flag_documents():
    docs = documents(
        doc("t3_1", AS_OF - 5000, kind="post", author="pumper", title="$ABCD next GME",
            body="Get in now before it's too late, PT $5. Low float!", url="https://promo-site.example/abcd"),
        doc("t1_2", AS_OF - 4000, author="pumper", body="$ABCD short squeeze incoming, get in now before it's too late"),
        doc("t1_3", AS_OF - 3000, author="other", body="ABCD announced earnings beat, revenue up"),
        doc("t1_4", AS_OF - 2000, author="third", body="ABCD and WXYZ on my watch list, offering risk though"),
    )
    f = text.text_features(docs, "ABCD")
    assert f["n_docs"] == 4
    assert f["top_author_share"] == 0.5
    assert f["promo_share"] == 0.5  # urgency / price target / low float / next big in the first two
    assert f["squeeze_share"] == 0.25
    assert f["news_share"] == 0.25
    assert f["dilution_share"] == 0.25
    assert f["link_share"] == 0.25  # reddit links don't count
    assert f["multi_ticker_share"] == 0.5  # "next GME" and the watch list
    assert f["dup_share"] == 0.0
    assert f["length_log"] == pytest.approx(math.log1p(sum(len(d["title"] or "") + len(d["body"] or "") for d in docs) / 4))


def test_copy_paste_counts_only_across_authors():
    pitch = "This one is going to run hard, huge news coming, load up on {} today"
    docs = documents(
        doc("t1_1", AS_OF - 500, author="a", body=pitch.format("$ABCD")),
        doc("t1_2", AS_OF - 400, author="b", body=pitch.format("ABCD") + " https://reddit.com/r/x"),
        doc("t1_3", AS_OF - 300, author="c", body="ABCD meh, sold my position this morning and moved on"),
        doc("t1_4", AS_OF - 200, author="c", body="ABCD meh, sold my position this morning and moved on"),  # one author
        doc("t1_5", AS_OF - 100, author="d", body="ABCD 1"),
        doc("t1_6", AS_OF - 50, author="e", body="ABCD 2"),  # identical once digits go, but too short to judge
    )
    assert text.text_features(docs, "ABCD")["dup_share"] == pytest.approx(2 / 6)


def test_no_documents_means_no_text_features():
    f = text.text_features([], "ABCD")
    assert f["n_docs"] == 0 and all(f[k] is None for k in text.TEXT_FEATURES)


def snapshot(**extra):
    row = {"ticker": "ABCD", "name": "Abcd Therapeutics", "venue": "listed", "price_at_flag": "3.21", "cik": "123",
           "last_current_report_at": "2026-10-01T20:05:00Z", "last_current_report_items": "2.02,9.01",
           "last_dilution_at": "2026-09-15T21:00:00Z", "last_dilution_form": "S-3"}
    row.update(extra)
    return row


def test_prompt_shows_posts_first_anonymises_authors_and_caps_its_size():
    records = [doc("t3_p", AS_OF - 9000, kind="post", author="promoter", title="$ABCD to the moon", body="DD inside")]
    records += [doc(f"t1_{i:03d}", AS_OF - 8000 + i, author=f"user{i % 7}", body=f"$ABCD comment {i} " + "x" * 600)
                for i in range(60)]
    system, user = text.build_prompt(snapshot(), documents(*records), AS_OF)
    assert "JSON" in system
    assert "Abcd Therapeutics" in user and "$3.21" in user and "2026-10-05 14:09 UTC" in user
    assert "8-K" in user and "2.02" in user and "S-3 on 2026-09-15" in user
    assert "promoter" not in user and "user3" not in user
    lines = [ln for ln in user.splitlines() if ln.startswith("[")]
    assert lines[0].startswith("[1] post, r/pennystocks, A1")
    assert "comment 59" in user and "comment 0 " not in user  # the most recent comments are kept
    assert len(lines) <= text.MAX_DOCS and sum(len(ln) for ln in lines) <= text.MAX_CHARS
    assert all(len(ln) <= text.DOC_CHARS + 60 for ln in lines)


def test_prompt_for_a_company_without_sec_filings():
    _, user = text.build_prompt(snapshot(cik="", last_current_report_at="", last_dilution_at="", last_dilution_form=""),
                                documents(doc("t1_a", AS_OF - 60, body="$ABCD")), AS_OF)
    assert "not an SEC filer" in user


def test_parse_rating_reads_the_json_and_keeps_values_in_range():
    content = '```json\n{"promotion": 3, "coordination": 5, "news": 0, "sentiment": -1.6, "catalyst": "Earnings", ' \
              '"summary": "Pump talk."}\n```'
    r = text.parse_rating(content)
    assert r == {"llm_promotion": 3, "llm_coordination": 3, "llm_news": 0, "llm_sentiment": -2,
                 "llm_catalyst": "earnings", "llm_summary": "Pump talk."}
    assert text.parse_rating('{"promotion": 1, "coordination": 0, "news": 2, "sentiment": 0, "catalyst": "merger"}')[
        "llm_catalyst"] == "other"
    with pytest.raises(ValueError):
        text.parse_rating("I can't help with that.")
    with pytest.raises(ValueError):
        text.parse_rating('{"promotion": "high"}')


class FakePost:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, url, headers=None, json=None, timeout=None):
        self.calls.append({"url": url, "headers": headers, "json": json})
        status, body = self.responses.pop(0)
        return FakeResponse(status, body)


class FakeResponse:
    def __init__(self, status, body):
        self.status_code = status
        self._body = body
        self.text = body if isinstance(body, str) else json.dumps(body)
        self.headers = {}

    def json(self):
        return self._body


def test_github_models_client_sends_the_prompt_with_the_built_in_token():
    post = FakePost((200, {"choices": [{"message": {"content": '{"promotion": 1}'}}]}))
    client = text.GitHubModels("tok", post=post, sleep=lambda s: None)
    assert client.complete("sys", "user") == '{"promotion": 1}'
    call = post.calls[0]
    assert call["url"] == text.GITHUB_MODELS_URL and call["headers"]["Authorization"] == "Bearer tok"
    assert call["json"]["model"] == text.LLM_MODEL and call["json"]["temperature"] == 0
    assert [m["role"] for m in call["json"]["messages"]] == ["system", "user"]


def test_github_models_client_tells_a_refusal_from_a_retryable_error():
    client = text.GitHubModels("tok", post=FakePost((400, {"error": {"code": "content_filter"}})), sleep=lambda s: None)
    with pytest.raises(text.LLMRefused):
        client.complete("sys", "user")
    for status, body in ((429, "busy"), (500, "busy"), (403, "no access"),
                         (400, {"error": {"code": "unknown_model", "message": "Unknown model: x"}})):
        client = text.GitHubModels("tok", post=FakePost((status, body)), sleep=lambda s: None)
        with pytest.raises(text.LLMError) as exc:
            client.complete("sys", "user")
        assert not isinstance(exc.value, text.LLMRefused)


def test_github_models_client_spaces_its_calls():
    sleeps, now = [], [100.0]
    ok = (200, {"choices": [{"message": {"content": "{}"}}]})
    client = text.GitHubModels("tok", post=FakePost(ok, ok), sleep=sleeps.append, clock=lambda: now[0], min_interval=4.5)
    client.complete("s", "u")
    now[0] += 1.0
    client.complete("s", "u")
    assert sleeps == [3.5]
