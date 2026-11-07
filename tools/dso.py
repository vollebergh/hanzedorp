#!/usr/bin/env python3
"""Client voor DSO-Ozon (Presenteren v8) en de Ruimtelijke Plannen API (v4).

Sleutels: keyring-service `dso`, user `presenteren-v8` (Ozon, header x-api-key) en
`ruimtelijke-plannen-v4` (Ruimtelijke Plannen, header X-Api-Key); fallback `dso.txt`/`rp.txt` in de
hoofdmap (of $DSO_KEY_FILE / $RP_KEY_FILE; gitignored). De sleutels worden nooit geprint. Alleen standaardbibliotheek; draai met `python3 -I`.

Commando's:
  regelingen GM [--ontwerp] [--type RE]       regelingen of ontwerpregelingen van bevoegd gezag (gm0285, pv25)
  vergunningen GM [--grep RE]                 gepubliceerde omgevingsvergunningen (alleen metadata)
  tekst ID [--ontwerp] [--grep RE] [--context N]   regeltekst (identificatie, bv. /akn/nl/act/gm0285/2020/omgevingsplan,
                                                   of technischId bij --ontwerp) als markdown, evt. gefilterd
  pons GM                                     ponsen (tijdelijk deel buiten werking) van het omgevingsplan
  rp-plannen GM4 [--grep RE] [--tam] [--type T] [--alle]   RP-plannen (GM4 = CBS-code zonder 'gm', bv. 0285); standaard alleen geldend
  rp-tekst PLANID [--grep RE] [--context N]   planregels/toelichting als markdown (bv. NL.IMRO.0285.20100-VS00)
  rp-info PLANID                              metadata, status, bekendmakingen en gerelateerde plannen
  locatie X Y                                 RD-punt: Ozon-regelingen/onderwerpen en RP-plannen op die plek
"""
import argparse, html, json, os, re, sys, time, urllib.error, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OZON = 'https://service.omgevingswet.overheid.nl/publiek/omgevingsdocumenten/api/presenteren/v8'
RP = 'https://ruimte.omgevingswet.overheid.nl/ruimtelijke-plannen/api/opvragen/v4'


def _key(env, fname, user):
    """Sleutel uit de keyring (service `dso`), met bestand als fallback (zie srd: § Zoek-API's / keyrings.cryptfile)."""
    p = os.environ.get(env)
    if not p:
        snippet = (
            "import getpass,keyring;from keyrings.cryptfile.cryptfile import CryptFileKeyring;"
            "getpass.getpass=lambda prompt='',stream=None:open('/home/nick/.secrets/keyring_pass').read().strip();"
            f"keyring.set_keyring(CryptFileKeyring());print(keyring.get_password('dso','{user}') or '')")
        try:
            import subprocess
            v = subprocess.run(['/home/nick/.venv/bin/python3', '-I', '-c', snippet], capture_output=True, text=True, timeout=60).stdout.strip()
            if v:
                return v
        except (OSError, subprocess.SubprocessError):
            pass
        p = os.path.join(ROOT, fname)
    try:
        return open(p).read().strip()
    except OSError:
        sys.exit(f'sleutel niet gevonden (keyring dso/{user} en bestand {p})')


def call(url, key, hdr, body=None, crs=None, tries=5):
    h = {hdr: key, 'Accept': 'application/hal+json'}
    if body is not None:
        h['Content-Type'] = 'application/json'
    if crs:
        h['Content-Crs'] = crs
    data = json.dumps(body).encode() if body is not None else None
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, data=data, headers=h), timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code in (429, 502, 503, 504) and i < tries - 1:
                time.sleep(3 * (i + 1)); continue
            sys.exit(f'HTTP {e.code} voor {url.split("?")[0]}')
        except (urllib.error.URLError, TimeoutError):
            if i < tries - 1:
                time.sleep(3 * (i + 1)); continue
            raise


def ozon(path, body=None, crs=None, **q):
    u = (path if path.startswith('http') else OZON + path)
    if q:
        u += ('&' if '?' in u else '?') + urllib.parse.urlencode(q)
    return call(u, _key('DSO_KEY_FILE', 'dso.txt', 'presenteren-v8'), 'x-api-key', body, crs)


def rp(path, body=None, crs=None, **q):
    u = (path if path.startswith('http') else RP + path)
    if q:
        u += ('&' if '?' in u else '?') + urllib.parse.urlencode(q)
    return call(u, _key('RP_KEY_FILE', 'rp.txt', 'ruimtelijke-plannen-v4'), 'X-Api-Key', body, crs)


