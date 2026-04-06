from __future__ import annotations

import json
import re
from typing import Any


QUERY_GROUPS = [
    {
        "name": "quote-bank-primary",
        "purpose": "优先找到可追溯的一手经典语录、书信、演讲、公开文本与原始出处。",
    },
    {
        "name": "first-person-writings",
        "purpose": "找人物自己的长文本、访谈稿、专栏、手记，用来提炼稳定表达与世界观。",
    },
    {
        "name": "conversations-and-interviews",
        "purpose": "找真实互动场景，判断他在被质疑、被赞美、被追问时怎么回。",
    },
    {
        "name": "personality-and-external-views",
        "purpose": "找外界对其性格、标签、争议点与魅力点的持续描述。",
    },
    {
        "name": "decision-style",
        "purpose": "找关键决策、取舍、风险偏好和判断启发式。",
    },
    {
        "name": "timeline-and-evolution",
        "purpose": "找人设形成、转折、出圈和风格固化的时间线证据。",
    },
]


_ZH_CONTEXT_SUFFIXES = {
    "quote-bank-primary": "名言",
    "first-person-writings": "采访",
    "conversations-and-interviews": "对话",
    "personality-and-external-views": "评价",
    "decision-style": "决策",
    "timeline-and-evolution": "时间线",
}
_EN_CONTEXT_SUFFIXES = {
    "quote-bank-primary": "quotes",
    "first-person-writings": "interview",
    "conversations-and-interviews": "conversation",
    "personality-and-external-views": "profile",
    "decision-style": "decision making",
    "timeline-and-evolution": "timeline",
}
_GENERIC_CONTEXT_TERMS = {
    "公众人物",
    "人物",
    "角色",
    "角色类型",
    "网络人物",
}


def _contains_cjk(text: str) -> bool:
    return bool(re.search(r"[\u3400-\u9fff]", text))


