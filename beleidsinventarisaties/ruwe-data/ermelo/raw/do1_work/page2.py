import sys,re,urllib.request,html as H
sys.path.insert(0,'.')
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
def get(url):
    return urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA,'Accept-Language':'nl'}),timeout=60).read().decode('utf8','replace')
def clean(t):
    t=re.sub(r'(?is)<(script|style|noscript|nav|footer|header)[^>]*>.*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>','\n',t)
    t=re.sub(r'(?i)</(p|div|li|h\d|tr|table|ul|ol|section)>','\n',t)
    t=re.sub(r'(?i)<li[^>]*>','- ',t)
    t=re.sub(r'<[^>]+>','',t); t=H.unescape(t)
    t=re.sub(r'[ \t\xa0]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
    return t.strip()
if __name__=='__main__':
    url=sys.argv[1]; h=get(url)
    m=re.search(r'(?is)<main.*?</main>',h)
    body=m.group(0) if m else h
    print('URL:',url,'(geraadpleegd 2026-10-26)')
    c=clean(body); c=c.split('Deel deze pagina')[0]; print(c)
    links=re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>',body,re.S)
    seen=set()
    print('\n--- LINKS ---')
    for u,tx in links:
        tx=re.sub(r'<[^>]+>','',tx).strip()
        if (u,tx) in seen or not tx or re.search(r'facebook|bsky|linkedin|twitter|mailto|readspeaker|^/$',u) or tx in ('Lees voor',): continue
        seen.add((u,tx)); print(tx[:80],'|',H.unescape(u))
