#!/bin/bash
# usage: savepages.sh path1 path2 ... (elburg.nl paden zonder domein)
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/71b1cb0f-b448-4fa9-8f76-50a461e4c761/scratchpad/elburg
for p in "$@"; do
  f=$W/raw/do1_bronnen/elburgnl_$(echo "$p" | tr / _).txt
  echo "URL: https://www.elburg.nl/$p (geraadpleegd 2026-10-24)" > "$f"
  /home/nick/.venv/bin/python3 -I $W/tools/page.py "https://www.elburg.nl/$p" >> "$f" 2>&1
  echo "== $p : $(wc -c < "$f") bytes"
done
