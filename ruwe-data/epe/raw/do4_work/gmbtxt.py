import sys,re,subprocess
sys.path.insert(0,'.')
ident=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 4000
import urllib.request,html
u=f"https://zoek.officielebekendmakingen.nl/{ident}.html"
d=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read().decode('utf8','replace')
open(f'src/{ident}.html','w').write(d)
t=re.sub(r'<script.*?</script>|<style.*?</style>','',d,flags=re.S)
t=re.sub(r'</(p|div|h\d|li|tr|dt|dd|table)>','\n',t)
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
k=t.find('Informatie\nPrinten')
if k<0: k=t.find('Delen\n')
open(f'src/{ident}.txt','w').write(t)
print(t[k:k+n])
