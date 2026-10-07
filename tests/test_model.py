import csv
import json
import math
from datetime import datetime, timezone

import pytest

pytest.importorskip("lightgbm")

from model_fakes import HOLDOUT, START, close_ts, letters, make_datastore, sessions_after  # noqa: E402
from pumpdump import cli, model, technical, text  # noqa: E402
from pumpdump.market import SNAPSHOTS  # noqa: E402

DAY = 86_400


def test_weeks_start_on_monday_00_utc():
    wednesday = datetime(2026, 10, 7, 15, tzinfo=timezone.utc).timestamp()
    assert model.week_start(wednesday) == START
    assert model.week_start(START) == START
    assert model.week_start(START - 1) == START - 7 * DAY
    assert model.HOLDOUT_START == HOLDOUT == model.week_start(HOLDOUT)


def test_targets_follow_stage_4():
    assert model.targets({"crash_10": "1", "label": "pending"}) == {"crash": 1, "pump": None}
    assert model.targets({"crash_10": "0", "label": "real_news"}) == {"crash": 0, "pump": 0}
    assert model.targets({"crash_10": "", "label": "pump"}) == {"crash": None, "pump": 1}
    assert model.targets({"crash_10": "0", "label": "unknown"}) == {"crash": 0, "pump": None}
    assert model.targets({"crash_10": "", "label": "not_pump"})["pump"] == 0


def test_a_label_counts_from_the_close_of_the_session_that_settles_it():
    as_of = START + 14 * 3600  # Monday 10:00 ET
    days = {k: d.isoformat() for k, d in enumerate(sessions_after(as_of, START + 60 * DAY), 1)}
    lab = {"track_status": "active", "ret_max_5": "0.1"}
    four_h = 4 * 3600
    assert model.available_at(lab, days, "crash") == close_ts(sessions_after(as_of, START + 60 * DAY)[9]) + four_h
    assert model.available_at(lab, days, "pump") == model.available_at(lab, days, "crash")
    assert model.available_at({**lab, "ret_max_5": "0.6"}, days, "pump") == close_ts(
        sessions_after(as_of, START + 60 * DAY)[14]) + four_h
    short = {k: d for k, d in days.items() if k <= 7}
    assert model.available_at(lab, short, "crash") is None  # still tracked: wait for session 10
    assert model.available_at({**lab, "track_status": "expired"}, short, "crash") == close_ts(
        sessions_after(as_of, START + 60 * DAY)[6]) + four_h
    assert model.available_at({**lab, "track_status": "no_data"}, {}, "crash") is None


EPISODE = {"mentions_24h": "20", "authors_24h": "10", "posts_24h": "5", "baseline_mean": "1.5", "z": "4.2",
           "hype_docs_24h": "8", "reasons": "mention_spike hype_spike",
           "by_subreddit": '{"wallstreetbets": 15, "pennystocks": 5}', "methods": '{"cashtag": 4, "bare": 16}',
           "stocktwits_rank": ""}
AS_OF = datetime(2026, 10, 5, 14, tzinfo=timezone.utc).timestamp()
SNAP = {"role": "candidate", "as_of": str(AS_OF), "price_at_flag": "2.5", "move_since_close": "0.1", "ret_1d": "0.2",
        "rel_vol_last": "3", "rel_vol_today": "", "float_shares": "", "shares_outstanding": "4000000",
        "market_cap": "10000000", "venue": "otc", "first_trade_date": "2026-09-05", "reverse_splits_1y": "1",
        "cik": "77", "si_shares": "150", "si_prev_shares": "100", "si_pct_float": "0.2",
        "last_current_report_at": "2026-10-03T14:00:00Z", "last_current_report_items": "1.01,9.01",
        "last_dilution_at": "", "dilution_filings_90d": "0", "last_name_change": "2026-03-01"}


