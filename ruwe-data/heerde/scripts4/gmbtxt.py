import sys,re,urllib.request,xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
out=sys.argv[1]
for pid in sys.argv[2:]:
    kind=pid.split('-')[0]
    year=pid.split('-')[1]
    u=f'https://repository.overheid.nl/frbr/officielepublicaties/{kind}/{year}/{pid}/1/xml/{pid}.xml'
    try:
        x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=90).read()
    except Exception as e:
        print(pid,'ERR',e); continue
    open(f'{out}/{pid}.xml','wb').write(x)
    root=ET.fromstring(x)
    lines=[]
    for e in root.iter():
        t=e.tag.split('}')[-1]
        if t=='row':
            cells=[re.sub(r'\s+',' ',''.join(en.itertext())).strip() for en in e if en.tag.split('}')[-1]=='entry']
            lines.append(' | '.join(cells))
        elif t in('al','kop'):
            s=re.sub(r'\s+',' ',''.join(e.itertext())).strip()
            if s: lines.append(s)
    txt='\n'.join(lines)
    open(f'{out}/{pid}.txt','w').write(txt)
    print(pid,len(txt))
