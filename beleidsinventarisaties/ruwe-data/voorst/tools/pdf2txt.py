import sys, pdfplumber
src, dst = sys.argv[1], sys.argv[2]
out=[]
with pdfplumber.open(src) as pdf:
    for i,p in enumerate(pdf.pages,1):
        out.append(f"\n=== PAGE {i} ===\n"+(p.extract_text() or ""))
open(dst,"w").write("".join(out))
