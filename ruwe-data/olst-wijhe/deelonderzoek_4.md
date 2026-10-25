# Deelonderzoek 4: juridische en officiële registers (verificatieronde Olst-Wijhe)

**Raadplegingsdatum van alle bronnen: 2026-10-04.** Geraadpleegd: CVDR (lokaleregelgeving.overheid.nl, kop + `?show-wti=true`; SRU zoekservice.overheid.nl `x-connection=cvdr`), officielebekendmakingen.nl (Gemeenteblad, Staatscourant, Provinciaal blad; SRU repository.overheid.nl), ruimtelijkeplannen.nl, planviewer.nl, ro.olst-wijhe.nl, PDOK-locatieserver (alleen voor CBS-buurtnamen). Eén document uit iBabs (Handreiking KGO) is gelezen omdat het de vraag naar publicatie als beleidsregel direct raakt; dat hoort primair bij deelonderzoek 1.

Werkwijze:
- Alle **628 CVDR-records met organisatie "Olst-Wijhe"** zijn via SRU opgehaald (`dcterms.creator="Olst-Wijhe"`, 458 unieke regelingen, ook ingetrokken versies).
- Alle **2.235 officiële publicaties van Olst-Wijhe sinds 1-1-2024** zijn via SRU opgehaald (`dt.creator="Olst-Wijhe" AND dt.date>=2024-01-01`), aangevuld met full-text-zoekacties.
- Het **Provinciaal blad Overijssel sinds 2023** is doorzocht op "Olst-Wijhe" (69 treffers).

Ruwe bestanden staan in `$S/d4/`.

---

## 0. CVDR-verificatietabel (organisatie letterlijk uit de kop "Overheidsorganisatie")

| Nummer | Organisatie volgens kop | Titel (officiële naam) | Datum (ondertekening / inwerkingtreding / status) | Bekendmaking | URL |
|---|---|---|---|---|---|
| CVDR305226 | **Tubbergen** | Gemeentelijk beleidskader Kwaliteitsimpuls groene omgeving (KGO) | raad Tubbergen 7-10-2013; versie 2 in werking 31-3-2016; **vervallen per 16-02-2022** | Gemeenteblad 2013, 28; Gemeenteblad 2016, 23 | https://lokaleregelgeving.overheid.nl/CVDR305226 |
| CVDR696503 | **Olst-Wijhe** | Omgevingsplan gemeente Olst-Wijhe | in werking 01-01-2024; huidige versie 4 geldt vanaf 03-09-2026 | Stb 2023, 113; Gmb 2024, 169225; Gmb 2025, 249653; Gmb 2026, 416930 | https://lokaleregelgeving.overheid.nl/CVDR696503 |
| CVDR720837 | **Harlingen** | Nota grondbeleid 2024-2027 | ondertekening 24-04-2024; in werking 14-06-2024 | gmb-2024-254640 | https://lokaleregelgeving.overheid.nl/CVDR720837 |
| CVDR691005 | **Olst-Wijhe** | Nota Grondbeleid 2023 - 2026 | raad, ondertekening **12-12-2022**; in werking 17-01-2023 | gmb-2023-16454 | https://lokaleregelgeving.overheid.nl/CVDR691005 |
| CVDR752237 | **Olst-Wijhe** | Verordening op de heffing en de invordering van leges 2026 | raad **24-11-2025**; in werking 23-12-2025 (heffing per 1-1-2026) | gmb-2025-561668 | https://lokaleregelgeving.overheid.nl/CVDR752237 |
| CVDR663985 | **Bladel** | Beleidsregels Collectief Particulier Opdrachtgeverschap | B&W, 28-09-2021; in werking 12-11-2021 | gmb-2021-402990 | https://lokaleregelgeving.overheid.nl/CVDR663985 |
| CVDR638437 | **Best** | Beleid vrijkomende agrarische bebouwing | raad, 09-12-2019; in werking 21-03-2020 | gmb-2020-74732 | https://lokaleregelgeving.overheid.nl/CVDR638437 |
| CVDR734442 | **Sint-Michielsgestel** | Beleidsregels functiewijziging VAB en woningbouw buitengebied | raad, 12-12-2024; in werking 22-01-2025 | gmb-2025-24550 | https://lokaleregelgeving.overheid.nl/CVDR734442 |
| CVDR738282 | **Urk** | Beleidsregels woningsplitsing, woningomzetting en woninguitbreiding | B&W, 01-04-2025; in werking 18-04-2025 | gmb-2025-169482 | https://lokaleregelgeving.overheid.nl/CVDR738282 |
| CVDR726084 | **Hof van Twente** | KGO beleid 2023 - 2028 | raad, 07-03-2023 | gmb-2024-458764 | https://lokaleregelgeving.overheid.nl/CVDR726084 |
| CVDR743316 | **Steenwijkerland** | Randvoorwaarden toekomst bij vrijkomende agrarische bebouwing (VAB) | raad, 27-05-2025; in werking 09-08-2025 | gmb-2025-350369 | https://lokaleregelgeving.overheid.nl/CVDR743316 |
| CVDR734518 | **Rijssen-Holten** | Ruimtelijke Ontwikkelingen in het buitengebied 2024 | raad, 09-12-2024; in werking 24-01-2025 | gmb-2025-27684 | https://lokaleregelgeving.overheid.nl/CVDR734518 |
| CVDR729056 | **Gooise Meren** | Woonvisie 2025 - 2030 "Het begint met wonen" | raad, 06-11-2024; in werking 01-01-2025 | gmb-2024-521152 | https://lokaleregelgeving.overheid.nl/CVDR729056 |
| CVDR739354 | **Groningen** | Huisvestingsverordening 2025 | raad, 26-03-2025; in werking 20-05-2025 | gmb-2025-213560 | https://lokaleregelgeving.overheid.nl/CVDR739354 |
| *Nieuw:* CVDR765519 | **Olst-Wijhe** | Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten gemeente Olst-Wijhe 2026 | B&W, 11-08-2026; in werking 14-08-2026 | gmb-2026-385444 | https://lokaleregelgeving.overheid.nl/CVDR765519 |
| *Nieuw:* CVDR704153 | **Olst-Wijhe** | Besluit tot aanwijzing van categorieën van gevallen van een buitenplanse omgevingsplanactiviteit waarvoor een advies van de raad nodig is | raad, 07-02-2022; in werking 01-01-2024 | gmb-2023-499448 | https://lokaleregelgeving.overheid.nl/CVDR704153 |
| *Nieuw:* CVDR638025 | **Olst-Wijhe** | Notitie Buurtschappenbeleid | B&W, 18-02-2020; in werking 18-03-2020 | gmb-2020-63767 | https://lokaleregelgeving.overheid.nl/CVDR638025 |
| *Nieuw:* CVDR410483 | **Olst-Wijhe** | Beleidsnota Inwoning | B&W, 05-07-2016; in werking 28-07-2016 | Gemeenteblad 2016, 103300 | https://lokaleregelgeving.overheid.nl/CVDR410483 |

Kopcitaat CVDR305226 (wetstechnische informatie):
> "Regeling vervallen per 16-02-2022 / Gemeentelijk beleidskader Kwaliteitsimpuls groene omgeving (KGO) / Geldend van 31-03-2016 t/m 15-02-2022 / Algemeen / Overheidsorganisatie / Tubbergen / Organisatietype / Gemeente […] Vastgesteld door / gemeenteraad"

> "De raad van de gemeente Tubbergen, […] Aldus besloten in de openbare vergadering van 7 oktober 2013 […] Beleidskader voor de toepassing van de kwaliteitsimpuls groene omgeving / Gemeente Tubbergen & Dinkelland / augustus 2013"

— Bron: CVDR305226, https://lokaleregelgeving.overheid.nl/CVDR305226?show-wti=true en https://lokaleregelgeving.overheid.nl/CVDR305226 (geraadpleegd 2026-10-04)

**Conclusie:** CVDR305226 hoort bij **Tubbergen**. Het is een gezamenlijk opgesteld kader van Tubbergen en Dinkelland, gepubliceerd door Tubbergen, en het is **sinds 16-02-2022 vervallen**. Het heeft niets met Olst-Wijhe te maken. De vermelding in `provincie_overijssel.md` §2.3 ("een gemeentelijk beleidskader KGO (zie CVDR305226 …)") moet worden geschrapt. In de verificatietabel van het concept moet staan: "Tubbergen (gezamenlijk kader Tubbergen & Dinkelland, 2013), vervallen 16-02-2022".

---

## 1. Omgevingsplan CVDR696503: versiehistorie, huidige versie en omgevingsplanwijzigingen 2024-2026 (prioriteit 6)

**Bevinding.**
> "Omgevingsplan gemeente Olst-Wijhe […] Geldend van 03-09-2026 t/m heden / Overheidsorganisatie / Olst-Wijhe […] Vastgesteld door / Gemeenteraad […] Datum inwerkingtreding 01-01-2024 is vastgesteld in Staatsblad 2023, 113 met datum ondertekening 05-04-2023."

Versieoverzicht (wti):

| Inwerkingtreding | Tot | Bron |
|---|---|---|
| 01-01-2024 | 17-04-2024 | Staatsblad 2023, 113 (en Stb 2020/2021/2022: Invoeringswet/bruidsschat) |
| 17-04-2024 | 06-06-2025 | Gemeenteblad 2024, 169225 |
| 06-06-2025 | 03-09-2026 | Gemeenteblad 2025, 249653 |
| 03-09-2026 | heden | Gemeenteblad 2026, 416930 |

— Bron: CVDR696503, https://lokaleregelgeving.overheid.nl/CVDR696503?show-wti=true (geraadpleegd 2026-10-04)

De drie gemeentelijke versies zijn **uitsluitend technisch**:
> "Door middel van deze publicatie neemt de gemeente Olst-Wijhe het Omgevingsplan technisch in beheer. Met dit document worden uitsluitend enige technische aanpassingen doorgevoerd in de Bruidsschat. Het bevat geen wijzigingen in de juridische inhoud van de bruidsschatregels […] Deze technische aanpassing treedt in werking op 17 april 2024."

— Bron: Gemeenteblad 2024, 169225, https://zoek.officielebekendmakingen.nl/gmb-2024-169225.html (geraadpleegd 2026-10-04)

> "Om technische redenen is het nodig om het omgevingsplan opnieuw te publiceren. Deze publicatie bevat geen wijzigingen in de juridische inhoud en de aanpassingen hebben geen rechtsgevolg […] Dit besluit treedt in werking per 03‑09‑2026"

