#!/bin/bash
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
cd /tmp/claude-1000/-home-nick-Claude-Hanzedorp/3c80c995-1808-47ef-a381-5857ae4d18ae/scratchpad/nunspeet/w
for p in "$@"; do f=h_$(echo $p | tr '/' '_').html; echo "=========== https://www.nunspeethuisaanhuis.nl/$p"; [ -s $f ] || curl -sL -m 40 -A "$UA" "https://www.nunspeethuisaanhuis.nl/$p" -o $f; python3 -I ../hah.py $f; done
