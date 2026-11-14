#!/bin/bash
# usage: getpage.sh slug...
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
D=/home/nick/.local/share/hanzedorp-raalte/raw/do1/pages
for s in "$@"; do
  [ -s "$D/$s.html" ] || curl -s -A "$UA" -m 30 "https://www.raalte.nl/$s" -o "$D/$s.html"
  python3 -I /home/nick/.local/share/hanzedorp-raalte/raw/do1_tools/h2t.py "$D/$s.html" > "$D/$s.txt"
done
