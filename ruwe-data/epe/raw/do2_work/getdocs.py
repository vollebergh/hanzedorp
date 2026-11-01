import json, subprocess, os, sys
ORI='/home/nick/Claude/Hanzedorp/tools/ori.py'
os.environ['ORI_CACHE']=os.path.abspath('ori')
idx=json.load(open('data/docs/_collect_index.json'))
bykey={k.split(':')[-1]:k for k in idx}
for i in sys.argv[1:]:
    fn='data/docs/%s.md'%i
    if os.path.exists(fn) and os.path.getsize(fn)>0: continue
    eid=bykey.get(i) or 'document:notubiz:gemeente:ermelo:'+i
    r=subprocess.run(['python3','-I',ORI,'--rate','40','get',eid,'--out',fn],capture_output=True,text=True)
    t=idx.get(eid,{}).get('title','?'); d=idx.get(eid,{}).get('date','?')
    print(i,d,t[:60],os.path.getsize(fn) if os.path.exists(fn) else 'FAIL '+r.stderr[:100],flush=True)