def test_candidate_features_come_from_its_episode_snapshot_and_text():
    text_row = dict.fromkeys(text.TEXT_FEATURES, "0.25")
    llm_row = {"status": "ok", "llm_version": text.LLM_VERSION, "llm_about_share": "1", "llm_pitch_share": "0.5",
               "llm_warning_share": "0", "llm_event_share": "0.1", "llm_sentiment": "2"}
    f = model.features(SNAP, EPISODE, text_row, llm_row)
    assert set(f) == set(model.FEATURES)
    assert f["mentions_log"] == pytest.approx(math.log1p(20)) and f["baseline_log"] == pytest.approx(math.log1p(1.5))
    assert (f["spike_z"], f["authors_ratio"], f["post_share"], f["hype_share"], f["hype_spike"]) == (4.2, 0.5, 0.25, 0.4, 1)
    assert (f["wsb_share"], f["pennystocks_share"], f["cashtag_share"], f["stocktwits_trending"]) == (0.75, 0.25, 0.2, 0)
    assert f["top_author_share"] == 0.25 and f["near_dup_share"] == 0.25
    assert f["llm_pitch_share"] == 0.5 and f["llm_sentiment"] == 2
    assert f["price_log"] == pytest.approx(math.log(2.5)) and f["rel_vol_last_log"] == pytest.approx(math.log1p(3))
    assert f["rel_vol_today_log"] is None
    assert f["float_log"] == pytest.approx(math.log1p(4e6))  # no float: shares outstanding
    assert f["otc"] == 1 and f["sec_filer"] == 1 and f["si_change"] == pytest.approx(0.5)
    first_trade = datetime(2026, 9, 5, tzinfo=timezone.utc).timestamp()
    assert f["listing_age_log"] == pytest.approx(math.log1p((AS_OF - first_trade) / DAY))
    assert f["days_since_report"] == pytest.approx(2.0) and f["report_hard_news"] == 1
    assert f["days_since_dilution"] is None and f["name_change_1y"] == 1


def test_controls_have_no_chatter_and_failed_ratings_count_as_missing():
    f = model.features({**SNAP, "role": "control"}, EPISODE, None, None)
    assert f["mentions_log"] == 0 and f["baseline_log"] == 0
    assert all(f[k] is None for k in model.GROUPS["chatter"][2:] + model.GROUPS["text"] + model.GROUPS["llm"])
    assert f["price_log"] == pytest.approx(math.log(2.5))
    f = model.features(SNAP, EPISODE, None, {"status": "failed", "llm_pitch_share": "", "llm_version": text.LLM_VERSION})
    assert f["llm_pitch_share"] is None and f["mentions_log"] > 0
    old = {"status": "ok", "llm_version": "llm-v1", "llm_promotion": "3", "llm_sentiment": "2"}
    assert all(model.features(SNAP, EPISODE, None, old)[k] is None for k in model.GROUPS["llm"])  # another version


def test_technical_features_join_by_snapshot_and_version():
    row = {"technical_version": technical.TECHNICAL_VERSION, "vwap_ext": "0.3", "ssr_today": "1", "ret_60m": ""}
    f = model.features(SNAP, EPISODE, None, None, row)
    assert f["vwap_ext"] == 0.3 and f["ssr_today"] == 1 and f["ret_60m"] is None
    assert model.features(SNAP, EPISODE, None, None, {**row, "technical_version": "technical-v0"})["vwap_ext"] is None
    assert "technical" in model.MARKET_GROUPS and set(model.GROUPS["technical"]) == set(technical.FEATURES)


def test_ticker_history_counts_only_what_was_known_at_the_flag(tmp_path):
    ds = make_datastore(tmp_path, weeks=6, per_day=1, now=START + 50 * DAY)
    eps = ds.read_csv("candidates/episodes.csv")
    snaps = ds.read_csv(SNAPSHOTS)
    labels = ds.read_csv(model.LABELS)
    # day 20's candidate is the same stock as day 0's and day 18's; day 0's crashed, day 18's did not
    first, second, third = eps[0], eps[18], eps[20]
    for e in (second, third):
        old = e["ticker"]
        e["ticker"] = first["ticker"]
        for r in snaps + labels:
            if r["episode_id"] == e["episode_id"] and r["ticker"] == old:
                r["ticker"] = first["ticker"]
    for r in labels:
        if r["ticker"] == first["ticker"]:
            r["crash_10"] = "1" if r["episode_id"] == first["episode_id"] else "0"
    ds.write_csv("candidates/episodes.csv", list(eps[0]), eps)
    ds.write_csv(SNAPSHOTS, list(snaps[0]), snaps)
    ds.write_csv(model.LABELS, list(labels[0]), labels)
    rows = {r.episode_id: r for r in model.load_rows(ds) if r.role == "candidate"}
    a, b, c = rows[first["episode_id"]], rows[second["episode_id"]], rows[third["episode_id"]]
    assert (a.x["prior_flags_90d"], a.x["days_since_prior_flag"], a.x["prior_crashes"]) == (0, None, 0)
    assert b.x["prior_flags_90d"] == 1 and b.x["days_since_prior_flag"] == pytest.approx((b.as_of - a.as_of) / DAY)
    assert a.avail["crash"] < b.as_of and b.x["prior_crashes"] == 1  # day 0's crash had settled by day 18
    assert c.x["prior_flags_90d"] == 2 and c.x["days_since_prior_flag"] == pytest.approx((c.as_of - b.as_of) / DAY)
    assert c.x["prior_crashes"] == 1  # day 18's label was not available yet, and it did not crash anyway
    control = next(r for r in model.load_rows(ds) if r.role == "control")
    assert control.x["prior_flags_90d"] == 0 and control.x["days_since_prior_flag"] is None


