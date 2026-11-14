#!/usr/bin/env python3
"""usage: get.py name url  -> src/name.raw + src/name.txt"""
import sys, subprocess, os, io
S=os.path.dirname(os.path.abspath(__file__))+'/src'
os.makedirs(S,exist_ok=True)
name,url=sys.argv[1],sys.argv[2]
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36'
raw=f'{S}/{name}.raw'
r=subprocess.run(['curl','-sL','-A',UA,'-H','Accept-Language: nl-NL,nl;q=0.9','--max-time','120','-o',raw,'-w','%{http_code} %{content_type}',url],capture_output=True,text=True)
code=r.stdout
data=open(raw,'rb').read()
if data[:4]==b'%PDF':
    import pdfplumber
    out=[]
    with pdfplumber.open(raw) as pdf:
        for i,p in enumerate(pdf.pages):
            out.append(f'\n=== p{i+1} ===\n'+(p.extract_text() or ''))
    txt=''.join(out)
else:
    from bs4 import BeautifulSoup
    soup=BeautifulSoup(data,'html.parser')
    for t in soup(['script','style','noscript','svg']): t.decompose()
    txt=soup.get_text('\n')
    txt='\n'.join(l.strip() for l in txt.splitlines() if l.strip())
open(f'{S}/{name}.txt','w').write(txt)
print(name,code,len(data),'bytes ->',len(txt),'chars')
