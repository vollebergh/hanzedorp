import json,sys,urllib.request,re,os
import xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
recs=json.load(open(sys.argv[1])); outdir=sys.argv[2]
byid={}
for d in recs:
    b,_,v=d['identifier'].partition('_'); byid.setdefault(b,[]).append(d)
for cid in sys.argv[3:]:
    ds=sorted(byid[cid],key=lambda d:int(d['identifier'].split('_')[1])); d=ds[-1]
    url=d.get('publicatieurl_xml')
    x=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=120).read()
    open(f'{outdir}/{d["identifier"]}.xml','wb').write(x)
    root=ET.fromstring(x)
    # text with block breaks
    parts=[]
    def walk(e):
        tag=e.tag.split('}')[-1]
        if e.text and e.text.strip(): parts.append(e.text.strip())
        for c in e: walk(c)
        if tag in ('al','titel','kop','li','artikel','regeling-tekst','row','entry','nr','lid','tussenkop','divisie'): parts.append('\n')
        if e.tail and e.tail.strip(): parts.append(e.tail.strip())
    walk(root)
    t=' '.join(parts); t=re.sub(r' *\n *','\n',t); t=re.sub(r'\n{3,}','\n\n',t)
    open(f'{outdir}/{d["identifier"]}.txt','w').write(t)
    print(d['identifier'],len(t.split()),'woorden',d.get('creator'),url)
