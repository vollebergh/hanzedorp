import json,subprocess,os
UA=open('ua.txt').read().strip()
ev=json.load(open('d1/notubiz/events.json'))
cand=[e for e in ev.values() if e['event_type_data'].get('agenda_item_count',0)>0]
items=[]
def walk(ai, mid, mdate, mname, parent=''):
    attrs={a['id']:a.get('value') for a in ai.get('type_data',{}).get('attributes',[])}
    title=attrs.get(1,'')
    pre=ai.get('type_data',{}).get('title_prefix') or ''
    docs=[{'id':d['id'],'title':d.get('title') or d.get('name'), 'url':d.get('url'),'self':d.get('self')} for d in ai.get('documents',[])]
    items.append({'meeting':mid,'date':mdate,'mname':mname,'prefix':pre,'title':title,'docs':docs,'text':attrs.get(3,'') if attrs.get(3) else '', 'parent':parent})
    for c in ai.get('agenda_items',[]): walk(c,mid,mdate,mname,title)
for e in sorted(cand,key=lambda e:e['plannings'][0]['start_date']):
    r=subprocess.run(['curl','-sL','-A',UA,'-H','Accept: application/json','--max-time','60',f"https://api.notubiz.nl/events/meetings/{e['id']}?format=json&version=1.10.8"],capture_output=True)
    try: j=json.loads(r.stdout.decode('utf8','replace'))
    except Exception as ex: print('ERR',e['id']); continue
    m=j.get('meeting')
    if not m: print('norights',e['id']); continue
    name=[a['value'] for a in m['attributes'] if a['id']==1]
    for ai in m.get('agenda_items',[]): walk(ai,e['id'],m['plannings'][0]['start_date'],name[0] if name else '')
    for d in m.get('documents',[]):
        items.append({'meeting':e['id'],'date':m['plannings'][0]['start_date'],'mname':name[0] if name else '','prefix':'DOC','title':d.get('title') or d.get('name'),'docs':[{'id':d['id'],'title':d.get('title'),'url':d.get('url'),'self':d.get('self')}],'text':'','parent':''})
json.dump(items,open('d1/notubiz/items.json','w'))
print(len(items))
