import json,re,sys,urllib.parse
rows=json.load(open('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/835c9923-b702-4c3d-931a-b64d86db2f73/scratchpad/ommen/raw/d1/ris/items.json'))
pat=re.compile(sys.argv[1],re.I)
mid=sys.argv[2] if len(sys.argv)>2 else None
seen=set()
for r in rows:
    if pat.search(r['item']) and (not mid or r['mid']==mid):
        k=(r['mid'],r['item'])
        if k in seen: continue
        seen.add(k)
        print('###',r['year'],r['mid'],r['mtitle'],'|',r['item'][:100])
        for u,nm in r['docs']: print('  ',urllib.parse.unquote(nm)[:80],'|',u.split('?')[0])
