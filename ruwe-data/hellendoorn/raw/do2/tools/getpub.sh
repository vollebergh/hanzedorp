#!/bin/bash
# Haalt officiele publicaties (gmb-/prb-...) op als HTML en tekst. Gebruik: getpub.sh id ...  -> docs/pub/<id>.txt
T=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/do2
mkdir -p $T/docs/pub
for id in "$@"; do
 [ -s $T/docs/pub/$id.html ] || curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) Chrome/126" "https://zoek.officielebekendmakingen.nl/$id.html" -o $T/docs/pub/$id.html
 python3 -I $T/tools/h2t.py $T/docs/pub/$id.html > $T/docs/pub/$id.txt
 echo "== $id $(wc -w < $T/docs/pub/$id.txt) words"
done
