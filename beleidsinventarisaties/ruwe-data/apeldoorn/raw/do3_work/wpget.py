import sys,json,urllib.request,urllib.parse,html,re
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
def get(url):
    m=re.match(r'(https?://[^/]+)/(.*)',url)
    base=m.group(1); path=m.group(2).strip('/')
    slug=path.split('/')[-1]
    u=f"{base}/wp-json/wp/v2/posts?slug={urllib.parse.quote(slug)}&_fields=id,date,link,title,content"
    d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30))
    out=[]
    for p in d:
        t=re.sub(r'(?is)<(script|style).*?</\1>','',p['content']['rendered'])
        t=re.sub(r'(?i)<br\s*/?>|</p>|</li>|</h\d>','\n',t); t=re.sub(r'<[^>]+>','',t); t=html.unescape(t)
        out.append(f"### {html.unescape(p['title']['rendered'])} | {p['date'][:10]} | {p['link']}\n{t.strip()}\n")
    return '\n'.join(out) if out else f'NOT FOUND {url}\n'
for u in sys.argv[1:]: print(get(u))
