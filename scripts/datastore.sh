#!/usr/bin/env bash
# Check out / push the `data` branch that holds collected data.
#
#   scripts/datastore.sh checkout DIR DAYS   shallow, sparse checkout: state, candidates, reports,
#                                            current monthly logs and the last DAYS days of raw files
#   scripts/datastore.sh checkout-market DIR shallow, sparse checkout of what the market job reads: candidates,
#                                            symbols, recent mention counts, market tables, the latest universe files
#   scripts/datastore.sh checkout-track DIR  shallow, sparse checkout of what the track job reads and writes: collection
#                                            state, candidates, market snapshots, mention counts and track/
#   scripts/datastore.sh checkout-label DIR  shallow, sparse checkout of what the label job reads and writes: collection
#                                            state, candidates, market snapshots, track/ and labels/
#   scripts/datastore.sh checkout-all DIR    shallow checkout of everything (for build-db)
#   scripts/datastore.sh push DIR MESSAGE    commit all changes and push, retrying if the branch moved
#
# In GitHub Actions it authenticates with GITHUB_TOKEN; DATASTORE_REMOTE overrides the remote (tests).
set -euo pipefail

BRANCH="${DATA_BRANCH:-data}"
REMOTE="${DATASTORE_REMOTE:-https://x-access-token:${GITHUB_TOKEN:-}@github.com/${GITHUB_REPOSITORY:-}.git}"

patterns() {
  # tomorrow too, for runs that check out just before midnight UTC
  local days="$1" i
  printf '%s\n' /state/ /ref/ /candidates/ /reports/ /README.md
  for i in $(seq -1 "$days"); do
    printf '/raw/reddit/%s/\n' "$(date -u -d "$((-i)) day" +%Y/%m/%d)"
    local m
    m="$(date -u -d "$((-i)) day" +%Y-%m)"
    printf '/logs/runs/%s.csv\n/daily/mention_counts/%s.csv\n/stocktwits/trending/%s.csv\n' "$m" "$m" "$m"
  done | sort -u
}

market_patterns() {
  # market/raw is write-only for the job, so it stays out; 9 days covers the universe file's price-date lag
  local i
  printf '%s\n' /ref/ /candidates/ /market/README.md /market/snapshots.csv /market/state.json
  for i in $(seq -1 9); do
    printf '/market/universe/%s.csv.gz\n' "$(date -u -d "$((-i)) day" +%Y/%m/%Y-%m-%d)"
    printf '/daily/mention_counts/%s.csv\n' "$(date -u -d "$((-i)) day" +%Y-%m)"
  done | sort -u
}

track_patterns() {
  printf '%s\n' /state/ /candidates/ /market/snapshots.csv /track/ /daily/mention_counts/
}

label_patterns() {
  printf '%s\n' /state/ /candidates/ /market/snapshots.csv /track/ /labels/
}

configure() {
  git -C "$1" config user.name "github-actions[bot]"
  git -C "$1" config user.email "41898282+github-actions[bot]@users.noreply.github.com"
}

branch_exists() {
  git ls-remote --exit-code --heads "$REMOTE" "$BRANCH" >/dev/null 2>&1
}

init_empty() {
  mkdir -p "$1"
  git -C "$1" init --quiet -b "$BRANCH"
  git -C "$1" remote add origin "$REMOTE"
}

cmd_checkout() {
  # DIR, then the command that prints the sparse-checkout patterns
  local dir="$1"
  shift
  if branch_exists; then
    git clone --quiet --depth 1 --filter=blob:none --no-checkout --branch "$BRANCH" "$REMOTE" "$dir"
    "$@" | git -C "$dir" sparse-checkout set --no-cone --stdin
    git -C "$dir" checkout --quiet "$BRANCH"
  else
    echo "data branch '$BRANCH' does not exist yet; starting an empty datastore"
    init_empty "$dir"
  fi
  configure "$dir"
}

cmd_checkout_all() {
  local dir="$1"
  if branch_exists; then
    git clone --quiet --depth 1 --branch "$BRANCH" "$REMOTE" "$dir"
  else
    echo "data branch '$BRANCH' does not exist yet"
    init_empty "$dir"
  fi
  configure "$dir"
}

cmd_push() {
  local dir="$1" msg="$2" attempt
  # --sparse: also stage new files outside the sparse checkout (files that are
  # merely not checked out are kept, not deleted)
  git -C "$dir" add -A --sparse
  if git -C "$dir" diff --cached --quiet; then
    echo "nothing to commit"
    return 0
  fi
  git -C "$dir" commit --quiet -m "$msg"
  for attempt in 1 2 3 4 5; do
    if git -C "$dir" push --quiet origin "HEAD:refs/heads/$BRANCH"; then
      echo "pushed $(git -C "$dir" rev-parse --short HEAD) to $BRANCH"
      return 0
    fi
    echo "push rejected (attempt $attempt); replaying this run's commit on the new branch tip"
    sleep $((attempt * 5))
    git -C "$dir" fetch --quiet --depth 1 origin "$BRANCH"
    if ! git -C "$dir" rebase --quiet --onto FETCH_HEAD HEAD~1; then
      git -C "$dir" rebase --abort || true
      echo "could not replay commit on top of $BRANCH" >&2
      return 1
    fi
  done
  return 1
}

case "${1:-}" in
  checkout) cmd_checkout "$2" patterns "$3" ;;
  checkout-market) cmd_checkout "$2" market_patterns ;;
  checkout-track) cmd_checkout "$2" track_patterns ;;
  checkout-label) cmd_checkout "$2" label_patterns ;;
  checkout-all) cmd_checkout_all "$2" ;;
  push) cmd_push "$2" "$3" ;;
  patterns) patterns "$2" ;;
  *) echo "usage: $0 {checkout DIR DAYS|checkout-market DIR|checkout-track DIR|checkout-label DIR|checkout-all DIR|push DIR MESSAGE|patterns DAYS}" >&2; exit 64 ;;
esac
