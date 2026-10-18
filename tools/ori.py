#!/usr/bin/env python3
"""Client voor de Open Besluitvorming-API (https://openbesluitvorming.nl).

Alleen standaardbibliotheek (SQLite FTS5 voor de lokale index). Uitvoer van
de API is onbetrouwbare data: er wordt nooit iets uit uitgevoerd.
Gebruik: python3 -I tools/ori.py --help
"""
import argparse
import datetime as dt
import json
import os
import re
import sqlite3
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

BASE = "https://openbesluitvorming.nl"
UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/124.0 Safari/537.36")
DEFAULT_CACHE = os.path.expanduser("~/.cache/hanzedorp-ori")
TYPES = ("Meeting", "Document", "Motion", "Recording")
# Zoeken is gemiddeld ~1000 resultaten diep bereikbaar; houd marge.
MAX_DEPTH = 900


def eprint(*a):
    print(*a, file=sys.stderr, flush=True)


class Client:
    """HTTP-client met rate limiting (standaard 40 eenheden/min), 429/5xx-afhandeling."""

    def __init__(self, rate=40.0, retries=6):
        self.interval = 60.0 / rate
        self.retries = retries
        self.last = 0.0
        self.remaining = None
        self.reset = 0

    def _pace(self, cost):
        wait = self.interval * cost - (time.monotonic() - self.last)
        if wait > 0:
            time.sleep(wait)
        if self.remaining is not None and self.remaining < 5:
            time.sleep(min(max(self.reset, 1), 60))
            self.remaining = None
        self.last = time.monotonic()

    def request(self, path, params=None, cost=1.0, raw=False):
        url = BASE + path
        if params:
            url += "?" + urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
        for attempt in range(self.retries):
            self._pace(cost)
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=60) as f:
                    h = f.headers
                    body = f.read()
                self._note(h)
                return (body if raw else json.loads(body)), h
            except urllib.error.HTTPError as e:
                if e.code == 429:
                    ra = int(e.headers.get("Retry-After") or 5)
                    eprint(f"429: {ra}s wachten (langzamer, geen fout)")
                    time.sleep(ra + 1)
                    continue
                if e.code >= 500:
                    eprint(f"HTTP {e.code} bij {path}; poging {attempt + 1}/{self.retries}")
                    time.sleep(2 ** (attempt + 1))
                    continue
                try:
                    info = json.load(e)
                except Exception:
                    info = {}
                raise ApiError(e.code, info.get("code"), info.get("error") or str(e))
            except (urllib.error.URLError, TimeoutError, ConnectionError) as e:
                eprint(f"Netwerkfout bij {path}: {e}; poging {attempt + 1}/{self.retries}")
                time.sleep(2 ** (attempt + 1))
        raise ApiError(0, "retries_exhausted", f"Opgegeven na {self.retries} pogingen: {path}")

    def _note(self, h):
        try:
            self.remaining = float(h.get("RateLimit-Remaining"))
            self.reset = float(h.get("RateLimit-Reset") or 0)
        except (TypeError, ValueError):
            self.remaining = None


class ApiError(Exception):
    def __init__(self, status, code, msg):
        super().__init__(f"HTTP {status} [{code}]: {msg}")
        self.status, self.code = status, code


def search_cost(limit):
    return 1.0 if limit <= 24 else 1.0 + (limit - 24) / 250.0


def search_page(c, query, org, etype, dfrom, dto, sort, limit, offset):
    return c.request("/api/search", dict(
        query=query or None, organization=org, entityType=etype, dateFrom=dfrom,
        dateTo=dto, sort=sort, limit=limit, offset=offset), cost=search_cost(limit))[0]


