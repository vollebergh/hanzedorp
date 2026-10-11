# Gemeente Ommen — CPO-naslagwerk (provincie Overijssel)

> **Status: samengevoegd rapport met verificatieronde (2026-10-11).** Vier gelijktijdige deelonderzoeken (bestuursinformatie, provinciaal-lokale toepassing, nieuws 2024-2026, juridische registers) zijn samengevoegd en dubbelingen zijn weggehaald. Kerncitaten zijn tegen de brontekst gecontroleerd; waar deelonderzoeken elkaar tegenspraken of een bevinding niet onafhankelijk kon worden herhaald, staat dat onder "Tegenstrijdigheden en onzekerheden". Wat niet gevonden is, staat met de vindplaats in "Niet gevonden / niet onderzocht".

## Verantwoording
- **Raadplegingsdatum:** 2026-10-06 en 2026-10-11 (bronnen met eigen datum waar die afwijkt).
- **Provincie en gebruikt provinciebestand:** Overijssel, [`provincie_overijssel.md`](provincie_overijssel.md) (stand 2026-10-02; in deze ronde op één punt gecorrigeerd, zie "Correctie op het provinciebestand"). Het Overijsselse regime is leidend voor het omgevingsplan. Bijlage A is van toepassing; Bijlage B (Gelderland) niet.
- **Primair model + effort:** de synthese en het eindrapport zijn geschreven door Claude Sonnet 5.5 (`claude-sonnet-5-5`); het reasoning-effort van de sessie is niet expliciet ingesteld of bekend.
- **Deelonderzoeken (Fase 2):**

| Deelonderzoek | Brontype | Model | Opmerking |
|---|---|---|---|
| 1 | Gemeentelijke bestuursinformatie | Claude Sonnet 5.5 | Eerste run (2026-10-06) is door een sessielimiet afgebroken vóór het rapport; herstart op 2026-10-11 met hergebruik van de al geëxtraheerde bronbestanden. Kerncitaten zijn in de herstart opnieuw tegen de brontekst gecontroleerd. |
| 2 | Provinciaal-lokale toepassing | Claude Sonnet 5.5 | Idem (afgebroken 2026-10-06, afgerond 2026-10-11). |
| 3 | Nieuws en actualiteit 2024-2026 | Claude Sonnet 5.5 | Eén run; rapport compleet. |
| 4 | Juridische en officiële registers | Claude Sonnet 5.5 | Eén run; rapport compleet. |

- **Methode:** vier deelonderzoeken met elk één brontype maar alle 12 onderwerpen, samengevoegd door de hoofdagent. Zelf gecontroleerd door de hoofdagent: de kop van CVDR757546 (organisatie en vaststellend orgaan), de classificatie van drie projectpunten (Van Alewijkstraat Beerzerveld, Koloniedijk 22a Vinkenbuurt, Lemelerweg 53a Lemele) tegen de landbouwgebied-typologie van de provinciale verordening-viewer, en alle onderlinge tegenstrijdigheden tussen de deelrapporten (zie verderop).
- **Toegang en technische beperkingen:** ommen.nl en woneninommen.nl waren bereikbaar met een gewone browser-user-agent; het raadsinformatiesysteem (Notubiz, `ommen.raadsinformatie.nl` / `ommen.bestuurlijkeinformatie.nl`) was via de API volledig uitleesbaar (2.436 agendapunten 2021-2026 geïndexeerd). CVDR, Gemeenteblad en Provinciaal blad zijn via de SRU-diensten volledig doorzocht (477 unieke CVDR-nummers van Ommen; 4.239 officiële publicaties; 878 Provinciaal-blad-treffers). De Stentor was niet toegankelijk (betaalmuur); De Toren (detoren.net) gaf deels 403 en is daarom deels via een samenvatting gelezen (gemarkeerd **[WF]**). De regeltekst van het tijdelijk omgevingsplan Buitengebied was niet te bereiken via ruimtelijkeplannen.nl (404) en de DSO-API vraagt een sleutel.
- **Betrouwbaarheidsmarkering:** citaten zijn letterlijk uit de brontekst. **[PB]** = uit `provincie_overijssel.md`; **[TK]** = trainingskennis, niet live geverifieerd; **[INT]** = interpretatie van de samensteller; **[BER]** = eigen berekening; **[WF]** = via samenvatting gelezen, lager betrouwbaar; **[OCR]** = scan, niet letterlijk te citeren.
- **Plaatsen in de gemeente (BAG-woonplaatsen, PDOK Locatieserver, 2026-10-06):** Arriën, Beerze, Beerzerveld, Dalmsholte, Giethmen, Lemele, Ommen, Stegeren, Vilsteren, Vinkenbuurt, Witharen. Besthmen, Hammerbrug, Junne en Eerde zijn buurtschappen zonder BAG-woonplaats; Den Ham ligt in Twenterand en Mariënberg in Hardenberg. De gemeente noemt voor het omgevingsplan "Kleine Kernen" ook Junne, Ommerkanaal en Varsen.
- **Woonregio:** West-Overijssel (Woondeal West-Overijssel 2025-2030, 20-3-2025; verstedelijkingsstrategie Regio Zwolle). De woonregio overschrijdt de provinciegrens niet; afstemming met Drentse buurgemeenten is in de gelezen stukken niet gevonden.

### Verificatie van CVDR-nummers (organisatie uit de kop "Overheidsorganisatie", geraadpleegd 2026-10-06/11)
| Nummer | Organisatie volgens kop | Titel | Opmerking |
|---|---|---|---|
| CVDR757546 | **Ommen** | Beleidsregels Rood voor Rood gemeente Ommen 2026 | Geldend vanaf 26-2-2026; kop: "Vastgesteld door college van burgemeester en wethouders"; Gmb 2026-82708 (ondertekend 10-2-2026); vervangt CVDR658628. Kop zelf opnieuw gelezen op 2026-10-11. |
| CVDR658628 | **Ommen** | Beleidsregels Rood voor Rood gemeente Ommen | 3-6-2021 t/m 25-2-2026 (vervallen); vastgesteld door de raad |
| CVDR712101 | **Ommen** | Lijst Bindend Adviesrecht Ommen | Raad 23-11-2023; in werking 1-1-2024; Gmb 2023-564653 |
| CVDR753504 | **Ommen** | Verordening op de heffing en de invordering van leges Ommen 2026 | Raad; in werking 1-1-2026; Gmb 2025-567439 |
| CVDR696206 | **Ommen** | Omgevingsplan gemeente Ommen | Bevat de nieuwe hoofdstukken (bruidsschat); het tijdelijk deel (voormalige bestemmingsplannen) staat er niet in |
| CVDR695681 | **Ommen** | Woonprogramma 2021-2025 | **Collegestuk**; in werking 8-5-2023, terugwerkend 1-7-2021; Gmb 2023-201096 |
| CVDR745908 | **Ommen** | Beleidsnotitie woningsplitsing oktober 2025 | Raad; in werking 30-10-2025; Gmb 2025-463667 |
| CVDR765864 | **Ommen** | Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten Ommen 2026 | College; in werking 28-8-2026; Gmb 2026-404594. **Niet verwarren met CVDR765519 (Olst-Wijhe, zelfde titel).** |
| CVDR712088 | **Ommen** | Verordening nadeelcompensatie Ommen 2024 | Raad; € 300 per aanvraag |
| CVDR679031 | **Ommen** | Verordening starterslening gemeente Ommen 2022 | Raad; max. € 30.000 |
| CVDR755720 | **Ommen** | Financiële verordening gemeente Ommen 2025 | Art. 24: Nota Grondbeleid ten minste eens per vier jaar |
| CVDR737758 / CVDR737769 | **Ommen** | Voorbereidingsbesluiten raatakkercomplexen / karrensporenzones | In werking 4-4-2025; Prb 2025-5561 / 5563 |
| CVDR708884, 713315, 714041 | **Overijssel (kop)** | Voorbereidingsbesluiten Omgevingsverordening/Zonneparken/Windenergie "gemeente Ommen" | Staan in de SRU onder creator "Ommen", maar de kop noemt Overijssel. Niet als Ommens beleid gebruikt. |
| CVDR708401 | **BZK (kop)** | Voorbeschermingsregels hyperscale datacentra | Rijksregeling, idem |
| CVDR305226, 720837, 765519, 704153 e.d. | n.v.t. | Nummers uit het Olst-Wijhe-rapport | Niet voor Ommen gebruikt |

Wat in CVDR en Gemeenteblad **niet** bestaat voor Ommen: een huisvestingsverordening/urgentieregeling, een eigen KGO-kader of aparte VAB-beleidsregel, een Nota Grondbeleid, een nota kostenverhaal, een CPO-beleidsregel en een volkshuisvestingsprogramma.

### Correctie op het provinciebestand
`provincie_overijssel.md` §6.2 punt 2 stelt dat de nieuwe landbouwgebied-typologie (art. 4.123) niet in de publieke WFS staat en gebruikt de voormalige ONW-zone als indicatie. Uit dit onderzoek blijkt dat de typologie wel bevraagbaar is via de verordening-viewer (zie §3.6 en Bijlage A, C1). Voor Ommen onderschat de ONW-proxy (8,0%) het gebiedsspecifieke type met een factor vijf (41,6%). Die passage is in het provinciebestand aangepast.

---

## Samenvatting
1. **CPO is in Ommen uitgewerkt gemeentelijk beleid, maar bijna uitsluitend op gemeentegrond in of aan de kernen en voor lokale starters en senioren.** Vijf CPO's zijn gerealiseerd of lopend (Lemele, De Meerkoet, Beerzerveld, Erve Arriërflier, Vinkenbuurt), elk met 4-8 woningen. Sinds mei 2024 bestaat ook een route voor een collectief met **eigen grond zonder woonfunctie** (CPO-fonds tot € 50.000, terug te betalen). Dat is steun in de voorfase, geen planologische toezegging.
2. **Buitengebied: geen kader voor 10-12 woningen.** Rood voor Rood 2026 geeft standaard maximaal twee compensatiewoningen per slooplocatie; het grootste precedent op een agrarisch erf is **drie woningen** (Varsenerweg 5a, maatwerk). Beerzerweg 36 kreeg een negatief principebesluit als "solitair woonerf".
3. **Wel een open route via de kern:** aansluitend aan een kern behandelt de gemeente woningbouw op agrarische grond als "uitleg van het dorp" (Van Alewijkstraat Beerzerveld, 34 woningen, raad 10-7-2025). Dat was echter gemeentegrond met raadsbesluit en gemeentelijke regie.
4. **Raadsadvies is bindend** voor elke woning buiten bestaand stedelijk gebied; in de praktijk loopt grotere woningbouw via een raadsbesluit ("TAM-omgevingsplan"), niet via een BOPA.
5. **De provincie sluit in de gevonden Ommense dossiers steeds aan of stemt in; een formele zienswijze, aanwijzing of onthouden instemming 2023-2026 is niet gevonden.** Wel zijn er informele remmende signalen: Vinkenbuurt ging van 11 naar 8 woningen ("aan de forse kant"), en de Lemele-visie noemt de provincie "terughoudend" bij uitbreidingslocaties.
6. **Typologie:** 41,6% van de gemeente is landbouwgebied met gebiedsspecifieke opgaven, 16,8% met generieke opgaven. Van de landbouwgrond ligt 60,2% in het gebiedsspecifieke en 27,3% in het generieke type; alleen Vinkenbuurt grenst aan generiek landbouwgebied.
7. **Praktische drempels voor een nieuw project:** netcongestie (volgordelijst met aanmeldtermijn tot 10-9-2026, inmiddels verstreken), stikstof (22,0% van de gemeente is Natura 2000; provinciale opschorting van natuurvergunningen tot ten minste 1-2-2027), en een nog ontbrekend nieuw kader (woonvisie, huisvestingsverordening, Ontwikkelperspectieven Landelijk Gebied, volkshuisvestingsprogramma).
8. **Bestuurlijk klimaat:** coalitie VOV + CDA + PRO Ommen (11 van 17 zetels), akkoord 26-6-2026, college geïnstalleerd 2-7-2026. **Er is geen coalitie in vorming.** Wethouder Wonen én Ruimtelijke Ordening is Alice van den Nieuwboer (CDA). Het akkoord noemt "inzet op collectief particulier opdrachtgeverschap" als te onderzoeken instrument, maar kent geen doelstelling voor nieuwe woningen op onbebouwde agrarische grond.

---

## 1. CPO-beleid

### 1.1 Omgevingsvisie "Ommen Jouw Toekomst" (raad 16-12-2021, unaniem)
Bron: https://www.ommen.nl/wp-content/uploads/2022/10/Gemeente_Ommen_omgevingsvisie_dec_2021.pdf (geraadpleegd 2026-10-06; IMRO NL.IMRO.0175.omgevingsvisieOV01-VG01).

> "Naast nieuwe fysieke woonvormen kijken we samen met onze partners ook naar nieuwe organisatievormen, zoals vormen van collectief particulier opdrachtgeverschap."

> "De verstrekken van starterslening en het mede faciliteren van Collectief Particulier Opdrachtgeverschap (CPO) zijn enkele instrumenten die we inzetten om eigen inwoners zicht op een woning in Ommen te geven."

> "Samen met de kernen zullen we bijvoorbeeld via vormen van collectief particulier opdrachtgeverschap (CPO) zoeken naar mogelijkheden om de bouw van nieuwe woningen zo goed mogelijk aan te laten sluiten op de lokale behoefte en ook bereikbaar te houden de mensen uit de kern die er willen blijven wonen."

De visie is faciliterend en niet-bindend; CPO wordt gekoppeld aan de kernen en aan lokale binding.

### 1.2 Woonprogramma 2021-2025 (college; CVDR695681)
Bron: https://lokaleregelgeving.overheid.nl/CVDR695681 (geraadpleegd 2026-10-06). Vastgesteld door het college, niet de raad; er is geen opvolger gevonden.

