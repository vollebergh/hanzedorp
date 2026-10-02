# Gemeente Zwolle — CPO-naslagwerk (provincie Overijssel)

## Verantwoording
- **Raadplegingsdatum:** onderzoek (live bronnen over Zwolle) 2026-08-21; **deze actualisatie 2026-10-02**.
- **Provincie en gebruikt provinciebestand:** Overijssel — [`provincie_overijssel.md`](provincie_overijssel.md), versie **2026-10-02** (de eerste versie van dit rapport gebruikte de versie van 2026-08-21; die is sindsdien inhoudelijk gecorrigeerd, zie de changelog hieronder).
- **Primair model + effort:** eerste versie (2026-08-21): Claude Sonnet 5, effort-niveau "extra". **Deze actualisatie (2026-10-02): Claude Sonnet 5.5 (`claude-sonnet-5-5`); effort-niveau niet expliciet ingesteld/bekend in deze sessie.**
- **Aard van de actualisatie:** het rapport is herstructureerd en aangevuld op basis van (a) de bijgewerkte masterprompt `prompt.md` (o.a. landelijke context bij §2, Bijlage A-controlepunten, gelaagde beantwoording van de kernvragen, houdbaarheidsparagraaf) en (b) de bijgewerkte inzichten uit `provincie_overijssel.md` (2026-10-02). **Daarnaast is op 2026-10-02 een gerichte verificatieronde met WebSearch/WebFetch uitgevoerd** op de openstaande punten en tegenstrijdigheden (geen volledig nieuw onderzoek). Gelezen of gecontroleerd: het volledige coalitieakkoord 2026-2030 (PDF, lokaal geëxtraheerd), de raadsbrief "Beleidsupdate Wonen" (16-12-2025), de scenarionota "Bouwstenen Huisvestingsverordening" (1-7-2024), de provinciale brief "Routekaart VAB- en Erftransformatie-programma's" (25-2-2025) en de CVDR-nummers CVDR739354 en CVDR729056. Alle overige Zwolse feiten dateren van de raadpleging op 2026-08-21 en zijn niet opnieuw geverifieerd. Waar een Zwolse bevinding door een provinciale wijziging mogelijk is verouderd, is dat gemarkeerd als *interpretatie*.
- **Deelonderzoeken:** Fase 1 (provinciaal referentiekader Overijssel) en alle vier Fase 2-deelonderzoeken (bestuursinformatie; provinciaal-lokale toepassing; nieuws en actualiteit 2024-2026; juridische en officiële registers) zijn uitgevoerd met hetzelfde model en effort-niveau als het primaire model (Claude Sonnet 5, "extra") — één gecombineerde vermelding volstaat daarom.
- **Methode:** vier gelijktijdige deelonderzoeken (elk gericht op één brontype, elk alle 12 onderwerpen doorzoekend) plus het reeds afgeronde provinciale referentieonderzoek, hier samengevoegd tot één samenhangend rapport. Dubbele bevindingen zijn gededupliceerd; tegenstrijdigheden tussen deelonderzoeken zijn expliciet benoemd (zie de kaders "⚠️ Tegenstrijdige bevinding" hieronder) in plaats van stilzwijgend één versie te kiezen.
- **Provinciaal kader:** zie [`provincie_overijssel.md`](provincie_overijssel.md) voor het volledige provinciale beleidskader (Omgevingsvisie, Kwaliteitsimpuls Groene Omgeving/art. 4.11 Omgevingsverordening, subsidies, voorkantsamenwerking/Lijst BOPA). Dit rapport herhaalt dat kader niet, maar verwijst ernaar en behandelt uitsluitend de Zwolse toepassing ervan. Zwolle ligt in Overijssel; het Overijsselse regime is leidend voor het omgevingsplan.
- **Methodologische waarschuwing (geldt voor het hele rapport):** generieke zoekacties (Google, CVDR-volltekstzoeken) bleken herhaaldelijk regelgeving/nieuws van ándere Overijsselse/Gelderse gemeenten als "Zwolle" te tonen. Alle vondsten in dit rapport zijn expliciet geverifieerd op de daadwerkelijke uitgevende overheid. Waar een aanvankelijk kansrijke bron bij verificatie een andere gemeente bleek te betreffen, is dat vermeld omdat de negatieve bevinding zelf relevant is (het toont aan dat Zwolle op dat punt kennelijk géén eigen beleid heeft gepubliceerd).
- Meerdere zwolle.nl-pagina's gaven een HTTP 403-foutmelding bij geautomatiseerde raadpleging (WebFetch); de inhoud van die pagina's is in dit rapport gebaseerd op zoekresultaat-samenvattingen, niet altijd op letterlijk geverifieerde brontekst. Dit is per geval vermeld. **Aanbeveling voor de opdrachtgever:** deze pagina's alsnog handmatig via een browser raadplegen voor exacte citaten.

### Wijzigingen t.o.v. de versie van 2026-08-21 (changelog)
| # | Eerdere formulering | Stand per 2026-10-02 |
|---|---|---|
| 1 | Provinciale "vooroverleg"-procedure (impliciet Bro 3.1.1) | **Gecorrigeerd:** sinds 1-1-2024 *voorkantsamenwerking* + *Lijst BOPA* (provinciaal advies én instemming) + kennisgeving. Verwerkt in §3 (a), (c) en Bijlage A (E1-E3). |
| 2 | "Nieuwe provinciale 'nee, tenzij'-regime voor generieke landbouwgebieden" als zware horde | **Genuanceerd:** de verordening (art. 4.124, in werking 1-7-2026) is smaller dan de visietekst; stuurt op *transformatie van (agrarische) bouwpercelen*. Voor onbebouwde grond werkt de "nee, tenzij" vooral informeel (voorkantsamenwerking/instemming). Verwerkt in §3 (a), (d), (e), kernvragen. |
| 3 | Zwolse OF/WAAR/HOE- en "Overijsselse ladder"-tekst als actueel kader | **Vermoedelijk deels achterhaald:** de ladder heet sinds 1-7-2026 "Overijsselse verstedelijkingsprincipes", het Uitvoeringsmodel is vervangen door de redeneerlijn (art. 4.122). Verwerkt in §2. |
| 4 | Woonafspraken: "80%-grens" | Het is een **voorkeur** ("bij voorkeur maximaal 80%"), geen harde grens. Verwerkt in §5. |
| 5 | Landelijke ladder/regie volkshuisvesting niet behandeld | Toegevoegd in §2 (Regiewet in werking 1-7-2026; ladder naar verwachting vervallen 1-1-2027 onder voorwaarde van een gemeentelijk volkshuisvestingsprogramma). |
| 6 | Geen Bijlage A-tabel | Toegevoegd: tabel **Overijssel-controlepunten (Bijlage A)** aan het slot, plus houdbaarheidsparagraaf. |
| 7 | Kernvragen niet gelaagd | Beide kernvragen nu gelaagd beantwoord: (a) gemeente, (b) provincie, (c) eindoordeel + onzekerheden. |
| 8 | ⚠️ Tegenstrijdigheid "Huisvestingsverordening 2025 (CVDR739354)" | **Opgelost (2026-10-02):** CVDR739354 is de Huisvestingsverordening 2025 van **gemeente Groningen**, niet van Zwolle. Zwolle heeft nog geen vastgestelde algemene huisvestingsverordening gevonden; de raad kreeg op 1-7-2024 een scenarionota (verkenningsfase). Verwerkt in §8. |
| 9 | ⚠️ Tegenstrijdigheid "Woonvisie 2025-2030 'Het begint met wonen' (CVDR729056)" | **Opgelost (2026-10-02):** CVDR729056 is de woonvisie van **Gooise Meren**. Zwolle werkt aan een **Volkshuisvestingsprogramma** (oplevering gepland derde kwartaal 2026, raadsbevoegdheid) op basis van een woningbehoefteonderzoek (2025). Verwerkt in §2, §12. |
| 10 | Coalitieakkoord niet integraal doorzocht; "geen CPO-vermelding" onbevestigd | **Opgelost:** PDF integraal doorzocht. Geen vermelding van CPO/zelfbouw/kavels/collectief wonen als woonvorm, **wél** een toezegging om de **KGO te actualiseren** voor meer ruimte voor ontwikkelingen op erven en in het buitengebied. Verwerkt in §3, §10. |
| 11 | Spelling wethouder "Willigers/Willegers" | **Gecorrigeerd:** "Johran **Willegers**" (coalitieakkoord). Portefeuille mede Vastgoed en grondbeleid. |
| 12 | Status Omgevingsvisie Zwolle onbekend | **Aangevuld:** ontwerp (college 14-10-2025; ter inzage 27-10 t/m 8-12-2025); definitieve vaststelling vertraagd en niet gevonden. Verwerkt in §2. |

---

## 1. CPO-beleid

Zwolle heeft **geen zelfstandige, in CVDR gepubliceerde "Beleidsregels CPO"** — bevestigd door drie onafhankelijke deelonderzoeken via gerichte CVDR-zoekacties (0 treffers op "CPO"/"collectief particulier opdrachtgeverschap"/"zelfbouw" binnen de Zwolse regelgeving). CPO-beleid loopt in Zwolle via de Omgevingsvisie, het reguliere grondprijsbeleid en per-locatie projectkaders.

### Nieuwe Veemarkt — actief, huidig CPO-project
Bron: https://www.zwolle.nl/collectieve-woonvormen-op-de-nieuwe-veemarkt (21-08-2026)

> "De Nieuwe Veemarkt in Zwolle biedt een unieke kans voor collectieve woonvormen waarin solidariteit, burenhulp en duurzaamheid centraal staan. Op één van de ontwikkelvelden is er ruimte voor circa 30 woningen, speciaal bedoeld voor een collectief initiatief."

> "Waarom stimuleert de gemeente collectieve woonvormen? In 2023 deed de gemeente Zwolle onderzoek naar de interesse in collectief wonen. De belangstelling was groot. Tegelijkertijd werden plannen gemaakt voor de Nieuwe Veemarkt. **Het college en de gemeenteraad vonden collectief wonen belangrijk en besloten hiervoor ruimte te bieden.**"

Vastgestelde vormen: coöperatief wonen, CPO ("bewoners ontwikkelen samen hun woningen en worden individueel eigenaar"), mede-opdrachtgeverschap. Ondersteuning: mogelijke garantstelling voor een coöperatie, begeleidend projectleider. Planning: aanmeldfase afgerond dec. 2025 (5 groepen, waaronder expliciet "CPO Samen Groen Wonen in Zwolle", ca. 25 huishoudens); selectiefase april-nov. 2026; bouwstart vanaf 2028. Contact: veemarkt@zwolle.nl. Dit is echter een **stedelijke locatie** (Kamperpoort), geen buitengebied/agrarische grond.

### Historische precedenten (stedelijk, ter context)
- **Stinspoort, Westenholte (2011):** college besloot 25 januari 2011 een CPO-beleidskader vast te stellen, 11 betaalbare koopwoningen in "pure" CPO-vorm. Bron: https://www.weblogzwolle.nl/nieuws/21303/gemeente-start-pilot-cpo-in-westenholte.html (21-08-2026). Stadsrand-locatie, geen agrarisch buitengebied.
- **GroeneBurenErf/Groeneburenhof (De Tippe):** CPO-achtige duurzame woongroep, ca. 15-18 wooneenheden, doelgroep 50+. Bronnen: https://groeneburenerfzwolle.nl/, https://www.hetkanwel.nl/cpo-woonproject-zwolle/ (21-08-2026). Zie ook §6/§7.

### Ontbrekende koppeling CPO ↔ buitengebied/agrarische grond
Geen enkel gemeentelijk document koppelt CPO expliciet aan het buitengebied of agrarische herbestemming. Ter vergelijking: buurgemeente **Ommen** doet dit wél expliciet in haar Woonprogramma 2021-2025: *"In het buitengebied geven we ruimte aan woningbouw op de plek van bijvoorbeeld vrijkomende agrarische bebouwing. Door middel van oprichten van CPO's vanuit de plaatselijke belangen worden vraag en aanbod bij elkaar gebracht. Dergelijke CPO's kunnen rekenen op ondersteuning vanuit de gemeente."* (CVDR695681/1, **dit is Ommen-beleid, niet Zwolle** — ter illustratie van wat elders wél is vastgelegd).

Ook het coalitieakkoord 2026-2030 noemt CPO, zelfbouw of collectief wonen niet (integraal doorzocht, 2026-10-02; zie §10).

**Lacune:** een gemeentebreed CPO-beleidskader specifiek voor het buitengebied ontbreekt. **Waar te vinden/navragen:** team Nieuwe Ruimtelijke Initiatieven (ruimtelijkeinitiatieven@zwolle.nl); mogelijk relevante ontwikkeling via het programma Vechtrand/Nieuw Zuthem (zie §2/§5).

---

## 2. Openheid voor nieuwbouw buiten woonkernen

Zwolle's ruimtelijke koers is uitgesproken **stad-georiënteerd**. Bron: https://www.zwolle.nl/de-ruimtelijke-koers-van-zwolle (21-08-2026):

> "Ons buitengebied is voor ons van grote waarde, voor landbouw, landschap, natuur en recreatie. […] We zetten in op een multifunctioneel buitengebied, waarbij stad en buitengebied verbonden zijn."

Zwolle past de provinciale **Ladder voor duurzame verstedelijking** nog toe, met een gemeentelijk OF/WAAR/HOE-toetsingskader (bron: zwolle.nl/vestigen-buitengebied, samenvatting; brontekst zelf gaf HTTP 403 bij direct ophalen — zie methodologische waarschuwing):

> "OF: de Overijsselse ladder voor duurzame verstedelijking geeft een nadere invulling aan de vraag hoe de behoefte moet worden bepaald […]. WAAR: het buitengebied wordt in de Omgevingsvisie van de provincie de Groene Omgeving genoemd. 'Groene' functies hebben prioriteit […]. Op (voormalige) agrarische erven is — onder voorwaarden — ruimte voor aanvullende woon- en werkmilieus waarvoor aantoonbaar een marktvraag is en de Stedelijke Omgeving geen ruimte biedt. HOE: bij grootschalige ontwikkelingen in het buitengebied […] is de Kwaliteitsimpuls Groene Omgeving (KGO) van toepassing."

In de onderzochte Zwolse bronnen (stand 2026-08-21) is geen aanwijzing gevonden dat Zwolle zich voorbereidt op het vervallen van de landelijke ladder; dit is echter niet gericht onderzocht (zie "Landelijke context" hieronder en Bijlage A, A4).

**Het Zwolse OF/WAAR/HOE-kader is vermoedelijk deels achterhaald (interpretatie).** De Zwolse webtekst verwijst naar de "Overijsselse ladder" en het provinciale Uitvoeringsmodel. Volgens `provincie_overijssel.md` §1.1 is de ladder met Actualisatie 2026 van de Omgevingsverordening (in werking **1 juli 2026**) hernoemd tot **"Overijsselse verstedelijkingsprincipes"** en is het Uitvoeringsmodel (OF-WAAR-HOE) vervangen door de **provinciale redeneerlijn (art. 4.122)**. Of Zwolle haar eigen tekst en omgevingsplan al heeft aangepast, is niet onderzocht. Gemeenten hebben tot **1 juli 2029** om het omgevingsplan aan te passen (art. 4.2a); bij een BOPA of projectbesluit gelden de nieuwe regels echter **direct**.

