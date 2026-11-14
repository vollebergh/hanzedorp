import sys, pypdf
for p in sys.argv[1:]:
    r = pypdf.PdfReader(p)
    out = "\n\n".join(f"--- p{i+1} ---\n" + (pg.extract_text() or "") for i, pg in enumerate(r.pages))
    open(p.rsplit('.',1)[0]+'.txt','w').write(out)
    print(p, len(r.pages), len(out.split()))
