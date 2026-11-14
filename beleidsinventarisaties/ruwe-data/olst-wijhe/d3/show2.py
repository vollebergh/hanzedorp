import sys,re
t=open(sys.argv[1]).read()
parts=re.split(r'\n(?====== \[)',t)
d={}
for p in parts:
    m=re.match(r'===== \[(\d+)\]',p.strip())
    if m: d[int(m.group(1))]=p.strip()
for a in sys.argv[2:]:
    print(d[int(a)]); print()
