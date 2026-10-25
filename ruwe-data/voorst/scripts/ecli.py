import sys,re,html,urllib.request
e=sys.argv[1]
r=urllib.request.Request('https://data.rechtspraak.nl/uitspraken/content?id='+e,headers={'User-Agent':'Mozilla/5.0'})
s=urllib.request.urlopen(r,timeout=60).read().decode('utf-8','replace')
s=re.sub(r'<[^>]+>','\n',s); s=html.unescape(s); s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
open('src/'+e.replace(':','_')+'.txt','w').write(s)
print(len(s))
