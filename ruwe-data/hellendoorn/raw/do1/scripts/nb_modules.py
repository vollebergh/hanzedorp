import json,urllib.request,sys,os
UA="Mozilla/5.0 Chrome/130"
D=sys.argv[1]
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':UA})
    return json.load(urllib.request.urlopen(r,timeout=90))
rows=[]
for mid in [1,5,6,12,18,19]:
    seen=set(); page=1
    while page<60:
        d=get(f'https://api.notubiz.nl/organisations/2952/modules/{mid}/items?format=json&page={page}')
        items=d.get('item',[]) if isinstance(d,dict) else []
        if isinstance(items,dict): items=[items]
        new=0
        for it in items:
            iid=it['@attributes']['id']
            if iid in seen: continue
            seen.add(iid); new+=1
            r={'module':mid,'id':iid,'docs':[]}
            for a in it['attributes']['attribute']:
                v=a.get('value', a.get('values'))
                if isinstance(v,dict) and 'url' in v: r['docs'].append((a['label'],v['title'],v['url']))
                else: r[a['label']]=v if not isinstance(v,dict) else json.dumps(v,ensure_ascii=False)
            rows.append(r)
        if not isinstance(d,dict): break
        tot=d.get('pagination',{}).get('@attributes',{}).get('total_results')
        print(mid,page,len(items),new,tot,file=sys.stderr)
        if new==0 or len(seen)>=int(tot or 0): break
        page+=1
json.dump(rows,open(f'{D}/modules_items.json','w'),ensure_ascii=False)
with open(f'{D}/modules_items.tsv','w') as f:
    for r in rows:
        f.write('\t'.join([str(r['module']),str(r.get('Datum','')),str(r.get('Nummer','')),str(r.get('Onderwerp','')).replace('\n',' '),str(r.get('Status','') or r.get('Afhandeling','')),' || '.join(f"{l}: {t} <{u}>" for l,t,u in r['docs'])])+'\n')
print(len(rows))
