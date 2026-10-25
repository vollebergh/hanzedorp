import sys, pdfplumber
with pdfplumber.open(sys.argv[1]) as pdf:
    out=[]
    for i,p in enumerate(pdf.pages):
        out.append(f"\n=== p{i+1} ===\n"+(p.extract_text() or ''))
open(sys.argv[2],'w').write(''.join(out))
print(len(pdf.pages) if False else 'ok')
