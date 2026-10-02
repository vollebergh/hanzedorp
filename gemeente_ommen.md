# Gemeente Ommen — CPO-naslagwerk (provincie Overijssel) — CONCEPT

> **Status: concept (eerste verkenning, lage verificatiegraad).** In de onderzoekssessie was WebFetch voor alle geprobeerde hosts geblokkeerd door de egress-proxy (`EGRESS_BLOCKED`: o.a. ommen.nl, lokaleregelgeving.overheid.nl, officielebekendmakingen.nl, planviewer.nl, ruimtelijkeplannen.nl, woneninommen.nl, overijssel.nl) en het WebSearch-budget (200 zoekopdrachten per deelonderzoek) raakte uitgeput. **Geen enkel brondocument is rechtstreeks geopend of letterlijk gelezen.** Alle Ommen-specifieke bevindingen berusten op titels, URL's en door de zoektool gegenereerde samenvattingen van zoekresultaten. Citaten zijn daarom alleen opgenomen waar ze al in `gemeente_zwolle.md` stonden (second-hand) en dan als zodanig gemarkeerd. Zie de aanbevolen vervolgstappen aan het slot.

## Verantwoording
- **Raadplegingsdatum:** 2026-10-02 (alle bronnen, tenzij anders vermeld).
- **Provincie en gebruikt provinciebestand:** Overijssel, [`provincie_overijssel.md`](provincie_overijssel.md), versie 2026-10-02. Ommen ligt in Overijssel; het Overijsselse regime is leidend voor het omgevingsplan. Dit rapport herhaalt het provinciale kader niet maar verwijst ernaar.
- **Primair model + effort:** Claude Sonnet 5.5 (`claude-sonnet-5-5`); effort-niveau niet expliciet ingesteld/bekend in deze sessie.
- **Deelonderzoeken (Fase 2, subagents 1 t/m 4):** alle vier uitgevoerd met hetzelfde model en effort als het primaire model (Claude Sonnet 5.5, effort niet expliciet ingesteld); één gecombineerde vermelding volstaat. Fase 1 (provinciaal kader) is niet opnieuw uitgevoerd; `provincie_overijssel.md` is hergebruikt.
- **Methode:** vier gelijktijdige deelonderzoeken (1 bestuursinformatie, 2 provinciaal-lokale toepassing, 3 nieuws 2024-2026, 4 juridische/officiële registers), samengevoegd. Dubbele bevindingen zijn gededupliceerd; tegenstrijdigheden zijn expliciet benoemd (kaders "Tegenstrijdig").
- **Betrouwbaarheidslabels in dit rapport:** **[ZOEK]** = samenvatting van een zoekresultaat, bronpagina niet geopend (parafrase, geen citaat); **[ZWOLLE-MD]** = overgenomen uit `gemeente_zwolle.md` (daar op 2026-08-21 geraadpleegd, hier niet opnieuw geverifieerd); **[PROV-MD]** = uit `provincie_overijssel.md`; **[INTERPRETATIE]** = eigen redenering; **[TRAINING]** = trainingskennis, niet live geverifieerd.
- **Waarschuwing verkeerde uitgevende overheid:** zoekresultaten bij Ommen-vragen toonden herhaaldelijk regelgeving van andere gemeenten (CVDR) en van Emmen (Drenthe). Alleen treffers die Ommen expliciet noemen zijn als Ommen-beleid opgenomen. De lijst van **niet aan Ommen toe te schrijven** CVDR-nummers staat in de bijlage "Niet-Ommense treffers".
- **Landelijke context (stand 2026-10-02):** de Wet versterking regie volkshuisvesting is per 1-7-2026 in werking; de ladder voor duurzame verstedelijking vervalt naar verwachting per 1-1-2027 onder voorwaarde van een gemeentelijk volkshuisvestingsprogramma (primair: uiterlijk 1-7-2027) [PROV-MD §5].

### Kernbevindingen in het kort
1. Ommen is een **"overige kern"** (art. 4.4 Omgevingsverordening Overijssel; afgeleid uit [PROV-MD], niet uit een Ommense bron): alleen lokale behoefte en bijzondere doelgroepen, tenzij regionale afspraak.
2. Ommens eigen buitengebiedbeleid voor woningen is **Rood voor Rood (raad 3-6-2021, CVDR658628)** met **woningsplitsing (okt. 2025)**; de ontwerp-actualisatie met VAB-evaluatie lag ter inzage tot 12-11-2025, **vaststelling niet gevonden**. Schaal: 1-2 compensatiewoningen per slooplocatie [ZOEK]. **10-12 woningen passen niet in dit regime.**
3. Ommen heeft een **actieve CPO-praktijk, maar gemeentelijk geregisseerd** op gemeentegrond in of aansluitend aan kernen/buurtschappen: De Meerkoet (6), Beerzerveld Van Alewijkstraat (8 CPO binnen 34 woningen op voormalige landbouwgrond), Erve Arriërflier (8-10), Vinkenbuurt (7+1, met provincie), Lemele (6). Een particulier CPO van 10-12 woningen in het open buitengebied is **niet gevonden**.
4. **Bestuur:** college VOV, CDA en PRO Ommen (11 van 17 zetels) sinds 2-7-2026; **geen coalitie in vorming**; wethouder Wonen/RO: Alice van den Nieuwboer (CDA). De tekst van het coalitieakkoord is niet gelezen.
5. Niet gevonden: volkshuisvestingsprogramma, huisvestingsverordening, kostenverhaalsnota, leges-tarieven, erfpachtbeleid, Ommens KGO-kader, plancapaciteit, provinciale zienswijzen 2023-2026.

---

## 1. CPO-beleid

**Geen afzonderlijke, in CVDR gepubliceerde "Beleidsregels CPO" gevonden** (twee deelonderzoeken; niet bewezen afwezig omdat de CVDR-zoekfunctie zelf niet bereikbaar was). CPO-beleid loopt via het Woonprogramma, de Omgevingsvisie en projectgerichte voorwaarden op https://woneninommen.nl.

### 1.1 Woonprogramma 2021-2025 (CVDR695681/1)
Bron: https://lokaleregelgeving.overheid.nl/CVDR695681/1 (geraadpleegd 2026-10-02 alleen als zoekresultaat). De zoektool gaf als brontekst: "In het buitengebied geven we ruimte aan woningbouw op de plek van bijvoorbeeld vrijkomende agrarische bebouwing (afgekort VAB)." [ZOEK]. De CPO-zinnen zijn second-hand overgenomen uit `gemeente_zwolle.md` §1 [ZWOLLE-MD], niet in deze sessie teruggelezen:

> "In het buitengebied geven we ruimte aan woningbouw op de plek van bijvoorbeeld vrijkomende agrarische bebouwing. Door middel van oprichten van CPO's vanuit de plaatselijke belangen worden vraag en aanbod bij elkaar gebracht. Dergelijke CPO's kunnen rekenen op ondersteuning vanuit de gemeente."

Het programma loopt formeel t/m 2025; een opvolger (volkshuisvestingsprogramma of nieuwe woonvisie) is niet gevonden. De prestatieafspraken 2026 verwijzen nog naar de "Woonvisie Ommen" en het "Addendum Woonvisie Ommen" (woningbouwprogramma).

