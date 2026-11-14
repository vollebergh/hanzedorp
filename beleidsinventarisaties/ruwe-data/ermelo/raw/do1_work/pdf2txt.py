import sys,pdfplumber
src,dst=sys.argv[1],sys.argv[2]
out=[]
with pdfplumber.open(src) as pdf:
    for i,p in enumerate(pdf.pages):
        out.append(f'--- pagina {i+1} ---\n'+(p.extract_text() or ''))
open(dst,'w').write('\n'.join(out))
print(src,len(pdf.pages) if False else len(out),'pagina\'s')
