#!/bin/bash
# ss.sh "query" [from-date] [limit]
cd /home/nick/Claude/Hanzedorp
python3 -I tools/ori.py search "$1" --org elburg --date-from "${2:-2021-01-01}" --limit "${3:-30}" --summary --sort date_desc 2>&1 | cut -c1-420
