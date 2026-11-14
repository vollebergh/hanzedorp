# DO2 Elburg: puntentoets - in welke provinciale overlays liggen concrete Elburgse locaties (adrescoordinaten PDOK Locatieserver, RD)
# Draaien: /home/nick/.venv/bin/python3 -I do2_punten.py
import json, os, urllib.request, urllib.parse
from shapely.geometry import shape, Point
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'do2_data'); W = os.path.join(D, 'wfs')
def ls(q):
    u = 'https://api.pdok.nl/bzk/locatieserver/search/v3_1/free?' + urllib.parse.urlencode({'q': q, 'fq': 'gemeentenaam:Elburg', 'rows': 1, 'fl': 'weergavenaam,type,centroide_rd'})
    d = json.load(urllib.request.urlopen(u, timeout=30))['response']['docs']
    if not d: return None
    x = d[0]; c = x['centroide_rd'].replace('POINT(', '').replace(')', '').split()
    return x['weergavenaam'], x['type'], float(c[0]), float(c[1])
LAYERS = {'GNN': 'Gelders_natuurnetwerk', 'GOZ': 'Groene_ontwikkelingszone', 'Weidevogel': 'Weidevogelgebieden', 'Ganzenrust': 'Ganzenrustgebieden',
          'Stikstofreductiegebied': 'Stikstofreductiegebied', 'NatLandschap': 'Nationale_landschappen', 'Molenbiotoop': 'Molenbiotoop', 'Intrekgebied': 'Intrekgebieden',
          'GWBG': 'Grondwaterbescherming', 'Waterwin': 'Waterwingebieden', 'ASV': 'Drinkwaterreservering_ASV', 'Ammoniakbuffer': 'Ammoniakbuffergebied'}
geo = {}
for k, fn in LAYERS.items():
    geo[k] = [shape(f['geometry']).buffer(0) for f in json.load(open(os.path.join(W, fn + '.json')))['features']]
n2 = [shape(f['geometry']).buffer(0) for f in json.load(open(os.path.join(D, 'pdok', 'natura2000.json')))['features']]; geo['Natura2000'] = n2
strk = [(f['properties']['streekgebied_naam'], shape(f['geometry']).buffer(0)) for f in json.load(open(os.path.join(W, 'Streekgebieden.json')))['features']]
Q = ['Nagelhoudsweg 1 \'t Harde', 'Verlengde Haerderweg 3 Doornspijk', 'Berkenweg 7 Doornspijk', 'Koeweg 4b \'t Harde', 'Schiksweg 35 Doornspijk', 'Hokseberg 2 \'t Harde',
     'Horstkamp Elburg', 'Vossenakker Elburg', 'Lageweg Doornspijk', 'Kamperdijk Elburg', 'Oostendorp Elburg', 'Vaarbekerweg 23 Doornspijk', 'Gerichtenweg Doornspijk', 'Kamperweg Elburg',
     'Oostendorperstraatweg 31A Elburg', 'Huisdijk 18 Doornspijk', 'Nieuwstadsweg 23 Elburg', 'Mezenbergerweg 7 Elburg', 'Diepesteeg 11 Elburg', 'Koopsweg 19 Elburg', 'Tempelweg 7a Elburg', 'Haerderweg 12 Elburg', 'Zuiderzeestraatweg 129 Elburg']
out = []
for q in Q:
    try: r = ls(q)
    except Exception as e: r = None
    if not r: print(q, '-> niet gevonden'); continue
    name, typ, x, y = r; p = Point(x, y)
    hits = [k for k, gs in geo.items() if any(g.contains(p) for g in gs)]
    st = [n for n, g in strk if g.contains(p)]
    out.append({'zoekterm': q, 'gevonden': name, 'type': typ, 'rd': [x, y], 'overlays': hits, 'streek': st})
    print('%-36s | %-48s | %-6s | streek %s | %s' % (q, name[:48], typ, ','.join(st) or '-', ', '.join(hits) or '(geen)'))
json.dump(out, open(os.path.join(D, 'puntentoets_locaties.json'), 'w'), indent=1, ensure_ascii=False)
