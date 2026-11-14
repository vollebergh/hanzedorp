import sys,re,urllib.request,os,html
for id in sys.argv[1:]:
    p=f'gmb/{id}.txt'
    if os.path.exists(p): continue
    t,y,n=id.split('-')
    url=f'https://repository.overheid.nl/frbr/officielepublicaties/{t}/{y}/{id}/1/xml/{id}.xml'
    try:
        d=urllib.request.urlopen(url,timeout=120).read().decode('utf-8','replace')
    except Exception as e:
        print(id,'ERR',e); continue
    d=re.sub(r'<(/?)(al|titel|kop|li|tussenkop|p|entry|row|regeling-tekst|alinea)[^>]*>','\n',d)
    d=re.sub(r'<[^>]+>','',d); d=html.unescape(d); d=re.sub(r'\n\s*\n+','\n',d)
    open(p,'w').write(d.strip()); print(id,len(d))