**Landelijke context (provincie_overijssel.md §5; stand 2026-10-02, per gemeente herverifiëren):** de Wet versterking regie volkshuisvesting is per **1 juli 2026** in werking getreden. De ladder voor duurzame verstedelijking (Bkl 5.129g) wordt voor woningbouw geschrapt via het Besluit versterking regie volkshuisvesting, naar verwachting per **1 januari 2027**, onder de voorwaarde dat een **gemeentelijk volkshuisvestingsprogramma** (uiterlijk 1 juli 2027 volgens Rijksoverheid/Staatsblad; PONT Omgeving noemt andere termijnen) de woningbouwopgave en locaties aanwijst. Zwolle werkt aan een **Volkshuisvestingsprogramma** (oplevering gepland Q3 2026, raadsbevoegdheid; zie hieronder bij "Status Omgevingsvisie"); of het is opgeleverd en buitengebied- of uitbreidingslocaties aanwijst, is niet gevonden. Een eigen Zwolse "Woonvisie 2025-2030" bestaat naar nu blijkt niet (zie §12). **Het provinciale beleid blijft daarnaast gelden:** de verstedelijkingsprincipes (art. 4.4-4.6), de redeneerlijn en art. 4.5 lid 2 (eerst bestaande bebouwing benutten) vervallen niet met de landelijke ladder.

**Positie in het provinciale kader (art. 4.4):** Zwolle is aangewezen als **"grote stad"** (met Almelo, Deventer, Enschede en Hengelo): daar mag voor de lokale, regionale én bovenregionale behoefte worden gebouwd. Dit regelt de stedelijke opgave in en aansluitend aan de stad; voor een locatie in het buitengebied blijft **art. 4.5 lid 2** gelden (nieuw ruimtebeslag alleen als hergebruik van bestaande bebouwing en combinatie van functies op bestaande erven in redelijkheid niet mogelijk zijn) en blijft de gemeente zelf bepalen of een stadsrandlocatie als stedelijk gebied of als Groene Omgeving telt (provincie_overijssel.md §1.2).

**Woon-/verstedelijkingsregio en grensoverschrijdende verbanden:** Zwolle ligt in woonregio **West-Overijssel** (Woondeal 2025-2030, zie §5). Daarnaast is de regio Zwolle aangewezen als **NOVEX-gebied** (verstedelijkingsstrategie "Warme harten in een klimaatadaptieve delta"; in de provinciale gebiedsbijlage "klimaatadaptieve groeiregio Zwolle") en is Zwolle onderdeel van het samenwerkingsverband **Regio Zwolle** (volgens de gebruikte bron 22 gemeenten en 4 provincies, dus grensoverschrijdend) en van de ZSDZ-samenwerking (Zwolle-Staphorst-Dalfsen-Zwartewaterland, o.a. energielandschap A28). Het regime van Overijssel is leidend voor het Zwolse omgevingsplan; beleid van buurprovincies is hooguit context. Bron: Actualisatie Woondeal West-Overijssel, p. 2, en provinciale bijlage "Gebiedseigen perspectieven voor vier windstreken in Overijssel" (beide geraadpleegd 2026-08-21).

### Vechtrand en Nieuw Zuthem — de facto het belangrijkste uitlaatklep voor grootschalige groei
De gemeente onderzoekt sinds 2025 nieuwe woongebieden **Vechtrand** en **Nieuw Zuthem**, met een bewust gevestigd **voorkeursrecht (Wvg)** om grondregie te houden. Citaat wethouder Gerdien Rots: *"Zwolle groeit, en dat willen we doen mét de stad. […] Met de aangepaste planning houdt de gemeente regie op de grond."* Vechtrand (deelgebieden Vechtpoort 1, Vechtpoort 2, Ceintuurbaanzone, tussen Berkum en het spoor Zwolle-Meppel) is **grotendeels agrarisch** in huidig gebruik (incl. een actieve bloemenkwekerij), potentieel 1.500-3.000 woningen. Zwolle-Zuid (nieuw stadsdeel): 2.000-3.000 + 250-500 woningen. Totaalambitie tot 2040: 18.250-23.500 nieuwe woningen. Bronnen: https://www.zwolle.nl/vechtrand, https://www.rtvfocuszwolle.nl/nieuwe-wijken-zwolle-woningen/ (21-08-2026).

**Weerstand tegen grootschalige buitenwaartse groei:** bewoners van Berkum verzetten zich tegen de omvang van de geplande uitbreiding ("dorpse karakter" in het geding, pleidooi voor 500 i.p.v. duizenden woningen); dit was een expliciet verkiezingsthema rond maart 2026. Bron: https://www.oost.nl/nieuws/3628172/woningnood-in-zwolle-groot-maar-bouwen-buiten-de-stad-schuurt (Omroep Oost, 12-03-2026). Dit betreft echter weerstand tegen **grootschalige** uitbreiding (2.000-3.000 woningen); geen bericht gevonden dat zich specifiek uitspreekt tegen kleinschalige (10-12 woningen) buitengebied-initiatieven.

### Buitengebied-deelgebieden van Zwolle (geverifieerd)
Zwolle onderscheidt in het buitengebied deelgebieden met een eigen karakter: **Herfte/Wijthmen**, de **IJsselzone**, en **Langenholte/Vechtcorridor**. Geverifieerd Zwols: Windesheim, Wijthmen, Herfte, Zalné, Langenholte, Mastenbroek (nu wijk 22/Stadshagen), Berkum-buitengebied/Berkum Veldhoek. **Niet Zwols, ondanks suggestie in de onderzoeksopdracht:** Zalk (dorp in gemeente **Kampen**; "Zalkerdijk" is de dijkweg richting Zalk, het Zwolse deel ligt bij de grens met Kampen), "Veecaten" (geen actuele buurtschap, maar de naam van de private ontwikkelaar "Veecaten B.V." — zie §3/§6), Voorst (ligt bij Apeldoorn/Twello in Gelderland, niet bij Zwolle — mogelijk verward met de gelijknamige gemeente Voorst die elders in dit 19-gemeenten-onderzoek apart wordt behandeld).

