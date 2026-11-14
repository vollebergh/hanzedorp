# haalt geselecteerde Open Besluitvorming-stukken (Apeldoorn) op via ori.py get; sla bestaande over
import json, subprocess, os, re
ORI='/home/nick/Claude/Hanzedorp/tools/ori.py'
os.environ['ORI_CACHE']=os.path.abspath('ori')
sel=json.load(open('data/docs/_selected.json'))
OUT='data/docs/ori_md'
for k,v in sorted(sel.items(), key=lambda kv: kv[1]['date'], reverse=True):
    fn=os.path.join(OUT, k.split(':')[-1]+'.md')
    if os.path.exists(fn): continue
    p=subprocess.run(['python3','-I',ORI,'--rate','20','get',k,'--out',OUT],capture_output=True,text=True)
    print(v['date'], v['title'][:70], 'rc',p.returncode, p.stderr[:100].replace('\n',' '), flush=True)
