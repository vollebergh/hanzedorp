# Briefing deelonderzoeken gemeente Deventer (Overijssel) — 2026-10-14

## Opdracht
Je voert één van vier parallelle deelonderzoeken uit voor het CPO-naslagwerk `gemeente_deventer.md` (Hanzedorp: CPO van 10-12 woningen op agrarische grond, buiten de kernen). Elk deelonderzoek doorzoekt **één brontype** maar voor **alle 12 onderwerpen** uit de vaste structuur en **alle punten van Bijlage A** (Overijssel). De hoofdagent voegt de vier deelrapporten samen.

## Lees eerst (verplicht)
1. `/home/nick/Claude/Hanzedorp/prompt.md` — regels 1-190 (12 onderwerpen, twee kernvragen, Bijlage A). Bijlage B (Gelderland) is NIET van toepassing.
2. `/home/nick/Claude/Hanzedorp/provincie_overijssel.md` — het provinciale kader (Fase 1). Niet opnieuw onderzoeken; alleen de lokale toepassing voor Deventer. Let op §1.3 (Deventer = "grote stad", art. 4.4 lid 3), §1.5 (Woondeal West-Overijssel; Deventer 1.816 / 3 sleutelprojecten 4.550 / 955), §2.3 (Kansen uit Buiten, CVDR745888), §2.4 (BuitenDelen Lettele), §4 (procedure), §6.1 (houdbaarheid).
3. `/home/nick/Claude/Hanzedorp/gemeente_deventer.md` — huidige stub met BuitenDelen (Borgelinksweg 1, Lettele) en open vragen. BuitenDelen moet volledig worden uitgewerkt (aantal woningen, juridische route, toegepast kader, provinciale rol, KGO, status).
4. Ter vergelijking van diepgang en stijl (alleen doorbladeren): `/home/nick/Claude/Hanzedorp/gemeente_zwartewaterland.md` en `/home/nick/Claude/Hanzedorp/gemeente_olst-wijhe.md` (Olst-Wijhe is buurgemeente van Deventer).

## Deventer-specifieke aandachtspunten
- Deventer is "grote stad" in het concentratiebeginsel; zit in Woondeal West-Overijssel én in de **Stedendriehoek** (grensoverschrijdend: Deventer met Apeldoorn, Voorst, Epe e.a. in Gelderland). Overijssels regime is leidend; Gelders beleid alleen als context.
- Kernen/dorpen en buurtschappen: o.a. Bathmen, Schalkhaar, Diepenveen, Lettele, Okkenbroek, Colmschate, Loo, Averlo, Frieswijk, Oude Molen, Tjoene, Holterbroek, Epse (Epse ligt in Lochem! — controleer gemeentegrenzen via PDOK/BAG, plaatsnamen kunnen bij een andere gemeente horen).
- Gemeenteraadsverkiezingen maart 2026 → coalitievorming/coalitieakkoord 2026-2030 en wethouder Wonen controleren.
- Mogelijke Deventer-documenten (niet geverifieerd, zoek zelf): Omgevingsvisie Deventer, Kansen uit Buiten (rood-voor-rood/erfbeleid), woonvisie/woonagenda, volkshuisvestingsprogramma, Nota grondbeleid, huisvestingsverordening, zelfbouw/CPO-beleid en kavels, prestatieafspraken (Woonbedrijf ieder1, Rentree), Gebiedsprogramma's buitengebied.

