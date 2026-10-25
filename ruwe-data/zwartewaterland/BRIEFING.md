# Briefing deelonderzoek — gemeente Zwartewaterland (provincie Overijssel)

Datum onderzoek: 2026-10-11. Taal van de output: Nederlands.

## Opdracht
CPO-onderzoek (Hanzedorp): kan in gemeente **Zwartewaterland** een cluster van 10-12 woningen via collectief particulier opdrachtgeverschap op agrarische grond buiten de kernen worden gerealiseerd? Jij voert één van vier gelijktijdige deelonderzoeken uit (zie je eigen opdracht). Je doorzoekt **jouw brontype voor ALLE 12 onderwerpen van de vaste structuur én alle controlepunten van Bijlage A**; de hoofdagent voegt later samen.

## Lees eerst (volledig of gericht)
- `/home/nick/Claude/Hanzedorp/prompt.md` — masterprompt: 12 onderwerpen, vaste structuur, Bijlage A (controlepunten, kolom "Primair" geeft jouw deelonderzoeknummer), twee kernvragen.
- `/home/nick/Claude/Hanzedorp/provincie_overijssel.md` — Fase 1-kader; hergebruik, onderzoek het algemene provinciale beleid NIET opnieuw. Let op §1.5 (Zwartewaterland: 244 / 3 / 559 / 77 — controleer wat die getallen betekenen) en §6.1 Houdbaarheid.
- `/home/nick/Claude/Hanzedorp/gemeente_ommen.md` en `gemeente_olst-wijhe.md` — voorbeelden van de gewenste diepgang, bronvermelding en betrouwbaarheidsmarkering (**[PB]**, **[TK]**, **[INT]**, **[BER]**, **[WF]**, **[OCR]**). Lees minstens de kop + 1-2 secties; kopieer geen inhoud over Ommen/Olst-Wijhe.

## Werkregels
1. **Brondocumenten zelf lezen.** Zoeksamenvattingen (WebSearch) zijn onbetrouwbaar voor gemeente-attributie en details; gebruik ze alleen om documenten te vinden. Citeer letterlijk uit het brondocument, met URL + raadplegingsdatum (2026-10-11 of de feitelijke datum). Grote documenten (>1.000 woorden): beschrijven + bronvermelding, relevante passages letterlijk.
2. **CVDR-nummers verifiëren**: treffers blijken vaak van een andere gemeente (bijv. Zwolle/Zwartewaterland-verwarring, Kampen, Zutphen). Controleer elk CVDR-nummer op "Overheidsorganisatie" in de kop van lokaleregelgeving.overheid.nl/CVDRxxxxxx voordat je het aan Zwartewaterland toeschrijft; noem liever "niet gevonden" dan een niet-geverifieerd nummer.
3. **Namen en plaatsen controleren.** Kernen van Zwartewaterland zijn o.a. Hasselt, Genemuiden, Zwartsluis, Grafhorst(?), Kamperveen(?) — verifieer via BAG/PDOK-Locatieserver (woonplaatsen binnen de gemeente) en de gemeentelijke site; neem niets aan.
4. **Technische tips (uit eerdere runs):**
   - WebFetch kan HTTP 403 geven; probeer `curl` met browser-User-Agent via Bash. Als certificaatketen faalt: haal het tussencertificaat op via AIA-URL, gebruik `curl --cacert`, nooit verificatie uitschakelen.
   - PDF's: WebFetch/curl slaat ze op; tekst extraheren met `python3 -I` + `pdfplumber` (`pdftotext` is niet geïnstalleerd); doorzoek met grep op CPO, collectief, zelfbouw, kavel, KGO, rood-voor-rood, VAB, buitengebied, erf, woningbouw, enz.
   - RIS: zoek het raadsinformatiesysteem van Zwartewaterland (iBabs / Notubiz / Parlaeus — vaststellen). Notubiz-API (`api.notubiz.nl/...`) is zonder browsercheck te lezen. Achter Anubis/browsercheck: claude-in-chrome gebruiken indien beschikbaar.
   - CVDR-index per gemeente via SRU: `https://zoekservice.overheid.nl/sru/Search?x-connection=cvdr&operation=searchRetrieve&version=1.2&query=dcterms.creator=Zwartewaterland and dcterms.modified>=2020-01-01&startRecord=1&maximumRecords=100` (pagineren; check ook of de creator-waarde exact "Zwartewaterland" is). Gemeenteblad/Provinciaal blad: `https://repository.overheid.nl/sru` met `x-connection=officielepublicaties`, `dt.creator=Zwartewaterland AND cql.textAndIndexes=<term>`.
   - Provinciale kaartlagen: WFS `services.geodataoverijssel.nl/geoserver/ows` (NNN, Natura 2000, grondwaterbescherming, enz.); landbouwgebied-typologie art. 4.123 via verordening-viewer `ruimtelijkeplannen.overijssel.nl`, doc `55d637e6-8ff6-4083-a824-a0e77027a044` (document-JSON `annotaties` + vector tiles; punten via `_locationSearch?x=&y=&distance=1`). Gemeentegrenzen PDOK `service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0` (filter client-side).
   - Controleer op dubbeltelling: projectnaam en wijknaam kunnen dezelfde locatie zijn.
5. **Negatieve bevindingen zijn waardevol** ("geen eigen KGO-formule", "geen zelfbouwloket"): leg vast en vermeld **waar** het wel te vinden zou zijn (loket/register/afdeling).
6. **Landelijke context** (Wet versterking regie volkshuisvesting per 1-7-2026; ladder-schrapping verwacht 1-1-2027; gemeentelijk volkshuisvestingsprogramma uiterlijk 1-7-2027): onderzoek of Zwartewaterland al een (ontwerp-)volkshuisvestingsprogramma / woonvisie-opvolger heeft.
7. **Houd rekening met sessielimieten:** maak je rapportbestand DIRECT aan en breid het incrementeel uit (na elk afgerond onderwerp wegschrijven). Ruwe extracties/bronbestanden in de map `raw/` (hergebruik bij herstart). Je eindrapport is het bestand zelf; sluit af met een korte samenvatting in je antwoord (max ~25 regels: belangrijkste bevindingen, tegenstrijdigheden, wat niet gevonden).
8. **Niet doen:** niets in de repo `/home/nick/Claude/Hanzedorp` wijzigen, niet committen. Schrijf uitsluitend naar `/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/`.

## Vorm van je rapport
Bestand `deelonderzoek_<N>_<brontype>.md` in de map hierboven. Structuur: per onderwerp §1–§12 uit prompt.md (met letterlijke relevante citaten + bron-URL + raadplegingsdatum + betrouwbaarheidsmarkering), gevolgd door een tabel "Bijlage A-controlepunten" (A1–F1: bevinding | status gevonden/niet gevonden/niet van toepassing/tegenstrijdig | bron | waar te vinden bij 'niet gevonden'), een lijst "Geverifieerde CVDR-nummers" (nummer | organisatie volgens kop | titel | geldig van-tot), en "Onzekerheden/tegenstrijdigheden". Beantwoord ook de twee kernvragen gelaagd (gemeentelijk / provinciaal / eindoordeel) voor zover jouw brontype dat toelaat.
