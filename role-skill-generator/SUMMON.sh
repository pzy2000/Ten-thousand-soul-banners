#!/bin/zsh
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
WORKSPACE_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

ROLE_NAME="${1:-}"
ROLE_DESCRIPTION="${2:-}"
RESEARCH_BIAS="${3:-}"

if [[ -z "$ROLE_NAME" ]]; then
  printf "角色名称: "
  read -r ROLE_NAME
fi

if [[ -z "$ROLE_DESCRIPTION" ]]; then
  printf "角色描述: "
  read -r ROLE_DESCRIPTION
fi

if [[ -z "$RESEARCH_BIAS" ]]; then
  printf "资料偏向 (humor/serious/comprehensive): "
  read -r RESEARCH_BIAS
fi

case "$RESEARCH_BIAS" in
  humor|serious|comprehensive)
    ;;
  *)
    echo "无效偏向: $RESEARCH_BIAS"
    echo "只接受 humor、serious、comprehensive"
    exit 1
    ;;
esac

# Document fetches default to skipping TLS cert verification (see providers.py).
# To enforce verification: ROLE_SKILL_FETCH_INSECURE_SSL=0 or SUMMON_FETCH_VERIFY_SSL=1
if [[ "${SUMMON_FETCH_VERIFY_SSL:-}" == "1" ]]; then
  export ROLE_SKILL_FETCH_INSECURE_SSL=0
fi

PROVIDER="${ROLE_SKILL_PROVIDER:-duckduckgo-html}"
if [[ -n "${TAVILY_API_KEY:-}" && "$PROVIDER" == "duckduckgo-html" ]]; then
  PROVIDER="tavily"
fi

cd "$SCRIPT_DIR"
PYTHONPATH=src python3 -m role_skill_generator summon \
  "$ROLE_NAME" \
  "$ROLE_DESCRIPTION" \
  "$RESEARCH_BIAS" \
  --workspace-root "$WORKSPACE_ROOT" \
  --runs-root "$SCRIPT_DIR/runs" \
  --provider "$PROVIDER"
