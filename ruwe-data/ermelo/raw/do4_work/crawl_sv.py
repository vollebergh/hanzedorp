import sys,re,urllib.request
sys.path.insert(0,'.')
from fetch import html2text
B='https://acc.digitaleplannen.nl/joris/C34ABDC7-B822-4485-B141-CB4D49727C00/'
P='b_NL.IMRO.0233.SVfunctieverander-0401_'
seen={};queue=['1','2','3','4','5','6']
out=[]
while queue:
    n=queue.pop(0)
    if n in seen: continue
    try: d=urllib.request.urlopen(urllib.request.Request(B+P+n+'.html',headers={'User-Agent':'Mozilla/5.0'}),timeout=60).read().decode('utf8','replace')
    except Exception as e: seen[n]=None; print('ERR',n,e); continue
    seen[n]=d
    for m in re.findall(r'href="'+re.escape(P)+r'([0-9.]+)\.html"',d):
        if m not in seen and m not in queue: queue.append(m)
def key(n): return [int(x) for x in n.split('.')]
for n in sorted([k for k,v in seen.items() if v],key=key):
    t=html2text(seen[n])
    i=t.find('Omhoog')
    out.append('\n\n##### SECTIE %s\n'%n+t[i+6:] )
open('src/sv_full.txt','w').write('BRON: '+B+P+'<n>.html\n'+''.join(out))
print(sorted(seen,key=key))
