import sys,pdfplumber
src,dst=sys.argv[1],sys.argv[2]
cuts=[float(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else None
out=[]
with pdfplumber.open(src) as pdf:
    for i,p in enumerate(pdf.pages):
        W=p.width
        cs=cuts if cuts else [W/4,W/2,3*W/4]
        edges=[0]+[c for c in cs if c<W]+[W]
        txt=[]
        for a,b in zip(edges,edges[1:]):
            t=p.crop((a,0,b,p.height)).extract_text() or ''
            if t.strip(): txt.append(t)
        out.append(f"\n=== p.{i+1} ===\n"+"\n---col---\n".join(txt))
open(dst,'w').write(''.join(out))
