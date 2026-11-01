import sys,re
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/cbd7d9f0-97a4-45cc-923f-0df0e26b9a22/scratchpad/epe/raw/do3_work')
from fetch import fetch, html2text
d,ct=fetch(sys.argv[1]); t=d.decode('utf-8','replace')
pat=sys.argv[2] if len(sys.argv)>2 else '.'
seen=set()
for h,l in re.findall(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',t,re.S):
    l=html2text(l).replace('\n',' ')[:100]
    if h in seen or not re.search(pat,h+l,re.I): continue
    seen.add(h); print(h,'|',l)
