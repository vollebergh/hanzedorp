import requests, json, os, datetime
from concurrent.futures import ThreadPoolExecutor
os.chdir('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/raw')
H={'User-Agent':'Mozilla/5.0 Chrome/124'}
evs={}
d=datetime.date(2022,1,1)
while d<datetime.date(2026,10,12):
    e=(d.replace(day=1)+datetime.timedelta(days=32)).replace(day=1)
    r=requests.get('https://api.notubiz.nl/events',params={'organisation_id':438,'date_from':f'{d} 00:00:00','date_to':f'{e-datetime.timedelta(days=1)} 23:59:59','format':'json','version':'1.17.0'},headers=H,timeout=60)
    j=r.json()
    for ev in j.get('events',[]):
        evs[ev['id']]=ev
    d=e
print(len(evs))
json.dump(evs,open('nb_events.json','w'))
def det(i):
    fn=f'nb/ev_{i}.json'
    if os.path.exists(fn): return
    r=requests.get(f'https://api.notubiz.nl/events/meetings/{i}',params={'format':'json','version':'1.17.0'},headers=H,timeout=60)
    open(fn,'w').write(r.text)
with ThreadPoolExecutor(8) as ex: list(ex.map(det,list(evs)))
print('done')
