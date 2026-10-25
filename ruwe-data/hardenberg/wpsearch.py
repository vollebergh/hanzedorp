import json,subprocess,sys,urllib.parse,re,html,os
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
base=sys.argv[1]; outf=sys.argv[2]; terms=sys.argv[3:]
db=json.load(open(outf)) if os.path.exists(outf) else {}
for t in terms:
    page=1
    while True:
        u=base+'/wp-json/wp/v2/posts?'+urllib.parse.urlencode({'search':t,'per_page':100,'page':page,'after':'2024-01-01T00:00:00','_fields':'id,date,link,title,content'})
        r=subprocess.run(['curl','-s','-A',UA,u],capture_output=True,text=True).stdout
        try: d=json.loads(r)
        except Exception: print('ERR',t,r[:200]); break
        if not isinstance(d,list) or not d: break
        for p in d:
            txt=html.unescape(re.sub(r'<[^>]+>',' ',p['content']['rendered']))
            txt=' '.join(txt.split())
            k=str(p['id'])
            db.setdefault(k,{'date':p['date'],'link':p['link'],'title':html.unescape(p['title']['rendered']),'text':txt,'terms':[]})
            if t not in db[k]['terms']: db[k]['terms'].append(t)
        if len(d)<100: break
        page+=1
    print(t, sum(1 for v in db.values() if t in v['terms']))
json.dump(db,open(outf,'w'),ensure_ascii=False)
