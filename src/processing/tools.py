"""Built-in tools available to enrichment blocks."""

import asyncio
from dataclasses import dataclass
import logging
import re
from typing import Any
from urllib.parse import urlparse

import httpx
from ddgs import DDGS

logger = logging.getLogger(__name__)

ARTICLE_HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/135.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,*/*",
    "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
}
MAX_EXTRACTED_CHARS = 3500


@dataclass(frozen=True)
class ToolResult:
    request_id: str
    block_id: str
    tool: str
    results: list[dict[str, str]]


def _clean_text(value: str) -> str:
    value = re.sub(r"\s+", " ", value or "").strip()
    return value


def _article_excerpt(url: str) -> str:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return ""
    try:
        import trafilatura
    except ImportError:
        return ""
    try:
        with httpx.Client(timeout=12, follow_redirects=True, headers=ARTICLE_HEADERS) as client:
            response = client.get(url)
            response.raise_for_status()
        extracted = trafilatura.extract(response.text, favor_recall=True) or ""
        extracted = _clean_text(extracted)
        return extracted[:MAX_EXTRACTED_CHARS]
    except Exception as exc:
        logger.debug("Could not extract article text for %s: %s", url, exc)
        return ""


class WebSearchTool:
    name = "web_search"

    async def execute(self, arguments: dict[str, Any]) -> list[dict[str, str]]:
        query = arguments.get("query")
        if not isinstance(query, str) or not query.strip():
            raise ValueError("web_search requires a non-empty query")
        try:
            raw = await asyncio.to_thread(DDGS().text, query.strip(), max_results=3)
        except Exception as exc:
            logger.warning("web_search failed for %r: %s", query, exc)
            return []

        results: list[dict[str, str]] = []
        for result in raw or []:
            href = str(result.get("href", ""))
            if not href:
                continue
            body = _clean_text(str(result.get("body", "")))
            excerpt = await asyncio.to_thread(_article_excerpt, href)
            text = body
            if excerpt and excerpt not in body:
                text = (body + "\n\nArticle excerpt: " + excerpt).strip()
            results.append(
                {
                    "title": str(result.get("title", "")),
                    "url": href,
                    "text": text,
                }
            )
        return results


class ToolRegistry:
    """Small allowlisted registry for executable profile tools."""

    def __init__(self):
        self._tools = {WebSearchTool.name: WebSearchTool()}

    @property
    def names(self) -> set[str]:
        return set(self._tools)

    async def execute(
        self,
        request_id: str,
        block_id: str,
        tool: str,
        arguments: dict[str, Any],
    ) -> ToolResult:
        try:
            implementation = self._tools[tool]
        except KeyError as exc:
            raise ValueError(f"Unknown enrichment tool: {tool}") from exc
        return ToolResult(
            request_id=request_id,
            block_id=block_id,
            tool=tool,
            results=await implementation.execute(arguments),
        )

