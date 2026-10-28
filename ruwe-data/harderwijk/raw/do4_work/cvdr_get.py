import sys,urllib.request,re,html
w=sys.argv[1]; v=sys.argv[2]; out=sys.argv[3]
url=f"https://repository.officiele-overheidspublicaties.nl/cvdr/{w}/{v}/xml/{w}_{v}.xml"
d=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read().decode('utf8','replace')
open(out+'.xml','w').write(d)
t=re.sub(r'</(al|titel|kop|nr|label|li|lid|artikel|tr|row|dt|dd|para|wat|intro|nootnr|gegevensgroep)>','\n',d)
t=re.sub(r'<[^>]+>',' ',t); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(out+'.txt','w').write(t)
print(len(t.split()),'woorden')
