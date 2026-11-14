#!/bin/bash
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
cd /tmp/claude-1000/-home-nick-Claude-Hanzedorp/3c80c995-1808-47ef-a381-5857ae4d18ae/scratchpad/nunspeet/w
for s in "$@"; do echo "=========== https://www.nunspeet.nu/$s/"; [ -f c_$s.html ] || curl -sL -m 40 -A "$UA" "https://www.nunspeet.nu/$s/" -o c_$s.html; python3 -I ../art.py c_$s.html | cut -c1-1500; done
