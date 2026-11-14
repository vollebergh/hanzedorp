import sys,re,xml.etree.ElementTree as ET
blocks={'Al','Opschrift','Kop','Term','Definitie','LiNummer','Bijschrift','Titel','Entry','entry'}
for p in sys.argv[1:]:
    t=ET.parse(p).getroot(); out=[]
    def walk(e):
        tag=e.tag.split('}')[-1]
        if tag in ('Kop',):
            out.append('## '+re.sub(r'\s+',' ',' '.join(x.strip() for x in e.itertext() if x.strip()))); return
        if tag in ('Al','Definitie','Term','Bijschrift','entry','Entry'):
            out.append(re.sub(r'\s+',' ',''.join(e.itertext())).strip()); return
        if tag=='LiNummer':
            out.append('- '+(e.text or '').strip()); return
        if tag in ('Illustratie',): out.append('[illustratie '+e.get('naam','')+']'); return
        for c in e: walk(c)
    walk(t)
    open(p.replace('.xml','.txt'),'w').write('\n'.join(x for x in out if x))
