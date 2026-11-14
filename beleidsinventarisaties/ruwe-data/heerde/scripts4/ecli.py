import sys,re,urllib.request
UA='Mozilla/5.0 Chrome/130'
for e in sys.argv[2:]:
    u='https://data.rechtspraak.nl/uitspraken/content?id='+e
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60).read()
    open(f'{sys.argv[1]}/{e.replace(":","_")}.xml','wb').write(x)
    t=re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',x.decode('utf8')))
    open(f'{sys.argv[1]}/{e.replace(":","_")}.txt','w').write(t); print(e,len(t))
