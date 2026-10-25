import sys,re
t=open('$F').read()
parts=re.split(r'\n(?====== \[)',t)
d={}
for p in parts:
    m=re.match(r'===== \[(\d+)\]',p.strip())
    if m: d[int(m.group(1))]=p.strip()
for a in sys.argv[1:]:
    print(d[int(a)]); print()
