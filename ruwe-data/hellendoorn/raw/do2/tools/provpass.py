# Extraheert passages over provincie/vooroverleg/KGO/woonafspraken/landbouwgebied uit tekstbestanden.
# Gebruik: python3 -I provpass.py <max_passages> bestand...
import re,sys
pat=re.compile(r'(vooroverleg|voorkant|omgevingstafel|ketenpartner|provincie (Overijssel )?(heeft|geeft|is|ziet|kan|stemt|gaf|reageerde|ging|adviseert|vraagt|wijst|merkt)|reactie (van|op) de provincie|instemming|melding KGO|Kwaliteitsimpuls|KGO|landbouwgebied(en)? met|generieke opgaven|gebiedsspecifieke opgaven|woonafspraken|Woondeal|woondeal|streekcentrum|regionale behoefte|redeneerlijn|artikel 4\.(4|5|11|14|15|122|123|124|125)\b|Uitzonderingenlijst|Lijst BOPA|art\. 4\.)',re.I)
n=int(sys.argv[1])
for fn in sys.argv[2:]:
    s=re.sub(r'\s+',' ',open(fn,errors='replace').read())
    hits=[(max(0,m.start()-300),min(len(s),m.end()+400)) for m in pat.finditer(s)]
    merged=[]
    for a,b in sorted(hits):
        if merged and a<=merged[-1][1]: merged[-1]=(merged[-1][0],max(b,merged[-1][1]))
        else: merged.append((a,b))
    print('\n#####',fn,len(s.split()),'woorden,',len(merged),'passages')
    for a,b in merged[:n]:
        print('  ...',s[a:b],'...\n')