def iter_search(c, a, dfrom, dto, limit=100):
    """Alle resultaten voor een venster; splitst het venster als de diepte wordt overschreden."""
    off = 0
    got = []
    while True:
        d = search_page(c, a.query, a.org, a.type, dfrom, dto, a.sort, limit, off)
        got += d["results"]
        if not d.get("hasMore") or not d["results"]:
            return got
        off += len(d["results"])
        if off >= MAX_DEPTH:
            break
    # te diep: venster halveren (alleen mogelijk met datumgrenzen)
    f = dt.date.fromisoformat(dfrom)
    t = dt.date.fromisoformat(dto)
    if f >= t:
        eprint(f"Waarschuwing: >{MAX_DEPTH} treffers op één dag ({dfrom}); rest ontbreekt.")
        return got
    mid = f + (t - f) // 2
    seen = {}
    for lo, hi in ((f, mid), (mid + dt.timedelta(days=1), t)):
        for r in iter_search(c, a, lo.isoformat(), hi.isoformat(), limit):
            seen[r["entityId"]] = r
    return list(seen.values())


def cmd_search(a):
    c = Client(a.rate)
    if a.alles:
        dfrom = a.date_from or "2010-01-01"
        dto = a.date_to or dt.date.today().isoformat()
        res = iter_search(c, a, dfrom, dto)
        uniq = {r["entityId"]: r for r in res}
        res = list(uniq.values())
    else:
        d = search_page(c, a.query, a.org, a.type, a.date_from, a.date_to, a.sort, a.limit, a.offset)
        res = d["results"]
        eprint(f"totaal: {d.get('totalCount')}{'~' if d.get('totalIsApproximate') else ''}, meer: {d.get('hasMore')}")
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return
    for r in res:
        print(f"{(r.get('sortDate') or '')[:10]}  {r['entityType']:<8} {r['entityId']}\n    {r.get('title')}")
        if a.summary and r.get("summary"):
            print("    " + re.sub(r"\s+", " ", r["summary"])[:200])


def safe(entity_id):
    return re.sub(r"[^A-Za-z0-9._-]", "_", entity_id)


def fetch_entity(c, entity_id):
    return c.request("/api/entities/" + urllib.parse.quote(entity_id, safe=""))[0]


def fmt_time(s):
    s = int(s or 0)
    return f"{s // 3600:d}:{s % 3600 // 60:02d}:{s % 60:02d}"


def entity_to_md(e, transcript=False, meeting=False):
    """Zet een entiteit om naar markdown met frontmatter."""
    today = dt.date.today().isoformat()
    fm = {
        "entityId": e.get("entityId"), "titel": e.get("title"),
        "type": e.get("entityType"), "organisatie": e.get("organization"),
        "vergaderdatum": (e.get("sortDate") or "")[:10],
        "dateModified": e.get("dateModified"), "meetingId": e.get("meetingId"),
        "downloadUrl": e.get("downloadUrl"), "pdfUrl": e.get("pdfUrl"),
        "ophaaldatum": today,
    }
    out = ["---"] + [f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in fm.items() if v] + ["---", ""]
    out.append(f"# {e.get('title') or e.get('entityId')}\n")
    if e.get("markdownText"):
        out.append(e["markdownText"])
    if e.get("motion"):
        m = e["motion"]
        out.append(f"## Motie\n\nResultaat: {m.get('result')} ({m.get('status')}); stemmen: {m.get('tally')}\n")
    if e.get("agenda") is not None:
        out.append("## Agenda\n")

        def walk(items, depth=0):
            for it in items or []:
                out.append(f"{'  ' * depth}- {it.get('number') or ''} {it.get('title') or ''}".rstrip())
                for d in it.get("documents") or []:
                    out.append(f"{'  ' * (depth + 1)}- [doc] {d.get('name')} — `{d.get('id')}`")
                walk(it.get("agenda_items"), depth + 1)
        walk(e["agenda"])
        out.append("")
    if e.get("motions"):
        out.append("## Moties en amendementen\n")
        for m in e["motions"]:
            t = m.get("tally") or {}
            out.append(f"- {m.get('name')}: **{m.get('result')}** (voor {t.get('in_favour', '?')}, "
                       f"tegen {t.get('against', '?')}) — `{m.get('id')}`"
                       + (f"; bijlage `{m['attachment_id']}`" if m.get("attachment_id") else ""))
        out.append("")
    for r in e.get("recordings") or []:
        out.append(f"## Opname ({r.get('media_type')}, {fmt_time(r.get('duration_seconds'))}, "
                   f"transcript: {r.get('transcript_kind')} — spraakherkenning, onbetrouwbaar)\n")
        for ch in r.get("chapters") or []:
            out.append(f"- {fmt_time(ch.get('start_seconds'))} {ch.get('title')}")
        if transcript:
            out.append("")
            for s in r.get("segments") or []:
                out.append(f"[{fmt_time(s.get('start_seconds'))}] {s.get('text')}")
        out.append("")
    return "\n".join(out) + "\n"


