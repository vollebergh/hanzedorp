import sys,urllib.request,re,html
e=sys.argv[1]
u="https://data.rechtspraak.nl/uitspraken/content?id="+e
d=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"}),timeout=60).read().decode('utf8','replace')
t=re.sub(r'<[^>]+>',' ',d); t=html.unescape(t); t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open('src/'+e.replace(':','_')+'.txt','w').write(t)
print(e,len(t.split()))