def test_recency_weight_halves_every_eight_weeks():
    assert model.recency_weight(0) == 1
    assert model.recency_weight(56 * DAY) == pytest.approx(0.5)
    assert model.recency_weight(112 * DAY) == pytest.approx(0.25)


def test_a_week_model_learns_only_from_labels_available_before_the_week(tmp_path):
    ds = make_datastore(tmp_path, weeks=8, now=START + 70 * DAY)
    rows = model.load_rows(ds)
    cutoff = START + 5 * 7 * DAY
    m = model.fit(rows, "crash", cutoff, model.FEATURES)
    used = [r for r in rows if r.y["crash"] is not None and r.avail["crash"] < cutoff]
    assert isinstance(m, model.Fitted) and m.n == len(used) and m.pos == sum(r.y["crash"] for r in used)
    assert all(r.as_of < cutoff - 11 * DAY for r in used)  # session 10's close is at least 11 days after a flag
    assert any(r.y["crash"] is not None and r.avail["crash"] >= cutoff for r in rows)  # settled later: left out
    cands = [r for r in used if r.role == "candidate"]
    w = [model.recency_weight(cutoff - r.as_of) for r in cands]
    base = sum(wi * r.y["crash"] for wi, r in zip(w, cands)) / sum(w)
    assert m.threshold == pytest.approx(model.LIFT * max(base, model.MIN_BASE_RATE))


def test_no_model_until_enough_labels_are_available(tmp_path):
    ds = make_datastore(tmp_path, weeks=3, now=START + 30 * DAY)
    res = model.fit(model.load_rows(ds), "crash", START + 14 * DAY, model.FEATURES)
    assert isinstance(res, model.NoModel) and (res.n < model.MIN_ROWS or res.pos < model.MIN_POS)


def test_the_model_finds_the_planted_pattern(tmp_path):
    ds = make_datastore(tmp_path, weeks=11, per_day=4, now=START + 95 * DAY)
    rows = model.load_rows(ds)
    items = []
    for week in (START + 8 * 7 * DAY, START + 9 * 7 * DAY, START + 10 * 7 * DAY):
        m = model.fit(rows, "crash", week, model.FEATURES)
        test = [r for r in rows if r.role == "candidate" and r.week == week and r.y["crash"] is not None]
        items += [(r.y["crash"], s, s >= m.threshold) for r, s in zip(test, m.predict(test))]
    met = model.metrics(items)
    assert met["positives"] >= 10
    assert met["auc"] > 0.8 and met["ap"] > 2 * met["base_rate"] and met["precision"] > 2 * met["base_rate"]


def test_metrics_on_a_hand_checked_example():
    items = [(1, 0.9, True), (0, 0.8, True), (1, 0.7, True), (0, 0.3, False), (0, 0.2, False), (1, 0.1, False)]
    m = model.metrics(items)
    assert (m["n"], m["positives"], m["flagged"]) == (6, 3, 3)
    assert m["precision"] == pytest.approx(2 / 3) and m["recall"] == pytest.approx(2 / 3) and m["f1"] == pytest.approx(2 / 3)
    assert m["base_rate"] == 0.5 and m["lift"] == pytest.approx(4 / 3)
    assert m["ap"] == pytest.approx((1 + 2 / 3 + 1 / 2) / 3)
    assert m["auc"] == pytest.approx(5 / 9)
    ties = model.metrics([(1, 0.5, False), (0, 0.5, False)])
    assert ties["auc"] == 0.5 and ties["ap"] == 0.5 and ties["precision"] is None and ties["f1"] is None
    assert model.metrics([(0, 0.2, True)])["ap"] is None


def test_development_weeks_split_into_three_blocks():
    assert model.split_blocks([1, 2, 3, 4, 5, 6, 7]) == [[1, 2, 3], [4, 5], [6, 7]]
    assert model.split_blocks([1, 2, 3]) == [[1], [2], [3]]
    assert model.split_blocks([1, 2]) is None


