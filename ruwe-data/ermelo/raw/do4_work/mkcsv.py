import json,csv,re
rows=json.load(open('cvdr_ermelo.json'))
g=lambda r,k:(r.get(k) or [''])[0]
by={}
for r in rows:
    m=re.match(r'(CVDR\d+)_(\d+)',g(r,'identifier'))
    w,v=m.group(1),int(m.group(2))
    by.setdefault(w,[]).append((v,r))
out=[]
for w,l in by.items():
    l.sort(key=lambda x:x[0]); v,r=l[-1]
    out.append([w,v,len(l),g(r,'title'),g(r,'alternative'),g(r,'type'),g(r,'issued'),g(r,'inwerkingtredingDatum'),g(r,'uitwerkingtredingDatum'),g(r,'modified'),g(r,'isRatifiedBy'),g(r,'isFormatOf'),g(r,'subject'),g(r,'onderwerp'),g(r,'omgevingswet'),g(r,'preferred_url').replace('/%d'%v,'')])
out.sort(key=lambda x:int(x[0][4:]))
with open('../do4_cvdr.csv','w',newline='') as f:
    wr=csv.writer(f); wr.writerow(['work','laatste_versie','aantal_versies','titel','alt_titel','type','issued','inwerking','uitwerking','modified','vastgesteld_door','bekendgemaakt_in(isFormatOf)','subject','onderwerp','omgevingswet','url'])
    wr.writerows(out)
print(len(out), 'werken;', len(rows),'records')
import datetime
t='2026-10-26'
act=[o for o in out if not o[8] or o[8]>t]
print('zonder/toekomstige uitwerking',len(act))
# non-Ermelo hints
for o in out:
    s=(o[3]+' '+o[4]+' '+o[11]).lower()
    if any(x in s for x in ['harderwijk','putten','nunspeet','barneveld','nijkerk','zeewolde','elburg','oldebroek','epe','apeldoorn']) and 'ermelo' not in s: print('HINT',o[0],o[3][:80],'|',o[11])
