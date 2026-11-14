import sys,pdfplumber
src,dst=sys.argv[1],sys.argv[2]
ncol=int(sys.argv[3]) if len(sys.argv)>3 else 2
out=[]
with pdfplumber.open(src) as pdf:
    for i,p in enumerate(pdf.pages):
        w,h=p.width,p.height
        t=[]
        if ncol==1: t.append(p.extract_text() or '')
        else:
            for c in range(ncol):
                b=p.crop((w*c/ncol,0,w*(c+1)/ncol,h))
                t.append(b.extract_text() or '')
        out.append(f'--- pagina {i+1} ---\n'+'\n'.join(t))
open(dst,'w').write('\n'.join(out))
print(len(out))
