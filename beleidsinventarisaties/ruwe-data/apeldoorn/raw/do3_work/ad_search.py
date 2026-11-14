import sys, json, urllib.request, urllib.parse, html
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
base=sys.argv[1]  # e.g. https://www.apeldoorndirect.nl
after=sys.argv[2] # 2024-01-01
terms=sys.argv[3:]
seen={}
for t in terms:
    for page in range(1,6):
        u=f"{base}/wp-json/wp/v2/posts?search={urllib.parse.quote(t)}&per_page=50&page={page}&orderby=date&order=desc&after={after}T00:00:00&_fields=id,date,link,title"
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30)
            d=json.load(r)
        except Exception as e:
            print('ERR',t,page,e,file=sys.stderr);break
        for p in d:
            seen.setdefault(p['id'],(p['date'][:10],html.unescape(p['title']['rendered']),p['link'],set()))[3].add(t)
        if len(d)<50:break
for id,(d,t,l,ts) in sorted(seen.items(), key=lambda x:x[1][0], reverse=True):
    print(d,'|',t,'|',l,'|',','.join(sorted(ts)))
