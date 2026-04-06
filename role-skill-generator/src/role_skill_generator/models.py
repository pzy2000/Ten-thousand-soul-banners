from __future__ import annotations

import json
import hashlib
import re
from copy import deepcopy
from datetime import date
from pathlib import Path
from typing import Any

DEFAULT_SOURCE_SCOPE = ["公开采访", "公开视频", "公开文本"]
DEFAULT_RESEARCH_FOCUS = [
    "经典语录",
    "第一手表达",
    "性格与外界评价",
    "决策方式",
    "时间线与人设变化",
]
ALLOWED_TARGET_ROOTS = {"soulbanner_skills", "sovereign_skills"}
ALLOWED_RESEARCH_BIASES = {"humor", "serious", "comprehensive"}


class ValidationError(ValueError):
    """Raised when user-provided JSON does not satisfy the subproject contract."""


def today_string() -> str:
    return date.today().isoformat()


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug:
        digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
        slug = f"persona-{digest}"
    return slug


def load_json(path: str | Path) -> dict[str, Any]:
    file_path = Path(path)
    data = json.loads(file_path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValidationError(f"{file_path} 顶层必须是 JSON object。")
    return data


def write_json(path: str | Path, data: dict[str, Any]) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _required_str(data: dict[str, Any], key: str) -> str:
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"字段 `{key}` 必须是非空字符串。")
    return value.strip()


def _optional_str(
    data: dict[str, Any],
    key: str,
    default: str = "",
) -> str:
    value = data.get(key, default)
    if value is None:
        return default
    if not isinstance(value, str):
        raise ValidationError(f"字段 `{key}` 必须是字符串。")
    return value.strip()


def _str_list(
    value: Any,
    *,
    key: str,
    default: list[str] | None = None,
    min_items: int = 0,
) -> list[str]:
    if value is None:
        result = list(default or [])
    elif isinstance(value, list) and all(isinstance(item, str) for item in value):
        result = [item.strip() for item in value if item.strip()]
    else:
        raise ValidationError(f"字段 `{key}` 必须是字符串数组。")
    if len(result) < min_items:
        raise ValidationError(f"字段 `{key}` 至少需要 {min_items} 项。")
    return result


