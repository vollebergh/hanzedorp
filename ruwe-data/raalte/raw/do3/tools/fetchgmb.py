import sys,urllib.request,re,html,os
for idn in sys.argv[1:]:
    fn='gmb/'+idn+'.txt'
    if os.path.exists(fn): continue
    _,y,n=idn.split('-')
    u=f'https://repository.overheid.nl/frbr/officielepublicaties/gmb/{y}/{idn}/1/xml/{idn}.xml'
    try: x=urllib.request.urlopen(u,timeout=60).read().decode('utf-8','ignore')
    except Exception as e: print(idn,e); continue
    x=re.sub(r'<[^>]+>',' ',x); x=html.unescape(re.sub(r'\s+',' ',x)); open(fn,'w').write(x)
