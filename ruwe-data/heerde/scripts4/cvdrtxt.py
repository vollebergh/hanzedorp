import sys, re, urllib.request, os
import xml.etree.ElementTree as ET
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
outdir=sys.argv[1]
def fetch(cid,ver):
    n=cid.replace('CVDR','')
    u=f'https://repository.officiele-overheidspublicaties.nl/cvdr/{cid}/{ver}/xml/{cid}_{ver}.xml'
    x=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=90).read()
    open(f'{outdir}/{cid}_{ver}.xml','wb').write(x)
    root=ET.fromstring(x)
    lines=[]
    def txt(e): return ''.join(e.itertext())
    def walk(e,depth=0):
        tag=e.tag.split('}')[-1]
        if tag in('kop','titel','label','nr'): return
        if tag in ('al','lid','li','tekst'):
            pass
        for c in e:
            ct=c.tag.split('}')[-1]
            if ct=='kop':
                lines.append('\n'+re.sub(r'\s+',' ',txt(c)).strip())
            elif ct in('al','tekst','titel') and tag!='kop':
                s=re.sub(r'\s+',' ',txt(c)).strip()
                if s: lines.append(s)
            elif ct=='table' or ct=='tgroup':
                for row in c.iter():
                    if row.tag.split('}')[-1]=='row':
                        cells=[re.sub(r'\s+',' ',''.join(en.itertext())).strip() for en in row if en.tag.split('}')[-1]=='entry']
                        lines.append(' | '.join(cells))
            else:
                walk(c,depth+1)
    walk(root)
    t='\n'.join(lines)
    open(f'{outdir}/{cid}_{ver}.txt','w').write(t)
    return t
for a in sys.argv[2:]:
    cid,ver=a.split('/')
    t=fetch(cid,ver); print(a,len(t))
