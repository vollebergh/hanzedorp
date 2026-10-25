#!/bin/bash
# usage: g.sh gmb-2026-34752  -> raw/<id>.txt (html to text)
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/do2/raw
curl -sL -A "$UA" -o $D/$1.html "https://zoek.officielebekendmakingen.nl/$1.html"
python3 -I /tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/do2/h2t.py $D/$1.html > $D/$1.txt
wc -c $D/$1.txt
