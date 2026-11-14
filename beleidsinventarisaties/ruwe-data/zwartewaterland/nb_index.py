import json,glob,re,os
os.chdir('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/raw')
rows=[]
def walk(items,mid,mdate,gremium,depth=0):
    for it in items:
        td=it.get('type_data',{})
        title=None
        for a in td.get('attributes',[]):
            if a.get('id')==1 or a.get('label')=='Titel': title=a.get('value'); break
        docs=[(d.get('id'),d.get('title') or d.get('name') or '', d.get('url') or d.get('self')) for d in it.get('documents',[])]
        rows.append(dict(mid=mid,date=mdate,gremium=gremium,item=it.get('id'),title=title,docs=docs))
        walk(it.get('agenda_items',[]),mid,mdate,gremium,depth+1)
for f in glob.glob('nb/ev_*.json'):
    dd=json.load(open(f))
    if 'meeting' not in dd: continue
    m=dd['meeting']
    mid=m['id']
    pl=m.get('plannings',[{}])
    mdate=(pl[0].get('start_date') or '')[:10] if pl else ''
    gr=m.get('gremium',{}).get('id')
    # meeting-level docs
    for d in m.get('documents',[]):
        rows.append(dict(mid=mid,date=mdate,gremium=gr,item=None,title='[meeting doc]',docs=[(d.get('id'),d.get('title') or '',d.get('url') or d.get('self'))]))
    walk(m.get('agenda_items',[]),mid,mdate,gr)
json.dump(rows,open('nb_rows.json','w'),ensure_ascii=False)
print(len(rows))
kw=re.compile(r'provinc|buitengebied|agrarisch|VAB|vrijkomend|KGO|kwaliteitsimpuls|rood|woonvisie|woningbouw|woondeal|volkshuisvest|omgevingsvisie|omgevingsplan|Binnenveld|Overwaters|ontwikkellocatie|grondbeleid|erf|CPO|zelfbouw|kavel|Kamperzeedijk|Mastenbroek|Zwartsluis|Hasselt om|Weede|woning|stikstof|Natura|Wieden|zienswijze|ontwerp|TAM|principe',re.I)
out=[]
for r in sorted(rows,key=lambda r:r['date'],reverse=True):
    t=r['title'] or ''
    dt=' | '.join(d[1] for d in r['docs'])
    if kw.search(t) or kw.search(dt):
        out.append(f"{r['date']} m{r['mid']} i{r['item']} :: {t[:140]} :: {dt[:260]}")
open('nb_hits.txt','w').write('\n'.join(out))
print(len(out))
