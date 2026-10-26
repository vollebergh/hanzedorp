import re,html,sys,time,urllib.request
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
out=open('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/10db2ce5-cf65-46a7-800e-29355f749163/scratchpad/ermelo/raw/do3_ermelonl/newslist.tsv','w')
seen=set()
for n in range(1,int(sys.argv[1])+1):
    url='https://www.ermelo.nl/nieuws/nieuwspagina/%d'%n
    try:
        t=urllib.request.urlopen(urllib.request.Request(url,headers={'User-Agent':UA}),timeout=60).read().decode('utf-8','replace')
    except Exception as e:
        print(n,'ERR',e); break
    items=re.findall(r'<a[^>]+href="(/nieuws/(?!nieuwspagina)[^"]+)"[^>]*>(.*?)</a>',t,re.S)
    # dates
    cnt=0
    for h,l in items:
        if h in seen: continue
        seen.add(h)
        l=re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>','',l))).strip()
        out.write(f'{n}\t{h}\t{l[:150]}\n'); cnt+=1
    print(n,cnt,flush=True)
    if cnt==0: break
    time.sleep(0.7)
