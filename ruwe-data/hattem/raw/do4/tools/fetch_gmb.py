import sys,urllib.request,re,html
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
out=sys.argv[1]
for i in sys.argv[2:]:
    url=f'https://zoek.officielebekendmakingen.nl/{i}.html'
    try:
        h=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=120).read().decode('utf8','replace')
    except Exception as e:
        print(i,'ERR',e); continue
    m=re.search(r'<div[^>]*id="broodtekst".*',h,re.S)
    b=m.group(0) if m else h
    b=re.sub(r'(?s)<(script|style).*?</\1>','',b)
    b=re.sub(r'<(br|/p|/h\d|/li|/tr|/div)[^>]*>','\n',b); b=re.sub(r'<[^>]+>',' ',b)
    b=html.unescape(b); b=re.sub(r'[ \t]+',' ',b); b=re.sub(r'\n\s*\n+','\n',b)
    open(f'{out}/{i}.txt','w').write(b)
    pdfs=set(re.findall(r'href="([^"]+\.pdf)"',h))
    print(i,len(b.split()),'woorden; pdf-links:',list(pdfs)[:5])
