from __future__ import annotations

from pathlib import Path
from typing import Any


def _yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def _section(title: str) -> list[str]:
    return [f"## {title}", ""]


def _bullet_lines(items: list[str]) -> list[str]:
    if not items:
        return ["* 待补。", ""]
    return [f"* {item}" for item in items] + [""]


def _quote_lines(items: list[dict[str, str]]) -> list[str]:
    if not items:
        return ["* 暂无已追溯的一手语录候选。", ""]
    lines: list[str] = []
    for item in items:
        source = item["source"]
        confidence = item["confidence"]
        url = item["url"]
        suffix = f" | 置信度：{confidence}"
        if url:
            suffix += f" | {url}"
        lines.append(f'* “{item["text"]}”')
        lines.append(f"  来源：{source}{suffix}")
    lines.append("")
    return lines


def _trait_lines(items: list[dict[str, str]]) -> list[str]:
    if not items:
        return ["* 暂无结构化 trait 证据。", ""]
    lines: list[str] = []
    for item in items:
        lines.append(f'* `{item["trait"]}`：{item["evidence"]}（来源：{item["source"]}）')
    lines.append("")
    return lines


def render_skill_markdown(bundle: dict[str, Any]) -> str:
    style = bundle["style"]
    dna = bundle["expression_dna"]
    tension = bundle["persona_tension"]
    boundaries = bundle["boundaries"]

    lines = [
        "---",
        f'name: {_yaml_quote(bundle["slug"])}',
        f'description: {_yaml_quote(bundle["description"])}',
        "triggers:",
    ]
    for trigger in bundle["triggers"]:
        lines.append(f"  - {_yaml_quote(trigger)}")
    lines.extend(["source_scope:"])
    for item in bundle["source_scope"]:
        lines.append(f"  - {_yaml_quote(item)}")
    lines.append(f'updated_at: {_yaml_quote(bundle["updated_at"])}')
    lines.extend(["category_tags:"])
    for tag in bundle["category_tags"]:
        lines.append(f"  - {_yaml_quote(tag)}")
    lines.extend(
        [
            "---",
            "",
            "# 角色定位",
            "",
            "## 他是谁",
            "",
            bundle["who_is"],
            "",
            "## 为什么会被收进万魂幡",
            "",
            bundle["why_distilled"],
            "",
            "## 用户会在什么问题里调用他",
            "",
        ]
    )
    lines.extend(_bullet_lines(bundle["user_scenarios"]))
    lines.extend(
        [
            "# 输出风格",
            "",
            "## 语气",
            "",
            style["tone"],
            "",
            "## 节奏",
            "",
            style["rhythm"],
            "",
            "## 句长",
            "",
            style["sentence_length"],
            "",
            "## 口头禅",
            "",
        ]
    )
    lines.extend(_bullet_lines(style["catchphrases"]))
    lines.extend(["## 标志性表达动作", ""])
    lines.extend(_bullet_lines(style["signature_moves"]))
    lines.extend(["# 核心认知框架", ""])
    lines.extend(_bullet_lines(bundle["cognitive_frames"]))
    lines.extend(["# 决策启发式", ""])
    lines.extend(_bullet_lines(bundle["decision_heuristics"]))
    lines.extend(
        [
            "# 表达 DNA",
            "",
            "## 开场方式",
            "",
            dna["opening"],
            "",
            "## 转折方式",
            "",
            dna["transition"],
            "",
            "## 压人方式",
            "",
            dna["pressure"],
            "",
            "## 自嘲方式",
            "",
            dna["self_mockery"],
            "",
            "## 反问方式",
            "",
            dna["questioning"],
            "",
            "## 收尾方式",
            "",
            dna["closing"],
            "",
            "# 人设张力",
            "",
            "## 他最迷人的地方",
            "",
            tension["charm"],
            "",
            "## 他最招黑的地方",
            "",
            tension["criticism"],
            "",
            "## 他最容易被二创放大的点",
            "",
            tension["exaggeration"],
            "",
            "# 使用边界",
            "",
            "## 能回答什么",
            "",
        ]
    )
    lines.extend(_bullet_lines(boundaries["can_answer"]))
    lines.extend(["## 不能回答什么", ""])
    lines.extend(_bullet_lines(boundaries["cannot_answer"]))
    lines.extend(["## 哪些是素材不足的领域", ""])
    lines.extend(_bullet_lines(boundaries["weak_domains"]))
    lines.extend(
        [
            "## 明确不替代本人",
            "",
            boundaries["disclaimer"],
            "",
            "# 示例对话",
            "",
        ]
    )
    for index, dialogue in enumerate(bundle["sample_dialogues"], start=1):
        lines.extend(
            [
                f"## 示例 {index}",
                "",
                f"**用户：** {dialogue['user']}",
                "",
                f"**角色：** {dialogue['persona']}",
                "",
            ]
        )
    return "\n".join(lines)


