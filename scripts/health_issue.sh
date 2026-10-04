#!/usr/bin/env bash
# Keep one GitHub issue open while the collector is unhealthy (GitHub emails
# the repo owner when it opens) and close it when health recovers.
#
# Usage: scripts/health_issue.sh path/to/health.json
# Needs GH_TOKEN (issues: write, actions: read) and the gh CLI. RUN_STATUS is
# this job's status so far; when it isn't "success" the health report on disk is
# the previous run's, so only repeated failed runs count.
set -euo pipefail

file="${1:?health.json path}"
label="collector-health"
run_url="${GITHUB_SERVER_URL:-https://github.com}/${GITHUB_REPOSITORY:-}/actions/runs/${GITHUB_RUN_ID:-}"
open_issue="$(gh issue list --state open --label "$label" --json number --jq '.[0].number // empty' 2>/dev/null || true)"

alert() {
  local problems="$1"
  if [ -n "$open_issue" ]; then
    echo "health issue #$open_issue already open"
    return 0
  fi
  gh label create "$label" --color B60205 --description "Automated collector health alerts" 2>/dev/null || true
  gh issue create --title "Collector health check failing" --label "$label" --body "The collector's health check is failing:

$problems

Latest run: $run_url

This issue closes itself when collection is healthy again."
}

if [ "${RUN_STATUS:-success}" != "success" ]; then
  # earlier finished runs, newest first; cancelled (superseded) runs don't count either way
  failed_before="$(gh run list --workflow collect.yml --limit 20 --json status,conclusion \
    --jq '[.[] | select(.status == "completed" and .conclusion != "cancelled" and .conclusion != "skipped")][:2] | map(select(.conclusion == "failure")) | length' \
    2>/dev/null || echo 0)"
  if [ "${failed_before:-0}" -ge 2 ]; then
    alert "- 3 collection runs in a row failed; see the run logs."
  else
    echo "run failed; alerting only after 3 failures in a row"
  fi
  exit 0
fi

[ -f "$file" ] || { echo "no health report"; exit 0; }
healthy="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["healthy"])' "$file")"
if [ "$healthy" = "False" ]; then
  alert "$(python3 -c 'import json,sys; print("\n".join("- " + p for p in json.load(open(sys.argv[1]))["problems"]))' "$file")"
else
  if [ -n "$open_issue" ]; then
    gh issue close "$open_issue" --comment "Collector is healthy again (run ${GITHUB_RUN_ID:-?})."
  fi
  echo "healthy"
fi