def cmd_get(a):
    c = Client(a.rate)
    e = fetch_entity(c, a.entity_id)
    if a.json:
        print(json.dumps(e, ensure_ascii=False, indent=1))
        return
    md = entity_to_md(e, transcript=a.transcript, meeting=a.meeting)
    if a.meeting and e.get("entityType") == "Meeting":
        docs = []

        def collect(items):
            for it in items or []:
                docs.extend(d.get("id") for d in it.get("documents") or [])
                collect(it.get("agenda_items"))
        collect(e.get("agenda"))
        md += "## Bijbehorende documenten\n\n" + "\n".join(f"- `{d}`" for d in dict.fromkeys(docs) if d) + "\n"
    out = a.out
    if out:
        if os.path.isdir(out):
            out = os.path.join(out, safe(a.entity_id) + ".md")
        with open(out, "w", encoding="utf-8") as f:
            f.write(md)
        eprint("opgeslagen:", out)
    else:
        sys.stdout.write(md)


# ---------------------------------------------------------------- harvest

def src_dir(cache, src):
    d = os.path.join(cache, src)
    os.makedirs(os.path.join(d, "entities"), exist_ok=True)
    return d


def load_state(d):
    try:
        with open(os.path.join(d, "state.json")) as f:
            return json.load(f)
    except (OSError, ValueError):
        return {}


def save_state(d, st):
    tmp = os.path.join(d, "state.json.tmp")
    with open(tmp, "w") as f:
        json.dump(st, f)
    os.replace(tmp, os.path.join(d, "state.json"))


def ndjson_records(body):
    for line in body.decode("utf-8").split("\n"):
        if line.strip():
            yield json.loads(line)


def harvest_feed(c, d, st, kind, log):
    """Haal snapshot- of changes-pagina's op en sla de cursor na elke pagina op."""
    key = "snapshot_cursor" if kind == "snapshot" else "changes_cursor"
    n = 0
    while True:
        params = {"source": st["source"], "limit": 1000, "cursor": st.get(key)}
        body, h = c.request(f"/api/export/{kind}", params, raw=True)
        recs = list(ndjson_records(body))
        for r in recs:
            log.write(json.dumps(r, ensure_ascii=False) + "\n")
        log.flush()
        os.fsync(log.fileno())
        n += len(recs)
        if kind == "snapshot" and not st.get("changes_cursor_start") and h.get("X-Changes-Cursor"):
            st["changes_cursor_start"] = h.get("X-Changes-Cursor")
        nxt = h.get("X-Next-Cursor")
        if nxt:
            st[key] = nxt
        more = (h.get("X-Has-More") or "").lower() == "true"
        if kind == "snapshot" and not more:
            st["snapshot_done"] = True
            st.setdefault("changes_cursor", st.get("changes_cursor_start"))
        save_state(d, st)
        eprint(f"{kind}: {n} records")
        if not more:
            return n