def render_readme_markdown(bundle: dict[str, Any]) -> str:
    readme = bundle["readme"]
    lines = [
        f"# {bundle['display_name']}",
        "",
        "## 一句话介绍",
        "",
        readme["intro"],
        "",
        "## 为什么这个人值得蒸馏",
        "",
        readme["why_worth"],
        "",
        "## 他蒸馏了什么",
        "",
    ]
    lines.extend(_bullet_lines(readme["distilled_points"]))
    lines.extend(["## 适合回答什么问题", ""])
    lines.extend(_bullet_lines(readme["fit_questions"]))
    lines.extend(["## 触发词", ""])
    lines.extend(_bullet_lines([f"`{item}`" for item in bundle["triggers"]]))
    lines.extend(["## 示例问题", ""])
    lines.extend(_bullet_lines([f"`{item}`" for item in readme["sample_questions"]]))
    lines.extend(["## 素材来源", ""])
    lines.extend(_bullet_lines(bundle["source_scope"]))
    lines.extend(
        [
            "## 诚实边界",
            "",
            "* 这是基于公开素材蒸馏出的二创人格，不替代本人",
            "* 不保证时效事实正确",
            "* 不用于冒充、诈骗、误导",
        ]
    )
    lines.extend(_bullet_lines(bundle["boundaries"]["weak_domains"]))
    lines.extend(
        [
            "## 仓库结构",
            "",
            "```text",
            f"{bundle['slug']}/",
            "├── SKILL.md",
            "├── README.md",
            "└── references/",
            "    └── research/",
            "        ├── 01-writings.md",
            "        ├── 02-conversations.md",
            "        ├── 03-expression-dna.md",
            "        ├── 04-external-views.md",
            "        ├── 05-decisions.md",
            "        └── 06-timeline.md",
            "```",
            "",
            "## 关于此人",
            "",
            readme["about"],
            "",
            "## License",
            "",
            "默认跟随仓库根目录 License。",
            "",
        ]
    )
    return "\n".join(lines)


def render_research_writings(bundle: dict[str, Any]) -> str:
    writings = bundle["research"]["writings"]
    lines = [
        "# 01-writings",
        "",
        "## 当前蒸馏结论",
        "",
    ]
    lines.extend(_bullet_lines(writings["conclusions"]))
    lines.extend(["## 暂定关键词", ""])
    lines.extend(_bullet_lines(writings["keywords"]))
    lines.extend(["## 经典语录候选", ""])
    lines.extend(_quote_lines(writings["quotes"]))
    return "\n".join(lines)


def render_research_conversations(bundle: dict[str, Any]) -> str:
    conversations = bundle["research"]["conversations"]
    lines = [
        "# 02-conversations",
        "",
        "## 对话模式",
        "",
    ]
    lines.extend(_bullet_lines(conversations["patterns"]))
    lines.extend(["## 常见回应方式", ""])
    lines.extend(_bullet_lines(conversations["responses"]))
    lines.extend(["## 可继续补的互动片段", ""])
    lines.extend(_bullet_lines(conversations["snippets"]))
    return "\n".join(lines)


def render_research_expression(bundle: dict[str, Any]) -> str:
    notes = bundle["research"]["expression_dna"]
    lines = [
        "# 03-expression-dna",
        "",
        "## 节奏",
        "",
        notes["rhythm"],
        "",
        "## 风格关键词",
        "",
    ]
    lines.extend(_bullet_lines(notes["style_keywords"]))
    lines.extend(["## 标志动作", ""])
    lines.extend(_bullet_lines(notes["signature_actions"]))
    lines.extend(["## 语录指纹", ""])
    lines.extend(_bullet_lines(notes["quote_fingerprints"]))
    return "\n".join(lines)


def render_research_external_views(bundle: dict[str, Any]) -> str:
    notes = bundle["research"]["external_views"]
    lines = [
        "# 04-external-views",
        "",
        "## 支持者视角",
        "",
    ]
    lines.extend(_bullet_lines(notes["supporters"]))
    lines.extend(["## 吐槽者视角", ""])
    lines.extend(_bullet_lines(notes["critics"]))
    lines.extend(["## 二创社区视角", ""])
    lines.extend(_bullet_lines(notes["fan_views"]))
    lines.extend(["## trait 证据表", ""])
    lines.extend(_trait_lines(notes["traits"]))
    return "\n".join(lines)


def render_research_decisions(bundle: dict[str, Any]) -> str:
    notes = bundle["research"]["decisions"]
    lines = [
        "# 05-decisions",
        "",
        "## 初步判断规则",
        "",
    ]
    lines.extend(_bullet_lines(notes["rules"]))
    lines.extend(["## 常见取舍", ""])
    lines.extend(_bullet_lines(notes["tradeoffs"]))
    lines.extend(["## 后续可补", ""])
    lines.extend(_bullet_lines(notes["follow_ups"]))
    return "\n".join(lines)


def render_research_timeline(bundle: dict[str, Any]) -> str:
    lines = [
        "# 06-timeline",
        "",
        "## 关键节点",
        "",
    ]
    lines.extend(_bullet_lines(bundle["research"]["timeline"]["events"]))
    return "\n".join(lines)


def render_bundle_to_directory(bundle: dict[str, Any], output_root: str | Path) -> Path:
    root = Path(output_root)
    persona_dir = root / bundle["slug"]
    research_dir = persona_dir / "references" / "research"
    research_dir.mkdir(parents=True, exist_ok=True)

    (persona_dir / "SKILL.md").write_text(render_skill_markdown(bundle), encoding="utf-8")
    (persona_dir / "README.md").write_text(render_readme_markdown(bundle), encoding="utf-8")
    (research_dir / "01-writings.md").write_text(render_research_writings(bundle), encoding="utf-8")
    (research_dir / "02-conversations.md").write_text(
        render_research_conversations(bundle),
        encoding="utf-8",
    )
    (research_dir / "03-expression-dna.md").write_text(
        render_research_expression(bundle),
        encoding="utf-8",
    )
    (research_dir / "04-external-views.md").write_text(
        render_research_external_views(bundle),
        encoding="utf-8",
    )
    (research_dir / "05-decisions.md").write_text(
        render_research_decisions(bundle),
        encoding="utf-8",
    )
    (research_dir / "06-timeline.md").write_text(render_research_timeline(bundle), encoding="utf-8")
    return persona_dir
