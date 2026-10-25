#!/bin/bash
# usage: get.sh URL outname  -> dl/outname (raw) + txt/outname.txt (text)
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do1
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
curl -sL -A "$UA" -m 180 "$1" -o "$D/dl/$2" -w "%{http_code} %{content_type} %{size_download}\n"
python3 -I $D/scripts/totext.py "$D/dl/$2" "$D/txt/$2.txt"