def item(y, flagged, week, archetype="low_float_runner", ret10=None, controls=(0, 0), score=None):
    return {"y": y, "flagged": flagged, "score": score if score is not None else (0.9 if flagged else 0.1), "week": week,
            "archetype": archetype, "ret10": ret10 if ret10 is not None else (-0.5 if y else 0.05),
            "control_ys": list(controls)}


def good_items():
    out = []
    for week in (1, 2, 3):
        for i in range(12):
            y = int(i % 6 < 2)
            out.append(item(y, bool(y) or i % 6 == 2, week, "low_float_runner" if i < 6 else "otc_penny"))
    return out


def test_a_signal_that_holds_everywhere_is_robust():
    checks = model.robustness(good_items())
    assert [c["status"] for c in checks] == ["pass"] * 5
    assert model.is_robust(checks)


def test_a_signal_that_flags_the_wrong_candidates_fails():
    items = [{**it, "flagged": not it["flagged"]} for it in good_items()]
    checks = model.robustness(items)
    assert {c["check"]: c["status"] for c in checks}["beats the base rate"] == "fail"
    assert not model.is_robust(checks)


def test_too_few_labels_is_not_a_verdict():
    checks = model.robustness([item(1, True, 1), item(0, False, 1), item(1, False, 2)])
    assert [c["status"] for c in checks] == ["not enough data"] * 5
    assert not model.is_robust(checks)


def test_a_group_is_weak_when_leaving_it_out_never_lowers_ap():
    everything = (0.5, [0.4, 0.5, 0.6])
    without = {
        "chatter": (0.3, [0.2, 0.3, 0.4]),  # needed
        "text": (0.55, [0.5, 0.5, 0.5]),  # not lower pooled, nor in 2 of 3 blocks: weak
        "llm": (0.5, [0.3, 0.5, 0.5]),  # not lower pooled, but lower in 2 of 3 blocks: kept
        "price_volume": (0.45, [0.5, 0.6, 0.7]),  # lower pooled: kept
    }
    assert model.weak_groups(everything, without) == ["text"]
    assert model.weak_groups(everything, {g: (0.6, [0.6, 0.6, 0.6]) for g in model.GROUPS}) == []  # never all


def test_run_scores_every_candidate_once_and_keeps_the_holdout_locked(tmp_path):
    now = HOLDOUT + 20 * DAY
    ds = make_datastore(tmp_path, weeks=15, now=now)  # flags up to 2027-01-17: two hold-out weeks
    summary = model.run_model(ds, clock=lambda: now)
    preds = ds.read_csv(model.PREDICTIONS)
    cands = [r for r in ds.read_csv(SNAPSHOTS) if r["role"] == "candidate"]
    assert sorted((p["snapshot_id"], p["target"]) for p in preds) == sorted(
        (c["snapshot_id"], t) for c in cands for t in model.TARGETS)
    hold = [p for p in preds if p["holdout"] == "1"]
    assert hold and all(p["score"] != "" for p in hold if p["target"] == "crash")  # scored prospectively
    early = [p for p in preds if p["week_utc"] < "2026-10-19"]
    assert early and all(p["score"] == "" and "no model" in p["note"] for p in early)
    assert all(p["model_version"] == model.MODEL_VERSION for p in preds)

    wf = ds.read_csv(model.WALKFORWARD)
    assert wf and all(r["as_of_utc"] < "2027-01-04" for r in wf)  # the replay never touches hold-out flags
    readme = ds.path(model.README).read_text()
    assert "locked" in readme and "Development walk-forward" in readme
    assert not ds.path(model.HOLDOUT_MD).exists() and summary["finished"] is False
    assert summary["holdout"] == "locked"

    model.run_model(ds, clock=lambda: now + DAY)
    assert ds.read_csv(model.PREDICTIONS) == preds  # nothing re-scored, nothing rewritten


def test_a_score_uses_its_week_model(tmp_path):
    now = START + 70 * DAY
    ds = make_datastore(tmp_path, weeks=9, now=now)
    model.run_model(ds, clock=lambda: now)
    rows = {r.snapshot_id: r for r in model.load_rows(ds)}
    p = next(p for p in ds.read_csv(model.PREDICTIONS) if p["target"] == "crash" and p["score"])
    r = rows[p["snapshot_id"]]
    assert p["groups"] == " ".join(model.GROUPS)  # too few labels to prune anything yet
    m = model.fit(list(rows.values()), "crash", r.week, model.features_of(p["groups"].split()))
    assert int(p["n_train"]) == m.n and float(p["score"]) == pytest.approx(m.predict([r])[0], abs=1e-6)
    assert p["flagged"] == str(int(m.predict([r])[0] >= m.threshold))


