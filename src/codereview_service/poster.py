from __future__ import annotations

import json
import logging
import urllib.error
import urllib.request
from typing import Any

LOGGER = logging.getLogger(__name__)


class ResultPoster:
    def __init__(self, url: str, timeout_seconds: int):
        self.url = url
        self.timeout_seconds = timeout_seconds

    def post(self, payload: dict[str, Any]) -> None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        request = urllib.request.Request(
            self.url,
            data=data,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
                body = response.read().decode("utf-8", errors="replace")
                if response.status >= 300:
                    raise RuntimeError(f"API returned HTTP {response.status}: {body}")
                LOGGER.info("Posted review result to %s, status=%s", self.url, response.status)
        except urllib.error.URLError as exc:
            raise RuntimeError(f"Failed to post review result to {self.url}: {exc}") from exc