### 1.2 Gemeentelijk CPO-kader (https://woneninommen.nl/woonbeleid/cpo) [ZOEK]
- Subsidie van **70% van de kosten van een CPO-begeleider, tot maximaal € 20.000**, en een **lening voor een architect in de beginfase**; na selectie volgt een **samenwerkingsovereenkomst**.
- CPO-kavels worden door de **gemeente zelf** uitgegeven (gemeentegrond), met bindingseisen: CPO-groep als notarieel opgerichte vereniging met aantoonbare sociale en/of economische binding met Ommen; leden bouwen voor eigen bewoning (inschrijfprocedures Arriërflier en Vinkenbuurt, PDF's niet geopend).
- Een gemeentelijke CPO-subsidie in een verordening/beleidsregel (CVDR) is niet gevonden; Beleidsregels subsidieverlening Ommen = CVDR679033 (inhoud niet gelezen).

### 1.3 Omgevingsvisie "Ommen Jouw Toekomst"
Unaniem vastgesteld door de raad op **16-12-2021** (IMRO NL.IMRO.0175.omgevingsvisieOV01-VG01; https://www.ommen.nl/bestuur-organisatie/omgevingsvisie/; Gemeenteblad 2022, 415629) [ZOEK]. Parafrase: maximaal 1.250 woningen tot 2040; vraaggestuurde ontwikkeling in kernen en buitengebied; vijf gebiedsprogramma's (centrum, kleine kernen, buitengebied, wonen, werken). Specifieke CPO-passages: niet gevonden. Een actieplan "ontwikkelperspectieven voor een leefbaar buitengebied" is aangekondigd; vaststelling niet gevonden.

**Waar te vinden (lacune):** RIS Ommen (collegebesluiten "verdelingsmethode kavels"), https://woneninommen.nl (verkoopprocedures), afdeling Ruimte/Wonen.

---

## 2. Openheid voor nieuwbouw buiten woonkernen

### 2.1 Gemeentelijke koers
- **Kernen:** het bestemmingsplan Buitengebied is niet van toepassing op Ommen, Lemele, Beerzerveld, Vilsteren en Witharen (behandeld als kernen); Arriën en Vinkenbuurt zijn buurtschappen [ZOEK]. Het kernenoverzicht uit de opdracht klopt niet geheel ("Beerze" = Beerzerveld).
- **Grootschalige uitleg aansluitend aan de kern op agrarisch land wordt doorgezet:** *Vlierlanden fase 3 / Gebied Arriën-Ommen*, circa 375 woningen (30-40-30), op voormalig agrarisch land; bouwclaimovereenkomst gemeente-Bemog 25-2-2025 (varkenshouderij Arriërveldsweg); verhit raadsdebat 17-18-4-2025; Plaatselijk Belang Arriën "luidt de noodklok" (1-10-2026). Bronnen: https://woneninommen.nl/hoofdproject/gebied-arrien-ommen ; https://ommencity.nl/2025/04/18/verhit-debat-over-woningbouwproject-vlierlanden-3/ ; https://www.vechtdalcentraal.nl/2025/02/bemog-en-gemeente-ommen-geven-startsein-voor-ontwikkeling-vlierlanden-iii/ ; https://weblog.oudommen.nl/2026/10/01/plaatselijk-belang-arrien-luidt-noodklok-voor-behoud-eigen-eeuwenoude-buurtschap/ [ZOEK]. Dit is stedelijke uitleg (art. 4.5 lid 1 + redeneerlijn, geen KGO), geen buitengebiedbeleid [INTERPRETATIE].
- **Beerzerveld Van Alewijkstraat:** de raad stelde een wijzigingsbesluit omgevingsplan vast voor 34 woningen op landbouwgrond aan de rand van de kern; onherroepelijk (https://www.ommen.nl/actueel/gemeenteraad-stemt-in-met-wijziging-omgevingsplan-voor-woningbouw-beerzerveld/ ; https://www.ommen.nl/actueel/omgevingsplan-beerzerveld-onherroepelijk-woningbouw-kan-starten/) [ZOEK]. Datum raadsbesluit niet vastgesteld. Route: omgevingsplanwijziging, geen BOPA.
- **Buitengebied:** volgens een zoeksamenvatting "in wezen gesloten" voor nieuwe woningbouw; woningen komen er via VAB/Rood voor Rood, woningsplitsing en bestaande volgfuncties [ZOEK; document dat dit letterlijk zegt niet vastgesteld, mogelijk verouderd]. Een oudere zinsnede dat het beleid "geen mogelijkheden voor permanente bewoning buiten de kernen" biedt is van onbekende herkomst en strookt niet met het latere Rood-voor-Rood-/splitsingsbeleid: als verouderd behandeld.

### 2.2 Ladder en volkshuisvestingsprogramma
- **Eigen (ontwerp-)volkshuisvestingsprogramma: niet gevonden** (drie deelonderzoeken). De prestatieafspraken 2026 verwijzen naar Woonvisie + Addendum. Het provinciale programma (Prb 2026 nr. 11834) verscheen als zoekresultaat (niet geopend).
- Of Ommen de ladder nog toepast of zich op afschaffing voorbereidt: **niet gevonden**. Waar: ruimtelijke onderbouwingen/ladderparagrafen omgevingsplanwijzigingen 2025-2026 (o.a. NL.IMRO.0175.2024TAMOP0002), RIS Ommen (raadsvoorstel volkshuisvestingsprogramma; verwacht najaar 2026 [INTERPRETATIE]).
- **Provinciaal blijft gelden:** art. 4.4-4.5 (concentratie), redeneerlijn art. 4.122, woonafspraken art. 4.14-4.15 [PROV-MD].

### 2.3 Positie in het provinciale kader (Bijlage A1/A2)
Ommen is "overige kern" [PROV-MD §1.3]; woonregio West-Overijssel (Woondeal 2025-2030, 20-3-2025): netto gerealiseerd Q1 2022 - Q4 2024: **290**; sleutelprojecten 2024-2030: **2 projecten / 508 woningen**; doorkijk 2031-2035: geen [PROV-MD §1.5]. Ommen heeft **geen post "kleine kernen"** in de Woondeal. Geen grensoverschrijdende regio; Regio Zwolle is een breder samenwerkingsverband (Regio Deal-middelen voor "Ruimte voor de Vecht"). Werkgebied corporatie: Vechtdal Wonen.

> **Tegenstrijdig (opgave):** Woonprogramma 2021-2025: **650 woningen t/m 2030** (375 lokaal + 275 regionaal; grootste deel in kern Ommen; **buitengebied maximaal circa 75**) [ZOEK] versus prestatieafspraken/projectsites: **1.250 woningen voor de kern Ommen** (Vechtdal Wonen 485 huurwoningen = 39%) en Omgevingsvisie: maximaal 1.250 woningen tot 2040. Mogelijke verklaring (niet geverifieerd): Addendum Woonvisie heeft de opgave verhoogd en de periodes verschillen. Ook de identiteit van de twee Woondeal-sleutelprojecten (Vlierlanden fase 3 / Arriën-Ommen / een binnenstedelijk gebied) is niet eenduidig; Woondeal-bijlage 1 raadplegen.

---

## 3. Openheid voor agrarische herbestemming (10-12 woningen)

### 3.1 Wettelijk/procedureel kader
- **Omgevingsplan Ommen:** CVDR696206; alleen het tijdelijk deel (per 1-1-2024; Gemeenteblad 2024-117665); versie 2 per 23-1-2026; verdere wijzigingsbesluiten 2026 (gmb-2026-132501, 310721, 316656, 325338, 781) waarvan inhoud niet vastgesteld is, dus laatste geldende versie onbekend. Omzetting naar het eigen omgevingsplan: kleine kernen/wonen 2024-2026, **buitengebied als laatste (2025-2028)** [ZOEK, Beleidsplan VTH 2025-2028, CVDR740793]. Voor het buitengebied geldt dus nog het bestemmingsplan Buitengebied (2012-2013 voorloper met 5 thematische plannen; regels https://www.ommen.nl/wp-content/uploads/2022/10/Regels.pdf, niet gelezen) met een regeling voor vrijkomende agrarische bedrijven met volgfuncties [ZOEK].
- **Route in de praktijk:** Ommen gebruikt voor woningbouw bij kernen een **wijziging van het omgevingsplan** (Beerzerveld, Arriërflier, Vinkenbuurt); een Ommense BOPA-beleidsregel en BOPA's voor woningbouw in het buitengebied 2023-2026 zijn **niet gevonden** (uitgezonderd twee aanvragen: Migaweg 9-9a, Rood voor Rood, 2 woningen/1.200 m³ bij ca. 3.400 m² sloop, 2023; en Dalmsholterweg 30, Dalmsholte, afhandeling onbekend). Een BOPA met nieuwe woningen in de Groene Omgeving valt onder de Lijst BOPA (provinciaal advies én instemming) [PROV-MD §4.3].
- **Raadsrol/participatie:** Participatiekader gemeente Ommen (CVDR717595, in werking 27-3-2024); een Zwolse variant met drempel voor woningen in het buitengebied is niet gevonden.
- **Provinciaal toetsingskader:** concentratiebeginsel (art. 4.4), art. 4.5 lid 2 (eerst bestaande bebouwing benutten), KGO (art. 4.11), landbouwgebied-typologie (art. 4.123-4.124), woonafspraken (art. 4.14-4.15), redeneerlijn (art. 4.122), water/bodem (art. 4.13). Een provinciebrede KGO-rekenformule bestaat niet; zie §3.2.

### 3.2 Rood voor Rood (Beleidsregels Rood voor Rood gemeente Ommen)
- **Geldend:** raad **3-6-2021**, vervangt notitie 2011; CVDR658628; Gemeenteblad 2021, 180221; evaluatie na twee jaar voorgeschreven. Inwerkingtreding niet gevonden. Bronnen: https://lokaleregelgeving.overheid.nl/CVDR658628/1 ; https://zoek.officielebekendmakingen.nl/gmb-2021-180221.pdf [ZOEK].
- **Kerninhoud (parafrase uit zoeksamenvattingen):** slooplocatie = voormalige agrarische bedrijfsbebouwing; alle voormalige agrarische bedrijfsbebouwing en overige opstallen (silo's, mestkelders, kuilvloeren, verharding) moeten verdwijnen; **minimaal 850 m² sloop voor 1 compensatiewoning (max. 750 m³, max. 150 m² bijgebouwen), minimaal 2.000 m² voor 2 compensatiewoningen**; bij onvoldoende sloop ter plaatse mogen sloopmeters elders in het Ommense buitengebied worden ingebracht, met minimaal 500 m² per woning; monumentale/karakteristieke bebouwing blijft behouden. Formule = sloopstaffel, **geen waardestijgingspercentage** (Bijlage A B1).
- **Schaal:** maximaal 2 compensatiewoningen per slooplocatie; buitengebied-streefcijfer circa 75 woningen (Woonprogramma). Evaluatie 2021-aug. 2025: 34 principeverzoeken, **11 gerealiseerde woningen** [ZOEK].
- **Actualisatie:** het college legde de ontwerp-geactualiseerde regels met rapport "Evaluatie en actualisatie VAB-beleid Ommen" ter inzage van **1-10 t/m 12-11-2025** (https://www.ommen.nl/actueel/ontwerp-geactualiseerde-beleidsregels-rood-voor-rood/ ; https://openpub.ommen.nl/wp-content/uploads/2025/09/1.-Ontwerp-rapport-Evaluatie-en-Actualisatie-VAB-beleid-gemeente-Ommen.pdf ; https://www.detoren.net/nieuws/ommen/104690/gemeente-ommen-stelt-geactualiseerde-rood-voor-rood-beleidsre). Strekking (parafrase): meer flexibiliteit (meerdere kleinere woningen, meer woningtypen i.p.v. één woning van 750 m³), vastlegging in het omgevingsplan. **Definitieve vaststelling niet gevonden** (verkiezingen maart 2026 en collegewissel kunnen vertraging verklaren [INTERPRETATIE]). Het ontwerp dateert van vóór Actualisatie 2026 van de Omgevingsverordening (1-7-2026): aanpassing aan landbouwgebied-typologie niet gevonden.
- **Eigen KGO-kader:** niet gevonden. Rood-voor-Rood-voorwaarden zijn volgens een samenvatting deels ontleend aan het provinciale KGO-kader. KGO-/Rood-voor-Rood-CVDR's van andere gemeenten (o.a. CVDR305226/305339 Dinkelland/Tubbergen; CVDR743755 vermoedelijk Almelo) zijn niet aan Ommen toegeschreven; zie bijlage "Niet-Ommense treffers".
- **Woningsplitsing:** Beleidsnotitie woningsplitsing, okt. 2025 (CVDR745908/1; https://www.ommen.nl/woningsplitsing/): in het buitengebied onder voorwaarden (o.a. gesplitste woning min. 200 m³); alleen extra woningen in bestaande bouwmassa [ZOEK].
- **Onbevestigde kandidaat:** CVDR745896 "Beleidsregels voor woningbouw in het buitengebied": uitgevende overheid niet geverifieerd (nummer ligt vlak bij CVDR745908); **eerste punt voor controle bij herhaling**.

### 3.3 Gemeentelijke houding
Positief voor kleine, lokaal ingebedde initiatieven: Woonprogramma (VAB-locaties, CPO's vanuit plaatselijk belang), gemeentelijke CPO-ondersteuning, VOV-programma 2026 steunt CPO, tiny houses en woningsplitsing en wil "25 extra starterswoningen per kern binnen 12 maanden" [ZOEK]. Terughoudend/gevoelig voor verdichting van buurtschappen en landschap (Arriën-debat, CDA en VOV tonen begrip voor bewoners). Geen signaal gevonden voor open-buitengebied-clusters.

### 3.4 Concreet stappenplan (indicatief; geen Ommense bevestigde doorlooptijden)
Provinciale stappen volgens [PROV-MD §4]; gemeentelijke praktijk aangevuld:
1. **Informeel voorgesprek** met de gemeente (team Ruimtelijke Ordening/Wonen; wethouder A. van den Nieuwboer) en Plaatselijk Belang van de betreffende kern; Ommen kent een principeverzoekformulier. Het Beleidsplan VTH 2025-2028 (CVDR740793) noemt dat de gemeente "indien nodig" de regionale Omgevingstafel gebruikt en bij complexe initiatieven overleg voert met ketenpartners waaronder de provincie [ZOEK]; of een principeverzoek standaard vóór het gemeentelijk besluit aan de provincie wordt voorgelegd: **niet gevonden**.
2. **Voorkantsamenwerking provincie** (accounthouder Ruimte; Omgevingstafel IJsselland: tweewekelijks, geïntegreerd advies vóór besluit): indicatief 1-3 maanden [INTERPRETATIE]. Naam accounthouder niet openbaar; Overijssel Loket 038 499 88 99.
3. **Omgevingsplanwijziging of BOPA:** regulier 8 weken, uitgebreid 26 weken; bij BOPA op de Lijst BOPA provinciaal advies (4-6 weken) en instemming (4 weken) [PROV-MD §4.5]; waterschap, Natura 2000/stikstofberekening, waterwinning waar relevant.
4. **Bezwaar/beroep:** Afdeling bestuursrechtspraak Raad van State.
Een Ommen-specifiek stappenplan is niet gevonden.

### 3.5 Kansrijk versus kansarm [INTERPRETATIE]
- **Kansrijker:** bestaand erf met sloop van voormalige agrarische bedrijfsbebouwing (1-2 woningen); karakteristieke boerderij met woningsplitsing; initiatief met lokale binding en steun van plaatselijk belang; locatie in/aansluitend aan een kern of buurtschap met starters-/ouderenaanbod; beperkt programma dat "in het landschap past" (Vinkenbuurt, ontwerp samen met de provincie: de provincie was volgens een zoeksamenvatting "niet gemakkelijk" over woningen in het buitengebied maar had begrip voor jongeren die in de buurtschap willen blijven wonen) [ZOEK].
- **Kansarm:** nieuwe woningen op onbebouwde agrarische grond in open buitengebied; cluster van 10-12 woningen op een erf buiten een kern; gevoelige cultuurhistorische buurtschappen (Arriën); locaties in/nabij Natura 2000, NNN en waterwinning (zie §3.7).

### 3.6 Eindoordeel per schaalscenario [INTERPRETATIE; onzeker door beperkte bronnentoegang]
| Scenario | Inschatting |
|---|---|
| 1-2 woningen op bestaand erf (Rood voor Rood/VAB) | Kansrijk; bestaande regeling |
| 3-6 woningen op bestaand erf (VAB) | Mogelijk, maatwerk; afhankelijk van uitkomst actualisatie 2025-2026 (maximum niet gevonden) en provinciale instemming bij BOPA |
| 10-12 woningen op bestaand erf (cluster) | Kansarm tot onzeker: buiten de rood-voor-rood-schaal; alleen via maatwerk/ruimtelijk kwaliteitsplan en regionale afspraak |
| 10-12 woningen op onbebouwde agrarische grond buiten de kern | Zeer kansarm (art. 4.4, 4.5 lid 2, KGO, nee-tenzij-sturing via voorkant/instemming) |
| 10-12 woningen aansluitend aan een kern (uitleg) op gemeentegrond of met gemeentelijke regie | Het kansrijkst: gangbare Ommense praktijk (Arriërflier 8-10, Beerzerveld 8 CPO, Vinkenbuurt 7); vraagt wel programmering binnen de Woondeal, lokale binding en minimaal 30% sociale huur-component (zie §8, §12) |

**Vervolgstap:** informeel gesprek met de gemeente Ommen (gemeente@ommen.nl; portefeuillehouder A. van den Nieuwboer; platform https://woneninommen.nl); bij een buitengebiedlocatie parallel voorkantsamenwerking met de provincie (Overijssel Loket 038 499 88 99, overijsselloket@overijssel.nl; VAB: vab@overijssel.nl).

### 3.7 Provinciale overlays in het Ommense buitengebied (Bijlage A C1-C3) [ZOEK/TRAINING]
| Overlay | Bevinding |
|---|---|
| Natura 2000 | **Vecht- en Beneden-Reggegebied** (ca. 4.122 ha; Hardenberg, Ommen, Twenterand; Dalfsen wel/niet genoemd, tegenstrijdig) met stikstofoverbelasting (PAS-gebiedsanalyse 2017, verouderd). Sallandse Heuvelrug niet in Ommen aangetoond. |
| NNN / zone ONW | Vechtdal is NNN-gebied (deels Natura 2000); winterbedherzieningen Karshoek-Stegeren i.v.m. Ruimte voor de Vecht. |
| Stikstof/GGA | Gebiedsgerichte Aanpak Stikstof, regio Vechtdal (Ommen, Dalfsen, Hardenberg). Stikstofgerelateerd nieuws specifiek voor Ommen woningbouw: niet gevonden; stikstofberekening bouwfase waarschijnlijk nodig [INTERPRETATIE]. |
| Grondwater | Winning Hammerflier (Vitens; Beerze/Archemerberg) en beschermingsgebied Witharen. |
| Landbouwgebied-typologie (art. 4.123) | **Niet vastgesteld** (kaartlaag niet raadpleegbaar). Rond Vecht/Natura 2000/beekdalen/waterwinning waarschijnlijk "gebiedsspecifiek", elders mogelijk "generiek" [INTERPRETATIE]. |
| Nationaal Landschap | Niet gevonden dat Ommen erin ligt (IJsseldelta niet; [TRAINING]). |
| Cultuurhistorie | Beschermd dorpsgezicht Beerze; Stegerveld; nieuwe landgoederen Witharen. |
| Vakantieparken | Afwegingskader Vitalisering en transformatie vakantieparken (CVDR681336/1): vitalisering primair; geen route voor nieuw cluster op agrarische grond. |
Catalogus Gebiedskenmerken, raatakkers/karrensporen: niet onderzocht.

---

## 4. VAB-beleid

- Ommen heeft **expliciet VAB-beleid**, gekoppeld aan Rood voor Rood en de volgfuncties in het bestemmingsplan Buitengebied (tijdelijk deel). Geen zelfstandige VAB-beleidsregel in CVDR gevonden. Evaluatie/actualisatie: zie §3.2.
- **Maximum aantal woningen per VAB-erf:** niet gevonden. Treffers met "maximaal 5 woningen per locatie/3-km-regel" betreffen andere gemeenten en zijn niet gebruikt.
- Voorwaarden "3 jaar eerder gebouwd en agrarisch gebruikt" uit een eerste zoeksamenvatting zijn voor Ommen onzeker.
- **Intergemeentelijk VAB-/erftransformatieprogramma, subsidie 4.39 (D1):** de provinciale site noemt dat gebiedsprocessen in het Vechtdal (deels) in Ommen liggen (https://toekomstvooronsplatteland.nl/investeren/vab-vrijkomende-agrarische-bebouwing-en-erftransformatie); deelname van Ommen aan 4.39 niet gevonden.
- **Erfcoach (D2):** de inzage-publicatie noemt de inzet van erfcoaches. > **Tegenstrijdig:** digitaleerfcoach.nl noemt Hendry van Ittersum (Hardenberg, Ommen, Staphorst) en Yvonne In 't Veld, een andere pagina een organisatie voor o.a. Hellendoorn en Ommen, terwijl [PROV-MD] Ommen niet in de lijst heeft; actuele dekking verifiëren via https://erfcoachoverijssel.nl/contact-met-de-erfcoaches.
- **Collectieve VAB-precedenten (D3):** niet gevonden. VAB als aparte opgave in de woonprogrammering: Woonprogramma noemt VAB-locaties als bouwlocatie (max. circa 75 in buitengebied); aparte kwantitatieve opgave niet gevonden.

---

## 5. Grondbeleid

- **Nota Grondbeleid:** de vigerende nota dateert volgens nieuwsberichten van **2018** met overwegend **faciliterend** grondbeleid (CVDR-nummer niet gevonden). De raad nam op **27-11-2025** unaniem een motie aan (Lokale Partij Ommen) om de nota te actualiseren; de nieuwe raad stelt die **uiterlijk november 2027** vast (https://www.vechtdalcentraal.nl/2025/11/gemeenteraad-ommen-unaniem-voor-actualisatie-nota-grondbeleid/ ; https://www.detoren.net/nieuws/ommen/106244/raad-unaniem-voor-actualisatie-nota-grondbeleid). Financiële verordening 2025 (CVDR755720) schrijft een nota minstens eens per vier jaar voor (via samenvatting CVDR732998) [ZOEK].
  > **Tegenstrijdig:** een zoeksamenvatting meldt "momenteel geen actieve gemeentelijke grondexploitaties", terwijl de gemeente zelf kavels uitgeeft (Haven Oost, Vlierlanden 2, Beerzerveld, Arriërflier: raad gaf 27-2-2025 toestemming voor de grondexploitatie) en een bouwclaim sloot (Vlierlanden 3). Mogelijke uitleg: de uitspraak had betrekking op een categorie; niet opgelost.
- **Grondposities buitengebied:** via bouwclaimovereenkomst (25-2-2025) Vlierlanden 3; voorkeursrecht (Wvg) niet gevonden.
- **Grondprijzen:** jaarlijkse Grondprijzenbrief door het college; Grondprijzenbrieven 2026 in CVDR (o.a. CVDR752764, 755587, 761668, 761701) zijn niet aan Ommen toe te schrijven. Kavelprijzen woningbouw: niet gevonden (behalve losse kavel Beerzerveld, Schuurmanstraat 26b: 702 m², € 164.970, onder optie, juni 2026). Spelregels verkoop gemeentelijk vastgoed 1.0 (CVDR678509): marktprijs via taxatie of biedingen [ZOEK, M].
- **Erfpacht:** geen Ommens beleid gevonden (CVDR636460 is Meierijstad).

### 5.1 Actueel kavelaanbod (niet op actualiteit gecontroleerd)
| Locatie | Aanbod | Opmerking |
|---|---|---|
| Haven Oost (Ommen) | 5 vrije kavels | inschrijving via woneninommen.nl; prijs niet vermeld |
| Beerzerveld Van Alewijkstraat | 6 vrije kavels (2 vrijstaand, 4 twee-onder-een-kap) + 8 CPO | bouwrijp naar verwachting dec. 2026 |
| Vlierlanden fase 2 | 90 kavels | alle onder optie of verkocht |
| Lemele | zelfbouw voor starters | aanduiding uit 2022 |
**Er is geen direct beschikbare CPO-kavel van 10-12 woningen.**

### 5.2 Grote ontwikkellocaties met gemeentelijke positie
| Locatie | Omvang | Status | CPO/collectief |
|---|---|---|---|
| Vlierlanden 3 / Arriën-Ommen | ca. 375 | planvorming, sleutelproject Woondeal; bouwstart onzeker | nog niet; "innovatie woonvormen" besproken |
| Erve Arriërflier | ca. 60 | omgevingsplan "medio 2026" (eerder Q1 2026; memo aangepast ontwerp april 2026) | 8-10 CPO-kavels |
| Haven Oost | ca. 110 | in aanbouw | 5 vrije kavels |
| Guido de Brès / Julianaschool | 56 / 26 | omgevingsplan in procedure | n.v.t. |
| Van Alewijkstraat (Beerzerveld) | 34 | onherroepelijk; bouw eind 2026 | 8 CPO |
| Tijdelijk Sportlaan | 50 flexwoningen | "wederom vertraagd" | n.v.t. |

### 5.3 Plancapaciteit en tempo
Netto 290 woningen Q1 2022 - Q4 2024 [PROV-MD]; cijfer 2025 per gemeente niet gevonden. **Harde/zachte plancapaciteit, 80/20-ruimte en Planmonitor-status van een CPO: niet gevonden** (een zoeksamenvatting "290 hard / 19.743 zacht voor Ommen" is aantoonbaar onjuist: 290 = gerealiseerd, 19.743 = zachte capaciteit regio West-Overijssel; verworpen). Waar: Planmonitor/Dashboard Wonen Overijssel, https://overijsselsewoonaanpak.nl/speerpunten/realisatie-woningbouw, Woondeal-bijlage 1.

---

## 6. Praktijkvoorbeelden (2024-2026)
| # | Voorbeeld | Datum | Bron | Relevantie |
|---|---|---|---|---|
| 1 | **CPO De Meerkoet:** 6 woningen (4+2) gemeentegrond Ommen-kern; koopovereenkomst 11-12-2024; omgevingsvergunning aangevraagd sept. 2025; bouwstart juli 2026 | okt. 2024 - jul. 2026 | https://www.rondommen.nl/nieuws/22029/starterswoningen-de-meerkoet-via-cpo.html ; https://www.bijkeradvies.nl/nieuws/laatste-nieuws-bouw-de-meerkoet-in-ommen-is-gestart-juli-2026/ | CPO-route werkt (ca. 20 maanden oproep tot bouw); stedelijk, kleiner dan 10-12 |
| 2 | **Erve Arriërflier:** raad 27-2-2025 grondexploitatie; aanbesteding 10 CPO-starterswoningen; samenwerkingsovereenkomst 4 maart (2026) | 2025-2026 | https://www.detoren.net/nieuws/ommen/106131/ommen-start-aanbesteding-voor-tien-cpo-starterswoningen-in-er ; https://www.ommen.nl/actueel/cpo-verenigingen-erve-arrierflier-en-vinkenbuurt-zetten-volgende-stap-samenwerkingsovereenkomsten-ondertekend/ | Schaal 8-10, gemeentegrond, kernrand |
| 3 | **CPO Vinkenbuurt:** 7 CPO + 1 vrije kavel, voormalig schoolterrein in buurtschap; raad 30-1-2025 middelen; ontwerp met provincie; inschrijving t/m 18-2-2026 | 2025-2026 | https://woneninommen.nl/hoofdproject/vinkenbuurt ; https://www.detoren.net/nieuws/hardenberg/108726/samen-bouwen-in-vinkenbuurt | **Meest relevant buitengebied-precedent** (buurtschap, provincie aan de voorkant), maar geen agrarische grond en 7-8 woningen |
| 4 | **Beerzerveld Van Alewijkstraat:** omgevingsplanwijziging 34 woningen op landbouwgrond; 8 CPO; overeenkomst 20 woningen Vechtdal Wonen/Le Clercq 11-2-2026 | 2025-2026 | https://www.ommen.nl/actueel/omgevingsplan-beerzerveld-onherroepelijk-woningbouw-kan-starten/ ; https://www.vechtdalcentraal.nl/2026/02/overeenkomst-voor-20-woningen-in-beerzerveld-ondertekend/ | **Sterkste precedent** voor omzetting agrarische grond aan kleine kern; gemeentelijk project met sociale huur en ontwikkelaar |
| 5 | Lemele: hofje van 6 seniorenwoningen (CPO, eerder 4 kavels) | 2022-2023 | https://ommenaar.nl/nieuws/lemele-krijgt-hofje-met-zes-seniorenwoningen-aan-bulemansteeg/ | Ouder dan 2024; kleine kern |
| 6 | Verhit debat en bouwclaim Vlierlanden 3 | feb.-apr. 2025 | zie §2.1 | Politieke gevoeligheid uitleg op agrarisch land |
| 7 | Ontwerp Rood-voor-Rood/VAB-evaluatie ter inzage | 1-10 t/m 12-11-2025 | zie §3.2 | Beleidsruimte buitengebied wordt herzien |
| 8 | Beleidsnotitie woningsplitsing | okt. 2025 | https://www.ommen.nl/woningsplitsing/ | Extra woningen in bestaande bouw |
| 9 | Plaatselijk Belang Arriën "luidt noodklok" | 1-10-2026 | zie §2.1 | Lokale weerstand tegen verdichting |
| 10 | Prestatieafspraken 2026 gemeente/Vechtdal Wonen/huurders | dec. 2025 | https://www.ommen.nl/actueel/gemeente-ommen-en-vechtdal-wonen-maken-voor-2026-afspraken-over-wonen-en-leefbaarheid/ | Projectenlijst; 30% sociale huur |
| 11 | Raad motie actualisatie Nota Grondbeleid | 27-11-2025 | zie §5 | Ruimte voor diverse woonvormen en versnelling |

---

## 7. Inventarisatie bestaande initiatieven
| Initiatief | Woningen | Status | Relevantie |
|---|---|---|---|
| CPO De Meerkoet (Starters Collectief Ommen) | 6 | bouwstart juli 2026 | Bewezen route, stedelijk |
| CPO Starters Collectief Ommen - Erve Arriërflier | 10 (nieuws) of 8 (inschrijfflyer) | samenwerkingsovereenkomst; omgevingsplan medio 2026 | Zelfde orde als ons concept; gemeentegrond |
| Vereniging CPO Vinkenbuurt | 7 (+1 vrij; plan 8-10) | selectie 2026; omgevingsplan nog te doorlopen | Buurtschap; provincie betrokken |
| CPO Beerzerveld (in Van Alewijkstraat) | 8 (7-8 leden) | onherroepelijk; bouwstart eind 2026 | Agrarische grond aan kernrand |
| Lemele hofwoningen / CPO LemeleWoont | 6 | gerealiseerd/aangekondigd 2022-2023 | Kleine kern |
| Seniorenhofje + jongeren (4 jongeren + 11 senioren, gedeelde binnenplaats) | 15 | locatie niet vastgesteld | Collectief-achtig |
**Buitengebied-CPO van 10-12 woningen door particulieren: geen gevonden.**
> **Tegenstrijdig (aantallen):** Arriërflier 10 versus 8; Vinkenbuurt 7+1 versus 8-10; Meerkoet "5 tot 7" versus 6; Beerzerveld 20, 34 en 8 woningen zijn kennelijk verschillende fasen/onderdelen (niet vastgesteld). "Starters Collectief Ommen" is de naam bij zowel Meerkoet als Arriërflier; of het dezelfde vereniging is, is niet vastgesteld.

---

## 8. Huisvestingsverordening
- **Aanwezig: niet gevonden** (drie deelonderzoeken; niet bewezen afwezig). CVDR753410 en CVDR741632 zijn niet aan Ommen toe te schrijven. Er bestaat een urgentieregeling (via derdenpagina https://www.mijnurgentie.nl/urgentie-aanvragen-ommen/; inhoud onbekend). Waar: CVDR (filter Ommen, "huisvesting/urgentie"), Vechtdal Wonen. Landelijk: verordening termijn 1-1-2028 [PROV-MD §5].
- **Sociale huur:** geen verordeningspercentage. Prestatieafspraken: minimaal gemiddeld **30% sociale huur** in nieuwe plannen conform de Woondeal; een zoeksamenvatting meldt dat dit als minimumeis voor **alle particuliere woningbouwinitiatieven** geldt (bron-tekst niet gecontroleerd; voor een CPO van 10-12 woningen = 3-4 sociale huurwoningen of alternatieve invulling: **hoogst relevant, eerst verifiëren**). Ambitie 36% sociale nieuwbouw op gemeentegrond (311 woningen). Aandeel sociale huur in Ommen 18% (Overijssel 27%).
  > **Tegenstrijdig:** Woonprogramma 2021-2025 noemde een streefpercentage van 15% sociale huur (en 1.360 sociale huurwoningen = 19% van de voorraad) versus 30% in latere afspraken; de nieuwere afspraken prevaleren.
- Bronnen: https://www.vechtdalwonen.nl/media/1719/prestatieafspraken-ommen-2025.pdf ; https://www.ommen.nl/actueel/gemeente-ommen-en-vechtdal-wonen-maken-voor-2025-afspraken-over-huurwoningen/

---

## 9. Zelfbouwloket / contactpersoon
- **Wonen in Ommen** (https://woneninommen.nl) is het gemeentelijke platform voor projecten, kavels (zelfbouw/CPO), verkoopprocedures en nieuws. Een zoeksamenvatting meldt een "betaald account" als voorwaarde voor kavelinschrijving: niet geverifieerd.
- CPO-aanmelding Beerzerveld: motivatiebrief (max. 4 pagina's) aan **gemeente@ommen.nl** met vermelding "CPO Beerzerveld".
- Een benoemde contactpersoon (naam/e-mail/telefoon) voor zelfbouw/CPO is **niet gevonden**. Waar: https://woneninommen.nl (contact), team Ruimte/Wonen, wethouder. Algemeen nummer gemeente 14 0529 [TRAINING].
- Provinciaal: Overijssel Loket 038 499 88 99, overijsselloket@overijssel.nl; VAB: vab@overijssel.nl [PROV-MD].

---

## 10. Bestuurlijk klimaat

### 10.1 Verkiezingen 18-3-2026
Definitieve uitslag (centraal stembureau 26-3-2026; opkomst 65,4%): **VOV 5**, **CDA 4**, **Lokale Partij Ommen 2**, **ChristenUnie 2**, **GroenLinks/PvdA 2**, **VVD 1**, **D66 1** (17 zetels). Bronnen: https://www.ommen.nl/actueel/definitieve-uitslag-gemeenteraadsverkiezingen-2026/ ; https://www.vechtdalcentraal.nl/2026/03/vov-grote-winnaar-van-gemeenteraadsverkiezingen-in-ommen/ [ZOEK]. (Opkomst 65,42% of 65,45% in twee bronnen.)

### 10.2 Coalitie en college
- **Coalitieakkoord "Krachtige keuzes voor een verbonden samenleving" (2026-2030)** van **VOV, CDA en PRO Ommen**; verkenner Frank de Grave (raadsvergadering 7-4-2026); akkoord op hoofdlijnen rond 2-6-2026; wethouders geïnstalleerd **2-7-2026**. Bronnen: https://www.ommen.nl/actueel/vov-cda-en-pro-ommen-sluiten-coalitieakkoord/ ; https://www.vechtdalcentraal.nl/2026/06/vov-cda-en-pro-ommen-sluiten-coalitieakkoord-krachtige-keuzes-voor-een-verbonden-samenleving/ ; https://www.vechtdalcentraal.nl/2026/07/nieuwe-college-aan-de-slag-voor-de-gemeente-ommen/ [ZOEK].
- **Wethouders:** René de Koff (VOV), **Alice van den Nieuwboer (CDA)**, Sonja Rasenberg (PRO Ommen). **Wethouder Wonen:** Alice van den Nieuwboer; portefeuille o.a. Ruimtelijke ordening (incl. omgevingsplannen), Wonen en huisvesting (https://www.ommen.nl/medewerker/a-alice-van-den-nieuwboer/) [ZOEK]. Dezelfde wethouder had Wonen ook in 2022-2026. Portefeuilles De Koff en Rasenberg, en wie "ontwikkelperspectieven landelijk gebied" nu heeft: niet gevonden.
- **Politieke samenstelling college:** VOV, CDA, PRO Ommen = 11 van 17 zetels. > **Open/tegenstrijdig (identiteit "PRO Ommen"):** de uitslag kent geen "PRO Ommen". Eén zoeksamenvatting stelt dat de Lokale Partij Ommen is hernoemd; aannemelijker is dat PRO Ommen de lokale GL-PvdA-fractie is (landelijke hernoeming GroenLinks-PvdA naar PRO) [INTERPRETATIE]. Beide leiden tot 5+4+2=11 zetels, maar de duiding verschilt (LPO, drijvende kracht achter de motie grondbeleid, vermoedelijk in de oppositie).
- **Coalitie in vorming op peildatum: nee.** Geen val of fractiebreuk gevonden sinds juli 2026. Alleen een nieuwe burgemeester is in procedure: Hans Vroomen trad af per 10-4-2026; waarnemend burgemeester Annemiek Jetten; aanbeveling door de raad in oktober 2026 (> **tegenstrijdig:** 8 oktober versus artikel van 26 september 2026), benoeming verwacht Q1 2027. Raakt CPO nauwelijks.

### 10.3 Inhoud coalitieakkoord en programma's
- **De tekst van het akkoord is niet gelezen.** Parafrase: leefbaarheid in dorpen, buurtschappen en wijken, ruimte voor inwonersinitiatief, aandacht voor wonen en buitengebied; uitwerking in het uitvoeringsprogramma [ZOEK]. CPO, zelfbouw en agrarische herbestemming zijn niet te bevestigen of uit te sluiten. Waar: bijlage raadsvoorstel 2-7-2026 op ommen.nl/RIS; https://www.ommen.nl/bestuur-organisatie/bestuursakkoord/.
- **VOV-verkiezingsprogramma 2026 (parafrase):** betaalbaar wonen met voorrang voor inwoners, uitbreiding in kernen én buitengebied, gemeente neemt regie, steun voor CPO/tiny houses/woningsplitsing, 25 starterswoningen per kern binnen 12 maanden, enkele locaties in het buitengebied als toekomstige uitbreiding geschikt voor flexwonen (https://www.vov-ommen.nl/index.php/verkiezingen-2026/). VVD- en ChristenUnie-programma's niet gelezen; CDA-programma niet gevonden.
- **Vorig akkoord 2022-2026** (LPO, CDA, ChristenUnie, "Bouwen aan de toekomst"): ouderen/starters, zorgwoningen, flexwonen [ZOEK; niet gelezen].
- **Indicatie ruimte voor CPO [INTERPRETATIE]:** gunstig voor CPO in en bij kernen (grootste partij schrijft CPO in het programma; wethouder Wonen steunt de projecten publiek); geen signaal voor clusters in het open buitengebied; gevoeligheid voor landschap en buurtschappen.

---

## 11. Kostenverhaal en leges
- **Legesverordening 2026:** "Verordening op de heffing en de invordering van leges Ommen 2026", **CVDR753504**, raad 18-12-2025, in werking 1-1-2026; rechtsgrond o.a. art. 13.1a Omgevingswet (https://lokaleregelgeving.overheid.nl/CVDR753504?show-wti=true; Gemeenteblad 2025-567439). **Tarieven niet gevonden** (tarieventabel niet gelezen). Bedragen uit zoekresultaten betroffen andere gemeenten en zijn bewust niet overgenomen.
- **Kostenverhaal/anterieure overeenkomst:** Ommense nota niet gevonden (CVDR725235, 735924, 740547, 764145 niet aan Ommen toe te schrijven). Aanwijzingen: bouwclaimovereenkomst Vlierlanden 3; bij CPO op gemeentegrond is kostenverhaal verwerkt in de kavelprijs [INTERPRETATIE]; Rood voor Rood als compensatievorm. Een zoeksamenvatting over "beleidsregel 9: in beginsel anterieure overeenkomst" is niet tot een Ommense bron herleid en niet als bevinding gerekend.
- **Waar:** tarieventabel bij CVDR753504; omgevingsplan (kostenverhaalsregels, afd. 13.6 Omgevingswet); afdeling Ruimte/Grondzaken.

---

## 12. Woningbehoefte en doelgroepen
- **Woonprogramma 2021-2025 (parafrase):** 650 woningen t/m 2030; aandacht voor starters, senioren, kleinere woningen, woningsplitsing en nieuwe bouwconcepten. Recent woningbehoefteonderzoek 2025-2026: niet gevonden.
- **Prestatieafspraken (Vechtdal Wonen):** 485 huurwoningen 2022-2030 (39% van 1.250 voor de kern Ommen); 2025: 25 woningen voor jongeren <28, 15% van vrijkomende huur voor senioren, 20 woningen voor mensen met een beperking; pilot Woningdelen 2026; max. huurstijging 6,5% (2025) [ZOEK].
- **Betaalbaarheid:** 30-40-30 (Woondeal; Vlierlanden 3); lokaal aangescherpte koopgrens voor kleine kernen en toepassing op CPO: niet gevonden (A3).
- **Aansluiting CPO:** Ommens CPO's richten zich op **starters met lokale binding**; een CPO van 10-12 woningen met seniorencomponent sluit conceptueel aan op de ouderen-/doelgroepopgave en het Woonprogramma (CPO's vanuit plaatselijk belang), maar een gemeentelijke behoefte-onderbouwing voor het buitengebied is niet gevonden. Woonzorgvisie-doorvertaling (A5): niet gevonden. Starterslening: Verordening starterslening Ommen 2022 (CVDR679031; max. € 30.000, NHG) [ZOEK].

---

## Twee kernvragen (gelaagd)

### 1. Wonen in het buitengebied: ruimte voor een cluster van 10-12 woningen buiten de bestaande woonkernen?
- **(a) Gemeente:** het buitengebied is volgens beschikbare samenvattingen vrijwel gesloten voor nieuwe woningbouw; ruimte bestaat via Rood voor Rood/VAB (1-2 woningen per slooplocatie; buitengebied circa 75 in totaal), woningsplitsing en volgfuncties. Een cluster van 10-12 woningen valt in geen enkele gevonden regeling. Grotere programma's worden uitsluitend gemeentelijk geregisseerd aansluitend aan kernen of in buurtschappen (Vlierlanden 3, Beerzerveld, Arriërflier, Vinkenbuurt).
- **(b) Provincie:** "overige kern" (art. 4.4: lokale behoefte en bijzondere doelgroepen); art. 4.5 lid 2; KGO (art. 4.11); woonafspraken 4.14-4.15 (Woondeal West-Overijssel); redeneerlijn 4.122; instemming bij BOPA op de Lijst BOPA; Natura 2000/stikstof, NNN, waterwinning in het Vechtdal.
- **(c) Eindoordeel:** **beperkt tot onzeker, voor een vrijstaand cluster buiten een kern waarschijnlijk negatief.** Kansrijker: aansluitend aan een kern of buurtschap, met lokale binding, gemeentelijke regie of -medewerking, en een beperkter programma (7-10 woningen heeft precedent). Belangrijkste onzekerheden: uitkomst actualisatie Rood voor Rood/VAB, tekst coalitieakkoord 2026-2030, nieuw volkshuisvestingsprogramma, werkelijke BOPA-praktijk en provinciale houding, landbouwgebied-typologie van de locatie, Woondeal-programmering van een CPO, 30%-sociale-huureis voor particuliere initiatieven.

### 2. Agrarische herbestemming: ruimte voor omzetting van agrarisch bestemde grond naar bouw-/woonfunctie op deze schaal?
- **(a) Gemeente:** herbestemming van agrarische bedrijfsbebouwing naar wonen is geregeld op kleine schaal (VAB/Rood voor Rood); omzetting van onbebouwde agrarische grond naar wonen gebeurt alleen bij kernuitbreiding (Beerzerveld, Vlierlanden 3) met gemeentelijke regie en grondposities.
- **(b) Provincie:** art. 4.124 (landbouwgebied met generieke opgaven: transformatie van agrarische bouwpercelen; "nee, tenzij"-sturing via voorkant/instemming), KGO-investering gericht op natuur/water/klimaat in gebiedsspecifieke gebieden, woonafspraken, Lijst BOPA.
- **(c) Eindoordeel:** **gematigd negatief tot onzeker voor 10-12 woningen; kleinschalige varianten (1-6 woningen op bestaand erf) kansrijker; 10-12 aansluitend aan een kern het meest realistisch.** Zelfde onzekerheden als hierboven.

---

## Overijssel-controlepunten (Bijlage A)
Status: **G** gevonden, **D** deels gevonden, **N** niet gevonden, **T** tegenstrijdig, **NvT** niet van toepassing. Alle bronnen zijn zoekresultaat-samenvattingen (2026-10-02) tenzij anders vermeld.

| # | Bevinding | Status | Bron (URL) | Waar te vinden bij "niet gevonden" |
|---|---|---|---|---|
| A1 | Overige kern (art. 4.4) [PROV-MD]; geen bijzonder groeiprofiel gevonden; Ommen in Regio Zwolle-samenwerking; Vlierlanden 3 (375) als kernuitbreiding | D | [PROV-MD §1.3]; https://www.ommen.nl/actueel/start-uitvoering-van-19-projecten-van-ruimte-voor-de-vecht/ | Verstedelijkingsstrategie DSS Zwolle; Woondeal-bijlage |
| A2 | West-Overijssel; 290 gerealiseerd; 2 sleutelprojecten/508; opgave 650 vs. 1.250; harde/zachte plancapaciteit, 80/20, telling CPO, post kleine kernen: niet gevonden | D/T | [PROV-MD §1.5]; https://lokaleregelgeving.overheid.nl/CVDR695681/1 | Planmonitor/Dashboard Wonen; Addendum Woonvisie; Woondeal-bijlage 1 |
| A3 | 30% sociale huur nieuwe plannen (ook particuliere initiatieven volgens zoektool); 30-40-30 Vlierlanden 3; 15% in Woonprogramma; CPO-toepassing en lokale koopgrens kleine kernen: niet gevonden | T/D | https://www.vechtdalwonen.nl/media/1719/prestatieafspraken-ommen-2025.pdf | Prestatieafspraken 2026; Addendum Woonvisie; CPO-verkoopbrochures |
| A4 | Geen volkshuisvestingsprogramma; basis Woonvisie + Addendum; ladderpraktijk niet gevonden | N | https://www.ommen.nl/actueel/gemeente-ommen-en-vechtdal-wonen-maken-voor-2026-afspraken-over-wonen-en-leefbaarheid/ | RIS Ommen najaar 2026; Gemeenteblad |
| A5 | Doelgroepen in prestatieafspraken; seniorenhofje Lemele; woonzorgvisie-doorvertaling en geclusterde opgave niet gevonden; urgentieregeling via derde | D | https://ommencity.nl/2024/12/12/meer-woningen-voor-jong-en-oud-in-ommen/ | CVDR huisvesting/urgentie; woonzorgvisie West-Overijssel |
| B1 | Rood voor Rood CVDR658628 (3-6-2021), sloopstaffel 850/2.000 m², actualisatie ontwerp 1-10 t/m 12-11-2025, vaststelling niet gevonden; eigen KGO-kader niet gevonden | D | https://lokaleregelgeving.overheid.nl/CVDR658628/1 | CVDR-versiehistorie; Gemeenteblad na 12-11-2025; RIS |
| B2 | Max. 2 compensatiewoningen per locatie; buitengebied circa 75; 10-12 niet voorzien | D | zie §3.2 | Ontwerp-rapport evaluatie VAB (PDF) |
| B3 | Actualisatie t.o.v. Actualisatie 2026 (1-7-2026) niet gevonden; omgevingsplan nog tijdelijk deel; art. 4.2a-aanpassing niet gevonden | N | https://lokaleregelgeving.overheid.nl/CVDR696206/2 | Gemeenteblad 2026; DSO/ruimtelijkeplannen |
| B4 | Contour bestaand bebouwd gebied niet gevonden; Vlierlanden 3/Beerzerveld als uitleg aan de kern; Vinkenbuurt buurtschap [INTERPRETATIE] | N/D | zie §2.1 | Kaarten Omgevingsvisie 2021; ruimtelijke onderbouwing Vlierlanden 3 |
| B5 | Kwaliteitsinvestering = sloop (Rood voor Rood), bouwclaim (Vlierlanden 3); fonds/bankgarantie niet gevonden | D | zie §3.2, §11 | Beleidsregels (zekerheidsstelling); kostenverhaalsnota |
| C1 | Landbouwgebied-typologie niet bepaald (kaartlaag niet raadpleegbaar) | N | n.v.t. | https://ruimtelijkeplannen.overijssel.nl ; https://omgevingswet.overheid.nl/regels-op-de-kaart |
| C2 | Gebiedsvisie art. 4.124 lid 4 niet gevonden; aanknopingspunten Ruimte voor de Vecht, PPLG/GGA Vechtdal (niet beoordeeld) | N | zie §3.7 | Gemeentelijke gebiedsvisie buitengebied |
| C3 | Overlays: Natura 2000 Vecht en Beneden-Regge, NNN, GGA Vechtdal, waterwinning Hammerflier/Witharen; Catalogus niet gelezen | D | https://www.natura2000.nl/gebieden/overijssel/vecht-en-beneden-reggegebied | Catalogus Gebiedskenmerken (Bijlage VII); DSO-viewer |
| C4 | Redeneerlijn/energieparagraaf/netcongestie niet gevonden voor Ommen | N | n.v.t. | Ruimtelijke onderbouwingen 2026; Enexis |
| D1 | Deelname VAB-programma/4.39 niet gevonden (Vechtdal-gebiedsprocessen deels in Ommen) | N | https://toekomstvooronsplatteland.nl/investeren/vab-vrijkomende-agrarische-bebouwing-en-erftransformatie | vab@overijssel.nl; regelen.overijssel.nl; RIS |
| D2 | Erfcoach genoemd door gemeente; dekking Ommen tegenstrijdig (zie §4) | T | https://www.digitaleerfcoach.nl/gemeentes/ommen | https://erfcoachoverijssel.nl/contact-met-de-erfcoaches |
| D3 | VAB-beleid + Rood voor Rood + splitsing aanwezig; maximum per erf, collectieve precedenten niet gevonden; VAB in woonprogrammering ja (circa 75) | D | zie §3, §4 | CVDR/planviewer (verleende Rood-voor-Rood-plannen) |
| E1 | Accounthouder Ruimte (o.a. Ommen, Dalfsen, Zwartewaterland, Staphorst, Steenwijkerland), naam niet openbaar; Omgevingstafel IJsselland "indien nodig"; voorafgaand principeverzoek-aan-provincie niet standaard bevestigd; 1-op-1-gesprekken niet gevonden | D | https://www.odijsselland.nl/over/omgevingstafel ; https://lokaleregelgeving.overheid.nl/CVDR740793/1 | RIS; Overijssel Loket |
| E2 | Route: omgevingsplanwijziging (Beerzerveld, Arriërflier, Vinkenbuurt); BOPA-voorkeur/doorlooptijd Ommen niet gevonden; Lijst BOPA provinciaal [PROV-MD] | D | zie §3.1 | Afdeling RO; Gemeenteblad |
| E3 | Uitzonderingenlijst niet getoetst voor Ommen; 7-10 CPO-woningen blijven onder de grens van 11 in bestaand bebouwd gebied (Ommen-kern > 1.000 inwoners) [INTERPRETATIE]; geldt niet voor buitengebied | N | [PROV-MD §4.2] | Toelichting omgevingsplan Arriërflier |
| E4 | Geen provinciale zienswijze/aanwijzing/onthouden instemming 2023-2026 gevonden; historisch: reactieve aanwijzing bestemmingsplan Buitengebied (2010; Stcrt 2010, 5612; relatie ABRvS 201004545/1/R2 niet geverifieerd) | N | zie §3 | Nota's van zienswijzen; Prb; DSO |
| F1 | Gemeentelijke CPO-regeling (70% begeleider, max. € 20.000; architectlening) gevonden; provinciale regelingen niet aan Ommen gekoppeld (alleen Ruimte voor de Vecht-cofinanciering, vakantieparken); provinciale subsidie Collectieve wooninitiatieven niet onderzocht | D | https://woneninommen.nl/woonbeleid/cpo | https://regelen.overijssel.nl ; begroting/jaarstukken Ommen |

### Houdbaarheid
- Provinciale wijzigingen die Bijlage A-uitkomsten raken: Actualisatie 2026-2 Omgevingsverordening (PS-besluit gepland dec. 2026), Besluit versterking regie volkshuisvesting (1-1-2027), gemeentelijke volkshuisvestingsprogramma's (uiterlijk 1-7-2027), subsidie 4.39 (verplichting vóór eind 2026), Lijst BOPA verwijst nog naar Woonagenda's 2021-2025 [PROV-MD §6.1].
- **Controleer vóór citeren altijd** de geconsolideerde Omgevingsverordening (CVDR706717) en de kaartlaag art. 4.123 voor artikelnummers en gebiedstypen. In deze sessie zijn geen provinciale artikelen opnieuw geverifieerd.
- Ommense kerndocumenten die snel kunnen wijzigen: definitieve Rood voor Rood/VAB 2025-2026, Nota Grondbeleid (uiterlijk nov. 2027), volkshuisvestingsprogramma, coalitieakkoord-uitwerking, omgevingsplan (versies 2026), Erve Arriërflier-planning (Q1 2026 → medio 2026).

---

## Tegenstrijdigheden en open punten (samenvatting)
1. Woningbouwopgave: 650 (Woonprogramma 2021-2025) versus 1.250 (prestatieafspraken/Addendum/projectsites; ook Omgevingsvisie 1.250 tot 2040).
2. Sleutelprojecten Woondeal: "Vlierlanden + binnenstedelijk = 508" versus "Arriën-Ommen circa 375" versus "Vlierlanden 3 circa 375".
3. Erve Arriërflier: 10 versus 8 CPO-kavels; planning omgevingsplan Q1 2026 versus medio 2026.
4. Vinkenbuurt 7+1 versus 8-10; Beerzerveld 8, 20 en 34 woningen (fasen/onderdelen, niet vastgesteld).
5. Sociale huur: 15% (Woonprogramma) versus 30% (afspraken).
6. Grondbeleid: "geen actieve grondexploitaties" versus gemeentelijke kavelgronduitgifte en bouwclaim.
7. Rood voor Rood: 850/2.000 m² versus sloop-bouwverhoudingen 1:3/1:4 in dezelfde samenvatting; onduidelijk of 2.000 m²/2 woningen de 2021- of 2025-versie betreft; "950-1.150 m²" bij een ander (vermoedelijk Almelo) document niet aan Ommen toegeschreven.
8. Identiteit PRO Ommen (hernoemde LPO of GL-PvdA); datum burgemeestersaanbeveling; opkomst 65,42% versus 65,45%.
9. Erfcoach-dekking Ommen; Natura 2000 Vecht en Beneden-Regge (Dalfsen wel/niet genoemd); MeeDenkdagen Arriën (30-31 januari versus maart 2026).
10. Omgevingstafel IJsselland-URL: [PROV-MD] noemt een 404-pagina; vervangen door https://www.odijsselland.nl/over/omgevingstafel (niet geopend).

## Niet gevonden en waar te vinden
Zie ook de kolom "Waar te vinden" in de Bijlage A-tabel. Aanvullend: letterlijke tekst coalitieakkoord 2026-2030 (raadsvoorstel 2-7-2026, RIS Ommen); inhoud ontwerp-rapport VAB 2025 (https://openpub.ommen.nl/...pdf); Woonprogramma 2021-2025 volledige tekst (CVDR695681); inschrijfvoorwaarden en prijs CPO-kavels (woneninommen.nl, storyblok-PDF's); leges-tarieven (tarieventabel CVDR753504); welstand/landschap (CVDR, omgevingsplan); Erve Arriërflier-onderbouwing en provinciale rol (https://www.beleidsradar.nl/documenten/woningbouw-erve-arrierflier-vlierlanden-b25b8ca0-8eac-4504-91e7-9cd51289d209); Facebook/LinkedIn, De Stentor, Tubantia, RTV Oost (niet doorzocht of zonder relevante Ommen-treffers).

## Bijlage: niet-Ommense treffers (gebruik deze nummers NIET voor Ommen)
CVDR734307 (Gennep, VAB), CVDR638437 (Best), CVDR722706, CVDR745888 (Deventer), CVDR672822/672839 (Dinkelland/Tubbergen), CVDR734518 (Rijssen-Holten), CVDR743316 (Steenwijkerland), CVDR11483 (Dalfsen, Rood voor Rood), CVDR725562 (Apeldoorn), CVDR725916 (Bronckhorst), CVDR636460 (Meierijstad), CVDR743755/exb-2025-32184 (vermoedelijk Almelo), CVDR305226/305339/379343/424954 (KGO-kaders andere gemeenten), CVDR739354 (Groningen), CVDR729056 (Gooise Meren), CVDR753410/741632 (huisvesting, gemeente onbekend), CVDR755748 (Omgevingsprogramma Volkshuisvesting, andere gemeente), alle "Nota Grondbeleid/Grondprijzenbrief 2026/Nota Kostenverhaal"-CVDR's in §5 en §11, "DOEN'22"-coalitieberichten (Hardenberg), gemeente.emmen.nl-resultaten (Emmen, Drenthe), Sallandse Heuvelrug-stikstofdocumenten (niet Ommen).

## Aanbevolen vervolgstappen (herhaling met werkende bronnentoegang)
1. **Netwerktoegang verruimen** (Network access in de omgevingsinstellingen) voor: ommen.nl, openpub.ommen.nl, lokaleregelgeving.overheid.nl, zoek.officielebekendmakingen.nl, repository.overheid.nl, planviewer.nl, ruimtelijkeplannen.nl/.overijssel.nl, woneninommen.nl, detoren.net, vechtdalcentraal.nl, ommen.bestuurlijkeinformatie.nl/pcportal, vechtdalwonen.nl, overijssel.nl, overijsselsewoonaanpak.nl; en het zoekbudget verhogen.
2. **Prioriteit bij herhaling:** (1) ontwerp-rapport VAB 2025 + vaststelling geactualiseerde Rood voor Rood; (2) CVDR745896 (uitgever); (3) coalitieakkoord 2026-2030; (4) Woonprogramma 2021-2025 en Addendum (CPO-passage, kavelbeleid, 650/1.250); (5) 30%-sociale-huureis voor particuliere initiatieven; (6) kaartlaag art. 4.123 en overlays voor concrete locaties; (7) Legesverordening-tarieventabel en kostenverhaal; (8) Nota Grondbeleid; (9) volkshuisvestingsprogramma/huisvestingsverordening; (10) Woondeal-bijlage 1 en Planmonitor.