def test_the_holdout_waits_for_its_last_labels(tmp_path):
    now = HOLDOUT + 18 * DAY
    ds = make_datastore(tmp_path, weeks=15, now=now, live_since=START - 100 * DAY)  # collection over
    summary = model.run_model(ds, clock=lambda: now)
    assert summary["holdout"] == "locked" and summary["finished"] is False
    assert not ds.path(model.HOLDOUT_MD).exists()


def test_the_holdout_is_evaluated_once_after_collection_ends(tmp_path):
    now = HOLDOUT + 40 * DAY  # every hold-out label has settled
    ds = make_datastore(tmp_path, weeks=15, now=now, live_since=START - 100 * DAY)
    summary = model.run_model(ds, clock=lambda: now)
    assert summary["holdout"] == "evaluated" and summary["finished"] is True
    report = ds.path(model.HOLDOUT_MD).read_text()
    assert "crash" in report and "precision" in report.lower()
    rows = ds.read_csv(model.HOLDOUT_CSV)
    assert rows and all(r["as_of_utc"] >= "2027-01-04" for r in rows)
    ds.path(model.HOLDOUT_MD).write_text("sealed")
    summary = model.run_model(ds, clock=lambda: now + DAY)
    assert ds.path(model.HOLDOUT_MD).read_text() == "sealed" and summary["finished"] is True


def test_a_snapshot_stage_4_never_labeled_holds_the_holdout_only_for_a_while(tmp_path):
    now = HOLDOUT + 40 * DAY
    ds = make_datastore(tmp_path, weeks=15, now=now, live_since=START - 100 * DAY)
    labels = ds.read_csv(model.LABELS)
    gone = next(r["snapshot_id"] for r in labels if r["as_of_utc"] >= "2027-01-10")
    ds.write_csv(model.LABELS, list(labels[0]), [r for r in labels if r["snapshot_id"] != gone])
    assert model.run_model(ds, clock=lambda: now)["holdout"] == "locked"  # its label may still come
    last_flag = max(float(r["as_of"]) for r in ds.read_csv(SNAPSHOTS))
    later = last_flag + model.HOLDOUT_GRACE + DAY
    assert model.run_model(ds, clock=lambda: later)["holdout"] == "evaluated"


class FakeLLM:
    model = "fake/model"

    def __init__(self, *replies):
        self.replies = list(replies)
        self.prompts = []

    def complete(self, system, user, schema=None):
        self.prompts.append(user)
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        return reply


RATING = ('{"summary": "Hype and earnings.", "labels": {"1": "pitch", "2": "event"}, '
          '"event_type": "earnings", "event_quote": "earnings were announced", "sentiment": 1}')


def raw_doc(id_, created, collected, body, author="alice", kind="comment"):
    return {"id": id_, "kind": kind, "subreddit": "pennystocks", "author": author, "created_utc": created,
            "collected_at": collected, "source": "arctic_shift", "title": None, "body": body, "url": None,
            "permalink": f"/r/pennystocks/{id_}", "run_id": "r", "fetch_mode": "live"}


def chatter(ds, as_of, ticker):
    ds.write_raw([raw_doc(f"t1_{ticker}a", as_of - 3000, as_of - 2900, f"${ticker} to the moon, get in now", "a"),
                  raw_doc(f"t1_{ticker}b", as_of - 2000, as_of - 1900, f"${ticker} earnings were announced", "b")],
                 run_started=as_of - 1900, run_id="1")


