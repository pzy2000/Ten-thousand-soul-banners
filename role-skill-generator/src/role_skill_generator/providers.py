from __future__ import annotations

import html
import json
import os
import re
import ssl
import threading
import time
from dataclasses import dataclass
from typing import Any
from urllib.error import HTTPError as UrllibHTTPError
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


_DEFAULT_HTTP_TIMEOUT = 30.0
_LLM_CHAT_TIMEOUT_DEFAULT = 600.0
_RESEARCH_WAIT_HEARTBEAT_SEC = 5.0


def _urlopen_ssl_context() -> ssl.SSLContext | None:
    """Optional TLS relax for sources with legacy chains (e.g. missing SKI). Set ROLE_SKILL_FETCH_INSECURE_SSL=1."""
    raw = os.getenv("ROLE_SKILL_FETCH_INSECURE_SSL", "").strip().lower()
    if raw in ("1", "true", "yes", "on"):
        return ssl._create_unverified_context()
    return None


def _llm_chat_timeout_seconds() -> float:
    raw = os.getenv("ROLE_SKILL_OPENAI_TIMEOUT")
    if raw is None or str(raw).strip() == "":
        return _LLM_CHAT_TIMEOUT_DEFAULT
    try:
        return float(raw)
    except ValueError as exc:
        raise HTTPError(
            f"ROLE_SKILL_OPENAI_TIMEOUT 必须是数字（秒），当前为 {raw!r}。"
        ) from exc


def _request_json(
    url: str,
    *,
    method: str = "GET",
    headers: dict[str, str] | None = None,
    payload: dict[str, Any] | None = None,
    timeout: float = _DEFAULT_HTTP_TIMEOUT,
    research_wait_progress: bool = False,
) -> dict[str, Any]:
    request_headers = {"User-Agent": USER_AGENT, **(headers or {})}
    data = None
    if payload is not None:
        data = json.dumps(payload).encode("utf-8")
        request_headers["Content-Type"] = "application/json"
    request = Request(url, method=method, headers=request_headers, data=data)
    done = threading.Event()

    def _heartbeat() -> None:
        start = time.monotonic()
        while not done.wait(_RESEARCH_WAIT_HEARTBEAT_SEC):
            elapsed = int(time.monotonic() - start)
            print(f"Already researched for {elapsed} seconds...", flush=True)

    thread: threading.Thread | None = None
    if research_wait_progress:
        thread = threading.Thread(target=_heartbeat, daemon=True)
        thread.start()
    try:
        try:
            with urlopen(request, timeout=timeout) as response:
                body = response.read().decode("utf-8")
        except TimeoutError as exc:
            raise HTTPError(f"请求在 {timeout:g} 秒内未完成: {url}") from exc
        except UrllibHTTPError as exc:
            detail = exc.read().decode("utf-8", errors="replace").strip() or "(empty body)"
            if len(detail) > 8000:
                detail = f"{detail[:8000]}…"
            raise HTTPError(
                f"请求 {url} 失败: HTTP {exc.code} {exc.reason}。服务端响应: {detail}"
            ) from exc
        return json.loads(body)
    finally:
        done.set()
        if thread is not None:
            thread.join(timeout=1.0)


def _request_text(
    url: str,
    *,
    headers: dict[str, str] | None = None,
) -> str:
    request_headers = {"User-Agent": USER_AGENT, **(headers or {})}
    request = Request(url, headers=request_headers)
    open_kw: dict[str, Any] = {"timeout": 30}
    ctx = _urlopen_ssl_context()
    if ctx is not None:
        open_kw["context"] = ctx
    with urlopen(request, **open_kw) as response:
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
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "response_format": {"type": "json_object"},
        }
        temp_raw = os.getenv("ROLE_SKILL_OPENAI_TEMPERATURE")
        if temp_raw is not None and str(temp_raw).strip() != "":
            try:
                payload["temperature"] = float(temp_raw)
            except ValueError as exc:
                raise HTTPError(
                    f"ROLE_SKILL_OPENAI_TEMPERATURE 必须是数字，当前为 {temp_raw!r}。"
                ) from exc

        data = _request_json(
            f"{self.base_url}/chat/completions",
            method="POST",
            headers={"Authorization": f"Bearer {self.api_key}"},
            payload=payload,
            timeout=_llm_chat_timeout_seconds(),
            research_wait_progress=True,
        )
        if isinstance(data, dict) and data.get("success") is False:
            raise HTTPError(f"聊天接口返回错误: {data}")
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
