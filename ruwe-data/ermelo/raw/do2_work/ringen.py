# DO2 Elburg: ringen rond kernen (CBS 2021) - agrarisch gebied (BRP 2025 excl. natuurterrein) en overlay-druk; namen van gebieden
# Draaien: DO2_GEO=ermelo_gemeente_gm.json /home/nick/.venv/bin/python3 -I do2_ringen.py
import json, os, collections
from shapely.geometry import shape
from shapely.ops import unary_union
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'); W = os.path.join(D, 'wfs')
G = shape(json.load(open(os.path.join(D, os.environ.get('DO2_GEO', 'ermelo_gemeente_gm.json'))))['features'][0]['geometry'])
def L(fn, filt=None):
    out = []
    for f in json.load(open(fn))['features']:
        s = shape(f['geometry'])
        if not s.is_valid: s = s.buffer(0)
        if s.intersects(G): out.append((f['properties'], s))
    return out
brp = [(p, shape(f['geometry']).buffer(0)) for f in json.load(open(os.path.join(D, 'pdok', 'brp2025.json')))['features'] for p in [f['properties']]]
agr = unary_union([s.intersection(G) for p, s in brp if p['category'] not in ('Natuurterrein', 'Overige') and s.intersects(G)])
def lay(fn): return unary_union([s for p, s in L(os.path.join(W, fn))]).intersection(G)
OV = {'GNN': lay('Gelders_natuurnetwerk.json'), 'GOZ': lay('Groene_ontwikkelingszone.json'), 'Weidevogel': lay('Weidevogelgebieden.json'),
      'Ganzenrust': lay('Ganzenrustgebieden.json'), 'Stikstofstrook': lay('Stikstofreductiegebied.json'), 'Intrekgebied': lay('Intrekgebieden.json'),
      'Molenbiotoop': lay('Molenbiotoop.json'), 'Ammoniakbuffer': lay('Ammoniakbuffergebied.json'), 'Grondwaterbesch.': lay('Grondwaterbescherming.json'),
      'Waterwin': lay('Waterwingebieden.json'), 'Veluwe-streek': unary_union([s for p, s in L(os.path.join(W, 'Streekgebieden.json')) if p['streekgebied_naam'] == 'Veluwe']).intersection(G)}
n2 = unary_union([s for p, s in L(os.path.join(D, 'pdok', 'natura2000.json'))]).intersection(G); OV['Natura2000'] = n2
VRIJ_SET = ['GNN', 'GOZ', 'Weidevogel', 'Ganzenrust', 'Stikstofstrook', 'Natura2000']
vrij_u = unary_union([OV[k] for k in VRIJ_SET])
kernen = {f['properties']['naam2021']: shape(f['geometry']).buffer(0) for f in json.load(open(os.path.join(D, 'pdok', 'kernen2021.json')))['features'] if shape(f['geometry']).intersects(G) and shape(f['geometry']).intersection(G).area > 1e4}
out = []
print('kernen in Elburg:', list(kernen))
for nm, k in kernen.items():
    inn = k.intersection(vrij_u).area / k.area * 100
    stk = k.intersection(OV['Stikstofstrook']).area / k.area * 100
    print('\nKERN', nm, 'kern zelf: %% in stikstofreductiegebied %.0f, in GNN %.0f, GOZ %.0f, Natura2000 %.0f' % (stk, k.intersection(OV['GNN']).area / k.area * 100, k.intersection(OV['GOZ']).area / k.area * 100, k.intersection(OV['Natura2000']).area / k.area * 100))
    prev = k
    for lo, hi in [(0, 250), (250, 500), (500, 1000), (1000, 2000)]:
        ring = k.buffer(hi).difference(k.buffer(lo)).intersection(agr) if lo else k.buffer(hi).difference(k).intersection(agr)
        if ring.is_empty or ring.area < 1e3: print('  ring %d-%d m: geen agrarisch gebied' % (lo, hi)); continue
        a = ring.area / 1e4
        row = {'kern': nm, 'ring': '%d-%d' % (lo, hi), 'agr_ha': round(a, 1)}
        for key in OV: row[key] = round(ring.intersection(OV[key]).area / ring.area * 100)
        row['vrij'] = round(ring.difference(vrij_u).area / ring.area * 100)
        out.append(row)
        print('  ring %4d-%4d m: agr %.0f ha | vrij %d%% | ' % (lo, hi, a, row['vrij']) + ' '.join('%s %d%%' % (k2, row[k2]) for k2 in OV if row[k2]))
json.dump(out, open(os.path.join(D, 'ringen_kernen.json'), 'w'), indent=1)
# Namen van gebieden binnen Elburg
def names(fn, key, extra=()):
    c = collections.defaultdict(float)
    for p, s in L(os.path.join(W, fn)):
        c[' | '.join(str(p.get(k)) for k in (key,) + tuple(extra))] += s.intersection(G).area / 1e4
    return {k: round(v, 1) for k, v in sorted(c.items(), key=lambda x: -x[1]) if v > 0.05}
print('\nWEIDEVOGEL', names('Weidevogelgebieden.json', 'gebiedsnaam'))
print('GANZENRUST', names('Ganzenrustgebieden.json', 'gebiedsnaam'))
print('GNN regio', names('Gelders_natuurnetwerk.json', 'regio'))
print('GOZ regio', names('Groene_ontwikkelingszone.json', 'regio'))
print('GOZ objectnaam (top)', list(names('Groene_ontwikkelingszone.json', 'objectnaam').items())[:10])
print('NATLANDSCHAP', names('Nationale_landschappen.json', 'gebiedsnaam'))
print('STREEK', names('Streekgebieden.json', 'streekgebied_naam', ('deelgebied_naam',)))
print('WATERWIN', names('Waterwingebieden.json', 'geb_naam', ('gemeente',)))
print('GWBG', names('Grondwaterbescherming.json', 'geb_naam', ('gemeente',)))
print('INTREK', names('Intrekgebieden.json', 'objectnaam'))
print('ASV', names('Drinkwaterreservering_ASV.json', 'gebiedsnaam', ('type_asv_gebied',)))
print('MOLEN', names('Molenbiotoop.json', 'objectnaam'))
print('PEIL', names('Peilbesluitgebied.json', 'gebiedsnaam', ('waterschap',)))
print('WATERSCHAP', names('Waterschappen.json', 'waterschap'))
print('PROVWEG', names('Provinciale_wegen.json', 'objectnaam', ('beheerder',)))
print('N2000', {nm: round(sum(s.intersection(G).area for p, s in L(os.path.join(D, 'pdok', 'natura2000.json')) if p['naamN2K'] == nm) / 1e4, 1) for nm in set(p['naamN2K'] for p, s in L(os.path.join(D, 'pdok', 'natura2000.json')))})