def _dict(value: Any, *, key: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ValidationError(f"字段 `{key}` 必须是 object。")
    return value


def _dialogues(value: Any) -> list[dict[str, str]]:
    if not isinstance(value, list) or not value:
        raise ValidationError("字段 `sample_dialogues` 必须是非空数组。")
    dialogues: list[dict[str, str]] = []
    for index, item in enumerate(value, start=1):
        if not isinstance(item, dict):
            raise ValidationError(f"`sample_dialogues[{index}]` 必须是 object。")
        user = _required_str(item, "user")
        persona = _required_str(item, "persona")
        dialogues.append({"user": user, "persona": persona})
    return dialogues


def _quote_items(value: Any, *, key: str) -> list[dict[str, str]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValidationError(f"字段 `{key}` 必须是数组。")
    items: list[dict[str, str]] = []
    for index, item in enumerate(value, start=1):
        if not isinstance(item, dict):
            raise ValidationError(f"`{key}[{index}]` 必须是 object。")
        items.append(
            {
                "text": _required_str(item, "text"),
                "source": _optional_str(item, "source", "未补"),
                "url": _optional_str(item, "url"),
                "confidence": _optional_str(item, "confidence", "medium"),
            }
        )
    return items


def _trait_items(value: Any, *, key: str) -> list[dict[str, str]]:
    if value is None:
        return []
    if not isinstance(value, list):
        raise ValidationError(f"字段 `{key}` 必须是数组。")
    items: list[dict[str, str]] = []
    for index, item in enumerate(value, start=1):
        if not isinstance(item, dict):
            raise ValidationError(f"`{key}[{index}]` 必须是 object。")
        items.append(
            {
                "trait": _required_str(item, "trait"),
                "evidence": _optional_str(item, "evidence", "待补"),
                "source": _optional_str(item, "source", "待补"),
            }
        )
    return items


def normalize_target_profile(data: dict[str, Any]) -> dict[str, Any]:
    profile = deepcopy(data)
    slug = profile.get("slug")
    if isinstance(slug, str) and slug.strip():
        slug = slugify(slug)
    else:
        slug = slugify(_required_str(profile, "display_name"))

    target_root = _optional_str(profile, "target_root", "soulbanner_skills")
    if target_root not in ALLOWED_TARGET_ROOTS:
        raise ValidationError(
            "`target_root` 只能是 `soulbanner_skills` 或 `sovereign_skills`。"
        )

    research_bias = _optional_str(profile, "research_bias", "comprehensive")
    if research_bias not in ALLOWED_RESEARCH_BIASES:
        raise ValidationError(
            "`research_bias` 只能是 `humor`、`serious` 或 `comprehensive`。"
        )

    result = {
        "slug": slug,
        "display_name": _required_str(profile, "display_name"),
        "classification": _required_str(profile, "classification"),
        "description": _optional_str(profile, "description"),
        "category_tags": _str_list(profile.get("category_tags"), key="category_tags", min_items=1),
        "target_root": target_root,
        "research_bias": research_bias,
        "triggers": _str_list(profile.get("triggers"), key="triggers", default=[]),
        "source_scope": _str_list(
            profile.get("source_scope"),
            key="source_scope",
            default=DEFAULT_SOURCE_SCOPE,
            min_items=1,
        ),
        "updated_at": _optional_str(profile, "updated_at", today_string()),
        "known_aliases": _str_list(profile.get("known_aliases"), key="known_aliases", default=[]),
        "research_focus": _str_list(
            profile.get("research_focus"),
            key="research_focus",
            default=DEFAULT_RESEARCH_FOCUS,
            min_items=1,
        ),
        "primary_languages": _str_list(
            profile.get("primary_languages"),
            key="primary_languages",
            default=["zh", "en"],
            min_items=1,
        ),
    }
    if not result["triggers"]:
        name = result["display_name"]
        result["triggers"] = [f"切到{name}模式", f"用{name}的视角看这件事"]
    if result["display_name"] not in result["known_aliases"]:
        result["known_aliases"].insert(0, result["display_name"])
    return result


def normalize_persona_bundle(data: dict[str, Any]) -> dict[str, Any]:
    bundle = deepcopy(data)
    profile = normalize_target_profile(bundle)

    style = _dict(bundle.get("style"), key="style")
    expression_dna = _dict(bundle.get("expression_dna"), key="expression_dna")
    persona_tension = _dict(bundle.get("persona_tension"), key="persona_tension")
    boundaries = _dict(bundle.get("boundaries"), key="boundaries")
    readme = _dict(bundle.get("readme"), key="readme")
    research = _dict(bundle.get("research"), key="research")

    writings = _dict(research.get("writings"), key="research.writings")
    conversations = _dict(research.get("conversations"), key="research.conversations")
    expression_notes = _dict(
        research.get("expression_dna"),
        key="research.expression_dna",
    )
    external_views = _dict(
        research.get("external_views"),
        key="research.external_views",
    )
    decisions = _dict(research.get("decisions"), key="research.decisions")
    timeline = _dict(research.get("timeline"), key="research.timeline")

    normalized = {
        **profile,
        "who_is": _required_str(bundle, "who_is"),
        "why_distilled": _required_str(bundle, "why_distilled"),
        "user_scenarios": _str_list(
            bundle.get("user_scenarios"),
            key="user_scenarios",
            min_items=3,
        ),
        "style": {
            "tone": _required_str(style, "tone"),
            "rhythm": _required_str(style, "rhythm"),
            "sentence_length": _required_str(style, "sentence_length"),
            "catchphrases": _str_list(style.get("catchphrases"), key="style.catchphrases", default=[]),
            "signature_moves": _str_list(
                style.get("signature_moves"),
                key="style.signature_moves",
                default=[],
            ),
        },
        "cognitive_frames": _str_list(
            bundle.get("cognitive_frames"),
            key="cognitive_frames",
            min_items=3,
        ),
        "decision_heuristics": _str_list(
            bundle.get("decision_heuristics"),
            key="decision_heuristics",
            min_items=4,
        ),
        "expression_dna": {
            "opening": _required_str(expression_dna, "opening"),
            "transition": _required_str(expression_dna, "transition"),
            "pressure": _required_str(expression_dna, "pressure"),
            "self_mockery": _required_str(expression_dna, "self_mockery"),
            "questioning": _required_str(expression_dna, "questioning"),
            "closing": _required_str(expression_dna, "closing"),
        },
        "persona_tension": {
            "charm": _required_str(persona_tension, "charm"),
            "criticism": _required_str(persona_tension, "criticism"),
            "exaggeration": _required_str(persona_tension, "exaggeration"),
        },
        "boundaries": {
            "can_answer": _str_list(boundaries.get("can_answer"), key="boundaries.can_answer", min_items=2),
            "cannot_answer": _str_list(
                boundaries.get("cannot_answer"),
                key="boundaries.cannot_answer",
                min_items=2,
            ),
            "weak_domains": _str_list(
                boundaries.get("weak_domains"),
                key="boundaries.weak_domains",
                min_items=1,
            ),
            "disclaimer": _required_str(boundaries, "disclaimer"),
        },
        "sample_dialogues": _dialogues(bundle.get("sample_dialogues")),
        "readme": {
            "intro": _required_str(readme, "intro"),
            "why_worth": _required_str(readme, "why_worth"),
            "distilled_points": _str_list(
                readme.get("distilled_points"),
                key="readme.distilled_points",
                min_items=3,
            ),
            "fit_questions": _str_list(
                readme.get("fit_questions"),
                key="readme.fit_questions",
                min_items=3,
            ),
            "sample_questions": _str_list(
                readme.get("sample_questions"),
                key="readme.sample_questions",
                min_items=2,
            ),
            "about": _required_str(readme, "about"),
        },
        "research": {
            "writings": {
                "conclusions": _str_list(
                    writings.get("conclusions"),
                    key="research.writings.conclusions",
                    min_items=1,
                ),
                "keywords": _str_list(
                    writings.get("keywords"),
                    key="research.writings.keywords",
                    min_items=1,
                ),
                "quotes": _quote_items(writings.get("quotes"), key="research.writings.quotes"),
            },
            "conversations": {
                "patterns": _str_list(
                    conversations.get("patterns"),
                    key="research.conversations.patterns",
                    min_items=1,
                ),
                "responses": _str_list(
                    conversations.get("responses"),
                    key="research.conversations.responses",
                    default=[],
                ),
                "snippets": _str_list(
                    conversations.get("snippets"),
                    key="research.conversations.snippets",
                    default=[],
                ),
            },
            "expression_dna": {
                "rhythm": _required_str(expression_notes, "rhythm"),
                "style_keywords": _str_list(
                    expression_notes.get("style_keywords"),
                    key="research.expression_dna.style_keywords",
                    min_items=1,
                ),
                "signature_actions": _str_list(
                    expression_notes.get("signature_actions"),
                    key="research.expression_dna.signature_actions",
                    min_items=1,
                ),
                "quote_fingerprints": _str_list(
                    expression_notes.get("quote_fingerprints"),
                    key="research.expression_dna.quote_fingerprints",
                    default=[],
                ),
            },
            "external_views": {
                "supporters": _str_list(
                    external_views.get("supporters"),
                    key="research.external_views.supporters",
                    default=[],
                ),
                "critics": _str_list(
                    external_views.get("critics"),
                    key="research.external_views.critics",
                    default=[],
                ),
                "fan_views": _str_list(
                    external_views.get("fan_views"),
                    key="research.external_views.fan_views",
                    default=[],
                ),
                "traits": _trait_items(
                    external_views.get("traits"),
                    key="research.external_views.traits",
                ),
            },
            "decisions": {
                "rules": _str_list(
                    decisions.get("rules"),
                    key="research.decisions.rules",
                    min_items=1,
                ),
                "tradeoffs": _str_list(
                    decisions.get("tradeoffs"),
                    key="research.decisions.tradeoffs",
                    default=[],
                ),
                "follow_ups": _str_list(
                    decisions.get("follow_ups"),
                    key="research.decisions.follow_ups",
                    default=[],
                ),
            },
            "timeline": {
                "events": _str_list(
                    timeline.get("events"),
                    key="research.timeline.events",
                    min_items=1,
                ),
            },
        },
        "sources": [],
    }

    sources = bundle.get("sources", [])
    if sources is None:
        sources = []
    if not isinstance(sources, list):
        raise ValidationError("字段 `sources` 必须是数组。")
    for index, item in enumerate(sources, start=1):
        if not isinstance(item, dict):
            raise ValidationError(f"`sources[{index}]` 必须是 object。")
        normalized["sources"].append(
            {
                "title": _required_str(item, "title"),
                "url": _required_str(item, "url"),
                "kind": _optional_str(item, "kind", "web"),
                "note": _optional_str(item, "note"),
            }
        )
    return normalized