> "Door middel van oprichten van CPO's vanuit de plaatselijke belangen worden vraag en aanbod bij elkaar gebracht. Dergelijke CPO's kunnen rekenen op ondersteuning vanuit de gemeente."

> "33. Als initiatieven voor collectieve woonvormen (bijvoorbeeld wonen in een hofje of Collectief Particulier Opdrachtgeverschap) zich aandienen, willen we deze faciliteren en ondersteunen, mits er sprake is van een aantoonbare lokale behoefte."

Voor kleine kernen toetst de gemeente de concrete vraag onder meer op: "a. Vorm van het initiatief: individueel of collectief? b. Locatie: van wie is de grond? c. Financiële draagkracht" (maatregel 6).

### 1.3 Addendum Woonvisie "Naar een ruimtelijke strategie" (definitief 5-10-2023; raad 23-11-2023 unaniem)
Bron: https://ommen.raadsinformatie.nl/document/13330501/1/Bijlage+1+20231010-Addendum+Ommen_DEFINITIEF (geraadpleegd 2026-10-06). Groot document, beschreven:
- Twaalf gemeentelijke locaties met voorkeursscenario's, **allemaal gemeentelijk bezit in of bij de kern Ommen**, geen agrarische grond buiten de kernen.
- CPO-label in de locatietabellen: Havengebied Oost (6 van 109), Boven Vlierlanden XL links (18 van 33), Vlierlanden XL rechts (12 van 28) en Meerkoet (4 van 5). De samenvattingstabel noemt 30 CPO-woningen en 50 flexwoningen; de som van de locatietabellen is 40 [BER] (zie Tegenstrijdigheden).

> "De ontwikkeling van gemeentegronden door collectief particulier opdrachtgeverschap is voor de gemeente een passende ontwikkelvorm voor starters en/of ouderen. [...] Door als gemeente gronden beschikbaar te stellen met een passend bestemmingsplan kunnen collectieven, zonder tussenkomst van ontwikkelaars, zelfstandig goedkopere woningen realiseren. [...] Om CPO initiatieven te stimuleren zal een CPO-Ontwikkelbudget door de gemeente beschikbaar worden gesteld." (PDF-kolommen; woordvolgorde licht gereconstrueerd)

### 1.4 CPO Uitvoeringsregels (mei 2024)
Bron: https://a.storyblok.com/f/284824/x/cfd69c0eea/uitvoeringsregels-cpo-gemeente-ommen_mei-2024.pdf (ook woneninommen.nl/woonbeleid/cpo; geraadpleegd 2026-10-06). Korte regeling, kern integraal:

> "Voor elke CPO-locatie [...] wordt er een kopersvereniging opgericht die bestaat uit evenveel leden als mogelijk aantal woningen/kavels. [...] Alleen een lid van desbetreffende vereniging kan in aanmerking komen voor een ontwikkelrecht voor maximaal één woning."

> "De juridische entiteit 'Vereniging met volledige rechtsbevoegdheid' stellen we verplicht [...]. In de statuten dient de doelgroep benoemd te worden én de zelfbewoningsplicht [...]. Verhuur en/of speculatie is niet toegestaan."

> "De gemeente stelt de vereniging een subsidie ter beschikking voor het inhuren van de onafhankelijk procesbegeleider voor 70% van de geoffreerde kosten tot een maximum van €20.000,-." "De gemeente stelt de vereniging een voorschot ter beschikking van €15.000,- om een deel voor te financieren voor het inhuren van een architect die is aangesloten bij BNA." "De gemeente stelt per locatie een projectleider ter beschikking."

> "4. CPO-project zonder gemeentelijke gronduitgifte. Het is mogelijk dat een CPO-collectief eigenaar is van een perceel waar op dit moment geen woonfunctie mogelijk is, maar waar de gemeente wel positief tegenover staat om de activiteit wonen mogelijk te maken. Hiervoor geldt dat de gemeente een budget beschikbaar stelt, met een maximum van €50.000. Het gaat hier om een CPO-fonds (in de vorm van een terug te betalen voorschot) om werkzaamheden (bijv. uitvoeren van onderzoeken) voor te financieren. De beschikbare middelen worden vastgelegd in een anterieure overeenkomst tussen collectief en gemeente Ommen."

Overig: doelgroepen "(koop)starters, senioren en bijzondere wooninitiatieven"; uitgifte via inschrijving op woneninommen.nl met punten (inschrijvingen voor Vinkenbuurt en Arriërflier: volgorde 50 punten, motivatie 50 punten); grondprijs volgens de grondprijsbrief; participatieplicht (aangrenzende grondeigenaren binnen 300 m); levering binnen twee weken na een onherroepelijke omgevingsvergunning. Er staat geen maximumaantal woningen in de regels; de uitgegeven projecten zijn 4-8 woningen.

**Relevantie [INT]:** §4 is de enige gemeentelijke regeling die letterlijk een collectief met eigen grond zonder woonfunctie noemt. Het is een toezegging van financiële ondersteuning, geen toezegging van planologische medewerking: de gemeente moet "positief [...] staan", en de omgevingsplanprocedure en de provinciale toets blijven een apart traject.

### 1.5 Raadsbesluiten en -aanzetten (2022-2026)
- **Motie "CPO fonds"** (ChristenUnie, mede namens CDA en LPO; raad 10-3-2022, algemene stemmen): college komt "Uiterlijk 1 juli 2022 met een voorstel, voor een revolverend CPO fonds". Bron: https://ommen.raadsinformatie.nl/document/11290733/1/220309+Motie+CU+-+CPO+fonds+-+raad+10+mrt_22+%28getekend%29 (2026-10-11). Dit is de politieke herkomst van het ontwikkelbudget (2023) en het CPO-fonds (2024).
- **Perspectiefgesprek 20-3-2025**, opdracht d.4: een voorstel over het behouden en toegankelijk maken van de opgebouwde CPO-kennis. Of dat voorstel is uitgebracht, is niet gevonden.
- **Amendement A2 bij de Stedenbouwkundige visie Lemele** (raad 12-3-2026; 16 voor, 1 tegen = VVD): de gemeente houdt "regie [...] zodat CPO's daadwerkelijk aan tafel kunnen komen" en zet "pro-actief de mogelijkheden voor ondersteuning van CPO's" in.
- **Coalitieakkoord 2026-2030**: "inzet op collectief particulier opdrachtgeverschap" als te onderzoeken instrument (zie §10).

---

## 2. Openheid voor nieuwbouw buiten woonkernen

### 2.1 Beleidslijn (omgevingsvisie 2021)
> "We groeien in een omvang die past bij het profiel van Ommen en komen dan uit bij maximaal 1.250 nieuw te bouwen woningen tot 2040. Dat is het maximale aantal dat we kunnen accommoderen in het uitleggebied De Vlierlanden, bestaande en nieuwe inbreidingslocatie en vanuit een vraag gestuurde woningbouw in onze kernen en het buitengebied. Meer dan 1.250 vraagt om nieuwe uitleggebieden voor woningbouw en dat vinden we niet passen bij het groene karakter van Ommen en doet afbreuk aan de bestaande waarden van landbouw en natuur."

> "Voor het behoud van vitale en krachtige kernen is een op de behoefte afgestemde vraag gestuurde ontwikkeling van nieuwe woningen nodig. Dit kan de behoefte aan kleinschalige uitleggebieden bij kernen wenselijk maken."

> "Ook voor een qua oppervlak ruim bemeten gemeente als Ommen geldt de ladder. [...] Nieuwe opgaven [...] ontwikkelen we zoveel mogelijk compact door het inbreiden binnen bestaand bebouwd gebied."

Voor het buitengebied: "We willen ons buitengebied nadrukkelijk niet op slot zetten." Wonen in het buitengebied loopt via VAB en Rood voor Rood. Het woonprogramma rekent in totaal op "maximaal zo'n 75 woningen" in het buitengebied (zie §4.1) en 50-100 woningen vraaggestuurd in de kleine kernen.

### 2.2 De woningbouwopgave: vier verschillende cijfers
Omgevingsvisie 2021: maximaal 1.250 tot 2040. Addendum 2023: ambitie 1.250 tot 2040, met de wens dit al in 2030 te halen. MJP Grondexploitaties 2026: "Wij bouwen tot 2030 1250 woningen". Coalitieakkoord 2026: "Tot 2040 moeten wij circa 1.625 nieuwe woningen bouwen". De 1.625 komt niet uit een gepubliceerd rapport (waarschijnlijk uit de niet openbaar gevonden uitvoeringsstrategie Woon- en werklocaties); er is nog geen nieuwe woonvisie die dit bekrachtigt.

### 2.3 Ladder en volkshuisvestingsprogramma (A4)
- De omgevingsvisie verwijst expliciet naar de ladder. Bij Van Alewijkstraat is de ladder toegepast: "Voorliggend project voorziet in de realisatie van maximaal 34 woningen en betreft daarmee een nieuwe stedelijke ontwikkeling. [...] In de toetsing is aangetoond dat sprake is van zowel een kwantitatieve als een kwalitatieve behoefte." De gemeentelijke lezing: "meer dan 11 woningen" is een woningbouwlocatie; bij 12 woningen is de ladder dus aan de orde en bij 10-11 per geval te motiveren. In de toelichting op Erven Benninck (2022) staat dat bij minder dan 12 woningen "geen sprake is van een stedelijke ontwikkeling".
- **Er is geen (ontwerp-)volkshuisvestingsprogramma** gevonden (CVDR, Gemeenteblad, Provinciaal blad, RIS, ommen.nl). Het coalitieakkoord kondigt een "vernieuwde woonvisie met meer ambitie" aan. De gemeente kent een besloten commissieagendapunt van 3-4-2025 over "mogelijke toekomstige ontwikkelrichtingen voor woon- en werklocaties", en het akkoord noemt de "uitvoeringsstrategie 'Woon- en werklocaties'" en de "Ruimtelijke Visie Ommen 2040" als integraal beleidskader. **Beide stukken zijn niet openbaar gevonden.**
- Provinciaal blijven art. 4.4, 4.5 en 4.15 gelden en worden in de Ommense stukken gebruikt (Van Alewijkstraat, Beerzerweg 26), niet het nieuwe programma.

### 2.4 Positie in het concentratiebeginsel (A1)
Ommen is voor art. 4.4 een "overige kern": alleen lokale behoefte en bijzondere doelgroepen, tenzij regionale afspraken anders bepalen [PB]. De gemeente positioneert zich in de Regionale Woonagenda als "Centraal Wonen". In de verstedelijkingsstrategie Regio Zwolle kan voor Ommen een bijdrage tot "2.000+ woningen tot 2040" gelden, die de raad bewust op 1.250 begrenst. Een eigen groeiprofiel voor de kleine kernen is niet gevonden; het Strategieboek zelf is niet gelezen.

---

## 3. Openheid voor agrarische herbestemming