— Bron: Gemeenteblad 2026, 416930, https://zoek.officielebekendmakingen.nl/gmb-2026-416930.html (geraadpleegd 2026-10-04); Gemeenteblad 2025, 249653 heeft dezelfde strekking.

Juridisch onderdeel van het omgevingsplan zijn verder (wti, "andere regelingen"): het Voorbereidingsbesluit bedrijfsverzamelgebouwen en opslag/of garageboxen (Gmb 2026, 116040, in werking 11-03-2026), omgevingsplanregels uit het projectbesluit IJsselwerken van waterschap Drents Overijsselse Delta (Wsb 2025, 23607), de voorbeschermingsregels hyperscale datacentra (Stcrt 2023, 35432) en de provinciale voorbereidingsbesluiten Omgevingsverordening 2021, Windenergie 2024 en Zonneparken 2024 (de laatste twee beëindigd).

**Inhoudelijke omgevingsplanwijzigingen 2024-2026** lopen als aparte IMRO/TAM-hoofdstukken buiten de CVDR-consolidatie:
- **Hoofdstuk 22a IJsseldal, Wesepe** (Raalterweg 50; 81 woningen; coördinatie met de omgevingsvergunning voor 50 woningen): ontwerp Gmb 2025, 278742; gewijzigd vastgesteld en ter inzage 26-9 t/m 6-11-2025, Gmb 2025, 416049 (NL.IMRO.1773.TAMH22a-0301).
- **Hoofdstuk 22b Wengelerhoek fase 1, Wijhe**:
  > "Het plan voorziet in het realiseren van een nieuwe woonwijk ten zuiden van de kern Wijhe. In het plan worden 135 nieuwe woningen gerealiseerd en 50 tijdelijk vergunde (flex)woningen permanent planologisch toegestaan. […] voor in totaal 186 woningen."

  — Bron: Gemeenteblad 2026, 257200, https://zoek.officielebekendmakingen.nl/gmb-2026-257200.html (geraadpleegd 2026-10-04); rectificatie Gmb 2026, 290212.
- Geen omgevingsplanwijziging voor wonen in het buitengebied gevonden. Wonen in het buitengebied loopt na 1-1-2024 uitsluitend via **BOPA's** (zie §5).

**Correctie op het concept.**
- §3a en Tegenstrijdigheid 5: de huidige versie is CVDR696503/4, geldend vanaf **03-09-2026**. De reeks is 01-01-2024 → 17-04-2024 → 06-06-2025 → 03-09-2026. Beide lezingen uit het concept waren deels juist. Alle drie de gemeentelijke versies zijn technisch, zonder inhoudelijke wijziging. Het buitengebied valt dus nog onder het tijdelijk deel (Bestemmingsplan Buitengebied Olst-Wijhe 2021).
- Bijlage A B3: "omgevingsplan nog tijdelijk deel" is bevestigd. Een aanpassing aan Actualisatie 2026 (art. 4.2a) is in CVDR/Gmb **niet gevonden**.

### 1a. Bestemmingsplan Buitengebied Olst-Wijhe (NL.IMRO.1773.BP2020001001)

**Bevinding.**
> "De gemeenteraad stelde op 12 april 2021 het bestemmingsplan Buitengebied Olst-Wijhe gewijzigd vast. Het plan geldt voor het gehele buitengebied van de gemeente Olst-Wijhe, met uitzondering van de IJssel en haar uiterwaarden."

— Bron: Staatscourant 2021, 22714, https://zoek.officielebekendmakingen.nl/stcrt-2021-22714.html (geraadpleegd 2026-10-04). Het geleideformulier van versie **-0301** vermeldt "Status vastgesteld / Datum 2021-04-12": https://www.ruimtelijkeplannen.nl/documents/NL.IMRO.1773.BP2020001001-0301/g_NL.IMRO.1773.BP2020001001-0301.xml.

**Let op:** de door het concept gebruikte URL (planviewer, versie **-0201**) en de map op ro.olst-wijhe.nl zijn het **ontwerp**. Het geleideformulier zegt daar "Status ontwerp, Datum 2020-12-01". Citeer de vastgestelde versie: regels https://www.ruimtelijkeplannen.nl/documents/NL.IMRO.1773.BP2020001001-0301/r_NL.IMRO.1773.BP2020001001-0301.html.

Relevante regels (vastgestelde versie -0301):
- Bedrijfswoning/plattelandswoning in de agrarische bestemming (art. 3.2, tabel):
  > "bedrijfs-/plattelandswoning (inclusief aan- en uitbouwen | één, tenzij middels een aanduiding anders is aangegeven | - | 750 m³ | 4,5 m | 10 m"

  Burgerwoning (art. 24, tabel): "750 m³, tenzij middels een aanduiding anders is aangegeven". Afwijking tot 1.000 m³ is alleen mogelijk "ten behoeve van volwaardige agrarische bedrijven […] ten behoeve van de inwoning van een tweede arbeidskracht, of een rustende boer" (art. 3.4.4).
- Vervolgfuncties na beëindiging van een agrarisch bedrijf (art. 3.9.5): sloop/terugbouw 250 m² / 1/3 tot max. 850 m², inrichtingsplan verplicht, en uitdrukkelijk:
  > "p. het aantal woningen mag niet toenemen;"
- Extra woningen zijn alleen via een wijzigingsbevoegdheid voor karakteristieke panden mogelijk (art. 44.1):
  > "a. woningsplitsing is alleen toegestaan ter plaatse van de aanduiding 'karakteristiek' en ter plaatse van een monumentaal hoofdgebouw; […] g. woningsplitsing in twee woningen is uitsluitend toegestaan als de inhoud van het te splitsen pand meer dan 1.000 m³ bedraagt; h. woningsplitsing in 3 woningen is uitsluitend toegestaan als de inhoud van het te splitsen pand meer dan 1.500 m³ bedraagt; […] n. woningsplitsing is uitsluitend mogelijk indien het erf op een adequate wijze landschappelijk ingepast wordt."

  Art. 44.2 regelt een woning in een karakteristiek bijgebouw binnen het bestaande volume.
- Inrichtingsplan (art. 1.64):
  > "een inrichtingsplan is de grafische beschrijving van de gewenste ruimtelijke ontwikkeling waarin de situering van bouwwerken ten opzichte van elkaar en van de omgeving en het al dan niet aanbrengen van beplanting op een goede manier is weergegeven."

  Dit wordt bij nagenoeg alle afwijkings- en wijzigingsbevoegdheden geëist, "conform de richtlijnen uit het Landschapsontwikkelingsplan".
- Het plan is conserverend (toelichting §3):
  > "Nieuwe (grootschalige) ontwikkelingen worden in dit bestemmingsplan dan ook niet mogelijk gemaakt."

  Een KGO- of rood-voor-rood-regeling voor nieuwe woningen staat **niet** in de regels. Het woord "Rood voor Rood" komt alleen voor in "deze wijzigingsbevoegdheid is niet van toepassing op gronden waar een Rood voor Rood-ontwikkeling heeft plaatsgevonden" (art. 6 en art. 24).

— Bron: Regels en toelichting Bestemmingsplan Buitengebied Olst-Wijhe, NL.IMRO.1773.BP2020001001-0301, https://www.ruimtelijkeplannen.nl/documents/NL.IMRO.1773.BP2020001001-0301/r_NL.IMRO.1773.BP2020001001-0301.html en …/t_NL.IMRO.1773.BP2020001001-0301.html (geraadpleegd 2026-10-04)

**Correctie op het concept §3a.** "Het regelt volgens samenvattingen onder meer twee woningen met sloopcompensatie conform KGO, een bedrijfswoning van maximaal 750 m3 en een verplicht inrichtingsplan" is onjuist voor het KGO-deel. Het moet luiden: het plan regelt de bedrijfswoning (750 m³) en een inrichtingsplan, maar **bevat geen KGO-regeling voor extra woningen**. Bij vervolgfuncties mag het aantal woningen niet toenemen (art. 3.9.5 onder p). Extra woningen ontstonden tot eind 2023 via **aparte partiële bestemmingsplannen** en sinds 2024 via **BOPA's**. Voorbeelden van zulke plannen: "Bestemmingsplan Buitengebied, De Wesenberg 3" (raad 26-2-2024: "met toepassing van de KGO-regeling […] ter compensatie twee woningen realiseren", Gmb 2024, 93285) en "Wechterholt 11-11a" (raad 6-2-2024: één vrijstaande woning "in het kader van het KGO-beleid", Gmb 2024, 64287). De bron van "twee woningen met sloopcompensatie" is dus waarschijnlijk zo'n partieel plan, niet het Bestemmingsplan Buitengebied. Vervang daarnaast de ontwerp-URL (-0201) door de vastgestelde versie (-0301).

---

## 2. Handreiking KGO Olst-Wijhe: gepubliceerd als beleidsregel? (prioriteit 3)

**Bevinding (registers).**
- Geen CVDR-regeling. Onder de 458 unieke Olst-Wijhe-regelingen in CVDR komt geen titel met KGO, kwaliteitsimpuls, rood voor rood, erf, woningsplitsing of kleinschalige initiatieven voor. De enige wonen-gerelateerde beleidsregels zijn de Notitie Buurtschappenbeleid (CVDR638025), de Beleidsnota Inwoning (CVDR410483) en de beleidsregels wonen in het kernwinkelgebied Olst (CVDR637651).
- Geen Gemeenteblad-publicatie. Full-text-zoekacties op "kwaliteitsimpuls" (16 treffers) en "KGO" (47 treffers) leveren alleen partiële bestemmingsplannen en vooraankondigingen uit 2016-2024 op. "woningsplitsing" levert alleen de Beleidsnota Inwoning (2016) op, "kleinschalige initiatieven" 0 treffers. Er is dus **geen bekendmaking als beleidsregel** van de Handreiking KGO (2024), noch van "beleid woningsplitsing en kleinschalige initiatieven".

**Bevinding (document, iBabs; aanvullend voor deelonderzoek 1).**
> "Handreiking KGO Gemeente Olst-Wijhe / Werken aan een leefbaar platteland / Olst-Wijhe, 28 mei 2024"

> "Op het moment dat deze handreiking wordt vastgesteld door het college, wordt ook hard gewerkt aan de omgevingsvisie […] Deze handreiking heeft dan ook een tijdelijk karakter."

> "Dat wat in deze handreiking staat sluit grotendeels aan bij de huidige werkwijze en betreft dus geen herziening. Wel is sprake van een aanvulling in de vorm van de mogelijkheid voor woningsplitsing van niet-karakteristieke panden in het buitengebied. Dit komt voort uit de motie van de gemeenteraad […]. De handreiking is geldig totdat er nieuw, integraal beleid voor het landelijk gebied is opgesteld dat voort zal vloeien uit de omgevingsvisie."

