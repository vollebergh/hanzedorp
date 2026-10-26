# Ruwe deelonderzoeksdata per gemeente

Gefilterd archief van de werkbestanden van de deelonderzoeken (stand 2026-10-27), geordend per gemeente. Bedoeld om bevindingen in de eindrapporten (`gemeente_<naam>.md` in de hoofdmap) te kunnen narekenen.

## Wat erin zit
- Deelrapporten van de subagents (`raw/do1.md` t/m `do4.md`, `deelonderzoek_*.md`), briefings (`BRIEF.md`, `BRIEFING.md`), voortgangs- en statusbestanden.
- Scripts (`.py`, `.sh`) waarmee data is opgehaald of berekend (CVDR/SRU, geodata, Open Besluitvorming, overlays).
- Kleine tabellen (`.csv`, `.tsv`), elk kleiner dan 1 MB.

## Wat er bewust niet in zit
- Gedownloade bronnen: PDF's, HTML, binaire bestanden, geëxtraheerde brontekst (`*_bronnen/`, `src/`, `cache/`, RIS-documentdumps). Die blijven lokaal (publiek repository; auteursrecht en persoonsgegevens in raadsstukken).
- Alles wat groter is dan 1 MB.

## Let op
- Het zijn werkbestanden: ze kunnen voorlopige uitspraken bevatten die in het eindrapport zijn gecorrigeerd. Het eindrapport in de hoofdmap is leidend.
- Niet per gemeente aanwezig: Zwolle en Kampen (geen werkmap teruggevonden). Dalfsen en Olst-Wijhe bestaan uit losse bestanden uit een gedeelde werkmap en zijn minder compleet.
- Padverwijzingen in scripts (`/tmp/claude-…/scratchpad/…`) verwijzen naar de oorspronkelijke werkmappen en bestaan elders niet meer.
