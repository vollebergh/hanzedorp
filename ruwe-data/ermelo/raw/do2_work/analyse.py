# DO2 Elburg: doorsnijden van provinciale overlays (Gelderse WFS) en PDOK-lagen met gemeentegrens Elburg (GM0230) en BRP 2025
# Draaien met: /home/nick/.venv/bin/python3 -I do2_analyse.py
import json, os, collections
from shapely.geometry import shape
from shapely.ops import unary_union
from shapely.prepared import prep
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
W = os.path.join(D, 'wfs')
GEOFILE = os.environ.get('DO2_GEO', 'ermelo_gemeente_gm.json')
G = shape(json.load(open(os.path.join(D, GEOFILE)))['features'][0]['geometry'])
GA = G.area / 1e4
pg = prep(G)
def load(fn):
    return json.load(open(fn))['features']
def geoms(fn, filt=None):
    out = []
    for f in load(fn):
        if filt and not filt(f['properties']): continue
        s = shape(f['geometry'])
        if not s.is_valid: s = s.buffer(0)
        if pg.intersects(s): out.append((f['properties'], s))
    return out
def union_clip(items):
    if not items: return None
    u = unary_union([s for _, s in items])
    return u.intersection(G)
# BRP
brp = []
for f in load(os.path.join(D, 'pdok', 'brp2025.json')):
    s = shape(f['geometry'])
    if not s.is_valid: s = s.buffer(0)
    if not pg.intersects(s): continue
    c = s.intersection(G)
    if c.is_empty: continue
    brp.append((f['properties'], c))
agr_all = unary_union([c for p, c in brp])
excl_nat = unary_union([c for p, c in brp if p['category'] not in ('Natuurterrein', 'Overige')])
prod = unary_union([c for p, c in brp if p['category'] in ('Grasland', 'Bouwland')])
A = {'BRP totaal (alle categorieen)': agr_all, 'BRP excl. natuurterrein/overige (def. provinciebestand 1.6.8)': excl_nat, 'Productief (grasland+bouwland)': prod}
print('Gemeentegebied ha', round(GA, 1))
for k, v in A.items(): print(k, round(v.area / 1e4, 1))
LAYERS = {
 'GNN': ('Gelders_natuurnetwerk.json', None),
 'GOZ': ('Groene_ontwikkelingszone.json', None),
 'Weidevogelgebied': ('Weidevogelgebieden.json', None),
 'Ganzenrustgebied': ('Ganzenrustgebieden.json', None),
 'Beschermingszone natte landnatuur': ('Beschzones_nat_landnat.json', None),
 'Nationaal Landschap Veluwe': ('Nationale_landschappen.json', None),
 'Waterwingebied': ('Waterwingebieden.json', None),
 'Grondwaterbeschermingsgebied': ('Grondwaterbescherming.json', None),
 'KWO-vrije zone': ('KWO_vrije_zone.json', None),
 'Intrekgebied': ('Intrekgebieden.json', None),
 'Drinkwaterreservering/ASV': ('Drinkwaterreservering_ASV.json', None),
 'Molenbiotoop': ('Molenbiotoop.json', None),
 'Stiltegebied': ('Stiltegebieden.json', None),
 'Stikstofreductiegebied (POVE, per 23-10-2026)': ('Stikstofreductiegebied.json', None),
 'Ammoniakbuffergebied': ('Ammoniakbuffergebied.json', None),
 'Provinciale weg (gebied)': ('Provinciale_wegen.json', None),
 'Provinciale weg beperking': ('Provinciale_wegen_beperking.json', None),
 'Provinciale weg zorgplicht': ('Provinciale_weg_zorgplichtgebied.json', None),
 'Windturbines verbodsgebied Veluwe': ('Windturbines_verbodsgebied_Veluwe.json', None),
 'Windturbines aandachtsgebied rond Veluwe': ('Windturbines_aandachtsgebied_rondom_de_Veluwe.json', None),
 'Glastuinbouw': ('Glastuinbouw.json', None),
 'Aanvoergebied IJsselmeergebied': ('Aanvoergebied_IJsselmeergebied.json', None),
 'Peilbesluitgebied': ('Peilbesluitgebied.json', None),
}
res = {}; U = {}
for name, (fn, filt) in LAYERS.items():
    items = geoms(os.path.join(W, fn), filt)
    u = union_clip(items)
    U[name] = u
    r = {'n_features_in_gemeente': len(items), 'ha_gemeente': 0 if u is None else u.area / 1e4}
    r['pct_gemeente'] = r['ha_gemeente'] / GA * 100
    for k, a in A.items():
        if u is None: r['ha_' + k] = 0; r['pct_' + k] = 0
        else:
            x = u.intersection(a).area / 1e4
            r['ha_' + k] = x; r['pct_' + k] = x / (a.area / 1e4) * 100
    res[name] = r
# Natura 2000 (PDOK)
n2 = geoms(os.path.join(D, 'pdok', 'natura2000.json'))
names = collections.defaultdict(list)
for p, s in n2: names[p['naamN2K']].append(s)
for nm, ss in list(names.items()) + [('Natura 2000 (alle)', [s for _, s in n2])]:
    u = unary_union(ss).intersection(G)
    key = 'Natura 2000 ' + nm if nm != 'Natura 2000 (alle)' else nm
    U[key] = u
    r = {'ha_gemeente': u.area / 1e4}; r['pct_gemeente'] = r['ha_gemeente'] / GA * 100
    for k, a in A.items():
        x = u.intersection(a).area / 1e4; r['ha_' + k] = x; r['pct_' + k] = x / (a.area / 1e4) * 100
    res[key] = r
