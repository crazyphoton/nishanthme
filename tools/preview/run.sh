#!/usr/bin/env bash
# Local preview with an in-page edit-suggestion overlay. LOCAL DEV ONLY —
# never run as part of the production build (see overlay_server.py header).
#
# Usage: tools/preview/run.sh   then open http://localhost:8080/
# Requires Hugo >= 0.160 (repo/CI pin is 0.163.3) and python3.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
HUGO_PORT="${HUGO_PORT:-1313}"
PREVIEW_PORT="${PREVIEW_PORT:-8080}"

cleanup() { kill "${HUGO_PID:-}" "${PROXY_PID:-}" 2>/dev/null || true; }
trap cleanup EXIT INT TERM

cd "$REPO_ROOT"
hugo server -D --disableLiveReload --bind 127.0.0.1 --port "$HUGO_PORT" \
  --baseURL "http://localhost:${PREVIEW_PORT}/" --appendPort=false &
HUGO_PID=$!

PREVIEW_PORT="$PREVIEW_PORT" HUGO_URL="http://127.0.0.1:${HUGO_PORT}" \
  python3 "$REPO_ROOT/tools/preview/overlay_server.py" &
PROXY_PID=$!

echo "Preview + edit overlay: http://localhost:${PREVIEW_PORT}/  (Ctrl-C to stop)"
wait
