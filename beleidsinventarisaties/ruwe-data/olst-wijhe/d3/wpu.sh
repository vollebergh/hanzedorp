#!/bin/bash
# wpu.sh URL -> full text via WP API
url="$1"; host=$(echo "$url" | awk -F/ '{print $3}'); slug=$(echo "$url" | sed 's:/*$::' | awk -F/ '{print $NF}')
python3 /tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad/d3/wpfull.py "$host" "$slug"
