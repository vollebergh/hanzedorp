#!/bin/bash
# usage: gb.sh slug...  (voorst.nl news article body)
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
for s in "$@"; do
curl -sL -A "$UA" -o $D/src/g_$s.html "https://www.voorst.nl/nieuws/artikel/$s"
echo "######## $s"
python3 -I $D/h2t.py $D/src/g_$s.html | awk '/Altijd op de hoogte|Let op: dit is een nieuwsbericht/{f=1;next} f' | awk '/Delen:|Terug naar|Snel naar|Heeft u vragen/{exit} {print}' | grep -v '^\s*$' | cut -c1-1500 | head -${N:-60}
done
