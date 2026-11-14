#!/bin/bash
# usage: art.sh URL name  (curl with retry on 403, saves text of article)
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
for i in 1 2 3 4 5 6; do
  code=$(curl -s -o "art_$2.html" -w '%{http_code}' -A "$UA" -L --max-time 40 "$1")
  [ "$code" = "200" ] && break
  sleep 12
done
echo "$2 $code"
/home/nick/.venv/bin/python3 -I - "art_$2.html" > "art_$2.txt" <<'PY'
import re,html,sys
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>','',t,flags=re.S)
m=re.search(r'<h1.*?(?=Lees ook|Meest gelezen)',t,flags=re.S)
t=m.group(0) if m else t
t=re.sub(r'</(p|div|li|h\d|tr|br)>','\n',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n',t)
print(t.strip())
PY