def harvest_search_fallback(c, d, st, log, dfrom):
    """Fallback: per maand via /api/search, records in dezelfde vorm als de export."""
    start = dt.date.fromisoformat(st.get("fallback_month") or dfrom)
    today = dt.date.today() + dt.timedelta(days=120)  # agenda's liggen in de toekomst
    ns = argparse.Namespace(query=None, org=st["source"], type=None, sort="date_asc")
    cur = start.replace(day=1)
    while cur <= today:
        nxt = (cur.replace(day=28) + dt.timedelta(days=4)).replace(day=1)
        res = iter_search(c, ns, cur.isoformat(), (nxt - dt.timedelta(days=1)).isoformat())
        for r in res:
            log.write(json.dumps({
                "op": "upsert", "entity_id": r["entityId"], "entity_type": r["entityType"],
                "source_key": st["source"], "content_hash": None,
                "payload": {"name": r.get("title"), "sort_date": r.get("sortDate"),
                            "download_url": r.get("downloadUrl")}}, ensure_ascii=False) + "\n")
        log.flush()
        os.fsync(log.fileno())
        st["fallback_month"] = nxt.isoformat()
        save_state(d, st)
        eprint(f"zoek-fallback {cur:%Y-%m}: {len(res)} resultaten")
        cur = nxt
    st["snapshot_done"] = True
    st["via_search"] = True
    save_state(d, st)


def current_entities(d):
    """Lees het log; laatste record wint, deletes verwijderen."""
    ents = {}
    p = os.path.join(d, "records.ndjson")
    if not os.path.exists(p):
        return ents
    with open(p, encoding="utf-8") as f:
        for line in f:
            try:
                r = json.loads(line)
            except ValueError:
                continue  # half weggeschreven regel na onderbreking
            if r.get("op") == "delete":
                ents.pop(r["entity_id"], None)
            else:
                ents[r["entity_id"]] = r
    return ents


def entity_path(d, eid):
    return os.path.join(d, "entities", safe(eid) + ".json")


def cmd_harvest(a):
    c = Client(a.rate)
    d = src_dir(a.cache, a.gemeente)
    st = load_state(d)
    st["source"] = a.gemeente
    log = open(os.path.join(d, "records.ndjson"), "a", encoding="utf-8")
    try:
        if not st.get("snapshot_done"):
            n = harvest_feed(c, d, st, "snapshot", log) if not st.get("via_search") else 0
            if n == 0 and not st.get("snapshot_cursor"):
                eprint("Snapshot leeg; terugval op zoeken per maand.")
                harvest_search_fallback(c, d, st, log, a.vanaf)
        elif not st.get("via_search"):
            harvest_feed(c, d, st, "changes", log)
        else:
            harvest_search_fallback(c, d, st, log, a.vanaf)
    finally:
        log.close()
    ents = current_entities(d)
    want = set(a.types.split(","))
    todo = []
    for eid, r in ents.items():
        if r.get("entity_type") not in want:
            continue
        p = entity_path(d, eid)
        if os.path.exists(p):
            try:
                with open(p, encoding="utf-8") as f:
                    if json.load(f).get("_hash") == r.get("content_hash"):
                        continue
            except ValueError:
                pass
        todo.append(eid)
    def pick(eid):
        pl = ents[eid].get("payload") or {}
        if a.naam and not re.search(a.naam, pl.get("name") or "", re.I):
            return False
        if a.klasse and not re.search(a.klasse, " ".join(pl.get("classification") or []), re.I):
            return False
        datum = (pl.get("last_discussed_at") or pl.get("date_modified") or pl.get("sort_date") or "")[:10]
        return not a.sinds or datum >= a.sinds

    def sortkey(eid):
        pl = ents[eid].get("payload") or {}
        return (pl.get("last_discussed_at") or pl.get("date_modified") or pl.get("sort_date") or "")

    todo = sorted((e for e in todo if pick(e)), key=sortkey, reverse=True)  # nieuwste eerst
    if a.max is not None:
        todo = todo[:a.max]
    eprint(f"{len(ents)} entiteiten in log; {len(todo)} details op te halen")
    for i, eid in enumerate(todo, 1):
        try:
            e = fetch_entity(c, eid)
        except ApiError as ex:
            eprint(f"overgeslagen {eid}: {ex}")
            continue
        tmp = entity_path(d, eid) + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump({"_hash": ents[eid].get("content_hash"), "_fetched": dt.date.today().isoformat(),
                       "data": e}, f, ensure_ascii=False)
        os.replace(tmp, entity_path(d, eid))
        if i % 50 == 0:
            eprint(f"details {i}/{len(todo)}")
    counts = {}
    for r in ents.values():
        counts[r["entity_type"]] = counts.get(r["entity_type"], 0) + 1
    print(json.dumps({"bron": a.gemeente, "via": "zoeken" if st.get("via_search") else "export",
                      "entiteiten": counts, "details_opgehaald": len(todo)}, ensure_ascii=False))


