import sys, pdfplumber
src=sys.argv[1]; ncol=int(sys.argv[2]); pages=[int(x) for x in sys.argv[3].split(',')]
with pdfplumber.open(src) as pdf:
    for n in pages:
        p=pdf.pages[n-1]; w=p.width; h=p.height
        print(f"\n######## PAGE {n}")
        for c in range(ncol):
            box=(c*w/ncol,0,(c+1)*w/ncol,h)
            t=p.crop(box).extract_text() or ''
            print(f"--- col {c+1}\n{t}")
