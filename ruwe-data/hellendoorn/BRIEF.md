# Brief deelonderzoeken Hellendoorn (Hanzedorp CPO-onderzoek)

Gemeente: **Hellendoorn**, provincie **Overijssel** (volgens art. 4.4 "overige kern": alleen lokale behoefte + bijzondere doelgroepen; woonregio **Twente**, Woondeal Twente; kernen en buurtschappen: stel de actuele lijst zelf vast uit gemeentelijke bronnen; namen uit de opdracht of uit je geheugen kunnen fout zijn).

Opdracht: CPO van 10-12 woningen op agrarische grond. Volg exact de masterprompt `/home/nick/Claude/Hanzedorp/prompt.md`:
de 12 vaste onderwerpen (§1-12), de twee kernvragen en **Bijlage A (r.136-190) = Overijssel-controlepunten A1-F1**.
Bijlage B (Gelderland) is NIET van toepassing. Gebruik geen Gelderse begrippen.

Fase 1-kader: `/home/nick/Claude/Hanzedorp/provincie_overijssel.md` (lees integraal; herverifieer §6.1 waar relevant). Let op: Hellendoorn zit in de **Twente**-woondeal (niet West-Overijssel); basisgegevens staan in §1.5 (189 gerealiseerd 2022-2024; 6 sleutelprojecten / 825 woningen; doorkijk 645; Nijverdal Centrum 350, Hoge Dijkje 165, Reggesteyn 75, Hellendoorn uitbreiding 80, Haarle De Grave 65, Daarlerveen 90, Nijverdal Zuid 0/500). Omgevingstafel = Twente (niet IJsselland).
Voorbeeldrapporten (structuur/stijl/markeringen [PRIMAIR]/[PB]/[TK]/[INT]/[BER]/[WF]): `/home/nick/Claude/Hanzedorp/gemeente_hardenberg.md` (nieuwste), `gemeente_raalte.md`, `gemeente_deventer.md`.
Lees ook de praktijkles-memory: `/home/nick/.claude/projects/-home-nick-Claude-Hanzedorp/memory/project_zoekmethodiek_praktijk.md`
(403/UA-trucs, CVDR-SRU, Notubiz/iBabs-API, Overijssel WFS + landbouwgebied-typologie via ruimtelijkeplannen.overijssel.nl, pdfplumber voor PDF).

Herbruikbare scripts van het Hardenberg-onderzoek (alleen lezen/kopiëren, pas gemeente-parameters aan):
`/home/nick/.local/share/hanzedorp-hardenberg/raw/do2/tools/` (wfs.py, overlay.py, planmonitor.py, brp.py, gem.py, woonplaatsen.py, raat.py, sru.py, pdf2txt.py, ...) en `.../raw/do1/scripts/` (sru.py, nb_events.py, totext.py) en `.../raw/do4/scripts/gmb_harvest.py`. Kopieer naar je eigen submap voordat je ze aanpast.

Bekende aandachtspunten Hellendoorn (uit eigen kennis, **niet geverifieerd**, alleen als zoekrichting): Nijverdal is de grootste kern; kernen o.a. Hellendoorn, Haarle, Daarle, Daarlerveen, Marle, Egede, Hulsen; Sallandse Heuvelrug/Natura 2000 en NNN; windopgave (windpark De Graven?); raadsarchief.hellendoorn.nl en openpdc.hellendoorn.nl bestaan; de RIS-leverancier (iBabs/Notubiz/anders) en de coalitiesamenstelling moet je zelf vaststellen. Controleer ook of het provinciebestand-lemma "Daarlerveen 90 / 45 nieuw" klopt in de Woondeal Twente en of er een eigen KGO/erfbeleid ("Kwaliteitsimpuls", "erftransformatie", "VAB", "Kwaliteit in de ruimte" e.d.) bestaat.

## Deelonderzoeken (elk: eigen brontype, ALLE 12 onderwerpen + ALLE Bijlage A-punten)
- DO1 gemeentelijke bestuursinformatie (hellendoorn.nl, omgevingsvisie, omgevingsplan, woonvisie, RIS, raadsbesluiten, coalitieakkoord) -> raw/do1.md
- DO2 provinciaal-lokale toepassing + geodata (landbouwgebied-typologie art. 4.123 per kern/buitengebied, NNN, Natura 2000, grondwater, Bijlage A: A1-A3, C, E; provinciale correspondentie, BOPA-precedenten, Omgevingstafel Twente) -> raw/do2.md
- DO3 nieuws en actualiteit 2024-2026 (regionaal: Tubantia, De Stentor, Salland/Hellendoorn-weekbladen, RTV Oost, Nijverdal-nieuws → verifieer; praktijkvoorbeelden, coalitie, wethouder Wonen) -> raw/do3.md
- DO4 juridische/officiële registers (CVDR via SRU, officielebekendmakingen/Gemeenteblad, Provinciaal blad, ruimtelijkeplannen/planarchief) -> raw/do4.md

## Spelregels
- Schrijf het deelrapport DIRECT als bestand aan en breid het incrementeel uit; sluit elk bestand af met een regel `Gedaan: ... | Nog te doen: ...` (sessielimiet-risico).
- Ruwe extracties (PDF-tekst, JSON, scripts) in raw/doN/ (eigen submap per agent).
- Bronnen: URL + raadplegingsdatum (2026-10-15), letterlijke citaten voor relevante passages, betrouwbaarheidsmarkeringen [PRIMAIR]/[PB]/[TK]/[INT]/[BER]/[WF].
- **Verifieer elk CVDR-nummer** op uitgevende gemeente (veel treffers zijn van andere gemeenten; let ook op Hellendoorn vs. Haaksbergen/Holten/Rijssen-Holten/Wierden/Raalte). Namen/plaatsnamen uit de opdracht kunnen fout zijn.
- WebSearch-samenvattingen zijn onbetrouwbaar: gebruik ze om documenten te vinden en lees het brondocument zelf.
- Telwerk (aantal projecten, woningen, percentages) uit de brontekst zelf (regex/Python), niet uit het hoofd.
- "Niet gevonden" is een geldige uitkomst: vermeld waar het wel te vinden zou zijn.
- Tegenstrijdigheden niet wegmiddelen maar benoemen; bronnen met eigen inconsistentie vermelden.
- Geen git-acties; schrijf alleen onder `/tmp/claude-1000/-home-nick-Claude-Hanzedorp/badd7466-a102-440a-9a30-b6c10de0f032/scratchpad/hellendoorn/raw/`.
- Werk met curl en een volledige Chrome-user-agent als WebFetch een 403 geeft; PDF's lokaal extraheren met pdfplumber (`python3 -I`).
