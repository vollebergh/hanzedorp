import sys,pypdf
r=pypdf.PdfReader(sys.argv[1])
open(sys.argv[2],'w').write('\n=====PAGE=====\n'.join((p.extract_text() or '') for p in r.pages))
print(sys.argv[1],len(r.pages))