> "• Voor het bouwen van 1 woning van maximaal 750 m3 moet minimaal 1000 m2 landschapsontsierende bebouwing gesloopt worden.
> • Voor de bouw van 2 vrijstaande woningen van maximaal 750 m3 moet minimaal 2000 m2 landschapsontsierende bebouwing gesloopt worden.
> • Voor de bouw van 2 woningen van samen maximaal 800 m3 in een aaneengesloten bouwblok moet minimaal 1000 m2 bebouwing gesloopt worden.
> • Voor de bouw van 3 woningen van samen maximaal 1200 m3 in een aaneengesloten bouwblok moet minimaal 1600 m2 gesloopt worden.
> • Er is een maximum van 2 bouwblokken (2 vrijstaande woningen of 2 blokken met woningen) voor wonen toegestaan per erf.
> • De woning(en) worden gebouwd op het eigen erf óf op een daarvoor geschikte locatie in of aan een kern óf in een bestaand bebouwingslint."

> "Een woning van 750 m3 mag maximaal uitgebreid worden tot 1000 m3. Hiervoor geldt dat voor elke m3 die wordt toegevoegd er 4 m2 aan schuren gesloopt moet worden."

> "Een andere mogelijkheid is een financiële compensatie voor de impact op de omgeving aan de Voorziening Ruimtelijke Kwaliteit (voorheen heette dit het landschapsfonds)."

> "Stap 5: Collegebesluit […] Als het college een positief besluit neemt, is de vervolgstap dat u en de gemeente een overeenkomst sluiten, de anterieure overeenkomst." en "Met deze motivering gaat de casemanager in sommige gevallen naar de regionale omgevingstafel. Aan deze tafel schuiven ketenpartners van de gemeente aan, zoals de provincie en het waterschap."

— Bron: Handreiking KGO Gemeente Olst-Wijhe, 28 mei 2024, https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/ba55b732-4944-450f-ab35-046ed41b697d (PDF, 13 p.; geraadpleegd 2026-10-04). De versie "2024-07" op mijnleefomgeving.olst-wijhe.nl is niet vergeleken.

**Vaststellend orgaan:** het **college** (de handreiking zegt dat zelf). Het is geen gepubliceerde beleidsregel in de zin van art. 4:81 Awb (niet in Gmb/CVDR). Juridisch is het dus een niet-bekendgemaakt beleidsdocument.

**Correctie op het concept.**
- §3a: "Er is geen CVDR-regeling voor dit kader gevonden" is bevestigd. Toevoegen: "ook niet als beleidsregel in het Gemeenteblad bekendgemaakt; vastgesteld door het college (document gedateerd 28 mei 2024)".
- Kader "Rekenregels": de **2-woningenregel** splitst zich. 2 vrijstaande woningen vragen 2.000 m² sloop; 2 woningen in één aaneengesloten blok (samen ≤ 800 m³) vragen 1.000 m². Beide samenvattingen waren dus deels juist (Tegenstrijdigheid 4).
- "Ruimtelijke Kwaliteitsprovisie" moet "**Voorziening Ruimtelijke Kwaliteit** (voorheen landschapsfonds)" zijn.
- §3d en §1: de handreiking staat toe dat KGO-woningen "op een daarvoor geschikte locatie in of aan een kern" worden gebouwd (rood-voor-rood elders). Dat is relevant voor de route "aansluitend aan een kern".

---

## 3. Notitie Buurtschappenbeleid (nieuw gevonden; relevant voor Elshof en Herxen)

**Bevinding.**
> "Het buurtschappenbeleid geldt momenteel alleen voor de dorpen Elshof en Herxen."

> "Punt 2 aangaande het te stellen maximum per jaar is niet realistisch, omdat dit bijvoorbeeld de mogelijkheid blokkeert dat enkele starters gezamenlijk gaan bouwen. Dergelijke drempels zijn niet wenselijk."

> "Nieuw beleid (beleidsregel) / Voor de toepassing van het buurtschappenbeleid gelden de volgende voorwaarden en toetsingscriteria: / Algemene voorwaarden: / 1.De landschappelijke, natuurlijke en landbouwkundige waarden mogen niet onevenredig worden aangetast. De bebouwing moet aansluiten bij de aanwezige (stedelijke) bebouwing en het landschap. / Nadere toetsingscriteria: / 1.Aanvrager dient een starter, doorstarter of senior te zijn en een bijzondere binding met het buurtschap te hebben. / 2.Bouwen alleen in het lint aangegeven op bijgevoegde kaart. […] Aldus vastgesteld in de vergadering van 18 februari 2020; Burgemeester en wethouders van Olst-Wijhe"

> "Voor de kern Elshof geldt ook dat de mogelijkheden beperkt zijn. Op dit moment is aan de zuid-oostzijde nog ruimte voor enkele kavels (aan de weg Elshof richting Engeweg) binnen het bestaande lint."

— Bron: Notitie Buurtschappenbeleid, Gemeenteblad 2020, 63767 / CVDR638025, https://zoek.officielebekendmakingen.nl/gmb-2020-63767.html (geraadpleegd 2026-10-04)

**Correctie op het concept.** Toevoegen in §1 (CPO-beleid), §2 (Herxen) en §3b (Engeweg/Elshof): Olst-Wijhe heeft een **gepubliceerde beleidsregel buurtschappen** (B&W 18-2-2020) voor Elshof en Herxen. Die staat bouwen toe voor starters, doorstarters en senioren met bijzondere binding, **alleen in het aangewezen lint**. Het maximum van 1 woning per jaar is geschrapt, uitdrukkelijk om "gezamenlijk bouwen" door starters niet te blokkeren. Dat is een vroeg CPO-signaal. Het Engeweg-initiatief (8 woningen, Elshof) en "CPO Herxen" (3 woningen) moeten tegen deze regel worden gelezen [INT]. Of Engeweg in het lint ligt, is niet vastgesteld.

---

## 4. Legesverordening 2026 en tarieventabel (prioriteit 4)

**Bevinding.** CVDR752237 is van **Olst-Wijhe** (zie tabel). De tarieventabel is in dezelfde regeling opgenomen; er is geen apart CVDR-nummer voor de tabel.
> "De raad van de gemeente Olst-Wijhe; gelezen het voorstel van burgemeester en wethouders d.d. 14 oktober 2025 nr. 38187-2025 […] Aldus besloten in de openbare raadsvergadering d.d. 24 november 2025."

— Bron: Gemeenteblad 2025, 561668 / CVDR752237 (geraadpleegd 2026-10-04)

Letterlijke tarieven (Hoofdstuk 2, Omgevingswet):
> "Artikel 2.4 Conceptverzoek […] a. voor het beoordelen van een conceptverzoek in verband met het verkrijgen van een indicatie of een voorgenomen project of ontwikkeling vergunbaar is | € 306,00 | b. voor een richtinggevende uitspraak van het gemeentebestuur (principebesluit) of zij wil meewerken aan het planologisch faciliteren van een conceptverzoek dat niet past in het omgevingsplan en alleen vergund kan worden na een herziening of wijziging van het omgevingsplan of met een omgevingsvergunning | € 1.225,00"

> "Artikel 2.5 Bouwactiviteit (Technisch) […] a. bij bouwkosten minder dan € 50.000,-, van de bouwkosten 2,5% met een minimum van € 117,50 / b. bij bouwkosten van € 50.000,- of meer, maar minder dan € 1.000.000,- van de bouwkosten 2,1% met een minimum van € 1.275,00 / c. bij bouwkosten van € 1.000.000,- of meer, van de bouwkosten 1,4% met een minimum van € 21.440,00 en een maximum van € 255.000,00"

> "Artikel 2.6 Bouwactiviteit (omgevingsplan) […] 1. voor een binnenplanse omgevingsplanactiviteit (geen wijzigingsbevoegdheid of uitwerkingsplicht) a. bij bouwkosten minder dan € 150.000,-, van de bouwkosten 2,0% met een minimum van € 155,00 b. bij bouwkosten vanaf € 150.000,- € 3.000,- vermeerderd met het volgende percentage van de bouwkosten boven € 150.000,- 1,0% met een totaal maximum van € 20.000,- […] 4. voor een buitenplanse omgevingsplanactiviteit, niet zijnde een kleine buitenplanse omgevingsplanactiviteit € 8.850 vermeerderd met het volgende percentage van de bouwkosten boven € 150.000,- 1% met een totaal maximum van € 20.515,00"

> "Artikel 2.7 Afwijken van regels in het omgevingsplan […] (geen bouwactiviteit) 1. voor een binnenplanse omgevingsplanactiviteit voor het afwijken van het omgevingsplan € 350,00 / 2. voor een kleine buitenplanse omgevingsplanactiviteit € 670,00 / 3. […] waarbij er geen (beoordeling van een) ruimtelijke motivering nodig is € 4.700,00 / 4. […] waarbij er een (beoordeling van een) ruimtelijke motivering nodig is € 7.800,00"

> "Artikel 2.21 Wijzigen van het omgevingsplan / Het tarief bedraagt voor het in behandeling nemen van een aanvraag tot het wijzigen van het omgevingsplan, waarbij geen sprake is van een bouwactiviteit: € 13.275,00"

> "Artikel 2.24 Uitgebreide voorbereidingsprocedure […] b. als sprake is van een buitenplanse omgevingsplanactiviteit: € 1.101,65"; "Artikel 2.25 Beoordeling onderzoeksrapporten […] c. voor de beoordeling van een landschappelijk inpassingsplan € 396,20 d. voor de beoordeling van een stedenbouwkundig plan € 396,20"; "Artikel 2.26 Advies […] a. voor een advies van de gemeenteraad (adviesrecht raad): € 521,70"; "Artikel 2.27 Instemming […] b. als een ander bestuursorgaan moet besluiten over de instemming: het bedrag dat dit bestuursorgaan aan rechten zou heffen als het voor de activiteit waarvoor instemming wordt verzocht zelf bevoegd gezag zou zijn"; "Artikel 2.28 Vermindering na conceptverzoek […] De vermindering bedraagt: 50% van de voor het conceptverzoek geheven leges […] c. binnen 12 maanden na het laatste conceptverzoek"

— Bron: Legesverordening 2026, CVDR752237, https://lokaleregelgeving.overheid.nl/CVDR752237 (geraadpleegd 2026-10-04)

Een apart tarief voor "vooroverleg" bestaat in hoofdstuk 2 niet; vooroverleg loopt via het conceptverzoek (art. 2.4). "Vooroverleg" komt alleen voor bij telecommeldingen (€ 253,50).

