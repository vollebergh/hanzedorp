import sys,json,urllib.request,html
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
base=sys.argv[1]; after=sys.argv[2]
page=1; n=0
while True:
    u=f"{base}/wp-json/wp/v2/posts?per_page=100&page={page}&after={after}T00:00:00&_fields=id,date,link,title,excerpt"
    try:
        r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60)
    except Exception as e:
        print('END',e,file=sys.stderr);break
    d=json.load(r)
    if not d:break
    for p in d:
        print(p['date'][:10],'|',html.unescape(p['title']['rendered']),'|',p['link'])
        n+=1
    if len(d)<100:break
    page+=1
print('total',n,file=sys.stderr)
