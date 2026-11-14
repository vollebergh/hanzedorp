#!/bin/bash
# usage: g.sh <entityId-zonder-prefix> [--meeting]  -> bewaart in raw/do1_bronnen/ori_<id>.md en print kop
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/71b1cb0f-b448-4fa9-8f76-50a461e4c761/scratchpad/elburg
export ORI_CACHE=$W/ori
id="$1"; shift
cd /home/nick/Claude/Hanzedorp
python3 -I tools/ori.py --rate 20 get "document:ibabs:gemeente:elburg:$id" "$@" --out $W/raw/do1_bronnen 2>&1 | tail -3
