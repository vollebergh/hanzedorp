import json,sys,os
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=json.load(open(W+"/snapshot_payloads.json"))
for pre in sys.argv[1:]:
    for e,p in S.items():
        if e.split(':')[-1].startswith(pre): print(e.split(':')[-1],p.get('last_discussed_at','')[:10],p.get('name'))
