import sys, pdfplumber
src,out=sys.argv[1],sys.argv[2]
res=[]
with pdfplumber.open(src) as pdf:
    for i,p in enumerate(pdf.pages):
        w,h=p.width,p.height
        if w>h:  # landscape: two columns
            l=p.crop((0,0,w/2,h)).extract_text() or ''
            r=p.crop((w/2,0,w,h)).extract_text() or ''
            res.append(f'\n=== p{i+1} L ===\n{l}\n=== p{i+1} R ===\n{r}')
        else:
            res.append(f'\n=== p{i+1} ===\n'+(p.extract_text() or ''))
open(out,'w').write(''.join(res))
