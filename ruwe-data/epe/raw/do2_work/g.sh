#!/bin/bash
# usage: g.sh ID [ID...] -> docs/document_notubiz_gemeente_epe_<ID>.md
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/cbd7d9f0-97a4-45cc-923f-0df0e26b9a22/scratchpad/epe/raw/do2_work
export ORI_CACHE=$W/ori
cd /home/nick/Claude/Hanzedorp
for id in "$@"; do python3 -I tools/ori.py --rate 40 get document:notubiz:gemeente:epe:$id --out $W/docs 2>&1 | tail -1; done
