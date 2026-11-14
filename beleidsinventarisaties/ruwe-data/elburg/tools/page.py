#!/usr/bin/env python3
"""Haal een elburg.nl-pagina: hoofdtekst (vanaf <h1>) + lijst van links in de content. Gebruik: page.py URL"""
import sys,re,html
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/71b1cb0f-b448-4fa9-8f76-50a461e4c761/scratchpad/elburg/tools')
from fetch import fetch, html2text
url=sys.argv[1]
d,ct=fetch(url); t=d.decode('utf-8','replace')
i=t.find('<h1'); j=t.find('id="content-footer"')
body=t[i:j] if i>=0 else t
links=re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',body,re.S)
print(html2text(body))
print('\n--- LINKS ---')
seen=set()
for h,l in links:
    l=html2text(l)
    if h in seen: continue
    seen.add(h); print(h,'|',l[:80])
