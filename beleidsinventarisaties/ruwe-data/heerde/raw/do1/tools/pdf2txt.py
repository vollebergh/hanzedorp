import sys,pdfplumber
src,dst=sys.argv[1],sys.argv[2]
out=[]
with pdfplumber.open(src) as p:
    for i,pg in enumerate(p.pages,1):
        out.append(f'\n=====PAGE {i}=====\n'+(pg.extract_text() or ''))
open(dst,'w').write(''.join(out))
print(src,len(out),'pages',sum(map(len,out)),'chars')
