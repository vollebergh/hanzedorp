import sys,re,html
t=open(sys.argv[1],encoding='utf-8',errors='replace').read()
base=sys.argv[2]
seen=set()
for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>',t,re.S):
    h,txt=m.group(1),re.sub(r'<[^>]+>','',m.group(2)); txt=html.unescape(' '.join(txt.split()))
    if len(txt)>25 and h not in seen and base in h:
        seen.add(h); print(h,'|',txt[:140])
