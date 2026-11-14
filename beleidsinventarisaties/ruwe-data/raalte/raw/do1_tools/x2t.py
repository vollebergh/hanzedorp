import sys,re,html
for f in sys.argv[1:]:
    s=open(f,encoding='utf-8').read()
    s=re.sub(r'<(al|titel|kop|li|tr|p|regeling-sluiting|artikel|nr|lid|lidnr)\b[^>]*>',r'\n',s)
    s=re.sub(r'<[^>]+>',' ',s); s=html.unescape(s)
    s=re.sub(r'[ \t]+',' ',s); s=re.sub(r'\n\s*\n+','\n',s)
    open(f[:-4]+'.txt','w').write(s.strip()); print(f, len(s))
