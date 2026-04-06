from __future__ import annotations

import json
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
    aliases = target["known_aliases"]
    languages = set(target["primary_languages"])
    research_bias = target.get("research_bias", "comprehensive")
    profile_terms = aliases[:2] if aliases else [display_name]
    primary_alias = profile_terms[0]
    quote_terms = [
        "famous quotes",
        "quote",
        "interview transcript",
        "speech transcript",
        "writing",
        "letter",
        "biography",
        "personality",
        "leadership style",
        "decision making",
        "timeline",
    ]

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
            f'"{profile_terms[0]}" famous quotes',
            f'"{profile_terms[0]}" quote source',
            f'site:wikiquote.org "{profile_terms[0]}"',
            f'"{profile_terms[0]}" speech transcript',
        ],
        "first-person-writings": [
            f'"{profile_terms[0]}" interview transcript',
            f'"{profile_terms[0]}" writings',
            f'"{profile_terms[0]}" letters',
            f'"{profile_terms[0]}" essay OR article',
        ],
        "conversations-and-interviews": [
            f'site:youtube.com "{profile_terms[0]}" interview',
            f'"{profile_terms[0]}" podcast interview',
            f'"{profile_terms[0]}" Q&A transcript',
            f'"{profile_terms[0]}" responds to criticism',
        ],
        "personality-and-external-views": [
            f'"{profile_terms[0]}" personality profile',
            f'"{profile_terms[0]}" leadership style',
            f'"{profile_terms[0]}" critics describe',
            f'"{profile_terms[0]}" supporters describe',
        ],
        "decision-style": [
            f'"{profile_terms[0]}" decision making style',
            f'"{profile_terms[0]}" major decisions',
            f'"{profile_terms[0]}" risk appetite',
            f'"{profile_terms[0]}" management style',
        ],
        "timeline-and-evolution": [
            f'"{profile_terms[0]}" timeline',
            f'"{profile_terms[0]}" biography milestones',
            f'"{profile_terms[0]}" turning points',
            f'"{profile_terms[0]}" public image evolution',
        ],
    }

    bias_expansions = _bias_query_expansions(display_name, primary_alias)
    query_pack: list[dict[str, Any]] = []
    for group in QUERY_GROUPS:
        queries: list[str] = []
        if "zh" in languages:
            queries.extend(zh_queries[group["name"]])
        if "en" in languages:
            queries.extend(en_queries[group["name"]])
        if len(aliases) > 1:
            alt_name = aliases[1]
            queries.append(f'"{alt_name}" {quote_terms[0]}')
            queries.append(f'"{alt_name}" {quote_terms[7]}')
        queries.extend(bias_expansions.get(research_bias, {}).get(group["name"], []))
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