**Status Omgevingsvisie Zwolle:** de **Ontwerp-Omgevingsvisie** is gepubliceerd als Gemeenteblad 2025, 448748 (bekendmakingsdatum 15-10-2025, https://zoek.officielebekendmakingen.nl/gmb-2025-448748.html). **Aanvulling verificatieronde 2026-10-02:** het college keurde de ontwerp-Omgevingsvisie ("Zwolle van Overmorgen", aanvulling op "Zwolle van Morgen" 2021; horizon 2040/2050) op 14-10-2025 goed; ter inzage 27-10 t/m 8-12-2025 (bron: zoekresultaat-samenvattingen o.a. https://zoek.officielebekendmakingen.nl/gmb-2025-448748.html). Volgens de raadsbrief "Beleidsupdate Wonen" (16-12-2025, https://zwolle.bestuurlijkeinformatie.nl/Document/View/d8b52ba3-fcae-4c51-a879-f282118c70ef) heeft de beoogde vaststelling eind 2025 **vertraging** opgelopen; de raad stelde wél het tussenproduct **Ruimtelijk Toekomstperspectief (RTP)** vast. Het coalitieakkoord 2026-2030 kondigt aan dat voor Vechtrand en Nieuw Zuthem "gebiedsvisies" worden gemaakt "om een complete omgevingsvisie vast te stellen". Een definitief raadsbesluit over de Omgevingsvisie is niet gevonden; de huidige Omgevingsvisie blijft vermoedelijk "Zwolle van Morgen" (2021) met het RTP als richting.

**Volkshuisvestingsprogramma Zwolle (nieuw, verificatieronde 2026-10-02):** volgens dezelfde raadsbrief wordt het Volkshuisvestingsprogramma een "integraal beleidskader voor het wonen", gebaseerd op een woningbehoefteonderzoek (Primos 2024-prognose), met **oplevering gepland in het derde kwartaal van 2026**. Omdat de Omgevingsvisie nog niet is vastgesteld, komt de visie op wonen in het programma te staan en wordt het een **raadsbevoegdheid** (i.p.v. collegebevoegdheid); na de verkiezingen van maart 2026 wordt hiervoor een proces met de nieuwe raad ingericht. Kader: Wet versterking regie volkshuisvesting (toen nog niet in werking; sinds 1-7-2026 wel). Of het programma inmiddels (Q3 2026) is opgeleverd of buitengebied-/uitbreidingslocaties aanwijst, is niet gevonden. Dit beantwoordt Bijlage A, A4 deels.

**Lacune:** een definitief vastgesteld raadsbesluit (niet-ontwerp) van de Omgevingsvisie Zwolle en een opgeleverd Volkshuisvestingsprogramma zijn niet gevonden — status navragen bij de gemeenteraad (zwolle.bestuurlijkeinformatie.nl)/www.zwolle.nl/omgevingsvisie.

---

## 3. Openheid voor agrarische herbestemming (10-12 woningen)

### (a) Wettelijk/procedureel kader
Zwolle werkt onder de Omgevingswet met het **Omgevingsplan gemeente Zwolle** (CVDR696214, meest actuele versie geldend vanaf **08-05-2026**; eerdere versies vanaf 01-01-2024, 06-12-2024, 24-07-2025 — regelmatig geactualiseerd). Voor initiatieven die niet binnen het omgevingsplan passen: het traject **Nieuwe Ruimtelijke Initiatieven (NRI)** (aanmelding: formulier + situatietekening → ruimtelijkeinitiatieven@zwolle.nl) of, bij grotere gebieds-/locatieontwikkelingen, de **Routekaart gebieds- en locatieontwikkelingen** (in overleg met markt/corporaties/Concilium Zwolle). Aan de "initiatieventafel" wordt bepaald welk traject van toepassing is. Contact beleidskaders: E. Boogmans (e.boogmans@zwolle.nl), algemene vragen F. van Dijk (f.van.dijk@zwolle.nl).

Nieuwbouw op agrarische grond die niet past binnen het omgevingsplan loopt via een **buitenplanse omgevingsplanactiviteit (BOPA)**. Kern van de wettelijke toets, letterlijk uit de toelichting op het Omgevingsplan: *"Voor een buitenplanse omgevingsplanactiviteit geldt dat op grond van artikel 8.0a, tweede lid, van het Bkl, de vergunning alleen wordt verleend met het oog op een evenwichtige toedeling van functies aan locaties."* Een aparte "Beleidsnota BOPA" (zoals sommige buurgemeenten die hebben) bestaat in Zwolle niet als losse CVDR-regeling — de toets ligt besloten in het Omgevingsplan en de Omgevingsvisie zelf.

> **⚠️ Belangrijke, cruciale bevinding — bindend raadsadvies + verplichte participatie boven 5 woningen buitengebied:**
> Het **"Besluit adviesrecht gemeenteraad en verplichte participatie onder de Omgevingswet"** (CVDR726092, vastgesteld door de raad 7 februari 2022) bepaalt: *"5 woningen of meer in één project ... in het stedelijk gebied of meer dan 5 woningen in het buitengebied"* → **bindend adviesrecht van de gemeenteraad** én **verplichte participatie**. Een CPO-project van 10-12 woningen in het buitengebied overschrijdt deze drempel ruimschoots. Dit betekent: de raad krijgt formeel, bindend adviesrecht op de BOPA-vergunning (niet alleen het college), en participatie is wettelijk verplicht, niet optioneel. Er zijn aanwijzingen (niet volledig geverifieerd) dat de raad in september 2025 een geactualiseerde versie heeft vastgesteld — controleer de actuele versie op https://lokaleregelgeving.overheid.nl/CVDR726092.

**Provinciaal toetsingskader bovenop de Zwolse procedure** (uit `provincie_overijssel.md` §1.3-1.6, §2, §4; stand 2026-10-02; de Zwolse toepassing hiervan is, tenzij anders vermeld, niet apart onderzocht):
- **KGO (art. 4.11):** "de bouw van nieuwe woningen" valt expliciet onder lid 2 sub c, dus ook een CPO van 10-12 woningen zodra het nieuwvestiging in de Groene Omgeving betreft. Er is **geen provinciebrede rekenformule**; de gemeente kan een kader opstellen, anders moet per geval worden onderbouwd dat extra "rood" in evenwicht is met de investering in ruimtelijke kwaliteit (en bij gebiedsspecifieke landbouwgebieden gericht op natuur, water en landschap). De KGO is *niet* bedoeld voor **stadsuitleg**: daar geldt art. 4.5 lid 1 met de redeneerlijn. Of een Zwolse kandidaatlocatie "stadsrand" (uitleg) of "Groene Omgeving" (KGO) is, bepaalt Zwolle zelf — de contour is in de gevonden Zwolse stukken niet vastgesteld (Bijlage A, B4).
- **Landbouwgebied-typologie (art. 4.123-4.124):** art. 4.124 lid 1 staat bij transformatie van (agrarische) bouwpercelen in *generieke* landbouwgebieden alleen nieuwe functies toe die geen beperking voor de landbouw in de omgeving opleveren; lid 4 biedt afwijkingsroutes (landbouw heeft feitelijk geen ontwikkelruimte meer, of een samenhangende gebiedsvisie toont aan dat landbouw per saldo verbetert — o.a. rood-voor-rood-woningen elders bij een kern). In *gebiedsspecifieke* landbouwgebieden moet de KGO-investering gericht zijn op klimaat, natuur en water. Welk type voor een Zwolse locatie geldt, is niet vastgesteld (kaartlaag niet geraadpleegd).
- **Woonafspraken (art. 4.14-4.15):** nieuwe woningen moeten passen binnen de Woondeal West-Overijssel; omgevingsplannen leggen **bij voorkeur max. 80%** van de behoefte vast (de overige 20% is ruimte voor niet-voorziene initiatieven). Afwijking vergt instemming van de regiogemeenten én GS.
- **Redeneerlijn (art. 4.122), water en bodem sturend (art. 4.13), energiesysteem (art. 4.125):** nieuwe/aangescherpte onderbouwingspunten; de redeneerlijn mag "in verhouding tot de omvang" beperkt zijn bij kleine ontwikkelingen.
- **Voorkantsamenwerking en Lijst BOPA:** sinds 1-1-2024 geen Bro 3.1.1-vooroverleg meer, maar voorkantsamenwerking (provinciale front-office/accounthouder Ruimte; regionale Omgevingstafel) plus kennisgeving. Voor een **BOPA** waarover hoofdstuk 4 van de verordening instructieregels stelt (dus ook nieuwe woningen in de Groene Omgeving) is **provinciaal advies én instemming** vereist (streeftermijn advies 4 weken, bij de uitgebreide procedure 6 weken; instemming 4 weken). Een CPO van 10-12 nieuwe woningen op agrarische grond valt hier vrijwel zeker onder (*interpretatie*; Zwolse praktijk niet onderzocht).
- **Uitzonderingenlijst vooroverleg 2023:** geen vooroverleg nodig voor ≤ 11 woningen in bestaand bebouwd gebied van kernen > 1.000 inwoners; in de Groene Omgeving nooit voor nieuwe woningen. 10-12 woningen ligt precies op de 11-woningengrens; kennisgeving aan de provincie blijft in alle gevallen verplicht.
- **Directe werking (art. 4.2a):** sinds de Actualisatie 2026 (1-7-2026) gelden nieuwe instructieregels bij een BOPA direct, ook als het Zwolse omgevingsplan nog niet is aangepast.

**Rood-voor-Rood** wordt in Zwolle toegepast (gemeentelijke uitwerking van de provinciale KGO; er is geen apart provinciaal rood-voor-rood- of sloopfonds, provincie_overijssel.md §3.3): vereist doorgaans een omgevingsplanwijziging via het NRI-traject, met als voorwaarde dat nieuwbouw de ruimtelijke kwaliteit verbetert. Concrete voorbeelden:
- **Kiekeboslaantje:** na sloop van agrarische bedrijfsbebouwing ruimte voor max. 7 bouwkavels; 2 voor de vertrekkende eigenaar (maatschap Beltman), opbrengst overige 5 naar kwaliteitsverbetering elders.
- **Windesheim (landgoed):** twee voormalige agrarische bedrijfslocaties (Wijheseweg 49/59) — sloop van bedrijfsgebouwen in ruil voor **2 nieuwe woningen** op Wijheseweg 59. Kleinschalig maar een direct precedent van de rood-voor-rood-logica.

### Geen gepubliceerde Zwolse KGO-rekenformule
In tegenstelling tot buurgemeenten (Dinkelland/Tubbergen, Deventer, Rijssen-Holten, Hardenberg, Bronckhorst — die allen wél een eigen CVDR-gepubliceerde KGO-/rood-voor-rood-beleidsregel met rekenformule hebben) heeft **Zwolle geen eigen gepubliceerde KGO-rekenformule of sloop-bouw-ratio**. Dit is drievoudig bevestigd (drie onafhankelijke deelonderzoeken, tientallen zoekvarianten, telkens bleken kansrijk ogende CVDR-treffers bij verificatie van andere gemeenten — Tubbergen, Best, Peel en Maas, Nissewaard, Bronckhorst, Staphorst, Hof van Twente, Haaksbergen — te zijn). In plaats daarvan hanteert Zwolle een **interne, niet-openbaar-gepubliceerde "Handreiking KGO gemeente Zwolle"**, expliciet genoemd als kaderdocument in officiële raadsstukken (zie hieronder), en behandelt erfontwikkelingen als maatwerk/pilot.

Uit de Raadsbrief "Pilot erfontwikkeling Zalkerdijk 26" (15-04-2025, portefeuillehouder Gerdien Rots), integraal geciteerd — **dit bevestigt expliciet dat Zwolle op raadpleegdatum geen actueel, geactualiseerd buitengebiedbeleid heeft**:

> "Het plan tot realisatie van meerdere wooneenheden op het erf van Zalkerdijk 26a is bij toepassing van het huidige beleid (zowel bij gemeente als provincie) niet passend. Daarom hebben wij een pilot doorlopen om te onderzoeken op welke wijze het wel passend te maken is. Op basis van deze pilot hebben wij input opgehaald voor het (op termijn) te actualiseren beleid voor het buitengebied en specifiek voor erfontwikkelingen in het buitengebied."
>
> "Voor het ontwikkelen van beleid voor het buitengebied zijn wij als college verantwoordelijk. In de prioritering van werkzaamheden bepalen we op welk moment we het beleid voor het buitengebied actualiseren."
>
> "Het buitengebied van Zwolle is in transitie. Agrarische bedrijven stoppen, de vragen om erven te ontwikkelen met woningen nemen toe. De kans op verrommeling in het buitengebied neemt toe door de aanwezigheid van leegstaande stallen en/of boerderijen."

> **Nieuw (verificatieronde 2026-10-02) — het coalitieakkoord 2026-2030 kondigt een KGO-actualisatie aan.** Uit het volledige akkoord "Bouwen op Zwolse kracht" (https://media.d66.nl/uploads/sites/78/2026/06/Coalitieakkoord-Zwolle-2026-2030-Bouwen-op-Zwolse-kracht.pdf, p. 22, lokaal geëxtraheerd): *"We kijken bij ruimtelijke ontwikkelingen in dorpen, buurtschappen en het buitengebied zorgvuldig wat past bij de schaal, identiteit en leefkwaliteit van het gebied. Samen met partners actualiseren we het beleid Kwaliteitsimpuls Groene Omgeving (KGO), zodat er meer ruimte ontstaat voor passende ontwikkelingen op erven en in het buitengebied."* En (p. 20-21): *"Nieuwe ontwikkelingen dragen bij aan de kwaliteit, eigen identiteit en samenhang [en] de leefbaarheid van het bestaande buitengebied en versterken de eigen waarde en het karakter daarvan."* Dit bevestigt (a) dat Zwolle een bestaand KGO-beleid hanteert dat wordt herzien, (b) een gunstige bestuurlijke koers voor erfontwikkeling ("meer ruimte"), maar (c) zonder termijn, schaal of mention van CPO/woningaantallen. Het is een voornemen, geen vastgesteld beleid. Dit verfijnt Bijlage A, B3.

**Schaal van de Zwolse rood-voor-rood-/erfpraktijk (koppeling aan provincie_overijssel.md §2.3):** de provincie merkt op dat rood-voor-rood- en erftransformatieregimes doorgaans zijn ontworpen voor enkele woningen per erf (*interpretatie*, niet door de provincie bevestigd). Dat past bij de Zwolse voorbeelden: Windesheim 2 woningen, Zalkerdijk 26a 3 wooneenheden, Kiekeboslaantje maximaal 7 kavels. Het enige grotere Zwolse buitengebied-voorbeeld (Erfgenamenweg Wijthmen, 32 zorgeenheden) loopt niet via rood-voor-rood maar via een gebiedsontwikkeling met Ruimtelijk Ontwikkelplan en omgevingsplanwijziging. Een CPO van 10-12 woningen valt dus buiten de schaal van de gevonden Zwolse erfprecedenten; de "Handreiking KGO gemeente Zwolle" (intern) is niet gelezen, dus of die een maximum per erf kent, is onbekend (Bijlage A, B2).

### (b) Gemeentelijke houding — kernprecedent Zalkerdijk 26a / "Buitengoed Veecaten" (2024-2025)
Dit is het meest concrete, actuele en relevante precedent uit het hele onderzoek voor een kleinschalig collectief woonproject op voormalige agrarische grond in het Zwolse buitengebied.

**Feitenrelaas** (gereconstrueerd uit officiële bestuursdocumenten):
- Initiatiefnemer **Veecaten B.V.** wil het voormalig agrarisch erf **Zalkerdijk 26a** (grens Zwolle/Kampen) ontwikkelen tot een kleinschalige erfontwikkeling: **drie wooneenheden** aanvullend op de bestaande woonboerderij, onder de naam "Buitengoed Veecaten" — expliciet aangeduid als "**collectief erf**".
- **September 2024:** intentieovereenkomst gemeente-initiatiefnemer voor een pilot.
- **6 november 2024** (raadsvoorstel Stadsbroek/IJsselvizier): *"Samen met de provincie Overijssel spreken wij over de wens om beleid te ontwikkelen op het gebied van KGO waar we zoeken naar een gebiedsgerichte aanpak, in plaats van een locatiegerichte aanpak."*
- **24 maart 2025** (beslisnota college, "Afronding Pilot Zalkerdijk 26a"): college besluit expliciet **af te wijken van de standaard-KGO-werkwijze**: *"De kaders van het huidige KGO beleid en de wijze waarop wij dit als gemeente Zwolle toepassen, maakt dat een erfontwikkeling niet altijd mogelijk blijkt vanwege de reden dat maatregelen om de groene omgeving kwalitatief te verbeteren niet altijd passen op de percelen van een initiatief."*
- **Provinciale/waterschaps-rol, integraal geciteerd:** *"Provincie Overijssel en Waterschap Drents Overijsselse Delta hebben een positieve grondhouding. […] Bovendien heeft de provincie onlangs besloten meer ruimte te bieden voor (erf)ontwikkelingen in het buitengebied die zijn gelegen in de stadsrandzone. Dit plan past in deze gewijzigde werkwijze."*
- *Duiding met het provinciale kader (interpretatie):* de provinciale verruiming "voor erfontwikkelingen in de stadsrandzone" sluit aan bij de bevoegdheid van de gemeente om te bepalen of een stadsrandlocatie als stedelijk gebied of als Groene Omgeving telt (provincie_overijssel.md §1.2). Of de provincie Zalkerdijk 26a via de KGO, via art. 4.5 lid 1 of via een andere route heeft beoordeeld, en onder welk landbouwgebied-type de locatie valt, volgt niet uit de gevonden stukken; de brief van de provincie (bijlage bij de raadsbrief) zou dat kunnen verhelderen. De pilot dateert bovendien van vóór de Actualisatie 2026 (1-7-2026), zodat nieuwe instructieregels (4.122, 4.124) er niet op zijn getoetst.
- **Uitkomst:** max. drie wooneenheden, collectief binnenerf, collectief gebruik van een hooimijt, beheer via een VvE; voorwaarde: een **"KGO-balans"** (waardeontwikkeling vs. investering groene omgeving) op te stellen "in overleg met initiatiefnemer **en de provincie**". Initiatiefnemer betaalde **€7.500** als NRI-projectbijdrage voor de pilotfase; voor het vervolg gelden "reguliere financiële en procedurele afspraken qua kostenverhaal, leges, etc."
- **Precedentwerking uitdrukkelijk beperkt:** *"Dit proces hebben wij specifiek als 'pilot' behandeld. Daarmee geven we aan dat voor dit proces, gezien de historie en de context specifieke afspraken gemaakt zijn en daarmee voorkomen we precedentwerking ten opzichte van andere, in bepaalde opzichten vergelijkbare vraagstukken."*

Bronnen (bestuursdocumenten Zwolle, geraadpleegd 21-08-2026): raadsvoorstel Stadsbroek en IJsselvizier (6-11-2024, zwolle.bestuurlijkeinformatie.nl/Document/View/2bdfbb94-a505-4f25-a8d7-cb8dc98c2dbe); beslisnota college (24-3-2025, .../e489cd29-772e-452c-9c60-3265dfa475ca); raadsbrief (15-4-2025, .../561bbd5c-6691-452e-9ff6-ed79d8c91179). **Lacune:** de bijlagen (eindrapportage pilot, inrichtingsplan, brief provincie) zijn niet apart doorzocht — aanbevolen vervolgstap voor de opdrachtgever.

**Gebiedsproces IJsselvizier** (waarbinnen Zalkerdijk 26a valt) was aangewezen voor een landschapsontwikkelplan expliciet bedoeld om "bestaande agrarische erven die niet meer als zodanig in gebruik zijn" te transformeren naar "plekken waar nieuwe woonvormen en -gemeenschappen kunnen ontstaan" — vrijwel een blauwdruk voor het type CPO-project van dit onderzoek. Het proces is echter per raadsbesluit van 6-11-2024 **voorlopig niet doorgezet** wegens gebrek aan ambtelijke capaciteit (benodigd budget: €238.000). Grondpositie: ca. 8 ha gemeentelijk (kortlopend verpacht), ca. 11 ha particulier.

**Geen bevestigd voorbeeld van een provinciale reactieve aanwijzing of zienswijze tegen een Zwols buitengebied-plan** is gevonden (een aanvankelijke treffer uit 2010 bleek bij verificatie over gemeente Ommen te gaan, niet Zwolle) — consistent met de vondst uit het provinciale onderzoek dat dit instrument sinds 2014 provinciebreed slechts éénmaal is ingezet.

**Erfgenamenweg Wijthmen (2026, in voorbereiding)** — tweede belangrijke precedent, groter van schaal: op ca. 20 ha agrarische grond (eigendom Herstructureringsmaatschappij Overijssel/HMO) wordt een gemengd plan ontwikkeld met 24 + 8 = 32 wooneenheden (wonen+zorg), een kleinschalige biologische zorgboerderij en natuurontwikkeling. Processtatus medio 2026: startnotitie vastgesteld, samenwerkingsovereenkomst HMO getekend, Ruimtelijk Ontwikkelplan (ROP) in voorbereiding voor indiening 2e helft 2026, omgevingsplanwijziging vereist, participatietraject volgens de Zwolse "Hanza!"-aanpak loopt. Bron: https://www.rtvfocuszwolle.nl/zorg-natuur-en-water-komen-samen-in-wijthmen-32-zorgwoningen-boerderij-en-waterwinning-gepland-aan-erfgenamenweg/ (01-02-2026). **Geeft een reële indicatie van doorlooptijd:** meer dan een jaar tussen startnotitie en indiening ROP, vóór een omgevingsplanwijziging goedgekeurd hoeft te zijn.

### (c) Concreet stappenplan
1. Vooroverleg/melding bij team **Nieuwe Ruimtelijke Initiatieven** (formulier + situatietekening → ruimtelijkeinitiatieven@zwolle.nl); beoordeling of het idee past binnen omgevingsplan/beleidskaders.
2. Aan de "initiatieventafel": bepaling of het traject **Routekaart** (grotere gebieds-/locatieontwikkeling) of **NRI** (kleiner/individueel) van toepassing is.
3. Bij rood-voor-rood/KGO-achtige constructies: aanvraagfase, beoordeling ruimtelijke kwaliteitsverbetering ("KGO-balans"), eventueel in samenspraak met de provincie (zie Zalkerdijk-precedent).
3a. **Voorkantsamenwerking met de provincie, parallel aan stap 1-3 en vóór het gemeentelijk besluit:** via de gemeentelijke RO-afdeling (provinciale accounthouder Ruimte/front-office; evt. Omgevingstafel). Het provinciaal belang (KGO, art. 4.5 lid 2, woonafspraken, landbouwgebied-typologie, redeneerlijn) wordt hier voorlopig/definitief beoordeeld. Bij Zalkerdijk 26a waren gesprekken met provincie en waterschap onderdeel van de pilotfase.
4. Omgevingsplanwijziging of buitenplanse omgevingsplanactiviteit (BOPA) via omgevingsvergunning; bij een BOPA met nieuwe woningen in de Groene Omgeving **provinciaal advies én instemming** (Lijst BOPA; zie het kader hierboven). Bij een omgevingsplanwijziging: kennisgeving van het ontwerp aan de provincie, die zo nodig een zienswijze indient.
5. Vanwege de omvang (10-12 woningen, >5 in buitengebied): **bindend adviesrecht raad + verplichte participatie** (CVDR726092) — dit voegt een extra formele stap toe t.o.v. kleinere initiatieven.
6. Publicatie, zienswijzen, besluitvorming, beroepstermijn.

**Indicatieve doorlooptijd:** niet expliciet door de gemeente gepubliceerd. Uit de kavelproject-Q&A (Oude Mars) blijkt dat 12 maanden gebruikelijk wordt geacht voor individuele bouwkavels; uit het Zalkerdijk-precedent (intentieovereenkomst sept. 2024 → beslisnota maart 2025 → raadsbrief april 2025, dus ca. 7 maanden voor de pilotfase alléén, exclusief het vervolgtraject) en Erfgenamenweg Wijthmen (>1 jaar tussen startnotitie en ROP-indiening) is een realistische inschatting **1-2 jaar van vooroverleg tot onherroepelijk besluit**, oplopend bij complexere plannen of wanneer (zoals bij 10-12 woningen zeer waarschijnlijk) het bindend raadsadvies-traject van toepassing is. **Provinciale deeltermijnen (provincie_overijssel.md §4.5):** 10 werkdagen voor een reactie op eenvoudige KGO-plannen (Uitzonderingenlijst; niet geverifieerd of dit in 2026 nog geldt), 4 weken advies (BOPA categorie B/reguliere procedure), 6 weken advies bij de uitgebreide procedure en 4 weken voor instemming; voor complexere plannen (NNN, water/bodem sturend, afwijking van woonafspraken) geen vaste termijn. Moment van betrokkenheid: provincie vroeg (voorkantsamenwerking), waterschap (Drents Overijsselse Delta bij Zalkerdijk) in dezelfde fase, raad bij de BOPA-beoordeling (bindend advies).

**Lacune:** geen officiële bevestiging door de gemeente van de Zwolse doorlooptijd; navraag bij team NRI nodig voor een projectspecifieke inschatting.

### (d) Kansrijk vs. kansarm
**Kansrijk:** initiatief op een **bestaand (voormalig) agrarisch erf** (niet onbebouwde grond); aantoonbare marktvraag; sloopcompensatie (rood-voor-rood-achtige constructie); investering in landschappelijke/water-/natuurkwaliteit; ligging in een deelgebied waar functiemenging al wordt gestimuleerd (Herfte/Wijthmen, IJsselzone, Langenholte/Vechtcorridor); collectieve/VvE-achtige beheervorm (sluit aan bij het Zalkerdijk-precedent); positionering in de "stadsrandzone" (expliciet genoemd door de provincie als gebied met verruimde ruimte voor erfontwikkeling).

**Kansarm:** nieuwbouw op **onbebouwde landbouwgrond** zonder sloopcompensatie; locaties in "Natuurlandschap" of gebieden met expliciete natuurwaarden (Vecht/uiterwaarden, Dijklanden — *"In Dijklanden bieden we geen ruimte voor een nieuwe woonwijk"*); ontwikkelingen zonder aantoonbare landschappelijke meerwaarde; locaties in een **generiek landbouwgebied** waar de nieuwe functie de omliggende landbouw beperkt (art. 4.124 lid 1, tenzij een afwijkingsroute uit lid 4 onderbouwd kan worden) — de provinciale visie noemt dit "nee, tenzij". Voor VAB-erven geldt dat herontwikkeling mogelijk is "zolang het past bij omliggende agrarische bedrijven" (provincie_overijssel.md §1.4). Het type landbouwgebied van een concrete Zwolse locatie is niet onderzocht.

### (e) Eindoordeel per schaalscenario
- **3-6 woningen op bestaand erf (VAB/rood-voor-rood-achtig):** **relatief kansrijk.** Sluit direct aan bij bestaand instrumentarium (rood-voor-rood, KGO-maatwerk) en bij het Zalkerdijk-precedent (3 wooneenheden toegestaan als "pilot", met positieve grondhouding van provincie én waterschap). Vervolgstap: melding bij team NRI (ruimtelijkeinitiatieven@zwolle.nl).
- **10-12 woningen op bestaand erf:** **matig kansrijk, mits goed onderbouwd.** Grotere schaal dan het Zalkerdijk-precedent (3 woningen); overschrijdt de drempel van het bindend raadsadvies + verplichte participatie (CVDR726092, >5 woningen buitengebied); vergt waarschijnlijk het Routekaart-traject i.p.v. een eenvoudige NRI-melding, met vroege betrokkenheid van de provincie (naar analogie van Zalkerdijk) en een uitgewerkte KGO-balans/sloopcompensatie. Vervolgstap: contact E. Boogmans (e.boogmans@zwolle.nl) of F. van Dijk (f.van.dijk@zwolle.nl); vroegtijdig verkennend gesprek met team NRI wordt sterk aanbevolen gezien de precedentwerking-terughoudendheid die de gemeente bij Zalkerdijk expliciet uitsprak.
- **10-12 woningen op onbebouwde agrarische grond:** **het minst kansrijke scenario** binnen het huidige kader. De Omgevingsvisie beschermt de Groene Omgeving expliciet; vereist "geen ruimte in de Stedelijke Omgeving" plus aantoonbare marktvraag; zonder sloopcompensatie naar verwachting kansarm — tenzij het samenvalt met een gebied waarvoor de gemeente al actief regie voert (Vechtrand/Nieuw Zuthem, waar overigens de gemeente zelf de ontwikkelaar/regisseur is via het gevestigde voorkeursrecht, niet een externe CPO-initiatiefnemer). Provinciaal: de juridisch relevante instructieregels zijn hier vooral art. 4.4/4.5 lid 2, 4.11 (KGO), 4.13, 4.14-4.15 en 4.122; de "nee, tenzij" uit de visie werkt voor onbebouwde grond (buiten een erf) vooral via de provinciale afweging in voorkantsamenwerking en bij BOPA-instemming — een zwaardere informele hobbel dan de verordeningstekst alleen suggereert (*interpretatie* in provincie_overijssel.md §1.4). Vervolgstap: navraag bij team NRI of de beoogde locatie binnen of buiten de Vechtrand/Nieuw Zuthem-gebiedsvisies valt, en welk type landbouwgebied (generiek vs. gebiedsspecifiek, kaartlaag art. 4.123) op de locatie geldt.

---

## 4. VAB-beleid (Vrijkomende Agrarische Bebouwing)

**Drievoudig bevestigde bevinding: Zwolle heeft geen zelfstandige, gepubliceerde VAB-beleidsregel.** Uitgebreide, onafhankelijke CVDR-zoekacties door drie deelonderzoeken (tientallen zoekvarianten: "VAB", "vrijkomende agrarische bebouwing", "agrarisch", "buitengebied", "functieverandering") leverden stelselmatig **0 Zwolse treffers** op. Treffers die aanvankelijk kansrijk leken, bleken bij verificatie regelingen van andere gemeenten (Haaksbergen — vervallen 2012 —, Hof van Twente, Peel en Maas, en met name **Best**, waarvan een CVDR-nummer aanvankelijk abusievelijk aan Zwolle werd toegeschreven).

VAB-gebruik wordt in Zwolle kennelijk **niet via een losstaande beleidsregel** geregeld, maar via:
- De generieke Omgevingsvisie-uitgangspunten (§2/§3: op voormalige agrarische erven is onder voorwaarden ruimte voor aanvullende woon-/werkmilieus).
- De functie-specifieke regels in het **Omgevingsplan gemeente Zwolle** (CVDR696214), met name de agrarische functie-afdelingen 4.1-4.15 — deze bevatten vermoedelijk de daadwerkelijke wijzigings-/afwijkingsbevoegdheden, maar zijn (gezien de omvang van ca. 900.000 tekens) niet artikel-voor-artikel doorzocht in dit onderzoek.
- **Ad-hoc pilots** zoals Zalkerdijk 26a (§3), niet via een vooraf vastgesteld toetsingskader.

**Lacune (kernlacune van dit rapport):** een geverifieerd, geciteerd Zwols VAB-beleidsdocument ontbreekt. **Waar te vinden/navragen:** rechtstreeks de gebiedsspecifieke onderdelen van het Omgevingsplan via DSO/Omgevingsloket (omgevingswet.overheid.nl) of ruimtelijkeplannen.nl/planviewer.nl voor de specifieke locatie; team Nieuwe Ruimtelijke Initiatieven (ruimtelijkeinitiatieven@zwolle.nl); afdeling Ruimte en Economie (038-498 3266). 

**Provinciale VAB-ondersteuning (provincie_overijssel.md §2.4, §3.1; Bijlage A, categorie D):**
- **Subsidie 4.39 "Beleid transformatie agrarische bebouwing, erven en gronden"** (voor gemeenten, niet voor initiatiefnemers; activiteit A max. € 30.000, B/C intergemeentelijk): niet vastgesteld of Zwolle meedoet of een aanvraag heeft lopen. De regeling stond op 2026-10-02 nog open, maar het plafond (€ 1.640.250) kan snel uitgeput raken en middelen moeten **vóór eind 2026 verplicht** zijn — tijdgevoelig. Het IJsselvizier-proces is stilgelegd wegens capaciteitsgebrek (€ 238.000 nodig voor een landschapsontwikkelplan); dat maakt dit een logisch aanknopingspunt, maar er is **geen bewijs** dat Zwolle subsidie heeft aangevraagd. Navraag: vab@overijssel.nl / Overijssel Loket.
- **Erfcoach Overijssel** (gratis, tot 2026 verzekerd, voornemen tot 2029) en **Atelier Overijssel**: niet vastgesteld of die in Zwolle zijn ingezet.
- **Provinciale brief aan alle colleges, 25-2-2025 ("Routekaart VAB- en Erftransformatie-programma's", ook in het Zwolse raadsinformatiesysteem: https://zwolle.bestuurlijkeinformatie.nl/Document/View/420f3788-b48d-4782-9cbb-e04f0a083739, verificatieronde 2026-10-02):** GS nodigt gemeenten uit een intergemeentelijk VAB-/erftransformatieprogramma te ontwikkelen en biedt "ruimte om te leren" (voorkantsamenwerking voor "sympathieke initiatieven die mogelijk niet direct binnen de standaard beleidslijnen lijken te passen"; prioriteit bij koplopersprojecten). Citaat: *"We zien de meeste kansen (en minste knelpunten) op VAB-locaties [...] nabij (groei)kernen. In eerste instantie voor woonfuncties [...] mits het geen belemmeringen opwerpt voor functies die afhankelijk zijn van specifieke omstandigheden, zoals landbouw met generieke opgaven of natuur."* Beoordeling gebeurt aan de hand van de (concept-)Omgevingsvisie. Het Rijk stelde in het PPLG-maatregelpakket € 3.645.000 beschikbaar voor Overijsselse gemeenten voor ruimtelijk en VAB-beleid, deels via subsidie 4.39. Deze brief is niet Zwolle-specifiek; een Zwolse reactie of aanmelding is niet gevonden.
- **Provinciale lijn voor VAB's:** herontwikkeling met bijbehorende erven en gronden is mogelijk "zolang het past bij omliggende agrarische bedrijven en agrarische bedrijven uit de omgeving niet worden beperkt"; de Woondeal West-Overijssel noemt VAB-transformatie niet als opgave (de Twente-woondeal wel). Het door de provincie genoemde collectieve erfprecedent BuitenDelen (Lettele) ligt in gemeente **Deventer**, niet in Zwolle.
- **Zwolse precedenten (gemeentelijk VAB-beleid ontbreekt, zie boven):** Zalkerdijk 26a (3 wooneenheden), Kiekeboslaantje (max. 7 kavels), Windesheim (2 woningen), Erfgenamenweg Wijthmen (zorg/natuur, HMO-grond); een maximumaantal woningen per VAB-erf en eisen aan omliggende bedrijven zijn niet gevonden.

---

## 5. Grondbeleid

### Grondprijzen
Bron: Grondprijzenbrief (jaarlijks door het college vastgesteld), 21-08-2026.

> "De grondprijzen voor grondgebonden woningen en kavels die in particulier opdrachtgeverschap worden uitgegeven komen tot stand volgens de residuele grondwaarde rekenmethodiek. Hierbij moet de uitkomst aan de minimale grondprijs voldoen die staat opgenomen in tabel 2."

| Categorie | Minimale grondprijs |
|---|---|
| Sociale woningbouw (grondgebonden/gestapeld) | € 125,00 /m² |
| Vrije sector woningbouw, grondgebonden | € 270,00 /m² |
| **PO-kavels (particulier opdrachtgeverschap), tot 750 m²** | **€ 370,00 /m²** |
| **PO-kavels, elke m² boven 750 m²** | **€ 210,00 /m²** |
| Bedrijventerrein Hessenpoort | € 160,00 /m² |
| Maatschappelijke voorzieningen | € 180,00 /m² |

> "De grondprijzen zijn minimale prijzen. Differentiatie in de grondprijs is mogelijk en wordt beïnvloed door factoren zoals de ligging van de kavel […] en specifieke omstandigheden."

> **⚠️ Tegenstrijdige bevinding — erfpacht/huurpercentage:** het deelonderzoek gebaseerd op de (op zwolle.nl gepubliceerde) **Grondprijzenbrief 2026** vond: *"De gemeente hanteert voor het bepalen van de huurprijs van grond een percentage van 5% van de grondwaarde. Er wordt een minimale huurprijs van € 175,00 per jaar gehanteerd."* Het deelonderzoek gebaseerd op de **Grondprijzenbrief 2025** (vastgesteld door B&W 26-11-2024, geraadpleegd via het bestuurlijke-informatiesysteem) vond echter: erfpachtcanon/huurprijs **6%** van de grondwaarde, minimum **€ 150,00/jaar**. Beide cijfers zijn correct geciteerd uit hun eigen bron; het verschil is vermoedelijk een reële aanpassing tussen de 2025- en 2026-editie van de Grondprijzenbrief, maar dit kon in dit onderzoek niet met een directe vergelijking van beide volledige documenten worden bevestigd. **Voor een concreet project: altijd de meest actuele Grondprijzenbrief (thans 2026) rechtstreeks bij de gemeente opvragen.** *Verificatieronde 2026-10-02:* een poging de Grondprijzenbrief 2026 van Zwolle terug te vinden leverde alleen brieven van andere gemeenten (Zutphen, Noordenveld) en een Zwolse erfpachtrapportage van Over Morgen (2021/22) op; de tegenstrijdigheid is dus **niet opgelost**.

**Grondbeleid in het coalitieakkoord 2026-2030 (verificatieronde 2026-10-02, p. 5 en 21-22):** de portefeuille *Vastgoed en grondbeleid* ligt bij wethouder Johran Willegers (VVD). Het akkoord wil de huidige **7.000 woningen in zachte plannen versneld omzetten naar harde plancapaciteit** (minimaal 4.400 woningen in de bestuursperiode), kritisch kijken naar "lokale koppen" die grondexploitaties onder druk zetten, het voortouw nemen "bij gebieden waar we als gemeente regie hebben over de grond", en marktpartijen faciliteren met parallel plannen. Dit bevestigt de gemeentelijke regiepositie en prioriteit voor grotere locaties; een reservering voor initiatieven van derden/CPO is niet vermeld.

Een expliciete grondprijs voor **agrarische grond** (los van woningbouw) is in geen van beide brieven als webtekst/geëxtraheerde tekst aangetroffen — vermoedelijk alleen in de volledige PDF. Een gesuggereerde "extra korting op de grondprijsopslag voor CPO-projecten die in één keer veel grond afnemen" kon **niet met een geverifieerd citaat** worden bevestigd (een aanvankelijk gevonden CVDR-link bleek van een andere gemeente). **Lacunes:** exacte agrarische grondprijs 2026 en een eventuele CPO-korting — navraag via contact@zwolle.nl of Afdeling Vastgoed/Ontwikkeling (genoemd contactpersoon: i.de.vos@zwolle.nl).

### Actueel kavelaanbod (zelfbouw/PO)
- **Oude Mars** (zuidrand Zwolle): 100 kavels totaal opgezet, op raadpleegdatum 1 kavel beschikbaar (1.101 m², € 560.000 k.k.).
- **Weideburen/De Tippe:** 10 kavels geschakelde woningen.
- **Mastenveld/De Tippe:** 13 kavels (7 vrijstaand, 6 twee-onder-een-kap), 309-592 m², € 180.000-€ 382.000 v.o.n.
- **De Plantage (Breecamp-Oost):** vrije-sectorkavels.
Contact: team Kopersbegeleiding, 038-498 2200, ikbouwmijndroomhuisin@zwolle.nl.

### Grote ontwikkellocaties met gemeentelijke grondpositie/regie
| Locatie | Aantal woningen (indicatief) | Status/bouwstart | CPO-relevantie |
|---|---|---|---|
| Nieuwe Veemarkt (Kamperpoort) | ~750, waarvan 50% betaalbaar | Selectiefase 2026, bouwstart vanaf 2028 | Bevat expliciet CPO/collectief-wonenveld (~30 woningen) |
| Stadshagen/De Tippe/Breezicht/Breecamp West | ~1.300 (De Tippe alleen) | Lopend | Diverse collectieve projecten (Groeneburenhof e.a.) |
| Vechtrand (Vechtpoort 1/2, Ceintuurbaanzone) | 1.500-3.000 | Onderzoeksfase, voorkeursrecht gevestigd | Grotendeels agrarisch, maar gemeente-geregisseerd, geen CPO-reservering bekend |
| Zwolle-Zuid (nieuw stadsdeel) | 2.000-3.000 + 250-500 | Onderzoeksfase | Geen CPO-reservering bekend |

### Plancapaciteit, woondeal en bouwtempo
De **Actualisatie Woondeal West-Overijssel 2025 t/m eind 2030** (25-03-2025) geeft de meest concrete regionale cijfers: regionale plancapaciteit **38.787 woningen** (19.044 hard, 19.743 zacht) tegenover een ambitie van minimaal 28.200 woningen tot 2030. Zwolle's aandeel in de "sleutelprojecten": **7 projecten, 9.000 woningen** op een regionaal totaal van 24.210 (**~37%** van alle sleutelproject-woningen in West-Overijssel):

| Sleutelproject | Woondeal 2022 | 2024-2030 | Doorkijk na 2030 |
|---|---|---|---|
| Zwolle Spoorzone | 3.000 | 1.000 | 1.400 |
| Zwolle Stadshart | 2.000 | 1.400 | 800 |
| Zwolle Nieuwe Veemarkt/Meeuwenlaan | 1.400 | 1.200 | 200 |
| Zwolle Zwartewaterallee/-zone | 1.600 | 500 | 200 |
| Zwolle Oosterenk | 1.000 | 500 | 300 |
| Zwolle uitbreiding Stadshagen | 3.000 | 3.100 | - |
| Zwolle stedelijke verdichting (nieuw) | - | 1.300 | 100 |
| **Totaal Zwolle** | **12.000** | **9.000** | **3.000** |

> **⚠️ Cruciale bevinding:** in de volledige Woondeal-tekst (27 pagina's, doorzocht op trefwoorden) komen "CPO", "particulier opdrachtgeverschap", "zelfbouw", "KGO", "erftransformatie" en "VAB" **geen enkele keer** voor. Alle acht Zwolse sleutelprojecten zijn stedelijke locaties. **Een CPO op agrarische grond in het buitengebied valt volledig buiten de formele, aan het Rijk gerapporteerde woondeal-boekhouding van Zwolle** — geen concurrentie om dat budget, maar ook geen formele regionale/provinciale prioritering.

**Aanvulling uit `provincie_overijssel.md` §1.5 (stand 2026-10-02), voor Zwolle:**
- Woondeal West-Overijssel 2025-2030 gedateerd 20 maart 2025 (bestandsnaam 25-03-2025). Zwolle: **1.615 woningen netto gerealiseerd Q1 2022 – Q4 2024**; 7 sleutelprojecten/9.000 woningen 2024-2030; doorkijk 2031-2035: 3.000. Regio West-Overijssel: opgave ≥ 28.200; plancapaciteit 38.787 (19.044 hard, 19.743 zacht); regionaal streven 130% plancapaciteit. Zwolse harde/zachte plancapaciteit: alleen de coalitie noemt **ca. 7.000 woningen in zachte plannen** (coalitieakkoord 2026-2030, p. 21); de harde capaciteit en de verhouding tot de behoefte zijn **niet gevonden** (zie lacunes).
- **Sleutelprojecten zijn (geclusterde) projecten van minimaal 50 woningen**; een CPO van 10-12 woningen telt daar alleen in mee als het wordt geclusterd of via overige plancapaciteit loopt (*interpretatie*). Of een Zwolse CPO/VAB-locatie in de provinciale Planmonitor Wonen als harde of zachte plancapaciteit staat, is niet onderzocht.
- **Art. 4.14-4.15:** nieuwe woningen moeten passen binnen de geldende woonafspraken; omgevingsplannen leggen **bij voorkeur** maximaal 80% van de behoefte vast, zodat 20% beschikbaar blijft voor niet-voorziene initiatieven (genoemd: o.a. inbreidingslocaties na sloop). Afwijking vergt instemming van regiogemeenten én GS. Voor Zwolle (de regio's dominante bouwer) is niet onderzocht hoeveel van die 20% is benut en of buitengebied-/VAB-woningen meetellen. De Woondeal noemt CPO, zelfbouw en kwantitatieve VAB-opgaven niet.
- Overijssel-breed zijn in 2024 5.443 en in 2025 5.747 woningen gerealiseerd (regionaal-provinciaal, geen Zwolse cijfers); Zwolle zelf: 2025 ca. 749 opgeleverd, zie hierboven.

**Bouwtempo:** 2024 werd door lokale media een "zwartjaar" genoemd; 2025: ca. 1.000 vergunningen, 749 woningen opgeleverd (vnl. Breezicht-Noord/De Tippe); 2026 verwacht ca. 800 opleveringen, oplopend naar 873 in 2027. De gemeente experimenteert vanaf 2026 met "parallelle planvorming" (2 pilots) om doorlooptijden te verkorten. Bron: coalitieakkoord 2026-2030 (§10); Actualisatie Woondeal West-Overijssel (https://overijsselsewoonaanpak.nl/media/xhadtdva/20250325_524100_woondeal-west-overijssel-digitaal-toegankelijk.pdf, 21-08-2026); diverse RTV Focus-berichten.

---

## 6. Praktijkvoorbeelden (2024-2026)

| # | Voorbeeld | Datum | Bron | Relevantie voor CPO 10-12 won. op agrarische grond |
|---|---|---|---|---|
| 1 | **Pilot erfontwikkeling Zalkerdijk 26a / Buitengoed Veecaten** — 3 wooneenheden op voormalig agrarisch erf, collectief beheer via VvE | sept. 2024 – apr. 2025 | Raadsbrief 15-4-2025, zwolle.bestuurlijkeinformatie.nl | **Zeer hoog** — beste precedent, maar expliciet niet-precedentscheppend verklaard |
| 2 | **Erfgenamenweg Wijthmen** — 32 wooneenheden wonen+zorg, coöperatieve zorgboerderij op 20 ha agrarische grond | vanaf 2026, in voorbereiding | RTV Focus, 01-02-2026 | Hoog — vergelijkbare schaal en transformatie-aard, geeft doorlooptijdindicatie |
| 3 | **Rood-voor-rood Windesheim** — sloop agrarische bebouwing, 2 nieuwe woningen | doorlopend | bestemmingsplan Buitengebied Landgoed Windesheim | Matig — kleine schaal, wel directe rood-voor-rood-precedentwerking |
| 4 | **Groeneburenhof** — CPO, max. 15 koopappartementen | bouw gereed voorjaar 2026 | groeneburenhof.nl, RTV Focus | Matig — CPO-proceservaring, maar stedelijke locatie (De Tippe) |
| 5 | **Veecatenhof** (2e Knarrenhof Zwolle) — 51 woningen (19 koop/32 sociale-middenhuur) | eerste bewoners april 2026 | RTV Focus | Matig — samenwerkingsvorm collectief-corporatie-gemeente, stedelijk |
| 6 | **Klein Wonen De Tippe** — kleine energieneutrale woningen rond gedeelde tuin | bouw gestart mrt. 2025, oplevering Q1 2026 | zwolle.nieuws.nl | Matig — CPO-achtig proces, stedelijk |
| 7 | **Nieuwe Veemarkt collectief wonen** (incl. "CPO Samen Groen Wonen") | aanmeldfase afgerond dec. 2025, selectiefase 2026 | zwolle.nl | Hoog qua proces/beleidscommitment, stedelijk van locatie |
| 8 | **Vechtrand/Nieuw Zuthem** — onderzoek nieuwe woongebieden op grotendeels agrarische grond | 2025-2026, onderzoeksfase | zwolle.nl/vechtrand | Context — toont dat grootschalige agrarisch-naar-woon-omzetting wél gebeurt, maar gemeente-geregisseerd |
| 9 | **Coalitieakkoord 2026-2030** "Bouwen op Zwolse kracht" — ambitie 4.400 woningen | gepresenteerd 25-06-2026 | zie §10 | Politieke context |
| 10 | **CDA-vragen stikstofplannen** — waarschuwing voor toenemende ruimtedruk buitengebied (woningbouw vs. landbouw vs. natuur) | 15-07-2026 | 1Zwolle/De Swollenaer | Signaal van toenemende politieke aandacht voor het spanningsveld |

**Kernconclusie:** Zwolle's actieve CPO/collectieve-woonprojecten spelen zich vrijwel volledig af in de **stedelijke uitbreidingswijk De Tippe/Stadshagen**, niet in het buitengebied. **Er is geen zuiver precedent gevonden van een CPO van ~10-12 reguliere woningen op agrarische grond in het Zwolse buitengebied** — dit is zowel een risico (geen direct beroepbaar precedent) als een kans (geen concurrerend initiatief, ruimte voor een eigen profiel).

---

## 7. Inventarisatie bestaande initiatieven

| Initiatief | Aantal woningen | Locatie | Status | Relevantie |
|---|---|---|---|---|
| CPO Samen Groen Wonen in Zwolle | ~25 huishoudens | Nieuwe Veemarkt (stedelijk) | Selectiefase 2026 | Enige met "CPO" in de naam; niet buitengebied |
| Stadserf Zwolle | 30-35 | Nieuwe Veemarkt | Aanmeldfase afgerond | Stedelijk |
| De Makershof | klein, oriënterend | Nieuwe Veemarkt | Aanmeldfase afgerond | Stedelijk |
| Knarrenhof (5e vestiging, Nieuwe Veemarkt) | onbekend | Nieuwe Veemarkt | Aanmeldfase afgerond | Stedelijk |
| Samen wonen, samen leven, samen zorgen | onbekend | Nieuwe Veemarkt | Aanmeldfase afgerond | Stedelijk, ouderen |
| Groeneburenhof | max. 15 | De Tippe | Bouw gereed voorjaar 2026 | Stedelijk |
| Veecatenhof (2e Knarrenhof) | 51 (19 koop/32 huur) | De Tippe | Eerste bewoners apr. 2026 | Stedelijk |
| Klein Wonen De Tippe | klein | De Tippe | Oplevering Q1 2026 | Stedelijk |
| Zalkerdijk 26a/Buitengoed Veecaten | 3 | Buitengebied (grens Kampen) | Pilot afgerond, vervolg in voorbereiding | **Enige buitengebied-precedent** |
| De Buitenmeent | onbekend (8 initiatiefnemers) | Buitengebied Zwolle | Status onduidelijk | Buitengebied, maar schaal/fase onbevestigd |

**Lacune:** de omvang en vergunningsfase van **De Buitenmeent** (initiatief van 8 personen, expliciet gericht op "anders wonen" in het buitengebied) kon niet worden vastgesteld. **Aanbeveling:** rechtstreeks contact via https://www.debuitenmeent.nl/.

---

## 8. Huisvestingsverordening

**Aanwezig: NEE** (met één zeer beperkte uitzondering). Dit is de dominante, drievoudig onderbouwde conclusie:

- De **Huisvestingsverordening 1996** (CVDR32779) is vervallen (laatst geldig t/m 06/24-12-2013) en **niet vervangen** door een algemene opvolger.
- De enige nog geldende regeling met "Huisvestingsverordening" in de naam is de **Huisvestingsverordening voor standplaatsen van woonwagens** (CVDR31503, geldend vanaf 16-12-1999), die uitsluitend woonwagenstandplaatsen regelt — niet relevant voor een CPO-woningbouwproject.
- Bevestigd door een officiële informatienota aan de raad (13-10-2021, portefeuillehouder Ed Anker), integraal geciteerd: *"Zwolle heeft op dit moment geen huisvestingsverordening in tegenstelling tot de grote steden zoals Amsterdam en Den Haag […]. Bij invoering van de Woningwet heeft Zwolle ervoor gekozen om geen Huisvestingsverordening te maken, omdat we al heldere afspraken hebben met de corporaties omtrent de Woonruimteverdeling in de Woningzoeker. Daarnaast hebben we de beleidsregel Klein wonen ingevoerd omtrent splitsing."*
- Een systematische CVDR-doorzoeking van alle 44 Zwolse regelingen onder "Volkshuisvesting en woningbouw" (21-08-2026) bevestigde: geen nieuwere huisvestingsverordening aangetroffen.

> **✅ Eerder tegenstrijdige bevinding — opgelost (verificatieronde 2026-10-02):** het nieuws-deelonderzoek trof een verwijzing aan naar een "Huisvestingsverordening 2025 (CVDR739354)". Directe controle van https://lokaleregelgeving.overheid.nl/CVDR739354 toont dat dit de **Huisvestingsverordening 2025 van gemeente Groningen** is (vastgesteld 26-3-2025), niet van Zwolle. De conclusie "Zwolle heeft geen algemene huisvestingsverordening" blijft dus staan.
>
> **Wel nieuw:** de **Scenarionota "Bouwstenen Huisvestingsverordening Zwolle"** (1-7-2024, portefeuillehouder Dorrit de Jong; https://zwolle.bestuurlijkeinformatie.nl/Document/View/009dd196-e242-4677-ad8b-fb63a6a28aba) bevestigt dat Zwolle sinds 2023 een verordening **uitwerkt** (verkenningsfase; scenario's 1-3 voor de bouwstenen woonruimteverdeling, woningvoorraadbeheer, opkoopbescherming van bestaande koopwoningen tot € 390.000 [prijspeil 2024] en andere). Citaat: *"Op basis van het wetsvoorstel Wet versterking regie volkshuisvesting wordt de bouwsteen 'urgentieregels' in ieder geval verplicht."* Regionale afstemming in West-Overijssel is vereist. Het eindresultaat (vastgestelde verordening) is **niet gevonden**; de scenarionota gaat over bestaande koopwoningen en woonruimteverdeling en heeft daardoor geen aanwijsbare invloed op nieuwbouw-CPO in het buitengebied.

**Minimumpercentage sociale huur** loopt in Zwolle dus niet via een huisvestingsverordening maar via het generieke woonbeleid. Integraal geciteerd uit "dwoon Zwolle — Uitgangspunten sociale huurwoningen":

> "Uitgangspunt is minimaal **20% sociale huur**. Minimaal 50% van de te realiseren sociale huurwoningen betreft huurwoningen onder de hoogste aftoppingsgrens. Woningen blijven minimaal **25 jaar** in de categorie sociale huur […]. Van de 30% (goedkoop), dient 2/3 minimaal sociale huur te zijn, zoals vastgelegd in de **Betaalbaarheidsagenda 2022**. […] De drie Zwolse corporaties (deltaWonen, SWZ, Openbaar Belang) zijn preferent partner bij gebiedsontwikkelingen groter dan 30 woningen."

*Verificatieronde 2026-10-02:* de raadsbrief "Beleidsupdate Wonen" (16-12-2025) bevestigt dat in nieuwbouwprojecten een **prestatieafspraak over "20% sociale huurwoningen"** met de corporaties geldt; de studentenhuisvesting telt daar niet voor mee. De datering van de "dwoon"-uitgangspunten blijft onbekend, maar het 20%-uitgangspunt is daarmee recent bevestigd. Het coalitieakkoord 2026-2030 handhaaft de 30-40-30-verdeling "met 50% betaalbaarheid" en wil die per wijk toepassen.

Dit 20%-minimum geldt in beginsel ook voor een CPO van 10-12 woningen; de "corporaties-preferent"-bepaling (>30 woningen) is niet direct van toepassing — mogelijk ruimte voor maatwerk bij een kleinere CPO.

**Landelijke ontwikkeling (provincie_overijssel.md §5):** onder de Wet versterking regie volkshuisvesting (in werking 1-7-2026) volgt een huisvestingsverordening volgens de primaire bron uiterlijk **1 januari 2028**; gemeentelijke volkshuisvestingsprogramma's volgen uiterlijk 1 juli 2027 (andere bronnen noemen andere data). Dit kan de Zwolse keuze om geen algemene verordening te hebben (informatienota 2021) op termijn herzien — niet onderzocht.

**Overige bevestigde, wél bestaande regelgeving:** Verordening Middenhuurwoningen Zwolle 2022 (CVDR679530, vastgesteld 13-06-2022, middenhuurgrens 2025: € 1.184,82/maand); Beleidsregel zelfstandige/onzelfstandige woonruimte (vanaf 07-05-2025); Beleidsregel studentenhuisvesting Zwolle 2025; Beleidsregel Wet goed verhuurderschap (vanaf 25-07-2025).

---

## 9. Zelfbouwloket / contactpersoon

Geen formeel apart "zelfbouwloket" als zodanig benoemd, maar wel functionele contactpunten:
- **Team Kopersbegeleiding** (reguliere zelfbouw-/PO-kavels): 038-498 2200, ikbouwmijndroomhuisin@zwolle.nl.
- **Team Nieuwe Ruimtelijke Initiatieven** (initiatieven buiten reguliere kavelverkoop, zoals een CPO op agrarische grond): ruimtelijkeinitiatieven@zwolle.nl.
- **Projectteam Nieuwe Veemarkt** (collectieve woonvormen specifiek): veemarkt@zwolle.nl.
- Beleidskaders Ruimtelijk ontwikkelplan: E. Boogmans (e.boogmans@zwolle.nl); algemeen: F. van Dijk (f.van.dijk@zwolle.nl).

**Lacune:** geen individuele naam/functie van een medewerker (anders dan teamnamen) op publieke pagina's gevonden.

---

## 10. Bestuurlijk klimaat

### Verkiezingen en coalitievorming (maart-juni 2026) — recent afgerond, geen lopende formatie meer
Gemeenteraadsverkiezingen: **18 maart 2026** (opkomst 62,25%, +7 procentpunt t.o.v. 2022; 39 zetels).

**Zetelverdeling na de verkiezingen:**

| Partij | Zetels 2022 | Zetels 2026 |
|---|---|---|
| PRO (Progressief Zwolle, GroenLinks+PvdA) | — | 8 |
| Swollwacht | 3 | 8 (na verkiezingen; zie hieronder) |
| VVD | 5 | 5 |
| ChristenUnie | 7 | 4 |
| D66 | 4 | 4 |
| CDA | 4 | 3 |
| Stadspartij Zwolle | — (nieuw) | 2 |
| Forum voor Democratie | — (nieuw) | 2 |
| SP | 2 | 1 |
| Partij voor de Dieren | 2 | 1 |
| Volt | 1 | 1 |

**Verloop van de formatie:** Swollwacht won spectaculair (3→8 zetels) en nam initieel het voortouw; verkenners adviseerden op 13-04-2026 een coalitie Swollwacht-VVD-ChristenUnie-D66 te onderzoeken. Op **20-04-2026** ontstond een vertrouwensbreuk binnen Swollwacht: raadslid Evelina Bijleveld (dochter van fractievoorzitter Bruggenkamp) verliet de fractie, Swollwacht zakte naar 7 zetels en verloor de status van grootste partij, en trok zich terug uit het voortouw. **PRO** nam het over; nieuwe verkenner **Jeroen Recourt** adviseerde op 8 mei 2026 een coalitie van **PRO, VVD, D66, ChristenUnie en CDA** (met uitsluiting van Swollwacht na 4,5 uur vastgelopen onderhandelen over participatie, mobiliteit en AZC De Tippe) als "de meest stabiele en breed gedragen basis". Kritiek van SP, Stadspartij Zwolle en FvD op dit advies (o.a. "verliezerscoalitie"-framing, omdat geen van de vijf coalitiepartijen zetels won).

**Coalitieakkoord "Bouwen op Zwolse kracht: blik op de toekomst, oog voor vandaag"** gepresenteerd **25 juni 2026**, besproken in de raad **29 juni 2026**. **De coalitievorming is dus afgerond**, geen lopend formatieproces meer op raadpleegdatum (21-08-2026; bij de verificatieronde van 2026-10-02 is geen aanwijzing gevonden voor een nieuwe coalitiecrisis, maar dit is niet gericht in nieuwsberichten van na 21-08-2026 gecontroleerd). De akkoordtekst noemt een bestuursstijl met "ruimte voor verschillende opvattingen en wisselende meerderheden". Ondertekenend namens de fracties: PRO (Luna Koops), ChristenUnie (Klariska ten Napel), CDA (Laura van de Giessen), VVD (Johran Willegers), D66 (Marco van Driel). De vijf coalitiepartijen hebben samen 24 van de 39 zetels; Swollwacht (7-8 zetels) zit in de **oppositie**.

### College van B&W
- **Burgemeester:** Peter Snijders.
- **Anja Roelfs (PRO) — Wonen**, plus Wmo, wonen-en-zorg, beschermd wonen, maatschappelijke opvang, cultuur, natuur, groen, dierenwelzijn, AZC De Tippe.
- **Tjitske Siderius (PRO)** — sociaal domein (jeugd, armoede, welzijn, wijkteams, onderwijs).
- **Johran Willegers (VVD)** — mobiliteit, bereikbaarheid, parkeren, economische zaken, bedrijventerreinen, **vastgoed en grondbeleid**, Agenda Regio Zwolle (spelling "Willegers" volgens het coalitieakkoord; in eerdere bronnen ook "Willigers"; VVD keerde met deze wethouder terug in het college).
- **Gerdien Rots (ChristenUnie) — Ruimtelijke Ordening en buitengebied; Omgevingswet en omgevingsvisie** (verder o.a. inwonerbetrokkenheid, maatschappelijke voorzieningen, water en klimaatadaptatie, zie §2). Portefeuillelijst volgens het coalitieakkoord (p. 5, 2026-10-02).
- **Paul Guldemond (D66)** — financiën, werk en inkomen, innovatie, digitalisering.
- **Arjan Spaans (CDA)** — asielopvang, nieuwkomers, energie, sport.

**Voor het CPO-dossier het meest relevant: Anja Roelfs (Wonen) en Gerdien Rots (Ruimtelijke Ontwikkeling/Omgevingsvisie).**

### Coalitieakkoord — relevante passages
> "De behoefte aan woningen blijft groot. Daarom krijgt de woningbouw de komende jaren een extra impuls. **De ambitie is om de woningbouwopgave deze bestuursperiode te verhogen naar minimaal 4.400 woningen** en de bestaande zachte plancapaciteit versneld om te zetten naar harde plannen. Ook wil de coalitie versneld werken aan een nieuwe uitbreidingslocatie om ook op langere termijn voldoende woningen te kunnen realiseren."

Overige speerpunten: verdeling 30% betaalbaar/40% middensegment/30% duur; **Vechtrand** krijgt prioriteit voor versnelde ontwikkeling; 400 betaalbare woningen voor jongeren; versoepeling/versnelling van bouwregelgeving; uitbreiding ouderenhuisvesting.

> **✅ Lacune ingevuld (verificatieronde 2026-10-02):** het volledige coalitieakkoord-PDF (https://media.d66.nl/uploads/sites/78/2026/06/Coalitieakkoord-Zwolle-2026-2030-Bouwen-op-Zwolse-kracht.pdf, 5,6 MB) is lokaal geëxtraheerd en doorzocht. **Geen enkele vermelding** van "CPO", "collectief particulier opdrachtgeverschap", "zelfbouw", "kavel(s)", "Knarrenhof" of "coöperatief wonen" als woonvorm. **Wél relevante passages (integraal, p. 20-22):**
>
> - *"Zwolle is meer dan de stad alleen. In het buitengebied werken we samen met onze inwoners, agrariërs en ondernemers. Onze dorpen, buurtschappen zoals Wijthmen, Windesheim en Herfte, en het buitengebied zijn een onmisbaar onderdeel van Zwolle."*
> - *"Samen met partners actualiseren we het beleid Kwaliteitsimpuls Groene Omgeving (KGO), zodat er meer ruimte ontstaat voor passende ontwikkelingen op erven en in het buitengebied."*
> - *"Daarvoor gaan we de huidige 7000 woningen in zachte plannen versneld omzetten naar harde plancapaciteit. [...] Om tegemoet te komen aan de brede woonwens van onze inwoners gaan we versneld een nieuwe uitbreidingslocatie uitwerken."*
> - *"Voor de uitbreidingswijken Vechtrand en Nieuw Zuthem maken we gebiedsvisies om een complete omgevingsvisie vast te stellen. Daarbij zetten we in op versnelde uitvoering van een van beide locaties, bij voorkeur Vechtrand [...] (1.500–3.000 woningen in Vechtrand)."*
> - *"We combineren in Stadsbroek landschapsontwikkeling met zorgvuldig ingepaste woningbouw [...] dit gebied leent zich niet voor grootschalige woningbouw."*
> - *"De verdeling goedkoop–middelduur–duur (30-40-30) met 50% betaalbaarheid blijft daarbij leidend"* en wordt per wijk toegepast; *"We stimuleren levensloopbestendige woonvormen, waar wonen en zorg worden gecombineerd"*; *"We evalueren de Zwolse routekaart voor gebieds- en locatieontwikkelingen"*; vermindering van "lokale koppen" en parallel plannen voor snelheid.
>
> Conclusie: de coalitie **noemt CPO/zelfbouw niet**, maar heeft **expliciet de intentie het KGO-beleid te verruimen voor erven en het buitengebied** (zonder termijn of schaal) en wil zorgvuldigheid naar "schaal, identiteit en leefkwaliteit". Dit is het sterkste bestuurlijke signaal voor het buitengebied-spoor.

### Politieke duiding voor CPO
**PRO** (opvolger van GroenLinks/PvdA, van oudsher affiniteit met duurzame/collectieve woonvormen) heeft nu zowel de grootste coalitiefractie als de wethouder Wonen — in beginsel gunstig voor CPO-achtige initiatieven, al is CPO in het akkoord zelf niet genoemd (bevestigd door het integraal doorzoeken van de akkoordtekst). **ChristenUnie** blijft aan tafel (was grootste coalitiepartner 2022-2026, nu gehalveerd), wat continuïteit geeft op het woondossier — relevant omdat wethouder Rots (Ruimtelijke Ontwikkeling) zowel in de vorige als de huidige coalitie zit en het Zalkerdijk-precedent onder haar portefeuille tot stand kwam. De coalitie is breed en middenveld-georiënteerd, met focus op tempoversnelling en schaal (grote uitbreidingslocaties) — dit kan betekenen dat kleinschalige buitengebied-initiatieven minder prioriteit krijgen dan grote projecten, al biedt de voortzetting van het Nieuwe Veemarkt-beleid (collectief wonen) een gunstig precedent voor CPO als instrument. **Swollwacht** (oppositie, lokale partij) profileert zich op andere thema's (participatie, mobiliteit, AZC) — standpunt over buitengebied-CPO niet gevonden.

---

## 11. Kostenverhaal en leges

**Legesverordening Zwolle 2026** (CVDR751052, vastgesteld door de raad 15-12-2025, in werking 1-1-2026):

**Art. 2.45 — Omgevingsplanwijziging:**
- Met bouwactiviteit: **€ 22.635,00**
- Zonder bouwactiviteit: **€ 22.129,00**

**Art. 2.6.3 — Buitenplanse omgevingsplanactiviteit (BOPA) gecombineerd met bouwactiviteit, naar bouwkosten:**
| Bouwkosten | Leges |
|---|---|
| < € 250.000 | € 543,00 |
| € 250.000 – € 500.000 | € 1.631,00 |
| € 500.000 – € 750.000 | € 5.439,00 |
| € 750.000 – € 1.000.000 | € 10.880,00 |
| € 1.000.000 – € 2.000.000 | € 20.672,00 |
| ≥ € 2.000.000 | € 30.464,00 |

**Art. 2.6A.4 — BOPA zonder bouwactiviteit (gebruikswijziging), naar oppervlakte:** < 1.500 m²: € 575,00; 1.500-5.000 m²: € 11.543,00; ≥ 5.000 m²: € 21.932,00.

**Art. 2.6.1.1 — reguliere omgevingsvergunning bouwactiviteit (binnenplans), naar bouwkosten:** vanaf € 328,00 + 2,59% (tot € 225.000) via € 5.807,00 + 2,09% (€ 225.000-1.000.000) tot € 21.152,00 + 1,97% boven € 1.000.000 (max. € 652.800,00).

**Indicatie voor een CPO-project van 10-12 woningen op agrarische grond:** bij bouwkosten voor het geheel > € 2 miljoen (zeer waarschijnlijk bij deze schaal) resulteert de BOPA-route (art. 2.6.3) in **minimaal € 30.464,00**, of — indien via een volledige omgevingsplanwijziging (art. 2.45) — **€ 22.635,00**, telkens **plus** de reguliere bouwleges (art. 2.6.1.1, potentieel enkele tienduizenden euro's extra) en eventuele separate plankosten.

**Kostenverhaal (exploitatiebijdrage/anterieure overeenkomst):** **geen aparte Zwolse beleidsregel gevonden** voor kostenverhaal, plankosten of anterieure overeenkomsten (systematische CVDR-zoekactie: 0 Zwolse treffers; treffers die kansrijk leken bleken van Zaltbommel of Houten). Kostenverhaal is wettelijk sowieso verplicht bij een omgevingsplanwijziging/BOPA (publiekrechtelijk via het omgevingsplan, privaatrechtelijk via een anterieure overeenkomst) en wordt in Zwolle vermoedelijk per project maatwerk-gewijs geregeld door Afdeling Vastgoed, zonder gepubliceerde algemene beleidsregel. **Concreet precedent:** bij Zalkerdijk 26a betaalde de initiatiefnemer € 7.500 als NRI-projectbijdrage tijdens de pilotfase; voor het vervolg gelden de "reguliere financiële en procedurele afspraken".

**Lacune:** een actuele, als raadsbesluit vastgestelde "Nota Grondbeleid" (opvolger van de vervallen 2005-nota, CVDR34931) is niet gevonden. **Navragen bij:** Afdeling Vastgoed/Ontwikkeling gemeente Zwolle.

---

## 12. Woningbehoefte en doelgroepen

### Doelgroepenbeleid
> "We zetten ons in om met name **jongeren en kenniswerkers** te behouden voor onze stad. […] ouderen die nu langer zelfstandig blijven wonen […] willen wel de passende voorzieningen."

### Cijfermatige onderbouwing
Uit een RIGO-onderzoek in opdracht van de gemeente ("De woningmarkt van Zwolle — Quick scan prijsdifferentiatie", 2 februari **2022** — geen recentere volledige update gevonden): bewoonde woningvoorraad (2021) ca. 57.850 woningen (44% goedkoop/32% middelduur/25% duur); 43% van de huishoudens onder de EU-doelgroepgrens sociale huur; huishoudensgroei volgens Primos-prognose van 60.800 (2021) naar 65.900 (2030); scheve verhouding aanbod/vraag in het middensegment (75% van koopaanbod duurder dan € 340.000). Actuelere signalen (2026): wachttijden voor sociale huur van **7-10 jaar** (bron: lokale nieuwsmedia); woningmarkt door bewoners als "vastgelopen" ervaren, vooral voor starters/jonge gezinnen/middeninkomens.

> **✅ Eerder tegenstrijdige bevinding — opgelost (verificatieronde 2026-10-02):** het nieuws-deelonderzoek verwees naar een "Woonvisie 2025-2030 — Het begint met wonen" (CVDR729056). Directe controle van https://lokaleregelgeving.overheid.nl/CVDR729056 toont dat dit de woonvisie van **gemeente Gooise Meren** is (geldend vanaf 1-1-2025), niet van Zwolle. Zwolle heeft dus **geen** als raadsbesluit vastgestelde "Woonvisie 2025-2030" gevonden, in lijn met de bevinding van het registers-deelonderzoek.
>
> **Wat Zwolle wél heeft (raadsbrief "Beleidsupdate Wonen", 16-12-2025, portefeuillehouder toen Dorrit de Jong; https://zwolle.bestuurlijkeinformatie.nl/Document/View/d8b52ba3-fcae-4c51-a879-f282118c70ef):** ambitie van **9.000 extra woningen tot en met 2030**; een **woningbehoefteonderzoek** (basis: Primos-prognose 2024; vertaalt kwantitatieve naar kwalitatieve behoefte per doelgroep, woningtype en prijssegment, met aandachts- en urgentiegroepen en inzichten per stadsdeel/wijk, o.a. geschikte locaties voor ouderenhuisvesting en potentie voor woningsplitsen) dat als bijlage bij de raadsbrief aan de raad is verstrekt (de bijlage zelf is niet gelezen); een **Volkshuisvestingsprogramma** (oplevering gepland Q3 2026; zie §2) dat de woonvisie vervangt; het "Zwols Actieplan Wonen"; en beleid voor studentenhuisvesting (beleidsregel: 500-650 woonplekken tot en met 2035) en "Beter benutten van de bestaande woningvoorraad". Een zoekresultaat (Binnenlands Bestuur, niet zelf geopend) noemt voor 65-plussers een groei van ca. 22.000 (2020) naar bijna 31.500 (2040) en een behoefte aan particuliere huur en koop naast sociale huur. Het onderzoek 2022 (RIGO) hierboven is daarmee **achterhaald als meest recente analyse**; de cijfers van het woningbehoefteonderzoek 2025 en een mogelijke buitengebied-/CPO-uitsplitsing zijn niet gevonden.

### Aansluiting CPO op buitengebied
Geen gemeentelijk document gevonden dat de woningbehoefteanalyse expliciet koppelt aan CPO of aan het buitengebied specifiek. Het "onderzoek naar interesse in collectief wonen" (2023, aanleiding voor het Nieuwe Veemarkt-initiatief) is stedelijk gepositioneerd, niet buitengebied-specifiek. **Lacune:** geen actuele (2024-2026) woningbehoefte-analyse gevonden die specifiek ingaat op vraag naar collectieve/zelfbouw-woonvormen in het buitengebied.

**Doorvertaling van het regionale/provinciale kader (provincie_overijssel.md §1.5; Bijlage A, A3 en A5):**
- *Betaalbaarheid:* de Woondeal hanteert 30% sociale huur / 40% middenhuur + betaalbare koop / 30% vrij als basis; Zwolle gebruikt dezelfde 30-40-30-verdeling (ruimtelijke koers; coalitieakkoord) en het uitgangspunt van minimaal 20% sociale huur uit "dwoon Zwolle" (zie §8; de datering van dat stuk is niet vastgesteld, het verwijst naar de Betaalbaarheidsagenda 2022). Het is niet gevonden of deze percentages ook voor een CPO/zelfbouwproject van 10-12 woningen gelden of dat hiervoor maatwerk bestaat. De Zwolse middenhuurgrens 2025 (€ 1.184,82) komt overeen met de landelijke grens in de Woondeal; de landelijke koopgrens 2025 is € 405.000 (NHG). Kleine kernen met een aangescherpte koopgrens zijn in Zwolle niet aangetroffen. Prestatieafspraken met corporaties zijn niet gelezen.
- *Ouderen/zorg:* Zwolle noemt ouderen in het doelgroepenbeleid, het coalitieakkoord kondigt uitbreiding van ouderenhuisvesting aan en het Veecatenhof (Knarrenhof, 45+) toont dat geclusterd/collectief ouderenwonen in Zwolle wordt gefaciliteerd. De Zwolse doorvertaling van de West-Overijsselse woonzorgvisie en een lokale opgave voor geclusterde woonvormen zijn niet gevonden. De provinciale regeling *Langer zelfstandig wonen* (op 1-10-2026 aangevuld tot € 21 miljoen; aanvrager: gemeente of corporatie, geen particulier collectief) is alleen relevant bij een zorggeschikte/geclusterde seniorencomponent.

---

## Samenvattend overzicht van belangrijkste lacunes (voor de opdrachtgever)

| Onderwerp | Lacune | Waar wél te vinden |
|---|---|---|
| §2/§3 | Volledige tekst zwolle.nl-pagina's (vestigen-buitengebied, omgevingsvisie) niet automatisch op te halen (HTTP 403); coalitieakkoord-PDF is inmiddels wél gelezen | Handmatig via browser raadplegen |
| §3/§4 | Gebiedsspecifieke omgevingsplanregels agrarische herbestemming/VAB (bouwvlakken, wijzigingsbevoegdheden) | DSO/Omgevingsloket, ruimtelijkeplannen.nl/planviewer.nl, art.-voor-art. doorzoeken van Omgevingsplan CVDR696214 |
| §3 | Interne "Handreiking KGO gemeente Zwolle" niet publiek gevonden | Rechtstreeks opvragen bij afdeling Ruimtelijke Ontwikkeling (evt. Woo-verzoek) |
| §3 | Bijlagen Zalkerdijk 26a-dossier (eindrapportage, inrichtingsplan, brief provincie) niet apart doorzocht | zwolle.bestuurlijkeinformatie.nl |
| §4 | Gebruik provinciale VAB-transformatiesubsidie door Zwolle niet vastgesteld | vab@overijssel.nl, Overijssel Loket |
| §5 | Exacte agrarische grondprijs 2026; CPO-grondprijskorting onbevestigd; discrepantie erfpachtpercentage 2025 vs. 2026 | Volledige PDF Grondprijzenbrief 2026, contact@zwolle.nl |
| §5 | Actuele plancapaciteitscijfers (hard/zacht) specifiek Zwolle | Woonprogramma/woningbouwmonitor, navraag gemeente |
| §8 | Uitkomst van de Zwolse huisvestingsverordening-procedure (scenarionota 1-7-2024; vervolg/besluit niet gevonden) | zwolle.bestuurlijkeinformatie.nl (trefwoord huisvestingsverordening/opkoopbescherming) |
| §11 | Actuele Nota Grondbeleid/kostenverhaalbeleid kleine plannen | Afdeling Vastgoed/Ontwikkeling gemeente Zwolle |
| §12 | Inhoud woningbehoefteonderzoek 2025 (bijlage bij raadsbrief 16-12-2025) en opgeleverd Volkshuisvestingsprogramma (gepland Q3 2026) | zwolle.bestuurlijkeinformatie.nl, raadsbrief 16-12-2025 en volgende raadsstukken |
| §12 | Actuele (2024-2026) woningbehoefteanalyse buitengebied-specifiek | Navraag gemeente |
| §2 | Opgeleverd volkshuisvestingsprogramma; definitieve Omgevingsvisie; contour bestaand bebouwd gebied/stadsrand; actualisatie van het OF/WAAR/HOE-kader na 1-7-2026 | zwolle.bestuurlijkeinformatie.nl (trefwoord "volkshuisvestingsprogramma"), definitieve Omgevingsvisie, afdeling Ruimte en Economie |
| §3 | Landbouwgebied-type (kaartlaag art. 4.123) en overige provinciale overlays (NNN, grondwaterbescherming, stikstof) voor Zwolse buitengebied-deelgebieden | ruimtelijkeplannen.overijssel.nl/omgevingsvisie, omgevingswet.overheid.nl/regels-op-de-kaart |
| §3 | Provinciale accounthouder voor Zwolle, Zwolse BOPA-praktijk (Lijst BOPA), eventuele provinciale zienswijzen 2023-2026 | Gemeentelijke RO-afdeling; Overijssel Loket (038 499 88 99) |
| §5 | Zwolse harde/zachte plancapaciteit en positie van kleine projecten in de Planmonitor Wonen | Woningbouwmonitor Zwolle; provinciaal Dashboard Wonen |
| §12 | Lokale doorvertaling ouderen-/betaalbaarheidsafspraken voor kleine projecten | Prestatieafspraken met corporaties; Volkshuisvestingsprogramma |

---

## Twee kernvragen

*Beide vragen zijn gelaagd beantwoord: (a) wat het gemeentelijk beleid toestaat, (b) wat het provinciale kader van Overijssel daar bovenop vraagt of begrenst (zie `provincie_overijssel.md` en Bijlage A hieronder), en (c) het gecombineerde eindoordeel met de belangrijkste onzekerheden.*

### 1. Wonen in het buitengebied: biedt het gemeentelijk beleid ruimte voor een cluster van 10-12 woningen buiten de bestaande woonkernen?

**(a) Gemeentelijk beleid — voorwaardelijk ja, met aanzienlijke beperkingen.** Zwolle's ruimtelijke koers is uitgesproken stad-georiënteerd (binnenstedelijk en stadsrand voorop) en grootschalige groei is bewust gekanaliseerd naar gemeentelijk geregisseerde gebieden (Vechtrand, Nieuw Zuthem, Zwolle-Zuid; voorkeursrecht). Het Zwolse toetsingskader (OF/WAAR/HOE, mogelijk deels achterhaald na 1-7-2026) laat "onder voorwaarden" ruimte voor aanvullende woon- en werkmilieus op **(voormalige) agrarische erven** bij aantoonbare marktvraag en als de stedelijke omgeving geen ruimte biedt. Het Zalkerdijk 26a-precedent (3 wooneenheden, collectief erf) toont bereidheid om af te wijken van standaardbeleid, maar is expliciet niet-precedentscheppend verklaard. Een eigen CPO-beleid voor het buitengebied, een KGO-rekenformule en een VAB-beleidsregel ontbreken; het coalitieakkoord 2026-2030 noemt CPO niet, maar kondigt wél een **actualisatie van de KGO** aan "zodat er meer ruimte ontstaat voor passende ontwikkelingen op erven en in het buitengebied". Voor 10-12 woningen (≥ 5 in stedelijk gebied, > 5 in het buitengebied) geldt bovendien **bindend adviesrecht van de raad en verplichte participatie** (CVDR726092).

**(b) Provinciaal kader (Overijssel) — begrenst en stuurt.** Zwolle is "grote stad" (art. 4.4): de stedelijke opgave mag in en aansluitend aan de stad. Buiten de kern vraagt **art. 4.5 lid 2** dat eerst bestaande bebouwing en erven worden benut; nieuwe woningen vallen onder de **KGO (art. 4.11 lid 2 sub c)** en moeten passen binnen de **woonafspraken** (Woondeal West-Overijssel; art. 4.14-4.15, bij voorkeur max. 80% van de behoefte vastleggen) en de **redeneerlijn (art. 4.122)**, **water en bodem sturend (4.13)** en het **energiesysteem (4.125)**. Bij een **BOPA** is **provinciaal advies én instemming** vereist (Lijst BOPA), en de nieuwe instructieregels gelden direct (art. 4.2a). De Uitzonderingenlijst (≤ 11 woningen vrijgesteld van vooroverleg) geldt alleen in bestaand bebouwd gebied van kernen > 1.000 inwoners; 10-12 woningen ligt op die grens. De **landbouwgebied-typologie** (generiek: art. 4.124 lid 1; gebiedsspecifiek: KGO-investering gericht op klimaat/natuur/water) kan een locatie extra belemmeren; het type van een concrete Zwolse locatie is niet vastgesteld. De landelijke ladder vervalt naar verwachting per 1-1-2027 onder voorwaarde van een gemeentelijk volkshuisvestingsprogramma, maar de provinciale principes blijven gelden.

**(c) Eindoordeel en onzekerheden.** Het meest kansrijke pad is een cluster op een **bestaand (voormalig agrarisch) erf** of in/aansluitend aan de stadsrand, met sloopcompensatie en een landschappelijke kwaliteitsinvestering, vroeg afgestemd met team NRI én (voorkantsamenwerking) met de provincie. **Kansrijk-matig** op 10-12 woningen (schaal boven de Zwolse erfprecedenten van 2-7 woningen); **kansarm** op onbebouwde agrarische grond los van een erf of stadsrandlocatie. *Belangrijkste onzekerheden:* (1) de Zwolse "Handreiking KGO" en het aangekondigde nieuwe buitengebiedbeleid zijn niet gelezen/gepubliceerd; (2) of de gemeente een kandidaatlocatie als stadsrand (uitleg, art. 4.5 lid 1) of als Groene Omgeving (KGO) behandelt; (3) landbouwgebied-type en overige overlays van de locatie; (4) de werkelijke provinciale houding bij BOPA-instemming voor een project van deze schaal (geen Zwolse precedenten van instemming/onthouding gevonden); (5) timing en inhoud van de aangekondigde KGO-actualisatie (coalitieakkoord; geen termijn) en van het Volkshuisvestingsprogramma/de Omgevingsvisie (vertraagd; Q3 2026 gepland); (6) de eerder tegenstrijdige bevindingen over Huisvestingsverordening en Woonvisie zijn inmiddels opgelost (CVDR-nummers betroffen Groningen resp. Gooise Meren), maar de uitkomst van de Zwolse huisvestingsverordening-procedure en de inhoud van het woningbehoefteonderzoek 2025 zijn niet gevonden.

### 2. Agrarische herbestemming: biedt het gemeentelijk beleid ruimte voor de omzetting van agrarisch bestemde grond naar een bouw- of woonfunctie op deze schaal?

**(a) Gemeentelijk beleid — in principe ja, maar zonder vastgesteld toetsingskader.** Zwolle heeft, anders dan meerdere buurgemeenten, geen gepubliceerde KGO-rekenformule, rood-voor-rood-regeling of VAB-beleidsregel. Het college erkent in de raadsbrief van 15-4-2025 dat het buitengebiedbeleid nog moet worden geactualiseerd en dat erfontwikkeling per geval ("maatwerk"/"pilot") wordt beoordeeld aan de hand van de Omgevingsvisie, het provinciale KGO-kader en een niet-openbare interne Handreiking. De routes zijn omgevingsplanwijziging of BOPA via NRI (kleinschalig) of de Routekaart (grotere locatieontwikkeling). Zwolse voorbeelden: Windesheim (2 woningen, rood-voor-rood), Zalkerdijk 26a (3 wooneenheden), Kiekeboslaantje (max. 7 kavels) en Erfgenamenweg Wijthmen (32 zorgeenheden via gebiedsontwikkeling) — geen voorbeeld van 10-12 reguliere woningen.

**(b) Provinciaal kader (Overijssel) — extra eisen per 1 juli 2026.** Naast KGO, art. 4.5 lid 2, woonafspraken en Lijst BOPA (zie vraag 1) geldt voor **transformatie van (agrarische) bouwpercelen** art. 4.124: in generieke landbouwgebieden alleen nieuwe functies die de omliggende landbouw niet beperken (afwijking via lid 4 alleen met onderbouwde gebiedsvisie of als de landbouw feitelijk geen ontwikkelruimte meer heeft); in gebiedsspecifieke gebieden moet de KGO-investering natuur, water en klimaat dienen. De provinciale visie noemt "nee, tenzij" voor functieverandering in generieke landbouwgebieden, maar de verordening is smaller (*interpretatie*, provincie_overijssel.md §1.4): voor onbebouwde grond werkt de "nee, tenzij" vooral informeel. De provincie toonde bij Zalkerdijk wél een "positieve grondhouding" en een verruiming voor erfontwikkelingen in de stadsrandzone (vóór de Actualisatie 2026).

**(c) Eindoordeel en onzekerheden.** Haalbaar bij een goed onderbouwd plan op een bestaand erf met sloopcompensatie, collectieve/VvE-opzet en vroege, actieve afstemming met gemeente (team NRI; wethouders Roelfs en Rots), raad (bindend advies) én provincie (voorkantsamenwerking, BOPA-instemming); 3-6 woningen op een erf relatief kansrijk, 10-12 woningen op een erf matig kansrijk, 10-12 op onbebouwde grond kansarm. *Onzekerheden:* (1) geen Zwolse formule of Handreiking beschikbaar, dus de uitkomst van de "KGO-balans" is vooraf niet te berekenen; (2) het gemeentelijk precedentbeleid (pilot "geen precedent"); (3) het landbouwgebied-type en het effect van art. 4.124 op de beoogde locatie; (4) de **aangekondigde KGO-actualisatie** (coalitieakkoord 2026-2030: meer ruimte voor erven en buitengebied) en de mogelijke aanpassing aan de nieuwe Omgevingsvisie en Actualisatie 2026 (omgevingsplan uiterlijk 1-7-2029) — kan de kansen verbeteren, maar termijn en schaal zijn onbekend; (5) de politiek-bestuurlijke koers van de nieuwe coalitie (tempo/schaal in grote uitbreidingen; CPO is in het akkoord niet genoemd, het buitengebied wel); (6) of subsidie 4.39 of een Erfcoach een gemeentelijk beleidstraject kan versnellen (niet onderzocht).

---

## Overijssel-controlepunten (Bijlage A)

*Per punt: de bevinding uit dit onderzoek, de status (gevonden / niet gevonden / niet van toepassing / tegenstrijdig; "gedeeltelijk" = deels beantwoord), de bron (URL + raadplegingsdatum) en, bij "niet gevonden", waar het wel te vinden zou zijn. Zwolse bronnen: geraadpleegd 2026-08-21 (niet opnieuw geverifieerd); provinciale grondslag: `provincie_overijssel.md` (2026-10-02). Er is voor deze actualisatie geen nieuw webonderzoek uitgevoerd, dus punten zonder bron zijn bewust als "niet gevonden" gemarkeerd.*

### A. Positie in het provinciale kader en woonafspraken
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| A1 | Zwolle is "grote stad" (art. 4.4): lokale, regionale en bovenregionale behoefte mag. Groeiprofiel: NOVEX-regio/"klimaatadaptieve groeiregio Zwolle" (DSS Zwolle, verstedelijkingsstrategie "Warme harten in een klimaatadaptieve delta"). | Gevonden | provincie_overijssel.md §1.3; ontwerp-Omgevingsvisie bijlage "Gebiedseigen perspectieven" (https://www.overijssel.nl/media/xnehl1kg/ontwerp-omgevingsvisie-26052025.pdf, 2026-08-21) | — |
| A2 | Woonregio West-Overijssel; Woondeal 2025-2030 (20-3-2025). Zwolle: 1.615 gerealiseerd (Q1 2022–Q4 2024), 9.000 in sleutelprojecten, doorkijk 3.000; regio-plancapaciteit 38.787 (19.044 hard/19.743 zacht). 80%/20%-voorkeur. CPO van 10-12 woningen telt niet mee als sleutelproject (≥ 50). Zwolse harde/zachte plancapaciteit en Planmonitor-positie ontbreken; buitengebied-/VAB-woningen komen in de Woondeal niet voor. | Gedeeltelijk gevonden | https://overijsselsewoonaanpak.nl/media/xhadtdva/20250325_524100_woondeal-west-overijssel-digitaal-toegankelijk.pdf (2026-08-21) | Woningbouwmonitor Zwolle; provinciaal Dashboard Wonen/Planmonitor Wonen; 1-op-1-gesprekken provincie-gemeente-corporaties |
| A3 | Zwolle gebruikt 30-40-30 (zoals regionale basis; coalitieakkoord 2026: "met 50% betaalbaarheid", per wijk); minimaal 20% sociale huur in nieuwbouw (prestatieafspraak, bevestigd in raadsbrief 16-12-2025; dwoon-nota nog zonder datering); corporaties preferent bij > 30 woningen. Toepassing op CPO 10-12 woningen en lokale koopgrens: niet gevonden; kleine-kernen-grens niet van toepassing/niet aangetroffen. | Gedeeltelijk gevonden | https://www.zwolle.nl/de-ruimtelijke-koers-van-zwolle; "dwoon Zwolle — Uitgangspunten sociale huurwoningen" (zwolle.bestuurlijkeinformatie.nl, 2026-08-21) | Prestatieafspraken Zwolle-corporaties; Betaalbaarheidsagenda 2022; afdeling Wonen |
| A4 | Volkshuisvestingsprogramma in voorbereiding: oplevering gepland Q3 2026, raadsbevoegdheid, gebaseerd op woningbehoefteonderzoek; vertraging Omgevingsvisie. Of het is opgeleverd en buitengebied-/uitbreidingslocaties aanwijst: niet gevonden. Zwolse webtekst verwijst nog naar de "Overijsselse ladder" (vermoedelijk verouderd na 1-7-2026). | Gedeeltelijk gevonden | Raadsbrief Beleidsupdate Wonen 16-12-2025 (https://zwolle.bestuurlijkeinformatie.nl/Document/View/d8b52ba3-fcae-4c51-a879-f282118c70ef, 2026-10-02); https://www.zwolle.nl/vestigen-buitengebied (2026-08-21) | zwolle.bestuurlijkeinformatie.nl (trefwoord volkshuisvestingsprogramma); afdeling Ruimte en Economie |
| A5 | Ouderen/zorg: Veecatenhof (Knarrenhof, 45+, 51 woningen), uitbreiding ouderenhuisvesting en levensloopbestendige woonvormen in coalitieakkoord; woningbehoefteonderzoek 2025 bevat locatie-inzichten voor ouderenhuisvesting (inhoud niet gelezen). Lokale doorvertaling woonzorgvisie West-Overijssel en opgave geclusterd wonen: niet gevonden. Huisvestingsverordening: Zwolle heeft er (nog) geen; procedure loopt (scenarionota 1-7-2024; CVDR739354 = Groningen). *Langer zelfstandig wonen* alleen via gemeente/corporatie. | Gedeeltelijk gevonden | https://www.rtvfocuszwolle.nl/tweede-knarrenhof-van-zwolle-komt-in-de-tippe-en-gaat-veecatenhof-heten/ (2026-08-21); https://zwolle.bestuurlijkeinformatie.nl/Document/View/009dd196-e242-4677-ad8b-fb63a6a28aba (2026-10-02) | Woonzorgvisie West-Overijssel; woningbehoefteonderzoek 2025; afdeling Wonen |

### B. KGO, rood-voor-rood en rekenmodellen
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| B1 | Geen eigen gepubliceerd Zwols KGO-/rood-voor-rood-kader en geen rekenformule (drievoudig bevestigd). Wel een interne "Handreiking KGO gemeente Zwolle"; per geval een "KGO-balans" in overleg met initiatiefnemer en provincie. | Niet gevonden (formule); gedeeltelijk (interne Handreiking) | Raadsbrief 15-4-2025 (https://zwolle.bestuurlijkeinformatie.nl/Document/View/561bbd5c-6691-452e-9ff6-ed79d8c91179, 2026-08-21) | Afdeling Ruimtelijke Ontwikkeling/NRI (Woo-verzoek mogelijk) |
| B2 | Schaalgrenzen niet gevonden. Precedenten: 2 (Windesheim), 3 (Zalkerdijk), max. 7 (Kiekeboslaantje), 32 zorgeenheden via gebiedsontwikkeling (Wijthmen). 10-12 woningen via erfregime onwaarschijnlijk; bindend raadsadvies > 5. | Gedeeltelijk gevonden | Zalkerdijk-stukken; https://www.rtvfocuszwolle.nl/zorg-natuur-en-water-komen-samen-in-wijthmen-32-zorgwoningen-boerderij-en-waterwinning-gepland-aan-erfgenamenweg/ (2026-08-21); CVDR726092 | Interne Handreiking KGO; team NRI |
| B3 | Zwols buitengebiedbeleid "op termijn te actualiseren" (apr. 2025); **coalitieakkoord 2026-2030 (25-6-2026) kondigt actualisatie van de KGO aan** voor "meer ruimte [...] op erven en in het buitengebied" (geen termijn); geen vastgestelde herziening gevonden; Omgevingsplan gewijzigd 8-5-2026 (inhoud niet onderzocht). Provinciale regels gewijzigd per 1-7-2026; aanpassing uiterlijk 1-7-2029, direct werking bij BOPA. Uitkomst afhankelijk van een provinciale regel die recent is gewijzigd. | Gedeeltelijk gevonden (voornemen) | Coalitieakkoord p. 22 (https://media.d66.nl/uploads/sites/78/2026/06/Coalitieakkoord-Zwolle-2026-2030-Bouwen-op-Zwolse-kracht.pdf, 2026-10-02); CVDR696214 (2026-08-21); provincie_overijssel.md §1.1 | Zwolse raadsagenda's 2025-2026 ("buitengebied", "erfontwikkeling", "KGO"); afdeling Ruimtelijke Ontwikkeling |
| B4 | Contour bestaand bebouwd gebied/stadsrand niet vastgesteld in gevonden stukken (ontwerp-Omgevingsvisie: Gemeenteblad 2025, 448748). Zwolle hanteert wel "Stedelijke Omgeving" vs "Groene Omgeving". Provincie verruimde erfontwikkeling in de stadsrandzone. | Niet gevonden | https://zoek.officielebekendmakingen.nl/gmb-2025-448748.html (2026-08-21) | Definitieve Omgevingsvisie Zwolle; kaarten op DSO/planviewer |
| B5 | Vorm kwaliteitsinvestering: college stelt dat maatregelen niet altijd op het perceel passen (Zalkerdijk); bij Kiekeboslaantje gaat opbrengst van 5 kavels naar kwaliteitsverbetering elders in het buitengebied. Afdwinging (anterieure overeenkomst/bankgarantie): niet gevonden. | Gedeeltelijk gevonden | Beslisnota 24-3-2025; zwolle.nl/Kiekeboslaantje-berichtgeving (2026-08-21) | Afdeling Vastgoed/NRI |

### C. Locatie-overlays
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| C1 | Landbouwgebied-type (generiek/gebiedsspecifiek) voor Zwolse deelgebieden niet vastgesteld; kaartlaag niet geraadpleegd. | Niet gevonden | provincie_overijssel.md §1.4 | https://ruimtelijkeplannen.overijssel.nl/omgevingsvisie; https://omgevingswet.overheid.nl/regels-op-de-kaart |
| C2 | Geen toepassing van art. 4.124 lid 4 gevonden. Het gepauzeerde gebiedsproces IJsselvizier (landschapsontwikkelplan erftransformatie; € 238.000; 6-11-2024) is een kandidaat-"samenhangende gebiedsvisie" (*interpretatie*, dateert van vóór art. 4.124). | Niet gevonden | Raadsvoorstel Stadsbroek/IJsselvizier 6-11-2024 (2026-08-21) | Afdeling Ruimtelijke Ontwikkeling; provinciale accounthouder |
| C3 | Aangetroffen: Natura 2000 Uiterwaarden Zwarte Water en Vecht (in omgevingsplan Zwolle), Nationaal Landschap IJsseldelta (Vreugderijkerwaard/Spoolde), Dijklanden ("geen ruimte voor een nieuwe woonwijk"). NNN, grondwaterbescherming, stikstof (CDA-vragen jul. 2026), raatakkers/karrensporen, Catalogus Gebiedskenmerken per deelgebied: niet gecontroleerd. | Gedeeltelijk gevonden | https://www.overijssel.nl/onderwerpen/natuur-en-landschap/natura-2000-n2000/alle-natura-2000-gebieden-in-overijssel/uiterwaarden-zwarte-water-en-vecht/; https://www.natuurmonumenten.nl/natuurgebieden/vreugderijkerwaard (2026-08-21) | Provinciale kaartlagen; DSO |
| C4 | Standaardonderbouwing redeneerlijn (art. 4.122) en energieparagraaf/netcongestie voor kleine woonprojecten in Zwolle: niet gevonden. Het gemeentelijke OF/WAAR/HOE-kader is de voorloper. | Niet gevonden | https://www.zwolle.nl/vestigen-buitengebied (2026-08-21) | Afdeling Ruimtelijke Ontwikkeling; netbeheerder (netcongestiekaart) |

### D. VAB en erftransformatie
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| D1 | Deelname aan subsidie 4.39/intergemeentelijk VAB-programma niet vastgesteld. Provinciale brief aan alle colleges (25-2-2025) nodigt uit tot VAB-/erftransformatieprogramma's en "ruimte om te leren"; Zwolse reactie niet gevonden. Regeling open op 2026-10-02, verplichting vóór eind 2026 (tijdgevoelig). | Niet gevonden | provincie_overijssel.md §3.1; https://zwolle.bestuurlijkeinformatie.nl/Document/View/420f3788-b48d-4782-9cbb-e04f0a083739 (2026-10-02) | vab@overijssel.nl; Overijssel Loket |
| D2 | Erfcoach/Atelier Overijssel in Zwolle niet vastgesteld. | Niet gevonden | provincie_overijssel.md §2.4 | BoerenPerspectief Overijssel; erfcoachoverijssel.nl |
| D3 | Geen Zwolse VAB-beleidsregel (drievoudig bevestigd). Precedenten: Zalkerdijk 26a, Kiekeboslaantje, Windesheim, Wijthmen. Maximum per VAB-erf en eisen aan omliggende bedrijven: niet gevonden. BuitenDelen (Lettele) = Deventer. | Gevonden (geen beleid); maximumaantal niet gevonden | CVDR-zoekacties Zwolle (https://lokaleregelgeving.overheid.nl/ZoekResultaat?gemeenten=Zwolle, 2026-08-21) | Omgevingsplan agrarische afdelingen 4.1-4.15; team NRI |

### E. Procedure en provinciale betrokkenheid
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| E1 | Naam accounthouder niet openbaar. Zalkerdijk: gesprekken met provincie en waterschap in pilotfase; brief van de provincie als bijlage bij raadsbrief. Omgevingstafel/1-op-1-gesprekken voor Zwolle: niet gevonden (Omgevingstafel IJsselland-URL gaf 404; welke tafel voor Zwolle geldt is niet geverifieerd). | Gedeeltelijk gevonden | Raadsbrief 15-4-2025 (2026-08-21); provincie_overijssel.md §4.2 | Gemeentelijke RO-afdeling; Overijssel Loket |
| E2 | Zwolle: NRI/Routekaart; BOPA via omgevingsvergunning. Provincie: BOPA met nieuwe woningen in Groene Omgeving vereist advies + instemming (4-6 weken advies, 4 weken instemming); raad: bindend advies. Zwolse doorlooptijd niet gepubliceerd (indicatief 1-2 jaar). | Gevonden (kader); gedeeltelijk (doorlooptijd) | https://www.zwolle.nl/ruimtelijke-initiatieven (2026-08-21); provincie_overijssel.md §4.3 | Team NRI |
| E3 | 10-12 woningen ligt op de 11-woningengrens van de Uitzonderingenlijst, die alleen geldt in bestaand bebouwd gebied van kernen > 1.000 inwoners; niet voor het buitengebied. Of Zwolle een locatie als bestaand bebouwd gebied aanwijst, is niet vastgesteld; raadsadvies (≥ 5 woningen) geldt ook in stedelijk gebied. | Gedeeltelijk gevonden | provincie_overijssel.md §4.2; CVDR726092 (2026-08-21) | Gemeentelijke RO-afdeling |
| E4 | Geen bevestigde provinciale zienswijze, aanwijzing of onthouden instemming voor een Zwols buitengebied-plan 2023-2026 gevonden (2010-aanwijzing betrof Ommen). Hasselterdijk 43a ging in vooroverleg met provincie e.a. (neutraal). | Niet gevonden | Deelonderzoek provinciaal-lokaal (2026-08-21) | Provinciale accounthouder; nota's van zienswijzen bij Zwolse ontwerpplannen (Gemeenteblad/planviewer) |

### F. Financiering
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| F1 | Gebruik van provinciale regelingen (Betaalbaar wonen in kleine steden en dorpen, Flexpools, Fysieke investeringen leefbaar platteland, Langer zelfstandig wonen e.d.) door Zwolle niet vastgesteld; de meeste regelingen zijn gemeentelijk/woonplatform-gericht, niet rechtstreeks voor een particulier collectief. Zwolle is grote stad, waardoor "kleine kernen"-regelingen vermoedelijk beperkt toepasbaar zijn (*interpretatie*). | Niet gevonden | provincie_overijssel.md §3.2 | https://regelen.overijssel.nl/Producten_en_diensten/Subsidies/Wonen_en_leefbaarheid; woonaanpak@overijssel.nl |

### Houdbaarheid (herverifiëren vóór gebruik)
- **Provinciaal:** Actualisatie 2026-2 (PS-besluit december 2026, technisch); Besluit regie volkshuisvesting/ladder (verwacht 1-1-2027); provinciaal volkshuisvestingsprogramma (status onbekend); subsidie 4.39 (verplichting vóór eind 2026); herziening Werkboek/Handreiking KGO en Kwaliteitsimpuls Agro & Food; Provinciale Statenverkiezingen maart 2027 (zie provincie_overijssel.md §6.1). Controleer altijd de geconsolideerde Omgevingsverordening (CVDR706717) en de kaartlaag landbouwgebieden vóór het citeren van artikelnummers of gebiedstypen.
- **Landelijk:** gemeentelijk volkshuisvestingsprogramma uiterlijk 1-7-2027 (bronnen verschillen); huisvestingsverordening uiterlijk 1-1-2028 (primaire bron).
- **Zwolle:** definitieve vaststelling Omgevingsvisie (vertraagd); **actualisatie KGO/buitengebiedbeleid** (aangekondigd in coalitieakkoord); Volkshuisvestingsprogramma (Q3 2026 gepland); uitkomst huisvestingsverordening-procedure; Omgevingsplan (laatst gewijzigd 8-5-2026); Grondprijzenbrief 2027; nog open: erfpachtpercentage 2025 vs. 2026. De eerdere tegenstrijdigheden CVDR739354/CVDR729056 zijn opgelost (andere gemeenten).
- **Afhankelijkheid van recente provinciale wijzigingen:** de uitkomsten bij A4, B3, B4, C1, C2, C4 en E2 hangen af van provinciale regels die per **1-7-2026** zijn gewijzigd of nog kunnen wijzigen.
