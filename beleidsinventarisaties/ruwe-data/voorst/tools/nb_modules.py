import json,subprocess
UA=open('ua.txt').read().strip()
def get(u):
    r=subprocess.run(['curl','-sL','-A',UA,'-H','Accept: application/json','--max-time','120',u],capture_output=True)
    return json.loads(r.stdout.decode('utf8','replace'))
allitems={}
for mod in [19,8,6,1,3,4]:
    j=get(f"https://api.notubiz.nl/organisations/742/modules/{mod}/items?format=json&version=1.10.8")
    its=j.get('item',[])
    if isinstance(its,dict): its=[its]
    print(mod,len(its),j.get('pagination'))
    out=[]
    for it in its:
        attrs=it['attributes']['attribute']
        if isinstance(attrs,dict): attrs=[attrs]
        rec={'module':mod,'id':it.get('@attributes',{}).get('id')}
        docs=[]
        for a in attrs:
            lab=a['label']; v=a.get('value')
            if isinstance(v,dict) and 'url' in v:
                docs.append({'label':lab,'title':v.get('title'),'url':v['url']})
            elif isinstance(v,list):
                for x in v:
                    if isinstance(x,dict) and 'url' in x: docs.append({'label':lab,'title':x.get('title'),'url':x['url']})
            else: rec[lab]=v
        att=it.get('attachments',{})
        if isinstance(att,dict):
            dl=att.get('document',[])
            if isinstance(dl,dict): dl=[dl]
            for x in dl: docs.append({'label':'attachment','title':x.get('title'),'url':x.get('url')})
        rec['docs']=docs
        out.append(rec)
    allitems[mod]=out
json.dump(allitems,open('d1/notubiz/modules.json','w'))
