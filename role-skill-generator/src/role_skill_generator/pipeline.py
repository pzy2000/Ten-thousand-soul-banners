from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from role_skill_generator.models import (
    load_json,
    normalize_persona_bundle,
    normalize_target_profile,
    write_json,
)
from role_skill_generator.providers import OpenAICompatibleClient, fetch_document, get_search_provider
from role_skill_generator.query_pack import build_query_pack, render_query_pack_markdown
from role_skill_generator.render import render_bundle_to_directory


def plan_queries(target_path: str | Path, output_markdown: str | Path | None = None) -> dict[str, Any]:
    target = normalize_target_profile(load_json(target_path))
    query_pack = build_query_pack(target)
    payload = {"target": target, "query_pack": query_pack}
    if output_markdown is not None:
        Path(output_markdown).write_text(
            render_query_pack_markdown(target, query_pack),
            encoding="utf-8",
        )
    return payload


def collect_sources(
    target_path: str | Path,
    run_dir: str | Path,
    *,
    provider_name: str = "duckduckgo-html",
    max_results: int = 5,
    max_documents: int = 12,
) -> dict[str, Any]:
    run_path = Path(run_dir)
    run_path.mkdir(parents=True, exist_ok=True)

    payload = plan_queries(target_path, run_path / "query-pack.md")
    target = payload["target"]
    query_pack = payload["query_pack"]
    write_json(run_path / "target.normalized.json", target)
    write_json(run_path / "query-pack.json", payload)

    provider = get_search_provider(provider_name)
    all_results: list[dict[str, Any]] = []
    seen_urls: set[str] = set()

    for group in query_pack:
        for query in group["queries"]:
            results = provider.search(query, max_results=max_results)
            for item in results:
                row = {
                    "group": group["name"],
                    "query": item.query,
                    "title": item.title,
                    "url": item.url,
                    "snippet": item.snippet,
                    "provider": item.provider,
                }
                all_results.append(row)
                seen_urls.add(item.url)

    _write_jsonl(run_path / "search_results.jsonl", all_results)

    documents: list[dict[str, Any]] = []
    for result in all_results:
        if len(documents) >= max_documents:
            break
        url = result["url"]
        if any(existing["url"] == url for existing in documents):
            continue
        try:
            document = fetch_document(url)
        except Exception as exc:  # noqa: BLE001
            document = {
                "url": url,
                "title": result["title"],
                "content": f"抓取失败：{exc}",
            }
        documents.append(
            {
                **document,
                "group": result["group"],
                "query": result["query"],
                "snippet": result["snippet"],
            }
        )

    _write_jsonl(run_path / "documents.jsonl", documents)
    return {
        "target": target,
        "query_pack": query_pack,
        "search_results": all_results,
        "documents": documents,
        "run_dir": str(run_path),
        "unique_urls": len(seen_urls),
    }


def synthesize_bundle(
    target_path: str | Path,
    documents_path: str | Path,
    output_bundle_path: str | Path,
    *,
    model: str | None = None,
) -> dict[str, Any]:
    target = normalize_target_profile(load_json(target_path))
    documents = _read_jsonl(documents_path)

    client = OpenAICompatibleClient(model=model)
    system_prompt = (
        "你是一个人物蒸馏编辑器。"
        "你的任务是把公开资料整理成 SoulBanner 仓库兼容的 persona bundle。"
        "你必须优先保守，不要编造事实，不要把出处不明的话当成稳定口头禅。"
        "输出必须是 JSON object，字段必须完整，值尽量用中文。"
    )
    user_prompt = _build_synthesis_prompt(target, documents)
    raw_bundle = client.generate_json(system_prompt, user_prompt)
    merged = {**target, **raw_bundle}
    normalized = normalize_persona_bundle(merged)
    write_json(output_bundle_path, normalized)
    return normalized


def render_bundle(
    bundle_path: str | Path,
    output_root: str | Path,
) -> Path:
    bundle = normalize_persona_bundle(load_json(bundle_path))
    return render_bundle_to_directory(bundle, output_root)


def generate_persona_materials(
    target_path: str | Path,
    run_dir: str | Path,
    output_root: str | Path,
    *,
    provider_name: str = "duckduckgo-html",
    max_results: int = 5,
    max_documents: int = 12,
    model: str | None = None,
) -> Path:
    collected = collect_sources(
        target_path,
        run_dir,
        provider_name=provider_name,
        max_results=max_results,
        max_documents=max_documents,
    )
    bundle_path = Path(run_dir) / "persona.bundle.json"
    synthesize_bundle(
        target_path,
        Path(run_dir) / "documents.jsonl",
        bundle_path,
        model=model,
    )
    return render_bundle(bundle_path, output_root)


