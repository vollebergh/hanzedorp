#!/bin/bash
# usage: fetch.sh URL OUTFILE
curl -skL -m 60 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -o "$2" -w "%{http_code} %{size_download} %{content_type}\n" "$1"