**BEREKENING (indicatief, door de onderzoeker; geen gemeentelijke opgave).** 10-12 woningen, bouwkosten excl. btw € 3,5 mln, route BOPA:

| Post | Grondslag | Bedrag |
|---|---|---|
| Bouwactiviteit technisch | 1,4% × 3.500.000 (art. 2.5c) | € 49.000,00 |
| BOPA met bouwactiviteit | 8.850 + 1% × 3.350.000 = 42.350 → **maximum** (art. 2.6 lid 4) | € 20.515,00 |
| Bindend advies raad (> 3 woningen buiten bebouwde kom, zie §5) | art. 2.26 lid 1a | € 521,70 |
| Beoordeling rapporten (bijv. 5 stuks: landschappelijk inpassingsplan, stedenbouwkundig plan, bodem, archeologie, overig) | 5 × € 396,20 (art. 2.25) | € 1.981,00 |
| Aftrek na conceptverzoek met principebesluit | −50% × € 1.225 (art. 2.28) | −€ 612,50 |
| **Subtotaal omgevingsvergunning** | | **≈ € 71.405** |
| Conceptverzoek met principebesluit (vooraf) | art. 2.4b | € 1.225,00 |
| Eventueel uitgebreide procedure | art. 2.24b | + € 1.101,65 |
| Provinciale instemming | art. 2.27 lid 1b: provinciaal tarief | onbekend |

Indicatief totaal ≈ **€ 72.600-73.700**, ofwel ca. € 6.000-7.300 per woning. Ruim twee derde daarvan komt uit de bouwactiviteit (technisch).

Alternatieve route via een omgevingsplanwijziging plus een binnenplanse vergunning: € 13.275 + € 49.000 + art. 2.6 lid 1 (3.000 + 1% × 3.350.000 = 36.500 → max **€ 20.000**) ≈ **€ 82.275** plus rapporten. Art. 2.21 geldt volgens de tekst alleen "waarbij geen sprake is van een bouwactiviteit"; of de gemeente bij een gecombineerd plan het art. 2.21-tarief heft, is niet vastgesteld [INT].

Kostenverhaal (anterieure overeenkomst) en de KGO-inspanning komen hier nog bovenop; dat zijn geen leges.

**Correctie op het concept §11** (kader "Tegenstrijdige bevinding"): vervangen door het volgende.
- CVDR752237 is **zeker Olst-Wijhe** (kop "Overheidsorganisatie Olst-Wijhe"), vastgesteld door de raad op **24-11-2025** (niet 10-11-2025), in werking 23-12-2025.
- De bedragen € 307,95 en € 516,45 komen **niet** voor in de tabel. Juist zijn € 350 (binnenplans afwijken), € 670 (kleine BOPA), **€ 4.700** (BOPA zonder ruimtelijke motivering) en **€ 7.800** (BOPA met ruimtelijke motivering, zonder bouwactiviteit).
- Met bouwactiviteit geldt de BOPA-staffel van € 8.850 + 1% met een maximum van € 20.515. De wijziging van het omgevingsplan kost € 13.275 en het conceptverzoek € 306 / € 1.225. Het bedrag van € 4.755 komt niet voor.
- Neem de berekening hierboven over, gemarkeerd als [berekening].

*Bijvangst:* de Legesverordeningen 2024 (Gmb 2024, 5367) en 2025 (Gmb 2024, 544288) zijn wel in het Gemeenteblad gepubliceerd, maar niet in CVDR opgenomen. Dat verklaart waarom eerdere zoekacties verwarrend waren.

---

## 5. Raadsadvies bij BOPA's (nieuw gevonden; procedureel bepalend voor 10-12 woningen)

**Bevinding.**
> "1. conform artikel 16.15a, lid b onder 10 van de Omgevingswet de volgende categorieën van gevallen van een buitenplanse omgevingsplanactiviteit aan te wijzen, waarvoor een bindend advies van de gemeenteraad nodig is: a. het bouwen van meer dan 12 woningen binnen de bebouwde kom en meer dan 3 woningen buiten de bebouwde kom; […] e. indien de activiteit niet past binnen door de gemeenteraad vastgestelde kaders en beleidsregels; […] Aldus besloten in de openbare raadsvergadering d.d. 7 februari 2022."

— Bron: CVDR704153 / Gmb 2023, 499448, https://lokaleregelgeving.overheid.nl/CVDR704153 (geraadpleegd 2026-10-04)

**Correctie op het concept §3c en Bijlage A E2.** Stap 5 (BOPA) moet aangeven dat bij **meer dan 3 woningen buiten de bebouwde kom** (dus een CPO van 10-12) een **bindend advies van de gemeenteraad** vereist is, naast de provinciale advies- en instemmingsrol (Lijst BOPA). Binnen de bebouwde kom ligt de grens op meer dan 12 woningen. Een CPO van 10-12 woningen binnen de bebouwde kom heeft dus géén raadsadvies nodig, tenzij het niet past in raadskaders (onder e). Dit verlengt de doorlooptijd en brengt het project in de raad [INT]. Legeskosten zijn € 521,70.

---

## 6. Nota Grondbeleid, kostenverhaal, Grondprijzenbrief, Lotingsreglement, kaveluitgifte, huisvestingsverordening (prioriteit 5)

### 6a. Nota Grondbeleid 2023-2026 (CVDR691005, Olst-Wijhe, raad)

> "Officiële naam regeling Nota Grondbeleid 2023 - 2026 […] Overheidsorganisatie Olst-Wijhe […] Vastgesteld door gemeenteraad […] Deze regeling vervangt de Nota Grondbeleid 2018-2021. […] 17-01-2023 nieuwe regeling 12-12-2022 gmb-2023-16454"

> "Beleidskeuze 1 / Situationeel grondbeleid is voor de looptijd van deze Nota het uitgangspunt. Per initiatief c.q. ontwikkeling wordt gekozen welke vorm van grondbeleid door de gemeente wordt gehanteerd: actief dan wel faciliterend."
> "Beleidskeuze 2 / De gemeente streeft er naar om, alvorens de planologische procedure wordt gestart, overeenstemming te bereiken met de initiatiefnemer door middel van het sluiten van een anterieure overeenkomst en geeft daarmee niet de voorkeur aan een Exploitatieplan."
> "De gemeente Olst-Wijhe geeft er de voorkeur aan om kosten te verhalen, door middel van een intentie-/samenwerkingsovereenkomst (SOK) en/of anterieure overeenkomst (kostendekkend). De berekening hiervan is maatwerk per project. Het ambtelijk uurtarief dat hierbij wordt doorberekend, wordt jaarlijks door het college vastgesteld in de Nota Rekentechnische uitgangspunten […] In anterieure overeenkomsten worden ook afspraken gemaakt over de vergoeding van eventuele toekomstige planschade (of nadeelcompensatie)"
> "Beleidskeuze 10 […] De grondprijzen worden daarbij jaarlijks vastgesteld door het college in de Grondprijzenbrief"
> "5. Onder voorbehoud van goedkeuring door het college, kan erfpacht als alternatief ingezet worden voor uitgifte van gronden."
> "Ad d. Vrije kavels (particulier opdrachtgeverschap) / […] Bij verkoop van een groter gebied, al dan niet projectmatig, kan het college beargumenteerd besluiten een korting te geven op de grondprijs. Dat kan met name aan de orde zijn als er sprake is van innovatieve initiatieven die maatschappelijk gezien wenselijk zijn en waarbij in één keer een grote hoeveelheid grond wordt afgenomen."
> "Situationeel grondbeleid geeft ruimte aan initiatieven en experimenten die een bijdrage leveren aan de ontwikkeling van onze gemeente"

— Bron: CVDR691005 / Gmb 2023, 16454, https://lokaleregelgeving.overheid.nl/CVDR691005 (geraadpleegd 2026-10-04)

De Gemeenteblad-publicatie bevat geen ondertekeningsdatum. CVDR noemt **12-12-2022** als datum van ondertekening/vaststelling. De "8-11-2022 (zaaknummer 51287-2022)" uit het concept is in de registers niet terug te vinden; waarschijnlijk is het een B&W-voorstel [INT].

**"Nota Grondbeleid 2024-2028":** bestaat **niet** voor Olst-Wijhe in CVDR of Gmb. Het concept/deelonderzoek koppelde CVDR720837 eraan, maar dat is **Harlingen**, "Nota grondbeleid 2024-2027". De geldende nota is 2023-2026 en verloopt eind 2026. Een opvolger is niet gevonden in Gmb of CVDR (stand 4-10-2026).

### 6b. Kostenverhaal in de praktijk (Gemeenteblad, zakelijke beschrijvingen)

De gemeente publiceert systematisch "Overeenkomst exploitatie …" met een vaste formule. Voorbeeld:
> "Het college van B en W heeft op 30 september 2024 een overeenkomst afgesloten voor de exploitatie van de locatie Vettewinkelweg 2 te Wijhe. Hiermee is het kostenverhaal van de voorgenomen ontwikkeling op deze locatie en de hiervoor benodigde planologische procedure verzekerd. U kunt de zakelijke beschrijving van de inhoud van de overeenkomst inzien bij ons klantcontactcentrum in Wijhe (Raadhuisplein 1). […] U kunt geen bezwaar of beroep indienen tegen de gesloten overeenkomst."

— Bron: Gemeenteblad 2024, 460019, https://zoek.officielebekendmakingen.nl/gmb-2024-460019.html (geraadpleegd 2026-10-04)

Buitengebied-overeenkomsten 2024-2025 (datum overeenkomst; Gmb):

| Locatie | Datum overeenkomst | Gemeenteblad |
|---|---|---|
| Scholtensweg 50 Wesepe | 19-11-2024 | Gmb 2024, 498712 |
| Elshagenweg 1 Wesepe | 28-1-2025 | Gmb 2025, 47545 |
| Lierderholthuisweg 12 | 5-2-2025 | Gmb 2025, 104887 |
| Zonnenbergerweg 1 Wesepe | 10-2-2025 | Gmb 2025, 104885 |
| Herxen 77/77a | 11-3-2025 | Gmb 2025, 104890 |
| Boerlestraat 8-8a | 12-3-2025 | Gmb 2025, 112233 |
| Het Anem 18 / Rietbergweg 12 | 25-3-2025 | Gmb 2025, 149089 |
| Diepenveenseweg 2 Olst | 5-6-2025 | Gmb 2025, 253991 |
| Lierderholthuisweg 13 | 9-9-2025 | Gmb 2025, 398661 |