def pages(fn, path, embedded, body=None, **q):
    out, p = [], 1
    while True:
        j = fn(path, body, page=p, **q)
        out += j.get('_embedded', {}).get(embedded, [])
        if 'next' not in j.get('_links', {}) and p >= j.get('page', {}).get('totalPages', 1):
            return out
        if 'next' not in j.get('_links', {}) and 'totalPages' not in j.get('page', {}):
            return out
        p += 1
        if p > 60:
            return out


def strip(x):
    x = re.sub(r'<(?:/p|/Al|/Li|br ?/?|/h\d|/tr|/Lijst)[^>]*>', '\n', x or '')
    x = re.sub(r'<Li[^>]*>', '- ', x)
    x = re.sub(r'<[^>]+>', ' ', x)
    return re.sub(r'[ \t]+', ' ', html.unescape(x)).strip()


def kop(x):
    if not x:
        return ''
    g = lambda t: (re.search(rf'<{t}[^>]*>(.*?)</{t}>', x, re.S) or [None, ''])[1]
    return ' '.join(s for s in (strip(g('Label')), strip(g('Nummer')), strip(g('Opschrift'))) if s)


def walk(comps, lvl=0, out=None):
    out = [] if out is None else out
    for c in comps:
        k, t = kop(c.get('kop')), strip(c.get('inhoud'))
        if k:
            out.append(f"{'#' * min(lvl + 2, 6)} {k}")
        if t:
            out.append(t)
        walk(c.get('_embedded', {}).get('ontwerpDocumentComponenten', c.get('_embedded', {}).get('documentComponenten', [])), lvl + 1, out)
    return out


def grep_lines(lines, rx, ctx):
    if not rx:
        return lines
    r = re.compile(rx, re.I)
    keep = set()
    for i, l in enumerate(lines):
        if r.search(l):
            keep.update(range(max(0, i - ctx), min(len(lines), i + ctx + 1)))
    out, last = [], -2
    for i in sorted(keep):
        if i != last + 1:
            out.append('…')
        out.append(lines[i]); last = i
    return out


def cache_get(name, fn):
    d = os.path.expanduser('~/.cache/hanzedorp-dso')
    os.makedirs(d, exist_ok=True)
    f = os.path.join(d, re.sub(r'[^A-Za-z0-9._-]', '_', name) + '.json')
    if os.path.exists(f) and time.time() - os.path.getmtime(f) < 6 * 3600:
        return json.load(open(f))
    v = fn()
    json.dump(v, open(f, 'w'))
    return v


def line(x):
    gm = x.get('geregistreerdMet') or {}
    t = (x.get('type') or {}).get('waarde', '')
    return f"{t} | {x.get('officieleTitel', '')[:110]} | inwerking {gm.get('beginInwerking', '-')} | {x['identificatie']}"


