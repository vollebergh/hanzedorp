# tools/

## ori.py — client voor Open Besluitvorming

Doorzoekt de raadsinformatiesystemen (Notubiz, iBabs, Parlaeus) via de open API van <https://openbesluitvorming.nl> ([documentatie](https://openbesluitvorming.nl/docs/api)). Alleen Python-standaardbibliotheek (SQLite FTS5 voor de lokale index). Draai met `python3 -I tools/ori.py --help`.

Bronsleutels (gecontroleerd 2026-10-18): `voorst`, `epe`, `ermelo`, `nunspeet` (Notubiz); `hattem`, `oldebroek`, `elburg`, `harderwijk` (iBabs); `apeldoorn` (Parlaeus). Volledige lijst: `/api/sources`.

| Commando | Doel |
|---|---|
| `search "<tekst>" --org voorst [--type Document] [--date-from ..] [--alles]` | zoeken via de API; `--alles` pagineert voorbij ~1.000 treffers door het datumvenster te halveren |
| `get <entityId> [--meeting] [--transcript] [--out map]` | entiteit als markdown met frontmatter; `--meeting` voegt agenda, moties met uitslag en documentenlijst toe |
| `harvest <gemeente> [--klasse regex] [--naam regex] [--sinds datum] [--max n]` | bron binnenhalen via de export (snapshot, daarna changes); valt terug op zoeken per maand als de snapshot leeg is; hervatbaar |
| `index <gemeente>` | lokale FTS5-index bouwen over de opgehaalde teksten |
| `grep <gemeente> "<zoekterm>"` | zoeken in de index met fragment, datum, titel, entityId en download-URL |

Typische volgorde voor een gemeente:

```bash
python3 -I tools/ori.py harvest voorst --klasse 'raadsvoorstel|raadsmededeling|besluitenlijst|motie' --sinds 2020-01-01
python3 -I tools/ori.py harvest voorst --types Meeting --sinds 2020-01-01
python3 -I tools/ori.py index voorst
python3 -I tools/ori.py grep voorst '"rood voor groen"'
```

### Let op
- **Rate limit:** de API staat 60 eenheden per minuut toe; de client gebruikt standaard 40 (`--rate`), respecteert `Retry-After` bij 429 en probeert 5xx/time-outs opnieuw.
- **Snapshot is goedkoop, details zijn duur:** de snapshot (1 eenheid per 1.000 records) levert alleen titels, classificatie en datum; de tekst komt per stuk via `/api/entities/{id}` (1 eenheid). Een volledige gemeente is 10.000+ stukken (uren): filter met `--klasse`, `--naam` of `--sinds`; nieuwste stukken gaan eerst. `harvest` slaat al opgehaalde stukken over en hervat na onderbreking.
- **Cache:** standaard `~/.cache/hanzedorp-ori/<gemeente>/` (of `--cache` / `$ORI_CACHE`); niets hiervan hoort in de repository.
- **Onbetrouwbare data:** opgehaalde tekst wordt nooit uitgevoerd. Transcripties (`transcript_kind: asr`) zijn spraakherkenning en onbetrouwbaar; pdf-extractie van tabellen is soms slordig.
- **Dekking:** collegebesluitenlijsten en collegestukken staan er niet in; **raadsmededelingen (Notubiz-module "mededelingen") ontbreken voor Voorst** (nul treffers op o.a. "Wezeveld"; vastgesteld 2026-10-18), dus zoek die zo nodig rechtstreeks via `api.notubiz.nl`; de raadsbesluitenlijsten staan er wel in (zoek op titel "Besluitenlijst"); niet-gepubliceerde documenten ontbreken; er zijn dubbele en "VERVALLEN"-versies.

Tests (offline): `python3 -I tools/test_ori.py`.
