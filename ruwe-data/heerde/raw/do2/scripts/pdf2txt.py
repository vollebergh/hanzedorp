import sys, pdfplumber
src,dst=sys.argv[1],sys.argv[2]
with pdfplumber.open(src) as pdf, open(dst,'w') as o:
    for i,p in enumerate(pdf.pages,1):
        o.write(f"\n\n=== PAGE {i} ===\n")
        try: o.write(p.extract_text() or '')
        except Exception as e: o.write(f'[ERR {e}]')
print(dst)
