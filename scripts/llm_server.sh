#!/usr/bin/env bash
# Start llama.cpp's server with the llm-v1 model (docs/stage5.md) on 127.0.0.1, for the model workflow's LLM
# ratings: an open-weights model on the runner itself, so no account, key or paid service is involved.
#
# Downloads the pinned llama.cpp build and model file into LLM_DIR (default ~/llm, which the workflow caches)
# unless they are already there, starts the server in the background and waits until it answers.
#
# Usage: scripts/llm_server.sh
# Needs LLAMA_CPP (a llama.cpp release tag), LLM_REPO, LLM_REVISION and LLM_FILE (a GGUF file on Hugging Face).
set -euo pipefail

dir="${LLM_DIR:-$HOME/llm}"
port="${LLM_PORT:-8080}"
build="$dir/llama-$LLAMA_CPP"
mkdir -p "$dir"

if [ ! -d "$build" ]; then
  mkdir -p "$build.part"
  curl -fsSL --retry 3 "https://github.com/ggml-org/llama.cpp/releases/download/$LLAMA_CPP/llama-$LLAMA_CPP-bin-ubuntu-x64.tar.gz" \
    | tar -xz -C "$build.part"
  mv "$build.part" "$build"
fi
if [ ! -s "$dir/$LLM_FILE" ]; then
  curl -fsSL --retry 3 -o "$dir/$LLM_FILE.part" "https://huggingface.co/$LLM_REPO/resolve/$LLM_REVISION/$LLM_FILE"
  mv "$dir/$LLM_FILE.part" "$dir/$LLM_FILE"
fi

server="$(find "$build" -name llama-server -type f -print -quit)"
if [ -z "$server" ]; then
  echo "::error::no llama-server in llama.cpp $LLAMA_CPP"
  exit 1
fi
# one request at a time, with room for the longest prompt (about 4,000 tokens) and the answer; --jinja runs the
# model's own chat template, which is what reads the request's chat_template_kwargs (thinking off)
LD_LIBRARY_PATH="$(dirname "$server")${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}" nohup "$server" -m "$dir/$LLM_FILE" \
  --host 127.0.0.1 --port "$port" -c 8192 -np 1 -t "$(nproc)" --jinja > "$dir/server.log" 2>&1 &
pid=$!

for _ in $(seq 1 150); do
  if curl -sf "http://127.0.0.1:$port/health" > /dev/null; then
    echo "llama.cpp $LLAMA_CPP is serving $LLM_FILE on port $port"
    exit 0
  fi
  kill -0 "$pid" 2> /dev/null || break  # it exited
  sleep 2
done
echo "::warning::the LLM server did not come up"
tail -n 40 "$dir/server.log"
exit 1
