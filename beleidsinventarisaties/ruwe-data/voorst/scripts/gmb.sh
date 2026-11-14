#!/bin/bash
# usage: gmb.sh gmb-2026-254967  -> src/<id>.html/.pdf/.txt
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst
id=$1
curl -s -L -A "$UA" -o $D/src/$id.html "https://zoek.officielebekendmakingen.nl/$id.html"
curl -s -L -A "$UA" -o $D/src/$id.pdf "https://zoek.officielebekendmakingen.nl/$id.pdf"
python3 -I $D/scripts/pdf2txt.py $D/src/$id.pdf $D/src/$id.pdf.txt 2>&1 | tail -1
python3 -I - $D/src/$id.html > $D/src/$id.html.txt <<'PY'
import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
m=re.search(r'<div class="(?:broodtekst|content)[^>]*>',s)
s=re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>','',s,flags=re.S)
s=re.sub(r'</(p|div|li|tr|h\d|table)>','\n',s)
s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
print(s)
PY
wc -c $D/src/$id.html.txt $D/src/$id.pdf.txt
