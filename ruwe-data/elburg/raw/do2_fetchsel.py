import json, subprocess, os, sys
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'do2_data', 'docs')
idx = json.load(open(os.path.join(OUT, '_collect_index.json')))
pref = sys.argv[1:]
for p in pref:
    m = [k for k in idx if k.split(':')[-1].startswith(p)]
    if not m: print('geen', p); continue
    eid = m[0]; fn = os.path.join(OUT, 'sel_%s_%s.md' % (idx[eid]['date'], p))
    if os.path.exists(fn): continue
    r = subprocess.run(['python3', '-I', '/home/nick/Claude/Hanzedorp/tools/ori.py', 'get', eid, '--out', fn], capture_output=True, text=True)
    print(p, idx[eid]['date'], idx[eid]['title'][:60], os.path.getsize(fn) if os.path.exists(fn) else 'FAIL', flush=True)
