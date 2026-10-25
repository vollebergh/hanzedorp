#!/bin/bash
# usage: fetch.sh URL outfile  -> saves html + text
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
curl -s -A "$UA" -L --max-time 40 "$1" -o "$2.html"
/home/nick/.venv/bin/python3 -I - "$2.html" > "$2.txt" <<'PY'
import re,html,sys
t=open(sys.argv[1],encoding='utf8',errors='ignore').read()
t=re.sub(r'<(script|style|nav|header|footer)[^>]*>.*?</\1>','',t,flags=re.S)
t=re.sub(r'</(p|div|li|h\d|tr|br)>','\n',t)
t=re.sub(r'<[^>]+>','',t)
t=html.unescape(t)
t=re.sub(r'\n\s*\n+','\n',t)
print(t)
PY
wc -c "$2.txt"