def main():
    a = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    s = a.add_subparsers(dest='c', required=True)
    p = s.add_parser('regelingen'); p.add_argument('gm'); p.add_argument('--ontwerp', action='store_true'); p.add_argument('--type')
    p = s.add_parser('vergunningen'); p.add_argument('gm'); p.add_argument('--grep')
    p = s.add_parser('tekst'); p.add_argument('id'); p.add_argument('--ontwerp', action='store_true'); p.add_argument('--grep'); p.add_argument('--context', type=int, default=2)
    p = s.add_parser('pons'); p.add_argument('gm')
    p = s.add_parser('rp-plannen'); p.add_argument('gm4'); p.add_argument('--grep'); p.add_argument('--tam', action='store_true'); p.add_argument('--type'); p.add_argument('--alle', action='store_true')
    p = s.add_parser('rp-tekst'); p.add_argument('planid'); p.add_argument('--grep'); p.add_argument('--context', type=int, default=2)
    p = s.add_parser('rp-info'); p.add_argument('planid')
    p = s.add_parser('locatie'); p.add_argument('x', type=float); p.add_argument('y', type=float)
    A = a.parse_args()
    RD = 'http://www.opengis.net/def/crs/EPSG/0/28992'

    if A.c == 'regelingen':
        path, key = ('/ontwerpregelingen/_zoek', 'ontwerpregelingen') if A.ontwerp else ('/regelingen/_zoek', 'regelingen')
        for x in pages(ozon, path, key, {'bevoegdGezag': [A.gm]}, size=200):
            if not A.type or re.search(A.type, (x.get('type') or {}).get('waarde', ''), re.I):
                if A.ontwerp:
                    print(line(x).rsplit('|', 1)[0], '| technischId', x['_links']['self']['href'].split('/ontwerpregelingen/')[1].split('?')[0])
                else:
                    print(line(x))
    elif A.c == 'vergunningen':
        for x in pages(ozon, '/omgevingsvergunningen/_zoek', 'omgevingsvergunningen', {'bevoegdGezag': [A.gm]}, size=200):
            if not A.grep or re.search(A.grep, x['officieleTitel'], re.I):
                print(f"{(x.get('geregistreerdMet') or {}).get('beginInwerking', '-')} | {x['officieleTitel'][:200]} | {x.get('publicatieID', '')}")
    elif A.c == 'tekst':
        if A.ontwerp:
            base = f"/ontwerpregelingen/{A.id}/documentstructuur"
        else:
            base = f"/regelingen/{A.id.replace('/', '_')}/documentstructuur"

        def load():
            return ozon(base)
        ds = cache_get('ozon' + base, load)
        e = ds.get('_embedded', {})
        lines = [l for t in walk(e.get('ontwerpDocumentComponenten', e.get('documentComponenten', []))) for l in t.split('\n') if l.strip()]
        print('\n'.join(grep_lines(lines, A.grep, A.context)))
    elif A.c == 'pons':
        j = ozon('/regelingen/_zoek', {'bevoegdGezag': [A.gm]}, size=50, _expand='true')
        for x in j['_embedded']['regelingen']:
            if (x.get('type') or {}).get('waarde') == 'Omgevingsplan':
                p = x.get('_embedded', {}).get('pons')
                print(x['identificatie'], 'versie', x['geregistreerdMet'].get('versie'), 'inwerking', x['geregistreerdMet'].get('beginInwerking'))
                if not p:
                    print('geen pons: tijdelijk deel (RP) geldt overal'); continue
                for g in p.get('_embedded', {}).get('omvat', []):
                    print(' pons-gebied', g.get('noemer', ''), g.get('boundingBox'))
    elif A.c == 'rp-plannen':
        q = {'beleidsmatigVerantwoordelijkeOverheid.code': A.gm4, 'pageSize': 100}
        if not A.alle:
            q['regelStatus'] = 'geldend'
        if A.tam:
            q['isTamPlan'] = 'true'
        if A.type:
            q['planType'] = A.type
        out, p = [], 1
        while p < 40:
            j = rp('/plannen', page=p, **q)
            out += j['_embedded']['plannen']
            if 'next' not in j.get('_links', {}):
                break
            p += 1
        for x in sorted(out, key=lambda x: (x.get('planstatusInfo') or {}).get('datum', '')):
            si = x.get('planstatusInfo') or {}
            if not A.grep or re.search(A.grep, x['naam'] + ' ' + x['id'], re.I):
                print(f"{x['id']} | {x['type']} | {x['naam'][:90]} | {si.get('planstatus')} {si.get('datum')} | TAM={x.get('isTamPlan')}")
    elif A.c == 'rp-tekst':
        def load():
            out, p = [], 1
            while p < 80:
                j = rp(f'/plannen/{A.planid}/teksten', page=p, pageSize=100)
                out += j['_embedded']['teksten']
                if 'next' not in j.get('_links', {}):
                    break
                p += 1
            return out
        t = cache_get('rp-' + A.planid, load)
        lines = []
        for x in t:
            lines.append(f"## {x['titel']}")
            if x.get('inhoud'):
                lines += [l for l in strip(x['inhoud']).split('\n') if l.strip()]
        print('\n'.join(grep_lines(lines, A.grep, A.context)))
    elif A.c == 'rp-info':
        j = rp(f'/plannen/{A.planid}')
        print(json.dumps({k: j.get(k) for k in ('id', 'type', 'naam', 'beleidsmatigVerantwoordelijkeOverheid', 'planstatusInfo', 'besluitnummer', 'regelStatus', 'regelBinding', 'isTamPlan', 'eindeRechtsgeldigheid', 'isHistorisch', 'verwijzingNaarVaststellingsbesluit', 'dossier')}, ensure_ascii=False, indent=1))
        for sub in ('bekendmakingen', 'gerelateerde-plannen'):
            try:
                print(sub, json.dumps(rp(f'/plannen/{A.planid}/{sub}'), ensure_ascii=False)[:1500])
            except SystemExit:
                print(sub, 'niet beschikbaar')
    elif A.c == 'locatie':
        geo = {'type': 'Point', 'coordinates': [A.x, A.y]}
        print('== Ozon regelingen op deze plek')
        for x in ozon('/regelingen/_zoek', {'geometrie': geo}, crs=RD, size=200).get('_embedded', {}).get('regelingen', []):
            print(line(x))
        print('== Ozon onderwerpen (activiteiten/gebiedsaanwijzingen)')
        print(json.dumps(ozon('/onderwerpen/_zoek', {'geometrie': geo}, crs=RD), ensure_ascii=False)[:3000])
        print('== RP-plannen (geldend)')
        for x in rp('/plannen/_zoek', {'_geo': {'intersects': geo}}, crs='epsg:28992', regelStatus='geldend', pageSize=100).get('_embedded', {}).get('plannen', []):
            print(f"{x['id']} | {x['type']} | {x['naam'][:80]}")


if __name__ == '__main__':
    main()
