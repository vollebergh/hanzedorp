import sys,pdfplumber
src,out=sys.argv[1],sys.argv[2]
parts=[]
with pdfplumber.open(src) as pdf:
    n=len(pdf.pages)
    for i,p in enumerate(pdf.pages):
        parts.append(f'\n--- pagina {i+1}/{n} ---\n'+(p.extract_text() or ''))
open(out,'w').write(''.join(parts)); print(n,'pagina\'s',sum(map(len,parts)),'tekens')
