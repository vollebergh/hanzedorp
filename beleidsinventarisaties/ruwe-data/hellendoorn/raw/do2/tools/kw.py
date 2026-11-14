# Toont context rond trefwoorden. Gebruik: python3 -I kw.py "<regex>" <venster> <max> bestand...
import re,sys
pat=re.compile(sys.argv[1],re.I); w=int(sys.argv[2]); n=int(sys.argv[3])
for fn in sys.argv[4:]:
    s=re.sub(r'\s+',' ',open(fn,errors='replace').read())
    ms=list(pat.finditer(s)); print('#####',fn,len(ms),'treffers')
    last=-1; k=0
    for m in ms:
        if m.start()<last: continue
        a=max(0,m.start()-w); b=min(len(s),m.end()+w); print('  >>',s[a:b]); last=b; k+=1
        if k>=n: break
