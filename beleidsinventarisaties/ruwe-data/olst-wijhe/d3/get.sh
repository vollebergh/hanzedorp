#!/bin/bash
# usage: get.sh <url> <name>  -> saves html to $D/<name>.html and text to $D/<name>.txt
S=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad
D=$S/d3
url="$1"; name="$2"
if [[ "$url" == *olst-wijhe.nl* ]]; then CA="--cacert $S/ow-ca.pem"; else CA=""; fi
code=$(curl -s -L $CA -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36" --max-time 60 -w "%{http_code}" "$url" -o $D/$name.raw)
echo "HTTP $code $(wc -c < $D/$name.raw) bytes"
if file $D/$name.raw | grep -q PDF; then
  python3 -c "import pdfplumber,sys; print('\n'.join((p.extract_text() or '') for p in pdfplumber.open(sys.argv[1]).pages))" $D/$name.raw > $D/$name.txt
else
  python3 $D/strip.py $D/$name.raw > $D/$name.txt
fi
wc -w $D/$name.txt
