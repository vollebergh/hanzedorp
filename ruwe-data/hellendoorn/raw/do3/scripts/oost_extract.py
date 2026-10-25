import json,re,os,sys,html
d=sys.argv[1]; out=[]
for fn in os.listdir(d):
    if not fn.endswith('.html'): continue
    s=open(os.path.join(d,fn),encoding='utf-8',errors='replace').read()
    body='';date='';head=''
    for m in re.finditer(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',s,re.S):
        try: j=json.loads(m.group(1))
        except Exception: continue
        for o in (j if isinstance(j,list) else [j]):
            if isinstance(o,dict) and o.get('articleBody'):
                body=o['articleBody']; date=o.get('datePublished',''); head=o.get('headline','')
    if not body:
        t=re.search(r'<title>(.*?)</title>',s,re.S); head=t.group(1) if t else fn
    out.append({'id':fn[:-5],'date':date[:10],'headline':html.unescape(head),'body':html.unescape(re.sub('<[^>]+>',' ',body))})
json.dump(out,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
print(len(out),sum(1 for o in out if o['body']))
