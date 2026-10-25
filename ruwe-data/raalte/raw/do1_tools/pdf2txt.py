import sys, pdfplumber
for f in sys.argv[1:]:
    out=f.rsplit('.',1)[0]+'.txt'
    with pdfplumber.open(f) as p, open(out,'w') as o:
        for i,pg in enumerate(p.pages,1):
            o.write(f'\n===== p.{i} =====\n'); o.write(pg.extract_text() or '')
    print(out, len(open(out).read()))