Daarnaast zijn er tientallen overeenkomsten uit 2021-2023 (full-text "kostenverhaal": 67 treffers). Voor kernlocaties: Raalterweg 48-50 Wesepe (81 woningen, Sujo Real Estate 1 B.V., 3-6-2025, Gmb 2025, 250025) en Wengelerhoek (anterieure overeenkomst met Rotij, getekend 13-11-2025, Gmb 2025, 546713).

**Nota kostenverhaal:** niet gevonden. Er is geen aparte regeling in CVDR of Gmb; het kader is de Nota Grondbeleid.

**Correctie op het concept §11.** "Een aparte nota kostenverhaal is niet gevonden" is bevestigd. Toevoegen: de anterieure overeenkomst is in de praktijk **standaard**, ook voor 1-2 woningen in het buitengebied. De gemeente publiceert de zakelijke beschrijving, inzage alleen op afspraak. Voor de Vettewinkelweg 2 is de overeenkomst gesloten op 30-9-2024, vóór de aanvraag van 24-12-2024. §5: Nota Grondbeleid "vastgesteld 8-11-2022" vervangen door "**raad, vastgesteld 12-12-2022** (CVDR691005, Gmb 2023, 16454; in werking 17-1-2023)". De zin "vaststellend orgaan niet vastgesteld" vervalt.

### 6c. Grondprijzenbrief 2026, Lotingsreglement 2025, kaveluitgiftebeleid

- **Grondprijzenbrief 2026:** niet in Gmb of CVDR. Full-text "grondprijzenbrief" leverde alleen de Nota Grondbeleid op. Het is een collegebesluit (Nota, beleidskeuze 10) dat niet als beleidsregel wordt bekendgemaakt. De bedragen in het concept-kader blijven onverifieerbaar via registers. Vindplaats: https://www.olst-wijhe.nl/grondprijzenbrief of het B&W-besluit (deelonderzoek 1).
- **Lotingsreglement particuliere bouwkavels 2025** en de intrekking van het **Kaveluitgiftebeleid 2014**: niet in Gmb (full-text "lotingsreglement" / "kaveluitgifte" alleen de Nota en mandaatstatuten) en niet in CVDR. Het kaveluitgiftebeleid 2014 heeft ook nooit in CVDR gestaan. Vindplaats: gemeentelijke website of B&W-besluiten van 18-11-2025 en 2-12-2025.
- Wel gevonden: de gemeente publiceert uitgiftevoornemens "Didam-conform" in het Gemeenteblad:
  > "De herontwikkeling van de Klimboom bestaat uit de sloop van de bestaande bebouwing en het bouwen van zeventien (17) woningen. Het woningbouwprogramma bestaat uit vier (4) twee-onder-één-kapwoningen en negen (9) rijwoningen. Vier (4) woningen zijn sociale huurwoningen en vier (4) beneden-bovenwoningen zijn betaalbare vrijesectorwoningen. De andere negen (9) woningen zijn zogenoemde Collectief Particulier Opdrachtgeverschap (CPO) woningen. -De woningbouwkavels bestemd voor CPO worden niet via een openbare selectieprocedure verkocht."

  — Bron: "Uitvoering Arrest Didam in gemeente Olst-Wijhe – project Klimboom", Gemeenteblad 2024, 142870, https://zoek.officielebekendmakingen.nl/gmb-2024-142870.html (geraadpleegd 2026-10-04)

  In dezelfde publicatie staat: "acht de gemeente Olst-Wijhe dit arrest over Didam tevens van toepassing op het vestigen van zakelijke rechten (zoals erfpacht of opstal)". Er is een 20-dagen-kortgedingtermijn.

**Correctie op het concept §1/§5/§7 (Klimboom).** Toevoegen dat de Didam-publicatie (Gmb 2024, 142870) bevestigt dat 9 van de 17 woningen CPO zijn en dat de CPO-kavels **zonder openbare selectie** zijn uitgegeven (maatwerkuitgifte). Dat is een bruikbaar precedent voor 1-op-1 uitgifte aan een CPO-vereniging.

### 6d. Huisvestingsverordening

**Bevinding.** Onder alle 628 CVDR-records van Olst-Wijhe (inclusief ingetrokken versies, vanaf 2001) staat **geen huisvestingsverordening, urgentieverordening of woonruimteverdelingsregeling**. De enige "huisvesting"-titels zijn de verordeningen voorzieningen huisvesting onderwijs (2001, 2012, 2020) en het "Handelingskader opvang vluchtelingen en huisvesting statushouders" (CVDR765985, B&W 7-11-2024, gepubliceerd Gmb 2026, 409157). Een CVDR-keywordzoekactie "Olst-Wijhe" + titel "huisvestingsverordening" levert alleen **Heerde** "Huisvestingsverordening 2002" op (CVDR111196, uitgewerkt 2004): een Gelderse regeling, niet van Olst-Wijhe. Gmb full-text "huisvestingsverordening" (Olst-Wijhe) levert alleen een Bibob-beleidslijn uit 2014 op.

**Correctie op het concept §8.** "Aanwezig: niet vastgesteld" kan scherper: **Aanwezig: nee.** In CVDR en Gemeenteblad is geen (huidige of eerdere) huisvestingsverordening van Olst-Wijhe en geen regionale verordening met Olst-Wijhe als deelnemer gevonden. De zin "Niet uitgesloten: de CVDR-zoekfunctie kon niet worden gefilterd" vervalt. Een nieuwe verordening in voorbereiding (B&W 18-8-2026) is niet als ontwerp gepubliceerd.

---

## 7. Netcongestie-beleidsregels en volgordelijst (prioriteit 5)

**Bevinding: kandidaat-nummers.**
- **gmb-2026-415179** = **Brunssum** ("Datum publicatie 03-09-2026 | Organisatie Brunssum […] Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten en onderwijshuisvesting Brunssum 2026"). Niet Olst-Wijhe.
- **gmb-2026-421329** = **Lansingerland** ("09-09-2026 09:00 | Lansingerland | Gemeenteblad 2026, 421329 | beleidsregel"). Niet Olst-Wijhe.
- Het juiste nummer is **Gemeenteblad 2026, 385444** (13-08-2026, organisatie Olst-Wijhe) = **CVDR765519**, geldend vanaf 14-08-2026, vastgesteld door B&W op 11-08-2026.

— Bronnen: https://zoek.officielebekendmakingen.nl/gmb-2026-415179.html, …/gmb-2026-421329.html, …/gmb-2026-385444.html, https://lokaleregelgeving.overheid.nl/CVDR765519 (geraadpleegd 2026-10-04)

Prioriteringscriteria (letterlijk):
> "Artikel 5 […] 2. Het in het eerste lid bedoelde verzoek kan worden ingediend tot en met 27 augustus 2026 / 3. Opname van een project op de volgordelijst resulteert in een inspanningsverplichting van de gemeente […] zonder dat de gemeente de beschikbaarheid of toewijzing van prioritering en transportcapaciteit garandeert."

> "Artikel 9. Rangordebepaling volgordelijst […] Stap 1: start bouw / Als eerste stap vindt een rangschikkingsplaats op basis van de maand van start bouw, waarbij een project hoger wordt gerangschikt als de bouw eerder start. Hierbij moet de maand van start bouw voldoende concreet zijn onderbouwd. / Stap 2: projectrijpheid […] 1 Er is een civielrechtelijke overeenkomst, en een onherroepelijk omgevingsvergunning voor een bouwactiviteit verleend voor de projectlocatie. 2 Er is een civielrechtelijke overeenkomst, en een onherroepelijk omgevingsplan vastgesteld of onherroepelijke vergunning voor een BOPA verleend voor de projectlocatie. 3 Er is alleen een onherroepelijke omgevingsvergunning verleend voor de projectlocatie. 4 Er is alleen een civielrechtelijke overeenkomst. 5 Er is alleen een omgevingsplan vastgesteld of vergunning voor een BOPA verleend voor de projectlocatie 6 Er zijn andere bewijsstukken waardoor een project in aanmerking komt voor prioritering. / Stap 3: maatschappelijk belang […] a. de projectlocatie draagt substantieel bij (in termen van aantal woningen) aan de gemeentelijke focus op wonen. b. Het project draagt bij aan en evenwichtige spreiding van wooninitiatieven over de kernen. […] Stap 4: datum oplevering"

> "Artikel 10 […] Als twee of meer projecten […] dezelfde positie behalen, bepaalt de gemeente de onderlinge volgorde door middel van een openbare loting."

> "Woningbouw — collectieve woonvormen: 1. Bestuursverklaring (zie artikel 5); 2. Overeenkomst over collectieve woonvorm (primair) óf omgevingsplan (fallback)." (toelichting art. 6) en het indieningsadres "netcongestie@olst-wijhe.nl"

— Bron: CVDR765519 (geraadpleegd 2026-10-04)

Een tweede aanmeldronde is in de beleidsregels niet geregeld. Art. 5 kent één venster tot en met 27-8-2026. Bij nieuwe rondes is een wijziging van de beleidsregels nodig [INT].

**Voorlopige volgordelijst** (B&W; Gemeenteblad 2026, 422235, 10-09-2026):
> "Tot en met 27 augustus konden initiatiefnemers zich hiervoor aanmelden. Bij deze maakt de gemeente de volgordelijst bekend van de in dit verband ingediende woningbouwinitiatieven. […] Eenieder die bezwaar heeft […] kan binnen 10 kalenderdagen na bekendmaking […] bezwaar indienen […] via netcongestieow@olst-wijhe.nl"

De lijst telt **47 regels met samen 1.400 woningen** (telling door de onderzoeker). Relevante regels (plannaam | locatie | kern | start bouw | projectrijpheid | woningen):

| Plannaam | Locatie | Kern | Start bouw | Projectrijpheid | Woningen |
|---|---|---|---|---|---|
| Engeweg Elshof | Engeweg | Elshof | 2027 | 6 | 8 |
| CPO Herxen | Kromme Koeweg | Herxen | 2027 | 6 | 3 |
| **CPO Boerhaar** | Boerhaar 18, 18a, 20 | Boerhaar | 2027 | 4 | **24** |
| **Wijlandhof** | Elshof nabij 19a | Elshof | 2027 | 6 | **12** |
| **De Brinkweiden** | Kappeweg 18 | **Buitengebied** | 2028 | 6 | **12** |
| Hemelrijk 2 | Hemelrijk 2 | Welsum | 2027 | 1 | 18 |
| Herontwikkeling Holsthoek | Holstweg 29 | Den Nul | 2028 | 6 | 19 |
| Kloosterhoekweg 3 rood voor rood | Kloosterhoekweg 3 | Welsum | 2027 | 3 | 2 |
| Kappeweg 1 | Kappeweg 1a, 1b | Buitengebied | 2027 | 4 | 3 |
| Lierderholthuisweg 12a, 12b | | Buitengebied | 2029 | 1 | 2 |
| Klimboom Boskamp | Hyacintstraat | Boskamp | 2027 | 1 | 18 |
| Wengelerhoek | Omloop/Zanduishuisweg | Wijhe | 2028 | 2 | 135 |
| Wijhe Noord | Het Anem 2 | Wijhe | 2028 | 6 | 309 |
| Olst NoordOost | Kleistraat-Enkweg-Averbergen | Olst | 2029 | 6 | 185 |
| Olst Zuid | Vink | Olst | 2030 | 6 | 90 |
| Gebiedsaanpak Wesepe | Meerdere locaties | Wesepe | 2029 | 6 | 88 |

