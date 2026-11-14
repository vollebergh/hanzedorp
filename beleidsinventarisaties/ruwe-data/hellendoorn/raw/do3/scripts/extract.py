import re,sys,os,html,json
src,dst=sys.argv[1],sys.argv[2]
os.makedirs(dst,exist_ok=True)
idx=[]
for fn in sorted(os.listdir(src)):
    s=open(os.path.join(src,fn),encoding='utf-8',errors='replace').read()
    m=re.search(r'datePublished":"([^"]+)',s); d=m.group(1)[:10] if m else ''
    t=re.search(r'<h1[^>]*>(.*?)</h1>',s,re.S); t=html.unescape(re.sub('<[^>]+>','',t.group(1))).strip() if t else fn
    mm=re.search(r'<main[^>]*>(.*?)</main>',s,re.S); body=mm.group(1) if mm else s
    body=re.sub(r'<(script|style)[^>]*>.*?</\1>','',body,flags=re.S)
    body=re.sub(r'<br\s*/?>|</p>|</li>|</h\d>','\n',body)
    body=html.unescape(re.sub('<[^>]+>','',body))
    body=re.sub(r'[ \t]+',' ',body); body=re.sub(r'\n\s*\n+','\n',body).strip()
    slug=fn[:-5]
    open(os.path.join(dst,slug+'.txt'),'w').write(f'{t}\n{d}\nhttps://www.hellendoorn.nl/actueel/{slug}/\n\n{body}\n')
    idx.append((d,slug,t))
idx.sort()
open(os.path.join(dst,'_index.tsv'),'w').write('\n'.join('\t'.join(x) for x in idx))
print(len(idx))
