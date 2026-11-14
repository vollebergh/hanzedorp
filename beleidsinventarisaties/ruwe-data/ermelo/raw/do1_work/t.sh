#!/bin/bash
# usage: t.sh URL slug  -> web/slug.txt
D=$(dirname "$0")
echo "URL: $1 (geraadpleegd 2026-10-26)" > $D/web/$2.txt
/home/nick/.venv/bin/python3 -I $D/fetch.py "$1" >> $D/web/$2.txt 2>&1
wc -c $D/web/$2.txt
