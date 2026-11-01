import sys,re,html,urllib.parse,json,os
sys.path.insert(0,'.')
from fetch import fetch, html2text
cache='va_cache.json'
C=json.load(open(cache)) if os.path.exists(cache) else {}
MON={'jan':1,'feb':2,'mrt':3,'apr':4,'mei':5,'jun':6,'jul':7,'aug':8,'sep':9,'okt':10,'nov':11,'dec':12}
def meta(u):
    if u in C: return C[u]
    try: d,_=fetch(u)
    except Exception as e: return None
    t=d.decode('utf-8','replace')
    body=html2text(t)
    m=re.search(r'door Redactie \| (\w+) (\d+), (\d{4})',body)
    ti=re.search(r'<title>(.*?)</title>',t,re.S)
    dt='%s-%02d-%02d'%(m.group(3),MON.get(m.group(1)[:3].lower(),0),int(m.group(2))) if m else '?'
    i=body.find('door Redactie'); j=body.find('Laatste nieuws',i)
    C[u]={'date':dt,'title':html.unescape(ti.group(1)).strip() if ti else '?','body':body[i:j][:4000]}
    json.dump(C,open(cache,'w'))
    return C[u]
for q in sys.argv[1:]:
    res=[]
    for pg in (1,2):
        url='https://www.vaassenactief.nl/'+('page/%d/'%pg if pg>1 else '')+'?s='+urllib.parse.quote_plus(q)
        try: d,_=fetch(url)
        except Exception: break
        t=d.decode('utf-8','replace')
        for h in dict.fromkeys(re.findall(r'<a[^>]+href="(https://www\.vaassenactief\.nl/[a-z0-9\-]+/)"',t)):
            if h.count('/')==4 and not re.search(r'/(category|tag|page|nieuws|agenda|fotos|contact)/',h): res.append(h)
    print('=== ',q)
    seen=set()
    for h in res:
        if h in seen: continue
        seen.add(h); m=meta(h)
        if m and m['date']>='2024' and m['date']!='?': print(m['date'],h.split('.nl/')[1],'|',m['title'][:80])
