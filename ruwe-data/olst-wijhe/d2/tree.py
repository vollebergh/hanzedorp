import json,sys
d=json.load(open(sys.argv[1]));A=d['annotaties']
def text(n):
    if isinstance(n,str): return n
    if isinstance(n,list): return ''.join(text(x) for x in n)
    if isinstance(n,dict):
        s=''
        if 'kop' in n:
            k=n['kop']; s+=' '.join(text(k.get(x,{}).get('children',[])) for x in ('label','nummer','opschrift'))+'\n'
        for key in ('content','children'):
            if key in n:
                for c in n[key]:
                    t=text(c)
                    s+=t+('\n' if isinstance(c,dict) and c.get('type') in ('alinea','lid','artikel','lijst','li','al','item') else '')
        return s
    return ''
arts={}
def walk(n,path):
    if isinstance(n,dict):
        if n.get('type')=='artikel':
            arts[n['id']]=n
        for key in ('children','content'):
            for c in n.get(key,[]) if isinstance(n.get(key),list) else []: walk(c,path)
walk(d['body'][0],[])
def annots(n,acc):
    if isinstance(n,dict):
        acc.update(n.get('annotaties',[]) or [])
        for key in ('children','content'):
            v=n.get(key)
            if isinstance(v,list):
                for c in v: annots(c,acc)
    return acc
import pickle
pickle.dump((arts,),open(sys.argv[1]+'.pkl','wb'))
mode=sys.argv[2]
if mode=='art':
    for aid,n in arts.items():
        if aid.endswith('art_'+sys.argv[3]): print(aid); print(text(n))
elif mode=='find':
    names=sys.argv[3:]
    for aid,n in arts.items():
        acc=annots(n,set())
        hits=set()
        for i in acc:
            a=A.get(i)
            if a and a.get('name') in names: hits.add(a['name'])
            # children of gebiedsaanwijzing
        if hits: print(aid, sorted(hits))
