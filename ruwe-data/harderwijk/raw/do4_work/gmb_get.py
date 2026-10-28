import sys,subprocess,re,html
ident=sys.argv[1]; out=sys.argv[2]
import urllib.request
u=f"https://zoek.officielebekendmakingen.nl/{ident}.html"
d=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read().decode('utf8','replace')
open(out+'.html','w').write(d)
t=re.sub(r'<script.*?</script>|<style.*?</style>','',d,flags=re.S)
t=re.sub(r'</(p|div|h\d|li|tr|dt|dd|table)>','\n',t)
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
i=t.find('Authentieke versie')
open(out+'.txt','w').write(t)
print(len(t.split()))