# Streek: per naam
st = geoms(os.path.join(W, 'Streekgebieden.json'))
bys = collections.defaultdict(list)
for p, s in st: bys[p['streekgebied_naam']].append(s)
for nm, ss in bys.items():
    u = unary_union(ss).intersection(G); key = 'Streek ' + nm; U[key] = u
    r = {'ha_gemeente': u.area / 1e4}; r['pct_gemeente'] = r['ha_gemeente'] / GA * 100
    for k, a in A.items():
        x = u.intersection(a).area / 1e4; r['ha_' + k] = x; r['pct_' + k] = x / (a.area / 1e4) * 100
    res[key] = r
# Woningbouwregios
wb = geoms(os.path.join(W, 'Woningbouwregios.json'))
for p, s in wb:
    u = s.intersection(G); print('Woningbouwregio', p.get('regio'), round(u.area / 1e4, 1), 'ha binnen gemeente')
# combinaties
def comb(names):
    return unary_union([U[n] for n in names if U.get(n) is not None])
COMBOS = {
 'GNN of GOZ': ['GNN', 'GOZ'],
 'Natuur/vogel (GNN/GOZ/N2000/weidevogel/ganzenrust)': ['GNN', 'GOZ', 'Natura 2000 (alle)', 'Weidevogelgebied', 'Ganzenrustgebied'],
 'Natuur/vogel + natte landnatuur': ['GNN', 'GOZ', 'Natura 2000 (alle)', 'Weidevogelgebied', 'Ganzenrustgebied', 'Beschermingszone natte landnatuur'],
 'Weidevogel of ganzenrust': ['Weidevogelgebied', 'Ganzenrustgebied'],
 'Alle vijf + stikstofreductiegebied + natte landnatuur (vrij = daarbuiten)': ['GNN', 'GOZ', 'Natura 2000 (alle)', 'Weidevogelgebied', 'Ganzenrustgebied', 'Beschermingszone natte landnatuur', 'Stikstofreductiegebied (POVE, per 23-10-2026)'],
 'BOPA-adviesgeval (Prb 2024/3109) - WFS-lagen': ['GNN', 'GOZ', 'Beschermingszone natte landnatuur', 'Ganzenrustgebied', 'Weidevogelgebied', 'Nationaal Landschap Veluwe', 'Molenbiotoop', 'Waterwingebied', 'Grondwaterbeschermingsgebied', 'KWO-vrije zone', 'Intrekgebied', 'Drinkwaterreservering/ASV'],
 'BOPA-adviesgeval zonder Nationaal Landschap': ['GNN', 'GOZ', 'Beschermingszone natte landnatuur', 'Ganzenrustgebied', 'Weidevogelgebied', 'Molenbiotoop', 'Waterwingebied', 'Grondwaterbeschermingsgebied', 'KWO-vrije zone', 'Intrekgebied', 'Drinkwaterreservering/ASV'],
 'Nationaal Landschap buiten GNN/GOZ': None,
 'Water-/bodembescherming (waterwin/GWBG/KWO/intrek/ASV)': ['Waterwingebied', 'Grondwaterbeschermingsgebied', 'KWO-vrije zone', 'Intrekgebied', 'Drinkwaterreservering/ASV'],
}
for cn, lst in COMBOS.items():
    if lst is None:
        u = U['Nationaal Landschap Veluwe'].difference(comb(['GNN', 'GOZ']))
    else: u = comb(lst)
    U[cn] = u
    r = {'ha_gemeente': u.area / 1e4}; r['pct_gemeente'] = r['ha_gemeente'] / GA * 100
    for k, a in A.items():
        x = u.intersection(a).area / 1e4; r['ha_' + k] = x; r['pct_' + k] = x / (a.area / 1e4) * 100
    res[cn] = r
# Vrij agrarisch gebied
for k, a in A.items():
    vrij = a.difference(U['Alle vijf + stikstofreductiegebied + natte landnatuur (vrij = daarbuiten)'])
    vrij2 = a.difference(U['Natuur/vogel (GNN/GOZ/N2000/weidevogel/ganzenrust)'])
    vrij3 = a.difference(U['BOPA-adviesgeval (Prb 2024/3109) - WFS-lagen'])
    res['VRIJ buiten alle natuur/vogel/N-reductie/natte landnatuur | ' + k] = {'ha': vrij.area / 1e4, 'pct': vrij.area / a.area * 100}
    res['VRIJ buiten natuur/vogel (5 lagen) | ' + k] = {'ha': vrij2.area / 1e4, 'pct': vrij2.area / a.area * 100}
    res['VRIJ buiten alle BOPA-adviesgevallen (WFS) | ' + k] = {'ha': vrij3.area / 1e4, 'pct': vrij3.area / a.area * 100}
json.dump(res, open(os.path.join(D, 'overlay_resultaat_' + GEOFILE.replace('.json','') + '.json'), 'w'), indent=1, ensure_ascii=False)
K1 = 'BRP excl. natuurterrein/overige (def. provinciebestand 1.6.8)'; K2 = 'Productief (grasland+bouwland)'
print('%-70s %8s %7s | %9s %7s | %9s %7s' % ('Overlay', 'ha gem', '%gem', 'ha exNat', '%exNat', 'ha prod', '%prod'))
for n, r in res.items():
    if 'pct_gemeente' in r:
        print('%-70s %8.1f %7.1f | %9.1f %7.1f | %9.1f %7.1f' % (n[:70], r['ha_gemeente'], r['pct_gemeente'], r['ha_' + K1], r['pct_' + K1], r['ha_' + K2], r['pct_' + K2]))
    else:
        print('%-90s %9.1f %7.1f' % (n[:90], r['ha'], r['pct']))
