import json,urllib.request,sys,os,time
UA="Mozilla/5.0 Chrome/130"
D=sys.argv[1]
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':UA})
    return json.load(urllib.request.urlopen(r,timeout=60))
rows=[]
def walk(items,mdate,gname,mid,path=''):
    for it in items:
        t=''
        for a in it.get('type_data',{}).get('attributes',[]):
            if a['id']==1: t=a['value']
        pref=it.get('type_data',{}).get('title_prefix','')
        for doc in it.get('documents',[]):
            rows.append(dict(date=mdate,gremium=gname,meeting=mid,item=f"{pref} {t}".strip(),doc_id=doc.get('id'),title=doc.get('title'),url=doc.get('url'),version=doc.get('version')))
        walk(it.get('agenda_items',[]),mdate,gname,mid)
for y in (2024,2025,2026):
    ev=json.load(open(f'{D}/events_{y}.json'))['events']
    for e in ev:
        mid=e['id']; fn=f'{D}/m_{mid}.json'
        if not os.path.exists(fn):
            try:
                m=get(f'https://api.notubiz.nl/events/meetings/{mid}?format=json&version=1.10.8'); json.dump(m,open(fn,'w'))
            except Exception as ex:
                print('ERR',mid,ex,file=sys.stderr); continue
        m=json.load(open(fn))['meeting']
        mdate=m['plannings'][0]['start_date'][:10] if m.get('plannings') else ''
        gname=next((a['value'] for a in m['attributes'] if a['id']==1),'')
        for doc in m.get('documents',[]):
            rows.append(dict(date=mdate,gremium=gname,meeting=mid,item='(vergadering)',doc_id=doc.get('id'),title=doc.get('title'),url=doc.get('url'),version=doc.get('version')))
        walk(m.get('agenda_items',[]),mdate,gname,mid)
json.dump(rows,open(f'{D}/docs_index.json','w'),ensure_ascii=False)
with open(f'{D}/docs_index.tsv','w') as f:
    for r in rows: f.write('\t'.join(str(r[k]) for k in ['date','gremium','item','doc_id','title','url'])+'\n')
print(len(rows))
