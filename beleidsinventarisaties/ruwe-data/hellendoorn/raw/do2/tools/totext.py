import sys,re,html
src,dst=sys.argv[1],sys.argv[2]
b=open(src,'rb').read()
if b[:4]==b'%PDF':
    import pdfplumber
    out=[]
    with pdfplumber.open(src) as p:
        for i,pg in enumerate(p.pages):
            out.append(f"\n=== p.{i+1} ===\n"+(pg.extract_text() or ''))
    t=''.join(out)
else:
    t=b.decode('utf-8','ignore')
    t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>','',t)
    t=re.sub(r'(?is)<(br|/p|/div|/li|/h\d|/tr)[^>]*>','\n',t)
    t=re.sub(r'<[^>]+>',' ',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
open(dst,'w').write(t)
print(dst,len(t))
