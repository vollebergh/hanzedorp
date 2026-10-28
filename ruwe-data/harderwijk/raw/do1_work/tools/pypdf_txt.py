import sys,pypdf
src,dst=sys.argv[1],sys.argv[2]
r=pypdf.PdfReader(src); out=[]
for i,p in enumerate(r.pages,1):
    try: t=p.extract_text() or ""
    except Exception as e: t="ERR "+str(e)
    out.append(f"\n=== p.{i} ===\n{t}")
open(dst,"w").write("".join(out)); print(len(r.pages),sum(map(len,out)))
