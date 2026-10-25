#!/bin/bash
# usage: cvdr.sh CVDRnnnn version
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/src
curl -s -L -A "$UA" -o $D/$1_$2.xml "https://repository.officiele-overheidspublicaties.nl/CVDR/$1/$2/xml/$1_$2.xml"
python3 -I - "$D/$1_$2.xml" > $D/$1_$2.txt <<'PY'
import sys,re,html
s=open(sys.argv[1],encoding='utf-8',errors='replace').read()
s=re.sub(r'<(/?)(al|lid|li|artikel|kop|titel|nr|label|tr|row|entry|p|sub|nootnoot)\b[^>]*>',lambda m:'\n' if m.group(1)=='/' or True else '',s)
s=re.sub(r'<[^>]+>',' ',s)
s=html.unescape(s)
s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
print(s)
PY
wc -c $D/$1_$2.txt
