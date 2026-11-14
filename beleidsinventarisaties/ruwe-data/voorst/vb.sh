#!/bin/bash
# usage: vb.sh url  -> prints article body only
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
for u in "$@"; do
n=$(echo "$u" | md5sum | cut -c1-10)
curl -sL -A "$UA" -o $D/src/b_$n.html "$u"
echo "######## $u"
python3 -I $D/h2t.py $D/src/b_$n.html | awk '{print} /^ *(maandag|dinsdag|woensdag|donderdag|vrijdag|zaterdag|zondag) +[0-9]+ [a-z]+ 20[0-9][0-9]/{exit}' | grep -v 'Facebook\|Twitter\|Print artikel\|Deel dit\|Advertentie\|^\s*$' | cut -c1-2500
done
