"""Polite HTTP for the Stage 2 market sources.

One client for Yahoo, SEC, FINRA and Nasdaq: requests to the same host are
spaced out, and network errors, 429s and 5xx answers are retried with backoff.
A host that still fails twice in a row is skipped for the rest of the run, so a
hanging source can't stretch a run past its time limit. Anything else is
returned as (status, text) for the caller to interpret.
"""

from __future__ import annotations

import time
from typing import Any, Callable
from urllib.parse import urlparse

import requests

# Yahoo and Nasdaq answer browsers, not scripts (checked from GitHub's runners, 2026-10-05)
BROWSER_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
)

Request = Callable[..., tuple[int, str]]


def requests_request() -> Request:
    session = requests.Session()  # keeps cookies (Yahoo's crumb needs its cookie)

    def request(method: str, url: str, params=None, headers=None, json=None, timeout: float = 30) -> tuple[int, str]:
        try:
            resp = session.request(method, url, params=params, headers=headers, json=json, timeout=timeout)
        except requests.RequestException as exc:
            return 0, f"{type(exc).__name__}: {exc}"
        return resp.status_code, resp.text

    return request


class Web:
    def __init__(
        self,
        request: Request | None = None,
        sleep: Callable[[float], None] = time.sleep,
        clock: Callable[[], float] = time.time,
        min_interval: float = 0.5,
        max_retries: int = 3,
        give_up_after: int = 2,
    ) -> None:
        self.request = request or requests_request()
        self.sleep = sleep
        self.clock = clock
        self.min_interval = min_interval
        self.max_retries = max_retries
        self.give_up_after = give_up_after
        self._last: dict[str, float] = {}
        self._failures: dict[str, int] = {}  # consecutive failed fetches per host

    def fetch(
        self, url: str, *, params: dict | None = None, headers: dict | None = None, json_body: Any = None, method: str = "GET"
    ) -> tuple[int, str]:
        host = urlparse(url).hostname or ""
        if self._failures.get(host, 0) >= self.give_up_after:
            return 0, f"skipped: {host} failed {self._failures[host]} times in a row this run"
        attempt = 0
        while True:
            last = self._last.get(host)
            if last is not None and last + self.min_interval > self.clock():
                self.sleep(last + self.min_interval - self.clock())
            self._last[host] = self.clock()
            status, text = self.request(method, url, params=params, headers=headers, json=json_body, timeout=30)
            failed = status == 0 or status == 429 or status >= 500
            if failed and attempt < self.max_retries:
                self.sleep(min(30.0, 2.0 * 2**attempt))
                attempt += 1
                continue
            self._failures[host] = self._failures.get(host, 0) + 1 if failed else 0
            return status, text


def short_text(text: str, limit: int = 160) -> str:
    """First words of a response body, for error messages."""
    return " ".join(str(text).split())[:limit]
