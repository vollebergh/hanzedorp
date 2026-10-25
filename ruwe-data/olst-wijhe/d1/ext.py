import sys,re,html
fn=sys.argv[1]
data=open(fn,'rb').read()
out=fn+'.txt'
if data[:4]==b'%PDF':
    import pdfplumber
    with pdfplumber.open(fn) as p:
        t='\n'.join(f'--- p{i+1} ---\n'+(pg.extract_text() or '') for i,pg in enumerate(p.pages))
else:
    s=data.decode('utf-8','replace')
    s=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>','',s)
    s=re.sub(r'(?is)<a [^>]*href="([^"]*)"[^>]*>(.*?)</a>',lambda m: m.group(2)+' [→'+m.group(1)+']',s)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>|</tr>|</div>','\n',s)
    s=re.sub(r'<[^>]+>',' ',s)
    s=html.unescape(s)
    s=re.sub(r'[ \t\r\xa0]+',' ',s)
    s=re.sub(r'\n\s*\n+','\n',s)
    t=s
open(out,'w').write(t)
print(fn, len(data), 'bytes ->', out, len(t), 'chars')
