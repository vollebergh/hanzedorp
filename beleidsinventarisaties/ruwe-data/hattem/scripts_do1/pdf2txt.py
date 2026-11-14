import sys, pdfplumber
src,out=sys.argv[1],sys.argv[2]
with pdfplumber.open(src) as pdf:
    parts=[]
    for i,pg in enumerate(pdf.pages):
        parts.append(f'\n=== p{i+1} ===\n'+(pg.extract_text() or ''))
open(out,'w').write(''.join(parts)); print(len(pdf.pages) if False else 'ok', sum(len(x) for x in parts))
