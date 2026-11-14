import sys,json,urllib.request,urllib.parse,html
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
base=sys.argv[1]; terms=sys.argv[2:]
seen={}
for t in terms:
    for page in range(1,4):
        u=f"{base}/wp-json/wp/v2/pages?search={urllib.parse.quote(t)}&per_page=50&page={page}&_fields=id,date,modified,link,title"
        try: d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=30))
        except Exception as e: break
        for p in d: seen.setdefault(p['id'],(p['date'][:10],p['modified'][:10],html.unescape(p['title']['rendered']),p['link'],set()))[4].add(t)
        if len(d)<50:break
for id,(d,m,t,l,ts) in sorted(seen.items(), key=lambda x:x[1][1], reverse=True):
    print(d,m,'|',t,'|',l,'|',','.join(sorted(ts)))
