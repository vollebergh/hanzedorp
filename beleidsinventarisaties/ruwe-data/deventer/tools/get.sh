#!/bin/bash
# usage: get.sh URL name [links]
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer
curl -sL --max-time 60 -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36" -o $D/raw3/html/$2.html -w "%{http_code} %{size_download}\n" "$1"
python3 -I $D/tools/h2t.py $D/raw3/html/$2.html $3 > $D/raw3/html/$2.txt
