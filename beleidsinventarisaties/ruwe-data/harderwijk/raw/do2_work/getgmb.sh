#!/bin/bash
# haalt Gemeenteblad/Prb-publicatie op als pdf+html en extraheert tekst: getgmb.sh gmb-2026-392261
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
D="$(dirname "$0")/src"; mkdir -p "$D"
for id in "$@"; do
  curl -s -L -m 120 -A "$UA" "https://zoek.officielebekendmakingen.nl/$id.pdf" -o "$D/$id.pdf" -w "$id pdf %{http_code} %{size_download}\n"
  /home/nick/.venv/bin/python3 -I - "$D/$id.pdf" "$D/$id.txt" <<'PY'
import sys
try:
    import pdfplumber
    out=[]
    with pdfplumber.open(sys.argv[1]) as pdf:
        for p in pdf.pages: out.append(p.extract_text() or '')
    open(sys.argv[2],'w').write('\n'.join(out)); print('pages',len(out),'chars',sum(map(len,out)))
except Exception as e: print('ERR',e)
PY
done
