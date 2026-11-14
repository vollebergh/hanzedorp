import json,re,sys
D=r'(\d{1,2}) (januari|februari|maart|april|mei|juni|juli|augustus|september|oktober|november|december) (20\d\d)'
M={m:i+1 for i,m in enumerate('januari februari maart april mei juni juli augustus september oktober november december'.split())}
def real(x):
    t=x['text']; i=t.find(x['title'][:30]) if x['title'] else 0
    m=re.search(D,t[max(i,0):])
    return (int(m.group(3)),M[m.group(2)],int(m.group(1))) if m else (0,0,0)
if __name__=='__main__':
    pat=re.compile(sys.argv[1],re.I); ymin=int(sys.argv[2]) if len(sys.argv)>2 else 2024
    seen=set();out=[]
    for l in open('hz.jsonl'):
        x=json.loads(l)
        if x['url'] in seen: continue
        seen.add(x['url'])
        d=real(x)
        if d[0]>=ymin and pat.search(x['title']+' '+x['text']):
            out.append((d,x['title'][:100],x['url'].split('/nieuws/')[-1][:70]))
    for d,t,u in sorted(out): print('%d-%02d-%02d'%d,t,'|',u)
    print(len(out))
