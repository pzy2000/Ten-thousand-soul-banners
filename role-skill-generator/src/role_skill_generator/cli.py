from __future__ import annotations

import argparse
from pathlib import Path

from role_skill_generator.pipeline import (
    collect_sources,
    generate_persona_materials,
    plan_queries,
    render_bundle,
    synthesize_bundle,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="role-skill-generator",
        description="Research and render persona skills in the SoulBanner format.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    plan_cmd = subparsers.add_parser("plan-queries", help="根据 target JSON 生成检索 query pack。")
    plan_cmd.add_argument("target", help="target profile JSON")
    plan_cmd.add_argument("--output", help="query-pack markdown 输出路径")

    collect_cmd = subparsers.add_parser("collect", help="执行搜索并抓取资料。")
    collect_cmd.add_argument("target", help="target profile JSON")
    collect_cmd.add_argument("run_dir", help="运行目录")
    collect_cmd.add_argument("--provider", default="duckduckgo-html", help="duckduckgo-html | tavily | serper")
    collect_cmd.add_argument("--max-results", type=int, default=5)
    collect_cmd.add_argument("--max-documents", type=int, default=12)

    synth_cmd = subparsers.add_parser("synthesize", help="把 documents.jsonl 合成为 persona bundle。")
    synth_cmd.add_argument("target", help="target profile JSON")
    synth_cmd.add_argument("documents", help="documents.jsonl")
    synth_cmd.add_argument("output_bundle", help="persona bundle 输出路径")
    synth_cmd.add_argument("--model", help="OpenAI-compatible model name")

    render_cmd = subparsers.add_parser("render", help="把 persona bundle 渲染成仓库目录。")
    render_cmd.add_argument("bundle", help="persona bundle JSON")
    render_cmd.add_argument("output_root", help="输出根目录")

    generate_cmd = subparsers.add_parser("generate", help="串起来执行 collect -> synthesize -> render。")
    generate_cmd.add_argument("target", help="target profile JSON")
    generate_cmd.add_argument("run_dir", help="运行目录")
    generate_cmd.add_argument("output_root", help="输出根目录")
    generate_cmd.add_argument("--provider", default="duckduckgo-html", help="duckduckgo-html | tavily | serper")
    generate_cmd.add_argument("--max-results", type=int, default=5)
    generate_cmd.add_argument("--max-documents", type=int, default=12)
    generate_cmd.add_argument("--model", help="OpenAI-compatible model name")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "plan-queries":
        payload = plan_queries(args.target, args.output)
        print(f"planned {sum(len(group['queries']) for group in payload['query_pack'])} queries")
        return

    if args.command == "collect":
        payload = collect_sources(
            args.target,
            args.run_dir,
            provider_name=args.provider,
            max_results=args.max_results,
            max_documents=args.max_documents,
        )
        print(
            f"collected {len(payload['search_results'])} search hits and "
            f"{len(payload['documents'])} documents into {args.run_dir}"
        )
        return

    if args.command == "synthesize":
        bundle = synthesize_bundle(
            args.target,
            args.documents,
            args.output_bundle,
            model=args.model,
        )
        print(f"synthesized bundle for {bundle['slug']} -> {args.output_bundle}")
        return

    if args.command == "render":
        persona_dir = render_bundle(args.bundle, args.output_root)
        print(f"rendered {persona_dir}")
        return

    if args.command == "generate":
        persona_dir = generate_persona_materials(
            args.target,
            args.run_dir,
            args.output_root,
            provider_name=args.provider,
            max_results=args.max_results,
            max_documents=args.max_documents,
            model=args.model,
        )
        print(f"generated {persona_dir}")
        return

    parser.error(f"unknown command: {args.command}")
