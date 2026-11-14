import json, subprocess, sys, datetime, os
UA=open('ua.txt').read().strip()
def get(url):
    r=subprocess.run(['curl','-sL','-A',UA,'-H','Accept: application/json','--max-time','60',url],capture_output=True)
    return json.loads(r.stdout.decode('utf8','replace'))
out={}
start=datetime.date(2022,6,1); end=datetime.date(2026,12,31)
d=start
while d<end:
    nd=(d.replace(day=1)+datetime.timedelta(days=32)).replace(day=1)
    url=f"https://api.notubiz.nl/events?organisation_id=742&date_from={d} 00:00:00&date_to={nd-datetime.timedelta(days=1)} 23:59:59&format=json&version=1.10.8".replace(' ','%20')
    try:
        j=get(url)
        for e in j.get('events',[]):
            out[e['id']]=e
    except Exception as ex:
        print('ERR',d,ex)
    d=nd
json.dump(out,open('d1/notubiz/events.json','w'))
print(len(out))
