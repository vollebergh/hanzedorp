import sys,re,html,json,http.cookiejar,urllib.request,urllib.parse
q=sys.argv[1]; order=sys.argv[2] if len(sys.argv)>2 else '1'; maxpages=int(sys.argv[3]) if len(sys.argv)>3 else 1
cj=http.cookiejar.CookieJar(); op=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
op.addheaders=[('User-Agent','Mozilla/5.0')]
h=op.open('https://olstwijhe.bestuurlijkeinformatie.nl/Search').read().decode()
tok=re.search(r'name="__RequestVerificationToken" type="hidden" value="([^"]+)"',h).group(1)
def parse(r):
    for p in re.split(r'<div class="panel"',r)[1:]:
        m=re.search(r'<a href="([^"]+)"[^>]*>(.*?)</a>',p,re.S)
        if not m: continue
        t=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',m.group(2)))).strip()
        sn=re.search(r'<p>(.*?)</p>',p,re.S); sn=html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',sn.group(1)))).strip() if sn else ''
        print('*',t,'|',html.unescape(m.group(1)),'\n   ',sn[:300])
for page in range(1,maxpages+1):
    data=urllib.parse.urlencode({'Query':q,'Page':str(page),'OrderBy':order,'__RequestVerificationToken':tok,'DateFrom':(sys.argv[4] if len(sys.argv)>4 else ''),'DateTo':(sys.argv[5] if len(sys.argv)>5 else '')}).encode()
    req=urllib.request.Request('https://olstwijhe.bestuurlijkeinformatie.nl/Search/Results',data=data,headers={'X-Requested-With':'XMLHttpRequest','RequestVerificationToken':tok})
    r=op.open(req).read().decode()
    n=re.search(r'(\d+ tot \d+ van \d+ resultaten)',r); print('==',q,'page',page,n.group(1) if n else '')
    parse(r)
    if n and re.search(r'van (\d+)',n.group(1)) and int(re.search(r'tot (\d+)',n.group(1)).group(1))>=int(re.search(r'van (\d+)',n.group(1)).group(1)): break
