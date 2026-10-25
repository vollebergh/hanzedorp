import sys,pdfplumber
src,dst=sys.argv[1],sys.argv[2]
out=[]
with pdfplumber.open(src) as p:
    for i,pg in enumerate(p.pages,1):
        w,h=pg.width,pg.height
        txt=''
        if w>h*1.2:  # landscape: two columns
            for box in ((0,0,w/2,h),(w/2,0,w,h)):
                txt+=(pg.crop(box).extract_text() or '')+'\n'
        else:
            txt=pg.extract_text() or ''
        out.append(f'\n=====PAGE {i}=====\n'+txt)
open(dst,'w').write(''.join(out))
print(src,len(out),'pages',w,h)
