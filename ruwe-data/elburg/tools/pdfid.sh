#!/bin/bash
# usage: pdfid.sh <id> -> pdf_<id>.txt (volledige pdfplumber-extractie) via downloadUrl in de md
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/71b1cb0f-b448-4fa9-8f76-50a461e4c761/scratchpad/elburg
cd $W/raw/do1_bronnen
for id in "$@"; do
  md=$(ls document_ibabs_gemeente_elburg_${id}*.md 2>/dev/null | head -1)
  [ -z "$md" ] && { $W/tools/g.sh $id >/dev/null; md=$(ls document_ibabs_gemeente_elburg_${id}*.md | head -1); }
  url=$(grep -m1 '^downloadUrl:' "$md" | sed 's/^downloadUrl: "//; s/"$//')
  /home/nick/.venv/bin/python3 -I $W/tools/pdf.py "$url" pdf_${id:0:8}.txt 2>&1 | tail -1
done