def test_text_features_and_llm_ratings_come_from_the_flag_documents(tmp_path):
    now = START + 2 * DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)  # candidates AAAA (Monday) and AAAB (Tuesday)
    eps = {e["ticker"]: e for e in ds.read_csv("candidates/episodes.csv")}
    chatter(ds, float(eps["AAAA"]["first_flagged_at"]), "AAAA")
    llm = FakeLLM(RATING)
    summary = model.run_model(ds, llm=llm, clock=lambda: now)

    rows = {r["ticker"]: r for r in ds.read_csv(text.TEXT)}
    assert rows["AAAA"]["n_docs"] == "2" and rows["AAAA"]["promo_share"] == "0.5" and rows["AAAA"]["news_share"] == "0.5"
    assert rows["AAAB"]["n_docs"] == "0" and rows["AAAB"]["promo_share"] == ""
    assert len(llm.prompts) == 1 and "$AAAA to the moon" in llm.prompts[0]  # nothing to rate for AAAB
    ratings = {r["ticker"]: r for r in ds.read_csv(text.LLM)}
    assert ratings["AAAA"]["status"] == "ok" and ratings["AAAA"]["llm_pitch_share"] == "0.5"
    assert ratings["AAAA"]["llm_event_share"] == "0.5" and ratings["AAAA"]["llm_checks"].startswith("quote=ok")
    assert ratings["AAAA"]["model"] == "fake/model" and ratings["AAAA"]["llm_version"] == "llm-v2"
    assert ratings["AAAB"]["status"] == "no_documents"
    assert summary["text"] == 2 and summary["llm"]["ok"] == 1
    report = ds.path(model.README).read_text()
    assert "| 100% / 50% / 0% / 50% | Hype and earnings. |" in report and "| no documents |" in report

    model.run_model(ds, llm=FakeLLM(), clock=lambda: now + 3600)  # computed once: no new rows, no calls
    assert len(ds.read_csv(text.TEXT)) == 2 and len(ds.read_csv(text.LLM)) == 2


def test_older_versions_are_redone_while_their_documents_are_checked_out(tmp_path):
    now = START + 6 * DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)  # AAAA flagged on Monday, rated by llm-v1 then
    e = ds.read_csv("candidates/episodes.csv")[0]
    chatter(ds, float(e["first_flagged_at"]), "AAAA")
    v1_text = ["episode_id", "ticker", "as_of_utc", "n_docs", *text.TEXT_FEATURES[:-1], "computed_at_utc", "text_version"]
    v1_llm = text.LLM_FIELDS[:text.LLM_FIELDS.index("llm_version") + 1]
    key = {"episode_id": e["episode_id"], "ticker": "AAAA", "as_of_utc": e["first_flagged_at_utc"]}
    ds.write_csv(text.TEXT, v1_text, [{**key, "n_docs": 2, "dup_share": 0, "text_version": "text-v1"}])
    ds.write_csv(text.LLM, v1_llm, [{**key, "status": "ok", "llm_promotion": 3, "llm_version": "llm-v1"}])
    # its raw files are no longer checked out: the old rows stay, nothing is given up
    def of_aaaa(rel):
        return [r for r in ds.read_csv(rel) if r["ticker"] == "AAAA"]

    model.run_model(ds, llm=FakeLLM(), clock=lambda: now, raw_since=datetime.fromtimestamp(now, timezone.utc).date())
    assert [r["llm_version"] for r in of_aaaa(text.LLM)] == ["llm-v1"]
    # checked out again: redone with the current versions, the old rows kept
    llm = FakeLLM(RATING)
    model.run_model(ds, llm=llm, clock=lambda: now, raw_since=datetime.fromtimestamp(START - DAY, timezone.utc).date())
    old, new = of_aaaa(text.LLM)
    assert old["llm_promotion"] == "3" and old["llm_pitch_share"] == ""
    assert new["llm_version"] == "llm-v2" and new["llm_pitch_share"] == "0.5" and len(llm.prompts) == 1
    texts = of_aaaa(text.TEXT)
    assert [t["text_version"] for t in texts] == ["text-v1", "text-v2"] and texts[1]["near_dup_share"] == "0.0"
    row = next(r for r in model.load_rows(ds) if r.ticker == "AAAA")
    assert row.x["llm_pitch_share"] == 0.5 and row.x["near_dup_share"] == 0.0


def test_text_waits_until_the_raw_files_it_needs_are_checked_out(tmp_path):
    now = START + 2 * DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)
    # only today's raw files are checked out: Monday's candidate needs Sunday's and Monday's
    model.run_model(ds, clock=lambda: now, raw_since=datetime.fromtimestamp(now, timezone.utc).date())
    assert {r["ticker"] for r in ds.read_csv(text.TEXT)} == set()
    model.run_model(ds, clock=lambda: now, raw_since=datetime.fromtimestamp(START - DAY, timezone.utc).date())
    assert {r["ticker"] for r in ds.read_csv(text.TEXT)} == {"AAAA", "AAAB"}


def test_scoring_waits_while_a_failed_rating_is_retried(tmp_path):
    now = START + DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)  # AAAA only
    as_of = float(ds.read_csv("candidates/episodes.csv")[0]["first_flagged_at"])
    chatter(ds, as_of, "AAAA")
    model.run_model(ds, llm=FakeLLM(text.LLMError("HTTP 429: busy")), clock=lambda: now)
    assert ds.read_csv(text.LLM) == [] and ds.read_csv(model.PREDICTIONS) == []
    model.run_model(ds, llm=FakeLLM(RATING), clock=lambda: now + DAY)
    assert ds.read_csv(text.LLM)[0]["status"] == "ok" and len(ds.read_csv(model.PREDICTIONS)) == 2