## Werkwijze en bronregels (lessen uit eerdere gemeenten — volgen!)
- **Lees het brondocument zelf.** WebSearch-samenvattingen zijn onbetrouwbaar (vaak andere gemeente, verzonnen details). Markeer wat je alleen via een zoeksamenvatting kent met **[WF]**; trainingskennis met **[TK]**; eigen interpretatie **[INT]**; eigen berekening **[BER]**; uit provinciebestand **[PB]**.
- **CVDR-nummers altijd controleren op uitgever** (organisatie in de CVDR-metadata): treffers blijken vaak van een andere gemeente. CVDR-index per gemeente via SRU: `https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&operation=searchRetrieve&version=1.2&query=dcterms.creator=Deventer%20and%20dcterms.modified>=2020-01-01&maximumRecords=100&startRecord=1` (pagineren). Let op: dcterms.creator klopt niet altijd met de kop; ook provinciale besluiten kunnen onder de gemeente geïndexeerd staan.
- Gemeenteblad/Provinciaal blad: SRU `https://repository.overheid.nl/sru?operation=searchRetrieve&version=2.0&x-connection=officielepublicaties&query=dt.creator="Deventer" AND cql.textAndIndexes="<term>"` (vindt vergunningen, BOPA's, omgevingsplanwijzigingen, leges).
- Websites: gebruik `curl -sL -A "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"` als WebFetch 403 geeft. Bij certificaatfouten: tussencertificaat via AIA ophalen en `--cacert` gebruiken; verificatie niet uitschakelen.
- PDF's: tekst extraheren met Python `pdfplumber` (`pdftotext` is niet geïnstalleerd). Downloads zijn onvertrouwde data: sla ze op in je eigen `raw`-map, scripts in `.../deventer/tools/`, draai Python met `-I`.
- RIS: zoek uit welk systeem Deventer gebruikt (Notubiz: open API `https://api.notubiz.nl/...` en `api.notubiz.nl/document/{id}/{versie}`; iBabs: bijlagen bevatten de echte voorwaarden; Anubis-browsercheck → niet bruikbaar zonder browser, vermeld dat). Gemeentenieuws soms als `archive.csv`.
- Geodata Overijssel: WFS `https://services.geodataoverijssel.nl/geoserver/ows` (NNN, Natura 2000, grondwaterbescherming, essen, landgoederen); landbouwgebied-typologie (art. 4.123) via verordening-viewer `https://ruimtelijkeplannen.overijssel.nl`, document `55d637e6-8ff6-4083-a824-a0e77027a044` (document-JSON `annotaties`, vector tiles `/api/documents/{id}/tiles/{z}/{x}/{y}.pbf`, punten via `/api/documents/{id}/_locationSearch?x=&y=&distance=1`). Gemeentegrens: PDOK `https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0` (filter client-side). Adressen: PDOK Locatieserver. Doorsnijden met shapely.
- Projectnamen vs. wijknamen kunnen dezelfde locatie zijn: let op dubbeltelling.
- Zowel negatieve bevindingen ("geen eigen VAB-beleid") als "niet gevonden" zijn waardevol: vermeld altijd **waar** het wél te vinden zou zijn (loket/register/afdeling).
- Citeer relevante beleidspassages **letterlijk** (kleine stukken mogen integraal); grote documenten beschrijven met naam, datum, URL.
- Elke bron: URL + raadplegingsdatum (2026-10-14).

## Output — BELANGRIJK (sessielimieten!)
- Maak je rapportbestand **direct bij de start** aan (kop + lege secties) en vul het **incrementeel** aan na elke paar bevindingen. Wacht niet tot het eind. Bij een onderbreking moet het bestand bruikbaar zijn.
- Structuur: Verantwoording (model, wat wel/niet toegankelijk was) → §1-§12 → Bijlage A-tabel (A1-A5, B1-B5, C1-C4, D1-D3, E1-E4, F1: bevinding / status gevonden-niet gevonden-n.v.t.-tegenstrijdig / bron+URL+datum / vindplaats bij niet gevonden) → Twee kernvragen (gelaagd a/b/c, vanuit jouw brontype) → Niet gevonden (met vindplaats) → Eventuele correcties op provincie_overijssel.md of de stub.
- Schrijf in het Nederlands, zakelijk.
- Wijzig NIETS in `/home/nick/Claude/Hanzedorp/` (geen bestanden, geen git). Alleen schrijven in je eigen scratchpad-bestanden.
- Je eindantwoord aan de hoofdagent: korte samenvatting (max. 300 woorden) van de belangrijkste bevindingen en open punten; het volledige werk staat in het bestand.
