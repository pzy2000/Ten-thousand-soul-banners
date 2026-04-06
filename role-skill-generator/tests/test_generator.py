from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

from role_skill_generator.models import (
    ValidationError,
    load_json,
    normalize_persona_bundle,
    normalize_target_profile,
)
from role_skill_generator.pipeline import _read_jsonl, generate_target_profile, summon_persona_materials
from role_skill_generator.query_pack import build_query_pack
from role_skill_generator.render import render_bundle_to_directory


class FakeLLMClient:
    def __init__(self, responses: list[dict[str, object]]) -> None:
        self._responses = list(responses)
        self.calls: list[tuple[str, str]] = []

    def generate_json(self, system_prompt: str, user_prompt: str) -> dict[str, object]:
        self.calls.append((system_prompt, user_prompt))
        if not self._responses:
            raise AssertionError("FakeLLMClient 收到的调用次数超出预期。")
        return self._responses.pop(0)


class GeneratorTests(unittest.TestCase):
    def test_target_profile_applies_defaults(self) -> None:
        target = normalize_target_profile(
            {
                "display_name": "Ada Lovelace",
                "classification": "公众人物 / 数学家 / 计算先驱",
                "category_tags": ["research-flag"],
            }
        )
        self.assertEqual(target["slug"], "ada-lovelace")
        self.assertEqual(target["target_root"], "soulbanner_skills")
        self.assertEqual(target["research_bias"], "comprehensive")
        self.assertRegex(target["updated_at"], r"^\d{4}-\d{2}-\d{2}$")
        self.assertIn("Ada Lovelace", target["known_aliases"])
        self.assertEqual(len(target["triggers"]), 2)

    def test_target_profile_rejects_unknown_research_bias(self) -> None:
        with self.assertRaises(ValidationError):
            normalize_target_profile(
                {
                    "display_name": "Ada Lovelace",
                    "classification": "公众人物 / 数学家 / 计算先驱",
                    "category_tags": ["research-flag"],
                    "research_bias": "chaotic",
                }
            )

    def test_target_profile_generates_stable_slug_for_non_latin_name(self) -> None:
        target = normalize_target_profile(
            {
                "display_name": "常熟阿诺",
                "classification": "网络人物 / 抽象系整活角色",
                "category_tags": ["abstract-flag"],
            }
        )
        self.assertRegex(target["slug"], r"^persona-[0-9a-f]{8}$")

    def test_query_pack_covers_quote_and_personality_tracks(self) -> None:
        target = normalize_target_profile(load_json(ROOT / "examples" / "ada-lovelace.target.json"))
        query_pack = build_query_pack(target)
        names = {item["name"] for item in query_pack}
        self.assertEqual(len(query_pack), 6)
        self.assertIn("quote-bank-primary", names)
        self.assertIn("personality-and-external-views", names)
        self.assertTrue(any("名言" in query for group in query_pack for query in group["queries"]))
        self.assertTrue(any("personality" in query for group in query_pack for query in group["queries"]))

    def test_query_pack_bias_changes_bias_specific_queries(self) -> None:
        humor_target = normalize_target_profile(
            {
                "display_name": "Ada Lovelace",
                "classification": "公众人物 / 数学家 / 计算先驱",
                "category_tags": ["research-flag"],
                "research_bias": "humor",
            }
        )
        serious_target = normalize_target_profile(
            {
                "display_name": "Ada Lovelace",
                "classification": "公众人物 / 数学家 / 计算先驱",
                "category_tags": ["research-flag"],
                "research_bias": "serious",
            }
        )
        humor_queries = [query for group in build_query_pack(humor_target) for query in group["queries"]]
        serious_queries = [query for group in build_query_pack(serious_target) for query in group["queries"]]
        self.assertTrue(any("梗" in query or "meme" in query for query in humor_queries))
        self.assertTrue(any("长篇 访谈" in query or "long-form interview" in query for query in serious_queries))
        self.assertFalse(any("梗图" in query or "meme compilation" in query for query in serious_queries))

    def test_query_pack_includes_user_description_context(self) -> None:
        target = normalize_target_profile(
            {
                "display_name": "骆源",
                "classification": "学者 / 教授",
                "description": "上海交通大学长聘教授",
                "category_tags": ["research-flag"],
                "primary_languages": ["zh"],
            }
        )
        queries = [query for group in build_query_pack(target) for query in group["queries"]]
        self.assertTrue(
            any('"骆源"' in query and '"上海交通大学长聘教授"' in query for query in queries)
        )

    def test_query_pack_does_not_expand_aliases_into_search_queries(self) -> None:
        target = normalize_target_profile(
            {
                "display_name": "Yann LeCun",
                "classification": "研究者 / AI scientist",
                "category_tags": ["research-flag"],
                "known_aliases": ["Y. LeCun", "Yann LeCun", "LeCun"],
                "primary_languages": ["en"],
            }
        )
        queries = [query for group in build_query_pack(target) for query in group["queries"]]
        self.assertFalse(any('"Y. LeCun"' in query for query in queries))
        self.assertFalse(any('"LeCun"' in query and '"Yann LeCun"' not in query for query in queries))

    def test_render_outputs_repo_shape(self) -> None:
        bundle = normalize_persona_bundle(load_json(ROOT / "examples" / "ada-lovelace.bundle.json"))
        with tempfile.TemporaryDirectory() as tmp_dir:
            persona_dir = render_bundle_to_directory(bundle, tmp_dir)
            self.assertTrue((persona_dir / "SKILL.md").exists())
            self.assertTrue((persona_dir / "README.md").exists())
            self.assertTrue((persona_dir / "references" / "research" / "01-writings.md").exists())
            self.assertTrue((persona_dir / "references" / "research" / "06-timeline.md").exists())
            skill_text = (persona_dir / "SKILL.md").read_text(encoding="utf-8")
            self.assertIn('name: "ada-lovelace"', skill_text)
            self.assertIn('# 角色定位', skill_text)
            self.assertNotIn("sources.md", "\n".join(path.name for path in persona_dir.iterdir()))

    def test_render_matches_golden_fixture(self) -> None:
        bundle = normalize_persona_bundle(load_json(ROOT / "examples" / "ada-lovelace.bundle.json"))
        expected_root = ROOT / "examples" / "rendered" / "ada-lovelace"
        with tempfile.TemporaryDirectory() as tmp_dir:
            actual_root = render_bundle_to_directory(bundle, tmp_dir)
            expected_files = self._relative_file_map(expected_root)
            actual_files = self._relative_file_map(actual_root)
            self.assertEqual(actual_files, expected_files)

    def test_bundle_validation_rejects_incomplete_payload(self) -> None:
        with self.assertRaises(ValidationError):
            normalize_persona_bundle(
                {
                    "display_name": "Ada Lovelace",
                    "classification": "公众人物 / 数学家 / 计算先驱",
                    "category_tags": ["research-flag"],
                }
            )

    def test_generate_target_profile_repairs_invalid_llm_output(self) -> None:
        client = FakeLLMClient(
            [
                {"classification": "公众人物 / 数学家 / 计算先驱"},
                {
                    "classification": "公众人物 / 数学家 / 计算先驱",
                    "category_tags": ["research-flag"],
                    "target_root": "soulbanner_skills",
                },
            ]
        )
        with tempfile.TemporaryDirectory() as tmp_dir:
            output_path = Path(tmp_dir) / "target.generated.json"
            target = generate_target_profile(
                "Ada Lovelace",
                "用 Ada Lovelace 的视角理解抽象建模与结构化想象。",
                "serious",
                output_path=output_path,
                client=client,
            )
            self.assertEqual(target["display_name"], "Ada Lovelace")
            self.assertEqual(target["research_bias"], "serious")
            self.assertEqual(target["target_root"], "soulbanner_skills")
            self.assertEqual(len(client.calls), 2)
            self.assertIn("未通过校验", client.calls[1][1])
            self.assertEqual(load_json(output_path)["research_bias"], "serious")

    def test_read_jsonl_preserves_line_separator_inside_strings(self) -> None:
        """U+2028 must not split records: splitlines() would break one JSON object into two."""
        doc = {"url": "https://example.com", "content": "before\u2028after", "title": "t"}
        line = json.dumps(doc, ensure_ascii=False)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".jsonl") as handle:
            handle.write(line + "\n")
            handle.write(json.dumps({"url": "u2"}, ensure_ascii=False) + "\n")
            path = Path(handle.name)
        try:
            rows = _read_jsonl(path)
            self.assertEqual(len(rows), 2)
            self.assertEqual(rows[0]["content"], "before\u2028after")
        finally:
            path.unlink()

    def test_summon_persona_materials_generates_target_then_runs_pipeline(self) -> None:
        generated_target = normalize_target_profile(
            {
                "display_name": "Elon Musk",
                "classification": "公众人物 / 企业家 / 强意志 power figure",
                "category_tags": ["renhuang-flag"],
                "target_root": "sovereign_skills",
                "research_bias": "serious",
            }
        )
        with patch(
            "role_skill_generator.pipeline.generate_target_profile",
            return_value=generated_target,
        ) as generate_target_mock, patch(
            "role_skill_generator.pipeline.generate_persona_materials",
            return_value=Path("/tmp/sovereign_skills/musk"),
        ) as generate_materials_mock:
            persona_dir = summon_persona_materials(
                "Elon Musk",
                "聚焦工程推进、强意志叙事与第一性原理。",
                "serious",
                workspace_root=Path("/workspace"),
                runs_root=Path("/tmp/runs"),
                provider_name="tavily",
                max_results=7,
                max_documents=9,
                model="gpt-test",
                verbose_collect=False,
            )

        self.assertEqual(persona_dir, Path("/tmp/sovereign_skills/musk"))
        generate_target_mock.assert_called_once()
        generate_args, generate_kwargs = generate_materials_mock.call_args
        self.assertEqual(generate_args[0], Path("/tmp/runs/elon-musk/target.generated.json"))
        self.assertEqual(generate_args[1], Path("/tmp/runs/elon-musk"))
        self.assertEqual(generate_args[2], Path("/workspace/soulbanner_skills"))
        self.assertEqual(generate_kwargs["provider_name"], "tavily")
        self.assertEqual(generate_kwargs["max_results"], 7)
        self.assertEqual(generate_kwargs["max_documents"], 9)
        self.assertEqual(generate_kwargs["model"], "gpt-test")
        self.assertFalse(generate_kwargs["verbose_collect"])

    def _relative_file_map(self, root: Path) -> dict[str, str]:
        return {
            path.relative_to(root).as_posix(): path.read_text(encoding="utf-8")
            for path in sorted(root.rglob("*"))
            if path.is_file()
        }


if __name__ == "__main__":
    unittest.main()