— Bron: Gemeenteblad 2026, 422235, https://zoek.officielebekendmakingen.nl/gmb-2026-422235.html (geraadpleegd 2026-10-04)

**Correctie op het concept §5 (netcongestie), §6, §7 en Tegenstrijdigheid 17.**
- Het nummer is **Gmb 2026, 385444 / CVDR765519** (B&W 11-8-2026). De kandidaten 415179 (Brunssum) en 421329 (Lansingerland) moeten worden geschrapt.
- Citeer de vier stappen (start bouw → projectrijpheid 1-6 → maatschappelijk belang [omvang; spreiding over kernen] → opleverdatum; daarna loting). Projectrijpheid beloont een **civielrechtelijke overeenkomst** plus een onherroepelijke vergunning of BOPA. Een CPO zonder grondpositie of overeenkomst valt in categorie 6. Collectieve woonvormen hebben een eigen subfunctie ("collectieve woonvormen") met als bewijsstuk een "overeenkomst over collectieve woonvorm".
- Dat de lijst op 1-10-2026 bij **Enexis** is aangeleverd, staat niet in de beleidsregels of de lijst (de netbeheerder wordt niet bij naam genoemd); zo niet vermelden zonder andere bron.
- Het aantal **47** is bevestigd.
- §6/§7 aanvullen met de **buitengebied/buurtschap-initiatieven van 12-24 woningen** op de lijst: **CPO Boerhaar (24)**, **Wijlandhof Elshof (12)**, **De Brinkweiden Kappeweg 18, buitengebied (12)**, Holsthoek Den Nul (19), Hemelrijk 2 Welsum (18). Dit zijn initiatieven op precies de schaal van het CPO-concept of groter, buiten de grote kernen. Status en planologie (projectrijpheid 4-6) zijn niet onderzocht. CPO Boerhaar is het meest vergelijkbare lopende initiatief.

---

## 8. Concrete dossiers in het Gemeenteblad (prioriteit 7)

### 8a. Lierderholthuisweg 3 (Gmb 2026, 169650 en vervolg)
> "Ontvangen aanvraag voor een omgevingsvergunning, het wijzigen van de bestemming, het splitsen van de bestaande woning, het bouwen van een vrijstaande woning en het aanplanten van bos, Lierderholthuisweg 3 en (voorlopig) 3a en 3b 8131PW Wijhe / Ontvangstdatum: 07-04-2026 […] Zaaknummer: 1773ESUITE151652026 / Activiteiten: - Werk, niet zijnde bouwwerk, of werkzaamheid uitvoeren - Bouwactiviteit (omgevingsplan) - Afwijken van regels in het omgevingsplan"

— Bron: Gemeenteblad 2026, 169650 (publicatie 10-04-2026), https://zoek.officielebekendmakingen.nl/gmb-2026-169650.html (geraadpleegd 2026-10-04)

Vervolg: termijn verlengd tot 17-7-2026 (Gmb 2026, 273043, 10-6-2026). Daarna:
> "Verleende omgevingsvergunning, het wijzigen van de bestemming, het splitsen van de bestaande woning, het bouwen van een vrijstaande woning en het aanplanten van bos, Lierderholthuisweg 3, (voorlopig) 3a en 3b Wijhe / Verzenddatum besluit: 23-06-2026"

— Bron: Gemeenteblad 2026, 302246, https://zoek.officielebekendmakingen.nl/gmb-2026-302246.html (geraadpleegd 2026-10-04)

Het besluit is genomen met een **reguliere procedure** (bezwaar binnen 6 weken). Over provinciale instemming staat niets in de bekendmaking. Het principebesluit van 20-1-2026 en "1,5 ha bos (Bossenstrategie)" staan niet in de registers.

**Correctie §3b/§3c/§6 #5.** De vergunning is **verleend op 23-6-2026**. De doorlooptijd van aanvraag tot besluit was **ca. 11 weken** (7-4 → 23-6-2026). De "[INT]-schatting 12-24 maanden" moet worden gerelativeerd: principebesluit (20-1) → aanvraag (7-4) → vergunning (23-6-2026) is ca. 5 maanden voor een KGO-dossier van 2 extra woningen.

### 8b. Vettewinkelweg 2
> "Ontvangen aanvraag voor een omgevingsvergunning, het wijzigen van de functie van agrarisch naar wonen en het bouwen van een vrijstaande woning, Vettewinkelweg 2 en (voorlopig) 2a, 8131SZ Wijhe / Ontvangstdatum: 24-12-2024 […] Activiteiten: - Afwijken van regels in het omgevingsplan - Bouwactiviteit (omgevingsplan)" (Gmb 2025, 1450)

> "Verleende omgevingsvergunning, het wijzigen van de functie van agrarisch naar wonen en het bouwen van een vrijstaande woning, Vettewinkelweg 2 en 2a 8131SZ Wijhe / Verzenddatum besluit: 07-04-2025" (Gmb 2025, 154624)

Anterieure overeenkomst 30-9-2024 (Gmb 2024, 460019).

— Bronnen: https://zoek.officielebekendmakingen.nl/gmb-2025-1450.html, …/gmb-2025-154624.html, …/gmb-2024-460019.html (geraadpleegd 2026-10-04)

Provinciale instemming wordt in de bekendmakingen **niet genoemd**. In het Provinciaal blad staat geen instemmingsbesluit; instemmingen worden daar niet gepubliceerd.

**Correctie §3b/§6 #6.** Toevoegen: anterieure overeenkomst 30-9-2024 → aanvraag 24-12-2024 → **vergunning verleend 7-4-2025** (ca. 15 weken, reguliere procedure). Of provinciale instemming formeel is verleend, blijkt niet uit de registers. Dat er is verleend, impliceert dat instemming niet is onthouden [INT].

### 8c. Engeweg/Elshof
Er staat **geen BOPA-aanvraag** voor de 8 woningen in het Gemeenteblad (stand 4-10-2026; full-text "Engeweg" 18 treffers, alleen oudere dossiers en een woningsplitsing Engeweg 6/6a, verleend 9-10-2025, Gmb 2025, 437654). Het project staat op de volgordelijst: "Engeweg Elshof | Engeweg | Elshof | 2027 | 6 | 8" (Gmb 2026, 422235). Projectrijpheid 6 betekent: nog geen overeenkomst, vergunning of omgevingsplan.

**Correctie §3b/§6 #1.** Toevoegen: stand 4-10-2026 nog geen aanvraag gepubliceerd, geen anterieure overeenkomst gepubliceerd, voorziene start bouw 2027 volgens de volgordelijst. Raadsadvies is vereist (> 3 woningen buiten de bebouwde kom, §5). Het buurtschappenlint Elshof is relevant (§3).

### 8d. Andere BOPA's en plannen voor wonen in het buitengebied 2024-2026 (nieuw; aanvulling §6)

| Locatie | Inhoud (citaat titel) | Besluit | Bron |
|---|---|---|---|
| **Zandhuisweg 7, Wijhe** | "het realiseren van drie vrijstaande woningen, vier onder één kapwoning en het splitsen van de bestaande boerderij tot twee woningen" (**9 woningen**) | aanvraag 6-11-2025, verleend 25-11-2025 (regulier) | Gmb 2025, 486680 en 514083 |
| **Steunenbergerweg 6, Olst** | "Dit plan maakt de realisatie van in totaal zeven woningen mogelijk door de wijziging van het bouwvlak op het 'achtererf' en de splitsing van de boerderij op het 'voorerf'." (**7 woningen**) | raad 26-2-2024 ongewijzigd vastgesteld | Gmb 2024, 97300 |
| IJsseldijk 115, Welsum | "acht woonzorg-studio's in de schuur van een karakteristieke boerderij" | raad 26-2-2024 | Gmb 2024, 97295 |
| De Wesenberg 3, Wijhe | KGO: sloop, "ter compensatie twee woningen" | raad 26-2-2024 | Gmb 2024, 93285 |
| Wechterholt 11-11a | KGO: 1 vrijstaande woning | raad 6-2-2024 | Gmb 2024, 64287 |
| Boxbergerweg 2 Olst | 2 woningen (landgoed Zorgvliet, verplaatsing) | raad 5-2-2024 | Gmb 2024, 62122 |
| Herxerenk 1 | karakteristiek bijgebouw naar woning | B&W 13-2-2024 | Gmb 2024, 72252 |
| Boxbergerweg 31-31a | 2 woningen + bedrijvigheid | raad 25-3-2024 | Gmb 2024, 142384 |
| Elshagenweg 1 Wesepe | "het wijzigen van de bestemming agrarisch naar wonen" | verleend 5-2-2025 | Gmb 2025, 59989 |
| Lierderholthuisweg 12/16 | "afwijken van de bedrijfsbestemming ten behoeve van wonen" | verleend 18-2-2025 | Gmb 2025, 71158 |
| Zonnenbergerweg 1 Wesepe | wijzigen bestemming | verleend 14-7-2025 | Gmb 2025, 310489 |
| Boerhaar 43 | wijzigen bestemming (en splitsen) | verleend 14-10-2025 | Gmb 2025, 447370 |
| Damshoekweg 1 Olst | bestemming + vrijstaande woning | verleend 7-11-2025 (publicatie) | Gmb 2025, 482771 |
| Kloosterhoekweg 3 Welsum | "het wijzigen van agrarische bestemming naar wonen" (op de volgordelijst "rood voor rood", 2 woningen) | verleend 12-5-2026 | Gmb 2026, 228113 |
| Scholtensweg 50 Wesepe | "het wijzigen van de bestemming voor het realiseren van drie woningen" | verleend 28-5-2026 | Gmb 2026, 255064 |
| Kletterstraat 7 Olst | extra woning | verleend 1-7-2026 (publicatie) | Gmb 2026, 313307 |
| Prinshoeveweg 1 / Scherpenzeelseweg 13a | wonen + vrijstaande woning (LBV) | termijn verlengd 29-7-2026 | Gmb 2026, 363854 |

