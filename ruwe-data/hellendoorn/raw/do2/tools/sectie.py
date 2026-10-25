# Print tekst na de laatste N treffers van een patroon (geen inhoudsopgave-regels) in plantoelichtingen
# Gebruik: python3 sectie.py <regex> <aantal_tekens> bestand...
import re,sys
pat=re.compile(sys.argv[1],re.I); n=int(sys.argv[2])
for fn in sys.argv[3:]:
    s=re.sub(r'\s+',' ',open(fn,errors='replace').read())
    ms=[m for m in pat.finditer(s) if '.....' not in s[m.start():m.start()+120]]
    print('#####',fn)
    seen=-1
    for m in ms[-3:]:
        if m.start()<seen: continue
        print('   >>',s[m.start():m.start()+n]); seen=m.start()+n
