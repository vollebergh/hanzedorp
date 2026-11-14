#!/bin/bash
# usage: nbdoc.sh docid/ver outname
UA=$(cat /tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/ua.txt)
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/d1/nbdocs
mkdir -p $D
curl -sL -A "$UA" --max-time 120 -o $D/$2.bin -w "$2 %{http_code} %{size_download} %{content_type}\n" "https://api.notubiz.nl/document/$1"
if file $D/$2.bin | grep -q PDF; then python3 -I /tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/tools/pdf2txt.py $D/$2.bin $D/$2.txt; wc -w $D/$2.txt; fi
