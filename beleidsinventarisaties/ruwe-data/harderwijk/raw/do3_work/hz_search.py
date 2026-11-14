import sys,re,html,urllib.request,urllib.parse,json
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
def search(q):
    d=urllib.parse.urlencode({'q':q}).encode()
    t=urllib.request.urlopen(urllib.request.Request('https://www.harderwijksezaken.nl/zoeken',data=d,headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','replace')
    m=re.search(r'<main.*?</main>',t,re.S)
    body=m.group(0) if m else t
    res=[]
    for h,l in re.findall(r'<a[^>]+href="(https://www.harderwijksezaken.nl/nieuws/[^"]+)"[^>]*>(.*?)</a>',body,re.S):
        l=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',l))).strip()
        res.append((h,l[:140]))
    seen=set();out=[]
    for h,l in res:
        if h in seen: continue
        seen.add(h);out.append((h,l))
    return out
if __name__=='__main__':
    for q in sys.argv[1:]:
        r=search(q); print('##',q,len(r))
        for h,l in r: print(h.split('/nieuws/')[1][:90],'|',l)
