#!/bin/bash
# usage: get.sh URL outname  -> dl/outname (raw) + txt/outname.txt (text)
D=/home/nick/.local/share/hanzedorp-hardenberg/raw/do1
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
curl -sL -A "$UA" -m 120 "$1" -o "$D/dl/$2"
python3 -I $D/scripts/totext.py "$D/dl/$2" "$D/txt/$2.txt"
