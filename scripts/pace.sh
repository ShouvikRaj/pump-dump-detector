#!/usr/bin/env bash
# Start the next collect run. The `pace` workflow calls this after the `pacer`
# environment's wait timer, so runs follow each other about every 15 minutes
# even when GitHub's cron doesn't fire.
#
# Does nothing when a collect run is already queued or running (that run queues
# the next pacer itself), and stops the chain when the last collect run started
# less than 10 minutes ago: that means the wait timer is missing, and without it
# the chain would restart collect every couple of minutes.
#
# Then it queues the next pacer itself as well, so a collect run that GitHub never
# gives a runner (it happened 2026-10-05 19:43 UTC and stopped collection for an
# hour) can't break the chain: collect -> pacer and pacer -> pacer both keep it
# going, and the `pace` concurrency group keeps it to one pacer at a time. It
# skips that when this pacer itself waited under 10 minutes (no wait timer).
#
# The nightly build's cron is just as unreliable, so this also starts it once a
# day, at the first pacer after 03:41 UTC, unless one already ran since then;
# likewise Stage 3's track run after 22:41 UTC and Stage 4's label run after
# 23:21 UTC (40 minutes later, so it labels from that day's tracking).
#
# Usage: scripts/pace.sh
# Needs GH_TOKEN (actions: write), GH_REPO, the gh CLI and jq.
set -euo pipefail

min_gap="${PACE_MIN_GAP_SECONDS:-600}"
retry_delay="${PACE_RETRY_DELAY:-10}"
now="${PACE_NOW:-$(date +%s)}"

start_daily_if_due() {
  # WORKFLOW HOUR MINUTE: start the workflow once a day, at the first pacer after HH:MM UTC
  local wf="$1" slot last
  slot=$(( now - now % 86400 + $2 * 3600 + $3 * 60 ))
  [ "$now" -ge "$slot" ] || return 0
  last="$(gh run list --workflow "$wf" --limit 1 --json createdAt --jq '.[0].createdAt // empty')"
  if [ -n "$last" ] && [ "$(jq -rn --arg t "$last" '$t | fromdateiso8601')" -ge "$slot" ]; then
    return 0
  fi
  if gh workflow run "$wf" --ref main; then
    echo "started today's $wf run"
  else
    echo "::warning::could not start $wf"
  fi
}

start_daily_if_due nightly.yml 3 41 || echo "::warning::nightly check failed"
start_daily_if_due track.yml 22 41 || echo "::warning::track check failed"
start_daily_if_due label.yml 23 21 || echo "::warning::label check failed"

queue_next_pacer() {
  local created waited
  created="$(gh api "repos/$GH_REPO/actions/runs/${GITHUB_RUN_ID:?}" --jq .created_at)" || return 1
  waited=$(( now - $(jq -rn --arg t "$created" '$t | fromdateiso8601') ))
  if [ "$waited" -lt "$min_gap" ]; then
    echo "::warning::this pacer waited only ${waited}s, so the pacer environment's wait timer seems to be missing; not queueing another"
    return 0
  fi
  gh workflow run pace.yml --ref main && echo "queued the next pacer"
}

start_collect() {
  local runs age attempt
  runs="$(gh run list --workflow collect.yml --limit 10 --json status,createdAt)"
  if [ "$(jq '[.[] | select(.status != "completed")] | length' <<<"$runs")" -gt 0 ]; then
    echo "a collect run is already queued or running; it queues the next pacer"
    return 0
  fi

  age="$(jq --argjson now "$now" 'if length == 0 then null else $now - (.[0].createdAt | fromdateiso8601) end' <<<"$runs")"
  if [ "$age" != "null" ] && [ "$age" -lt "$min_gap" ]; then
    echo "::warning::the last collect run started ${age}s ago, so the pacer environment's wait timer seems to be missing; not starting another (the cron still runs)"
    return 0
  fi

  for attempt in 1 2 3; do
    if gh workflow run collect.yml --ref main -f max_minutes=12; then
      echo "started the next collect run"
      return 0
    fi
    if [ "$attempt" -lt 3 ]; then sleep "$retry_delay"; fi
  done
  echo "::error::could not start the next collect run"
  return 1
}

status=0
start_collect || status=1
queue_next_pacer || echo "::warning::could not queue the next pacer"
exit "$status"