# ---------------------------------------------------------------- index / grep

def meeting_text(e, include_transcript):
    parts = []

    def walk(items):
        for it in items or []:
            parts.append(f"{it.get('number') or ''} {it.get('title') or ''}")
            parts.extend(d.get("name") or "" for d in it.get("documents") or [])
            walk(it.get("agenda_items"))
    walk(e.get("agenda"))
    for m in e.get("motions") or []:
        parts.append(f"Motie: {m.get('name')} — {m.get('result')}")
    if include_transcript:
        for r in e.get("recordings") or []:
            parts.extend(s.get("text") or "" for s in r.get("segments") or [])
    return "\n".join(parts)


def cmd_index(a):
    d = src_dir(a.cache, a.gemeente)
    db = os.path.join(d, "index.sqlite")
    if os.path.exists(db):
        os.remove(db)
    con = sqlite3.connect(db)
    con.execute("CREATE VIRTUAL TABLE fts USING fts5(title, body, entity_id UNINDEXED, "
                "etype UNINDEXED, date UNINDEXED, url UNINDEXED, tokenize='unicode61 remove_diacritics 2')")
    ents = current_entities(d)
    n = 0
    for eid, r in ents.items():
        p = entity_path(d, eid)
        if not os.path.exists(p):
            continue
        with open(p, encoding="utf-8") as f:
            e = json.load(f)["data"]
        et = e.get("entityType")
        if et == "Meeting":
            body = meeting_text(e, a.transcript)
        else:
            body = e.get("markdownText") or ""
            if e.get("motion"):
                body += f"\nMotie {e['motion'].get('name')} {e['motion'].get('result')}"
        url = e.get("downloadUrl") or e.get("pdfUrl") or ""
        con.execute("INSERT INTO fts VALUES (?,?,?,?,?,?)",
                    (e.get("title") or "", body, eid, et, (e.get("sortDate") or "")[:10], url))
        n += 1
    con.commit()
    con.close()
    print(f"{n} entiteiten geïndexeerd in {db}")


def fts_query(term):
    """Vrije tekst naar veilige FTS5-query: "frase" blijft frase, losse woorden AND."""
    toks = re.findall(r'"([^"]+)"|(\S+)', term)
    out = []
    for phrase, word in toks:
        txt = phrase or word
        words = re.findall(r"\w+", txt)
        if not words:
            continue
        out.append('"' + " ".join(words) + '"')
    return " AND ".join(out)


def cmd_grep(a):
    db = os.path.join(a.cache, a.gemeente, "index.sqlite")
    if not os.path.exists(db):
        sys.exit(f"Geen index voor {a.gemeente}; draai eerst: harvest en index.")
    q = fts_query(a.zoekterm)
    if not q:
        sys.exit("Lege zoekterm.")
    sql = ("SELECT title, snippet(fts, 1, '«', '»', ' … ', 24), entity_id, etype, date, url "
           "FROM fts WHERE fts MATCH ?")
    args = [q]
    if a.type:
        sql += " AND etype = ?"
        args.append(a.type)
    if a.date_from:
        sql += " AND date >= ?"
        args.append(a.date_from)
    if a.date_to:
        sql += " AND date <= ? "
        args.append(a.date_to)
    sql += " ORDER BY rank LIMIT ?"
    args.append(a.limit)
    rows = sqlite3.connect(db).execute(sql, args).fetchall()
    if a.json:
        keys = ("titel", "snippet", "entityId", "type", "datum", "downloadUrl")
        print(json.dumps([dict(zip(keys, r)) for r in rows], ensure_ascii=False, indent=1))
        return
    for t, sn, eid, et, date, url in rows:
        print(f"{date}  {et:<8} {t}\n    {eid}\n    {url}\n    {re.sub(chr(10), ' ', sn)}\n")
    eprint(f"{len(rows)} treffers")


