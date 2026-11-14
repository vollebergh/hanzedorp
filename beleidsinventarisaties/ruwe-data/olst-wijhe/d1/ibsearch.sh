#!/bin/bash
# usage: ibsearch.sh "query" outname [orderby]
cd /tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad/d1
curl -s -A "Mozilla/5.0" -X POST "https://olstwijhe.bestuurlijkeinformatie.nl/Search/Results" -H "X-Requested-With: XMLHttpRequest" --data-urlencode "Query=$1" --data "Page=1&OrderBy=${3:-1}" -o "$2"
python3 - "$2" <<'P'
import sys,json,re,html
d=open(sys.argv[1]).read()
try:
    j=json.loads(d); print(type(j), list(j.keys())[:10] if isinstance(j,dict) else len(j)); d=json.dumps(j,ensure_ascii=False)[:3000]; print(d)
except Exception as e:
    s=re.sub(r'<[^>]+>',' ',d); s=html.unescape(s); s=re.sub(r'\s+',' ',s); print(s[:4000])
    for m in re.finditer(r'href="([^"]+)"',d): print(m.group(1))
P
