import sys, pypdf
r=pypdf.PdfReader(sys.argv[1])
out=[]
for i,p in enumerate(r.pages,1):
    try: t=p.extract_text()
    except Exception as e: t='ERR '+str(e)
    out.append(f"\n=== PAGE {i} ===\n{t}")
open(sys.argv[2],'w').write(''.join(out))
print(len(r.pages))
