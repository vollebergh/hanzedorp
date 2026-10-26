import sys,pdfplumber
src,out=sys.argv[1],sys.argv[2]
parts=[]
with pdfplumber.open(src) as pdf:
    n=len(pdf.pages)
    for i,p in enumerate(pdf.pages):
        w,h=p.width,p.height
        if True:
            cols=[p.crop((0,0,w/2,h)),p.crop((w/2,0,w,h))]
        else: cols=[p]
        t='\n'.join((c.extract_text() or '') for c in cols)
        parts.append(f'\n--- pagina {i+1}/{n} ---\n'+t)
open(out,'w').write(''.join(parts)); print(n)
