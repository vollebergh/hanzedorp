#!/bin/bash
# usage: cvdr.sh CVDR755433_1
id=$1; n=${id%_*}; v=${id#*_}
curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0.0.0 Safari/537.36" -o $id.xml "https://repository.officiele-overheidspublicaties.nl/cvdr/$n/$v/xml/$id.xml"
python3 -I - $id <<'P'
import sys,re,html
id=sys.argv[1]
t=open(id+'.xml',encoding='utf8',errors='ignore').read()
t=re.sub(r'<(/?)(al|titel|kop|nr|label|li|lid|artikel|sub|tr|p|para|intro|tekst)\b[^>]*>',r'\n',t)
t=re.sub(r'<[^>]+>',' ',t);t=html.unescape(t)
t=re.sub(r'[ \t]+',' ',t);t=re.sub(r'\n\s*\n+','\n',t)
open(id+'.txt','w').write(t);print(id,len(t.split()),'woorden')
P
