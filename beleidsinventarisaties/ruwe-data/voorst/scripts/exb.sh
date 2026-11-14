#!/bin/bash
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/130.0.0.0 Safari/537.36'
D=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst
id=$1
curl -s -L -A "$UA" -o $D/src/$id.bin -w "%{http_code} %{content_type} %{size_download}\n" "https://repository.officiele-overheidspublicaties.nl/externebijlagen/$id/currentItem"
file $D/src/$id.bin | cut -c1-120
python3 -I $D/scripts/pdf2txt.py $D/src/$id.bin $D/src/$id.txt 2>&1 | tail -1
