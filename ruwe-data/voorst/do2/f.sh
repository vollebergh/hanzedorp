#!/bin/bash
# usage: f.sh url outfile  (browser UA)
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
curl -sL -A "$UA" -o "$2" -w "%{http_code} %{content_type} %{size_download} $1\n" "$1"
