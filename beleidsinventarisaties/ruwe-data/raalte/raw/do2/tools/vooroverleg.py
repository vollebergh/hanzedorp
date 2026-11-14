# Extraheert passages over vooroverleg/provincie/Omgevingstafel uit plantoelichtingen (plans/tl_*.txt)
import re,glob,sys
pat=re.compile(r'(vooroverleg|omgevingstafel|voorkant|ketenpartner|provincie (heeft|geeft|is|ziet|kan|stemt|gaf|reageerde|ging)|reactie (van|op) de provincie|instemming|melding KGO|Melding KGO|landbouwgebied(en)? met|generieke opgaven|gebiedsspecifieke opgaven|geen opmerkingen|akkoord)',re.I)
for fn in sorted(glob.glob('tl_*.txt')):
    s=open(fn,errors='replace').read()
    s=re.sub(r'\s+',' ',s)
    title=s[:0]
    hits=[]
    for m in pat.finditer(s):
        a=max(0,m.start()-250); b=min(len(s),m.end()+350)
        hits.append((a,b))
    # merge
    merged=[]
    for a,b in sorted(hits):
        if merged and a<=merged[-1][1]: merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
        else: merged.append((a,b))
    print('\n#####',fn,len(s.split()),'woorden')
    for a,b in merged[:int(sys.argv[1]) if len(sys.argv)>1 else 12]:
        print('  ...',s[a:b],'...')
