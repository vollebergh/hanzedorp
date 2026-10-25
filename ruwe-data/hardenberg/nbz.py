import json,subprocess,sys,os,time
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
out=sys.argv[1]
def get(u):
    r=subprocess.run(['curl','-s','-A',UA,u],capture_output=True,text=True).stdout
    try: return json.loads(r)
    except Exception: return None
evs=[]
for (a,b) in [('2024-01-01','2024-06-30'),('2024-07-01','2024-12-31'),('2025-01-01','2025-06-30'),('2025-07-01','2025-12-31'),('2026-01-01','2026-06-30'),('2026-07-01','2026-10-15')]:
    page=1
    while True:
        d=get(f'https://api.notubiz.nl/events?organisation_id=793&date_from={a}%2000:00:00&date_to={b}%2023:59:59&format=json&version=1.10.8&page={page}')
        if not d: break
        evs+=d['events']
        if not d['pagination']['has_more_pages']: break
        page+=1
print('events',len(evs))
res=[]
for e in evs:
    if e.get('type')!='meeting': continue
    m=get(f"https://api.notubiz.nl/events/meetings/{e['id']}?format=json&version=1.10.8")
    if not m: continue
    res.append(m)
json.dump(res,open(out,'w'),ensure_ascii=False)
print('meetings',len(res))
