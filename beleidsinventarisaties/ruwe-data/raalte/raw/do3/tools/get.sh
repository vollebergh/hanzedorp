#!/bin/bash
# usage: get.sh URL OUTFILE
curl -sL --compressed -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "Accept-Language: nl-NL,nl;q=0.9" -o "$2" -w "%{http_code} $1\n" "$1"
