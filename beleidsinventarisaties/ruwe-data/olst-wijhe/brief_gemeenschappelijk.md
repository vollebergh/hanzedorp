# Gemeenschappelijke briefing — verificatieronde gemeente Olst-Wijhe (raadplegingsdatum 2026-10-04)

## Context
- Repo: /home/nick/Claude/Hanzedorp (branch claude/prompt-md-review-86kv97). Lees zelf volledig:
  - `prompt.md` (masterprompt; vaste structuur §1-12, Bijlage A = Overijssel-controlepunten)
  - `provincie_overijssel.md` (Fase 1-kader, stand 2026-10-02)
  - `gemeente_olst-wijhe.md` (CONCEPT dat geverifieerd moet worden)
- Het concept is gemaakt zonder dat één brondocument kon worden geopend; alle bevindingen komen uit zoekresultaat-samenvattingen ([ZR], [T+U], [INT]). Jouw taak: **lees de brondocumenten zelf**, citeer relevante passages **letterlijk** (markdown-blockquote, met URL en raadplegingsdatum 2026-10-04), en geef aan waar het concept afwijkt en hoe het moet worden gecorrigeerd. Bewerk de repo-bestanden NIET; schrijf alleen je eigen uitvoerbestand in de scratchpad.

## Technische aanwijzingen (belangrijk)
- Scratchpad: `/tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad` (hierna $S).
- **`*.olst-wijhe.nl` stuurt geen intermediate certificaat mee.** Gebruik curl met de CA-bundel `$S/ow-ca.pem`:
  `curl -s -L --cacert $S/ow-ca.pem -A "Mozilla/5.0" "<url>" -o $S/<naam>`
  WebFetch kan op deze hosts falen; gebruik dan curl. Schakel certificaatverificatie niet uit.
- Alle andere hosts zijn bereikbaar (olstwijhe.bestuurlijkeinformatie.nl, lokaleregelgeving.overheid.nl, zoek.officielebekendmakingen.nl, repository.overheid.nl, ruimtelijkeplannen.nl, planviewer.nl, ruimtelijkeplannen.overijssel.nl, omgevingswet.overheid.nl, overijssel.nl, odijsselland.nl).
- PDF's: download met curl en extraheer met Python `pdfplumber` (`pdftotext` is niet geïnstalleerd), bijv.
  `python3 -c "import pdfplumber,sys; print('\n'.join((p.extract_text() or '') for p in pdfplumber.open(sys.argv[1]).pages))" bestand.pdf > bestand.txt` en grep daarin.
- HTML: strip met Python (bijv. `html.parser`/regex) of gebruik WebFetch; citeer de letterlijke tekst, niet een parafrase.
- Bestuurlijkeinformatie.nl (iBabs): documenten via `https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/<id>` (PDF), agenda's via `/Agenda/Index/<id>`; zoeken via `https://olstwijhe.bestuurlijkeinformatie.nl/Search?searchString=...` (probeer).
- CVDR: open `https://lokaleregelgeving.overheid.nl/CVDRxxxxx` en lees **de organisatie in de kop ("Organisatie"/"Uitgegeven door")**. Een CVDR-nummer hoort alleen bij Olst-Wijhe als daar "Olst-Wijhe" staat. Zoekresultaten vermengen vaak gemeenten (in eerdere runs bleek bijv. een "Zwolse" huisvestingsverordening van Groningen). Zoeken in CVDR: `https://lokaleregelgeving.overheid.nl/ZoekResultaat?...` of via de SRU-API `https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&q=...` (CQL, bijv. `creator="Olst-Wijhe" and title any "leges"`); officiële bekendmakingen via `https://repository.overheid.nl/sru?query=...` of `https://zoek.officielebekendmakingen.nl/resultaten?q=...`.
- WebSearch-samenvattingen zijn onbetrouwbaar; gebruik zoeken alleen om documenten te vinden en lees het document zelf.
- Verzin niets. Wat je niet vindt: zeg dat expliciet, met de plekken waar je gezocht hebt en waar het wel te vinden zou zijn.

## Uitvoer
Schrijf je resultaten in het Nederlands naar `$S/deelonderzoek_<n>.md`, met per onderwerp:
1. **Bevinding** met letterlijke citaten in blockquotes: `> "…"` + regel `— Bron: <titel>, <URL> (geraadpleegd 2026-10-04)`.
2. **Correctie op het concept**: welke zin/paragraaf (§-nummer) in `gemeente_olst-wijhe.md` fout/onvolledig is en wat er moet staan.
3. **Tegenstrijdigheden**: verwijs naar de genummerde lijst "Tegenstrijdigheden en onzekerheden" (1-20) onderaan het concept en geef per nummer dat jouw brontype raakt: opgelost (hoe, met citaat) / niet oplosbaar (waarom).
4. **Bijlage A-punten** die jouw brontype raakt: bevinding + status (gevonden / niet gevonden / niet van toepassing / tegenstrijdig) + bron.
5. Een korte lijst "Niet gevonden" met vindplaats.
Wees volledig: tokenverbruik heeft lage prioriteit; volledigheid en juistheid gaan voor. Eindig je antwoord aan de hoofdagent met een samenvatting van max. 300 woorden en het pad van je uitvoerbestand.
