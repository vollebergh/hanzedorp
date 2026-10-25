import sys,re,xml.etree.ElementTree as ET
for p in sys.argv[1:]:
    t=ET.parse(p).getroot()
    out=[]
    blocks={'al','titel','kop','li','entry','nr','tussenkop','label','th','td','p','title','identifier','creator','isRatifiedBy','issued','inwerkingtredingDatum','uitwerkingtredingDatum','isFormatOf','alternative','redactionele-correctie'}
    def walk(e):
        tag=e.tag.split('}')[-1]
        txt=''.join(e.itertext()).strip() if tag in blocks else None
        if txt is not None:
            out.append(('['+tag+'] ' if tag in ('identifier','creator','isRatifiedBy','issued','inwerkingtredingDatum','uitwerkingtredingDatum','isFormatOf','title','alternative') else '')+re.sub(r'\s+',' ',txt)); return
        for c in e: walk(c)
    walk(t)
    open(p.replace('.xml','.txt'),'w').write('\n'.join(out))