def test_a_rating_that_keeps_failing_is_given_up_after_three_days(tmp_path):
    now = START + DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)
    as_of = float(ds.read_csv("candidates/episodes.csv")[0]["first_flagged_at"])
    chatter(ds, as_of, "AAAA")
    model.run_model(ds, llm=FakeLLM(text.LLMError("HTTP 500")), clock=lambda: now)
    model.run_model(ds, llm=FakeLLM(text.LLMError("HTTP 500")), clock=lambda: as_of + 3 * DAY + 60)
    (row,) = ds.read_csv(text.LLM)
    assert row["status"] == "failed" and "HTTP 500" in row["error"] and row["llm_pitch_share"] == ""
    assert len(ds.read_csv(model.PREDICTIONS)) == 2


def test_a_refused_prompt_is_recorded_at_once(tmp_path):
    now = START + DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)
    chatter(ds, float(ds.read_csv("candidates/episodes.csv")[0]["first_flagged_at"]), "AAAA")
    model.run_model(ds, llm=FakeLLM(text.LLMRefused("HTTP 400: content_filter")), clock=lambda: now)
    (row,) = ds.read_csv(text.LLM)
    assert row["status"] == "failed" and "content_filter" in row["error"]


def test_an_unparseable_rating_is_recorded_at_once(tmp_path):
    now = START + DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=1, now=now)
    chatter(ds, float(ds.read_csv("candidates/episodes.csv")[0]["first_flagged_at"]), "AAAA")
    model.run_model(ds, llm=FakeLLM("I can't rate this."), clock=lambda: now)
    (row,) = ds.read_csv(text.LLM)
    assert row["status"] == "failed" and "unparseable" in row["error"]
    assert len(ds.read_csv(model.PREDICTIONS)) == 2  # scored without the rating


def test_llm_calls_stop_when_the_time_budget_is_spent(tmp_path):
    now = START + DAY
    ds = make_datastore(tmp_path, weeks=1, per_day=3, now=now)  # three Monday candidates
    for e in ds.read_csv("candidates/episodes.csv"):
        chatter(ds, float(e["first_flagged_at"]), e["ticker"])
    t = [0.0]

    class SlowLLM(FakeLLM):
        def complete(self, system, user, schema=None):
            t[0] += 30 * 60  # half an hour per rating
            return super().complete(system, user, schema)

    llm = SlowLLM(RATING, RATING, RATING)
    summary = model.run_model(ds, llm=llm, clock=lambda: now, llm_budget_s=35 * 60, timer=lambda: t[0])
    assert len(llm.prompts) == 2 and summary["llm"]["ok"] == 2 and summary["llm"]["waiting"] == 1
    assert len(ds.read_csv(model.PREDICTIONS)) == 4  # the third waits for its rating
    model.run_model(ds, llm=FakeLLM(RATING), clock=lambda: now + 3600)
    assert len(ds.read_csv(text.LLM)) == 3 and len(ds.read_csv(model.PREDICTIONS)) == 6


def test_cli_model_command_and_build_db(tmp_path, monkeypatch):
    now_ds = tmp_path / "ds"
    ds = make_datastore(now_ds, weeks=1, per_day=1, now=START + 2 * DAY)
    monkeypatch.setattr(cli.time, "time", lambda: START + 2 * DAY)
    assert cli.main(["model", "--datastore", str(now_ds), "--no-llm", "--summary", str(tmp_path / "s.md"),
                     "--github-output", str(tmp_path / "out.txt")]) == 0
    assert "finished=false" in (tmp_path / "out.txt").read_text()
    assert "Model run" in (tmp_path / "s.md").read_text()
    assert ds.path(model.README).exists()
    assert cli.main(["build-db", "--datastore", str(now_ds), "--out", str(tmp_path / "db.sqlite")]) == 0
    import sqlite3

    conn = sqlite3.connect(tmp_path / "db.sqlite")
    assert conn.execute("select count(*) from model_predictions").fetchone()[0] == 4
    assert conn.execute("select count(*) from model_text").fetchone()[0] == 2


