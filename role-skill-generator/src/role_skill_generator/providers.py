from __future__ import annotations

import html
import json
import os
import re
from dataclasses import dataclass
from typing import Any
from urllib.parse import parse_qs, quote_plus, unquote, urlparse
from urllib.request import Request, urlopen


USER_AGENT = "role-skill-generator/0.1 (+https://github.com/pzy2000/SoulBanner)"


@dataclass
class SearchResult:
    query: str
    title: str
    url: str
    snippet: str
    provider: str


class HTTPError(RuntimeError):
    pass


def _request_json(
    url: str,
    *,
    method: str = "GET",
    headers: dict[str, str] | None = None,
    payload: dict[str, Any] | None = None,
) -> dict[str, Any]:
    request_headers = {"User-Agent": USER_AGENT, **(headers or {})}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json"
    request = Request(url, method=method, headers=request_headers, data=data)
    with urlopen(request, timeout=30) as response:
        body = response.read().decode("utf-8")
    return json.loads(body)


def _request_text(
    url: str,
    *,
    headers: dict[str, str] | None = None,
) -> str:
    request_headers = {"User-Agent": USER_AGENT, **(headers or {})}
    request = Request(url, headers=request_headers)
    with urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, errors="ignore")


class DuckDuckGoHtmlSearchProvider:
    name = "duckduckgo-html"

    def search(self, query: str, max_results: int = 5) -> list[SearchResult]:
        url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
        html_body = _request_text(url)
        pattern = re.compile(
            r'<a[^>]*class="result__a"[^>]*href="(?P<url>[^"]+)"[^>]*>(?P<title>.*?)</a>',
            re.IGNORECASE | re.DOTALL,
        )
        snippets = re.findall(
            r'<a[^>]*class="result__snippet"[^>]*>(.*?)</a>|<div[^>]*class="result__snippet"[^>]*>(.*?)</div>',
            html_body,
            re.IGNORECASE | re.DOTALL,
        )
        results: list[SearchResult] = []
        for index, match in enumerate(pattern.finditer(html_body)):
            raw_url = html.unescape(match.group("url"))
            parsed = urlparse(raw_url)
            if "duckduckgo.com" in parsed.netloc and parsed.path.startswith("/l/"):
                params = parse_qs(parsed.query)
                resolved = params.get("uddg", [raw_url])[0]
            else:
                resolved = raw_url
            snippet_tuple = snippets[index] if index < len(snippets) else ("", "")
            snippet = snippet_tuple[0] or snippet_tuple[1]
            title = _strip_html(match.group("title"))
            results.append(
                SearchResult(
                    query=query,
                    title=title,
                    url=unquote(resolved),
                    snippet=_strip_html(snippet),
                    provider=self.name,
                )
            )
            if len(results) >= max_results:
                break
        return results


class TavilySearchProvider:
    name = "tavily"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("TAVILY_API_KEY")
        if not self.api_key:
            raise HTTPError("缺少 TAVILY_API_KEY。")

    def search(self, query: str, max_results: int = 5) -> list[SearchResult]:
        data = _request_json(
            "https://api.tavily.com/search",
            method="POST",
            payload={
                "api_key": self.api_key,
                "query": query,
                "max_results": max_results,
                "search_depth": "basic",
            },
        )
        return [
            SearchResult(
                query=query,
                title=item.get("title", "").strip(),
                url=item.get("url", "").strip(),
                snippet=item.get("content", "").strip(),
                provider=self.name,
            )
            for item in data.get("results", [])
            if item.get("url")
        ]


class SerperSearchProvider:
    name = "serper"

    def __init__(self, api_key: str | None = None) -> None:
        self.api_key = api_key or os.getenv("SERPER_API_KEY")
        if not self.api_key:
            raise HTTPError("缺少 SERPER_API_KEY。")

    def search(self, query: str, max_results: int = 5) -> list[SearchResult]:
        data = _request_json(
            "https://google.serper.dev/search",
            method="POST",
            headers={"X-API-KEY": self.api_key},
            payload={"q": query, "num": max_results},
        )
        organic = data.get("organic", [])
        return [
            SearchResult(
                query=query,
                title=item.get("title", "").strip(),
                url=item.get("link", "").strip(),
                snippet=item.get("snippet", "").strip(),
                provider=self.name,
            )
            for item in organic
            if item.get("link")
        ]


def get_search_provider(name: str):
    lowered = name.lower()
    if lowered == DuckDuckGoHtmlSearchProvider.name:
        return DuckDuckGoHtmlSearchProvider()
    if lowered == TavilySearchProvider.name:
        return TavilySearchProvider()
    if lowered == SerperSearchProvider.name:
        return SerperSearchProvider()
    raise HTTPError(f"未知搜索 provider: {name}")


def fetch_document(url: str) -> dict[str, str]:
    text = _request_text(url, headers={"Accept": "text/html,application/xhtml+xml"})
    title_match = re.search(r"<title[^>]*>(.*?)</title>", text, re.IGNORECASE | re.DOTALL)
    title = _strip_html(title_match.group(1)) if title_match else url
    stripped = _strip_html_document(text)
    return {"url": url, "title": title, "content": stripped}


def _strip_html(value: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(value))).strip()


def _strip_html_document(value: str) -> str:
    without_scripts = re.sub(
        r"(?is)<(script|style|noscript).*?>.*?</\1>",
        " ",
        value,
    )
    flattened = re.sub(r"(?is)<br\s*/?>", "\n", without_scripts)
    text = _strip_html(flattened)
    return text[:24000]


class OpenAICompatibleClient:
    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | None = None,
        model: str | None = None,
    ) -> None:
        self.api_key = api_key or os.getenv("ROLE_SKILL_OPENAI_API_KEY") or os.getenv("OPENAI_API_KEY")
        self.base_url = (
            base_url
            or os.getenv("ROLE_SKILL_OPENAI_BASE_URL")
            or os.getenv("OPENAI_BASE_URL")
            or "https://api.openai.com/v1"
        ).rstrip("/")
        self.model = model or os.getenv("ROLE_SKILL_OPENAI_MODEL") or "gpt-4.1-mini"
        if not self.api_key:
            raise HTTPError("缺少 ROLE_SKILL_OPENAI_API_KEY 或 OPENAI_API_KEY。")

    def generate_json(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        data = _request_json(
            f"{self.base_url}/chat/completions",
            method="POST",
            headers={"Authorization": f"Bearer {self.api_key}"},
            payload={
                "model": self.model,
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
                "response_format": {"type": "json_object"},
            },
        )
        try:
            content = data["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as exc:
            raise HTTPError(f"模型响应结构异常: {data}") from exc
        return json.loads(_strip_code_fence(content))


def _strip_code_fence(content: str) -> str:
    trimmed = content.strip()
    if trimmed.startswith("```"):
        trimmed = re.sub(r"^```(?:json)?", "", trimmed).strip()
        trimmed = re.sub(r"```$", "", trimmed).strip()
    return trimmed
