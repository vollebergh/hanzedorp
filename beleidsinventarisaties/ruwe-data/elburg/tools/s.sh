#!/bin/bash
# usage: s.sh "query" [extra args]
cd /home/nick/Claude/Hanzedorp
export ORI_CACHE=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/71b1cb0f-b448-4fa9-8f76-50a461e4c761/scratchpad/elburg/ori
q="$1"; shift
python3 -I tools/ori.py --rate 20 search "$q" --org elburg --limit 25 "$@" 2>&1 | sed -e 's/document:ibabs:gemeente:elburg://' -e 's/meeting:ibabs:gemeente:elburg://'
