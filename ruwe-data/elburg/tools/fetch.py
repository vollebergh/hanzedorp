#!/usr/bin/env python3
import sys, re, html, urllib.request, ssl
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
def fetch(url, binary=False):
    req=urllib.request.Request(url, headers={'User-Agent':UA,'Accept-Language':'nl'})
    with urllib.request.urlopen(req, timeout=60) as f:
        data=f.read(); ct=f.headers.get('Content-Type','')
    return data, ct
def html2text(t):
    t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'(?i)</(p|div|li|h\d|tr|table|ul|ol|section)>','\n',t)
    t=re.sub(r'(?i)<li[^>]*>','- ',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n\n',t)
    return t.strip()
if __name__=='__main__':
    url=sys.argv[1]
    data,ct=fetch(url)
    if 'pdf' in ct.lower() or url.lower().endswith('.pdf') or data[:4]==b'%PDF':
        import io, pdfplumber
        out=[]
        with pdfplumber.open(io.BytesIO(data)) as pdf:
            for i,p in enumerate(pdf.pages):
                out.append(f'--- pagina {i+1} ---\n'+(p.extract_text() or ''))
        print('\n'.join(out))
    else:
        print(html2text(data.decode('utf-8','replace')))
