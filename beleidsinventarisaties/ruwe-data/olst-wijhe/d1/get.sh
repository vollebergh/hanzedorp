#!/bin/bash
# usage: get.sh url name  -> downloads to name, if pdf extracts name.txt, if html strips to name.txt
S=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad
cd $S/d1
curl -s -L --max-time 90 --cacert $S/ow-ca.pem -A "Mozilla/5.0 (X11; Linux x86_64)" "$1" -o "$2"
python3 $S/d1/ext.py "$2"
