import sys,urllib.request,os
for idv in sys.argv[1:]:
    i,v=idv.replace('CVDR','').split('/')
    p=f'cvdr/CVDR{i}_{v}.xml'
    if os.path.exists(p): continue
    url=f'https://repository.officiele-overheidspublicaties.nl/cvdr/CVDR{i}/{v}/xml/CVDR{i}_{v}.xml'
    try:
        d=urllib.request.urlopen(url,timeout=120).read(); open(p,'wb').write(d); print(idv,len(d))
    except Exception as e: print(idv,'ERR',e)
