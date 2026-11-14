#!/usr/bin/env python3
"""pdf.py <url> <uitvoerbestand>  : download pdf en extraheer tekst met pdfplumber"""
import sys, io, urllib.request, urllib.parse
import pdfplumber
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
url=sys.argv[1]; out=sys.argv[2]
u=urllib.parse.urlsplit(url); url=urllib.parse.urlunsplit((u.scheme,u.netloc,urllib.parse.quote(u.path),u.query,u.fragment))
data=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=120).read()
parts=[]
with pdfplumber.open(io.BytesIO(data)) as pdf:
    n=len(pdf.pages)
    for i,p in enumerate(pdf.pages):
        parts.append(f'\n--- pagina {i+1}/{n} ---\n'+(p.extract_text() or ''))
open(out,'w').write(f'BRON-URL: {sys.argv[1]}\n'+''.join(parts))
print(out, n, 'pagina\'s', sum(len(x) for x in parts), 'tekens')
