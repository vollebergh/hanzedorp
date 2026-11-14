#!/bin/bash
# usage: oget.sh <uuid> <name> [--meeting]
cd /home/nick/Claude/Hanzedorp
python3 -I tools/ori.py get "document:ibabs:gemeente:oldebroek:$1" > /tmp/claude-1000/-home-nick-Claude-Hanzedorp/3dd1ee33-930f-4a23-bfbf-795635d03f68/scratchpad/oldebroek/raw/do1_src/ori/$2.md 2>&1
wc -w /tmp/claude-1000/-home-nick-Claude-Hanzedorp/3dd1ee33-930f-4a23-bfbf-795635d03f68/scratchpad/oldebroek/raw/do1_src/ori/$2.md
