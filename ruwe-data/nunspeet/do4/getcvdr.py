import sys,json,urllib.request,re
import xml.etree.ElementTree as ET
UA=open('ua.txt').read().strip()
r=json.load(open('cvdr_all.json'))
lat={}
for d in r:
    i=d['identifier'][0]; wk,v=i.split('_'); v=int(v)
    if wk not in lat or v>lat[wk][0]: lat[wk]=(v,d)
def fetch(wk,v=None):
    if v is None: v=lat[wk][0]
    url=f'https://repository.officiele-overheidspublicaties.nl/cvdr/{wk}/{v}/xml/{wk}_{v}.xml'
    x=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=90).read()
    root=ET.fromstring(x)
    out=[]
    def walk(e):
        t=e.tag.split('}')[-1]
        if t in('kop','titel','nr','label'): pass
        txt=(e.text or '').strip()
        if txt: out.append(txt)
        for c in e:
            walk(c)
            if c.tail and c.tail.strip(): out.append(c.tail.strip())
        if t in('al','lid','artikel','kop','li','tr','titel','head','p'): out.append('\n')
    walk(root)
    s=' '.join(out); s=re.sub(r' *\n *','\n',s); s=re.sub(r'\n{2,}','\n\n',s)
    open(f'{wk}_{v}.txt','w').write(s)
    return url,len(s)
for wk in sys.argv[1:]:
    wk,_,v=wk.partition(':')
    try: print(wk,fetch(wk,int(v) if v else None))
    except Exception as e: print(wk,'ERR',e)