### 3.1 Wettelijk/procedureel kader in Ommen
Ommen werkt nog met **tijdelijke omgevingsplannen** (voorheen bestemmingsplannen). Kleine Kernen en Wonen worden naar verwachting in 2027 omgezet (kennisgeving 3-6-2026), Buitengebied volgt in 2027-2030 (de VAB-evaluatie noemde 2028) (https://www.ommen.nl/omgevingsplan-ommen/, 2026-10-11). Het omgevingsplan is nog niet aangepast aan art. 4.123-4.124; de driejaarstermijn van art. 4.2a loopt tot 1-7-2029 [PB]. Drie routes:

| Route | Wanneer | Besluitvorming | Voorbeeld |
|---|---|---|---|
| **Wijziging omgevingsplan ("TAM-omgevingsplan", hoofdstuk 22b)** | Meerdere woningen, nieuwe woonbestemming, uitleg aan een kern, Rood voor Rood met extra woningen | Gemeenteraad (ontwerp 6 weken ter inzage, zienswijzen, vaststelling, beroep) | Van Alewijkstraat (34, raad 10-7-2025), Varsenerweg 5a (3, raad 29-1-2026), Beerzerweg 26 (2, raad 4-6-2026) |
| **BOPA** (omgevingsvergunning buitenplanse omgevingsplanactiviteit) | Kleinschalig, concreet bouwplan | College, na **bindend advies van de raad** | Bermerstraat 1 (raad 12-3-2026), Gravendijk Vilsteren (4 woningen, raad 24-9-2026), Beerzerpoort 1 en 6 (raad 24-9-2026) |
| **Binnenplanse afwijking/wijzigingsbevoegdheid** | VAB-functiewijziging binnen een bestaand bouwvlak | College, met de Rood-voor-Rood-regels als toetsingskader | circa 5 gevallen 2021-augustus 2025 |

**Lijst Bindend Adviesrecht (CVDR712101; geraadpleegd 2026-10-06):**

> "1. Wonen 1.1 Het toevoegen van meer dan twee woningen in bestaand stedelijk gebied. 1.2 Het toevoegen van één of meer woningen buiten bestaand stedelijk gebied. 1.3 Deze regel geldt niet als de gemeenteraad al eerder heeft besloten op de toevoeging van de woningen uit het voorgenomen plan [...]."

> "In het buitengebied is de toevoeging van woningen niet zondermeer toegestaan. Gezien de complexere afweging dienen deze altijd aan de gemeenteraad voor advies voorgelegd worden."

> "2.3 Het toepassen van de rood voor rood regeling, voor zover het betreft de toevoeging van extra woningen of functies; [...]"

Participatie is bij deze gevallen verplicht. De gepubliceerde tekst bevat nog concept-resten ("(raad?)", "???"). De evaluatie van de lijst is uitgesteld tot 1-1-2026 (raadsbrief 22-10-2024: "Tot op heden is er nog geen gebruik gemaakt van de genoemde delegatie" **[OCR]**); sinds 2026 zijn drie BOPA's op deze grondslag behandeld.

**Provinciale Lijst BOPA in de praktijk.** De motivering van Beerzerpoort 1 en 6 (§12.2.2, geraadpleegd 2026-10-11) is letterlijk:

> "In gevallen waarvoor GS in de 'Uitzonderingenlijst vooroverleg 2023' hebben bepaald dat er geen vooroverleg hoeft plaats te vinden met de provinciale diensten is geen advies met instemming vereist. Dit is het geval. Advies met instemming is dan ook niet aan de orde."

Dit is een kleine BOPA (drie wooneenheden op een bestaand erf in beschermd dorpsgezicht). Voor 10-12 **nieuwe** woningen op onbebouwde agrarische grond zou de Uitzonderingenlijst volgens [PB §4.2-4.3] niet gelden en is advies met instemming vereist. Een BOPA voor 10 of meer nieuwe woningen is in Ommen niet gevonden; grotere projecten (Beerzerveld 34, Vinkenbuurt 8, Arriërflier 45-50, Prinses Julianastraat 60) liepen via een TAM-omgevingsplan door de raad.

### 3.2 Rood-voor-Rood-beleidsregels 2026 (CVDR757546; Gmb 2026-82708; in werking 26-2-2026)
Ommens enige gepubliceerde reken-/weegkader. Kern, letterlijk (geraadpleegd 2026-10-06):

> "Artikel 4 [...] 1. Om in aanmerking te komen voor het bouwen van een compensatiewoning, dient op de slooplocatie minimaal 850 m2 aan voormalige agrarische bedrijfsbebouwing te worden gesloopt. 2. Om in aanmerking te komen voor het bouwen van twee compensatiewoningen, dient op de slooplocatie minimaal 2.000 m2 aan voormalige agrarische bedrijfsbebouwing te worden gesloopt. 3. Indien op de slooplocatie onvoldoende sloopmeters aanwezig zijn [...] mag ook het oppervlak van elders in het buitengebied van de gemeente Ommen te slopen voormalige agrarische bedrijfsbebouwing worden ingezet. [...] In dat geval dient het aantal sloopmeters op de locatie voor het bouwen van één compensatiewoning in beginsel minimaal 500 m2 te bedragen."

> "Artikel 5 [...] 1. Een compensatiewoning heeft een inhoud van maximaal 750 m3. 2. In de plaats van een compensatiewoning mag ook worden gekozen voor alternatieve woonvormen waarbij binnen de maximale 750m3 er 2 of meer zelfstandige wooneenheden worden teruggebouwd. 3. Bij een compensatiewoning of een alternatieve woonvorm met meerdere wooneenheden is per wooneenheid tot maximaal 150 m2 aan bijgebouwen toegestaan."

- **Kortingen op sloopmeters:** sociale huur −100 m² (één woning) / −250 m² (twee); middenhuur of goedkope koop −75 / −200 m²; terugbouwen in of aan de rand van een kern of buurtschap −100 / −250 m² (art. 5-6).
- **Andere functie (art. 7):** bouw/sloopverhouding 1:3 (250-500 m²) of 1:4 (> 500 m²).
- **Sloopmeterregister (bijlage 2):** minimaal 150 m² per registratie, vijf jaar geldig, geen rechten, overdraagbaar; de gemeente brengt partijen alleen samen.
- **Kwaliteit en draagvlak (art. 8-9):** landschapsinrichtingsplan, advies van de Adviescommissie Omgevingskwaliteit (Het Oversticht), initiatiefnemer zorgt voor draagvlak.
- **Maatwerk (art. 10):** afwijking "in beginsel alleen [...] in ruil voor een [...] extra inspanning aan de omgevingskwaliteit"; genoemd worden onder meer tiny houses en mantelzorg.
- **Locatie (art. 6 lid 1):** "op de slooplocatie, dan wel op een locatie in een kern of buurtschap dan wel aan de rand van een kern of buurtschap". Een volledig nieuwe, onbebouwde locatie midden in het buitengebied valt er niet onder.
- **Geen geldformule:** de financiële koppeling is losgelaten (evaluatie p. 11). Er is geen apart KGO-kader en geen kwaliteitsfonds.

**Schaalgrens (B2) [INT]:** de regels voorzien in 1 of 2 compensatiewoningen per slooplocatie. Alternatieve woonvormen zijn "2 of meer wooneenheden binnen de maximale 750 m³"; of die 750 m³ per compensatiewoning geldt (dus 1.500 m³ bij twee) is niet expliciet. 10-12 woningen vergt maatwerk (art. 10) en een veel groter sloopvolume dan 2.000 m²; er is geen formule. Het grootste gerealiseerde precedent is **Varsenerweg 5a: 3 woningen op 2.700 m² sloop**, met als motivering: "Het plan past niet binnen het huidige Rood voor Roodbeleid, waardoor maatwerk nodig is. Voor het realiseren van de woningen is een aanvullende KGO inspanning en het feit dat het bedrijf een piekbelaster is meegewogen." (ruimtelijke motivering BiedtRuimte, 1-7-2025; Gmb 2026-57513).

**Provinciale verwijzing in de toelichting:** "De provincie neemt dit over in haar programmeringsafspraken met gemeenten waarbij na 2025 ook woningen die in het kader van Rood-voor-Rood in het buitengebied worden gerealiseerd mee gaan tellen in de programmeringsafspraken." En: "Met name in landbouwgebieden met generieke opgaven geldt dat de provincie hier de prioriteit legt bij het landbouwperspectief. In die gebieden gaat de provincie uit van een terughoudend beleid voor het faciliteren van VAB-beleid voor het ontwikkelen van woningen [...]. De provincie zet er op in om de woningen dan in en aan de rand van bevolkingsconcentraties te bouwen."

### 3.3 VAB-evaluatie en actualisatie (raad 29-1-2026; zaaknr. 1015373)
Bron: raadsvoorstel https://ommen.raadsinformatie.nl/document/16407378/2/Getekend+raadsvoorstel+besluit+1015373+geamendeerd; ontwerprapport https://openpub.ommen.nl/wp-content/uploads/2025/09/1.-Ontwerp-rapport-Evaluatie-en-Actualisatie-VAB-beleid-gemeente-Ommen.pdf (geraadpleegd 2026-10-06; circa 10.700 woorden, beschreven):
- 34 principeverzoeken Rood voor Rood 2021-augustus 2025; 11 vervolgtrajecten; 7 onherroepelijk vergund; 32 compensatiewoningen in 2021-2024, vrijwel allemaal één standaardwoning.
- Circa 350 agrarische bedrijven, waarvan 300 met veehouderij; "mogelijk 75 tot 100 bedrijven" stoppen de komende tien jaar.
- "Het huidige gemeentelijk VAB-beleid is vooral gericht op individuele beoordeling van gevallen [...]. Een individuele en vooral casuïstische benadering [...] schiet op de langere termijn mogelijk te kort. [...] Dit vraagt om het ontwikkelen van een beleidskader op gebiedsniveau." Dat kader komt in de Ontwikkelperspectieven.
- De Rood-voor-Rood-processen kennen volgens meerdere stakeholders "een lange doorlooptijd, zowel aan de voorkant als in de uitvoeringsfase". Ommen gebruikt minder VAB/Rood voor Rood dan buurgemeenten.
- Raad nam amendement A3 aan (sloopmeters van mestkelders en silo's tellen mee).

### 3.4 Gemeentelijke houding: signalen
**Open/bereid:** "We willen ons buitengebied nadrukkelijk niet op slot zetten" (omgevingsvisie); coalitieakkoord: "ruimte te bieden voor hergebruik van agrarische gebouwen voor wonen en natuur, de Rood voor Rood-regeling en ontwikkeling, woningsplitsing, visie Rood voor Groen-regeling"; een **plattelandscoach** (drie jaar, evaluatie na twee jaar; aanstelling niet gevonden); woningsplitsing buitengebied (CVDR745908; min. 200 m³ per woning).

**Terughoudend:**
- **Beerzerweg 36:** één compensatiewoning als "solitair gelegen woonerf": negatief principebesluit van het college op het locatiecriterium (art. 6), opiniërend besproken in de raadscommissie 18-6-2026 op verzoek van de LPO. Alleen de heroverwegingsnotitie van de initiatiefnemer (24-4-2026) is gelezen; de gemeentelijke motivering niet. Volgens de initiatiefnemer ziet de provincie "een opening [...] indien de compensatiewoning onderdeel vormt van het bestaande erf"; dit is een derdenstuk.
- **Beerzerweg 26** (raad 4-6-2026): erf in beschermd dorpsgezicht, maximaal 2 woningen: "Er zijn onvoldoende sloopmeters om te voldoen aan de Rood voor Rood regeling. Wel draagt de nieuwe woonfunctie bij aan het behoud van karakteristieke panden. Daarnaast wordt op basis van de Kwaliteitsimpuls Groene Omgeving [...] aanvullend geïnvesteerd in de ruimtelijke kwaliteit."
- **Beerzerpoort 1 en 6** (BOPA, raad 24-9-2026): drie wooneenheden op een erf van Landschap Overijssel; monumentencommissie "nog niet akkoord"; het raadsadvies is positief.
- Draagvlak in het landelijk gebied is verdeeld (inloopavond Ontwikkelperspectieven 16-6-2026, circa 100 bezoekers): "Behoud landelijke ruimte, geen nieuwe woonbestemmingen" naast "Het buitengebied is allang niet meer alleen agrarisch" (https://www.ommen.nl/wp-content/uploads/2026/07/260715-Verslag-inloopavond-DEF.pdf).

### 3.5 Concreet stappenplan en indicatieve doorlooptijd (E2)
Bronnen: https://www.ommen.nl/direct-regelen/wonen-en-leefomgeving/plannen/bestemmingsplannen/ (nog met "bestemmingsplan"-terminologie), de raadsstukken en [PB §4].

| Stap | Inhoud | Termijn | Opmerking |
|---|---|---|---|
| 0 | Informeel vooroverleg: Woonteam of afdeling Ruimte; ervenconsulent (Het Oversticht) en erfcoach bij agrarische erven | n.v.t. | gemeente@ommen.nl, 14 0529 |
| 1 | **Principeverzoek** aan het college; geen bezwaar/beroep | "8 tot 12 weken", "kan binnen 2 weken, maar ook pas na 2 jaar" | ommen.nl |
| 1a | Voorkantsamenwerking met de provincie en het waterschap (bij Beerzerveld via de Omgevingstafel IJsselland) | niet vastgelegd; provinciaal streven 4 weken [PB] | raadsvoorstellen |
| 2 | Overeenkomst initiatiefnemer-gemeente over leges, planschade en kosten | gelijktijdig | zie §11 |
| 3 | Initiatiefnemer laat omgevingsplanwijziging of BOPA-aanvraag opstellen: ruimtelijke onderbouwing, landschapsinrichtingsplan/ruimtelijk kwaliteitsplan, onderzoeken (stikstof, ecologie, water, bodem), verplichte participatie | maanden | |
| 4 | Raadsbehandeling; ontwerp 6 weken ter inzage; bij BOPA bindend raadsadvies | "ongeveer een half jaar" (ommen.nl); in de praktijk 11-14 maanden | Beerzerweg 26: ontwerp juli 2025, raad 4-6-2026 |
| 5 | Provinciale reactie; bij BOPA op de Lijst BOPA advies met instemming | 4-6 weken advies, 4 weken instemming [PB] | |
| 6 | Omgevingsvergunning bouwen (regulier 8 weken, verlengbaar met 6; uitgebreid circa 6 maanden) en eventueel Natura 2000-toestemming | 8 weken tot 6 maanden | |
| 7 | Onherroepelijk (beroep 6 weken); "reactieve aanwijzing van de provincie" kan de procedure verlengen (volgens ommen.nl) | 6 weken+ | |

Indicatieve totaaltijd uit eigen precedenten [BER]: Van Alewijkstraat (gemeentegrond, 34 woningen) van start omgevingsplanwijziging in mei 2024 tot raadsbesluit 10-7-2025 is circa 14 maanden, onherroepelijk 20-10-2025; Erven Benninck: ontwerp 14-4-2022, raad 14-7-2022.

### 3.6 Provinciale toets: wat de typologie in Ommen betekent (C1)
De nieuwe typologie van art. 4.123 staat in de provinciale verordening-viewer (document `55d637e6-8ff6-4083-a824-a0e77027a044`, in werking vanaf 1-7-2026; geraadpleegd 2026-10-11). Het deelonderzoek heeft de geometrie uit de document-JSON en de vector tiles doorgesneden met de gemeentegrens (GM0175, 18.201 ha) en gevalideerd: dezelfde procedure geeft voor het NNN 6.687 ha, tegenover 6.688 ha in de provinciale WFS; een onafhankelijke rasterbevraging (2.914 punten) geeft 41,4% en 17,0%.

| Overlay (verordening, geldend 1-7-2026) | ha | % van de gemeente |
|---|---|---|
| Landbouwgebied met **gebiedsspecifieke** opgaven en kansen voor water, klimaat en natuur | 7.575 | **41,6%** |
| Landbouwgebied met **generieke** opgaven en kansen | 3.066 | **16,8%** |
| Natuurnetwerk Nederland (NNN) | 6.687 | 36,7% |
| Natura 2000 (Vecht- en Beneden-Reggegebied; WFS) | 4.001 | 22,0% |
| Zeer kwetsbare natuurgebieden (stikstof) | 4.750 | 26,1% |
| Landgoed of buitenplaats | 4.479 | 24,6% |
| Grondwaterbeschermingszone | 1.563 | 8,6% |
| Intrekgebied | circa 4.029 | circa 22% |
| Overstroombaar gebied | 1.892 | 10,4% |
| Essenlandschap | 1.223 | 6,7% |
| Kernrandzone | 1.001 | 5,5% |

**Landbouwgrond** (BRP 2025, 9.287 ha) naar overlay [BER]: gebiedsspecifiek 60,2%; generiek 27,3%; Natura 2000 7,2%; NNN buiten Natura 2000 5,1%. De lagen overlappen.

**Rond de kernen (250 m-ring buiten de kern) [BER]:** Vinkenbuurt 100% generiek (geen NNN of Natura 2000 binnen 2 km). Alle andere kernen liggen overwegend in gebiedsspecifiek: Lemele 97% (intrekgebied 99%, essen 63%), Beerzerveld 99% (intrekgebied 72%), Witharen 48% gebiedsspecifiek + 12% generiek (grondwaterbeschermingszone 100%), Vilsteren 57% (landgoed 100%), Beerze 68% (Natura 2000 26%). Arriën en Dalmsholte zijn niet betrouwbaar af te bakenen.

**Projectlocaties [BER]:** Van Alewijkstraat gebiedsspecifiek + intrekgebied (Natura 2000 en NNN op 1,2 km); Vinkenbuurt generiek; Varsenerweg 5a gebiedsspecifiek + essen + overstroombaar (NNN 149 m); Beerzerweg 36 gebiedsspecifiek (Natura 2000 172 m, NNN 25 m). **Spotcontrole door de hoofdagent (2026-10-11):** de classificatie van Van Alewijkstraat (gebiedsspecifiek) en Koloniedijk 22a Vinkenbuurt (generiek) is herhaald met dezelfde geëxtraheerde lagen; dat is dus geen onafhankelijke herhaling van de geometrie-extractie.

**Lezing [INT]:** een nieuw Ommens project op agrarische grond valt vrijwel zeker in het gebiedsspecifieke type, waarvoor art. 4.11 lid 1 sub c (kwaliteitsinvestering gericht op natuur, water en klimaat) geldt. Het generieke type (art. 4.124 lid 1: geen nieuwe functies die de omliggende landbouw beperken) is het ongunstigste voor woningbouw. De Rood-voor-Rood-regels uit februari 2026 verwijzen nog naar de "Ontwerp provinciale omgevingsvisie", niet naar de definitieve artikelen.

### 3.7 Kansrijk vs. kansarm [INT]
| Kansrijker | Kansarmer |
|---|---|
| In of aansluitend aan een kern of buurtschap, behandeld als "uitleg van het dorp" met aantoonbare lokale behoefte | Solitair, in het open veenontginningsgebied ("de focus [ligt] op de agrarische productiemogelijkheden") |
| Bestaand erf met sloop (850/2.000 m²); terugbouwen in de kernrand | Onbebouwde agrarische grond zonder sloopmeters |
| Gemeentegrond en gemeentelijke regie (Beerzerveld, Vinkenbuurt) | Particulier initiatief buiten het woonprogramma |
| Starters en senioren met lokale binding; 30-40-30; CPO-vereniging | Vrije-sectorwoningen |
| Kleine schaal (1-4 woningen) of dorpsuitbreiding van 30-40 woningen met breed draagvlak | Tussenschaal van 10-12 woningen op eigen grond, zonder precedent |
| Landschapsplan, natuurinclusief, landschapsbeheer (Landschap Overijssel als partner) | Ligging in intrekgebied of nabij Natura 2000 zonder stikstofoplossing; netcongestie zonder plaats op de volgordelijst |

### 3.8 Eindoordeel per schaalscenario (gemeentelijke én provinciale laag)
| Scenario | Haalbaarheid in Ommen [INT] | Route en aandachtspunten |
|---|---|---|
| 1-2 woningen op bestaand agrarisch erf met sloop | **Kansrijk** | Rood voor Rood 2026 of VAB; Beerzerweg 26 laat zien dat ook zonder voldoende sloopmeters een kwaliteitsplan (KGO) mogelijk is |
| 3-6 woningen op bestaand erf (grote sloop, aan een kernrand) | **Mogelijk, maatwerk** | Varsenerweg 5a (3 woningen, 2.700 m² sloop) is de bovengrens in het precedent; raadsbesluit, bindend advies en provinciaal akkoord; CPO-vorm niet eerder getest |
| 10-12 woningen op bestaand erf of aansluitend aan een kern, particulier/CPO | **Kansarm tot mogelijk, onzeker** | Geen beleidskader; alleen als vraaggestuurde dorpsuitbreiding met aantoonbare lokale behoefte, raadsbesluit en inpassing in de woonafspraken (art. 4.15). Van Alewijkstraat (34) bewijst dat schaal mogelijk is, maar op gemeentegrond. Provinciaal vond Vinkenbuurt (buurtschap) 11 woningen "aan de forse kant" |
| 10-12 woningen op onbebouwde agrarische grond buiten een kern | **Zeer kansarm** | Geen regeling; ontginningsgebied is voor landbouw bestemd; provinciaal "nee, tenzij"; alleen via kernuitbreiding |

**Concrete vervolgstap (informeel voorgesprek):** mail het Woonteam (woonteam@ommen.nl of gemeente@ommen.nl, onderwerp "Woonteam – CPO buitengebied"; 14 0529) met verwijzing naar CPO Uitvoeringsregels §4 en vraag om een gesprek met de afdeling Ruimte. Vraag tegelijk naar de ambtelijk trekker van de nieuwe woonvisie, naar de Ontwikkelperspectieven (wethouder Rasenberg) en naar de plattelandscoach. Bij een concrete kern: het Plaatselijk Belang en de dorpsvisie.

---

## 4. VAB-beleid (Vrijkomende Agrarische Bebouwing)

### 4.1 Gemeentelijk VAB-beleid (D3)
Het VAB-beleid "bestaat uit twee elementen" (toelichting Rood voor Rood 2026):

> "De gemeente faciliteert vanuit het tijdelijk omgevingsplan het hergebruik van leegkomende agrarische gebouwen. Het betreft functies die passend zijn voor in het landelijk gebied. [...] De gemeente faciliteert met de Rood-voor-Rood beleidsregels dat leegstaande (landschap ontsierende) gebouwen onder bepaalde voorwaarden kunnen worden vervangen door nieuwbouw die wordt gebruikt voor een woonfunctie of voor een andere functie mist [sic] passend in het buitengebied."

- Er is **geen aparte VAB-beleidsregel** in CVDR. De regel in het moederplan Buitengebied (aantal woningen per erf, eisen aan omliggende bedrijven) is niet gelezen; herzieningen tonen "maximaal één woning per bouwvlak" tenzij een aanduiding een hoger aantal toestaat. Zie "Niet gevonden".
- Omliggende bedrijven: "altijd voorwaarde dat omliggende agrarische bedrijven nu en in de toekomst niet onevenredig in hun bedrijfsvoering mogen worden beperkt" (art. 11 toelichting).
- Woonprogrammering: "Via Rood voor Rood en nieuwe invulling van vrijkomende agrarische bebouwing maken we nieuwe woningen in het buitengebied mogelijk. We streven op deze manier maximaal zo'n 75 nieuwe woningen in het buitengebied." Na 2025 tellen compensatiewoningen mee in de woonafspraken en in de 30-40-30-eis.
- Precedenten op een voormalig agrarisch erf: Varsenerweg 5a (3), Beerzerweg 26 (2, raad 4-6-2026, Gmb 2026-325677), Witharenweg 17 (2 appartementen in een voormalige boerderij, verleend 19-11-2025). **Collectieve/cohousing-precedenten op een agrarisch erf in Ommen zijn niet gevonden.** Het enige CPO op een boerderij-erf is Erven Benninck in Lemele, binnen de kern en met woonbestemming.

### 4.2 Intergemeentelijk programma en subsidie 4.39 (D1)
Ommen doet niet mee aan een intergemeentelijk VAB- of erftransformatieprogramma en een aanvraag voor subsidie 4.39 is niet gevonden. De evaluatie zegt: "Daarmee lijkt het vooralsnog logischer de routekaart te koppelen aan de uitwerking van de nog op te stellen ontwikkelperspectieven [...]. We bezien daarbij of en hoe we [...] aanspraak kunnen maken op de mogelijkheden die de routekaart VAB- en erftransformatie programma's biedt." Subsidiebeschikkingen worden niet gepubliceerd; navraag bij vab@overijssel.nl of Overijssel Loket (038 499 88 99).

### 4.3 Erfcoach en provinciale ondersteuning (D2)
- Erfcoaches Hendry van Ittersum (Stimuland) en Yvonne In 't Veld zijn sinds 3-2-2025 actief voor een kosteloos keukentafelgesprek over erf, Rood voor Rood en VAB (https://www.ommen.nl/actueel/de-erfcoach-staat-voor-u-klaar).
- Vanaf 2026 loopt de ondersteuning via Boerenperspectief Overijssel (sociaal-economische begeleiders voor agrarische erven; erfcoaches voor niet-agrarische erven).
- De ervenconsulent/adviescommissie is Het Oversticht. Gebruik van Atelier Overijssel of de Rijkshandreiking erftransformaties is niet gevonden.

### 4.4 Ontwikkelperspectieven Landelijk Gebied (C2/B3)
Bron: https://www.ommen.nl/ontwikkelperspectieven-landelijk-gebied/ (2026-10-11). Planning: stap 1 gebieden/kansen/risico's "gereed juli 2026"; stap 2 keuzes verkennen "oktober 2026"; stap 3 concept en uitvoeringsprogramma "maart 2027"; **stap 4 vaststelling "mei 2027"**. Twee landschapstypen: het jonge ontginningslandschap en het oude cultuurlandschap. Hier worden ook de omvang van nieuw toe te voegen functies en deelgebieden voor VAB beslist. **Tot mei 2027 is er voor het buitengebied geen gebiedsvisie als bedoeld in art. 4.124 lid 4 [INT].**

---

## 5. Grondbeleid

### 5.1 Beleidslijn
Omgevingsvisie 2021 §3.5:

> "De gemeente hanteert als uitgangspunt een faciliterend en situationeel grondbeleid. Initiatieven voor ruimtelijke ontwikkelingen laten we zoveel mogelijk bij de markt liggen. [...] Daar waar de markt niet wil overgaan tot realisatie, bijvoorbeeld rond woningbouwontwikkeling voor specifieke doelgroepen, is eventueel een meer actieve rol voor de gemeente weggelegd."

**In de praktijk is het grondbeleid actief** op de woningbouwlocaties in Ommen en op de dorpsuitbreidingen Beerzerveld en Vinkenbuurt (eigen grondexploitaties; MJP Grondexploitaties 2026, raad 13-11-2025). Het Addendum 2023 adviseert strategisch bezit van circa 25% van het programma (circa 300 woningen).

- **Nota Grondbeleid:** dateert van 2012 en is online niet gevonden. Motie vreemd LPO (raad 27-11-2025, algemene stemmen): een "herziene Nota Grondbeleid [...] geactualiseerd naar de huidige wet-regeling en [...] voorzien van een afwegingskader" uiterlijk bij de begroting 2027. De Financiële verordening 2025 (art. 24) schrijft een nota ten minste eens per vier jaar voor.
- **Coalitieakkoord 2026-2030:** "Daarom kiezen we voor een actieve aanpak. Dat betekent dat we zelf gaan sturen op ruimtelijke ontwikkelingen en bekijken welk grondbeleid daarbij past."

### 5.2 Grondposities in het buitengebied
- Niet in exploitatie genomen gronden (MVA) bedroegen per 1-7-2025 € 0 (MJP 2026 §5.2). Er is dus geen apart strategisch grondbezit buiten de lopende exploitaties; **agrarische grond als voorraad is niet aangetroffen**.
- **Vlierlanden fase 3 / Gebied Arriën-Ommen** is een voormalig agrarisch uitleggebied: de gemeente kocht een centraal gelegen varkenshouderij (bouwclaimovereenkomst Bemog, 25-2-2025) en opende de grondexploitatie in mei 2025. Gebiedsvisie vastgesteld 8-5-2025 (375 woningen; GREX 300).
- **Van Alewijkstraat:** gemeentegrond van circa 1,2 ha (raadsbrief) tot 1,6 ha (ruimtelijke onderbouwing); grondexploitatie geopend 16-5-2024.
- **Erfpacht:** niet in gebruik; het coalitieakkoord wil het onderzoeken. Beerzerpoort kent erfpacht (5% van de grondwaarde) tussen Landschap Overijssel en bewoners (geen gemeente).

### 5.3 Grondprijzen
- **Grondprijsbrief:** jaarlijks door het college vastgesteld; de pagina https://www.ommen.nl/direct-regelen/ondernemen/grondprijzen/ verwijst naar de Grondprijsbrief 2025. De prijzen per m² zijn niet gelezen; een brief 2026 is niet teruggevonden.
- CPO-kavels: de grondprijsbrief is het uitgangspunt; "De definitieve grondprijzen worden vastgesteld in de gemeentelijke grondexploitatie".
- Voor agrarische grond die een derde omzet is geen gemeentelijke prijs gevonden; de gemeente verhaalt kosten via een overeenkomst (zie §11) [INT].

### 5.4 Actueel kavelaanbod (woneninommen.nl, 2026-10-06 en 2026-10-11)
| Locatie | Aantal | Prijs / oppervlakte | Status |
|---|---|---|---|
| Haven Oost, Ommen (vrije kavels) | projectpagina 5; nieuwsbericht mei 2026: "Nog één vrije kavel" | 522 m² (privé 185 m² + aandeel gezamenlijke tuin); € 191.000 excl. btw (€ 231.110 incl.) | 1 kavel beschikbaar (mei 2026) |
| Beerzerveld Van Alewijkstraat (vrije kavels) | 6 | prijzen niet gepubliceerd | bouwrijp december 2026; bouwstroom pas vanaf half april 2027 |
| Beerzerveld Schuurmanstraat 26b | 1 | 702 m²; € 235/m² excl. btw (€ 164.970 excl.) | in optie |
| Vlierlanden fase 2 | 2 kavels in optie (feb. 2025) | n.v.t. | projectpagina leeg |

Verkoop: betaald account € 50 per jaar, één punt per week; optie maximaal zes maanden, optievergoeding € 750 incl. btw; kavels incl. 21% btw, geen overdrachtsbelasting (FAQ woneninommen.nl).

### 5.5 Grote ontwikkellocaties met gemeentelijke grondpositie
| Locatie | Aantal | Planning | Collectief/CPO |
|---|---|---|---|
| Vlierlanden fase 3 | 375 (GREX 300) | stedenbouwkundig plan eind 2026; bouw 2028-2030 | geen CPO-reservering gevonden |
| Havengebied Oost | 109 (6 CPO-label) | deels gerealiseerd | CPO-label, niet als project teruggevonden |
| Erve Arriërflier | 45-50 | omgevingsplan doel halverwege 2026 | 8 CPO |
| Guido de Brès | 56-58 | raad 12-3-2026: GREX en opdracht omgevingsplan | CPO onderzoekt een deel van het hofje; "nog geen definitief besluit" |
| Julianaschool, Kardoen, Fluitekruid | 26 / 31 / 8 | planvorming 2025-2026 | geen CPO-label |
| Meerkoet | 6 | start bouw Q3/Q4 2025 | 100% CPO |
| Van Alewijkstraat Beerzerveld | 34 | bouwrijp dec. 2026 | 8 CPO-rijwoningen + 6 vrije kavels |
| Vinkenbuurt (voormalige school) | 8 | omgevingsplan doel Q3 2026 onherroepelijk | 7 CPO + 1 vrije kavel |

### 5.6 Plancapaciteit, woningbouwtempo en regionale opgave (A2)
- **Gerealiseerd:** Woondeal West-Overijssel (20-3-2025): Ommen 290 woningen Q1 2022-Q4 2024 [PB]; gemeentelijk: de voorraad groeide tussen 2021 en 2024 met circa 345 woningen.
- **Sleutelprojecten:** 2 projecten / 508 woningen 2024-2030 (Vlierlanden fase 3: 450 → 332; binnenstedelijke locaties 160 → 186); geen doorkijk 2031-2035.
- **Gemeentelijke plancapaciteit (Addendum 2023):** 865 gemeentelijk + 253 derden = 1.118 tegenover 1.250.
- **Planmonitor Wonen (provinciale WFS `B82_Harde_en_zachte_woningbouwplannen_vlakken`, peildatum 1-1-2026) [BER]:** 31 plannen, **238 woningen hard + 579 zacht = 817** nog te bouwen. Kleine initiatieven staan erin: Van Alewijkstraat 34 (hard), Erve Arriërflier 45 (zacht), Vinkenbuurt 8 (zacht), Meerkoet 6 (hard). Een CPO van 10-12 woningen telt dus mee zodra het gemeentelijk plan is geregistreerd; het hoeft geen sleutelproject (≥ 50) te zijn. De laag is geen sluitende bron (plannen zonder bekende locatie ontbreken).
- **80%/20%- en 130%-toets:** niet publiek te berekenen. Van Alewijkstraat onderbouwt dat 34 woningen "binnen de geldende afspraken" passen, hoewel het geen sleutelproject is. Er is geen post voor "initiatieven van derden"; de 253 niet-gemeentelijke locaties in het addendum zijn de enige post.
- **Buitengebied:** raming maximaal circa 75; Rood-voor-Rood-woningen tellen na 2025 mee in de programmeringsafspraken.

### 5.7 Volgordelijst woningbouwprojecten (netcongestie; versie 17-9-2026)
Bron: https://openpdc.ommen.nl/wp-content/uploads/2026/08/Definitieve-Volgordelijst-woningbouwprojecten-Ommen-2026-dd-17-september-2026.pdf (2026-10-11). 29 projecten; de gemeente biedt ze vanaf 1-10-2026 aan bij Enexis, dat de verdeling bepaalt ("Het kan daarom nog steeds meerdere jaren duren"). Onder meer positie 12 Kruispunt Bulmensteeg-Lemelerweg (CPO, Lemele, 8 woningen), positie 18 Vlierlanden Erve Arriërflier (CPO, 8 CPO, 24 sociale verhuur, 50 woningen), positie 23 Vlierlanden fase 3 (375), positie 27 Broekdijkje Ommen (479, start 2029). Van Alewijkstraat en Vinkenbuurt staan er niet op (reden niet vermeld).

**Gevolgen voor het concept [INT]:** (a) een nieuw initiatief na 10-9-2026 staat niet op de lijst en een volgende ronde is niet aangekondigd; (b) de rangorde volgt startdatum en projectrijpheid (onherroepelijk omgevingsplan of BOPA), waarop een CPO met een nog niet gewijzigd omgevingsplan laag scoort; (c) bij niet doorgaan kan Enexis kosten verrekenen met de aanbetaling van 20%.

---

## 6. Praktijkvoorbeelden 2024-2026

| # | Voorbeeld | Datum / besluit | Bron | Relevantie voor het concept |
|---|---|---|---|---|
| 1 | **Van Alewijkstraat Beerzerveld:** 34 woningen (25 rij, 6 twee-onder-een-kap, 3 vrijstaand; 35% sociaal, 38% midden, 27% vrij) op agrarisch perceel aansluitend aan de kern, inclusief 8 CPO en 6 vrije kavels | GREX 16-5-2024; TAM-omgevingsplan raad 10-7-2025; onherroepelijk 20-10-2025 | RIS zaak 592651/942210; ommen.nl 22-7-2025 | **Dé referentie voor meer dan 10 woningen op agrarische grond:** "uitleg van dorpen" (art. 4.5 lid 3), KGO "niet bedoeld voor situaties van stadsuitleg", binnen woonafspraken (art. 4.15). Wel gemeentegrond en gemeentelijke regie. Plan is besproken in de Omgevingstafel IJsselland |
| 2 | **Vinkenbuurt (oude school):** 8 woningen, 7 via CPO (eerst 11, daarna 13 bij verplaatsing buurthuis, teruggebracht tot 8) | raad 30-1-2025; college 1-2026; inschrijving t/m 18-2-2026 | woneninommen.nl; memo herzien stedenbouwkundig ontwerp | **Sterkste lokale signaal dat 10-13 woningen in een buurtschap provinciaal gevoelig ligt.** Het centrumplan was in 2021 al door de provincie afgewezen om het ruimtelijk ontwerp |
| 3 | **Erve Arriërflier:** 45-50 woningen, 8 CPO | raad 27-2-2025 (GREX); samenwerkingsovereenkomst 4-3-2026 | RIS 827238 | Collectief binnen een groter gemeentelijk project |
| 4 | **De Meerkoet:** 6 CPO-woningen (7 starters) | koopovereenkomst 11-12-2024 | ommen.nl 20-12-2024 | Eerste CPO onder de nieuwe regels; "We hopen dat dit meer mensen inspireert zelfstandig nieuwe woningen te ontwikkelen" (wethouder) |
| 5 | **Varsenerweg 5a:** 3 woningen op 2.700 m² sloop (piekbelaster) | TAM raad 29-1-2026; Gmb 2026-57513 | ruimtelijkeplannen.nl NL.IMRO.0175.2025TAMOP0001-VG01 | Maatwerk boven de 2 woningen; provincie: "past in het provinciaal beleid"; kostenverhaal via planschadeovereenkomst |
| 6 | **Beerzerweg 26:** 2 woningen op erf in beschermd dorpsgezicht | raad 4-6-2026 | RIS 1040779 | Zonder voldoende sloopmeters wel KGO-kwaliteitsplan; provincie en waterschap "in te kunnen stemmen" |
| 7 | **Beerzerweg 36:** 1 compensatiewoning als solitair woonerf | negatief principebesluit; commissie 18-6-2026 | RIS (LPO-rondvraag 21-5-2026) | Strikte lezing van het locatiecriterium |
| 8 | **Beerzerpoort 1 en 6:** drie wooneenheden, BOPA | raad 24-9-2026 | RIS 1069381 | BOPA-route; provincie: "kwaliteitswinst [...] KGO"; aparte natuurtoestemming nodig |
| 9 | **Gravendijk Vilsteren:** 4 kwadrantwoningen op onbebouwd perceel in de kern | BOPA, positief bindend advies 24-9-2026 | RIS 1070870 | BOPA in een kleine kern; geen verwijzing naar de provincie in de stukken |
| 10 | **Stedenbouwkundige visie Lemele:** circa 80 woningen tot 2031; uitbreiding naast inbreiding | raad 12-3-2026 | RIS 1039738 | "De provincie Overijssel is terughoudend als het gaat om uitbreidingslocaties van dorpen als Lemele [...]. Uitgangspunt is dan ook dat inbreiding vóór uitbreiding gaat. Maar daarmee kan niet in de volledige woningbehoefte worden voorzien." (Vechtdal Centraal 3/2026, citaat uit de visie) |
| 11 | **Lemelerweg 36-40, Lemele:** circa 35 woningen als "passend" gekwalificeerd | beantwoording principeverzoek 9-7-2024 | Reactienotitie SV Lemele | Mede gebaseerd op een provinciale reactie op het principeverzoek |
| 12 | **Pilot Bouwstenen kleine kernen en buurtschappen Ommen** (provincie, gemeente, Ruimtevolk; niet vastgesteld) | augustus 2023; bijlage 3 SV Lemele | RIS 16636690 **[OCR]** | Kernen Lemele/Beerzerveld "Ja"; buurtschappen alleen enkele woningen via Rood voor Rood; Witharen en NNN/drinkwatergebieden terughoudend; natuur en water "Geen" |
| 13 | **Vlierlanden fase 3:** gemeente koopt varkenshouderij voor 375 woningen | 25-2-2025; gebiedsvisie 8-5-2025 | ommen.nl 27-2-2025 | Omzetting agrarisch bedrijf naar woongebied op stadsrandschaal; politiek omstreden (Arriën); stikstofrisico |
| 14 | **Netcongestie:** Enexis meldt Ommen Dante (MS-netdelen 1 en 5, afname) als nieuw knelpunt | update 16-7-2026 | enexis.nl | Beerzerveld: bouwstroom pas half april 2027 (6-9 maanden vertraging [BER]) |
| 15 | **Stikstof:** kabinetspakket 26-6-2026, trekkerprotest 10-8-2026, regionale brief 9-9-2026 (Ommen, Dalfsen, Hardenberg, Staphorst, Zwartewaterland) | 2026 | ommen.nl; Stadindex | De brief noemt het weer op gang brengen van vergunningverlening voor woningbouw als gedeeld doel |
| 16 | **Bermerstraat 1 Ommen:** bestemmingsplan op 24-10-2024 niet vastgesteld, daarna BOPA met bindend advies | 12-3-2026 | RIS 714643/1039724 | De raad kan een plan afwijzen; sinds 2026 loopt het via bindend adviesrecht |

---

## 7. Inventarisatie bestaande initiatieven

| Initiatief | Woningen | Locatie/grond | Status (2026-10-11) | Relevantie |
|---|---|---|---|---|
| **CPO LemeleWoont** (eerste Ommense CPO) | 4 (twee-onder-een-kappers) | Lemele, inbreidingslocatie | Verkocht 2022, bouw gestart 2022 | Eerste CPO; gemeentegrond |
| **CPO Lemele / Erven Benninck** | 6 senioren (hof) → 8 nieuwe eenheden + boerderij | Lemele, erf met woonbestemming binnen de kern | Bestemmingsplan raad 14-7-2022; vergunning 1-2-2023; uitvoering niet vastgesteld | **Enige CPO op een boerderij-erf**, maar binnen de kern |
| **Kruispunt Bulmensteeg-Lemelerweg (CPO)** | 8 | Lemele | Volgordelijst positie 12 | Opvolger CPO Lemele Woont |
| **CPO De Meerkoet** (Starters Collectief Ommen) | 6 (7 leden) | Ommen, gemeentegrond | Koopovereenkomst 11-12-2024; start bouw Q3/Q4 2025 (verloop niet gelezen) | Schaalt niet naar 10-12 |
| **CPO Erve Arriërflier** | 8 | Ommen, Vlierlanden fase 2, gemeentegrond | Samenwerkingsovereenkomst 4-3-2026; omgevingsplan doel halverwege 2026 | Collectief binnen groter project |
| **Vereniging CPO Beerzerveld** | 8 rijwoningen | Beerzerveld, gemeentegrond uit het 34-woningenplan | Samenwerkingsovereenkomst 20-8-2025; bouwrijp dec. 2026 | CPO in een kleine kern, in uitleg aan de kern |
| **Vereniging CPO Vinkenbuurt** | 7 + 1 vrije kavel | Vinkenbuurt, voormalige OBS | Samenwerkingsovereenkomst 4-3-2026; omgevingsplan doel Q3 2026 | CPO in een buurtschap; zie provinciale reactie |
| **CPO Guido de Brès** (onderzoek) | deel van het hofje (van 58) | Ommen | "nog geen definitief besluit" | Geen toezegging |
| **Havengebied Oost** (6 CPO-label) | 6 van 109 | Ommen | CPO-label in addendum; niet als project teruggevonden | Onzeker |
| **Starters Collectief Ommen** | koepel | n.v.t. | Actief kennisplatform | Aanspreekpunt voor ervaringen |
| **Kleinschalige woongroep Kerkplein 16** | onbekend | Ommen | Vergunning 11-9-2024 (Gmb 2024-377602) | Niet verder onderzocht |
| **Haven Oost hofwoningen / Hof van Vlierlanden** | 11+4 / 20+12 | Ommen | Gebouwd; corporatie resp. ontwikkelaar | Geen CPO; collectief hof |
| **Flexwoningen Sportlaan** | 50 | Ommen | Eerste 17 opgeleverd 5-10-2026 | Experimentele woonvorm, geen CPO |
| *Collectief op een voormalig agrarisch erf (vergelijkbaar met BuitenDelen, Lettele)* | n.v.t. | in Ommen niet gevonden | n.v.t. | Dichtst bij: Beerzerpoort (3 wooneenheden) en Beerzerweg 26 (2) |

Een cohousing- of knarrenhof-initiatief van burgers is niet gevonden.

---

## 8. Huisvestingsverordening
- **Aanwezig: nee.** Geen huisvestingsverordening, urgentieregeling of doelgroepenverordening in CVDR (477 nummers) of Gemeenteblad. Het woonprogramma beschrijft de instrumenten alleen als verkenning.
- **Plannen:** coalitieakkoord 2026-2030: "Binnen de kaders van de Huisvestingswet stellen wij een huisvestingsverordening op, zodat er meer voorrang kan worden gegeven aan woningzoekenden met aantoonbare binding met onze gemeente." en een "lokale voorrangsregeling [...] bij de toewijzing van woningen en bouwkavels". Er is nog geen ontwerp; het nieuwe uitvoeringsprogramma (CUP) is gepland voor oktober 2026 (Kaderbrief 2027-2030).
- **Minimum sociale huur:** niet via verordening. Beleid: coalitieakkoord "Nieuwbouw moet voor minimaal 30% uit sociale huur bestaan"; Addendum 30-40-30; streefprogramma woonprogramma 15% sociale huur / 15% goedkope koop / 5% middenhuur / 65% middelduur en duur, in de praktijk ingehaald door het addendum. Amendement A1 bij de visie Lemele (12-3-2026): de verdeling "is van toepassing op het gehele grondgebied van de gemeente Ommen. Per locatie kan de verdeling er anders uitzien".
- **Lokale binding:** nu via uitgiftecriteria (CPO-regels) en de starterslening (CVDR679031; max. € 30.000 tot de NHG-grens).
- De Regiewet vraagt een huisvestingsverordening uiterlijk 1-1-2028 [PB, primaire bron Staatsblad].

---

## 9. Zelfbouwloket / contactpersoon
- **Geen zelfbouwloket onder die naam.** De gemeente werkt met het platform Wonen in Ommen (https://woneninommen.nl) en een "Woonteam": "Vult u dan het contactformulier in of stuur een mail naar gemeente@ommen.nl onder vermelding van 'Woonteam'". Op woneninommen.nl/contact staat woonteam@ommen.nl. Telefoon 14 0529; Chevalleraustraat 2, 7731 EE Ommen; Postbus 100, 7730 AC Ommen.
- **Wethouder Volkshuisvesting/wonen en RO (incl. omgevingsplannen):** Alice van den Nieuwboer (CDA), 2e loco-burgemeester. **Ontwikkelperspectieven landelijk gebied, vitale kernen, gemeentelijke eigendommen, plattelandsontwikkeling:** Sonja Rasenberg (PRO Ommen).
- **Omgevingsvisie/omgevingsplan:** Henk van Kessel (henk.vankessel@ommen.nl; genoemd op de omgevingsvisie-pagina); Ontwikkelperspectieven: gemeente@ommen.nl t.a.v. "Ontwikkelperspectieven landelijk gebied".
- **Erfcoach:** Hendry van Ittersum (Stimuland, hvanittersum@stimuland.nl) volgens https://www.ommen.nl/direct-regelen/ondernemen/landelijk-gebied/persoonlijke-begeleiding-op-uw-erf/.
- **Netcapaciteit woningbouw:** eerderaanvragen@ommen.nl (termijn 10-9-2026 verstreken).
- **CPO-projectleiders per locatie:** namen niet publiek gevonden.

---

## 10. Bestuurlijk klimaat

### 10.1 Is er een coalitie in vorming? Nee.
Gecontroleerd op 2026-10-06 en 2026-10-11 (ommen.nl/actueel tot en met 5-10-2026, Vechtdal Centraal, RTV Vechtdal, De Toren): de formatie is afgerond, het college is op 2-7-2026 geïnstalleerd en er is geen tussentijdse val, fractiebreuk of heropende formatie gevonden. Wel loopt een los daarvan staande **burgemeestersprocedure**: burgemeester Hans Vroomen (CDA) is per 10-4-2026 eervol ontslagen; Annemiek Jetten (PvdA) is per 16-4-2026 waarnemend burgemeester; de raad had een vertrouwenscommissie (CVDR764217, 14-7-2026). Een aanbeveling stond volgens de gemeentesite gepland voor de raadsvergadering van 8-10-2026; de uitkomst is niet gevonden.

### 10.2 Uitslag en zetelverdeling (gemeenteraadsverkiezingen maart 2026)
Bron: https://www.ommen.nl/actueel/definitieve-uitslag-gemeenteraadsverkiezingen-2026/ (26-3-2026): 15.453 stemgerechtigden, 10.114 stemmen, opkomst 65,45%.

| Partij | Stemmen | Zetels |
|---|---|---|
| VOV-Ommen | 3.076 | 5 |
| CDA | 2.179 | 4 |
| LPO | 1.381 | 2 |
| ChristenUnie | 1.279 | 2 |
| GroenLinks/PvdA = **PRO Ommen** [INT] | 933 | 2 |
| VVD | 674 | 1 |
| D66 | 548 | 1 |

Coalitie VOV + CDA + PRO Ommen = 11 van 17 zetels [BER]; oppositie LPO (2), ChristenUnie (2), VVD (1), D66 (1).

### 10.3 Formatieverloop
| Datum | Gebeurtenis |
|---|---|
| 26-3-2026 | Definitieve uitslag; VOV draagt oud-minister Frank de Grave voor als verkenner |
| 7-4-2026 | Openbare bespreking verkennersadvies (advies zelf niet gevonden) |
| begin april 2026 | Onderhandelingen VOV, CDA, PRO Ommen |
| 2-6-2026 | Overeenstemming op hoofdlijnen; kandidaat-wethouders De Koff, Van den Nieuwboer, Rasenberg |
| 26-6-2026 | Akkoord "Krachtige keuzes voor een verbonden samenleving" definitief vastgesteld |
| 1-7-2026 | Afscheid wethouders Bongers (LPO) en Boerman (ChristenUnie) |
| 2-7-2026 | Installatie nieuw college in extra raadsvergadering |

### 10.4 College (benoemd 2-7-2026)
- **René de Koff (VOV), 1e loco:** financiën, economie incl. centrum en landbouw (agrarisch), recreatie, verkeer, openbare ruimte.
- **Alice van den Nieuwboer (CDA), 2e loco:** Ruimtelijke Ordening (inclusief omgevingsplannen), Volkshuisvesting, wonen, (jeugd)zorg en meer. Zij deed ook in 2022-2026 Wonen en zette het CPO-beleid mee op; haar combinatie met Ruimtelijke Ordening is nieuw.
- **Sonja Rasenberg (PRO Ommen), 3e loco:** vitale kernen, gemeentelijke eigendommen, ontwikkelperspectieven landelijk gebied, plattelandsontwikkeling landbouw, duurzaamheid/natuur/water.
- Vorig college (2022-2026): LPO, CDA, ChristenUnie; akkoord "Bouwen aan de toekomst" (7-6-2022) met "Ruimte bieden voor woningbouw in de kernen via onder meer CPO" en "Continueren erfcoaches".

### 10.5 Coalitieakkoord 2026-2030: relevante passages
Bron: https://openpub.ommen.nl/wp-content/uploads/2026/06/Coalitieakkoord-Ommen-2026-2030.pdf (36 p.; geraadpleegd 2026-10-06/11; tweekoloms PDF, per kolom geëxtraheerd).

> "Verruimen instrumentarium. Op korte termijn gaan we onderzoeken of het instrumentarium van de gemeente kan worden verruimd. [...] Ook in het koopsegment gaan wij onderzoeken of het instrumentarium verder kan worden ingezet met bijvoorbeeld: startersleningen; erfpacht; anti-speculatiebeding; leegstandsheffing; zelfbewoningsplicht; inzet op collectief particulier opdrachtgeverschap."

> "We willen meer mogelijkheden voor woningsplitsing en maatwerk. Nieuwbouw moet voor minimaal 30% uit sociale huur bestaan en aansluiten bij de vraag in gemeente Ommen."

> "Samen met de raad werken we aan een vernieuwde woonvisie met meer ambitie. [...] het versnellen en (langdurig) verhogen van de bouwproductie; de vorming van meer wijken met een mix van woningtypes; [...]"

> "Ook moet er ruimte zijn voor woningbouwontwikkeling naar behoefte in de kernen. Hierbij zetten we vooral in op starters- en seniorenwoningen."

> "Dat doen we door: [...] ruimte te bieden voor hergebruik van agrarische gebouwen voor wonen en natuur, de Rood voor Rood-regeling en ontwikkeling, woningsplitsing, visie Rood voor Groen-regeling; [...]"

> "In de omgevingsplannen willen wij ruimte bieden aan off-gridmogelijkheden bij de realisatie van nieuwe woonprojecten."

> "Wij hechten grote waarde aan sterke en leefbare dorpen [...]. De coalitie ziet Plaatselijke Belangen daarom als volwaardige gesprekspartner bij ontwikkelingen in de dorpen."

**Duiding [INT]:** het akkoord is kerngericht voor nieuwbouw en erf-/sloopgericht voor het buitengebied. Het bevat **geen** doelstelling voor nieuwe woningen op onbebouwde agrarische grond en geen passage over een cluster van 10-12 woningen. De financiële ruimte voor nieuw beleid is beperkt (begroting 2027 "een begroting bestaand beleid"; structurele tekorten volgens de financiële foto van mei 2026).

### 10.6 Partijstandpunten
- **VOV** (grootste partij; programma 2026): "Ruimte voor nieuwe woonvormen (CPO, tiny houses, splitsen)"; "Uitbreiding in kernen én buitengebied"; "Daarnaast dienen wij te kijken of meer CPO-projecten mogelijk zijn"; steunt Rood voor Rood.
- **VVD** (oppositie): wil 2.000 woningen tot 2040 in plaats van 1.250; "Per kern 25 extra startersplekken in 12 maanden [...] Er zijn al enkele locaties aangemerkt als toekomstige uitbreidingslocaties in buitengebied"; stemde als enige tegen het Lemele-amendement over CPO-regie.
- CDA, PRO Ommen, LPO, ChristenUnie en D66: programma's niet gelezen.

### 10.7 Politieke duiding voor CPO [INT]
De CPO-lijn heeft brede steun (motie 2022 en addendum 2023 met algemene stemmen) en de bestuurder die het dossier opzette zit nog in het college. De ChristenUnie, initiatiefnemer van de motie, en de LPO zitten nu in de oppositie. De ruimte is **groot voor CPO op gemeentegrond in of aan de kernen** en **beperkt voor CPO op agrarische grond buiten de kernen**. Het meest kansrijke venster is de nieuwe woonvisie en de Ontwikkelperspectieven (mei 2027), waarin wethouder Rasenberg deelgebieden en schaal kiest. Vlierlanden fase 3 (375 woningen) is politiek omstreden vanwege Arriën.

---

## 11. Kostenverhaal en leges

### 11.1 Kostenverhaal
- **Geen nota kostenverhaal, geen exploitatieplan-beleid en geen kostenverhaalsverordening** in CVDR of RIS. Per geval: "Daarnaast sluiten wij met iedere initiatiefnemer een overeenkomst om zaken te regelen die samenhangen met de herziening van het bestemmingsplan. Denk aan de leges, planschade en eventuele civieltechnische aanpassingen als gevolg van uw plan." (ommen.nl)
- Praktijk: *planschade-/kostenverhaalsovereenkomst*. Varsenerweg 5a: "Het is niet nodig een exploitatieplan vast te stellen omdat het kostenverhaal met een planschadeovereenkomst is geregeld." Beerzerweg 26: de overeenkomst verzekert dat "het risico op nadeelcompensatie voor rekening van de initiatiefnemer komt. De gemeentelijke kosten zijn hier ook in opgenomen."
- Grotere ontwikkelingen op particuliere grond (Lemele): "zal de gemeente Ommen een anterieure overeenkomst met de ontwikkelende partijen sluiten om afspraken te maken over typologieën, bebouwing/doelgroep, fasering, aanleg van voorzieningen."
- **Kwaliteitsinvestering (KGO):** geborgd in de regels van het omgevingsplan (ruimtelijk kwaliteitsplan/erfinrichtingsplan); bij Beerzerpoort via erfpacht en sanering. Geen kwaliteitsfonds; bankgarantie niet aangetroffen.
- **Nadeelcompensatie:** € 300 per aanvraag (CVDR712088).
- **CPO zonder gemeentegrond:** anterieure overeenkomst voor het CPO-fonds (zie §1.4).

### 11.2 Leges 2026 (CVDR753504)
Bron: https://lokaleregelgeving.overheid.nl/CVDR753504 (2026-10-06).

| Onderdeel | Tarief |
|---|---|
| **Wijzigen omgevingsplan op aanvraag (art. 2.45 lid 1)** | € 9.845,30, "Hierbij worden de door de gemeente [...] ter zake verschuldigde kosten voor voorbereiding van dat omgevingsplan, inclusief die van noodzakelijke (voor)-onderzoeken, eveneens in rekening gebracht bij aanvrager" (begroting vooraf; intrekken binnen vijf werkdagen mogelijk) |
| BOPA die niet voldoet aan bijlage 1 (art. 2.6 lid 5) | € 7.845,30 (kleine BOPA € 434,50; binnenplans € 434,50) |
| Omgevingsplanactiviteit zonder bouwactiviteit (art. 2.45 lid 2) | € 9.845,30 |
| Bouwactiviteit ruimtelijk deel (art. 2.6), bouwkosten > € 1.000.000 | € 16.006,30 + 0,87% over het meerdere |
| Bouwactiviteit technisch deel (art. 2.5), bouwkosten > € 1.000.000 | € 8.520,65 + 0,46% over het meerdere (maximum € 250.000) |
| Toets ruimtelijk kwaliteitsplan/erfinrichtingsplan (art. 2.7) | + € 518,15 |
| Uitgebreide voorbereidingsprocedure (art. 2.48) | € 2.390,15 |
| Advies gemeenteraad (art. 2.50 lid 1a) | € 253,80 |
| Omgevingsoverleg (art. 2.4) | € 341,60 (100% verrekend bij een aanvraag binnen 12 maanden) |

**Indicatie voor 12 woningen à € 250.000 [BER]:** de bouwleges (art. 2.5 + 2.6 lid 1 over € 3 mln bouwkosten) komen op circa € 51.100, met lid 5, RKP, uitgebreide procedure en raadsadvies op circa **€ 62.100**, exclusief welstand, onderzoeken, provinciale kosten en de gemeentelijke kosten bij een omgevingsplanwijziging (€ 9.845,30 + begroting). Of art. 2.6 lid 1 en lid 5 cumuleren is in de tekst niet eenduidig, en het welstandstarief is afgebroken in de gepubliceerde tekst. Legesverordening 2027 is nog niet gepubliceerd.

---

## 12. Woningbehoefte en doelgroepen

### 12.1 Kwantitatief en kwalitatief
- **Kern Ommen:** 1.250 woningen tot 2040/2030; Addendum: 750 koop / 500 huur; sociale huur 375 (30%), vrije huur 125 (10%), koop tot € 250.000 18%, € 250-355.000 18%, € 355-500.000 16%, boven € 500.000 8%. "Het accent op rijwoningen"; "levensloopbestendig wonen, grondgebonden – al dan niet in gemeenschapsvorm" is nieuw en te weinig aanwezig.
- **Markt:** "Vergeleken met Dalfsen en Hardenberg heeft ook Ommen opvallend weinig aanbod. Doorstroming is er ook weinig." Slaagkans huurwoning gemiddeld 5% (jongeren 3%); Vechtdal Wonen wil ruim 400 woningen bouwen.
- **Kleine kernen:** 50-100 woningen vraaggestuurd; Lemele circa 50-80 tot 2031 (woningbehoefteonderzoek 2024, alleen geciteerd); Beerzerveld 34; Vinkenbuurt 8; Witharen 11-17.
- **Betaalbaarheidsgrens:** € 355.000 en € 1.000 huur (addendum 2023); € 390.000 en € 1.157,95 (MJP 2026); de college-opgave van 16-4-2025 noemt € 405.000 en € 1.184,82 [WF/RTV Vechtdal].
- **Woonzorg:** de Woonzorgvisie is in voorbereiding (Companen, raadsinformatiebijeenkomst 11-6-2026); omgevingsvisie: het woonzorgaanbod wordt "vooral in de kern Ommen gerealiseerd"; geclusterd: Hof van Vlierlanden (20 hofwoningen), Haven Oost stadshof, CPO Lemele-hof (6 senioren), Prinses Julianastraat 8 (30 sociale-huurappartementen voor senioren).

### 12.2 Sluit CPO aan? [INT]
- **Ja voor het doelgroepprofiel:** starters en senioren met lokale binding, betaalbaar tot de NHG-grens, grondgebonden rij- of hofwoningen met gemeenschappelijke tuin.
- **Nee/beperkt voor ligging en schaal buiten de kern:** de gemeente wil het grootste deel in de kern Ommen, de kleine kernen vraaggestuurd en het buitengebied maximaal circa 75 via Rood voor Rood. Een CPO van 10-12 woningen past kwantitatief in de totaalopgave maar niet in de gekozen spreiding, tenzij het wordt behandeld als vraaggestuurde dorpsuitbreiding bij een kleine kern met aantoonbare lokale behoefte (Plaatselijk Belang, dorpsvisie), zoals Beerzerveld en Lemele. De woningsplitsingsnotitie zegt zelf dat het buitengebied voor senioren "naar zijn aard minder geschikt" is.

---

## Twee kernvragen

### 1. Wonen in het buitengebied: ruimte voor een cluster van 10-12 woningen buiten de bestaande woonkernen?
- **(a) Gemeentelijk beleid.** Nee, niet als aparte categorie. Buiten kernen en buurtschappen is alleen Rood voor Rood/VAB en woningsplitsing beschikbaar, met standaard maximaal twee woningen per slooplocatie en een raming van circa 75 woningen in totaal. Het grootste precedent is drie woningen (Varsenerweg 5a). Het beleid is wel open voor vraaggestuurde dorpsuitbreiding aansluitend aan een kern (Beerzerveld 34 woningen), kleine kernen 50-100 woningen en CPO's van 4-8 woningen op gemeentegrond.
- **(b) Provinciaal kader.** Ommen is "overige kern" (art. 4.4: alleen lokale behoefte en bijzondere doelgroepen). Nieuwe woningen moeten passen binnen de Woondeal West-Overijssel (art. 4.14-4.15); een CPO van 10-12 woningen telt als zacht/hard plan mee in de Planmonitor. De provincie toetst buiten bestaand bebouwd gebied aan het concentratiebeginsel, de redeneerlijn en de KGO; in de Ommense dossiers stemt zij steeds in, maar was zij informeel terughoudend bij 11 woningen in de buurtschap Vinkenbuurt en bij uitbreidingslocaties in Lemele. Natura 2000 (22,0%), NNN (36,7%) en intrekgebieden (circa 22%) beperken de locatiekeuze.
- **(c) Gecombineerd eindoordeel.** Een cluster van 10-12 woningen **buiten** de kernen is **zeer kansarm**. **Aansluitend aan een kern** is het **kansarm tot mogelijk, onzeker**: het kan alleen als vraaggestuurde uitbreiding met lokale behoefte, raadsbesluit en binnen de woonafspraken, bij voorkeur in een kern met voldoende omvang (Lemele, Beerzerveld) en niet in generiek of landgoed-/NNN-rijke omgeving. Belangrijkste onzekerheden: de nieuwe woonvisie en het volkshuisvestingsprogramma, de Ontwikkelperspectieven (mei 2027), de provinciale houding bij een concreet plan, netcongestie en stikstof.

### 2. Agrarische herbestemming: ruimte voor omzetting van agrarisch bestemde grond naar bouw- of woonfunctie op deze schaal?
- **(a) Gemeentelijk beleid.** Beperkt. Voor omzetting met sloop van bestaande agrarische bebouwing biedt Rood voor Rood 2026 een expliciete rekenregel (850 m² = 1 woning, 2.000 m² = 2, korting bij sociale huur en kernrand). Voor omzetting van onbebouwde agrarische grond bestaat geen regeling; dat gebeurt alleen bij kernuitbreiding op gemeentelijke regie. De gemeente kocht zelf agrarische grond (een varkenshouderij) voor Vlierlanden fase 3.
- **(b) Provinciaal kader.** Voor landbouwgebied met gebiedsspecifieke opgaven (60,2% van de Ommense landbouwgrond) is art. 4.11 lid 1 sub c (KGO gericht op natuur, water en klimaat) van toepassing; in het generieke type (27,3%, vooral rond Vinkenbuurt) geldt art. 4.124 lid 1 (geen beperking van omliggende landbouw) en "nee, tenzij". Er is geen provinciale rekenformule. Er is geen gebiedsvisie gevonden voor de afwijkingsroute van art. 4.124 lid 4; de zes provinciale gebiedsprocessen in het Vechtdal liggen geheel of gedeeltelijk in Ommen. Een BOPA voor 10 of meer nieuwe woningen vereist provinciale instemming.
- **(c) Gecombineerd eindoordeel.** Omzetting van **bestaand agrarisch erf met sloop** naar 1-3 woningen is kansrijk tot mogelijk. Omzetting van **onbebouwde agrarische grond** naar 10-12 woningen is zeer kansarm; aansluitend aan een kern en op basis van aantoonbare lokale behoefte is het kansarm tot mogelijk. Belangrijkste onzekerheden: de uitkomst van de Ontwikkelperspectieven, de regel uit het tijdelijk omgevingsplan Buitengebied (niet gelezen), de wijze waarop de provincie de nieuwe typologie bij een concreet plan toepast en de stikstofsituatie.

---

## Overijssel-controlepunten (Bijlage A)

| # | Controlepunt | Bevinding | Status | Bron (URL) / raadpleging |
|---|---|---|---|---|
| **A1** | Positie concentratiebeginsel; groeiprofiel | "Overige kern" (art. 4.4) [PB]. Gemeente: "Centraal Wonen" in de Woonagenda; bijdrage Regio Zwolle tot "2.000+ woningen tot 2040", door de raad begrensd op 1.250. Provinciaal VHP-ontwerp rekent Ommen tot woningbouwregio West-Overijssel (Prb 2026-11834). Eigen groeiprofiel kleine kernen: niet gevonden | gevonden; groeiprofiel Strategieboek niet geverifieerd | omgevingsvisie p. 15-26; Woondeal Bijlage 1; zoek.officielebekendmakingen.nl/prb-2026-11834.html; 2026-10-06/11 |
| **A2** | Woonregio, woonafspraken, plancapaciteit, 80/20, CPO-telling | West-Overijssel; 290 gerealiseerd 2022-2024; 2 sleutelprojecten / 508 woningen; geen doorkijk 2031-2035. Planmonitor 1-1-2026: 817 woningen (238 hard + 579 zacht); kleine initiatieven/CPO's (34, 45, 8, 6) zijn geregistreerd. 80/20- en 130%-toets niet publiek berekend. Rood voor Rood telt na 2025 mee | gevonden (aantallen); toets niet gevonden | WFS B82 (geoserver.overijssel); Woondeal; toelichting RvR; 2026-10-06/11. Navraag: woonaanpak@overijssel.nl, gemeente (Planregistratie) |
| **A3** | 30-40-30, CPO, kleine kernen, prestatieafspraken | 30-40-30 gemeentebreed gemonitord (A1 SV Lemele), niet per CPO-project verplicht; grenzen € 355.000/€ 1.000 (2023), € 390.000/€ 1.157,95 (MJP 2026), € 405.000 (2025). Geen aangescherpte koopgrens voor kleine kernen; prestatieafspraak 2025: vrije toewijzingsruimte sociale huur 7,5% → 15% voor kleine kernen. Corporatie: 485 woningen 2022-2030. CPO-woningen zijn "VON onder de NHG-grens" | gevonden | addendum p. 6, 8; RIS 1424302; prestatieafspraken 2025 (voettekst noemt Hardenberg, zie Tegenstrijdigheden) |
| **A4** | Volkshuisvestingsprogramma en ladder | Geen (ontwerp-)programma. Coalitie: "vernieuwde woonvisie". Ladder wordt toegepast (> 11 woningen) bij Van Alewijkstraat. Provinciale principes worden gebruikt | gevonden (afwezigheid) | CVDR/RIS/ommen.nl; 2026-10-06/11. Te vinden: raadsagenda's, CUP (oktober 2026); verplicht 1-7-2027 [PB] |
| **A5** | Ouderen/zorg, geclusterde woonvormen, urgentie | Woonzorgvisie in voorbereiding (Companen; RIB 11-6-2026). Prestatieafspraken 2025: Rijksopgave West-Overijssel 1.170 zorggeschikt / 1.800 geclusterd / 3.600 nultreden; actie: woonzorgvisie 2024-2025 (niet vastgesteld). Projecten: Hof van Vlierlanden, Haven Oost, Julianastraat 8, CPO Lemele-hof. Langer zelfstandig wonen: geen Ommense aanvraag. Geen urgentieverordening | deels gevonden | prestatieafspraken 2025; Gmb 2025-549668; 2026-10-06/11 |
| **B1** | Eigen KGO-kader / rekenformule | Geen KGO-kader. Rood voor Rood 2026 (CVDR757546; college): 850/2.000 m² sloop, 750 m³, kortingen, sloopmeterregister, maatwerk art. 10. Geen geldformule | gevonden | lokaleregelgeving.overheid.nl/CVDR757546; 2026-10-06/11 |
| **B2** | Schaalgrenzen | Standaard 1-2 compensatiewoningen; alternatieve woonvormen 2+ eenheden binnen 750 m³; grootste precedent 3. 10-12 alleen via maatwerk of eigen omgevingsplanwijziging bij een kern | gevonden | idem; Gmb 2026-57513 |
| **B3** | Actualiteit t.o.v. Actualisatie 2026 | RvR 2026 verwijst nog naar de "Ontwerp provinciale omgevingsvisie"; omgevingsplan niet aangepast aan art. 4.123-4.124; Kleine Kernen/Wonen 2027, Buitengebied 2027-2030; herziening na nieuwe typologie aangekondigd | gevonden | toelichting RvR; VAB-evaluatie; ommen.nl/omgevingsplan-ommen |
| **B4** | Uitleg of KGO | Aansluitend aan een kern: uitleg van dorpen (art. 4.5 lid 3), geen KGO. Erf buiten een kern: KGO + ruimtelijk kwaliteitsplan (art. 4.11). Geen contour in de omgevingsvisie | gevonden | TAM-motivering Beerzerveld p. 26-27 |
| **B5** | Vorm kwaliteitsinvestering | Sloop/asbestsanering, landschapsinrichtingsplan, natuurontwikkeling, erfpacht met afdracht aan natuurbeheer, behoud karakteristieke panden. Geen fonds, geen bankgarantie | gevonden | Beerzerpoort, Beerzerweg 26, Varsenerweg 5a |
| **C1** | Landbouwgebied-typologie | Gebiedsspecifiek 41,6% van de gemeente (60,2% van de landbouwgrond), generiek 16,8% (27,3%); Vinkenbuurt generiek, overige kernen gebiedsspecifiek | gevonden | ruimtelijkeplannen.overijssel.nl (doc 55d637e6-…); 2026-10-11 |
| **C2** | Afwijkingsroute art. 4.124 lid 4 | Geen gebiedsvisie. Ontwikkelperspectieven mei 2027; zes provinciale gebiedsprocessen in het Vechtdal (Landgoederenzone, Witharen, Lemelerveld-Dalmsholte-Giethmen, Junne, Archem-Eerde, Stegeren); Schapendijk 9 → Staphorst (sloopmeters over de gemeentegrens) | niet gevonden (in voorbereiding) | ommen.nl; toekomstvooronsplatteland.nl **[WF]** |
| **C3** | Overige overlays | NNN 36,7%; Natura 2000 22,0% (projectbesluit Arriën, Prb 2026-8); zeer kwetsbaar 26,1%; grondwaterbeschermingszone 8,6%, intrekgebied circa 22%; landgoed 24,6%; essen 6,7%; Nationaal Landschap n.v.t.; raatakkers/karrensporen (voorbereidingsbesluiten 4-4-2025); Hammerflier-gebiedsproces | gevonden | WFS; verordening-viewer; zoek.officielebekendmakingen.nl/prb-2026-8.html |
| **C4** | Redeneerlijn, energie, netcongestie | Geen standaard OF-WAAR-HOE of energieparagraaf; TAM-plannen toetsen aan art. 4.4/4.5/4.11/4.13/4.15/4.73. Beleidsregels transportcapaciteit (CVDR765864); volgordelijst 17-9-2026; Enexis Ommen Dante fase 1a (juli 2026). Congestiegebied in de regels niet vastgesteld | deels gevonden | CVDR765864; enexis.nl update juli 2026 |
| **D1** | VAB-/erftransformatieprogramma, subsidie 4.39 | Geen deelname of aanvraag gevonden; routekaart aan Ontwikkelperspectieven gekoppeld | niet gevonden | VAB-evaluatie; vab@overijssel.nl |
| **D2** | Erfcoach en ondersteuning | Erfcoaches actief; Boerenperspectief Overijssel vanaf 2026; plattelandscoach (coalitie) nog aan te stellen | gevonden | ommen.nl 3-2-2025 |
| **D3** | VAB-beleid en precedenten | Zie §4; geen aparte VAB-regel; max. 1-2 compensatiewoningen (3 met maatwerk); geen CPO-precedent op een agrarisch erf | gevonden (moederplanregel niet gelezen) | CVDR757546; VAB-evaluatie |
| **E1** | Accounthouder/Omgevingstafel/1-op-1 | Geen namen. Omgevingstafel IJsselland gebruikt (Beerzerveld). Provinciale reacties op principeverzoeken (Lemelerweg 36-40, Vinkenbuurt). 1-op-1-gesprekken niet gevonden | deels | RIS 15660112, 16636682; odijsselland.nl/over/omgevingstafel [WF] |
| **E2** | Routekeuze en doorlooptijd | Grotere woningbouw via TAM-omgevingsplan; kleine/erf-ingrepen via BOPA met bindend raadsadvies; provinciale Lijst BOPA via Uitzonderingenlijst afgedaan (Beerzerpoort). Doorlooptijd 11-14 maanden; principeverzoek 8-12 weken | gevonden | CVDR712101; RIS 17317123; ommen.nl |
| **E3** | Uitzonderingenlijst (≤ 11 / ≤ 6 woningen) | Inwoners (Rekenkamer 2025): Ommen ca. 18.500; Lemele 1.535; Beerzerveld 1.055 (of 505 volgens de TAM-motivering); Witharen 665; Vilsteren 380; Giethmen 235; Beerze 170. Alle dossiers ≥ 10 woningen zijn in de praktijk aan de provincie voorgelegd | gevonden (indicatief); tegenstrijdig (Beerzerveld) | RIS 15897701, 15660123 |
| **E4** | Provinciale zienswijzen/conflicten 2023-2026 | Geen formele zienswijze, aanwijzing of onthouden instemming; wel informeel remmende signalen (Vinkenbuurt 11 → 8; Lemele-visie); historisch: reactieve aanwijzing bp Buitengebied 2010 (RvS 2012) | niet gevonden (formeel) | Provinciaal blad (878), Gemeenteblad (3.601); RIS |
| **F1** | Provinciale regelingen | Gebruikt: Adviespool Woningbouw (Julianaschool/Guido de Brès), Leefbaar Platteland (ontwerp Vinkenbuurt), provinciale ondersteuning kleine kernen niet gevonden. Particulier CPO kan niet rechtstreeks gebruik maken [PB] | deels | RIS 15263990, 14966654 |

---

## Tegenstrijdigheden en onzekerheden
1. **ONW-indicatie (8,0%) versus nieuwe typologie (41,6% gebiedsspecifiek).** Opgelost in het voordeel van de typologie uit de verordening-viewer (geometrie van de vastgestelde verordening; NNN-validatie 6.687 vs. 6.688 ha). Voorbehoud: de percentages zijn gebaseerd op generalisatie van vector tiles (z=10) en kunnen aan de randen afwijken; latere verordeningswijzigingen zijn niet uitgesloten.
2. **Wie stelde Rood voor Rood 2026 vast?** De CVDR-kop (door de hoofdagent gecontroleerd): college; Gmb 2026-82708: "Besluiten college". De raad stemde op 29-1-2026 over het evaluatievoorstel, nam amendement A3 aan en stelde daarbij "Beleidsregels Rood voor Rood gemeente Ommen 2025" vast, waarbij het amendement stelt dat "niet het college bevoegd is, doch de raad". Of de raad de regels formeel vaststelde of dat het college dat deed met verwerking van het amendement, is niet opgelost. De inhoud is in beide gevallen dezelfde.
3. **Vlierlanden fase 3:** Woondeal 332 (450 → 332), gemeentesite "circa 375", GREX 300, gebiedsvisie 375. Het zijn verschillende peilmomenten of definities.
4. **Inwonertal Beerzerveld:** 505 (2023, kern 18 ha; TAM-motivering) versus 1.055 (2024; Rekenkamer, dorpsvisie-gebied). Bepaalt of de grens van ≤ 6 of ≤ 11 woningen in de Uitzonderingenlijst geldt.
5. **Woningbouwopgave:** 1.250 (2021/2023/2026) versus 1.625 tot 2040 (coalitieakkoord 2026, bron niet gevonden).
6. **Betaalbaarheidsgrens:** € 355.000 (addendum 2023), € 390.000 (MJP 2026), € 405.000 (college 16-4-2025, [PB] landelijke grens). Per project controleren welke grens geldt.
7. **Addendum 2023:** 30 CPO-woningen (samenvatting) versus 40 (som locatietabellen); XL rechts 8 versus 12. Haven Oost-6 ontbreekt in de samenvatting.
8. **Aantal CPO-woningen Erve Arriërflier:** 8 (inschrijfprocedure, volgordelijst) versus "tien" (De Toren 25-11-2025 **[WF]**); projectomvang 45, 50 of 50-60. Gevolgd: 8 CPO in een project van 45-50.
9. **Beerzerpoort:** het Gemeenteblad meldt "toevoegen twee woningen"; het raadsvoorstel spreekt van "drie wooneenheden". Aannemelijk is dat twee woningen worden toegevoegd aan één bestaande eenheid [INT].
10. **Provinciale houding:** de toelichting op Rood voor Rood en de Lemele-visie noemen de provincie "terughoudend"; tegelijk stemt de provincie in met 34 woningen aan Beerzerveld, 8 in Vinkenbuurt (na reductie) en gebiedsvisie Vlierlanden. De terughoudendheid betreft vooral buurtschappen, solitaire erven en aantal/dichtheid, niet kernuitbreiding met lokale behoefte [INT]. De bron voor "terughoudend" in Lemele is gemeentelijk en secundair; de provinciale reactie zelf is niet gelezen.
11. **Provinciale instemming bij BOPA's:** de bestuursinformatie noemde dit niet; de ruimtelijke motivering van Beerzerpoort geeft het antwoord (Uitzonderingenlijst, instemming "niet aan de orde"). Voor grotere BOPA's is dit onbekend omdat er geen is gevonden.
12. **Stikstofopschorting:** de provinciepagina (ongedateerd) meldt opschorting van natuurvergunningen "tot 1 februari 2027"; de raadscommissie van 13-2-2025 sprak nog over "on hold tot 1 februari 2026"; Ommense stukken van maart 2026 (Koloniedijk 1) beschrijven dat de Omgevingsdienst aanvragen "weer oppakt". Reikwijdte voor woningbouw onduidelijk.
13. **Prestatieafspraken 2025:** de voettekst noemt "Hardenberg" (sjabloon van een buurgemeente); inhoud wel voor Ommen. Herkomst controleren voor citatie.
14. **Lijst Bindend Adviesrecht:** de gepubliceerde tekst bevat concept-resten; een herziene versie na de evaluatie is niet gevonden.
15. **Leges:** niet eenduidig of art. 2.6 lid 1 en lid 5 cumuleren; de berekening is [BER].
16. **Doorlooptijd Beerzerweg 26:** het registerrapport noemt de periode 16-7 t/m 27-8-2026 als "ter inzage"; dat is de beroepstermijn na vaststelling op 4-6-2026 (ontwerp juli 2025).
17. **Plaatsnamen:** de opdracht noemde Besthmen, Hammerbrug en Junne als woonplaatsen; dit zijn buurtschappen of landgoed zonder BAG-woonplaats. Den Ham ligt in Twenterand.

## Niet gevonden / niet onderzocht (met vindplaats)
| Onderwerp | Reden | Waar te vinden |
|---|---|---|
| Ruimtelijke Visie Ommen 2040; uitvoeringsstrategie Woon- en werklocaties | Niet openbaar; besloten commissie 3-4-2025 | Griffie/afdeling Ruimte; CUP (oktober 2026) |
| Woningbehoefteonderzoek 2024 Ommen | Alleen geciteerd in SV Lemele | Afdeling Ruimte/Wonen; Woonzorgvisie-traject |
| Grondprijsbrief 2025/2026; Nota Grondbeleid 2012 | Niet gelezen resp. niet gevonden online | ommen.nl/direct-regelen/ondernemen/grondprijzen/; Grondzaken/RIS 2012; herziene nota uiterlijk begroting 2027 |
| VAB-regel in het moederplan Buitengebied (aantal woningen per erf) | Niet uitgelezen; ruimtelijkeplannen.nl 404, DSO-API met sleutel | omgevingswet.overheid.nl/regels-op-de-kaart; plan NL.IMRO.0175.buiten201200001; afdeling Ruimte |
| Strategieboek Verstedelijkingsstrategie Regio Zwolle (groeiprofiel Ommen) | PDF gaf geen inhoud | Regio Zwolle |
| Provinciale accounthouder; 1-op-1-gesprekken; zienswijzennota's bij TAM-plannen | Niet publiek | Gemeente (afdeling Ruimte), Overijssel Loket 038 499 88 99, bijlagen RIS/ruimtelijkeplannen.nl |
| Definitief Hammerflier-besluit (gepland mei 2026); beroep tegen projectbesluit Arriën | Niet gevonden | Provincie Overijssel; Raad van State |
| Of woningbouw valt onder de provinciale opschorting natuurvergunningen; stikstofrapporten per project | Niet beantwoord | overijssel.nl; AERIUS-bijlagen bij projecten |
| Perceelsgeometrie per concrete locatie | Geen kandidaatlocatie bekend | verordening-viewer en WFS direct bruikbaar (`_locationSearch`) |
| Catalogus Gebiedskenmerken (ambities per gebiedstype) | Niet uitgelezen (Bijlage VII) | Omgevingsverordening, bijlage VII |
| Uitkomst burgemeestersprocedure; verkennersadvies 7-4-2026 | Niet gevonden | RIS/griffie; BZK |
| Partijprogramma's CDA, PRO Ommen, LPO, ChristenUnie, D66 | Niet gelezen | Partijsites |
| De Stentor; sociale media van gemeente en CPO-verenigingen | Betaalmuur / inlog | — |
| Bouwstenen-pilot (OCR p. 7-27) | Scan met gespiegelde tekst | RIS 16636690 |

## Houdbaarheid (herverifiëren vóór gebruik)
Nieuw Ommens beleid verwacht: woonvisie en huisvestingsverordening (coalitieakkoord), uitvoeringsprogramma (CUP) oktober 2026, herziene Nota Grondbeleid uiterlijk begroting 2027, Ontwikkelperspectieven Landelijk Gebied (mei 2027), omzetting tijdelijk omgevingsplan Kleine Kernen/Wonen (2027), volkshuisvestingsprogramma (uiterlijk 1-7-2027). Overig: Besluit versterking regie volkshuisvesting (ladder, verwacht 1-1-2027); provinciale opschorting natuurvergunningen (tot 1-2-2027); subsidie 4.39 (plafond, verplichting vóór eind 2026); Actualisatie 2026-2 Omgevingsverordening (PS-besluit december 2026); Provinciale Statenverkiezingen maart 2027; volgende ronde volgordelijst netcongestie (niet aangekondigd).

## Bronnen (selectie)
- Omgevingsvisie, woonprogramma, addendum, CPO-uitvoeringsregels, coalitieakkoorden, Lijst Bindend Adviesrecht, Rood voor Rood 2021/2026, leges 2026, woningsplitsing, transportcapaciteit: zie de URL's in de tekst.
- RIS Ommen (Notubiz): https://ommen.raadsinformatie.nl en https://ommen.bestuurlijkeinformatie.nl (organisatie 434); geraadpleegde dossiers: 15660112/15660123 (Van Alewijkstraat), 16407392/16407399 (Varsenerweg 5a), 16004073/16004075 (Schapendijk 9), 16620502 (Prinses Julianastraat 8), 16910724 (Beerzerweg 26), 17317126/17317123 (Beerzerpoort), 17345188/17345180 (Gravendijk), 14966654 (Vinkenbuurt), 15307764 (Vlierlanden fase 3), 16636684/16636690 (SV Lemele en Bouwstenen), 16407378/16407379 (VAB-evaluatie), 15897701 (Rekenkamer).
- Provinciaal: verordening-viewer ruimtelijkeplannen.overijssel.nl (doc 55d637e6-…), WFS services.geodataoverijssel.nl/geoserver/ows (NNN, Natura 2000, B82-planmonitor), Prb 2026-8 en 2025-8252 (projectbesluit Arriën), Prb 2026-11834 (volkshuisvestingsprogramma-ontwerp), https://regelen.overijssel.nl (4.39).
- Nieuws: ommen.nl/actueel (84 artikelen gelezen), Vechtdal Centraal, RTV Vechtdal, Ommen City, Oost, De Toren **[WF]**, Enexis (netcapaciteit-updates 2025-2026).
