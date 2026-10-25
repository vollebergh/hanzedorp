#!/bin/bash
# usage: vnsearch.sh keyword
cd /tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/src
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
rm -f cj.txt
curl -sL -A "$UA" -c cj.txt -o vh.html https://www.voorsternieuws.nl/
python3 -I - "$1" <<'P'
import re,sys,subprocess,urllib.parse
h=open('vh.html',encoding='utf8').read()
m=re.search(r'<form method="post" action="https://www.voorsternieuws.nl/"\s*>(.*?)<form class="navbar-form"',h,re.S).group(1)
fields=dict(re.findall(r'name="([^"]+)" value="([^"]*)"',m))
fields['keywords']=sys.argv[1]
args=['curl','-sL','-A','Mozilla/5.0 (X11; Linux x86_64) Chrome/130','-b','cj.txt','-c','cj.txt','-o','sr.html','-w','%{http_code} %{url_effective}\n']
for k,v in fields.items(): args+=['--data-urlencode',f'{k}={v}']
args.append('https://www.voorsternieuws.nl/')
print(subprocess.run(args,capture_output=True,text=True).stdout)
P
python3 -I ../h2t.py sr.html | head -${2:-80}
