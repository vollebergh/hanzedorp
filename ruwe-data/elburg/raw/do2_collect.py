# DO2: verzamelt via Open Besluitvorming (bronsleutel elburg) documenten bij provinciale zoektermen en haalt de tekst op.
import json, subprocess, os, sys, re, time
ORI = '/home/nick/Claude/Hanzedorp/tools/ori.py'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'do2_data', 'docs')
QUERIES = ['"Groene ontwikkelingszone"', '"Gelders natuurnetwerk"', 'weidevogelgebied', 'ganzenrustgebied', '"Nationaal landschap" kernkwaliteiten',
           '"Omgevingsverordening Gelderland"', '"artikel 5.64"', '"regionale woonafspraken"', '"Natura 2000" vergunning provincie woningbouw',
           '"reactie van de provincie"', '"provincie Gelderland" vooroverleg', 'Regisseur', 'BOPA provincie advies', 'puntenmethode', 'versterkingsopgave',
           '"Noordrand Veluwe"', 'natte landnatuur', 'waterwingebied "De Haere"', 'stikstofruimte woningbouw', 'stikstofbank', 'ervenconsulent', 'functieverandering woningen buitengebied']
seen = {}
for q in QUERIES:
    p = subprocess.run(['python3', '-I', ORI, 'search', q, '--org', 'elburg', '--date-from', '2021-01-01', '--limit', '60', '--json', '--sort', 'date_desc'], capture_output=True, text=True)
    txt = p.stdout
    try:
        arr = json.loads(txt[txt.index('['):])
    except Exception as e:
        print('ERR', q, e); continue
    n = 0
    for d in arr:
        if d.get('entityType') != 'Document': continue
        eid = d['entityId']
        if eid not in seen:
            seen[eid] = {'title': d.get('title'), 'date': d.get('sortDate', '')[:10], 'q': [q]}
            n += 1
        else: seen[eid]['q'].append(q)
    print(q, len(arr), 'nieuw', n, flush=True)
json.dump(seen, open(os.path.join(OUT, '_collect_index.json'), 'w'), indent=1, ensure_ascii=False)
print('totaal uniek', len(seen))
