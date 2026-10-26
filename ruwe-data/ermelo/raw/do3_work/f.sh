#!/bin/bash
# f.sh URL [outfile] : curl with chrome UA, html -> text
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
curl -sL -m 60 -A "$UA" -H 'Accept-Language: nl' -w '\nHTTP:%{http_code} %{url_effective}\n' "$1" > ${2:-/tmp/f.out}
tail -1 ${2:-/tmp/f.out}