Toelichting bij Steunenbergerweg 6:
> "Het voormalige agrarische erf wordt een woonerf met 7 wooneenheden." / "voor het achtererf is in 2019 al een bestemmingsplan vastgesteld die het mogelijk maakt er 4 woningen te realiseren" / "De gemeente Olst-Wijhe heeft op 20 september 2022 aangegeven onder voorwaarden in principe medewerking te willen verlenen" / "Door de splitsing ontstaan drie relatief betaalbare woningen die geschikt zijn voor starters." / "Het bestemmingsplan wordt voor vooroverleg naar de provincie Overijssel gestuurd." / "Het ontwerp bestemmingsplan heeft vanaf 21 december 2023 gedurende zes weken ter inzage gelegen. Tijdens deze periode zijn geen zienswijzen ingediend."

— Bron: toelichting NL.IMRO.1773.BP2023001099-0301, https://www.ruimtelijkeplannen.nl/documents/NL.IMRO.1773.BP2023001099-0301/t_NL.IMRO.1773.BP2023001099-0301.html (geraadpleegd 2026-10-04)

Ligging Zandhuisweg 7 [INT]: PDOK plaatst het adres in de CBS-buurt "Krijtenberg en Noorder Koeslag" (Wijk 02 Wijhe), dus aan de rand van de kern Wijhe. De vervolgvergunning noemt het adres "Dolskamp (voorlopig) 23" (Gmb 2026, 260809), en op de volgordelijst heet Wengelerhoek "Omloop/Zanduishuisweg". Het gaat dus waarschijnlijk om een **kernrandlocatie**, niet het open buitengebied. De planologische status is niet vastgesteld.

**Correctie §3(e), §6 en de kernvragen.** De bewering "4-8 woningen … alleen maatwerk; 10-12 kansarm" moet worden genuanceerd met deze precedenten.
- Een **erf in het buitengebied met 7 woningen** is via een bestemmingsplan vastgesteld zonder zienswijzen (Steunenbergerweg 6, raad 26-2-2024; buurt Middel).
- Er is een **BOPA voor 9 woningen** (Zandhuisweg 7, 2025), vermoedelijk aan de kernrand.
- Er staan buurtschap- en buitengebiedinitiatieven van **12-24 woningen** op de volgordelijst (CPO Boerhaar, Wijlandhof, De Brinkweiden).

Of deze laatste planologisch kansrijk zijn, is niet onderzocht.

### 8e. Omgevingsvisie Olst-Wijhe
> "Door middel van deze publicatie legt het college van burgemeester en wethouders van de gemeente Olst-Wijhe de ontwerp-Omgevingsvisie Olst-Wijhe ter inzage." (Gmb 2024, 477293, 12-11-2024)

> "Wilt u de ontwerp-Omgevingsvisie inzien dan kan dat vanaf 13‑10‑2024. Dan ligt het ontwerp ter inzage tot en met 27 december. […] In het eerste kwartaal van 2025 neemt de gemeenteraad een besluit." (Gmb 2024, 480688, 14-11-2024)

"13-10-2024" in een publicatie van 14-11-2024 is kennelijk een verschrijving voor 13-11 [INT].

Een **Gemeenteblad-bekendmaking van de vastgestelde Omgevingsvisie is niet gevonden**: geen treffer op titel "visie", type "ruimtelijk plan of omgevingsdocument" of full-text "Omgevingsvisie Olst-Wijhe" in 2025-2026. Wel bevestigt een latere publicatie de vaststelling door de raad:
> "In de Omgevingsvisie 'Omgevingsvisie Olst Wijhe 2050' heeft de gemeenteraad vier algemene principes benoemd: •Een gezonde en veilige leefomgeving, nu en op de lange termijn en in alle gebieden •Gebiedskenmerken centraal voor nieuwe ontwikkelingen •Meervoudig ruimtegebruik: niet alles kan overal •Water en bodem als basis voor ruimtelijke ontwikkelingen"

— Bron: Uitvoerings- en handhavingsstrategie gemeente Olst-Wijhe, Gemeenteblad 2026, 70702 / CVDR757170, https://zoek.officielebekendmakingen.nl/gmb-2026-70702.html (geraadpleegd 2026-10-04)

**Tegenstrijdigheid 3 (12 of 13 mei 2025):** niet oplosbaar via registers. Vindplaats: raadsbesluit in iBabs (deelonderzoek 1) of het DSO-viewerdocument.

---

## 9. Provinciaal blad Overijssel: "Olst-Wijhe" 2023-2026 (prioriteit 8)

**Bevinding.** De SRU-zoekactie `dt.creator="Overijssel" AND dt.date>=2023-01-01 AND cql.textAndIndexes="Olst-Wijhe"` leverde **69 publicaties** op. Daaronder **geen** zienswijze, reactieve interventie, aanwijzing of (onthouden) instemming tegen een Olst-Wijhes omgevingsplan, BOPA of bestemmingsplan. De treffers betreffen dijkversterking Zwolle-Olst (HWBP), het projectbesluit IJsseluiterwaarden Fortmond-Duursche Waarden, wegwedstrijden, BUS-saneringen, de GR Omgevingsdienst IJsselland, de voorbereidingsbesluiten wind en zon (beëindigd, Prb 2025, 2265), subsidieplafonds en het Uitvoeringsbesluit subsidies.
- Subsidie **4.39**: alleen het plafond is gepubliceerd. Toekenningen per gemeente worden niet in het Prb gepubliceerd.
  > "4.39 Beleid transformatie agrarische bebouwing, erven en gronden / Het subsidieplafond voor 2025 en 2026 is in totaal samen: € 1.640.250,- (was € 1.640.250,- voor 2025)."

  — Bron: Provinciaal blad 2025, 17002 (GS-besluit 14-10-2025), https://zoek.officielebekendmakingen.nl/prb-2025-17002.html (geraadpleegd 2026-10-04)
- *Bijvangst voor `provincie_overijssel.md` §6.1:*
  > "Gedeputeerde Staten van Overijssel besluiten: Artikel I het ontwerp Volkshuisvestingsprogramma voor Overijssel 2026-2032 vast te stellen […] Zwolle, 30 juni 2026"

  — Bron: Provinciaal blad 2026, 11834 (publicatie 10-07-2026), https://zoek.officielebekendmakingen.nl/prb-2026-11834.html (geraadpleegd 2026-10-04)

  Titel "2026-2035", artikeltekst "2026-2032". Relevante passages:
  > "in sommige gevallen kan ook transformatie van vrijkomende agrarische bebouwing een kans bieden, mits deze in de directe nabijheid van een dorp ligt." / "Collectieve woonvormen passen hier goed bij: ze versterken de sociale cohesie én helpen de lokale woningvraag te vervullen." / VAB: "Stimuleren om meer gebiedsgericht geclusterd te ontwikkelen."

  Het programma noemt Olstergaard als voorbeeld:
  > "De wijk omvat een mix van 48 koopwoningen (grotendeels particulier opdrachtgeverschap), 13 sociale huurwoningen van woningcorporatie SallandWonen en twee woongebouwen. Deze gebouwen huisvesten 11 appartementen van 'Grijs en Groen Wonen', een project voor 50-plussers met een gemeenschappelijke huiskamer, logeerkamer en tuin."

  BuitenDelen Lettele wordt in het programma "een collectief particulier opdrachtgeverschap-project (CPO) op een voormalig agrarisch erf" genoemd.

**Correctie op het concept, Bijlage A E4.** Het concept zegt "Prb en Gemeenteblad niet doorzoekbaar". Dat moet worden: **doorzocht; geen provinciale zienswijze, aanwijzing of onthouden instemming 2023-2026 gevonden** (Prb, 69 treffers op "Olst-Wijhe"). Kanttekening: instemmingsbesluiten op BOPA's en vooroverlegreacties worden niet in het Prb gepubliceerd, dus "geen onthouden instemming gevonden" is een beperkte negatieve bevinding. Wel zijn alle gevonden buitengebied-BOPA's 2025-2026 **verleend** en is geen BOPA geweigerd (geen "geweigerde omgevingsvergunning" voor wonen in de Gmb-lijst; de enige weigering betreft het kappen van knotwilgen, Gmb 2026, 49115).

---

## 10. Volkshuisvestingsprogramma / woningbouwprogramma Olst-Wijhe (prioriteit 9)

**Bevinding.** Er is geen ontwerp of vastgesteld Volkshuisvestingsprogramma, woningbouwprogramma of nieuwe woonvisie van Olst-Wijhe in Gmb of CVDR gepubliceerd. Full-text "volkshuisvestingsprogramma" (Olst-Wijhe) leverde 0 treffers op; "woonvisie" alleen de Nota Grondbeleid, de Notitie Buurtschappenbeleid, een beheersverordening en de UHS. De Woonvisie 2022-2025 staat zelf ook **niet** in CVDR/Gmb. Het provinciale ontwerpprogramma is wel gepubliceerd (§9).

**Correctie A4.** De status "niet gevonden (programma in voorbereiding)" is bevestigd voor de registers. Voeg het provinciale ontwerp-VHP toe (Prb 2026, 11834) als context.

---

## Tegenstrijdigheden (genummerde lijst onderaan het concept)