def _write_jsonl(path: str | Path, rows: list[dict[str, Any]]) -> None:
    file_path = Path(path)
    file_path.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + ("\n" if rows else ""),
        encoding="utf-8",
    )


def _read_jsonl(path: str | Path) -> list[dict[str, Any]]:
    file_path = Path(path)
    rows: list[dict[str, Any]] = []
    for line in file_path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def _build_synthesis_prompt(target: dict[str, Any], documents: list[dict[str, Any]]) -> str:
    excerpted_docs = []
    for item in documents[:12]:
        excerpted_docs.append(
            {
                "group": item.get("group", ""),
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "snippet": item.get("snippet", ""),
                "content_excerpt": item.get("content", "")[:1800],
            }
        )

    schema_hint = {
        "description": "一句话说明这个 skill 蒸馏了什么",
        "who_is": "一句话说明人物身份、类型和为何值得蒸馏",
        "why_distilled": "解释其稳定人设、表达风格和梗点",
        "user_scenarios": ["适配场景1", "适配场景2", "适配场景3"],
        "style": {
            "tone": "语气",
            "rhythm": "节奏",
            "sentence_length": "句长偏好",
            "catchphrases": ["口头禅 1"],
            "signature_moves": ["标志性表达动作 1"],
        },
        "cognitive_frames": ["核心认知框架 1"],
        "decision_heuristics": ["决策启发式 1"],
        "expression_dna": {
            "opening": "开场方式",
            "transition": "转折方式",
            "pressure": "压人方式",
            "self_mockery": "自嘲方式",
            "questioning": "反问方式",
            "closing": "收尾方式",
        },
        "persona_tension": {
            "charm": "最迷人的地方",
            "criticism": "最招黑的地方",
            "exaggeration": "最容易被二创放大的点",
        },
        "boundaries": {
            "can_answer": ["能回答什么 1"],
            "cannot_answer": ["不能回答什么 1"],
            "weak_domains": ["素材不足领域 1"],
            "disclaimer": "这是基于公开素材蒸馏出的二创人格，不替代本人。",
        },
        "sample_dialogues": [{"user": "用户问题", "persona": "角色回答"}],
        "readme": {
            "intro": "README 一句话介绍",
            "why_worth": "为什么值得蒸馏",
            "distilled_points": ["蒸馏点 1"],
            "fit_questions": ["适合回答的问题 1"],
            "sample_questions": ["示例问题 1"],
            "about": "人物类型、收录理由与分类归属",
        },
        "research": {
            "writings": {
                "conclusions": ["文字蒸馏结论 1"],
                "keywords": ["关键词 1"],
                "quotes": [
                    {
                        "text": "经典语录",
                        "source": "出处",
                        "url": "https://example.com",
                        "confidence": "high|medium|low",
                    }
                ],
            },
            "conversations": {
                "patterns": ["对话模式 1"],
                "responses": ["常见回应方式 1"],
                "snippets": ["待继续补的互动片段 1"],
            },
            "expression_dna": {
                "rhythm": "节奏总结",
                "style_keywords": ["风格关键词 1"],
                "signature_actions": ["标志动作 1"],
                "quote_fingerprints": ["语录指纹 1"],
            },
            "external_views": {
                "supporters": ["支持者视角 1"],
                "critics": ["吐槽者视角 1"],
                "fan_views": ["二创社区视角 1"],
                "traits": [
                    {"trait": "性格特征", "evidence": "证据", "source": "来源"}
                ],
            },
            "decisions": {
                "rules": ["判断规则 1"],
                "tradeoffs": ["常见取舍 1"],
                "follow_ups": ["后续可补 1"],
            },
            "timeline": {"events": ["关键节点 1"]},
        },
        "sources": [{"title": "文档标题", "url": "https://example.com", "kind": "source kind", "note": "为何被引用"}],
    }

    return "\n".join(
        [
            "请根据下列目标画像和抓取到的公开资料，输出一个仓库兼容的 persona bundle。",
            "",
            "约束：",
            "1. 输出字段必须覆盖 schema_hint 的所有顶级结构。",
            "2. 经典语录要谨慎。出处弱时可以保留在 research.writings.quotes，但 confidence 不能写 high。",
            "3. 所有最终文案都写中文，风格要贴近当前仓库现有角色文档。",
            "4. 不要自称真实复活，不要冒充本人，不要编造私密信息。",
            "5. sample_dialogues 至少给两组。",
            "",
            "target_profile:",
            json.dumps(target, ensure_ascii=False, indent=2),
            "",
            "schema_hint:",
            json.dumps(schema_hint, ensure_ascii=False, indent=2),
            "",
            "documents:",
            json.dumps(excerpted_docs, ensure_ascii=False, indent=2),
        ]
    )
