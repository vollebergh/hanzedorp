import sys,pdfplumber
p=pdfplumber.open(sys.argv[1])
print("pages",len(p.pages))
for i,pg in enumerate(p.pages,1):
    t=pg.extract_text() or ''
    print(f"\n=== p{i} chars={len(t)} images={len(pg.images)}")
    print(t)
