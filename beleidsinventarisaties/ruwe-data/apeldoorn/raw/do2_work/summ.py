import re,glob,sys
ids=sys.argv[1:]
for i in ids:
    f=glob.glob('*'+i+'.md')[0]
    t=open(f).read()
    ti=re.search(r'titel:\s*"(.*)"',t).group(1); dt=re.search(r'vergaderdatum:\s*"(.*)"',t).group(1)
    print('#####',ti[:80],dt,'len',len(t))
    j=[m.start() for m in re.finditer(r'Aanleiding',t)]
    j=j[1] if len(j)>1 else (j[0] if j else 2500)
    print(re.sub(r'\s+',' ',t[j:j+1300]))
    for m in list(re.finditer(r'[^.\n]*(provinci|Regisseur|Groene ontwikkelingszone|woondeal|Woonagenda|ladder|Ladder)[^.\n]*\.',t))[:0]: pass
