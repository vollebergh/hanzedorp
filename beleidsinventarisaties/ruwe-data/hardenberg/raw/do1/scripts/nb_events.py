import json,urllib.request,urllib.parse,sys,os
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
out=sys.argv[1]
def get(url):
    r=urllib.request.Request(url,headers={'User-Agent':UA})
    return json.load(urllib.request.urlopen(r,timeout=60))
allev=[]
for (a,b) in [('2024-01-01','2024-06-30'),('2024-07-01','2024-12-31'),('2025-01-01','2025-06-30'),('2025-07-01','2025-12-31'),('2026-01-01','2026-06-30'),('2026-07-01','2026-12-31')]:
    q=urllib.parse.urlencode({'organisation':793,'date_from':a+' 00:00:00','date_to':b+' 23:59:59','format':'json'})
    d=get('https://api.notubiz.nl/events?'+q)
    ev=d['events']['event'] if d.get('events') else []
    if isinstance(ev,dict): ev=[ev]
    allev+=ev
    print(a,len(ev),file=sys.stderr)
json.dump(allev,open(out,'w'))
