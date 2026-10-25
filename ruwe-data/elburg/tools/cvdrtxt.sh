#!/bin/bash
# usage: cvdrtxt.sh CVDR678774 1
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/71b1cb0f-b448-4fa9-8f76-50a461e4c761/scratchpad/elburg
for spec in "$@"; do
  id=${spec%%/*}; ver=${spec##*/}
  url="https://lokaleregelgeving.overheid.nl/$id/$ver"
  f=$W/raw/do1_bronnen/cvdr_${id}_$ver.txt
  echo "URL: $url (geraadpleegd 2026-10-24)" > $f
  /home/nick/.venv/bin/python3 -I $W/tools/fetch.py "$url" >> $f 2>&1
  echo "$spec: $(wc -c < $f) bytes"
done
