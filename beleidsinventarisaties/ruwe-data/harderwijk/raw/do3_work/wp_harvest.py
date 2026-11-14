# Harvest WP REST API search results (Veluwe FM / RTV Harderwijk) - eigen script do3
import sys,json,urllib.request,urllib.parse,time,re,html
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
base=sys.argv[1]; out=sys.argv[2]; terms=sys.argv[3:]
seen={}
try:
    for l in open(out): d=json.loads(l); seen[d['id']]=d
except FileNotFoundError: pass
f=open(out,'a')
for t in terms:
    page=1;n=0
    while True:
        u=f"{base}/wp-json/wp/v2/posts?search={urllib.parse.quote(t)}&per_page=100&page={page}&after=2024-01-01T00:00:00&_fields=id,date,link,title,content,excerpt"
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA}),timeout=60)
            data=json.loads(r.read()); tp=int(r.headers.get('X-WP-TotalPages','1'))
        except Exception as e:
            print(t,page,'ERR',e); break
        for d in data:
            if d['id'] in seen: continue
            txt=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',d['content']['rendered'])))
            rec={'id':d['id'],'date':d['date'],'link':d['link'],'title':html.unescape(d['title']['rendered']),'text':txt,'term':t}
            seen[d['id']]=rec; f.write(json.dumps(rec,ensure_ascii=False)+'\n'); n+=1
        if page>=tp: break
        page+=1; time.sleep(0.5)
    print(t,'new',n,flush=True)