def test_cli_llm_probe_saves_nothing(tmp_path, monkeypatch, capsys):
    made = []

    class Client:
        def __init__(self, url, model):
            made.append((url, model))
            self.model = model

        def complete(self, system, user, schema=None):
            return RATING

    monkeypatch.setattr(cli, "ChatClient", Client)
    assert cli.main(["model", "--datastore", str(tmp_path), "--llm-probe", "--llm-url", "http://127.0.0.1:9/x",
                     "--llm-model", "some/model"]) == 0
    assert made == [("http://127.0.0.1:9/x", "some/model")] and "llm_pitch_share" in capsys.readouterr().out
    assert not any(tmp_path.iterdir())

    class Broken(Client):
        def complete(self, system, user, schema=None):
            raise text.LLMError("network: connection refused")

    monkeypatch.setattr(cli, "ChatClient", Broken)
    assert cli.main(["model", "--datastore", str(tmp_path), "--llm-probe"]) == 1
    assert "connection refused" in capsys.readouterr().out


def test_cli_llm_eval_scores_the_labels_and_saves_nothing(tmp_path, monkeypatch, capsys):
    now = START + 2 * DAY
    ds = make_datastore(tmp_path / "ds", weeks=1, per_day=1, now=now)
    eps = {e["ticker"]: e for e in ds.read_csv("candidates/episodes.csv")}
    chatter(ds, float(eps["AAAA"]["first_flagged_at"]), "AAAA")
    before = sorted(p.relative_to(tmp_path) for p in (tmp_path / "ds").rglob("*"))
    gold = {eps["AAAA"]["episode_id"]: {"pitch": {"yes": ["t1_AAAAa"], "maybe": []},
                                        "event": {"yes": [], "maybe": []},
                                        "not_about": {"yes": [], "maybe": ["t1_AAAAb"]},
                                        "warning": {"yes": ["t1_AAAAb"], "maybe": []}}}
    (tmp_path / "gold.json").write_text(json.dumps(gold))

    class Client(FakeLLM):
        def __init__(self, url, model):
            super().__init__(RATING)
            self.model = model

    monkeypatch.setattr(cli, "ChatClient", Client)
    monkeypatch.setattr(cli.time, "time", lambda: now)
    assert cli.main(["model", "--datastore", str(tmp_path / "ds"), "--llm-eval", str(tmp_path / "eval.csv"),
                     "--gold", str(tmp_path / "gold.json"), "--llm-model", "some/model"]) == 0
    out = capsys.readouterr().out
    assert "pitch: 1 right, 0 wrong, 0 missed" in out and "event: 0 right, 1 wrong, 0 missed" in out
    assert "warning: 0 right, 0 wrong, 1 missed" in out and "quotes: 1 found, 0 not found" in out
    assert "AAAA: warning missed [2]; event wrong [2]" in out  # by document number, for reading the log
    (row,) = list(csv.DictReader(open(tmp_path / "eval.csv")))
    assert row["ticker"] == "AAAA" and row["llm_pitch_share"] == "0.5" and json.loads(row["doc_ids"]) == [
        "t1_AAAAa", "t1_AAAAb"] and row["model"] == "some/model"
    assert sorted(p.relative_to(tmp_path) for p in (tmp_path / "ds").rglob("*")) == before


def test_llm_eval_scores_only_labelled_documents_still_shown(tmp_path):
    now = START + 2 * DAY
    ds = make_datastore(tmp_path / "ds", weeks=1, per_day=1, now=now)
    eps = {e["ticker"]: e for e in ds.read_csv("candidates/episodes.csv")}
    chatter(ds, float(eps["AAAA"]["first_flagged_at"]), "AAAA")
    # labelled when only t1_AAAAa and t1_gone were shown: t1_AAAAb (the model's event) wasn't labelled, and t1_gone
    # (a pitch the model can't see any more) is not a miss
    gold = {eps["AAAA"]["episode_id"]: {"docs": ["t1_AAAAa", "t1_gone"],
                                        "pitch": {"yes": ["t1_AAAAa", "t1_gone"], "maybe": []},
                                        "event": {"yes": [], "maybe": []},
                                        "not_about": {"yes": [], "maybe": []}, "warning": {"yes": [], "maybe": []}}}
    _, lines = model.evaluate_llm(ds, FakeLLM(RATING), None, gold)
    assert "pitch: 1 right, 0 wrong, 0 missed" in lines and "event: 0 right, 0 wrong, 0 missed" in lines
    assert "1 hand-labelled documents shown" in lines


def test_letters_are_valid_cashtags():
    assert letters(0) == "AAAA" and letters(27) == "AABB"
