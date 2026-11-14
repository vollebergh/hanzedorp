import sys,re
for f in sys.argv[1:]:
    t=open(f,encoding='utf-8').read().split('\n')
    title=t[0].strip()
    out=[];on=False
    for l in t[1:]:
        s=l.strip()
        if re.match(r'^(Inhoud|Het plan|De plannen|Plan|Inhoud van het plan)$',s): on=True; continue
        if on and re.match(r'^(Inzien|Reageren|Het vervolg|Ter inzage|Inzage|Waar kunt u|Informatie|Wijzigingen|De locatie)',s): break
        if on: out.append(s)
    if not out: out=[x.strip() for x in t[1:8]]
    txt=' '.join(out)
    print('=== '+f.split('/')[-1].replace('.txt','')+' | '+title); print(txt[:1600]); print()