| # | Status | Toelichting |
|---|---|---|
| 1 Reikwijdte 5/10 | **Niet oplosbaar via registers** | Geen beleidsregel "woningsplitsing en kleinschalige initiatieven" in CVDR/Gmb. De Handreiking KGO noemt geen 5/10. Vindplaats: beleidspagina wonen.olst-wijhe.nl en het onderliggende B&W-besluit (deelonderzoek 1). |
| 2 Grondprijzenbrief/leges | **Leges opgelost** (§4: CVDR752237 = Olst-Wijhe, raad 24-11-2025, tarieven geciteerd). **Grondprijzenbrief niet oplosbaar** via registers (niet gepubliceerd). | |
| 3 Omgevingsvisie 12/13 mei | **Niet oplosbaar** | Geen Gmb-bekendmaking van de vaststelling. Ontwerp: Gmb 2024, 477293 en 480688 (ter inzage tot 27-12-2024). Vaststelling door de raad bevestigd in Gmb 2026, 70702 zonder datum. |
| 4 Handreiking KGO | **Grotendeels opgelost** | Document gedateerd 28 mei 2024, vastgesteld door het college. Sloop bij 2 vrijstaande woningen 2.000 m², bij 2 woningen in één blok (≤ 800 m³) 1.000 m²: beide samenvattingen deels juist (citaat §2). Niet als beleidsregel bekendgemaakt. De datum van de motie (13-11-2023 of 2024) staat niet in de handreiking. |
| 5 Omgevingsplan CVDR696503 | **Opgelost** | 01-01-2024 (Stb 2023, 113) → 17-04-2024 → 06-06-2025 → **03-09-2026 (huidig)**, alle gemeentelijke versies technisch (§1). |
| 7 Plancapaciteit 161/339 | **Niet oplosbaar** | Niet in registers. Als ander meetpunt: de volgordelijst netcongestie telt 47 initiatieven met 1.400 woningen (Gmb 2026, 422235). Dat is geen plancapaciteitscijfer. |
| 8 Sociale huur % | **Niet oplosbaar via registers** | Er is geen huisvestingsverordening (§6d) en de woonvisie staat niet in CVDR. |
| 9 Aantal kernen | **Gedeeltelijk** | De volgordelijst hanteert als "Kern": Olst, Wijhe, Wesepe, Boskamp, Den Nul, Welsum, Herxen, Elshof, Boerhaar en "Buitengebied". De Notitie Buurtschappenbeleid noemt Elshof en Herxen "dorpen"/"kernen" met buurtschappenbeleid. Een formele telling is niet gevonden. |
| 11 Olstergaard-aantallen | **Gedeeltelijk opgelost** | Ontwerp-VHP Overijssel (Prb 2026, 11834): 48 koopwoningen + 13 sociale huur + 11 appartementen Grijs en Groen Wonen = 72 woningen (provinciale weergave). Volgordelijst: nog 2 woningen "Olstergaard / Sterappel". |
| 12 Klimboom | **Gedeeltelijk** | Gmb 2024, 142870: 17 woningen (9 CPO, 4 sociale huur, 4 beneden-boven). De volgordelijst 2026 noemt "Klimboom Boskamp | Hyacintstraat | 18" woningen. Het verschil 17/18 is niet verklaard. |
| 13 Grijs en Groen Wonen / Vriendenerf | **Opgelost voor Grijs en Groen** | Grijs en Groen Wonen (11 appartementen) ligt in Olstergaard (Prb 2026, 11834). Het is dus een ander project dan Vriendenerf. |
| 14 Landschapsbeschrijving | **Opgelost (consistent)** | Gmb 2026, 70702: "Aan weerszijden van de IJssel liggen de oeverwallen […] Belangrijke drogere gronden doorsneden door laagtes, liggen in het oosten en zuiden van de gemeente." De IJssel vormt de westgrens; de samenvatting is dus geografisch juist. |
| 16 Nota Grondbeleid 2023-2026 vs. "2024-2028" | **Opgelost** | Olst-Wijhe kent alleen de Nota Grondbeleid 2023-2026 (CVDR691005, raad 12-12-2022). "2024-2027" is Harlingen (CVDR720837). Een "2024-2028" is niet gevonden. |
| 17 Netcongestie-nummers | **Opgelost** | Gmb 2026, 385444 / CVDR765519 (B&W 11-8-2026). 415179 = Brunssum, 421329 = Lansingerland. |
| 19 Engeweg | **Niet opgelost (typen)** | Volgordelijst bevestigt 8 woningen, projectrijpheid 6, start bouw 2027. Geen aanvraag gepubliceerd. |
| 20 Systematisch | **Opgelost voor CVDR** | Alle nummers geverifieerd in de kop (§0). |

Niet van toepassing op dit brontype: 6, 10, 15, 18. Bij 15 (CPO "5-50"): niet in de registers.

---

## Bijlage A-punten (brontype registers)

| # | Bevinding | Status | Bron |
|---|---|---|---|
| A4 | Geen (ontwerp-)volkshuisvestingsprogramma, woningbouwprogramma of woonvisie van Olst-Wijhe in Gmb of CVDR. Provinciaal ontwerp-VHP Overijssel wel gepubliceerd (GS 30-6-2026; VAB "mits deze in de directe nabijheid van een dorp ligt"; collectieve woonvormen "passen hier goed bij"). | Niet gevonden (gemeentelijk); provinciale context gevonden | Prb 2026, 11834; SRU Gmb |
| A5 | Geen huisvestingsverordening of urgentieregeling (CVDR, alle versies sinds 2001; Gmb). Wel "Handelingskader opvang vluchtelingen en huisvesting statushouders" (CVDR765985). | Niet gevonden (= niet aanwezig in registers) | CVDR-SRU; Gmb 2026, 409157 |
| B1 | Eigen kader: Handreiking KGO (college, 28-5-2024), **niet** als beleidsregel bekendgemaakt (geen CVDR/Gmb). Rekenregels: 1 woning ≤ 750 m³ / 1.000 m²; 2 vrijstaand / 2.000 m²; 2 in blok ≤ 800 m³ / 1.000 m²; 3 in blok ≤ 1.200 m³ / 1.600 m²; max. 2 bouwblokken per erf; woning vergroten 1 m³ : 4 m². CVDR305226 = **Tubbergen**, vervallen. | Gevonden (document); niet in register | iBabs ba55b732…; CVDR305226 |
| B3 | Omgevingsplan = tijdelijk deel. Versies 2024-2026 zijn alleen technisch. Bestemmingsplan Buitengebied 2021: vervolgfuncties zonder extra woningen (art. 3.9.5 p), splitsing alleen karakteristiek (art. 44.1). Geen aanpassing aan Actualisatie 2026 gevonden. | Gevonden (geen aanpassing) | CVDR696503; r_NL.IMRO.1773.BP2020001001-0301 |
| B5 | Kostenverhaal en voorwaarden via **anterieure overeenkomst** (Nota Grondbeleid beleidskeuze 2; tientallen gepubliceerde zakelijke beschrijvingen, ook voor 1-2 woningen in het buitengebied). Fonds: "Voorziening Ruimtelijke Kwaliteit". Bankgarantie niet in de registers gevonden. | Gevonden | CVDR691005; Gmb 2024, 460019 e.v. |
| C3 | Overlays in de registers: geurverordeningen veehouderij (CVDR331496; "Verordening geurhinder en veehouderij Boskamp 2019", CVDR639927); voorkeursrecht Wengelerhoek en Wesepe West (Gmb 2024, 72340/201497; 2025, 296643/418205). NNN en grondwaterbescherming niet via dit brontype. | Deels gevonden | CVDR; Gmb |
| C4 | Netcongestie: beleidsregels CVDR765519 (vier stappen + loting; aanmelden t/m 27-8-2026); voorlopige volgordelijst Gmb 2026, 422235 (47 initiatieven / 1.400 woningen). Geen tweede ronde geregeld. | Gevonden | CVDR765519; Gmb 2026, 422235 |
| D1 | Prb: plafond 4.39 € 1.640.250 (2025-2026) ongewijzigd per 14-10-2025. Toekenning aan Olst-Wijhe is niet in het Prb of Gmb gepubliceerd. | Niet gevonden (deelname) | Prb 2025, 17002 |
| E2 | Route sinds 2024: **BOPA** (regulier; bezwaar). Doorlooptijden aanvraag → besluit: Vettewinkelweg 2 ca. 15 weken, Lierderholthuisweg 3 ca. 11 weken, Zandhuisweg 7 (9 woningen) ca. 3 weken. Bij > 3 woningen buiten de bebouwde kom of > 12 binnen de kom: **bindend raadsadvies** (CVDR704153). Kernuitleg via TAM-omgevingsplanwijziging (IJsseldal, Wengelerhoek). | Gevonden | Gmb (zie §8); CVDR704153 |
| E4 | Prb 2023-2026 doorzocht (69 treffers): geen provinciale zienswijze, aanwijzing of onthouden instemming. Instemmingen zelf worden niet gepubliceerd. Geen geweigerde BOPA voor wonen in Gmb 2024-2026. | Niet gevonden (beperkte negatieve bevinding) | SRU Prb; SRU Gmb |
| F1 | Prb-subsidieplafonds 2025-2026 bevatten geen Olst-Wijhe-specifieke toekenningen (alleen een regionaal deelplafond OV-infra West-Overijssel). | Niet gevonden | Prb 2026, 11093; Prb 2025, 17002 |

Houdbaarheid: B3, C4 en E2 hangen af van Actualisatie 2026 (1-7-2026), de Systeemcode Elektriciteit 2026 en de Lijst BOPA (Prb 2024, 1348).

---

## Niet gevonden (met vindplaats)

| Onderwerp | Waar gezocht | Waar wel te vinden |
|---|---|---|
| Handreiking KGO als beleidsregel | CVDR (alle 458 regelingen), Gmb full-text "KGO"/"kwaliteitsimpuls" | Bestaat alleen als collegedocument (iBabs) |
| Beleid "woningsplitsing en kleinschalige initiatieven" (maxima 5/10) | CVDR, Gmb | wonen.olst-wijhe.nl; B&W-besluit (deelonderzoek 1) |
| Grondprijzenbrief 2026 | Gmb, CVDR | https://www.olst-wijhe.nl/grondprijzenbrief; B&W-besluit |
| Lotingsreglement 2025; intrekking Kaveluitgiftebeleid 2014 | Gmb, CVDR | Gemeentelijke website; B&W 18-11-2025 en 2-12-2025 |
| Nota kostenverhaal | CVDR, Gmb | Bestaat niet apart; kader is de Nota Grondbeleid 2023-2026 |
| Opvolger Nota Grondbeleid (na 2026) | CVDR, Gmb | Raadsplanning/iBabs |
| Huisvestingsverordening (actueel, oud, regionaal) | CVDR (alle versies), CVDR-keyword, Gmb | Niet aanwezig; nieuwe verordening in voorbereiding (team Wonen) |
| Gmb-bekendmaking vastgestelde Omgevingsvisie / vaststellingsdatum | Gmb (titel, type, full-text) | Raadsbesluit iBabs; DSO "Regels op de kaart" |
| Ontwerp Volkshuisvestingsprogramma Olst-Wijhe | Gmb, CVDR | Nog niet gepubliceerd; plan van aanpak B&W 18-8-2026 |
| BOPA-aanvraag Engeweg/Elshof | Gmb (full-text "Engeweg") | Komt na de anterieure overeenkomst; zaakdossier gemeente |
| Provinciale instemmingsbesluiten (Vettewinkelweg 2, Lierderholthuisweg 3) | Prb, Gmb | Zaakdossier gemeente / provincie (niet gepubliceerd) |
| Toekenning subsidie 4.39 aan Olst-Wijhe | Prb | regelen.overijssel.nl / vab@overijssel.nl; B&W-besluiten |
| Woonvisie 2022-2025 in CVDR/Gmb | CVDR, Gmb | Gemeentelijke website (niet als beleidsregel gepubliceerd) |