def main():
    cache_default = os.environ.get("ORI_CACHE", DEFAULT_CACHE)
    p = argparse.ArgumentParser(
        description="Client voor Open Besluitvorming (raadsinformatie). Sleutels per gemeente: "
                    "zie /api/sources (bijv. voorst, hattem, apeldoorn).")
    p.add_argument("--cache", default=cache_default, help=f"cachemap (standaard {cache_default}, of $ORI_CACHE)")
    p.add_argument("--rate", type=float, default=40.0, help="max. eenheden per minuut (limiet is 60; standaard 40)")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("search", help="zoeken via de API")
    s.add_argument("query", nargs="?", help='zoektekst; "zin" voor frase')
    s.add_argument("--org", help="bronsleutel, bijv. voorst")
    s.add_argument("--type", choices=TYPES)
    s.add_argument("--date-from", help="JJJJ-MM-DD")
    s.add_argument("--date-to", help="JJJJ-MM-DD (inclusief)")
    s.add_argument("--sort", default="date_desc", choices=["date_desc", "date_asc", "title_asc", "relevance"])
    s.add_argument("--limit", type=int, default=24)
    s.add_argument("--offset", type=int, default=0)
    s.add_argument("--alles", action="store_true", help="alle treffers ophalen, venster automatisch splitsend voorbij ~1000")
    s.add_argument("--summary", action="store_true", help="toon fragment bij elk resultaat")
    s.add_argument("--json", action="store_true")
    s.set_defaults(f=cmd_search)

    g = sub.add_parser("get", help="entiteit ophalen en als markdown opslaan")
    g.add_argument("entity_id")
    g.add_argument("--meeting", action="store_true", help="vergadering: voeg lijst bijbehorende documenten toe")
    g.add_argument("--transcript", action="store_true", help="neem spraakherkenning-transcript op (asr, onbetrouwbaar)")
    g.add_argument("--out", help="bestand of map; standaard stdout")
    g.add_argument("--json", action="store_true")
    g.set_defaults(f=cmd_get)

    h = sub.add_parser("harvest", help="bron lokaal binnenhalen (export, anders zoeken per maand); hervatbaar. Details kosten 1 eenheid per stuk: beperk met --klasse/--naam/--sinds")
    h.add_argument("gemeente")
    h.add_argument("--types", default="Document,Meeting", help="types waarvan details (tekst) worden opgehaald")
    h.add_argument("--naam", help="regex: haal alleen details van stukken met deze titel (hoofdletterongevoelig)")
    h.add_argument("--klasse", help="regex op classificatie, bijv. 'raadsvoorstel|raadsmededeling|besluitenlijst'")
    h.add_argument("--sinds", help="alleen stukken besproken/gewijzigd vanaf JJJJ-MM-DD")
    h.add_argument("--max", type=int, help="maximaal aantal detailaanroepen in deze run")
    h.add_argument("--vanaf", default="2015-01-01", help="startdatum voor de zoek-fallback")
    h.set_defaults(f=cmd_harvest)

    i = sub.add_parser("index", help="lokale SQLite FTS5-index bouwen")
    i.add_argument("gemeente")
    i.add_argument("--transcript", action="store_true", help="transcripties meenemen in de index")
    i.set_defaults(f=cmd_index)

    r = sub.add_parser("grep", help="zoeken in de lokale index")
    r.add_argument("gemeente")
    r.add_argument("zoekterm")
    r.add_argument("--type", choices=TYPES)
    r.add_argument("--date-from")
    r.add_argument("--date-to")
    r.add_argument("--limit", type=int, default=20)
    r.add_argument("--json", action="store_true")
    r.set_defaults(f=cmd_grep)

    a = p.parse_args()
    try:
        a.f(a)
    except ApiError as e:
        sys.exit(f"API-fout: {e}")
    except KeyboardInterrupt:
        sys.exit("Onderbroken; hervat met hetzelfde commando.")


if __name__ == "__main__":
    main()
