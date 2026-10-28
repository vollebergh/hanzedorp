#!/bin/bash
# s.sh "query" [date-from]  -> compact results
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/8432dfd2-fcf1-4f6d-b3b4-4a53f8cada05/scratchpad/harderwijk/raw/do1_work
export ORI_CACHE=$W/ori_cache
python3 -I $W/tools/ori.py search "$1" --org harderwijk --date-from "${2:-2020-01-01}" --limit ${3:-40} --sort date_desc 2>&1