def _dedupe_keep_order(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in values:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def _looks_like_search_phrase(text: str) -> bool:
    stripped = " ".join(text.split()).strip(" -")
    if len(stripped) < 2:
        return False
    if stripped in _GENERIC_CONTEXT_TERMS:
        return False
    if _contains_cjk(stripped):
        if len(stripped) > 24:
            return False
    elif len(stripped) > 64:
        return False
    return True


def _extract_context_terms(target: dict[str, Any]) -> list[str]:
    description = " ".join(str(target.get("description", "")).split())
    classification = " ".join(str(target.get("classification", "")).split())
    candidates: list[str] = []

    if description and _looks_like_search_phrase(description) and not re.search(r"[，。,；;、/|]", description):
        candidates.append(description)

    split_pattern = r"[，。,；;、/|]+"
    for source in (description, classification):
        for chunk in re.split(split_pattern, source):
            normalized = " ".join(chunk.split()).strip(" -")
            if _looks_like_search_phrase(normalized):
                candidates.append(normalized)

    aliases = {alias.strip() for alias in target.get("known_aliases", []) if isinstance(alias, str)}
    aliases.add(str(target.get("display_name", "")).strip())
    return [term for term in _dedupe_keep_order(candidates) if term and term not in aliases][:3]


def _context_query_expansions(
    target: dict[str, Any],
    display_name: str,
) -> dict[str, list[str]]:
    context_terms = _extract_context_terms(target)
    expansions = {group["name"]: [] for group in QUERY_GROUPS}
    for group in QUERY_GROUPS:
        group_name = group["name"]
        zh_suffix = _ZH_CONTEXT_SUFFIXES[group_name]
        en_suffix = _EN_CONTEXT_SUFFIXES[group_name]
        for term in context_terms:
            if _contains_cjk(term):
                expansions[group_name].append(f'"{display_name}" "{term}" {zh_suffix}')
            else:
                expansions[group_name].append(f'"{display_name}" "{term}" {en_suffix}')
    return expansions


def _bias_query_expansions(
    display_name: str,
    primary_alias: str,
) -> dict[str, dict[str, list[str]]]:
    humor = {
        "quote-bank-primary": [
            f'"{display_name}" 梗图',
            f'"{primary_alias}" meme compilation',
        ],
        "conversations-and-interviews": [
            f'"{display_name}" 名场面',
            f'"{primary_alias}" parody',
        ],
        "personality-and-external-views": [
            f'"{display_name}" 二创',
            f'"{primary_alias}" meme',
        ],
    }
    serious = {
        "first-person-writings": [
            f'"{display_name}" 长篇 访谈',
            f'"{primary_alias}" long-form interview',
        ],
        "decision-style": [
            f'"{display_name}" 深度 复盘',
            f'"{primary_alias}" strategic analysis',
        ],
        "timeline-and-evolution": [
            f'"{display_name}" 生涯 转折 复盘',
            f'"{primary_alias}" long-term trajectory',
        ],
    }
    return {
        "humor": humor,
        "serious": serious,
        "comprehensive": {
            group_name: humor.get(group_name, []) + serious.get(group_name, [])
            for group_name in {*(humor.keys()), *(serious.keys())}
        },
    }


def build_query_pack(target: dict[str, Any]) -> list[dict[str, Any]]:
    display_name = target["display_name"]
    languages = set(target["primary_languages"])
    research_bias = target.get("research_bias", "comprehensive")

    zh_queries = {
        "quote-bank-primary": [
            f'"{display_name}" 名言',
            f'"{display_name}" 经典语录',
            f'"{display_name}" 演讲 原文',
            f'"{display_name}" 书信 原文',
        ],
        "first-person-writings": [
            f'"{display_name}" 采访 实录',
            f'"{display_name}" 专栏 文章',
            f'"{display_name}" 公开发言',
            f'"{display_name}" 访谈 逐字稿',
        ],
        "conversations-and-interviews": [
            f'site:youtube.com "{display_name}" 访谈',
            f'"{display_name}" 对话 采访',
            f'"{display_name}" 面对质疑 怎么回应',
            f'"{display_name}" 播客 访谈',
        ],
        "personality-and-external-views": [
            f'"{display_name}" 性格 分析',
            f'"{display_name}" 外界 评价',
            f'"{display_name}" 支持者 评价',
            f'"{display_name}" 争议 风格',
        ],
        "decision-style": [
            f'"{display_name}" 决策 风格',
            f'"{display_name}" 关键决定',
            f'"{display_name}" 风险 偏好',
            f'"{display_name}" 如何 取舍',
        ],
        "timeline-and-evolution": [
            f'"{display_name}" 时间线',
            f'"{display_name}" 生平 重要节点',
            f'"{display_name}" 出圈 节点',
            f'"{display_name}" 风格 变化',
        ],
    }

    en_queries = {
        "quote-bank-primary": [
            f'"{display_name}" famous quotes',
            f'"{display_name}" quote source',
            f'site:wikiquote.org "{display_name}"',
            f'"{display_name}" speech transcript',
        ],
        "first-person-writings": [
            f'"{display_name}" interview transcript',
            f'"{display_name}" writings',
            f'"{display_name}" letters',
            f'"{display_name}" essay OR article',
        ],
        "conversations-and-interviews": [
            f'site:youtube.com "{display_name}" interview',
            f'"{display_name}" podcast interview',
            f'"{display_name}" Q&A transcript',
            f'"{display_name}" responds to criticism',
        ],
        "personality-and-external-views": [
            f'"{display_name}" personality profile',
            f'"{display_name}" leadership style',
            f'"{display_name}" critics describe',
            f'"{display_name}" supporters describe',
        ],
        "decision-style": [
            f'"{display_name}" decision making style',
            f'"{display_name}" major decisions',
            f'"{display_name}" risk appetite',
            f'"{display_name}" management style',
        ],
        "timeline-and-evolution": [
            f'"{display_name}" timeline',
            f'"{display_name}" biography milestones',
            f'"{display_name}" turning points',
            f'"{display_name}" public image evolution',
        ],
    }

    bias_expansions = _bias_query_expansions(display_name, display_name)
    context_expansions = _context_query_expansions(target, display_name)
    query_pack: list[dict[str, Any]] = []
    for group in QUERY_GROUPS:
        queries: list[str] = []
        if "zh" in languages:
            queries.extend(zh_queries[group["name"]])
        if "en" in languages:
            queries.extend(en_queries[group["name"]])
        queries.extend(context_expansions.get(group["name"], []))
        queries.extend(bias_expansions.get(research_bias, {}).get(group["name"], []))
        queries = _dedupe_keep_order(queries)
        query_pack.append(
            {
                "name": group["name"],
                "purpose": group["purpose"],
                "queries": queries,
            }
        )
    return query_pack


def render_query_pack_markdown(target: dict[str, Any], query_pack: list[dict[str, Any]]) -> str:
    lines = [
        f"# {target['display_name']} Query Pack",
        "",
        "## 检索原则",
        "",
        "* 优先一手来源，再用高质量二手来源补背景。",
        "* 经典语录必须尽量追到最早可验证出处；追不到的保留在候选区，不直接上主 skill。",
        "* 性格判断必须有跨来源证据，不接受单篇营销稿定人设。",
        "* 时间线要服务于“风格形成与变化”，不是堆百科事实。",
        "",
    ]
    for group in query_pack:
        lines.append(f"## {group['name']}")
        lines.append("")
        lines.append(group["purpose"])
        lines.append("")
        for query in group["queries"]:
            lines.append(f"* `{query}`")
        lines.append("")
    lines.append("## 机器可读")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(query_pack, ensure_ascii=False, indent=2))
    lines.append("```")
    lines.append("")
    return "\n".join(lines)
