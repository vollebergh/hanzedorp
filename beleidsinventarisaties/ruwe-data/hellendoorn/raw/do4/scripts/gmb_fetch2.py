import sys,re,urllib.request,os,html,time
for id in sys.argv[1:]:
    p=f'gmb/{id}.txt'
    if os.path.exists(p): continue
    t,y,n=id.split('-')
    url=f'https://repository.overheid.nl/frbr/officielepublicaties/{t}/{y}/{id}/1/xml/{id}.xml'
    for att in range(6):
        try:
            d=urllib.request.urlopen(url,timeout=120).read().decode('utf-8','replace'); break
        except Exception as e:
            print(id,'retry',e,file=sys.stderr); time.sleep(10*(att+1))
    else:
        print(id,'FAILED'); continue
    d=re.sub(r'<(/?)(al|titel|kop|li|tussenkop|p|entry|row|regeling-tekst|alinea)[^>]*>','\n',d)
    d=re.sub(r'<[^>]+>','',d); d=html.unescape(d); d=re.sub(r'\n\s*\n+','\n',d)
    open(p,'w').write(d.strip()); print(id,len(d)); time.sleep(1.5)
