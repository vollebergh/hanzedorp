import sys,pypdfium2 as pdfium
src,dst=sys.argv[1],sys.argv[2]
pdf=pdfium.PdfDocument(src)
out=[]
for i in range(len(pdf)):
    out.append(f'\n=====PAGE {i+1}=====\n'+pdf[i].get_textpage().get_text_range())
open(dst,'w').write(''.join(out))
print(src,len(pdf),'pages',sum(map(len,out)),'chars')
