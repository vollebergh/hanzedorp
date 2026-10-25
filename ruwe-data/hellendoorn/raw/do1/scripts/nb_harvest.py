import json,urllib.request,urllib.parse,sys,os
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
D=sys.argv[1]; ORG=2952
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':UA})
    return json.load(urllib.request.urlopen(r,timeout=90))
allev=[]
for y in range(2022,2027):
  for (a,b) in [(f'{y}-01-01',f'{y}-06-30'),(f'{y}-07-01',f'{y}-12-31')]:
    q=urllib.parse.urlencode({'organisation_id':ORG,'date_from':a+' 00:00:00','date_to':b+' 23:59:59','format':'json','version':'1.10.8'})
    try: d=get('https://api.notubiz.nl/events?'+q)
    except Exception as e: print('ERR',a,e,file=sys.stderr); continue
    ev=d.get('events') or []
    if isinstance(ev,dict): ev=[ev]
    allev+=ev; print(a,len(ev),file=sys.stderr)
json.dump(allev,open(f'{D}/events.json','w'))
rows=[]
def walk(items,mdate,gname,mid):
    for it in items:
        t=''
        for a in it.get('type_data',{}).get('attributes',[]):
            if a['id']==1: t=a['value']
        pref=it.get('type_data',{}).get('title_prefix','')
        for doc in it.get('documents',[]):
            rows.append(dict(date=mdate,gremium=gname,meeting=mid,item=f"{pref} {t}".strip(),doc_id=doc.get('id'),title=doc.get('title'),url=doc.get('url'),version=doc.get('version')))
        walk(it.get('agenda_items',[]),mdate,gname,mid)
for e in allev:
    mid=e.get('id'); fn=f'{D}/m_{mid}.json'
    if not os.path.exists(fn):
        try:
            m=get(f'https://api.notubiz.nl/events/meetings/{mid}?format=json&version=1.10.8'); json.dump(m,open(fn,'w'))
        except Exception as ex:
            print('ERR',mid,ex,file=sys.stderr); continue
    m=json.load(open(fn))['meeting']
    mdate=m['plannings'][0]['start_date'][:10] if m.get('plannings') else ''
    gname=next((a['value'] for a in m.get('attributes',[]) if a['id']==1),'')
    for doc in m.get('documents',[]):
        rows.append(dict(date=mdate,gremium=gname,meeting=mid,item='(vergadering)',doc_id=doc.get('id'),title=doc.get('title'),url=doc.get('url'),version=doc.get('version')))
    walk(m.get('agenda_items',[]),mdate,gname,mid)
json.dump(rows,open(f'{D}/docs_index.json','w'),ensure_ascii=False)
with open(f'{D}/docs_index.tsv','w') as f:
    for r in rows: f.write('\t'.join(str(r[k]) for k in ['date','gremium','item','doc_id','title','url'])+'\n')
print(len(allev),len(rows))
