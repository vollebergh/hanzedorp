#!/bin/bash
# usage: f.sh URL name  -> src/name.txt
cd "$(dirname "$0")"
/home/nick/.venv/bin/python3 -I fetch.py "$1" > src/$2.txt 2>src/$2.err; wc -c src/$2.txt
