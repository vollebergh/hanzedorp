# Deelonderzoek 1 — Gemeentelijke bestuursinformatie: gemeente Voorst (Gelderland, woondealregio Stedendriehoek)

**Raadpleging:** 2026-10-17 en 2026-10-18. **Model:** Claude Sonnet 5.5 (subagent, deelonderzoek 1). **Kader:** `provincie_gelderland.md` (stand 2026-10-02) + Bijlage B. Gelderse begrippen gebruikt; geen Overijsselse.

**Bronmarkeringen:** **[PRIMAIR]** = brontekst zelf gelezen; **[PB]** = uit `provincie_gelderland.md`; **[TK]** = trainingskennis; **[INT]** = interpretatie; **[BER]** = eigen berekening; **[WF]** = via samenvatting/zoekresultaat (lager betrouwbaar).

**Toegang/methode:** voorst.nl werkt met curl + browser-user-agent (TYPO3, sitemap 669 pagina's). Raadsinformatiesysteem = **Notubiz** (`voorst.raadsinformatie.nl`, organisatie-id 742); de open Notubiz-API (`api.notubiz.nl`) is gebruikt voor volledige lijsten van vergaderpunten (2022-06 t/m 2026-10) en de modules Raadsvoorstellen (266), Raadsmededelingen, Moties, Ingekomen stukken, Schriftelijke vragen. College-besluitenlijsten 2023-2026 (188 weeklijsten) zijn gedownload en op trefwoorden doorzocht. CVDR en Gemeenteblad via SRU. PDF's met pdfplumber/pypdf uitgelezen; tweekoloms-PDF's (ontwerp-omgevingsvisie, PLG) met kolomdetectie. Afbeelding-PDF's (niet uitleesbaar zonder OCR): Nota landgoederen 2006 (scan), "Functieverandering en verevening", "Functieverandering: gecorrigeerde vervangingswaarde", "Functieverandering: het proces" — **niet gelezen**.

**Bronnenlijst-afkortingen** staan onderaan (S1-S40) met URL en datum.

---

## Kernbevindingen (voor de snelle lezer)

1. **Voorst heeft geen CPO-instrumentarium voor het buitengebied, wel een CPO-praktijk in kernen.** Enige CPO-kavel: Hessenlaan Teuge (inbreiding, 5-6 levensloopbestendige rijwoningen, vrije sector, uitvraag okt-nov 2023, ondergrens €665.000 incl. btw voor 1.705 m²); Jaarstukken 2025 melden "5 woningen Hessenlaan in Teuge" als gerealiseerd. Het Kader Volkshuisvesting 2026/2027 (raad 9-3-2026) en het coalitieakkoord 2026-2030 noemen CPO **niet**; het ontwerp-omgevingsvisie (juli 2026) is "open voor collectieve wooninitiatieven" in de dorpen (p. 45). De oude Woonvisie 2017 (waarin CPO expliciet stond) is op 9-3-2026 ingetrokken.
2. **Buitengebied:** kader is het **tijdelijke "Rood voor Groenbeleid"** (raad 30-1-2023; puntenstelsel; tabel loopt tot 6 wooneenheden / 3.000 m³ = 28 punten; daarboven maatwerk). Formele looptijd was 2 jaar (tot ca. 30-1-2025); een verlengings- of definitief besluit is **niet gevonden**, maar het college past het t/m sept. 2026 nog toe ("tijdelijk Rood voor Groen beleid"). Het Programma Landelijk Gebied (26-5-2025) wil woningbouw **clusteren in/rond dorpen**: op boerenerven "1 tot 3 woningen" (productief landschap), "in het middengebied wat meer".
3. **Schaal 10-12 woningen buiten de kern:** geen gevonden Rood-voor-Groen-precedent boven 2 woningen. Wel recente grotere BOPA-besluiten op voormalige agrarische/landgoedlocaties **aan de rand van kernen**: De Vecht, Lochemsestraat 40 (**17 woningen**, principebesluit 17-2-2026, beëindigd agrarisch erf, 2/3 betaalbaar) en landgoed Het Nieuwe Wezeveld bij Twello (**18 appartementen**, 24-2-2026). Dit zijn geen CPO's.
4. **Beleidskader wonen:** Kader Volkshuisvesting (ambitie 125 woningen/jaar; alle plannen ≥ 2/3 betaalbaar; vanaf 12 woningen ≥ 1/3 sociaal; verevening) is nu "interim-volkshuisvestingsprogramma"; het eigenlijke **Volkshuisvestingsprogramma Voorst 2026/2031 is nog niet vastgesteld** en geen ontwerp gevonden. De **ontwerp-Omgevingsvisie** (ter inzage 16-7 t/m 10-9-2026; raadsbesluit Q4 2026) kiest voor inbreiding/verdichting, ~3.000 woningen na 2030, en "Rood voor Groen" met "landgoedmodel" (kleine woonerven) in groene buffer/mozaïeklandschap.
5. **Bestuurlijk klimaat:** nieuwe coalitie Gemeente Belangen (5) + VoortvArend Voorst (5) + VVD (2) = 12/21 zetels, akkoord "Natuurlijk Voorst!" (26-6-2026; raad 6-7-2026). Wethouder Wonen/Ruimtelijke ordening: **Robert Bosch**. Houding "ja, mits"; coalitie wil "particuliere initiatieven actief stimuleren" en onderzoekt de "maatschappelijke meerwaarde van het rood-voor-groenbeleid".
6. **Belangrijkste drempels voor Hanzedorp:** (a) geen schaalruimte in RvG-tabel; (b) gemeentelijke voorkeur voor clusteren bij dorpen; (c) 2/3-betaalbaarheidseis en vereveningssystematiek; (d) netcongestie (Voorst heeft sinds 28-8-2026 een volgordelijst-beleidsregel; aanmelden kon t/m 6-9-2026); (e) raad kan bindend advies geven bij BOPA's (CVDR701428); (f) trage doorlooptijd (20-31 maanden principebesluit→vergunning bij 1-2 woningen RvG).

---

## 0. Gemeentelijke context en regio

- Voorst: 12 dorpen (Twello = centrumdorp; Klarenbeek, Terwolde, Voorst = middelgrote dorpen; Bussloo, De Vecht, Nijbroek, Posterenk, Steenenkamer, Teuge, Wilp, Wilp-Achterhoek). 25.568 inwoners per 1-1-2026 [PRIMAIR, S11 Kader p.1]. "Groene hart van de Stedendriehoek".
- **Woon-/verstedelijkingsregio:** Stedendriehoek (Apeldoorn, Brummen, Deventer, Epe, Heerde, Lochem, Voorst, Zutphen). **Grensoverschrijdend:** Deventer (Overijssel) neemt deel aan de regio; voor de woondeal-aantallen hoort Deventer bij West-Overijssel [PB §1.4.2]. Het Gelderse regime is leidend voor het omgevingsplan [PB]. Voorst-brede cijfers: woondeal 2025-2034 **1.000 woningen** (600 in 2025-2030 + 400 in 2031-2034) [PB §1.5.1; bevestigd in Portret Voorst p.21, S23]; regionale woonafspraken art. 5.64 [PB].
- **Gemeentelijke beleidsbronnen (overzicht):** website "Beleid en regelgeving" (S4) met Programma Bouwend Voorst / Mooi Voorst; Notubiz-RIS (S2); CVDR (S30-S33).

---

## 1. CPO-beleid

**Kern:** geen apart CPO-beleid of -regeling in het vigerende beleid; wel (a) een CPO-uitgiftepraktijk (Hessenlaan Teuge), (b) een CPO-brochure (sept. 2023), (c) positieve noties in ontwerp-omgevingsvisie, PLG en Portret. Kader Volkshuisvesting 2026/2027 en coalitieakkoord bevatten het woord CPO niet [PRIMAIR, tekstzoek: 0 treffers].

### 1.1 Woonvisie "Aantrekkelijk Voorst 2025" (maart 2017) — **ingetrokken 9-3-2026** [PRIMAIR, S12]
> "We bieden ruimte aan kleinschalige initiatieven en experimenten met nieuwe woonvormen. Voorbeelden zijn CPO-projecten, verticale woningsplitsing in de kleine kernen of woonzorgconcepten. De nadruk ligt hierbij op kleinschaligheid, maatwerk en inbreiding." (Woonvisie 2017; zelfde passage geciteerd in Woonzorgvisie Voorst 2023-2027, S13)
De Woonvisie is bij raadsbesluit 9-3-2026 ingetrokken (punt 5 raadsbesluit Kader Volkshuisvesting, S11b). Opvolger: Kader Volkshuisvesting + nog op te stellen Volkshuisvestingsprogramma.

### 1.2 Kader Volkshuisvesting 2026/2027 (raad 9-3-2026) [PRIMAIR, S11]
Noemt geen CPO/collectief/zelfbouw. Wel: "levensloopbestendige woningen ... zowel individueel als geclusterd" (§4), uitgangspunt "clusteren woningbouw in en rondom de bestaande dorpen. Op boerenerven zijn wel ontwikkelingen mogelijk, kleinschalig van aard of initiatieven die aansluiten bij het Rood voor Groenbeleid" (§2, p.2).

### 1.3 Ontwerp-omgevingsvisie (juli 2026) [PRIMAIR, S6]
- Dorpen (Bussloo, De Vecht, Nijbroek, Posterenk, Steenenkamer, Teuge, Wilp, Wilp-Achterhoek), keuze 3 (p.45): "In de dorpen bieden we voldoende ruimte om te voorzien in de lokale woonbehoefte ... zetten we in op de ontwikkeling van kleinere en levensloopbestendige woningen voor jongeren en senioren. Vanwege het karakter en de maat en schaal van de dorpen staan we hier **open voor collectieve wooninitiatieven**."
- Groene buffer, keuze 9 (p.57): dorpsranden met "ruimte voor ommetjes, speelgelegenheid, voedselbossen, moestuinen en **kleinschalige wooninitiatieven**".
- Mozaïek-/groene-buffer-landschap: "nieuwe woonvormen" binnen nieuwe landgoederen, "altijd gecombineerd met groen (conform het Rood voor Groen beleid)" (p.28).

### 1.4 Programma Landelijk Gebied (PLG; raad 26-5-2025) en Portret (sept. 2025) [PRIMAIR, S9, S23]
> "We staan in de basis positief tegenover meergeneratiewonen, pre-mantelzorgwoningen, ook als er nog geen zorgindicatie is, **wooncoöperaties en andere wooncollectieven**." (PLG uitgangspunt 7, p.28)
Portret p.20: "Hierbij bestaat de behoefte voor kleinschalige wooninitiatieven en experimenten met nieuwe woonvormen, zoals CPO-projecten en woonzorgconcepten" (verwijst naar Woonvisie).

### 1.5 CPO-uitgiftepraktijk
- **Hessenlaan, Teuge** (zie §5 en §7). **CPO-brochure** "Samen bouwen in de gemeente Voorst" (sept. 2023) [PRIMAIR, S16]: "De gemeente Voorst stimuleert actief CPO; zij wijst projectlocaties aan, stelt de randvoorwaarden voor ontwikkeling op en werft actief geïnteresseerden." Locaties worden door de gemeente aangewezen; inschrijven alleen als groep; groep krijgt 12 weken om begeleider te kiezen, rechtspersoon (vereniging) op te richten en tot ≥ 80% deelnemers te komen; reserveringsovereenkomst 28 weken; achtervangpartij voor max. 20% van de woningen; aanbetaling € 10.000 per deelnemer bij koopovereenkomst; grondkosten ± 25% van begroting; overdracht alleen als ≥ 80% door de groep zelf wordt ontwikkeld.
- **Avond van het Wonen 2-12-2025** (S14): "Meningen over of de gemeente Voorst meer moest doen om CPO ... te stimuleren waren verdeeld. Het gaat niet per se sneller. Wel kunnen we het aanbieden als mogelijkheid."
- Gemeentelijke Nota Grondbeleid noemt "uitgifte van kavels in particulier opdrachtgeverschap" als onderwerp waarover het omgevingsplan regels kan stellen (S10 §4.2).
- Gronduitgifteregeling koopwoningen 2020 (CVDR637112): geen bindingseisen of voorrangscriteria; loting (via notaris) of biedprocedure [PRIMAIR, S31].

### 1.6 Signalen uit de samenleving
Brief **Woongroep Teuge** aan de nieuwe raad (8-6-2026): oproep om "structureel ruimte te maken in beleid voor collectieve en coöperatieve woonvormen; grond en locaties actief beschikbaar te stellen aan bewonersinitiatieven" [PRIMAIR, S27]. Brief Cooplink (24-6-2024) over wooncoöperaties [PRIMAIR, S27b].

---

## 2. Openheid voor nieuwbouw buiten woonkernen

### 2.1 Visie en kaders
- **Kader VHV 2026/2027:** "We clusteren woningbouw daarom in en rondom de bestaande dorpen. Op boerenerven zijn wel ontwikkelingen mogelijk, kleinschalig van aard of initiatieven die aansluiten bij het Rood voor Groenbeleid." [PRIMAIR, S11 p.2]
- **Coalitieakkoord 2026-2030 (p.11-12):** "Nieuwe woningen realiseren wij bij voorkeur in of nabij bestaande kernen en voorzieningen. Om invulling te geven aan de verhoogde ambitie ... is het nodig om ook nieuwe locaties voor woningbouw te ontwikkelen." Grootste groei in Twello (centrum, stationsgebied; max. zes bouwlagen); inbreidingslocaties Rijksstraatweg; Wassenaer Obdamstraat; Twello-Noord; Voorst-West; Wilp-Achterhoek. "Op de langere termijn zullen echter ook nieuwe uitbreidingslocaties nodig zijn ... Wij willen daarin nadrukkelijk regie nemen" (actualisatie locatiestudies) [PRIMAIR, S8].
- **Ontwerp-omgevingsvisie** (S6, p.20-22): doel 3.000 woningen na 2030 (eerdere bovengrens 4.000 naar beneden bijgesteld; contourenschets 2.000-4.000); "Bij groei ligt in eerste instantie de focus op inbreiding en verdichting. In het geval van uitbreiding zetten we nadrukkelijk in op het 'Groen groeit mee'-principe"; proportionele strategie (grootste groei Twello, dan Klarenbeek, Voorst, Terwolde); in overige dorpen "beperkte en kleinschalige inbreiding of uitbreiding"; dorpen 250-750 woningen tot 2050, eerst binnen dorpscontouren. Acht deelgebieden: Twello, middelgrote dorpen, dorpen, werklocaties, groene buffer, mozaïeklandschap, agrarisch landschap, IJssellandschap.
- **PLG uitgangspunt 6** (S9 p.26-27): zie §3.
- Dorp Voorst: Kansenkaart; inbreidingsmogelijkheden "uitgeput"; uitbreiding **Voorst-West ± 150 woningen** (IBB 26-5-2026; stedenbouwkundig plan eind 2026; juridische procedure vanaf Q2 2027; procedure (omgevingsplanwijziging door raad of BOPA) nog niet gekozen) [PRIMAIR, S19].

### 2.2 Ladder en volkshuisvestingsprogramma
- **Ladder voor duurzame verstedelijking:** in Kader VHV, ontwerp-omgevingsvisie, PLG en coalitieakkoord **niet genoemd** (tekstzoek: alleen "participatieladder") [PRIMAIR]. Een eigen gemeentelijke lezing van de 11/12-woningengrens is niet gevonden; wel de beleidsgrens "vanaf 12 woningen" voor sociale 1/3 in het Kader.
- **Volkshuisvestingsprogramma:** Kader VHV 2026/2027 "werken wij uit in het gemeentelijk Volkshuisvestingsprogramma" ([PRIMAIR, S11 p.1]); raadsvoorstel: "Volkshuisvestingsprogramma Voorst **2026/2031**"; college is bevoegd; na vaststelling Kader zou het concept als ontwerp ter inzage worden gelegd (S11c). Ontwerp-omgevingsvisie (juli 2026) noemt het programma nog "nog op te stellen". **Een (ontwerp-)programma is op 2026-10-18 niet gevonden** (geen raadsstuk/pagina). Wijziging omgevingsplan om doelgroepbepalingen sociale koop/huur in het omgevingsplan op te nemen was gepland voor Q3 2026 (raad bevoegd) — **niet gevonden**.
- **Wet versterking regie volkshuisvesting:** Raadsbesluit Jaarstukken (6-7-2026) reserveert €101.000 "Wonen en bouwen" uit Decembercirculaire 2025 voor uitvoering Wet versterking regie volkshuisvesting [PRIMAIR, S36].

### 2.3 Provinciale/regionale begrenzing (context [PB])
Regionale woonafspraken (art. 5.64); woondeal Stedendriehoek 2025-2034; Voorst ligt volledig in streek IJsselvallei, buiten stikstofstrook; GOZ 20% van gemeentegebied; Nationaal Landschap Veluwe 69,9% van het gemeentegebied [PB §1.6.8].

---

## 3. Openheid voor agrarische herbestemming

### 3.1 Wettelijk/procedureel kader (gemeentelijk)
- **Omgevingsplan gemeente Voorst** (CVDR696255, versie 3, in werking 7-10-2024): tijdelijk deel = vigerende bestemmingsplannen (agrarisch bouwvlak etc.); omgevingsplanwijziging door raad; **BOPA** (buitenplanse omgevingsplanactiviteit) door college via "Verken uw idee" [PRIMAIR, S30, S5]. Gemeentelijke webpagina: past een idee niet in het (tijdelijke) omgevingsplan, "dan onderzoeken wij of wij tóch kunnen meewerken ... met toepassing van een vergunning voor een BOPA" (S5). Grotere ideeën (functiewijziging, woningbouwplan) gaan naar afdeling Ruimte en daarna naar het college [PRIMAIR, S5].
- **Bindend adviesrecht gemeenteraad** (Aanwijzingsbesluit, raad 3-7-2023, CVDR701428, in werking 1-1-2024) — voor BOPA's met uitgebreide procedure: bindend raadsadvies "a. als de activiteit niet past binnen de doelen van het omgevingsplan en/of (overige) door de gemeenteraad gestelde kaders; b. als de activiteit een bouwplan betreft met een geschatte bouwsom van meer dan € 2.000.000 (inclusief btw) **en** een bouwvolume van meer dan 2.000 m³ **en** een wijziging van toegestaan gebruik dat qua omvang een terrein van meer dan 2 ha in beslag neemt"; niet van toepassing "op gevallen die in strijd zijn met instructie(regel)s" [PRIMAIR, S31b]. [INT] Een CPO van 10-12 woningen (>2.000 m³, bouwsom > € 2 mln) valt vrijwel zeker onder (a) of (b); het college achtte bij De Vecht (17 woningen) en Het Nieuwe Wezeveld (18) het raadsadvies **niet** van toepassing (RM 17-2 en 3-3-2026) — de afbakening is dus niet automatisch.
- **Rood voor Groenbeleid** (S1): zie §3.2-3.5. Eerder regionaal "Waar de stallen verdwijnen: Oude erven, nieuwe functies" (2008; evaluatie 2017) + "Notitie ruimtelijke kwaliteit veranderende erven" (2009) = "Rood voor Rood"; raad stemde 30-1-2023 in met **keuzevrijheid** voor initiatiefnemers tussen oud en nieuw beleid (college-toezegging 28-11-2022; motie "behoud oud of nieuw" ingetrokken) [PRIMAIR, S3].
- **Nieuwe landgoederen:** Nota Landgoederen (raad 6-2-2006): definitie Rijk/provincie "maximaal twee á drie wooneenheden en ... minimaal 5 ha"; Voorst: "uitgangspunt van één wooneenheid per landgoed" (tweede/derde alleen als plan anders niet haalbaar is); zoekgebied aangewezen; ervaren adviseur, landgoedplan, vooroverleg provincie [PRIMAIR, S7]. Actueel gebruik: BOPA nieuw landgoed met crematorium (5,9 ha; RM 10-3-2026) [PRIMAIR, S19b].

### 3.2 Rood voor Groenbeleid — integrale inhoud (document: BiedtRuimte, "Tijdelijk beleid", 31-1-2023, 17 p.) [PRIMAIR, S1]
Doel: "wanneer een initiatiefnemer in het buitengebied een ontwikkeling wenst, moet dit in ieder geval leiden tot meer natuur en landschap" (§1.1). Punten: 1 punt = 0,25 ha natuurontwikkeling = 300 m² sloop landschapontsierende bebouwing = 1.500 m² sloop kassen = € 25.000 (restauratie/recreatieve route; maatwerk circa € 22.500). Basis: natuur € 80.000/ha; sloop € 75/m² → 1 punt = € 20.000-25.000. Tabel (punten te investeren): tiny house 4; generatiewoning (300 m³) 6; woning 450 m³ 8; woning 750 m³ 10; 2-3 wooneenheden in 1 gebouw (≤ 900 m³) 12; 2-4 wo. ≤ 1.200 m³ 16; 2-4 wo. ≤ 1.500 m³ (of buitenplaats) 20; 3-5 wo. ≤ 2.250 m³ 24; **4-6 wo. ≤ 3.000 m³ 28**; splitsing 5; bouwen op ander bestaand erf +2; niet-bestaand erf +2 (regelgeving) of **+4 (gewenst)**; **aansluitend aan dorp −2**; bestaande (karakteristieke) bebouwing hergebruiken −2. "De nieuwe ontwikkeling vindt plaats binnen de bestaande erfstructuur." **Bij 3 of meer woningen is differentiatie in woningtypen verplicht** (compact, onder NHG-grens/midden-huur, levensloopbestendig, groepswonen met gedeelde voorzieningen, natuurinclusief). Maatwerk "altijd mogelijk" bij grotere bebouwde complexen (genoemd: MOB Bussloo, betonfabriek) en extensivering landbouw. Elke ontwikkeling "geen recht". Planologische wijziging + inrichtingsplan met **kwalitatieve verplichting**, beeldkwaliteitsplan, **anterieure overeenkomst**; natuur/erfinrichting wordt geborgd "alvorens we het gebruik van de nieuwe ontwikkeling toestaan" (door raadsamendement 30-1-2023 versoepeld: erf hoeft niet vóór de bouw te worden ingericht). Kosten procedure, bouwrijp, K&L en planschade voor initiatiefnemer. Stappenplan: 1 voorverkenning/intake (quickscan), 2 principeverzoek (college, leges), 3 landschaps- en beeldkwaliteitsplan, 4 overeenkomst, 5 milieuonderzoek + bestemmingsplanprocedure (vooroverleg provincie/waterschap; 6 weken inzage; raad; 6 weken beroep), 6 uitvoering/sloop/natuur, 7 bouw, 8 handhaving.
Voorbeeld 2 in het beleid: landgoed op niet-bestaand erf met 5,5 ha bos (22 punten) + € 50.000 recreatieve route = woning 1.500 m³ (24 punten) — typische orde van grootte.

### 3.3 Is het beleid nog van kracht? (verificatie gevraagd)
- **Formeel "tijdelijk beleid"** voor "een periode van maximaal 2 jaar" (raadsvoorstel 13-9-2022 / raadsmededeling 13-12-2022; raadsbesluit 30-1-2023; webpagina functieverandering: "geldt voor een periode van maximaal 2 jaar") [PRIMAIR, S3, S1b]. Evaluatie was toegezegd "over twee jaar na uw besluit", gekoppeld aan PLG. Motie "Informatie over Rood voor Groen" (unaniem, 17-0): tussentijds informeren, in februari 2024 [PRIMAIR].
- **Tussenevaluatie** (RM 9-7-2024, 5 p.): 26 aanvragers; **16 positieve principebesluiten** (4 op oud Rood-voor-Rood-beleid, rest RvG), 10 serieuze verzoeken lopend; 7 van 16 zonder sloop; "veel interesse in het Rood voor Groenbeleid"; "definitieve evaluatie volgt na de afronding van het PLG" [PRIMAIR, S3b].
- **PLG (26-5-2025)** noemt rood-voor-groen "een helpend instrument" en kondigt een nieuw instrument voor clusteren aan, "nu nog niet" (S9).
- **Definitieve evaluatie / verlenging / definitief beleid: niet gevonden** in Notubiz (raadsvoorstellen, mededelingen, moties 2024-2026), CVDR of Gemeenteblad (zoekopdrachten op "rood voor groen", "evaluatie", "verleng", "functieverandering").
- **Feitelijke toepassing 2026:** college-besluitenlijsten wk 5, 7, 13, 14 (2026): "past binnen de kaders van het tijdelijk Rood voor Groen beleid"; wk 37 (sept. 2026): intentie "meewerken aan ontwikkelingen (rood voor groen)" Iordensweg; Jaarstukken 2025 (raad 6-7-2026): "op basis van het tijdelijke Rood voor Groen-beleid"; ontwerp-omgevingsvisie (juli 2026): "Momenteel loopt een groot aantal pilots waarin met de aanleg van nieuwe natuur 'punten' kunnen worden verworven ... We werken in dit kader aan ons Rood voor Groen beleid"; coalitieakkoord: "onderzoeken hoe de maatschappelijke meerwaarde van het rood-voor-groenbeleid verder kan worden uitgewerkt"; Kader VHV: afwijking van betaalbaarheid mogelijk bij "grote investeringen in de ruimtelijke kwaliteit conform het Rood voor Groenbeleid" [PRIMAIR].
- **Conclusie [INT]:** beleid wordt in de praktijk nog toegepast, maar de formele 2-jaarsperiode is verstreken zonder gevonden vervolgbesluit; de definitieve vorm is gekoppeld aan de omgevingsvisie (raadsbesluit Q4 2026). Voor een principeverzoek: bij de afdeling Ruimte navragen welke versie en welk puntenstelsel gelden. Het document staat niet in CVDR (wel bekendmakingen van anterieure overeenkomsten in het Gemeenteblad).

### 3.4 Gemeentelijke houding (signalen)
- **Positief/meewerkend ("ja, mits"):** coalitie: "Wij stimuleren actief particuliere initiatieven"; dienstverlening "ja, mits"; PLG: woningbouw als middel voor leefbaarheid; voor stoppende boeren "aantrekkelijke manier om hun erf of gronden een nieuwe functie te geven".
- **Terughoudend:** PLG/Kader: clusteren in en bij dorpen, "niet wenselijk dat er op heel veel plekken nieuwe bebouwing in het buitengebied verrijst"; PLG: "Op boerenerven zijn wel ontwikkelingen mogelijk, maar alleen kleinschalig van aard. In ons productieve landschap denken we dan aan 1 tot 3 woningen. In het middengebied van Voorst zouden dit ook wat meer woningen kunnen zijn, afhankelijk van de plek en de bijdrage aan Voorst als groene hart." (S9 p.26). Coalitie: landgoederen: "beperken ongewenste verdichting in het buitengebied". Ontwerp-OV agrarisch landschap: "terughoudend met het toevoegen van nieuwe bebouwing in relatief natte gebieden", "woonfunctie mag in beginsel geen belemmeringen opleveren voor de agrarische productie".
- **Afwijzing:** college-besluit 2025 wk 6: geen medewerking aan 1-2 woningen op agrarische percelen (sectie B 814-816, nabij buurtschap Appen en landgoed De Poll): "past niet binnen ons Rood voor Groenbeleid ... ook vanuit stedenbouwkundig oogpunt niet wenselijk" [PRIMAIR, S35].
- **Instrument in ontwikkeling** (PLG p.27): "We ontwikkelen een instrument dat het mogelijk maakt dat initiatiefnemers in het buitengebied met plannen voor meerdere woningen niet op hun eigen erf, maar juist in of nabij dorpen kunnen bouwen. Dit instrument is er nu nog niet": kavelruil, verhandelbare bouwrechten, "meer (kleinere) woningen op erven nabij de dorpskernen" extra naast het rekenmodel, bv. **Plan26 Nijbroek** (Coöperatie Polder Nijbroek: gedeeld woonerf van vijf woningen, twee sociale huur voor starters).

### 3.5 Vergelijkbare omzettingen (precedenten 2023-2026) [PRIMAIR, S35, S19c, S29]
| Locatie | Besluit | Omvang | Bron |
|---|---|---|---|
| Lochemsestraat 40, **De Vecht** (voorm. agrarisch erf, rand kern) | principebesluit 17-2-2026, BOPA-route; raad niet adviesbevoegd (RM 913478) | **17 woningen**, 2/3 betaalbaar, sloop bedrijfsgebouwen, wandelpad, natuurontwikkeling; participatie nog te doen | RM 17-2-2026 |
| Landgoed **Het Nieuwe Wezeveld**, Twello | principebesluit 24-2-2026; BOPA; verevening; natuurcompensatie in provinciale GOZ | **18 appartementen** (bouwrechten maatschappelijk bouwvlak geschrapt); anterieure overeenkomst | RM 3-3-2026 |
| Plan26, **Nijbroek** (leegstaand erf) | via RvG-pilot/Coöperatie Polder Nijbroek | 5 woningen (2 sociale huur) | PLG p.27 |
| Lochemsestraat 3, Terwolde | principebesluit 2024 wk 35 | 2 woningen (750 + 900 m³); 4,5 ha landbouw → natuur, sloop 932 m² | wk 35/2024 |
| Heegsestraat 10 Terwolde + Zeedijk Nijbroek | principe 29-10-2024; vergunning juni 2026 | 1-2 woningen | wk 44/2024; wk 26/2026 |
| Vermeersweg 59 Twello | principe 16-4-2024; vergunning apr. 2026 | generatiewoning; 1,1 ha natuur | wk 16/2024; wk 14/2026 |
| Vollehandsweg 5 Terwolde; Meermuidenseweg 19A/G Twello | principebesluit feb. 2026 | 1 extra woning | wk 5, 7/2026 |
| Wilp-Achterhoek (gemeente zelf; BOPA) | RM 10-3-2026 | ± 80 woningen (fase 1), 2/3 bereikbaar | RM 10-3-2026 |
| De Zutphenboer, landgoed De Poll | provinciale pilot "Wonen op de Boerderij"; raad bindend advies | wooncoöperatie in monumentaal erf (aantal onbekend) | RM 3-2-2026 |

**Doorlooptijd principebesluit → verleende vergunning (BER uit data):** Gravenstraat 30 ≈ 28 mnd (6-6-2023 → okt. 2025); Oude Wezeveldseweg ≈ 26 mnd; Bekendijk 11 ≈ 31 mnd; Boevenbrinkstraat 8 ≈ 31 mnd; Vermeersweg 59 ≈ 24 mnd; Heegsestraat 10 ≈ 20 mnd. Wettelijke beslistermijn omgevingsvergunning 8 weken (+6) volgens gemeente-website; het grootste deel van de tijd zit in planuitwerking, onderzoeken en anterieure overeenkomst.

### 3.6 Indicatief eindoordeel vanuit gemeentelijke bestuursinformatie [INT]
| Scenario | Haalbaarheid (gemeentelijk beleid) |
|---|---|
| 3-6 woningen, bestaand erf, Rood voor Groen (4-6 wo. = 28 punten ≈ 7 ha natuur of 8.400 m² sloop) | **Goed** — in de beleidstabel; wel verplichte differentiatie vanaf 3 woningen, 2/3 betaalbaar (Kader) |
| 10-12 woningen, bestaand (voormalig agrarisch) erf aan **kernrand** | **Kansrijk maar maatwerk/lang traject**: precedent De Vecht (17) en Wezeveld (18); mogelijk bonus voor "meer kleinere woningen op erven nabij dorpskernen" (PLG); 1/3 sociaal vanaf 12 woningen; raad bindend advies waarschijnlijk (CVDR701428 lid 1a/b) |
| 10-12 woningen, bestaand erf **ver buiten kern** (productief landschap) | **Laag**: PLG noemt 1-3 woningen; middengebied "wat meer" |
| 10-12 woningen, onbebouwde agrarische grond buiten kern | **Zeer laag**: RvG gaat uit van bestaande erfstructuur (+4 punten voor niet-bestaand erf); PLG wil clusteren in/bij dorpen; geen precedent |
| 10-12 woningen onbebouwde agrarische grond **aansluitend aan dorp** (dorpsrand) | **Onzeker, wel enige ruimte**: ontwerp-OV noemt "kleinschalige wooninitiatieven" in dorpsranden (groene buffer), "kleinschalige uitbreiding aan de dorpsranden" in dorpen waar inbreiding beperkt is; maar gemeente regisseert uitbreidingen zelf (voorkeursrecht, locatiestudie) |
Indicatieve puntenberekening 12 woningen van 450 m³ [BER, speculatief; geen tabel boven 6 eenheden]: lineaire extrapolatie van 28 punten/6 eenheden ≈ 56 punten ≈ 14 ha natuur of 16.800 m² sloop ≈ € 1,1-1,4 mln investering (−2 punten bij aansluiting aan dorp).
**Contactpunt voor informeel voorgesprek:** formulier "Verken uw idee" (vergunningintaker.voorst.nl) / omgevingsvergunning@voorst.nl, 0571-27 93 35 (afdeling Ruimte/Vergunningen); beleidsmedewerker functieverandering en landgoederen: Paulien Dekker-Klein Overmeen (p.dekker@voorst.nl, 0571-27 93 43; naam uit raadsstukken 2022-2026).

---

## 4. VAB-beleid (Vrijkomende Agrarische Bebouwing)

- **Geen apart VAB-beleid;** VAB loopt via functieverandering: Rood voor Groenbeleid (nieuw, tijdelijk) en Rood voor Rood ("Waar de stallen verdwijnen" 2008, "Aanpassing regionale beleidskader functieverandering"; "Notitie ruimtelijke kwaliteit veranderende erven"), nog op website als beleid (S1b, S4). Documenten "Functieverandering en verevening", "gecorrigeerde vervangingswaarde", "het proces": op website; beeld-PDF's, niet gelezen.
- Ontwerp-OV: "(her)ontwikkeling van vrijkomende stallen en schuren" mogelijk "zolang dit landbouw in de buurt niet hindert; in ruil voor een nieuwe woning vragen we om versterking van het landschap" (agrarisch landschap); in groene buffer/mozaïek "nieuwe landgoederen" en "kleine woonerven in combinatie met nieuwe natuur, water en recreatie" (S6/S7). VAB-transformaties: "zetten we in op ontwikkelingen die de landschappelijke kwaliteit versterken ... toewerken naar Rood voor Groen beleid met een duidelijke gebiedsgerichte zonering" (p.27).
- **Woningsplitsing:** Beleidsregels woningsplitsing (CVDR743645, in werking 1-9-2025; leges BOPA woningsplitsing € 9.625 + € 150/m² boven 100 m², max € 19.625). Programma ruimtelijke kwaliteit (karakteristieke panden): uitgangspunten raad 7-4-2025 [PRIMAIR, S32/S37].
- **Provinciale ondersteuning:** pilot **"Wonen op de Boerderij"** — Voorst neemt deel via De Zutphenboer/landgoed De Poll; provincie betaalt de procesbegeleider; voorwaarde: vernieuwende woonvorm, ≥ 2/3 betaalbaar (RM 3-2-2026) [PRIMAIR, S29]. Uitkoop veehouderij: Landelijke beëindigingsregeling (LBV/LBV+), "stoppersregeling piekbelasters" — gemeente zoekt combinatie met RvG [PRIMAIR, S3b].
- Eisen aan omliggende landbouw: ontwerp-OV "Deze woonfunctie mag in beginsel geen belemmeringen opleveren voor de agrarische productie" (agrarisch landschap); coalitie: "Het verworven recht van de één moet niet leiden tot de last van een ander." 
- Collectief/coöp-precedenten: Plan26 Nijbroek (5 woningen), De Zutphenboer (wooncoöperatie), Bekendijk 11 Terwolde (kleinschalig woonzorginitiatief, wijziging Wonen→Maatschappelijk; vergunning jan. 2026).

---

## 5. Grondbeleid

- **Type:** **regisserend grondbeleid** (Nota Grondbeleid 2024, raad 25-11-2024; per project actief/faciliterend/PPS volgens afwegingskader; evaluatie 2028) [PRIMAIR, S10]. Uitgifte: verkoop tegen marktconforme prijs (comparatief/residueel); **erfpacht/opstal**: "Gronden voor gebiedsontwikkelingen worden in beginsel beperkt in erfpacht en/of opstal uitgegeven"; specifieke situaties aan college voorgelegd. Grondverwerving: raad stelt €2 mln/jaar beschikbaar; voorkeursrecht (Wvg) toegepast (Twello-Noord 2019, Engelenburg-West 2025). Coalitie: "positieve gemeentelijke grondhouding ('ja, mits')", onderzoekt "grondbank" voor agrariërs en actiever grondbeleid (reactienota GL-PvdA).
- **Grondposities buitengebied:** gemeente koopt strategisch (Wilp-Achterhoek Bosgoed-terrein, Voorst-West-gronden deels, gronden Iordensweg Twello); geen overzicht van agrarische grondposities gevonden; Nota Grondbeleid noemt "strategische gronden" (taxatie 2-jaarlijks).
- **Grondprijs:** marktconform; CPO Hessenlaan: ondergrens € 665.000 incl. btw voor 1.705 m² (= ca. **€ 390/m²** of ca. € 110.800 per woning [BER]); Bongerdskamp 6a Voorst: vanafprijs € 245.000 incl. btw voor ca. 765 m² (vrijstaand; hoogste bieder; jan. 2023). Winkler Prins (14 betaalbare koopwoningen): max. VON € 350.000 (tussen)/€ 360.000 (hoek); uitvraag 17-12-2025 t/m 2-2-2026.
- **Actueel kavelaanbod (18-10-2026):** **geen direct beschikbare (zelfbouw/CPO-)kavels**; op kavelpagina's (S4b): Hessenlaan (voorlopig toegewezen), Bongerdskamp 6a (toegewezen), Dorpszicht fase 1 (8 kavels uitgegeven), Dorpszicht fase 2 appartementen (voorlopig toegewezen), Park van Teuge fase 1+2 (geen kavels), De Schaker Twello (geen), Nijbroek (14 kavels toegewezen), De Vecht (toegewezen), Winkler Prins (uitvraag 14 koopwoningen afgesloten feb. 2026; uitkomst niet gevonden). Proces kavels: inschrijfformulier → preadvies welstand ≤ 12 wkn → verkoopovereenkomst → aanvraag vergunning ≤ 8 wkn; loting of hoogste bod. Contact: Jerry Beer (j.beer@voorst.nl, 0571-27 92 42), Arjan Klein (a.klein@voorst.nl, 0571-27 92 65).
- **Grote ontwikkellocaties (gemeentelijke grondpositie):**
  | Locatie | Aantal | Status | CPO-reservering |
  |---|---|---|---|
  | Twello-Noord (Nieuw Basselt & Fliertlanden) | max. 289 | bp 7-2-2022; RvS tussenuitspraken 14-5-2025 en 11-3-2026 (kernkwaliteit Nationaal Landschap Veluwe, "open es" Basseltse Enk); tweede herstelbesluit raad 13-7-2026; zienswijze 30-9-2026; wacht definitieve RvS-uitspraak; voorkeursrecht 2019 | niet gevonden (hofjes, micro-wonen) |
  | Wilp-Achterhoek | ± 80 (fase 1) | BOPA-route, raad bindend advies | niet gevonden |
  | Voorst-West | ± 150 | concept-stedenbouwkundig plan; definitief Q4 2026; procedure Q2 2027 | niet gevonden ("hofjes en betaalbare woonvormen") |
  | Winkler Prins, Voorst | 14 koopwoningen (+ IJsseldal Wonen 13 sociale huur herbouw) | bp 2024; uitvraag 2025-26 | nee |
  | Lindeboomsland, Twello (Roosdom Tijhuis/Bouwfonds) | n.n.b. | inloop 2023; schetsen | nee |
  | Dorpszicht fase 2 Terwolde | 9 appartementen | uitvraag 2024 | nee |
  | Hietweideweg/Jupiter Twello | ca. 72 | bouw gestart 2025 | hofjesconcept levensloopbestendig |
  | Spoorzones Voorst (woondeal-sleutelproject, [PB] 400-600) | — | geen eigen projectpagina; coalitie: stationsgebied Twello, 6 lagen | niet gevonden |
- **Plancapaciteit:** Jaarstukken 2025 (raad 6-7-2026): "woningbouwplannen voor ongeveer 1.600 woningen in de gemeente Voorst. Bij een aantal van deze projecten zijn we nog in de verkennende fase" t.o.v. afspraak 1.000 (2025-2034) → ca. **160%** [BER; hard/zacht niet uitgesplitst] (2023: 110% totaal, 75% hard [PB]). Bewuste reserve voor initiatieven van derden: niet gevonden; wel BOPA-route voor particuliere initiatieven (De Vecht 17, Wezeveld 18) die als bijdrage aan de woondeal worden gepresenteerd.
- **Woningbouwtempo:** gerealiseerd 2022-2024: 361 (138%), 2024: 97 [PB]; 2025 (Jaarstukken): o.a. 15 Duistervoordseweg, 20 Stationsstraat-Veilingstraat, ± 20 Enklaan Posterenk, 5 Hessenlaan; Kader: "met de huidige capaciteit realiseren wij ongeveer negentig woningen per jaar"; doelstelling **125/jaar** vanaf 2026 (625 t/m 2030/31 + 500 in 2031-2034 = 1.125); woondeal 100/jaar. Sociale huur-nieuwbouw opgeleverd: 16 (2023), 5 (2024), 0 (2025); verwacht medio 2027 68 (Winkler Prins, Hietweideweg/Jupiter, Duistervoordseweg) [PRIMAIR, S11d].
- **Regionale opgave:** woondeal Stedendriehoek 2025-2034 Voorst 1.000 (302 sociale huur; 20 middenhuur; 350 betaalbare koop = 67% betaalbaar) [PB §1.5.2].

---

## 6. Praktijkvoorbeelden (2024-2026) [bestuursinformatie-perspectief; nieuws door deelonderzoek 3]

| Voorbeeld | Datum | Relevantie voor Hanzedorp | Bron |
|---|---|---|---|
| Principebesluit 17 woningen De Vecht (voorm. agrarisch erf) | 17-2-2026 | Eerste grotere woningbouw op voormalig agrarisch erf zonder raad-adviesrecht; 2/3 betaalbaar; participatie als voorwaarde | S19c |
| 18 appartementen landgoed Het Nieuwe Wezeveld | 24-2/3-3-2026 | Landgoed + bouwrechten schrappen; GOZ-compensatie; verevening | S19c |
| Nieuw landgoed met crematorium (5,9 ha), raad bindend advies | 10-3-2026 | Toepassing nieuw-landgoederenbeleid + raadsadvies (3 drempels) | S19b |
| Verwijsde 1-2 woningen agrarische percelen Appen/De Poll | 2025 wk 6 | Afwijzing buiten RvG-punten en stedenbouw | S35 |
| Hessenlaan Teuge CPO (5 woningen gerealiseerd 2025) | 2023-2025 | Enige CPO; inbreiding | S21, S22 |
| Motie "We wachten al zo lang" → geen huisvestingsverordening nieuwbouwkoop | 25-3-2024 / 14-10-2025 | 56% nieuwbouwkopers al lokaal; geen lokale voorrangsregel | S26 |
| Raad: Woningsplitsing-amendementen; legesdebat | 2025 | Leges kostendekkend (CDA, GL-PvdA/SGP moties) | S3c |
| Aanvraag omzetting agrarisch → wonen Holthoevensestraat 22 Teuge | 20-12-2024 | Ingekomen stuk | S27c |
| Zienswijze Provinciale Omgevingsvisie: eigen zienswijze "functieveranderingsbeleid" | wk 22/2026 | Voorst wil lokale functieveranderingsruimte behouden | S35 |
| GS Gelderland dient bezwaar in tegen vergunning zonnepanelen Beelelaan 2A | wk 25/2026 | Voorbeeld provinciale betrokkenheid (toetsing art. 5.90 OVG) | S35 |

---

## 7. Inventarisatie bestaande initiatieven

| Initiatief | Woningen | Status | Relevantie |
|---|---|---|---|
| **CPO Hessenlaan, Teuge** (gem. grond, bp Hessenlaan 3-7-2023, bedrijf→wonen) | 5-6 (max 6), rijwoningen, nul-op-de-meter, levensloopbestendig, vrije sector | Uitvraag 11-10 t/m 27-11-2023; "voorlopig toegewezen"; Jaarstukken 2025: 5 woningen gerealiseerd; winnende CPO-groep niet gevonden | Precedent kleinschalig CPO in kern; geen buitengebied |
| **Woongroep Teuge** | n.n.b. | Brief 8-6-2026 aan raad | Actieve collectieve initiatiefnemers in Teuge |
| **Plan26, Nijbroek** (Coöperatie Polder Nijbroek) | 5 (2 sociale huur) | Gerealiseerd/voorbeeld in PLG | Lokaal coöperatief erf |
| **De Zutphenboer/Santstein, landgoed De Poll** (Boeren, Wonen & Natuur, Open Kaart, Waterschap, Regio, RCE; provinciale pilot) | wooncoöperatie, aantal n.n.b.; plus 3 woningen Soerhuislaan | IBB 19-1-2026; Verken uw idee; raad bindend advies | Meest vergelijkbaar buitengebied-collectief |
| Bekendijk 11 Terwolde | kleinschalig woonzorginitiatief | Vergunning jan. 2026 | Zorgcollectief |
| Wooncoöperatie-brieven (Cooplink) | — | 2024 | Landelijke druk |
Niet gevonden: andere CPO's, zelfbouwverenigingen, Knarrenhof; woningcoöperaties met gemeentelijke grond.

---

## 8. Huisvestingsverordening

- **Ja/nee:** **Nee** — Voorst heeft **geen huisvestingsverordening** (geen CVDR-treffers voor Voorst/Stedendriehoek; titelzoek). Het college besloot (RM 14-10-2025, nr. 860773) **geen** huisvestingsverordening voor lokale/maatschappelijke binding bij nieuwbouwkoop op te stellen (Kadaster 2020-2024: 56% van nieuwbouwkopers woonde al in Voorst; 6,3% terugkeerder; totaal 62,3%) — "juridisch niet te onderbouwen". Motie "We wachten al zo lang" (25-3-2024) had 50% voorrang tot € 390.000 gevraagd [PRIMAIR, S26].
- Sociale huur: regionale toewijzing via **Woonkeus Stedendriehoek** met "voorrang landelijk gebied" (Kader p.4); uitgangspunt max. 30% vrijkomende sociale huur naar bijzondere/urgente doelgroepen (Kader).
- **Verordening sociale koop- en huurwoningen** (CVDR120802/2, geldend 14-12-2023): doelgroep sociale koop: inkomen ≤ € 60.000 (peiljaar); huur: Bth-grens; instandhouding sociale huur ≥ 10 jaar, sociale koop ≥ 5 jaar; hardheidsclausule [PRIMAIR, S31c]. Kader VHV: sociale koop ≤ € 300.000 (prijspeil 2026, CPI-geïndexeerd), doelgroep inkomen ≤ € 75.000 (cao-geïndexeerd), op te nemen in omgevingsplan ter vervanging van de verordening (tot dan geldt de verordening).
- **Minimumpercentage sociale huur:** beleid ≥ 2/3 betaalbaar waarvan 30% sociale huur (landelijk); gemeentelijk: alle plannen ≥ 2/3 betaalbaar; vanaf 12 woningen ≥ 1/3 sociale huur of koop (Kader p.3).
- **Gronduitgifteregeling 2020:** geen bindings-/voorrangseisen; loting via notaris.

---

## 9. Zelfbouwloket / contactpersoon

- **Geen zelfbouwloket of CPO-loket.** Aanspreekpunten:
  - **Verken uw idee** (intake voor bouw-/ruimtelijke ideeën, incl. functieverandering/BOPA): https://vergunningintaker.voorst.nl/direct/Verken_uw_idee ; omgevingsvergunning@voorst.nl; 0571-27 93 35 / 0571-27 99 11. Leges: 15% van de leges bij daadwerkelijke aanvraag (min. € 184,60); bij BOPA met uitgebreide onderbouwing € 1.031,25 (projectgebied < 5.000 m²) / € 1.706,05 (5.000-100.000 m²); omgevingsoverleg (intake-/omgevingstafel) € 773,35 per keer [PRIMAIR, S5, S33].
  - **Grondzaken/kavels:** Jerry Beer (j.beer@voorst.nl, 0571-27 92 42); Arjan Klein (a.klein@voorst.nl, 0571-27 92 65).
  - **Beleid wonen:** Gerben Beunk, beleidsadviseur wonen (g.beunk@voorst.nl, 0571-27 99 12) [raadsstukken 2025-2026].
  - **Functieverandering/landgoederen:** Paulien Dekker-Klein Overmeen (p.dekker@voorst.nl, 0571-27 93 43).
  - **Starterslening:** Oscar Swartjes (o.swartjes@voorst.nl, 0571-27 98 01).
  - **Bestuurssecretariaat** (college): bestuurssecretariaat@voorst.nl, 0571-27 93 24. **Griffie:** raad@voorst.nl, 0571-27 92 17.
  Namen komen uit raadsstukken/website en kunnen wijzigen.

---

## 10. Bestuurlijk klimaat

- **College** (S8 en website, S4c): burgemeester **Paula Jorritsma-Verkade**; wethouders **Robert Bosch** (1e locoburgemeester; **Ruimtelijke ordening; Wonen en woningbouw**; Klimaat en energietransitie; Afval/circulariteit; Vergunningverlening; Openbare ruimte; Landschap, waterbeheer en biodiversiteit; dorpswethouder Klarenbeek, Steenenkamer, Posterenk, Teuge; benoemd 6-7-2026; r.bosch@voorst.nl; zat t/m juli 2026 in de raadsfractie Gemeente Belangen [INT]); **Rosmarijn Boender** (2e locoburgemeester; **Grondexploitatie**; Cultuurhistorie en landgoederen; Economie; Financiën; Gemeentelijke gebouwen; benoemd 6-7-2026; lid DB VVD-Hanzenetwerk → waarschijnlijk VVD [INT]); **Daniëlle Beumer(-Röthengatter)** (3e locoburgemeester; Jeugd/Onderwijs, Kunst/cultuur, Integratie/asiel, Werk/inkomen, Wmo, Gezondheid, Sport; benoemd **7-9-2026** met 17 stemmen voor; partij niet vastgesteld, vermoedelijk VoortvArend Voorst [INT]); gemeentesecretaris Lisette Wolbers(-Cents). De website-tekst "Er zijn nu twee wethouders" is verouderd. Vorige wethouder wonen: Henk van Zeijts (t/m ca. 6-7-2026), eerder Bert Visser.
- **Raad (21 zetels), verkiezing 18-3-2026** (S28): Gemeente Belangen 5 (3.034 st.), VoortvArend Voorst 5 (2.708), GroenLinks-PvdA 3 (1.580; fractie heet inmiddels **PRO**), Lokaal Liberaal 2 (1.533), CDA 2 (1.406), VVD 2 (1.282), D66 1 (892), SGP 1 (581). Opkomst: 13.070 toegelaten kiezers.
- **Coalitie:** verkenner Jan Herman de Baas (rapport 16-4-2026) adviseerde GB + VoortvArend + VVD; akkoord **"Natuurlijk Voorst!" 2026-2030** gepresenteerd 26-6-2026, besproken/ vastgesteld in raad 6-7-2026 (12/21 zetels). **Geen coalitie in vorming** per 2026-10-18. Voorgaande periode: coalitie (2022) CDA, VVD-Liberaal2000, VoortvArend, PvdA-GroenLinks ("Samen beter") [WF/S39]; fractiebreuk VVD-Liberaal2000 → Lokaal Liberaal + VVD (motie "Liberaal echec", 12-1-2026 [PRIMAIR]). Eerdere driver CPO/duurzaam: niet vastgesteld.
- **Relevante passages coalitieakkoord** [PRIMAIR, S8]:
  > "Wij stimuleren actief particuliere initiatieven en lokale betrokkenheid. Waar mogelijk versnellen wij procedures en uitvoering, met behoud van kwaliteit en draagvlak. Verder onderzoeken wij hoe de maatschappelijke meerwaarde van het rood-voor-groenbeleid verder kan worden uitgewerkt. En op deze wijze een oplossing kan bieden voor diverse sociale opgaven." (p.12)
  > "Waar dit passend en uitvoerbaar is, willen wij ruimte bieden aan geclusterde woonvormen en andere maatwerkoplossingen die bijdragen aan zowel maatschappelijke opgaven als aan een betere benutting van de woningvoorraad door woningsplitsing." (p.10)
  > "In de middelgrote dorpen Klarenbeek, Voorst en Terwolde hanteren wij het uitgangspunt om te bouwen naar behoefte ... Ook in de andere dorpen is het uitgangspunt bouwen naar eigen behoefte, met name voor starters, ouderen en doorstromers." (p.12) — "Gelet op de dubbele vergrijzing is een sterker accent nodig op woningen voor ouderen." (p.10) — "bouwtempo van circa 125 woningen per jaar" (p.10).
  > "Dienstverlening die uitgaat van 'ja, mits': uitnodigend en oplossingsgericht" (p.22). Buitengebied: "Ook bij landgoederen ... beperken wij ongewenste verdichting in het buitengebied om het landelijk karakter te bewaren" (p.17); agrarisch: grondbank verkennen, "Het verworven recht van de één moet niet leiden tot de last van een ander" (p.14).
- **Indicatie ruimte voor CPO [INT]:** gunstig voor kleinschalig/collectief in/aan dorpen en voor ouderen- en starterswoningen; coalitie noemt CPO niet; Woongroep Teuge en D66/GL-PvdA-geluiden (niet onderzocht) kunnen steun bieden. Partijprogramma's niet onderzocht.

---

## 11. Kostenverhaal en leges

- **Nota Grondbeleid 2024** (S10): voorkeur voor **anterieure overeenkomst** (privaatrechtelijk) boven kostenverhaalsregels in omgevingsplan; afdeling 13.6 Ow; financiële bijdragen (art. 13.22/13.23 Ow) voor o.a. "evenwichtige samenstelling woningvoorraad" = **vereveningsbijdrage** aan Vereveningsfonds Sociale Woningbouw (sinds 2012; saldo 1-1-2026 ruim € 300.000); gemeente onderzoekt aparte Nota kostenverhaal/programma; Exploitatieverordening 2006 en delegatiebesluit exploitatieplannen bestaan nog. Geen exploitatieplan bij Hessenlaan.
- **Vereveningstabel (bijlage F, versie maart 2026; 67% betaalbaar):** grondgebonden woningen: 1 wo. € 50.000; 2: € 65.000; 3: € 100.000; 4: € 135.000; 5: € 170.000; 6: € 200.000; 7: € 235.000; 8: € 270.000; 9: € 300.000; **10: € 335.000**; niet-grondgebonden: factor × € 25.000 (10: € 167.500). Boven 10 "etc." — lineaire extrapolatie (+ ca. € 33.500-35.000 per woning) geeft **ca. € 370.000 (11) en ca. € 400.000 (12) voor grondgebonden** [BER, niet door gemeente bevestigd]. Verevening is bedoeld voor plannen die de 2/3-betaalbaarheid niet halen (afwijkingsgronden: grote RvG-investeringen; plan bestond al; concrete behoefte duurdere woningen, "zeer terughoudend"; landschappelijk/stedenbouwkundig geen betaalbare woningen wenselijk). Juridische basis: Volkshuisvestingsprogramma (nog niet vastgesteld) — tot dan Woonvisie-structuurvisie-constructie.
- **Anterieure overeenkomsten RvG:** college sluit overeenkomst per project; bekendmaking art. 16.138 Ow in Gemeenteblad (bv. Gravenstraat 30, 5-8-2025; Holthoevensestraat 3/3A, 27-11-2024; Heegsestraat 10, 29-1-2026): "Over deze overeenkomst kunt u geen zienswijzen indienen", stukken 2 weken ter inzage; contact Anna Zabihi 0571-27 92 07.
- **Planschade:** voor rekening initiatiefnemer volgens RvG-beleid; Verordening nadeelcompensatie 2022.
- **Leges** (Legesverordening Voorst 2026, raad 15-12-2025; eerste wijziging geldend vanaf 1-10-2026, CVDR753300/2; Tarieventabel 2026) [PRIMAIR, S33]:
  - Bouwactiviteit (technisch, art. 2.5): 1,13% tot € 1 mln bouwkosten (min. € 184,60); 0,94% € 1-5 mln; 0,75% € 5-10 mln.
  - Omgevingsplanactiviteit bouwen (art. 2.6): 3,40% tot € 1 mln; 3,14% € 1-5 mln; 2,58% € 5-10 mln; daarbovenop BOPA beknopt € 731,10 of **BOPA met uitgebreide onderbouwing (nieuwe hoofdgebouwen): € 9.625,00 (projectgebied < 5.000 m²), € 15.922,90 (5.000-100.000 m²), € 25.029,75 (> 100.000 m²)**. Woningsplitsing-BOPA € 9.625 (+ € 150/m² > 100 m²; max € 19.625).
  - Voorfase "verkennen en begeleiden initiatieven": 15% van toekomstige leges (min. € 184,60); BOPA uitgebreid: € 1.031,25/€ 1.706,05/€ 2.681,75; conceptverzoek € 257,80; omgevingsoverleg € 773,35 per overleg; externe adviseur € 128,85/uur.
  - **Indicatieve berekening voor 12 woningen, bouwkosten aangenomen € 4,8 mln (12 × € 400.000), projectgebied 5.000-100.000 m² [BER, sterk aannameafhankelijk; tarieven zouden gecumuleerd worden volgens art. 2.3 lid 2 — verifiëren bij gemeente]:** technisch € 11.300 + € 35.720 = € 47.020; omgevingsplanactiviteit € 34.000 + € 119.320 = € 153.320; BOPA-uitgebreid € 15.922,90; totaal ≈ **€ 216.000** (+ verken-uw-idee ± € 1.700-2.500). Raadsmotie "Kostendekkendheid leges" (10-11-2025) en CDA-wens "kostendekkende leges" wijzen op verhoging; CVDR753300 gewijzigd per 1-10-2026.
- Overige kosten: Sloop, onderzoeken, welstandsadvies (€ 128,85 per max. 3 adviezen), voorfinanciering plankosten CPO (brochure).

---

## 12. Woningbehoefte en doelgroepen

- **Woningmarktonderzoek Companen (eind 2023; RM 30-1-2024):** woningbehoefte 2022-2033 ≈ 1.000 woningen; groei ± 1.270 huishoudens tot 2040; tekort aan compacte en goedkopere grondgebonden koop, betaalbare huur voor kleine huishoudens en levensloopgeschikte woningen; bereikbaar segment (tot ≈ € 355.000) sterk afgenomen; koop 2/3 van voorraad; > 25% van de woningen in het buitengebied; aanbevelingen: woonconcepten ouderen centrale opgave, ≥ 30% sociale huur, compacte woningen, gedifferentieerd programma, meer appartementen in Twello [PRIMAIR, S20].
- **Kader VHV 2026/2027:** drie prioritaire groepen: (1) sociale huur (1-2-persoonshuishoudens), (2) starters/jongeren/jonge gezinnen (betaalbare koop), (3) senioren (levensloopbestendig; betaalbaar én duurder). Verschuiving van gezinnen naar deze groepen; vergrijzing; Primos: +2.190 inwoners/+630 huishoudens tot 2050. Betaalbaar 2026: sociale huurgrens € 932,93; liberalisatiegrens € 1.228,07; betaalbare koop € 420.000; sociale koop € 300.000. Actief woningzoekenden sociale huur: 2023 652; 2024 543; 2025 694; zoektijd ± 16 maanden (2024) [PRIMAIR, S11d].
- **Woonzorgvisie Voorst 2023-2027** (raad; uitvoeringsprogramma): ruimte voor kleinschalige initiatieven (CPO, verticale splitsing, woonzorgconcepten) [PRIMAIR, S13]. Afsprakenkader ouderenhuisvesting Stedendriehoek: Voorst 385 nultreden/105 geclusterd/80 zorggeschikt [PB §1.4.4e].
- **Ontwerp-omgevingsvisie:** nieuwbouw "voornamelijk op behoeften van starters, senioren en andere 1- tot 2-persoonshuishoudens"; "compacte en gestapelde bouw" in de dorpen; Voorst-West: 15 woningen/jaar autonome groei dorp.
- **Aansluiting CPO-concept (Hanzedorp) [INT]:** CPO met levensloopbestendige/senioren- of starterscomponent past bij prioriteiten; 10-12 vrije-sector woningen op agrarische grond sluit slechter aan (gemeente: "niet alleen grote woningen in het dure segment", gezinsbouw niet prioritair); ≥ 2/3 betaalbaar vereist tenzij onderbouwde afwijking (RvG-investering of concrete behoefte via initiatiefgroep: "zeer terughoudend").

---

## Twee kernvragen (gemeentelijk perspectief; provinciale laag zie masterprompt)

1. **Wonen in het buitengebied (10-12 woningen buiten de kernen):** gemeentelijk beleid biedt formeel de route (RvG-puntenstelsel, BOPA) maar **schaalt tot enkele woningen per erf** en wil grotere aantallen **clusteren in/rond dorpen**. Recent zijn wel 17-18 woningen op voormalig agrarisch erf/landgoed aan kernranden in principe toegestaan (maatwerk, 2/3 betaalbaar, verevening). Eindoordeel: **beperkt tot kansrijk bij kernrand/bestaand erf; kansarm op onbebouwde grond ver van de kern**. Provinciale laag (GOZ 20% gemeentegebied, art. 5.64, Nationaal Landschap Veluwe, hoogwatergeul-reservering Twello-Steenenkamer) vergroot onzekerheid.
2. **Agrarische herbestemming op deze schaal:** vereist BOPA/omgevingsplanwijziging, anterieure overeenkomst, natuur/landschapsinvestering (orde 56 punten ≈ 14 ha natuur voor 12 woningen [BER]) en waarschijnlijk raadsadvies; geen gevonden precedent van ≥ 10 woningen via Rood voor Groen. Eindoordeel: **mogelijk als maatwerk in samenwerking met gemeente (eventueel als dorpsrandproject), niet als standaardtraject**.

---

## Bijlage B — Gelderland-controlepunten (Voorst)

*Status: G = gevonden; NG = niet gevonden; N/V = niet van toepassing; T = tegenstrijdig. Primair-1-punten zijn volledig uitgewerkt; overige aangevuld. 'Waar te vinden' bij NG.*

| # | Bevinding | Status | Bron / datum | Waar te vinden (NG) |
|---|---|---|---|---|
| **A1** | Woondealregio **Stedendriehoek** (grensoverschrijdend: Deventer). Afspraak 2025-2034: **1.000** (600 + 400); realisatie 2022-2024: 361 = 138% [PB]. Ontwerp-Omgevingsvisie provincie: dorpen/kleine kernen [PB]. Gemeente ondersteunde regionale zienswijze op provinciale ontwerp-omgevingsvisie ("mits alinea logistiek cluster A50 geschrapt") en diende **eigen zienswijze** in met aandacht voor "functieveranderingsbeleid, gebiedsvisie De Kar, luchthaven Teuge" (college wk 22/2026). Inhoud zienswijze niet gelezen. Ook zienswijze op ontwerp-wijziging Omgevingsverordening (wk 12/2026: economie, werklocaties, energie, klimaatadaptatie, bosgroeiplaatsen). | G (inhoud zienswijze NG) | S35 wk 12, 22/2026; S2; PB | Stukken college of Statenstukken; griffie raad@voorst.nl |
| **A2** | Plancapaciteit ca. **1.600** woningen vs 1.000 (Jaarstukken 2025) → ± 160% [BER]; hard/zacht niet uitgesplitst; kleine projecten: niet vast te stellen of CPO telt mee; De Vecht (17) en Wezeveld (18) worden aan woondeal gekoppeld ("sluit aan bij Regionale Woondeal 2025-2034"). Lokaal 'reserve'-percentage niet gevonden. | G/NG (hard/zacht en monitor NG) | S36 p.18-19; RM 17-2-2026 | LMVW/planmonitor, afdeling Ruimtelijke ontwikkeling (G. Beunk) |
| **A3** | Afwijking art. 5.64 lid 2: geen gevonden voorbeeld of overweging; gemeente beoordeelt "past binnen woondeal" per project (RM De Vecht). | NG | — | Statenstukken/GS-besluiten instemming; regio Stedendriehoek |
| **A4** | Betaalbaarheid: alle plannen ≥ 2/3 betaalbaar (≤ € 420.000 koop 2026; sociale koop ≤ € 300.000, inkomen ≤ € 75.000; vanaf 12 woningen ≥ 1/3 sociaal), verevening (bijlage F maart 2026). Geen huisvestingsverordening Voorst; regionale koopprijsgrens Noord-Veluwe n.v.t. Prestatieafspraken IJsseldal Wonen/HBV 2023-2026 (jaarschijf 2024-26). Geldt expliciet ook voor CPO? Niet gevonden — algemeen geformuleerd ("alle nieuwbouwplannen"). | G | S11, S11d, S25 | Prestatieafspraken 2027+ (IJsseldal Wonen) |
| **A5** | Kader Volkshuisvesting 2026/2027 (9-3-2026) = kader; **Volkshuisvestingsprogramma 2026/2031 niet vastgesteld, ontwerp niet gevonden**; wijst nog geen buitengebied-locaties aan. Ladder: niet in beleid genoemd. Eigen 11/12-grens: niet gevonden; wel "vanaf 12 woningen" in Kader (sociaal 1/3). | G (programma NG) | S11, S11c | Gemeenteblad/overheid.nl, Omgevingsloket "Regels op de kaart" na terinzagelegging |
| **A6** | Ouderenhuisvesting: Afsprakenkader SD (385/105/80) [PB]; Woonzorgvisie 2023-2027 (CPO als voorbeeld); Kader: aandacht senioren, geclusterd; coalitie: accent ouderen; aanjaagteam WWZ ingekomen 23-6-2025. Lokale huisvestingsverordening/urgentie: regionaal Woonkeus; lokaal geen. | G | S11, S13, S8 | — |
| **B1** | Kader: **Rood voor Groenbeleid** (tijdelijk, 31-1-2023; beleidsregel, geen CVDR-nummer; bekendmakingen anterieure overeenkomsten in Gemeenteblad) + **Rood voor Rood** (Waar de stallen verdwijnen 2008/Notitie ruimtelijke kwaliteit 2009) naast elkaar; **Nota Landgoederen 6-2-2006**; Woningsplitsing CVDR743645. Geldigheid: tijdelijk, 2 jaar verstreken, geen formele verlenging gevonden, wel toegepast t/m sept. 2026 → zie T1. | **T** (status) | S1, S3, S7, S35 | Afdeling Ruimte; raadsbesluiten Q4 2026 (omgevingsvisie/Programma) |
| **B2** | Rekenmethode: punten (1 punt = 0,25 ha natuur / 300 m² sloop / 1.500 m² kassen / € 25.000); ervenconsulent/Gelders Genootschap alleen bij twijfel over karakteristiek (restauratie). Art. 5.33-invulling "per saldo versterking": landschapsplan/beeldkwaliteitsplan, LOP "Van Veluwe tot IJssel", Welstandsnota. Provinciale GOZ-rekentool: Wezeveld natuurcompensatie in GOZ; verder NG. | G | S1; RM 3-3-2026 | Provinciale GOZ-handleiding; afdeling Ruimte |
| **B3** | Tabel tot 6 wooneenheden/3.000 m³ (28 punten); daarboven maatwerk; PLG: 1-3 woningen productief landschap, meer in middengebied; precedenten ≥ 10: De Vecht 17, Wezeveld 18, Wilp-Achterhoek ± 80 (gemeentelijk). Geen RvG-precedent > 2 woningen. | G | S1, S9, S19c | — |
| **B4** | Niet vervallen regionaal kader formeel: "Waar de stallen verdwijnen" nog op website; gemeente verwijst nog naar "Regionaal Afsprakenkader Woningbouwprogrammering". Voorst vroeg in zienswijze (wk 22/2026) aandacht voor "ons functieveranderingsbeleid" bij provinciale visie (regionaal beleid wordt bestreden door SD-gemeenten [PB]). Opname in omgevingsplan: BOPA-route; omgevingsplan (CVDR696255) bevat tijdelijk deel; Delegatiebesluit Omgevingsplan 2025. Herziening aangekondigd: ja via omgevingsvisie/PLG-instrument (kavelruil/verhandelbare bouwrechten). | G | S1b, S9, S35 | — |
| **B5** | Ontwerp-OV: eerst inbreiding binnen dorpscontouren; uitbreiding aan dorpsranden "afronding"; groene buffer: dorpsranden voor "kleinschalige wooninitiatieven". Contouren: visiekaart (juli 2026, PNG) niet juridisch; geen contour-document. Voorst-West = gemeentelijke uitbreiding. | G (contour NG) | S6 p.45-46, 57; S19 | Visiekaart; omgevingsplan |
| **B6** | Kwaliteitsinvestering: natuur, sloop, restauratie, recreatieve routes, landschapsplan; afdwingen via **kwalitatieve verplichting/voorwaardelijke verplichting + anterieure overeenkomst**; geen "binnen vijf jaar" gevonden; stikstof: RvG noemt reductie bij stoppers; geen gemeentelijke eis tot beschikbaarstelling stikstofruimte gevonden (Voorst ligt buiten stikstofstrook [PB]); Winkler Prins: elektrische hijskraan vanwege stikstof. | G | S1, Gemeenteblad S38, S18 | — |
| **C1** | GOZ 20,0% van gemeentegebied, 22,8% van landbouwgrond; GNN 10,8%/4,5% [PB]. Gemeentelijk: Wezeveld "natuurcompensatie binnen de provinciale GOZ". Rekentool: niet gevonden voor andere gevallen. | G (PB) / deels NG | PB §1.6.8; RM 3-3-2026 | Deelonderzoek 2 (geodata) |
| **C2** | Weidevogel Epseweerdse Polder-Wilpse Klei 1,8%/2,5%; ganzenrust IJsseluiterwaarden 6,8%/8,5% [PB]. Gemeente: terughoudend met bebouwing in natte gebieden; ruimtereservering **hoogwatergeul Deventer-Twello** (Rijk) tussen Twello en Steenenkamer: "geen kapitaalintensieve ontwikkelingen" (ontwerp-OV p.67). | G | PB; S6 p.67, 28 | Deelonderzoek 2 |
| **C3** | Voorst: geen beperkingengebied stikstof [PB]; Natura 2000 Rijntakken (uiterwaarden), Veluwe 4,3%; Twello-Noord blijft RvS-toets; ontwerp-OV: reductie stikstofdepositie rond IJssel. Gemeente stelt geen stikstofruimte-eis. Streekregel Veluwe: n.v.t. maar Nationaal Landschap Veluwe 69,9% (Twello-Noord toets art. 2.56 OVG). | G | PB; RM 30-6-2026 | Deelonderzoek 2/3 |
| **C4** | Streek IJsselvallei (99,9%) [PB]; Nationaal Landschap Veluwe 69,9%; kernkwaliteiten onderdeel RvS-uitspraak 11-3-2026 ("open es" Basseltse Enk). LOP "Van Veluwe tot IJssel" (3 delen, website), Welstandsnota, Programma Landelijk Gebied (groene buffer/middengebied/productief landschap). | G | S2, S23, S6 | — |
| **C5** | Waterwingebied Twello (beschermingszone) en reserveringsgebieden oeverwaterwinning Wilpse/Nijenbeekse/Voorsterklei (ontwerp-OV p.28); waterschap Vallei en Veluwe bij gebiedsprocessen. Klimaatrisicoanalyse art. 5.85: niet gevonden. | G (klimaatrisicoanalyse NG) | S6 p.28 | Waterschap; provinciale kaarten |
| **C6** | Voorst heeft **geen onderstation**; congestiegebied; **Beleidsregels rangschikking transportcapaciteit onderwijs- en woningbouwprojecten 2026** (CVDR765873, in werking 28-8-2026): aanvragen volgordelijst t/m 6-9-2026; rangorde: start bouw, projectrijpheid (o.a. BOPA aangevraagd/verleend, anterieure overeenkomst, beslissing Verken uw idee), maatschappelijk belang. Coalitie: "vanaf 1 juli 2026 ook voor kleinverbruikers het prioriteringskader". Voorst-West: netneutraal. Pilot netbewust prioriteren (verdeelstation Harderwijk) raakt Voorst niet [PB]. Bodemenergie ≥ 15 wo.: n.v.t. onder 15. | G | S33b; S8 p.17-18 | Netbeheerder; afdeling Ruimte (volgordelijst) |
| **D1** | Zie §4: gemeentelijk beleid = RvG/Rood voor Rood; max. aantal: tabel 6 eenheden; eisen omliggende landbouw (geen belemmering); collectieve precedenten: Plan26 Nijbroek (5), De Zutphenboer (wooncoöperatie), Hessenlaan (CPO, kern). VAB als aparte opgave in programmering: ontwerp-OV noemt VAB in diverse zones; woondeal niet. | G | S1, S6, S9, S29 | — |
| **D2** | **Pilot "Wonen op de Boerderij": ja** (De Zutphenboer/De Poll; provincie betaalt procesbegeleider; vernieuwende woonvorm, ≥ 2/3 betaalbaar). Expertteam RVO, Rijkshandreiking, Atelier Gelderland, Handreiking Collectieve Wooninitiatieven, mini-leerlijn: niet gevonden voor Voorst. Gelders Genootschap: genoemd in RvG-beleid (advies bij twijfel karakteristiek). Overleg met provinciale Erfgoed/RCE: ja (Voorst-West, De Poll). | G (rest NG) | RM 3-2-2026 | Provincie Gelderland (Versnellingsteam/pilotcoördinator); gemeente (P. Dekker) |
| **D3** | Regionale kaders (2008) staan nog op de website als beleid; onduidelijk of formeel ingetrokken (Apeldoorn trok in [PB]); Voorst-RvG vult aan/vervangt (keuze initiatiefnemer). Gemeentelijke positie t.o.v. regionale uitwerking: zienswijze-aandacht voor eigen functieveranderingsbeleid. | G/T | S1b, S4, S35 | Besluit raad/college intrekking |
| **E1** | Regisseur Ruimte: naam niet openbaar. Vooroverleg met provincie en waterschap in RvG-stappenplan (stap 5); Voorst-West: gesprekken "met specialisten van provincie en erfgoed"; De Poll: provinciale pilot. Omgevingstafel/intaketafel gemeentelijk (leges € 773,35). Gebiedsagenda Stedendriehoek: niet onderzocht. | G (naam NG) | S1, S5, S19 | Provincie (Regisseur Ruimte Stedendriehoek) |
| **E2** | Voorkeur: **BOPA** via Verken uw idee → college (principebesluit) → anterieure overeenkomst → vergunning; raad bindend advies (CVDR701428) bij uitgebreide procedure. Provinciaal advies/instemming bij BOPA (Prb 2024 nr. 3109) in gemeentelijke stukken niet genoemd. Doorlooptijd waargenomen: 20-31 maanden bij 1-2 woningen; Voorst-West: plan eind 2026, procedure vanaf Q2 2027. | G (provinciale rol NG) | S5, S31b, S35 | Provincie; afdeling Ruimte |
| **E3** | Matrix/drempel 20 woningen: in gemeentelijke stukken niet genoemd; Kader noemt 12-woningengrens voor sociaal 1/3. | NG | — | Provincie (Matrix juli 2026); afdeling Ruimte |
| **E4** | Provinciale zienswijzen/instemmingen woningbouw buitengebied Voorst 2023-2026: niet gevonden. Wel: **GS-bezwaar** tegen vergunning zonnepanelen Beelelaan 2A Voorst (besluit 5-3-2026; bezwaar ongegrond, wk 25/2026). | NG (woningbouw) | S35 wk 25/2026 | Provinciaal Blad; deelonderzoek 4 |
| **E5** | Omgevingsplan gemeente Voorst CVDR696255/3 (7-10-2024); aanpassing aan provinciale instructieregels: niet gevonden; BOPA toetst aan Omgevingsverordening (bv. art. 5.90 bij zonnepanelen). | NG | S30; wk 25/2026 | DSO / Regels op de kaart; deelonderzoek 4 |
| **F1** | Provinciale subsidie Collectieve wooninitiatieven: gebruik door Voorst/Woongroep niet gevonden; geen intentieverklaring gevonden; gemeente heeft geen eigen CPO-subsidie. CPO-brochure (2023): provincie "voornemens ... stimuleringsregeling voor CPO" binnen SteenGoed Benutten. Voorst CPO-kavel Teuge bevestigd. | NG | S16 | Provincie (subsidieloket); gemeente |
| **F2** | Versnellingstafel (provinciaal/regionaal/gemeentelijk) en "provinciale middelen van de Regionale Woondeal" ingezet voor versnelling (beantwoording RTG 2-3-2026); Realisatiestimulans (Rijk, € 7.000 per betaalbare woning; Voorst stort in Vereveningsfonds; € 147.000 gereserveerd); Erfgoed Deal Polder Nijbroek (Rijk+provincie); Wijken- en dorpendeals/provinciale grondfaciliteit: niet gevonden. | G (deels NG) | S11, S11d, S36 | — |
| **F3** | Leefbaarheid Kleine Kernen 2026 (CVDR765130; 14-7-2026): subsidie voor dorpsbelangenorganisaties (€ 1.150 + dorpsondersteuning € 7-10k + initiatieven € 0,5-3k per jaar), **niet voor woningbouw/CPO**. Starterslening (≤ 34 jaar, 20%, max. € 30.000, NHG). Toekomstbestendig Wonen-lening. Erfpacht: beperkt (Nota Grondbeleid). | G | S34, S4c | — |

---

## Tegenstrijdigheden en onzekerheden

- **T1 — Status Rood voor Groenbeleid:** "tijdelijk, maximaal 2 jaar" (raadsbesluit 30-1-2023; website) vs. toepassing t/m 2026 zonder gevonden verlengingsbesluit; definitieve evaluatie en definitief beleid aangekondigd "na PLG"/in omgevingsvisie, maar niet gevonden. Het beleid bestaat niet in CVDR. *Actie:* verifiëren bij afdeling Ruimte of raad of college.
- **T2 — Datering RvG:** document "31 januari 2023"; raadsbesluit 30-1-2023 (vergadering); raadsvoorstel 13-9-2022 (raadsbehandeling uitgesteld van 28-11-2022). PB noemt 31-1-2023.
- **T3 — Landgoederenbeleid:** webpagina/PLG/Nota 2006: "maximaal één wooneenheid per landgoed" vs. recente praktijk: 18 appartementen Het Nieuwe Wezeveld (bestaand landgoed met maatschappelijk bouwvlak) en ontwerp-OV "landgoedmodel" met "kleinschalige, hoogwaardige woonerven met kleinere woningen". Niet strijdig voor *nieuwe* landgoederen, wel een verschuiving.
- **T4 — Aantallen/tempo:** Woonvisie 2017 "90/jaar"; Jaarstukken/Woonvisie "gemiddeld 80/jaar"; woondeal 100/jaar; Kader 125/jaar; werkelijk ± 90. Woondeal 2022-2030 "ca. 900" (Jaarstukken, woningmarktonderzoek) vs 921 [PB] vs 1.015 plancapaciteit 2023 [PB]; Kader "625 t/m 2030" vs woondeal 600 (2025-2030).
- **T5 — Inkomensgrens sociale koop:** € 60.000 (verordening, geldend) vs € 75.000 (Kader, nog niet in omgevingsplan); koopprijsgrenzen: € 390.000 (motie 2024), ≈ € 355.000 (woningmarktonderzoek bereikbaar), € 405.000 (SD-bijlage prijspeil 2025), € 420.000 (Kader 2026).
- **T6 — Hessenlaan:** webpagina "maximaal zes"; bp "5 tot 6"; Jaarstukken "5 woningen gerealiseerd 2025"; winnaar CPO-groep niet gevonden. De pagina noemt contact "m.lebbink@voorst.nl" in uitvraag (2023) vs. Jerry Beer op webpagina.
- **T7 — College:** website zegt "Er zijn nu twee wethouders" maar noemt drie (derde benoemd 7-9-2026). Portefeuille Wonen: Van Zeijts t/m ca. 6-7-2026 → Bosch (RM 14-7-2026). Partij van wethouders alleen indicatief (zie §10).
- **T8 — Raadsadviesrecht:** aanwijzingsbesluit lid 1a is breed ("niet past binnen doelen omgevingsplan/kaders"), maar het college achtte het niet van toepassing bij De Vecht (17) en Wezeveld (18). Geen toetsing op juridische onderbouwing gedaan.
- **T9 — Provinciaal beeld vs. gemeente:** [PB] stelt Voorst "buiten Veluwe", maar de gemeente toetst Twello-Noord aan kernkwaliteiten van het Nationaal Landschap Veluwe (RvS). Compatibel: Nationaal Landschap ≠ streek Veluwe (69,9% van gemeentegebied in Nationaal Landschap [PB]).
- **T10 — Fractienamen:** GroenLinks-PvdA heet in raadsvergaderingen vanaf zomer 2026 "PRO" (raadsleden Moleman, Grevinga, Van der Galiën).
- **Onzekerheden:** (1) volkshuisvestingsprogramma/gewijzigd omgevingsplan niet gevonden; (2) uitkomst raadsbehandeling BOPA Wilp-Achterhoek (8-6-2026 geagendeerd) niet gelezen; (3) winnaar Winkler Prins-uitvraag; (4) vervolg ontwerp-OV (nota van beantwoording, Q4 2026); (5) inhoud college-zienswijze op provinciale visie; (6) afbeelding-PDF's functieverandering/vervangingswaarde niet gelezen; (7) partijprogramma's 2026 niet onderzocht; (8) Notubiz-API toont niet alle documenten (alleen openbare); (9) leges-berekening aanname-afhankelijk; (10) de ontwerp-omgevingsvisie (46 MB) is voor wonen/buitengebied volledig doorzocht maar niet integraal gelezen.

---

## Niet gevonden — waar wel te vinden

| Onderwerp | Waar |
|---|---|
| Volkshuisvestingsprogramma Voorst 2026/2031 (ontwerp) | Gemeenteblad/officielebekendmakingen.nl, Omgevingsloket "Regels op de kaart", raadsinformatie (raadsmededeling), afd. Ruimtelijke ontwikkeling |
| Definitieve evaluatie / verlenging Rood voor Groen | Raadsinformatie (raadsvoorstel/mededeling), collegebesluitenlijsten; afd. Ruimte (P. Dekker) |
| Winnaar CPO Hessenlaan (naam vereniging), prijs | Gemeente Grondzaken (J. Beer); Kadaster; college-besluitenlijst nov-dec 2023 |
| Hard/zacht plancapaciteit, planmonitor | LMVW/Monitor Gelderland; afd. Ruimtelijke ontwikkeling; regio Stedendriehoek |
| Matrix/BOPA-gevallenlijst toepassing Voorst; provinciale instemming | Provincie Gelderland (Regisseur Ruimte), Prb 2024 nr. 3109 |
| Zienswijzetekst Voorst op provinciale omgevingsvisie | Collegestuk 923772; Statenstukken |
| Ontwerp-VHP & aanpassing omgevingsplan sociale koop | Raad Q3-Q4 2026 |
| Partijprogramma's/CPO-standpunten fracties 2026 | Partijwebsites; RIS |
| Scans "Functieverandering en verevening / gecorrigeerde vervangingswaarde / het proces" | voorst.nl/bestuur-organisatie/beleid-en-regelgeving (OCR nodig) |
| Overige CPO-projecten (Twello-Noord, Voorst-West reservering) | Nieuwsbrief Twello-Noord; raadsmededelingen |

---

## Bronnenlijst (URL + raadplegingsdatum)

Datum raadpleging: 2026-10-17/18 tenzij anders.

- **S1** Beleidsregel Rood voor Groenbeleid (BiedtRuimte, tijdelijk beleid, 31-1-2023, 17 p.; integraal gelezen) — https://www.voorst.nl/fileadmin/user_upload/Wonen__bouw__verbouw/Bouw/Rood_voor_Groenbeleid_Gemeente_Voorst.pdf. **S1b** Webpagina functieverandering buitengebied — https://www.voorst.nl/wonen-bouw/bouw/gebiedsontwikkeling/functieverandering-buitengebied. Spread: .../Bouw/Spread_Rood_voor_Groen_15mrt2023.pdf (niet gelezen).
- **S2** RIS Notubiz — https://voorst.raadsinformatie.nl/dashboard ; API https://api.notubiz.nl/organisations/742/modules/{19,8,6,1,3,4}/items.
- **S3** Raadsvoorstel Rood voor Groen (13-9-2022) https://api.notubiz.nl/document/11844308/2 ; RM 13-12-2022 https://api.notubiz.nl/document/12280769/2 ; moties/amendementen 30-1-2023 (documenten 12369638, 12369643, 12369642, 12368333). **S3b** Raadsmededeling tussenevaluatie 9-7-2024 https://api.notubiz.nl/document/14400147/2. **S3c** Moties/amendementen leges 2025 (module 6).
- **S4** Beleid en regelgeving https://www.voorst.nl/bestuur-organisatie/beleid-en-regelgeving ; **S4b** Kavels https://www.voorst.nl/vrije-kavels (+ subpagina's hessenlaan, winklerprinsvoorst, dorpszicht-fase2, twello-de-schaker e.a.); **S4c** College https://www.voorst.nl/bestuur-organisatie/college-van-bw (+ wethouderspagina's); Wonen/bouw https://www.voorst.nl/wonen-bouw ; Starterslening https://www.voorst.nl/wonen-bouw/wonen/starterslening ; Nieuwe landgoederen https://www.voorst.nl/wonen-bouw/bouw/gebiedsontwikkeling/nieuwe-landgoederen ; Twello-Noord https://www.voorst.nl/twello-noord ; Wilp-Achterhoek https://www.voorst.nl/woningbouw-wilp-achterhoek ; Voorst-West https://www.voorst.nl/wonen-bouw/bouw/gebiedsontwikkeling/wonen-in-het-dorp-voorst/woningbouw-voorst-west ; Lindeboomsland https://www.voorst.nl/woningbouw-lindeboomsland.
- **S5** Uw idee verkennen https://www.voorst.nl/wonen-bouw/uw-idee-verkennen.
- **S6** Ontwerp-omgevingsvisie gemeente Voorst (RUIMTEVOLK, juli 2026, 94 p.) https://www.voorst.nl/fileadmin/user_upload/Wonen__bouw__verbouw/Omgevingsvisie/20260714_5.25.116_Omgevingsvisie_Voorst_einddocument_DigitaalToegankelijk.pdf ; projectpagina https://www.voorst.nl/omgevingsvisie ; kennisgeving Gemeenteblad 2026, 347118 (17-7-2026) https://zoek.officielebekendmakingen.nl/gmb-2026-347118.html (inzage 16-7 t/m 10-9-2026; raadsbesluit Q4 2026). **S7** gebiedsgerichte toelichtingen Agrarisch landschap/Mozaïek/Groene buffer (zelfde map). Nota Landgoederen 2006 https://www.voorst.nl/fileadmin/user_upload/Wonen__bouw__verbouw/Bouw/Projecten/Landgoederen_beleidsnotitie_januari_2006.pdf (webpagina-versie: Nota_landgoederen_incl_visiekaart_def.pdf; vastgesteld raad 6-2-2006).
- **S8** Coalitieakkoord "Natuurlijk Voorst!" 2026-2030 https://www.voorst.nl/fileadmin/user_upload/Bestuur__organisatie/College/Coalitieakkoord_Natuurlijk_Voorst.pdf ; Notubiz doc 17150146; Portefeuilleverdeling doc 17150147; persbericht 26-6-2026; rapport verkenner 16-4-2026.
- **S9** Programma Landelijk Gebied (raad 26-5-2025) https://www.voorst.nl/fileadmin/user_upload/Bestuur__organisatie/Beleid_en_regelgeving/2._Mooi_Voorst/Programma_Landelijk_Gebied.pdf ; raadsbesluit/-voorstel via Notubiz (module 19 id 1035936).
- **S10** Nota Grondbeleid 2024 https://www.voorst.nl/fileadmin/user_upload/Bestuur__organisatie/Beleid_en_regelgeving/1._Bouwend_Voorst/Nota_Grondbeleid_Voorst_2024-gew.pdf (raad 25-11-2024; bijlage F maart 2026 = Notubiz doc 16549565).
- **S11** Kader Volkshuisvesting gemeente Voorst 2026/2027 https://www.voorst.nl/fileadmin/user_upload/Bestuur__organisatie/Beleid_en_regelgeving/1._Bouwend_Voorst/Kader_Volkshuisvesting_Voorst_2026_2027.pdf ; **S11b** raadsbesluit 9-3-2026 (Notubiz 16694761); **S11c** raadsvoorstel 27-1-2026 (Notubiz 16549571); **S11d** beantwoording vragen RTG 2-3-2026 (module 3 id 1140334).
- **S12** Woonvisie Aantrekkelijk Voorst 2025 (2017; ingetrokken) Notubiz doc 16549569. **S13** Woonzorgvisie Voorst 2023-2027 Notubiz doc 13563151. **S14** Uitkomsten Avond van het Wonen 2-12-2025 Notubiz doc 16549566.
- **S16** Informatiebrochure Samen bouwen in de gemeente Voorst (CPO, sept. 2023) https://www.voorst.nl/fileadmin/user_upload/Wonen__bouw__verbouw/Kavels_en_grondzaken/Hessenlaan/Informatiebrochure_samen_bouwen_in_de_gemeente_Voorst.pdf.
- **S18** Winkler Prins-uitvraag https://www.voorst.nl/winklerprinsvoorst.
- **S19** RM 14-7-2026 Voorst-West (module 8 id 1188321); **S19b** RM 10-3-2026 BOPA Wilp-Achterhoek (1142967) en landgoed met crematorium (1142972); **S19c** RM 17-2-2026 De Vecht (1135727), RM 3-3-2026 Wezeveld (1140286).
- **S20** RM 30-1-2024 Woningmarktonderzoek (module 8 id 916632). **S21** Uitvraag CPO Hessenlaan Teuge https://www.voorst.nl/fileadmin/user_upload/Wonen__bouw__verbouw/Kavels_en_grondzaken/Hessenlaan/Uitvraag_en_verkoopvoorwaarden_CPO_Hessenlaan_Teuge.pdf ; pagina https://www.voorst.nl/hessenlaan ; bp Hessenlaan raad 3-7-2023 (Notubiz module 19 id 857974).
- **S22** Jaarstukken 2025 (raad 6-7-2026) https://www.voorst.nl/fileadmin/user_upload/Bestuur__organisatie/Beleid_en_regelgeving/Jaarstukken_2025.pdf (p.18-19, 29). **S23** Portret van de gemeente Voorst (sept. 2025) .../Omgevingsvisie/Portret_van_de_gemeente_Voorst_def.pdf.
- **S25** Meerjaren-samenwerkingsafspraken IJsseldal Wonen/HBV (Notubiz 12458327). **S26** RM 14-10-2025 huisvestingsverordening binding (module 8 id 1093120). **S27** brief Woongroep Teuge 8-6-2026 (module 1 id 1173398); **S27b** Cooplink (955012); **S27c** Holthoevensestraat 22 (1006978).
- **S28** Verkiezingsuitslag GR26 https://www.voorst.nl/fileadmin/user_upload/Over_Voorst/Verkiezingen/2026_gemeenteraad/Voorst_verkiezingsuitslag_centraalstembureau_GR26.pdf. Raadssamenstelling https://www.voorst.nl/bestuur-organisatie/gemeenteraad/samenstelling.
- **S29** RM 3-2-2026 De Zutphenboer (module 8 id 1131831; presentatie IBB 19-1-2026).
- **S30** Omgevingsplan gemeente Voorst https://lokaleregelgeving.overheid.nl/CVDR696255 (v3 per 7-10-2024). **S31** Gronduitgifteregeling CVDR637112; **S31b** Aanwijzingsbesluit bindend adviesrecht CVDR701428; **S31c** Verordening sociale koop- en huurwoningen CVDR120802/2. **S32** Beleidsregels woningsplitsing CVDR743645. **S33** Legesverordening Voorst 2026 (1e wijziging) CVDR753300/2 ; **S33b** Beleidsregels transportcapaciteit CVDR765873 ; **S34** Beleidsregels Leefbaarheid Kleine Kernen 2026 CVDR765130 (Gemeenteblad gmb-2026-360338).
- **S35** College-besluitenlijsten 2023-2026 (voorst.nl/bestuur-organisatie/college-van-bw/besluitenlijsten; o.a. 2024 wk 16, 35, 44, 49; 2025 wk 6, 22, 36, 43; 2026 wk 3-7, 12-14, 22, 25, 26, 37, 40).
- **S36** Besluitenlijst raad 6-7-2026 (Notubiz doc 17200791); besluitenlijst 7-9-2026 (doc 17371329).
- **S37** Programma ruimtelijke kwaliteit: raad 24-3/7-4-2025 (Notubiz). **S38** Gemeenteblad-bekendmakingen anterieure overeenkomsten RvG (gmb-2024-498905, gmb-2025-342681, gmb-2026-40823 e.a.). **S39** "Voorst Rapport definitief" (dec. 2024, formatie 2022) — zoekresultaat [WF] https://voorst.nl/fileadmin/user_upload/Nieuws/2024/12_dec/Voorst_Rapport_definitief.pdf. **S40** Provinciebestand `provincie_gelderland.md` (2026-10-02) = [PB].

Werkbestanden (extracties) staan in `/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/d1/`.
