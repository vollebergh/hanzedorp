# Brief deelonderzoeken Hardenberg (Hanzedorp CPO-onderzoek)

Gemeente: **Hardenberg**, provincie **Overijssel** (streekcentrum volgens art. 4.4; woonregio West-Overijssel; kernen en buurtschappen: stel de actuele lijst zelf vast uit gemeentelijke bronnen; namen uit de opdracht of uit je geheugen kunnen fout zijn).

Opdracht: CPO van 10-12 woningen op agrarische grond. Volg exact de masterprompt `/home/nick/Claude/Hanzedorp/prompt.md`:
de 12 vaste onderwerpen (§1-12), de twee kernvragen en **Bijlage A (r.136-190) = Overijssel-controlepunten A1-F1**.
Bijlage B (Gelderland) is NIET van toepassing. Gebruik geen Gelderse begrippen.

Fase 1-kader: `/home/nick/Claude/Hanzedorp/provincie_overijssel.md` (lees integraal; herverifieer §6.1 waar relevant).
Voorbeeldrapport (structuur/stijl/markeringen [PRIMAIR]/[PB]/[TK]/[INT]/[BER]/[WF]): `/home/nick/Claude/Hanzedorp/gemeente_raalte.md`, ook gemeente_deventer.md.
Lees ook de praktijkles-memory: `/home/nick/.claude/projects/-home-nick-Claude-Hanzedorp/memory/project_zoekmethodiek_praktijk.md`
(403/UA-trucs, CVDR-SRU, Notubiz/iBabs-API, Overijssel WFS + landbouwgebied-typologie via ruimtelijkeplannen.overijssel.nl, pdfplumber voor PDF).

## Deelonderzoeken (elk: eigen brontype, ALLE 12 onderwerpen + ALLE Bijlage A-punten)
- DO1 gemeentelijke bestuursinformatie (hardenberg.nl, omgevingsvisie, omgevingsplan, woonvisie, RIS, raadsbesluiten, coalitieakkoord) -> raw/do1.md
- DO2 provinciaal-lokale toepassing + geodata (landbouwgebied-typologie art. 4.123 per kern/buitengebied, NNN, Natura 2000, grondwater, Bijlage A: A1-A3, C, E; provinciale correspondentie, BOPA-precedenten) -> raw/do2.md
- DO3 nieuws en actualiteit 2024-2026 (regionaal: De Stentor/Hardenberger Dagblad? , RTV Oost, Dedemsvaartse Courant/Gelderlander? -> verifieer; praktijkvoorbeelden, coalitie, wethouder Wonen) -> raw/do3.md
- DO4 juridische/officiële registers (CVDR via SRU, officielebekendmakingen/Gemeenteblad, Provinciaal blad, ruimtelijkeplannen/planarchief) -> raw/do4.md

## Spelregels
- Schrijf het deelrapport DIRECT als bestand aan en breid het incrementeel uit; sluit elk bestand af met een regel `Gedaan: ... | Nog te doen: ...` (sessielimiet-risico).
- Ruwe extracties (PDF-tekst, JSON, scripts) in raw/doN/ (eigen submap per agent; gedeelde tools in raw/tools/ alleen lezen).
- Bronnen: URL + raadplegingsdatum (2026-10-15 of eerder), letterlijke citaten voor relevante passages.
- **Verifieer elk CVDR-nummer** op uitgevende gemeente (veel treffers zijn van andere gemeenten). Namen/plaatsnamen uit de opdracht kunnen fout zijn.
- WebSearch-samenvattingen zijn onbetrouwbaar: gebruik ze om documenten te vinden en lees het brondocument zelf.
- "Niet gevonden" is een geldige uitkomst: vermeld waar het wel te vinden zou zijn.
- Tegenstrijdigheden niet wegmiddelen maar benoemen; bronnen met eigen inconsistentie vermelden.
- Geen git-acties; alleen schrijven onder /home/nick/.local/share/hanzedorp-hardenberg/raw/.
