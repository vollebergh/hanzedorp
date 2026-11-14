#!/bin/bash
# usage: getpub.sh id ...  -> raw4/pub/<id>.txt
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/c389bf58-3dd2-4443-a542-c4ae17b8d9b4/scratchpad/deventer
mkdir -p $D/raw4/pub
for id in "$@"; do
 if [ ! -s $D/raw4/pub/$id.html ]; then curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36" "https://zoek.officielebekendmakingen.nl/$id.html" -o $D/raw4/pub/$id.html; fi
 python3 -I $D/tools/h2t.py $D/raw4/pub/$id.html | grep -v "^\s*$" | sed -n '/Naar boven/q;p' | sed '1,/^ *Delen *$/d' > $D/raw4/pub/$id.txt
 echo "== $id $(wc -w < $D/raw4/pub/$id.txt) words"
done
