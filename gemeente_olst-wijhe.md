# Gemeente Olst-Wijhe — CPO-naslagwerk (provincie Overijssel)

> **Status: geverifieerde versie (2026-10-05).** Dit rapport vervangt het eerdere concept van 2026-10-02, dat zonder toegang tot brondocumenten uit zoekresultaat-samenvattingen was samengesteld. Alle bevindingen zijn nu getoetst aan de brondocumenten zelf (gemeentelijke stukken, iBabs, CVDR, Gemeenteblad, Provinciaal blad, provinciale kaartlagen) en waar mogelijk als letterlijk citaat opgenomen (blockquote met bron en raadplegingsdatum). Wat niet gevonden of niet oplosbaar is, staat expliciet vermeld met de vindplaats.

## Verantwoording
- **Raadplegingsdatum:** 2026-10-04 en 2026-10-05. Elk citaat vermeldt de eigen raadplegingsdatum.
- **Provincie en gebruikt provinciebestand:** Overijssel, [`provincie_overijssel.md`](provincie_overijssel.md) (stand 2026-10-02; in deze ronde op drie punten gecorrigeerd, zie "Correcties op het provinciebestand"). Het Overijsselse regime is leidend voor het omgevingsplan. Bijlage A is van toepassing; Bijlage B (Gelderland) niet.
- **Primair model + effort:** de synthese en het eindrapport zijn geschreven door Claude Sonnet 5.5 (`claude-sonnet-5-5`); de sessie is gestart met Claude Opus 5.5 (`claude-opus-5-5`), die de verificatieronde heeft opgezet en de deelonderzoeken heeft gelanceerd. Het ingestelde reasoning-effort van de sessie was 10 (waarde uit de sessieconfiguratie; schaal niet nader gespecificeerd); voor de subagents is geen effort expliciet ingesteld.
- **Deelonderzoeken (Fase 2), alle vier uitgevoerd door subagents, elk met één brontype en alle 12 onderwerpen:**

| Deelonderzoek | Brontype | Model | Opmerking |
|---|---|---|---|
| 1 | Gemeentelijke bestuursinformatie | Claude Sonnet 5.5 (herstart) | Eerste run (Opus 5.5) stopte door een sessielimiet voordat het rapport was geschreven; herstart na de modelwissel, met hergebruik van de al geëxtraheerde bronbestanden. Het model van de herstart is overgenomen van het hoofdmodel op dat moment en niet apart bevestigd. |
| 2 | Provinciaal-lokale toepassing | Claude Sonnet 5.5 (herstart) | Idem. |
| 3 | Nieuws en actualiteit 2024-2026 | Claude Opus 5.5 | Rapport volledig geschreven; de run is daarna afgebroken door een sessielimiet (volgens de foutmelding op `claude-opus-5-5`). |
| 4 | Juridische en officiële registers | Claude Opus 5.5 | Afgerond. |

- **Methode:** vier gelijktijdig uitgezette deelonderzoeken (daarna twee herstarts), samengevoegd tot dit rapport. Dubbele bevindingen zijn gededupliceerd. Waar deelonderzoeken elkaar tegenspraken, is de brontekst geraadpleegd (zie "Tegenstrijdigheden en onzekerheden: stand na verificatie"). De hoofdagent heeft zelf steekproefsgewijs gecontroleerd: de kop van CVDR305226 en CVDR704153, de Omgevingstafel-URL en -pagina, de tekst van de beleidsnota woningsplitsing (reikwijdte 1-5 woningen), de Grondprijzenbrief-bandbreedte, de motie van 26-5-2026 en de Engeweg-passage over de provincie.
- **Toegang en technische beperkingen (stand 2026-10-04/05):**
  - Alle gevraagde hosts waren bereikbaar: olst-wijhe.nl en de subdomeinen (www., mijnleefomgeving., mijnkijkop., wonen., ro., gemeenteraad., archief.), olstwijhe.bestuurlijkeinformatie.nl, lokaleregelgeving.overheid.nl, zoek.officielebekendmakingen.nl, repository.overheid.nl, ruimtelijkeplannen.nl, planviewer.nl, ruimtelijkeplannen.overijssel.nl, omgevingswet.overheid.nl, overijssel.nl en odijsselland.nl.
  - *.olst-wijhe.nl stuurt het tussencertificaat (Sectigo Public Server Authentication CA OV R36) niet mee; de verbinding is gevalideerd door dat tussencertificaat van de in het servercertificaat vermelde AIA-URL toe te voegen aan de vertrouwde keten. Certificaatverificatie is niet uitgeschakeld.
  - Veel losse nieuws- en woonnieuws-URL's die in het eerdere concept stonden (`.../nieuwsberichten/2026/m/d/slug`, `wonen.olst-wijhe.nl/woonnieuws/woonnieuws/2026/m/d/slug`) geven op 2026-10-04/05 een 404. De tekst is wel gelezen via de archiefexports van de gemeente (`.../nieuwsberichten/archive.csv`, `.../woonnieuws/archive.csv`, `.../b-amp-w-besluiten/archive.csv`); in dit rapport is bij zulke berichten de titel en publicatiedatum vermeld.
  - De Stentor was niet toegankelijk (betaalmuur); RTV Oost leverde niets relevants op.
  - Inhoud van Gemeenteblad en CVDR is via de SRU-zoekservices volledig doorzocht (628 CVDR-records van Olst-Wijhe; 2.235 Gemeenteblad-publicaties sinds 1-1-2024; Provinciaal blad sinds 2023 op "Olst-Wijhe": 69 treffers).
- **Betrouwbaarheidsmarkering:** citaten zijn letterlijk uit de brontekst; **[PB]** = uit `provincie_overijssel.md`; **[TK]** = trainingskennis, niet live geverifieerd; **[INT]** = interpretatie van de samensteller; **[BER]** = eigen berekening. Tekst zonder markering is een directe weergave van de aangegeven bron.

### Verificatie van CVDR-nummers (organisatie uit de kop "Overheidsorganisatie", geraadpleegd 2026-10-04)
| Nummer | Organisatie volgens kop | Titel | Opmerking |
|---|---|---|---|
| CVDR696503 | **Olst-Wijhe** | Omgevingsplan gemeente Olst-Wijhe | In werking 1-1-2024; huidige versie geldt vanaf 3-9-2026 |
| CVDR691005 | **Olst-Wijhe** | Nota Grondbeleid 2023-2026 | Raad 12-12-2022; in werking 17-1-2023 |
| CVDR752237 | **Olst-Wijhe** | Verordening op de heffing en de invordering van leges 2026 | Raad 24-11-2025; in werking 23-12-2025 |
| CVDR765519 | **Olst-Wijhe** | Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten 2026 | B&W 11-8-2026; Gmb 2026, 385444 |
| CVDR704153 | **Olst-Wijhe** | Besluit tot aanwijzing van categorieën van gevallen van een BOPA waarvoor een advies van de raad nodig is | Raad 7-2-2022; in werking 1-1-2024 |
| CVDR638025 | **Olst-Wijhe** | Notitie Buurtschappenbeleid | B&W 18-2-2020; Gmb 2020, 63767 |
| CVDR305226 | **Tubbergen** (gezamenlijk kader Tubbergen en Dinkelland, 2013) | Gemeentelijk beleidskader Kwaliteitsimpuls groene omgeving (KGO) | **Vervallen per 16-2-2022.** Niet Olst-Wijhe. |
| CVDR720837 | Harlingen | Nota grondbeleid 2024-2027 | Niet Olst-Wijhe; daarmee vervalt de "Nota Grondbeleid 2024-2028" |
| CVDR663985 / 638437 / 734442 / 738282 / 726084 / 743316 / 734518 / 729056 / 739354 | Bladel / Best / Sint-Michielsgestel / Urk / Hof van Twente / Steenwijkerland / Rijssen-Holten / Gooise Meren / Groningen | CPO-beleidsregels / VAB / VAB en woningbouw buitengebied / woningsplitsing / KGO 2023-2028 / VAB / buitengebied 2024 / woonvisie / huisvestingsverordening | Geen van deze is Olst-Wijhe |

Letterlijk, kop van CVDR305226:

> "Regeling vervallen per 16-02-2022 / Gemeentelijk beleidskader Kwaliteitsimpuls groene omgeving (KGO) / Geldend van 31-03-2016 t/m 15-02-2022 / Algemeen / Overheidsorganisatie / Tubbergen / Organisatietype / Gemeente"

— Bron: https://lokaleregelgeving.overheid.nl/CVDR305226?show-wti=true (geraadpleegd 2026-10-04)

### Correcties op het provinciebestand (`provincie_overijssel.md`), in dezelfde commit doorgevoerd
1. §2.3 (voorbeeld Olst-Wijhe): de verwijzing naar CVDR305226 is geschrapt; dat nummer is van Tubbergen en vervallen. Olst-Wijhe heeft de Handreiking KGO als collegedocument (geen CVDR-regeling).
2. §4.2 en §6.3: de Omgevingstafel IJsselland heeft als werkende URL https://www.odijsselland.nl/over/omgevingstafel (HTTP 200 op 2026-10-04/05). `…/omgevingstafel-ijsselland` en `…/omgevingstafel` geven 404.
3. §4.2: de pagina van de Omgevingstafel zegt dat de initiatiefnemer zelf aanwezig *kan en mag* zijn; de eerdere zin "in beginsel niet aanwezig" is aangepast.

### Gemeentelijke indeling (vastgesteld uit bronnen)
De Omgevingsvisie spreekt van twaalf kernen en buurtschappen. **Grote kernen:** Olst, Wijhe, Wesepe. **Kleine kernen:** Boerhaar, Boskamp, Den Nul, Welsum, Herxen. **Buurtschappen** o.a. Elshof, Marle, Eikelhof, Middel (bestuursakkoord p. 23 telt exact twaalf namen in de kernenwethouder-verdeling). De aantallen 7 (allecijfers.nl, statistische kernen [INT]) en 12 verschillen dus alleen door definitie. **Emst(-Noord) hoort niet bij Olst-Wijhe** (Gelderland, gemeente Epe [TK]).

**Regionale positie:** woonregio West-Overijssel (Woondeal 2025-2030) [PB]; het ontwerp-Volkshuisvestingsprogramma Overijssel (Prb 2026, 11834) plaatst Olst-Wijhe in de "Woningbouwregio West-Overijssel" én de "Woningmarktregio West-Overijssel". Regio Zwolle-lidmaatschap is bevestigd:

> "Salland is zowel onderdeel van de Stedendriehoek als van Regio Zwolle. De gemeenten Olst-Wijhe en Raalte werken samen binnen Regio Zwolle, terwijl gemeente Deventer samen met de gemeenten Apeldoorn, Brummen, Epe, Heerde, Lochem, Voorst en Zutphen de Stedendriehoek vormt."

— Bron: Omgevingsvisie Overijssel, Prb 2026, 10885, p. 124-125, https://zoek.officielebekendmakingen.nl/prb-2026-10885.pdf (geraadpleegd 2026-10-05). De gemeentelijke Omgevingsvisie (p. 38) noemt de gemeente eveneens onderdeel van de regio Zwolle en ook gericht op de Stedendriehoek; Hans Olthof heeft "Regio Zwolle" in zijn portefeuille en de gebiedsaanpak Wesepe wordt ingediend bij de Regio Deal Regio Zwolle II. De uittreding in 2023 betreft de **arbeidsmarktregio** Stedendriehoek en Noordwest-Veluwe (nota Deventer 2023-543, alleen titel en zoeksamenvatting gezien; het pdf gaf 404) en niet de woonregio. De gemeente grenst over de IJssel aan Gelderse gemeenten (Heerde, Epe, Voorst [TK]); Gelders beleid is alleen context.

---

## 1. CPO-beleid

Olst-Wijhe heeft **geen eigen, gepubliceerd CPO-beleid of CPO-handreiking** (niet in CVDR of Gemeenteblad; niet op de gemeentesite gevonden). CPO is verankerd als *open houding* in de Omgevingsvisie, de Woonvisie en het Uitvoeringsprogramma; de uitwerking loopt per project via uitgifteprotocollen en projectovereenkomsten.

**Omgevingsvisie "Olst-Wijhe 2050"** noemt CPO uitdrukkelijk (kleine kernen, p. 24, gebiedsgerichte keuze 1):

> "In de kleine kernen (Boerhaar, Boskamp, Den Nul, Welsum en Herxen) bieden we ruimte voor kleinschalige woningbouwinitiatieven, passend bij de schaal van de kern, de aantoonbare lokale behoefte en de draagkracht van het aanwezige bodem- en watersysteem. Indicatief kan gedacht worden aan een groei van 5% tot 10% tot en met 2050. Hoe en waar we dit gaan doen werken we uit in ons volkshuisvestingsprogramma. Qua woningbouwprogramma kiezen we hier voor een focus op doorstroming, waarbij we oog hebben voor het behouden en aantrekken van de jongere doelgroep. We staan open voor collectieve woonvormen en initiatieven vanuit de samenleving, bijvoorbeeld op het gebied van collectief particulier opdrachtgeverschap (CPO). Ook hier volgen we het principe van inbreiding (waaronder transformatie, herstructurering of woningsplitsing) voor uitbreiding. In de buurtschappen is maatwerk het uitgangspunt voor woningbouwinitiatieven."

— Bron: Omgevingsvisie Olst-Wijhe 2050, p. 24, https://mijnkijkop.olst-wijhe.nl/omgevingsvisie (geraadpleegd 2026-10-04)

Voor de grote kernen (p. 19-20, keuze 6): "[…] kleinschalige initiatieven op het gebied van collectieve woonconcepten. Op plekken waar dat voor de hand ligt stimuleren we vernieuwende, innovatieve vormen van woningen / woningbouwconcepten […]". Voor het **buitengebied** bevat de visie geen CPO-passage. Het principe is "inbreiding voor uitbreiding".

**Woonvisie 2022-2025** (raad juni 2022; formeel afgelopen per 1-1-2026), https://www.olst-wijhe.nl/bestuur/visies-beleid-en-regelgeving/wonen-en-leven/wonen/woonvisie-2022-2025/woonvisie-olst-wijhe-2022-2025 (geraadpleegd 2026-10-04):

> "4.4 Mogelijkheden voor vernieuwende vormen van wonen: […] Ook kunnen we aansluiten op de ervaringen die we al opgedaan hebben opgedaan bij de CPO-projecten zoals Vriendenerf en Aardenhuizen en staan we open voor concepten die inhaken op de groeiende behoefte aan Flexwonen." (p. 33)

> "Overige kernen: De woningbouw in de kleine kernen heeft overwegend een kleinschalig en wat meer incidenteel karakter. Nieuwe koopwoningen zullen overwegend vanuit particulier opdrachtgeverschap of kleine projectmatige ontwikkelingen worden gerealiseerd."

**Uitvoeringsprogramma Woonvisie** (B&W 25-4-2023; zaak 14775-2023), https://www.olst-wijhe.nl/bestuur/visies-beleid-en-regelgeving/wonen-en-leven/wonen/uitvoeringsprogramma/uitvoeringsprogramma-woonvisie-olst-wijhe (geraadpleegd 2026-10-04):

> "11 Collectief (particulier) opdrachtgeverschap: We staan open voor projecten via Collectief Particulier Opdrachtgeverschap (CPO). Op deze manier hebben lokale woningzoekers, waaronder jongeren, meer kans om een betaalbare woning te realiseren. Een recent voorbeeld hiervan is het CPO-project Boskamp dat in de opstartfase zit."

Actielijst: "Doorlopend | Begeleiden lokale initiatieven. Per project bezien of CPO van toegevoegde waarde kan zijn." Dezelfde stukken noemen ook experimentele woonvormen ("10 Experimenten en proeftuinprojecten […] zoals Olstergaard en Noordmanshoek"). De bandbreedte "vijf tot circa vijftig woningen" uit het eerdere concept is in **geen enkele Olst-Wijhese bron** gevonden en is verwijderd.

**College, november 2025** (lokale binding): het college noemt CPO uitdrukkelijk als instrument:

> "Als gemeente zetten we nu vooral in op andere instrumenten zoals de Starterslening, […] het regelen van betaalbare woningbouw (onder andere 30% sociale huur en koopwoningen tot € 260.000) en het gebruikmaken van het instrument CPO (collectief particulier opdrachtgeverschap)."

— Bron: B&W 11-11-2025, punt 12 (beantwoording vragen VVD over erfpacht en lokale bindingseisen), https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten (archive.csv) en Raadsinformatiebrief 10-11-2025, zaak 45292-2025, p. 3 (iBabs) (geraadpleegd 2026-10-04)

**Raadsmotie CPO-prioriteit, 26-5-2026.** Bij het raadsvoorstel "Aanvraag kredieten voor woningbouw Boerhaar" (zie §6) nam de raad een motie aan:

> "De fractie van GroenLinks-PvdA-D66 dient een motie in met het verzoek aan het college om: • CPO's en andere woningbouwinitiatieven afkomstig uit onze samenleving waar mogelijk naar deskundigen te verwijzen, binnen bestaande capaciteit en middelen […]; • Open, helder en tijdig te communiceren met initiatiefnemers over de (on)mogelijkheden van de realisatie van het project, alsmede over de te volgen procedures; • Daar waar mogelijk prioriteit te geven aan CPO-initiatieven en andere bouwinitiatieven afkomstig uit de samenleving; • De gemeenteraad actief en structureel te informeren over de voortgang van de realisatie van CPO-projecten en andere bouwprojecten vanuit de samenleving. De motie wordt aangenomen met 11 stemmen voor (GroenLinks-PvdA-D66, VVD, Jansen en Steenbergen) en 6 tegen (Gemeentebelangen en mevrouw Olthof)."

— Bron: Besluitenlijst raadsvergadering 26-5-2026, https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/8a11295f-c63c-4bd9-890c-5d94773657de (geraadpleegd 2026-10-05)

Een raadslid van de oppositie schreef over deze motie dat ze volgde op "stevige kritiek van de Boskamp, van de Boerhaar en uit Wesepe op B. en W." en dat het college haar ontraadde (column Toon Schuiling, HierinSalland, 13-6-2026, https://hierinsalland.nl/onze-man-in-wijhe-toon-schuiling-6/; opiniestuk). Of het college de motie uitvoert, is niet gevonden.

**Kaveluitgifte en CPO-spoor:**
- *De Klimboom, Boskamp:* in het Gemeenteblad publiceert de gemeente haar Didam-conforme uitgiftevoornemen: 

  > "De herontwikkeling van de Klimboom bestaat uit de sloop van de bestaande bebouwing en het bouwen van zeventien (17) woningen. […] De andere negen (9) woningen zijn zogenoemde Collectief Particulier Opdrachtgeverschap (CPO) woningen. -De woningbouwkavels bestemd voor CPO worden niet via een openbare selectieprocedure verkocht."

  — Bron: Gemeenteblad 2024, 142870, https://zoek.officielebekendmakingen.nl/gmb-2024-142870.html (geraadpleegd 2026-10-04). Dat is een bruikbaar precedent voor een-op-een-uitgifte aan een CPO-vereniging.
- *Lotingsreglement particuliere bouwkavels woningbouw 2025* (B&W 2-12-2025, zaak 47173-2025): 

  > "Inschrijving kan uitsluitend plaatsvinden door natuurlijke personen. Rechtspersonen zijn uitgesloten." (art. 6 lid 3)

  Het reglement vervangt het Lotingsreglement 2011 en het Reglement uitgifte bouwkavels via de Kavelwinkel 2014 (art. 2). CPO-groepen (rechtspersonen) worden niet apart genoemd en vallen dus buiten dit reglement; CPO-uitgifte loopt via een uitgifteprotocol of projectovereenkomst per locatie. Bron: Lotingsreglement 2025 (iBabs, https://www.olst-wijhe.nl/bestuur/visies-beleid-en-regelgeving/wonen-en-leven/wonen/lotingsreglement-bouwkavels/lotingsreglement-particuliere-bouwkavels-woningbouw-gemeente-olst-wijhe-2025-1) (geraadpleegd 2026-10-04)
- *Kavelwinkel* (https://wonen.olst-wijhe.nl/kavelwinkel, 2026-10-05): "Soms zijn er ook kavels voor twee-onder-1-kapwoningen of rijwoningen. Dan ontwikkel je het bouwplan samen met andere kopers, onder collectief particulier opdrachtgeverschap." en "Op dit moment zijn er geen kavels te koop."
- *Nota Grondbeleid* (p. 22): bij verkoop van een groter gebied kan het college "beargumenteerd besluiten een korting te geven op de grondprijs" bij "innovatieve initiatieven die maatschappelijk gezien wenselijk zijn" (zie §5).

**Bestuursakkoord 2026-2030:** CPO, collectief, zelfbouw, experiment, KGO en erf komen er **niet** in voor (gecontroleerd in de volledige tekst; zie §10).

**Niet gevonden:** een gemeentelijke CPO-beleidsregel, -handreiking of -loket; een CPO-grondprijsregeling; een CPO-reservering in Olst Zuid of Wijhe Noord. **Waar te vinden:** het Volkshuisvestingsprogramma (in voorbereiding), team Ruimtelijke Realisatie (Grondzaken en Vastgoed), uitwerking van de motie van 26-5-2026 in iBabs.

Landelijk hulpmiddel (niet Olst-Wijhe-specifiek): RVO, Handreiking Collectief bouwen en wonen voor gemeenten (10-2025), https://www.rvo.nl/sites/default/files/2025-10/Handreiking%20Collectief%20bouwen%20en%20wonen.pdf (niet gelezen).

*Duiding [INT]:* de gemeente heeft een aantoonbaar CPO-spoor in en aan de kernen (Klimboom, Olstergaard, Boerhaar, Herxen). Voor agrarische grond buiten de kernen bestaat geen CPO-kader; daar gelden KGO-Handreiking en maatwerk-BOPA.

---

## 2. Openheid voor nieuwbouw buiten woonkernen

**Omgevingsvisie "Olst-Wijhe 2050"** is op **12 mei 2025** door de raad vastgesteld, na een geamendeerd en unaniem aangenomen voorstel:

> "Raadsvergadering, d.d. 12 mei 2025 agendapunt 8 […] Onderwerp Voorstel tot vaststellen omgevingsvisie 'Olst-Wijhe 2050', het intrekken van de Structuurvisie 'Ruimte voor initiatief en innovatie' en in te stemmen met de nota van beantwoording van zienswijzen."

> "8. Voorstel tot vaststellen omgevingsvisie 'Olst-Wijhe 2050' […] Het amendement van de VVD 'Zonering', waarbij op 14 april de stemmen staakten, werd ingetrokken. De fractie van het CDA (mede-indieners Gemeentebelangen, VVD en PvdS) dienen een amendement in […] Het amendement wordt unaniem aangenomen. […] Het geamendeerde raadsvoorstel is unaniem aangenomen."

— Bron: raadsvoorstel zaak 44998-2024 en besluitenlijst raadsvergadering 12-5-2025, https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/108ea842-ae63-469e-a7b1-3d4c49fd2177 (geraadpleegd 2026-10-04/05). Het ontwerp lag ter inzage 13-11 t/m 27-12-2024 (Gemeenteblad 2024, 477293 en 480688; 33 zienswijzen). Een Gemeenteblad-bekendmaking van de vaststelling is niet gevonden.

Kernpunten (letterlijk):

> "We bouwen vooral in de grotere kernen: Wijhe, Olst en Wesepe. Er worden allerlei soorten woningen gebouwd […] In de kleinere kern komen kleinschalige woningbouwprojecten. We bouwen zo veel mogelijk binnen de dorpsgrenzen. Als agrarische schuren worden gesloopt, bouwen we woningen waar mogelijk terug dichtbij de kern in plaats van verspreid over het landschap." (p. 5)

> "Er is in de IJsselzone geen ruimte voor nieuwe woningbouw of grootschalige bedrijven." (p. 5) / "[…] we [streven] ernaar om in het IJsselgebied geen nieuwe woningbouw en (grootschalige) bedrijvigheid toe te staan […]" (p. 28)

> Kommenlandschap: "Vanuit 'bodem en water sturend' zijn we over het algemeen terughoudend in het toevoegen van nieuwe woningen. […] Voor vrijkomende (agrarische) bebouwing in het kommenlandschap zijn we terughoudend met de functieverandering naar wonen. We verkennen samen met de provincie Overijssel spelregels en randvoorwaarden voor de inzet van het verplaatsen van sloopmeters en bouwrechten, waarbij woningbouw van de vrijkomende locatie in principe verplaatst wordt naar de zone direct rondom de kernen." (p. 30-32)

> Dekzandgronden: "De hogere ligging van de dekzandgronden biedt mogelijkheden voor functieverandering naar wonen of woonzorgconcepten. Dit geldt voornamelijk voor (voormalige) boerenerven in de directe omgeving van de kernen en buurtschappen. […] Op de hogere dekzandgronden zien we in de toekomst ruimte voor het selectief toevoegen van woningen. In eerste instantie kijken we daarbij naar locaties rondom de kern Wesepe en ten zuidoosten van Boskamp." (p. 34-35)

> "5. We zetten beleidsregels en instrumentarium in om sloopmeters van vrijkomende agrarische bebouwing (VAB) elders in de gemeente in te zetten voor woningbouwinitiatieven rondom de kernen en buurtschappen. In de uitwerking van de visie in bijvoorbeeld een omgevingsprogramma bepalen we de specifieke afstand / zone rondom de kern en welke instrumenten we hiervoor inzetten." (p. 19-20)

— Bron: Omgevingsvisie Olst-Wijhe 2050, https://mijnkijkop.olst-wijhe.nl/omgevingsvisie (geraadpleegd 2026-10-04). **Wesepe** is groeikern: "Vanwege de relatief hogere ligging van Wesepe zien we hier potentie om naast inbreiding ook op zoek te gaan naar uitbreidingslocaties" (p. 19-20; circa 200 woningen tot 2032 volgens B&W 22-4-2025, zaak 36978-2024).

**Het amendement over de zone rond kernen** (CDA, mede-ingediend door Gemeentebelangen, VVD en PvdS) noemt geen 1 km-afstand. De definitieve tekst:

> "Om nadelige milieu- en gezondheidseffecten te voorkomen, zijn we over het algemeen terughoudend in het toestaan van nieuwe milieubelastende bedrijfsactiviteiten in een nog nader te definiëren zone rondom de kleine kernen. Deze zonering geldt niet voor (uitbreiding van) bestaande bedrijven, mits passend in de geldende wet- en regelgeving."

— Bron: raadsbesluit 12-5-2025 en Omgevingsvisie p. 25 (geraadpleegd 2026-10-04). De "1 kilometer zone" stond in de conceptvisie en is in een zienswijze op het ontwerp aangevochten (nota van beantwoording p. 35). De zone betreft **nieuwe milieubelastende bedrijfsactiviteiten rond kleine kernen**, niet woningbouw. Voor woningbouw zijn relevanter: de nog vast te stellen "specifieke afstand / zone rondom de kern" voor VAB-sloopmeters (visie p. 19-20 en 24) en de **dorpsrandzone** van "maximaal 200 tot 300 meter tot de kern" in het beleid van 24-5-2024 (zie hieronder).

**Contour bestaand bebouwd gebied (B4):** de visie gebruikt "dorpsgrenzen", "(huidige) bebouwd gebied" en "kernrandzones" maar legt **geen contour vast**; de afstandszone rond de kern wordt nog uitgewerkt in een Omgevingsprogramma landelijk gebied en/of het Volkshuisvestingsprogramma. De zonering staat alleen op de integrale visiekaart (afbeelding, iBabs-document 34e53813-5c68-491b-8ea3-9f3d5997f769). Status: niet gevonden.

**Provinciale reactie (nota van beantwoording, zienswijze 23 van 33):**

> "23. Provincie Overijssel — […] De provincie waardeert dat de ontwerp-omgevingsvisie van Olst-Wijhe grotendeels in lijn is met de concept-omgevingsvisie Overijssel. […] Woningbouw: De provincie steunt de focus op woningbouw in de kernen Olst en Wijhe, met nadruk op inbreiding nabij NS-locaties. Ze hebben vragen over de keuze voor Wesepe als hoofdkern, gezien de mobiliteitsuitdagingen en de omringende landbouwgronden. Ze pleiten voor woningbouw op inbreidingslocaties en voor lokale behoeften. […] Ze zijn positief over de uitwerking van kernrandzones en pleiten voor differentiatie op basis van kernomvang en voorzieningenniveau."

— Bron: Nota van beantwoording zienswijzen ontwerp-Omgevingsvisie Olst-Wijhe 2050, p. 24-26 (iBabs, bijlage bij raadsvoorstel zaak 44998-2024) (geraadpleegd 2026-10-04). De gemeente antwoordt dat differentiatie van de kernrandzones "in de uitwerking kan plaatsvinden". Dit is een **positieve provinciale zienswijze met vragen**, geen conflict.

**Provinciaal kader [PB]:** Olst-Wijhe is "overige kern" onder art. 4.4 Omgevingsverordening: woningbouw alleen voor lokale behoefte en bijzondere doelgroepen, tenzij regionale afspraak. Art. 4.5 (aansluiten op bestaand bebouwd gebied; bestaande bebouwing eerst) en de redeneerlijn (art. 4.122, per 1-7-2026) gelden naast de landelijke ladder. Art. 4.4 lid 1 is in de definitieve verordening (in werking 1-7-2026) ongewijzigd: woningbouw wordt alleen mogelijk gemaakt "als die voorzien in een lokale behoefte of in de behoefte van bijzondere doelgroepen"; Olst-Wijhe valt niet onder de grote steden of streekcentra.

**Gemeentelijke reacties op het provinciale beleid.** In de informele consultatie op de concept-omgevingsvisie (B&W 24-9-2024) schreef de gemeente: 

> "Wat wij hierbij niet begrijpen dat de provincie blijft vasthouden aan de eenzijdige en beperkende term lokale behoefte." / "Bij de gebieden met generieke opgaven en kansen vragen we concreet ruimte te bieden om Wesepe als derde groeikern te ontwikkelen […]."

— Bron: reactie op de concept-omgevingsvisie Overijssel (formulier informele consultatieronde, B&W 24-9-2024 punt 8; iBabs; geraadpleegd 2026-10-04). De gemeentelijke zienswijze van 24-6-2025 (B&W, adviesnota zaak 26633-2025) noemt in de adviesnota "veel raakvlakken, zoals op het vlak van woningbouw, recreatie en toerisme" en is kritisch over zon en wind; de zienswijze zelf (bijlage) is niet gepubliceerd gevonden, zodat niet vast te stellen is of zij ook de lokale-behoefteregel of de landbouwtypologie aankaart. Het provinciale antwoord staat in de Zienswijzenota Omgevingsvisie en Omgevingsverordening (Statenstuk PS26-000033), die niet is gevonden; Prb 2026, 10885 meldt alleen dat alle zienswijzen daarin zijn beantwoord en dat visie en verordening "op onderdelen" zijn aangepast. Het provinciale **ontwerp-Volkshuisvestingsprogramma** (Prb 2026, 11834) lag ter inzage van 16-7 t/m 26-8-2026 (Prb 2026, 11967); een gemeentelijke zienswijze daarop is niet gevonden.

**Houding t.o.v. kleinschalige woningbouw buiten de kern.** De gemeente hanteert twee sporen:

1. *Binnen de bebouwde kom:* het Beleid "woningsplitsing en kleinschalige verzoeken om woningbouw binnen de bebouwde kom" (B&W 28-5-2024, zaak 16512-2024; document 24-5-2024). Dat beleid **geldt uitsluitend binnen de bebouwde kom**; de eerdere samenvatting als "maximum van 5 woningen voor het buitengebied of 10 bij betaalbare koop" was onjuist:

   > "Er zijn daarnaast kleinschalige initiatieven voor het realiseren van kleine aantallen nieuwbouw (1 tot 5 woningen) binnen de bebouwde kom."

   > "Bij de uitwerking van de motie wordt onderscheid gemaakt tussen initiatieven binnen en buiten de bebouwde kom. Bij initiatieven buiten de bebouwde kom geldt een ander toetsingskader, mede in relatie tot het KGO beleid." (p. 2) / "In dit beleid wordt hieraan invulling gegeven voor de kernen. Voor het buitengebied wordt dit meegenomen in de handreiking KGO." (p. 4)

   > "In geval sprake is van een transformatie van een pand naar meer dan 5 woningen, valt het betreffende verzoek buiten het kader van dit beleid." (p. 6)

   — Bron: https://wonen.olst-wijhe.nl/woningsplitsing/beleid-woningsplitsing-en-kleinschalige-initiatieven-woningbouw (dit is zelf het PDF; geraadpleegd 2026-10-05). Een maximum van 10 woningen bij betaalbare koop komt in dit beleid, de adviesnota, de evaluatie, de raadsinformatiebrief van 26-5-2026 en de Handreiking KGO **niet** voor. Dorpsrandzones: "Bij een korte afstand van maximaal 200 tot 300 meter tot de kern is er een duidelijke functionele relatie en draagt een woningbouwontwikkeling binnen die zone bij aan de invulling van de behoefte voor die kern." (p. 6)
2. *Buiten de bebouwde kom:* de Handreiking KGO (zie §3). De gemeente onderzoekt actief hoe zij woningbouw in het buitengebied kan beperken. Evaluatie (B&W 26-5-2026, adviesnota zaak 13775-2026; periode 1-5-2024 t/m 1-11-2025):

   > "In de betreffende periode zijn er 52 verzoeken binnenkomen. Daarvan waren er 12 binnen de bebouwde kom en 40 buiten de bebouwde kom. […] Buiten de bebouwde kom (40) is de verdeling als volgt: Ja 16 Toegekend; Nee 11 Geweigerd; Afgebroken 1; Ja, mits: in behandeling 12 Lopend."

   > "Kleinschalige verzoeken om woningbouw zijn van beperkte betekenis voor onze woonprogrammering en kosten naar verhouding veel ambtelijke capaciteit; […] een kritische toetsing van kleinschalige verzoeken blijft daarom gewenst;" / "Zowel bij woningsplitsing als bij kleinschalige initiatieven zien we duidelijk meer verzoeken buiten de bebouwde kom als binnen de bebouwde kom; dat is opvallend, aangezien we ons voor het gemeentelijke woonprogramma meer op de kernen dan het buitengebied richten. De vraag is of we deze trend bij willen sturen;"

   > "Ook wordt onderzocht hoe woningbouw in het buitengebied verder kan worden beperkt."

   — Bron: Evaluatie beleid woningsplitsing en kleinschalige verzoeken om woningbouw (7-5-2026), Raadsinformatiebrief 26-5-2026 en adviesnota 26-5-2026, iBabs (geraadpleegd 2026-10-04)

**Raadssessie bouwsteen Erfontwikkeling, 28-9-2026** (presentatie in iBabs, geraadpleegd 2026-10-04) — de actueelste bron over buitengebied-woningbouw:

> "Woningbouw KGO (ruimte voor ruimte) - Het 'recht' op een woning in ruil voor sloop: niet meer houdbaar. - Alternatief: biedt een sloopsubsidie, maar zonder bouwrecht. - Veel steun om grote woningen in het buitengebied ('villa hagelslag') niet meer toe te staan" (slide 7)

> "Zoekgebied erfontwikkeling — Schakel tussen dorp en landschap. Kernranden van Olst, Wijhe, Wesepe, Herxen, Welsum, Boskamp en Den Nul. […] Hier wil de gemeente nieuwe woningen laten 'landen' via bijvoorbeeld schuifrechten, sloopmeters of een vereveningsfonds. Woningbouw nabij voorzieningen, passend bij de lokale behoefte en als logische afronding van de dorpsrand. Nadruk op levensloopbestendig, geclusterd en compact wonen voor starters en kleine huishoudens." (slide 12)

> "Stellingen: 1. Wie een dure woning in het buitengebied toevoegt, moet financieel bijdragen aan betaalbare woningbouw elders. 2. Nieuwe woningen horen zoveel mogelijk in en aan de randen van de kernen, niet (meer) verspreid in het buitengebied." (slide 15)

**Ladder en volkshuisvestingsprogramma (A4):**
- De Woonvisie liep per 1-1-2026 af. B&W nam op 18-8-2026 kennis van het (niet-openbare) plan van aanpak voor een **Volkshuisvestingsprogramma**:

  > "Vanuit de Wvrv moeten gemeenten en provincies uiterlijk één jaar na de inwerkingtreding van de wet een eigen Volkshuisvestingsprogramma hebben vastgesteld. Dit is dus uiterlijk vóór 1 juli 2027. Het Volkshuisvestingsprogramma vervangt de (huidige) Woonvisie en komt, als een thematisch omgevingsprogramma, onder de Omgevingsvisie te hangen."

  — Bron: B&W-besluitenlijst 18-8-2026, punt 04, https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/b-amp-w-besluiten-18-08-2026 (geraadpleegd 2026-10-04). Wijhe City meldt (24-8-2026) dat het programma "uiterlijk in de zomer van 2027 klaar" moet zijn.
- Een (ontwerp-)programma dat buitengebied- of uitbreidingslocaties aanwijst: **niet gevonden**. Voorbereiding specifiek op de afschaffing van de ladder: niet gevonden; in het raadsbesluit over bindend adviesrecht (2022) wordt de ladder nog als reden voor de 12-woningengrens genoemd ("Met het aantal van 12 woningen (binnen de bebouwde kom) wordt aangesloten bij de Ladder voor duurzame verstedelijking").
- De bedragen in het besluit van 18-8-2026 (koopsom maximaal € 420.000, huur maximaal € 1.228,07, minimaal 30% sociale huur, twee derde betaalbaar) zijn de landelijke Wvrv-kaders en geen eigen vastgesteld woningbouwprogramma. Het inwonerpanel levert input voor het nieuwe woonbeleid (zie §12).
- Het **Bestuursakkoord** wil "een Volkshuisvestingsprogramma ontwikkelen" (p. 8) en "geen nieuwe langjarige visies" (p. 20).

**Herxen (kleine kern):** B&W en GS van Overijssel hebben op 2-6-2026 een bestuursovereenkomst gesloten voor een gezamenlijk visietraject; zie §3b en §6.

---

## 3. Openheid voor agrarische herbestemming (10-12 woningen)

### (a) Wettelijk/procedureel kader

**Omgevingsplan.** Omgevingsplan gemeente Olst-Wijhe (CVDR696503; in werking 1-1-2024; versies 17-4-2024, 6-6-2025, **3-9-2026 (huidig)**). De drie gemeentelijke versies zijn uitsluitend technisch:

> "Om technische redenen is het nodig om het omgevingsplan opnieuw te publiceren. Deze publicatie bevat geen wijzigingen in de juridische inhoud en de aanpassingen hebben geen rechtsgevolg […] Dit besluit treedt in werking per 03-09-2026"

— Bron: Gemeenteblad 2026, 416930, https://zoek.officielebekendmakingen.nl/gmb-2026-416930.html (geraadpleegd 2026-10-04). Het omgevingsplan is tijdelijk (de gemeente heeft "tot en met 2029" om het aan te passen; https://www.olst-wijhe.nl/omgevingsplan); het buitengebied valt onder het tijdelijk deel (Bestemmingsplan Buitengebied). Een aanpassing aan de provinciale Actualisatie 2026 (art. 4.2a) is niet gevonden. Inhoudelijke omgevingsplanwijzigingen 2024-2026 betreffen kernlocaties (IJsseldal Wesepe, hoofdstuk 22a: 81 woningen; Wengelerhoek fase 1, hoofdstuk 22b: 186 woningen incl. 50 flexwoningen). Wonen in het buitengebied loopt na 1-1-2024 uitsluitend via **BOPA's**.

**Bestemmingsplan Buitengebied Olst-Wijhe** (NL.IMRO.1773.BP2020001001, **vastgestelde versie -0301**, raad 12-4-2021; Stcrt. 2021, 22714). De eerder gebruikte URL (-0201) is het ontwerp. Regels, https://www.ruimtelijkeplannen.nl/documents/NL.IMRO.1773.BP2020001001-0301/r_NL.IMRO.1773.BP2020001001-0301.html (geraadpleegd 2026-10-04):
- Bedrijfswoning/burgerwoning: 750 m³ (art. 3.2, art. 24); afwijking tot 1.000 m³ alleen voor volwaardige agrarische bedrijven (art. 3.4.4).
- Vervolgfuncties na bedrijfsbeëindiging (art. 3.9.5): sloop/terugbouw met verplicht inrichtingsplan en "p. het aantal woningen mag niet toenemen;".
- Woningsplitsing (art. 44.1): "a. woningsplitsing is alleen toegestaan ter plaatse van de aanduiding 'karakteristiek' en ter plaatse van een monumentaal hoofdgebouw; […] g. woningsplitsing in twee woningen is uitsluitend toegestaan als de inhoud van het te splitsen pand meer dan 1.000 m³ bedraagt; h. woningsplitsing in 3 woningen is uitsluitend toegestaan als de inhoud van het te splitsen pand meer dan 1.500 m³ bedraagt;".
- Het plan is conserverend: "Nieuwe (grootschalige) ontwikkelingen worden in dit bestemmingsplan dan ook niet mogelijk gemaakt." (toelichting §3). Het bevat **geen KGO-regeling voor extra woningen**; extra woningen ontstonden tot eind 2023 via aparte partiële bestemmingsplannen (bijv. De Wesenberg 3, Gmb 2024, 93285; Steunenbergerweg 6) en ontstaan sinds 2024 via BOPA's.

**Provinciaal kader [PB]:** art. 4.11 (KGO), art. 4.4/4.5, de landbouwgebied-typologie (art. 4.123-4.124) en de **Lijst BOPA** (Prb 2024 nr. 1348): nieuwe woningen in de Groene Omgeving vragen een BOPA met provinciaal advies en provinciale instemming. Er is **geen provinciebrede KGO-rekenformule**.

**Raadsadvies bij een BOPA (nieuw, procedureel bepalend voor 10-12 woningen).** De raad heeft categorieën van BOPA's aangewezen waarvoor een **bindend advies van de raad** nodig is:

> "1. conform artikel 16.15a, lid b onder 10 van de Omgevingswet de volgende categorieën van gevallen van een buitenplanse omgevingsplanactiviteit aan te wijzen, waarvoor een bindend advies van de gemeenteraad nodig is: a. het bouwen van meer dan 12 woningen binnen de bebouwde kom en meer dan 3 woningen buiten de bebouwde kom; […] e. indien de activiteit niet past binnen door de gemeenteraad vastgestelde kaders en beleidsregels; […] Aldus besloten in de openbare raadsvergadering d.d. 7 februari 2022."

— Bron: CVDR704153 / Gemeenteblad 2023, 499448, https://lokaleregelgeving.overheid.nl/CVDR704153 (geraadpleegd 2026-10-04). B&W had "meer dan 5" voorgesteld; de raad maakte er "meer dan 3" van (raadsvoorstel zaak 38288-2021). Een CPO van 10-12 woningen buiten de bebouwde kom vraagt dus een **extra besluitmoment bij de raad**. Binnen de kom ligt de grens bij meer dan 12 woningen (voorbeeld: 't Kleiland Olst, 20 woningen, bindend advies 9-2-2026).

**Gemeentelijke KGO-uitwerking: "Handreiking KGO Gemeente Olst-Wijhe".** Collegebesluit (B&W 28-5-2024, adviesnota zaak 19805-2024, portefeuillehouder Hans Olthof), **geen raadsbesluit**, niet als beleidsregel gepubliceerd in Gemeenteblad of CVDR (de raad is geïnformeerd via de lijst ingekomen stukken):

> "BESLUIT burgemeester en wethouders 1. In te stemmen met de handreiking KGO gemeente Olst-Wijhe; 2. De raad te informeren door de handreiking te plaatsen op de lijst ingekomen stukken."

> "De handreiking is geldig totdat er nieuw, integraal beleid voor het landelijk gebied is opgesteld dat voort zal vloeien uit de omgevingsvisie." / "De handreiking is een tijdelijk instrument."

> "Dat wat in deze handreiking staat sluit grotendeels aan bij de huidige werkwijze en betreft dus geen herziening. Wel is sprake van een aanvulling in de vorm van de mogelijkheid voor woningsplitsing van niet-karakteristieke panden in het buitengebied. Dit komt voort uit de motie van de gemeenteraad […]."

— Bron: Handreiking KGO Gemeente Olst-Wijhe — Werken aan een leefbaar platteland, 28 mei 2024 (13 p.), https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/ba55b732-4944-450f-ab35-046ed41b697d en adviesnota B&W 28-5-2024 (geraadpleegd 2026-10-04/05). De verkorte publieksversie (12 p.) staat op https://mijnleefomgeving.olst-wijhe.nl/kgo-rood-voor-rood/kwaliteitsimpuls-groene-omgeving-kgo/kgo-handreiking-202407 ("202407" is de URL-slug; het document is gedateerd mei 2024). De motie woningsplitsing is van **13-11-2023**.

**Rekenregels (letterlijk, §3.1.1):**

> "• Voor het bouwen van 1 woning van maximaal 750 m3 moet minimaal 1.000 m2 landschapsontsierende bebouwing gesloopt worden.
> • Voor de bouw van 2 vrijstaande woningen van maximaal 750 m3 moet minimaal 2.000 m2 landschapsontsierende bebouwing gesloopt worden.
> • Voor de bouw van 2 woningen van samen maximaal 800 m3 in een aaneengesloten bouwblok moet minimaal 1.000 m2 bebouwing gesloopt worden.
> • Voor de bouw van 3 woningen van samen maximaal 1200 m3 in een aaneengesloten bouwblok moet minimaal 1.600 m2 gesloopt worden.
> • Er is een maximum van 2 bouwblokken (2 vrijstaande woningen of 2 blokken met woningen) voor wonen toegestaan per erf."

> "De woning(en) worden gebouwd op het eigen erf óf op een daarvoor geschikte locatie in of aan een kern óf in een bestaand bebouwingslint."

> "Een woning van 750 m3 mag maximaal uitgebreid worden tot 1000 m3. Hiervoor geldt dat voor elke m3 die wordt toegevoegd er 4 m2 aan schuren gesloopt moet worden."

> Woningsplitsing van niet-karakteristieke panden: "• Woningsplitsing in 2 woningen kan als de inhoud van het te splitsen pand meer dan 1.000 m³ is. • Woningsplitsing in 3 woningen kan als de inhoud van het te splitsen pand meer dan 1.500 m³ is." Daarnaast schuur-voor-schuur (1:2 tot 250 m² bijgebouwen) en bedrijf-voor-sloop (1:1 tot 250 m², 1:3 van 250 tot 850 m²).

> "Een andere mogelijkheid is een financiële compensatie voor de impact op de omgeving aan de Voorziening Ruimtelijke Kwaliteit (voorheen heette dit het landschapsfonds)." / "De instrumenten zijn dus nadrukkelijk niet bedoeld als verdienmodel."

— Bron: Handreiking KGO, p. 4-8 (geraadpleegd 2026-10-04/05). De Handreiking stelt **geen totaalmaximum** aan het aantal woningen: per bouwblok maximaal 3 woningen (1.200 m³) en maximaal 2 bouwblokken per erf (theoretisch circa 6 woningen); "locatie is maatwerk". Een waardemethode (oude/nieuwe waarde) staat er niet in; de term is "Voorziening Ruimtelijke Kwaliteit" (niet "Ruimtelijke Kwaliteitsprovisie"). Voor 10-12 woningen: "Het kan zijn dat u een ander idee hebt dan de mogelijkheden die hier worden genoemd. U kunt dan contact met ons opnemen om uw idee te bespreken." (p. 5) en "Het kan ook zijn dat een ontwikkeling niet wordt goedgekeurd." (p. 4).

De zin over "harde normering […] vervangen door kwalitatief maatwerk" komt niet uit de Handreiking maar uit de adviesnota Vettewinkelweg 2 (B&W 23-1-2024), die verwijst naar de gemeentelijke **Nota Ruimtelijke Kwaliteit** (datum en orgaan niet vastgesteld).

**De Handreiking wordt vervangen.** De bouwsteen Erfontwikkeling en -transformatie ("Vaststelling door college — November 2026", slide 6, raadssessie 28-9-2026) moet leiden tot "Actualisatie/vervanging van de Handreiking KGO" (slide 14). De houdbaarheid van de rekenregels is dus **kort**; het "recht" op een woning in ruil voor sloop is volgens de raadssessie "niet meer houdbaar".

**Provinciale kaartlagen voor de locaties (C1, C3).** De viewer https://ruimtelijkeplannen.overijssel.nl bevat de geconsolideerde Omgevingsverordening (in werking 1-7-2026; `nld@129`); de geometrische werkingsgebieden zijn per punt bevraagd (API `…/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044/_locationSearch?x=<RD-x>&y=<RD-y>&distance=1`), NNN, Natura 2000, grondwaterbescherming en Nationaal Landschap via de WFS van Geodata Overijssel (geraadpleegd 2026-10-05):

> "Artikel 4.123 (werkingsgebieden ontwikkelingsperspectieven landbouwgebieden) In Overijssel worden de volgende ontwikkelingsperspectieven landbouwgebieden aangewezen en als zodanig geometrisch begrensd: a. landbouwgebied met generieke opgaven en kansen; b. landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur."

| Locatie | Landbouwgebied (art. 4.123) | Grondwaterbeschermingszone | Afstand NNN | Afstand Natura 2000 |
|---|---|---|---|---|
| Elshof/Engeweg 8 en 10a (8 woningen) | **generiek** | nee | ≤ 3.000 m | ≤ 5.000 m |
| Vettewinkelweg 2 | **gebiedsspecifiek** | **ja** (Boerhaar) | ≤ 3.000 m | ≤ 5.000 m |
| Lierderholthuisweg 3 | generiek | nee | ≤ 2.000 m | ≤ 3.000 m |
| Steunenbergerweg 6 (Middel) | generiek | nee | ≤ 500 m | ≤ 5.000 m |
| Marle, Welsum (Erveweg 8, Kloosterhoekweg), Den Nul, Elshagenweg Wesepe | gebiedsspecifiek | nee | ≤ 100-2.000 m | ≤ 100-500 m (IJsselzone) |
| Kleistraat Olst, Bokkelerweg Wesepe, Prinshoeveweg | generiek | nee | ≤ 1.000-2.000 m | ≤ 2.000-10.000 m |
| Herxen (CPO 7a; Grolleman 63), Wijhe, Olst, Wesepe, Boskamp, Boerhaar, Zandhuisweg 7 | niet in landbouwgebied (kaartlaag "bebouwd gebied"/"bebouwde kom") | nee | ≤ 100-2.000 m | ≤ 250-2.000 m |

Aandeel in de gemeente (raster van 250 m, 1.883 punten; 118,4 km² incl. IJssel): landbouwgebied met generieke opgaven **37,8%** (ca. 44,5 km²); met gebiedsspecifieke opgaven **38,2%** (ca. 45,1 km²); geen van beide 24,1% (NNN 15,6%, kernen en buurtschappen, water); grondwaterbeschermingszone 5,3% (waarvan 71 punten in gebiedsspecifiek). Het agrarisch buitengebied is dus ongeveer half generiek, half gebiedsspecifiek. Natura 2000: alleen Rijntakken (IJsselzone) raakt de gemeente; geen punt valt in een Nationaal Landschap (IJsseldelta op 5-10 km van Marle). "Bebouwd gebied" op de kaart is de water-en-bodem-aanduiding van art. 4.13 en **niet** het "bestaand bebouwd gebied" van art. 4.5. De provincie typeert Herxen en Elshof in de Catalogus Gebiedskenmerken als "dorp of buurtschap".

**Gemeente en provincie hanteren bewust verschillende gebiedsindelingen:**

> "Bij het vaststellen van de gemeentelijke omgevingsvisie heeft de raad destijds gekozen voor bovenstaande gebiedsindeling en daarmee is bewust afgeweken van de gebiedsindeling zoals die in de Provinciale omgevingsvisie is vastgelegd. […] In de praktijk betekent dit dat het in bepaalde gebieden zo kan zijn dat we als gemeente ontwikkelingen toestaan, terwijl de provincie deze niet toestaat en andersom. In de bouwsteen zoeken we naar een oplossing om met deze verschillen om te gaan."

— Bron: Raadsinformatiebrief voortgang bouwsteen Erfontwikkeling, 9-6-2026, p. 1-2, en adviesnota B&W 23-6-2026 (zaak 24972-2026), iBabs (geraadpleegd 2026-10-04). **[INT]** Engeweg ligt gemeentelijk in het dekzandgebied ("ja, mits") maar provinciaal in **generiek** landbouwgebied (art. 4.124 lid 1: geen beperking voor omliggende landbouw); voor elke kandidaatlocatie moeten beide kaarten naast elkaar worden gelegd.

### (b) Gemeentelijke houding
- **Positief-voorwaardelijk bij kleinschalige erfontwikkeling** (Handreiking KGO, woningsplitsing) en bij dorpsuitbreiding aan kleine kernen en buurtschappen met lokale binding (Engeweg, Hemelrijk-2, CPO Herxen).
- **Terughoudend** in de IJsselzone (geen nieuwe woningen), in het kommenlandschap ("nee, tenzij": "Nieuwe woningen alleen in een uitzonderingssituatie: met duidelijke kwaliteitswinst, zonder belemmering van de landbouw", slide 10) en bij verspreide woningen in het buitengebied (zie §2: gemeente onderzoekt beperking; "villa hagelslag").
- **[INT]** In de praktijk onderscheidt de gemeente drie typen initiatieven buiten de grote kernen: (1) KGO-erf (sloop voor woning), (2) dorpsuitbreiding bij een kern of buurtschap via BOPA (Engeweg 8; Hemelrijk-2 circa 18; 't Kleiland 20 aan de rand van Olst), (3) CPO of lokaal initiatief in een kleine kern (Boerhaar, Herxen).

**Precedenten met agrarische bestemming (principebesluiten en vergunningen):**

| Dossier | Schaal | Stand | Rol provincie |
|---|---|---|---|
| **Engeweg, Elshof** (grondeigenaren Dijk en Schrijver) | **8 woningen** (3 twee-onder-een-kap = 6, plus 2 vrijstaand); dorpsuitbreiding, geen KGO | Principebesluit B&W 3-2-2026; BOPA nog niet aangevraagd/gepubliceerd (2026-10-04); op volgordelijst netcongestie (start 2027, projectrijpheid 6); in de provinciale Planmonitor als **harde** plancapaciteit (8, oplevering 2028) | "Ook de provincie heeft al ingestemd met voorliggend plan." (adviesnota p. 5); formele BOPA-instemming nog open |
| **Hemelrijk-2 / Erveweg, Welsum** (grondeigenaren) | circa 18 koopwoningen (2 vrijstaand, 4 twee-onder-een-kap, 12 rij) op grond met agrarische en volkstuinbestemming aan de rand van Welsum | Principebesluit B&W 10-3-2026 | Voorwaarde: "De ketenpartners van de gemeente (o.a. provincie, waterschap, omgevingsdienst, veiligheidsregio) in kunnen stemmen met het plan" |
| **'t Kleiland, Kleistraat Olst** (Holleman Ontwikkeling) | 20 woningen (5 sociale huur, 8 sociale koop, 7 vrij) op grond met functie 'Agrarisch', binnen de bebouwde kom; provinciale kaart: generiek landbouwgebied en kernrandzone | Principebesluit B&W 7-1-2025; aanvraag 19-12-2025; raad: positief bindend advies 9-2-2026; BOPA-vergunning B&W 17-3-2026 (Gmb 2026, 130739; ca. 12 weken); Planmonitor hard (20) | Voorwaarde in het principebesluit: "De provincie akkoord gaat met de ontwikkeling;" (B&W 7-1-2025); het instemmingsstuk zelf is niet gepubliceerd |
| **Zandhuisweg 7, Wijhe** | 9 woningen (3 vrijstaand, 4 onder één kap, boerderij gesplitst in 2) | BOPA-aanvraag 6-11-2025, vergunning 25-11-2025 (regulier); Planmonitor hard (9); kaart: binnen "bebouwde kom" van Wijhe, dus kernrandlocatie [INT] | Niet in bekendmaking vermeld |
| **Steunenbergerweg 6, Olst** (Middel) | 7 woningen op een voormalig agrarisch erf (achtererf + splitsing boerderij) | Bestemmingsplan raad 26-2-2024 zonder zienswijzen; "Het bestemmingsplan wordt voor vooroverleg naar de provincie Overijssel gestuurd." | Vooroverleg |
| **Lierderholthuisweg 3, Wijhe** | splitsing karakteristieke woning + 1 extra woning na sloop (856 m² gesloopt, 198 m² hergebruikt) + 1,5 ha bos; KGO | Principebesluit 20-1-2026; aanvraag 7-4-2026; **vergunning verleend 23-6-2026** (Gmb 2026, 302246; ca. 11 weken) | Beplantingsplan door provincie en gemeente akkoord bevonden; provinciale instemming met de BOPA niet vermeld |
| **Vettewinkelweg 2, Wijhe** | 1 extra woning na sloop 1.174 m²; KGO | Principebesluit 23-1-2024; overeenkomst 30-9-2024; aanvraag 24-12-2024; **vergunning 7-4-2025** (Gmb 2025, 154624; ca. 15 weken) | "Het plan is in het kader van vooroverleg voorgelegd aan de provincie, waarbij zij hebben aangegeven in te kunnen stemmen met deze herontwikkeling." |
| **CPO Herxen** (onbebouwd perceel achter Herxen 7a) | 3 woningen | Principebesluit B&W 2-6-2026 | Bestuursovereenkomst GS-B&W (zie hieronder) |
| **Grolleman, Herxen 63** | 15 woningen (9 grondgebonden, 6 appartementen) op voormalig bedrijfsterrein | Principebesluit B&W 23-9-2025 (BOPA); Planmonitor zacht | "Ook de provincie heeft aangegeven dat ze positief is over de verandering van bedrijvenlocatie naar woningbouw." |

— Bronnen: B&W-besluitenlijsten 20-1-2026, 3-2-2026, 10-3-2026, 17-3-2026, 2-6-2026, 23-9-2025, 23-1-2024 (https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten); adviesnota's Engeweg (zaak 41952-2025), Lierderholthuisweg 3 (zaak 51610-2025), Vettewinkelweg 2 (zaak 30712-2023); Gemeenteblad 2025, 1450, 154624, 486680, 514083; 2026, 169650, 273043, 302246; toelichting NL.IMRO.1773.BP2023001099-0301; provinciale Planmonitor (WFS Geodata Overijssel, peildatum 1-1-2026) (geraadpleegd 2026-10-04/05). Vettewinkelweg 2, letterlijk: "Er moet toestemming worden verkregen van de provincie voor deze herontwikkeling, omdat er een provinciaal belang is." (adviesnota p. 1 en 3). Engeweg, letterlijk: "In principe (en onder voorwaarden) medewerking verlenen aan het verzoek tot wijziging van de functie van agrarisch naar wonen en realisatie van 8 woningen (3 tweekappers en 2 vrijstaande) conform inrichtingsschets met als doel kopers te vinden met een binding met de Elshof; […] BOPA […] anterieure overeenkomst […] In te stemmen met een verkleining van de normafstand met betrekking tot spuitzonering op basis van het opgestelde locatiespecifiek onderzoek." Engeweg: "Het verzoek is in strijd met het Omgevingsplan Olst-Wijhe, waarin de functie 'Agrarisch' geldt." Een formeel provinciaal instemmingsbesluit is in geen register gepubliceerd (het Provinciaal blad publiceert dat niet).

**Provinciale instemming in de principebesluiten 2024-2026.** In de B&W-besluitenlijsten 9-1-2024 t/m 22-9-2026 (volledig doorzocht) staat in minstens 13 principebesluiten een provinciale voorwaarde, o.a.:

> "Er moet toestemming worden verkregen van de provincie voor deze herontwikkeling, omdat er een provinciaal belang is." (Vettewinkelweg 2, 23-1-2024; idem Prinshoeveweg 1 en Boerlestraat 8-8a, 23-4-2024; Gravenweg 13 en Kloosterhoekweg 3, 17-12-2024)

> "De provincie akkoord gaat met de ontwikkeling;" (Herxen 77/77a, 11-6-2024; 't Kleiland, 7-1-2025) / "De provincie kan instemmen met deze herontwikkeling." (Diepenveenseweg 17, 8-7-2025; Kletterstraat, 26-8-2025) / "De provincie kan definitief instemmen met deze herontwikkeling." (Kappeweg 1A, 7-10-2025)

— Bron: B&W-besluitenlijsten, https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten (archive.csv; geraadpleegd 2026-10-04). Het patroon: in 2024 bijna altijd "toestemming provincie (provinciaal belang)", vanaf medio 2025 "provincie kan instemmen"; bij Boerhaarseweg 4 (16-10-2025) en Grolleman (23-9-2025) staat geen voorwaarde in het besluit. Dat bewijst niet dat de provincie niet betrokken is (de Lijst BOPA geldt voor alle nieuwe woningen in de Groene Omgeving [PB]); de besluitenlijsten zijn geen betrouwbare maat. Alle gevonden BOPA's voor wonen in het buitengebied zijn verleend; een geweigerde BOPA of onthouden instemming is niet gevonden. Het Provinciaal blad (69 treffers op "Olst-Wijhe", 2023-2026, ook gecontroleerd op "reactieve interventie") bevat geen zienswijze, aanwijzing of onthouden instemming; instemmingen en vooroverlegreacties worden daar niet gepubliceerd.

**Bestuursovereenkomst Herxen (B&W 2-6-2026, punt 08):**

> "In te stemmen met bijgaande bestuurlijke afspraken tussen het college van B&W van de gemeente Olst-Wijhe en Gedeputeerde Staten van de Provincie Overijssel […] Om de groei van Herxen in goede banen te leiden is op aangeven van de provincie Overijssel een bestuursovereenkomst voorbereid. Deze overeenkomst ziet op het op voorhand in procedure kunnen brengen van ruimtelijke initiatieven zoals het CPO Herxen in afwachting van een visietraject. Dit visietraject heeft betrekking op hoe woningbouw in Herxen moet gaan landen in de periode tot 2050."

— Bron: B&W-besluitenlijst 2-6-2026 (gepubliceerd 5-6-2026), https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten (geraadpleegd 2026-10-04). Wethouder Blind: "Wat ons betreft kan Herxen de komende jaren met gemiddeld zo'n 2 tot 4 woningen per jaar groeien. Om te voorkomen dat er her en der plukjes woningen worden gebouwd, gaan we samen met de provincie én de inwoners van Herxen kijken waar woningbouw kan komen en waar niet." (gemeentebericht 2-6-2026, "Gezamenlijke visie voor woningbouw in Herxen"; de losse URL geeft 404, tekst ook op https://wijhecity.nl/2026/06/02/gezamenlijke-visie-voor-woningbouw-in-herxen/). De afspraken zelf zijn niet openbaar teruggevonden (bijlage; €15.000 uitvoeringskosten 2026). Herxen: Plaatselijk Belang kreeg verzoek van de provincie om de woonparagraaf van de dorpsvisie te actualiseren (herxen.nl, 22-9-2026).

**Buurtschappenbeleid (Elshof en Herxen)**, gepubliceerd beleidsregel (CVDR638025, B&W 18-2-2020):

> "Nieuw beleid (beleidsregel) / […] Nadere toetsingscriteria: 1.Aanvrager dient een starter, doorstarter of senior te zijn en een bijzondere binding met het buurtschap te hebben. 2.Bouwen alleen in het lint aangegeven op bijgevoegde kaart."

> "Punt 2 aangaande het te stellen maximum per jaar is niet realistisch, omdat dit bijvoorbeeld de mogelijkheid blokkeert dat enkele starters gezamenlijk gaan bouwen. Dergelijke drempels zijn niet wenselijk."

— Bron: Notitie Buurtschappenbeleid, Gemeenteblad 2020, 63767, https://zoek.officielebekendmakingen.nl/gmb-2020-63767.html (geraadpleegd 2026-10-04). Het beleid (provinciaal concept 2004; lokaal 2007, 2010, 2020) staat **individuele lintwoningen met binding** toe; Engeweg (8 woningen) valt er niet onder en loopt via BOPA als dorpsuitbreiding. Het precedent Elshof 6c-e (3 starterswoningen op agrarisch perceel, raad 19-9-2022) is gebaseerd op dit beleid.

### (c) Stappenplan (indicatief; praktijk uit register en besluiten)
Provinciale stappen: [PB] §4 (voorkantsamenwerking, Omgevingstafel, Lijst BOPA, kennisgeving). Lokaal toegepast (Handreiking KGO p. 10-11, B&W-besluiten):
1. **Conceptverzoek** bij de gemeente (https://www.olst-wijhe.nl/vooroverlegomgevingsvergunning; leges € 306, zie §11), intaketafel (mogelijk wachtlijst) en gemeentelijke omgevingstafel; voor erven de ervenconsulent van Het Oversticht.
2. **Regionale Omgevingstafel IJsselland** "in sommige gevallen" (ketenpartners waaronder de provincie en het waterschap; https://www.odijsselland.nl/over/omgevingstafel). Volgens die pagina bepaalt de gemeente of de tafel nodig is, behandelt de tafel initiatieven in een vroege fase met twee of meer ketenpartners en een significante impact, en "kan en mag" de initiatiefnemer zelf aanwezig zijn; de tafel heeft "geen rol in de fase van vergunningverlening". De Handreiking KGO (stap 4) en de Koers team landelijk gebied ("Intaketafel en Omgevingstafel") nemen de tafel op in de eigen werkwijze; hoeveel Olst-Wijhese dossiers er in 2024 zijn behandeld, is niet verifieerbaar (het jaarverslag 2024 van de OD noemt alleen 29 projecten voor alle deelnemers samen). **Vooroverleg met de provincie vóór het gemeentelijk principebesluit** (Vettewinkelweg 2).
3. **Principebesluit B&W** met voorwaarden (ETFAL/evenwichtige toedeling van functies, anterieure overeenkomst, erfinrichtingsplan, participatieverslag, nadeelcompensatie; bij Engeweg ook spuitzone-onderzoek).
4. **Anterieure overeenkomst** vóór start van de formele procedure (Gemeenteblad publiceert de zakelijke beschrijving, zie §11).
5. **Bindend raadsadvies** bij een BOPA voor meer dan 3 woningen buiten de bebouwde kom (kosten € 521,70) of bij strijd met raadskaders.
6. **BOPA-aanvraag** (regulier, bezwaar mogelijk) met provinciaal advies/instemming (Lijst BOPA) [PB]; of omgevingsplanwijziging (raad) voor kernuitleg.
7. Omgevingsvergunning bouw; netcongestie-prioritering (zie §5).

**Doorlooptijden uit de registers:** Zandhuisweg 7 (9 woningen) aanvraag 6-11-2025 → vergunning 25-11-2025 (ca. 3 weken); Lierderholthuisweg 3 aanvraag 7-4 → vergunning 23-6-2026 (ca. 11 weken; principebesluit 20-1-2026, totaal ca. 5 maanden); Vettewinkelweg 2 aanvraag 24-12-2024 → vergunning 7-4-2025 (ca. 15 weken; principebesluit tot vergunning ca. 14,5 maanden); 't Kleiland (20 woningen, met raadsadvies) aanvraag 19-12-2025 → vergunning 17-3-2026 (ca. 12 weken). Dit zijn de gepubliceerde looptijden van aanvraag tot besluit; de voorfase (vooroverleg, principebesluit, overeenkomst) komt erbij. Een totale doorlooptijd voor 10-12 woningen is niet gevonden; een schatting van 12-24 maanden is **[INT]**.

### (d) Kansrijk versus kansarm [INT, gebaseerd op bovenstaande bronnen en [PB]]
- **Kansrijker:** bestaand erf met te slopen bebouwing; locatie in of aan een kleine kern of buurtschap met aantoonbare lokale behoefte en binding (Elshof, Herxen, Welsum, Boskamp, Boerhaar); dekzandgebied ("ja, mits"); aansluiting bij het gemeentelijke "zoekgebied erfontwikkeling" (kernranden); betaalbaar en geclusterd wonen voor starters en kleine huishoudens; inbreiding/transformatie vóór uitbreiding; ligging in provinciaal **gebiedsspecifiek** landbouwgebied biedt ruimte voor een kwaliteitsinvestering gericht op water, klimaat en natuur [PB]; vooroverleg en bestuursovereenkomst met de provincie (Herxen).
- **Kansarm:** onbebouwde agrarische grond in het open buitengebied; IJsselzone (Natura 2000-Rijntakken, waterveiligheid; "nauwelijks ontwikkelingen op erfniveau mogelijk"); kommenlandschap ("nee, tenzij"); locaties die omliggende landbouw beperken; **spuitzone van 50 meter** rond agrarische percelen (afwijking alleen met locatiespecifiek onderzoek en informatieplicht: Engeweg 30 m op drie zijden "reëel risico"; Kloosterhoekweg 3, B&W 21-4-2026); grondwaterbeschermingsgebied Boerhaar (Vettewinkelweg); verspreide grote woningen ("villa hagelslag"); netcongestie (zie §5); aanvraag voor 10-12 woningen buiten de kom die bindend raadsadvies en provinciale instemming vraagt.

### (e) Eindoordeel per schaalscenario [INT]
| Scenario | Inschatting |
|---|---|
| 1-3 woningen op bestaand erf (Handreiking KGO) | **Haalbaar** binnen bestaand beleid (Lierderholthuisweg 3, Vettewinkelweg 2: BOPA met provinciale toets, 11-15 weken). **Houdbaarheid kort**: de Handreiking wordt in november 2026 vervangen; het recht op een woning in ruil voor sloop is "niet meer houdbaar" |
| 4-8 woningen aansluitend aan een buurtschap of kleine kern | **Maatwerk, precedent aanwezig.** Engeweg (8; principebesluit 2026; provincie in vooroverleg ingestemd; Planmonitor hard); Steunenbergerweg 6 (7 op een erf, 2024); Elshof 6c-e (3, 2022). Raadsadvies vereist (> 3 buiten de kom). Lokale binding en spuitzone beslissend |
| 10-12 woningen op bestaand erf in het open buitengebied | **Kansarm.** Buiten de Handreiking (circa 6 per erf in theorie) en buiten elk kleinschalig regime; BOPA met bindend raadsadvies en provinciale instemming; alleen als gebiedsgerichte transformatie (bouwsteen/gebiedsvisie, art. 4.124 lid 4 [PB]). Twee initiatieven van 12 woningen staan op de volgordelijst netcongestie (De Brinkweiden, Kappeweg 18, "Buitengebied"; Wijlandhof, Elshof), maar hun inhoud en status zijn onbekend |
| 10-12 woningen op onbebouwde agrarische grond buiten een kern | **Zeer kansarm.** Art. 4.4 (overige kern), art. 4.5 lid 2, landbouwgebied-typologie [PB]; gemeentelijke lijn: "Nieuwe woningen horen zoveel mogelijk in en aan de randen van de kernen, niet (meer) verspreid in het buitengebied" |
| 10-12 woningen aansluitend aan een **kleine kern** (Welsum, Herxen, Boskamp, Den Nul, Boerhaar) als CPO of lokaal initiatief | **Reële route met voorwaarden.** Omgevingsvisie: "We staan open voor […] CPO" (p. 24); precedenten Hemelrijk-2 (circa 18, agrarische bestemming, principebesluit 2026), CPO Boerhaar (circa 22-24, kern), CPO Herxen (3). Beperkingen: indicatieve groei 5-10% tot 2050, "inbreiding voor uitbreiding", lokale binding, provinciale instemming, bindend raadsadvies, netcongestie |
| 10-12 woningen aansluitend aan een **grote kern** (Olst, Wijhe, Wesepe) als uitleg/CPO | **Meest kansrijke route, maar op gemeentegrond of bij gebiedsontwikkeling.** Via woningbouwprogrammering en omgevingsplanwijziging; CPO-spoor bestaat (Klimboom, Olstergaard, Boerhaar); Wesepe heeft uitbreidingspotentie ("hogere dekzandgronden"); art. 4.5 lid 1 en redeneerlijn [PB]; kavelwinkel leeg; netcongestie en Woondeal |

**Concrete vervolgstap:** een conceptverzoek bij team Ruimtelijke Realisatie/Ruimte en Samenleving (leges € 306; principebesluit € 1.225, zie §11), gecombineerd met een gesprek met **wethouder Marcel Blind** (wonen, ruimtelijke ordening en omgevingsplannen; kernenwethouder Olst, Eikelhof, Herxen, Middel) en **wethouder Hans Olthof** (toekomstbestendige kernen en buitengebied, grondbeleid, gebiedsgerichte aanpak; kernenwethouder Wesepe, Elshof, Marle, Welsum), en de ervenconsulent van Het Oversticht of de Erfcoach Overijssel (zie §4, §9).

---

## 4. VAB-beleid (Vrijkomende Agrarische Bebouwing)

**Geen apart gepubliceerd VAB-beleid (CVDR/Gemeenteblad).** VAB loopt via (1) het Bestemmingsplan Buitengebied/omgevingsplan (aantal woningen mag niet toenemen, art. 3.9.5 onder p), (2) de Handreiking KGO (woning-voor-schuur, schuur-voor-schuur, bedrijf-voor-sloop, woningsplitsing), (3) de Omgevingsvisie (sloopmeters VAB "elders in de gemeente […] rondom de kernen en buurtschappen") en (4) de **bouwsteen Erfontwikkeling en -transformatie**.

**Bouwsteen Erfontwikkeling en -transformatie:**
- *Plan van aanpak* (B&W 28-10-2025, adviesnota zaak 41596-2025):

  > "In spoor 1 van de routekaart geeft de provincie een subsidiemogelijkheid voor ondersteuning aan gemeenten ten behoeve van een gemeentelijke bouwsteen VAB en Erftransformatie én de mogelijkheid om een intergemeentelijk VAB- of Erftransformatieprogramma op te stellen." / "Zowel de gemeente Raalte als de gemeente Deventer neemt deel aan de subsidieregeling van de provincie. Als gemeente Olst-Wijhe ook meedoet, vergroot dat de kansen voor het samenwerken in de toekomst." / "Vanuit de subsidieregeling van de provincie wordt € 30.000,- van de benodigde € 40.000,- beschikbaar gesteld."

  — Bron: B&W-besluitenlijst 28-10-2025, punt 7, adviesnota (geraadpleegd 2026-10-04). Olst-Wijhe **doet dus mee aan de provinciale subsidieregeling** (activiteit A, gemeentelijke bouwsteen). Het regelnummer "4.39" wordt in de adviesnota niet genoemd; de Koers team landelijk gebied (B&W 4-11-2025, p. 13) bevestigt het bedrag ("Voor het opstellen van de bouwsteen VAB en Erftransformatie verwachten we een subsidie van € 30.000,- van de provincie […] volledig ingezet […] voor het inhuren van een bureau"). € 30.000 is het maximum van activiteit A in [PB] §3.1, wat de regeling als 4.39 activiteit A identificeert [INT, hoge zekerheid]. Raalte en Deventer nemen deel; of een intergemeentelijk programma (activiteit B/C) komt, was "voor eind 2026" nog open. De regeling stond op 2026-10-05 nog open ("U kunt aanvragen totdat het budget bereikt is.", https://regelen.overijssel.nl/Producten_en_diensten/Subsidies/Wonen_en_leefbaarheid/Beleid_transformatie_agrarische_bebouwing_erven_en_gronden); er is geen openbare lijst van deelnemende gemeenten. Het bestuursakkoord (p. 21) zegt dat deelname aan regionale samenwerkingsverbanden "kritisch beoordeeld" wordt.
- *RIB voortgang* (B&W 23-6-2026, adviesnota zaak 24972-2026; RIB 9-6-2026):

  > "In de IJsselzone (onderdeel van N2000-gebied Rijntakken), zijn nauwelijks ontwikkelingen op erfniveau mogelijk vanwege beperkingen die daar gelden in verband met waterveiligheid. In het kommenlandschap geven we voorrang aan de landbouw, wat betekent dat er op erven minder ruimte is voor ontwikkelingen die de landbouw kunnen belemmeren. Denk hierbij aan woningbouw en andere gevoelige functies […]. In het dekzandlandschap geven we meer ruimte voor het ontwikkelen van andere functies op erven. Daarnaast geven we invulling aan de overgangszone rond de kernen […]." / "Vaststelling van de bouwsteen is beoogd in november van dit jaar door het college."

  — Bron: https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/2026/6/29/b-amp-w-besluiten-23-06-2026/voortang-proces-bouwsteen.pdf (geraadpleegd 2026-10-04)
- *Raadssessie 28-9-2026*: zie §2 en §3a (Handreiking vervangen; "recht op woning" niet meer houdbaar; zoekgebied kernranden; verevening). Uit te werken: voorwaarden voor woningbouw in het buitengebied, beoordelingssystematiek, schuifrechten/sloopmeters, vereveningsfonds, juridische doorwerking in programma en omgevingsplan.
- *Koers team landelijk gebied* (B&W 4-11-2025) erkent een verschil in wetenschappelijk kader tussen gemeente (Sponsstrategie) en provincie ("Agrarisch Overijssel 2050").

**Provinciaal ontwerp-Volkshuisvestingsprogramma Overijssel** (GS 30-6-2026; Prb 2026, 11834; titel 2026-2035, artikeltekst 2026-2032) over VAB en collectieve woonvormen: "in sommige gevallen kan ook transformatie van vrijkomende agrarische bebouwing een kans bieden, mits deze in de directe nabijheid van een dorp ligt." en "Collectieve woonvormen passen hier goed bij: ze versterken de sociale cohesie én helpen de lokale woningvraag te vervullen." — Bron: https://zoek.officielebekendmakingen.nl/prb-2026-11834.html (geraadpleegd 2026-10-04). Het noemt Olstergaard als voorbeeld. (Relevant voor [PB] §6.1.)

**Subsidie 4.39, plafond:** "4.39 Beleid transformatie agrarische bebouwing, erven en gronden / Het subsidieplafond voor 2025 en 2026 is in totaal samen: € 1.640.250,-" (Prb 2025, 17002). Toekenningen per gemeente worden niet in het Provinciaal blad gepubliceerd; voor Olst-Wijhe is geen beschikking gevonden (vindplaats: vab@overijssel.nl; B&W-besluiten).

**Erfcoach (D2):** de gemeente verwees in 2025 naar twee erfcoaches ("In het buitengebied van Olst-Wijhe staan erfcoaches Yvonne In 't Veld en Niek Oude Scholten klaar", gemeentebericht 15-9-2025). De actuele lijst vermeldt:

> "Yvonne in 't Veld – Erfcoach – Werkzaam in de gemeenten: Dalfsen, Olst-Wijhe, Ommen en Hardenberg. Mobiel Telefoonnummer: 06 10 98 22 76 – Mail direct: ygw.in.t.veld@overijssel.nl"

— Bron: https://erfcoachoverijssel.nl/contact-met-de-erfcoaches/ (geraadpleegd 2026-10-04); Niek Oude Scholten staat niet meer op die lijst (het eerdere concept noemde hem op grond van een 2024-bericht). Daarnaast verwijst de gemeente naar een ervenconsulent van Het Oversticht (https://www.olst-wijhe.nl/ervenontwikkeling). De Kracht van Salland organiseert op 8-10-2026 de avond "Grond voor toekomst in Salland" voor grondeigenaren (gemeente, 23-9-2026). Gebruik van Atelier Overijssel/Rijkshandreiking: niet gevonden.

**Precedenten:** zie §3b (Vettewinkelweg 2, Lierderholthuisweg 3, Steunenbergerweg 6, Engeweg, Hemelrijk-2); verder Kloosterhoekweg 3 Welsum (2 woningen, rood-voor-rood, vergunning 12-5-2026), Bokkelerweg 1 Wesepe en Engeweg 10/10A (KGO-splitsing), LBV/LBV+-trajecten Marledijk 33/31a, Boerlestraat 8 en Prinshoeveweg 1 (Gmb 2026, 363854) en tientallen anterieure overeenkomsten voor buitengebiedlocaties 2024-2025 (zie §11). Geen collectief/cohousing-precedent op een VAB-erf in Olst-Wijhe gevonden (BuitenDelen in Lettele ligt in gemeente Deventer [PB]).

**Salland Loont/Gebiedsarrangement Salland:** B&W 28-10-2025, punt 10: de raad nam op 30-6-2025 unaniem de motie "Salland Loont" aan; "We hebben als gemeente vorig jaar 17.000 euro aan Salland Loont toegekend voor het opstarten van de organisatie. Ook Raalte en Deventer hebben dit bedrag […] doen toekomen. Vanuit ons gemeentelijke fonds ruimtelijke kwaliteit hebben we daarnaast eenmalig een bijdrage van 75.000 euro toegezegd […]." (geraadpleegd 2026-10-04).

---

## 5. Grondbeleid

**Nota Grondbeleid inclusief Grondprijsbeleid 2023-2026** (CVDR691005, Gemeenteblad 2023, 16454): **vastgesteld door de raad op 12-12-2022** (besluitenlijst raadsvergadering 12-12-2022: "12. Voorstel tot het vaststellen van de Nota Grondbeleid 2023-2026 en intrekking van de Nota Grondbeleid 2018-2021. Zonder hoofdelijke stemming gaat de raad akkoord met het voorstel"); in werking 17-1-2023. De nota is gedateerd 8-11-2022 (zaaknummer 51287-2022; B&W-voorstel). Een nota "2024-2028" bestaat niet voor Olst-Wijhe. De nota loopt **eind 2026 af**; een opvolger is niet gevonden. Bron: https://www.olst-wijhe.nl/notagrondbeleid2023-2026 en https://lokaleregelgeving.overheid.nl/CVDR691005 (geraadpleegd 2026-10-04).

> "De gemeente Olst-Wijhe kiest er daarom voor om situationeel grondbeleid toe te passen. Dit betekent dat per initiatief/ontwikkeling wordt gekozen welke vorm van grondbeleid door de gemeente wordt gehanteerd: actief en/of faciliterend. […] Situationeel grondbeleid geeft ruimte aan initiatieven en experimenten die een bijdrage leveren aan de ontwikkeling van onze gemeente […]"

> "Beleidskeuze 2: De gemeente streeft er naar om, alvorens de planologische procedure wordt gestart, overeenstemming te bereiken met de initiatiefnemer door middel van het sluiten van een anterieure overeenkomst en geeft daarmee niet de voorkeur aan een exploitatieplan."

> "Ad d. Vrije kavels (particulier opdrachtgeverschap): […] Bij verkoop van een groter gebied, al dan niet projectmatig, kan het college beargumenteerd besluiten een korting te geven op de grondprijs. Dat kan met name aan de orde zijn als er sprake is van innovatieve initiatieven die maatschappelijk gezien wenselijk zijn en waarbij in één keer een grote hoeveelheid grond wordt afgenomen."

> "Onder voorbehoud van goedkeuring door het college, kan erfpacht wel als alternatief ingezet worden voor uitgifte van gronden." (p. 25)

**Erfpacht, actueel standpunt:**

> "Gezien de nadelen die kleven aan het instrument erfpacht en de alternatieve instrumenten die we nu inzetten, is het college geen voorstander van het invoeren van erfpacht." / "De lokale cultuur in de gemeente Olst-Wijhe kenmerkt zich […] voornamelijk door eigen bezit, zowel voor wat betreft de woning als de grond."

— Bron: Raadsinformatiebrief 10-11-2025 (zaak 45292-2025, toezegging 55), iBabs (geraadpleegd 2026-10-04). Een gemeentebericht van 20-8-2025 ("voornemen tot uitgifte gemeentegrond in erfpacht", https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/2025/8/20/voornemen-tot-uitgifte-gemeentegrond-in-erfpacht) is niet gelezen; erfpacht is voor woningbouwkavels volgens de RIB geen werkend instrument.

**Grondprijzenbrief 2026** (Grondprijzenbrief 2026, 26-1-2026, nummer 40028-2025; **vastgesteld door B&W op 17-2-2026**), https://www.olst-wijhe.nl/bestuur/visies-beleid-en-regelgeving/wonen-en-leven/wonen/grondprijzenbrief/grondprijzenbrief-2026 (geraadpleegd 2026-10-04):

> "3.1.3. Particulier opdrachtgeverschap (vrije sector kavels): […] De minimale grondprijs bedraagt € 280 per m² en de bovengrens bedraagt € 450 per m². Bij grotere kavels kan, met oog op marktconformiteit, een gestaffelde prijsvorming worden gehanteerd." (p. 18)

Overig (tabel p. 5): sociale koop I vanaf € 230/m² (prijspeil 2026 v.o.n. < € 267.000), betaalbaarheidsgrens "< € 420.000 (= begrenzing 2026)", retributie opstalrecht 4% van de grondwaarde. De eerder in het concept genoemde bedragen (rijwoning € 200/m², vrije kavels € 250/m²) komen **niet** in de brief voor en zijn verwijderd. De brief geldt voor **uitgifte van gemeentegrond**; voor een CPO op eigen agrarische grond geldt kostenverhaal via een anterieure overeenkomst (§11).

**Actueel kavelaanbod:** de kavelwinkel meldt op 2026-10-05: "Op dit moment zijn er geen kavels te koop." **De Klimboom, Boskamp:** 17 woningen (9 CPO, 4 sociale huur, 4 via inschrijving); in april 2026 stonden 4-5 betaalbare woningen open voor aannemers, ontwikkelaars en CPO-groepen (inschrijving 10-4 t/m 1-5-2026; loting); uitkomst niet gevonden.

**Grote ontwikkellocaties met gemeentelijke grondpositie:**
- **Olst Zuid** (circa 90 woningen; actief grondbeleid; aankoop 2023; B&W 4-2-2025: voorbereidingskrediet € 165.000; netcongestielijst start 2030): CPO-reservering niet gevonden. Olst krijgt "ongeveer 450 woningen" van het programma.
- **Boerhaar** (CPO, circa 22-24 woningen): actief grondbeleid; zie §6.
- IJsseldal Wesepe (81 woningen; TAM-omgevingsplan hoofdstuk 22a; 7 sociale huur, 16 goedkope koop circa € 250.000, 32 betaalbare koop circa € 405.000, 26 hoog segment), Wengelerhoek Wijhe (186 woningen in fase 1, raad 26-5-2026), Wijhe Noord (circa 300), scholenlocaties Olst (59) en Wijhe (Mijnpleinschool/Matzer circa 44 sociale huur), Holsthoek Den Nul (19; raadsbesluit gepland 7-9-2026, uitkomst niet gevonden), Kleistraat/'t Kleiland (20).
- Gemeentelijke grondposities in het buitengebied: niet gevonden.

**Plancapaciteit en tempo:**
- Provinciale Planmonitor (dataset "Harde en zachte woningbouwplannen (vlakken)", peildatum 1-1-2026; WFS Geodata Overijssel, 37 vlakken; geraadpleegd 2026-10-05): voor locatiebekende plannen **hard 244 en zacht 770** woningen "nog te bouwen vanaf 2026". De laag zegt zelf dat de totale plancapaciteit niet uit dit bestand kan worden afgeleid. Voorbeelden: Engeweg Elshof (hard, 8), Zandhuisweg 7 (hard, 9), 't Kleiland (hard, 20), Grolleman Herxen (zacht, 15); het **CPO Herxen en CPO Boerhaar staan er niet in**. Het gemeentelijke cijfer "161/339 woningen plancapaciteit" uit het eerdere concept is in geen enkele bron teruggevonden en is verwijderd.
- Tempo: "In de onderzoeksperiode [2020-2024] zijn er 525 nieuwbouwwoningen opgeleverd. Dit zijn gemiddeld ongeveer 105 woningen per jaar." (RIB 2-12-2025); "bijna 450 woningen" in de bestuursperiode 2022-2026 (bestuursakkoord p. 6); "ruim 70 woningen" in 2025 (jaarrekening, gemeentebericht 29-5-2026); [PB] §1.5: 417 gerealiseerd Q1 2022-Q4 2024. Ambitie: 1.000-1.200 woningen in tien jaar ("tot 2032"; het bestuursakkoord noemt "tot en met 2031"); "+400" betekent "gemiddeld 100 woningen per jaar er bij, dus in totaal zo'n 400 nieuwe woningen" in 2026-2030 (akkoord p. 8), geen extra opgave.
- **Woondeal West-Overijssel** (Actualisatie 20-3-2025): bijlage 1 noemt voor Olst-Wijhe 435 (woondeal 2022), 841 (2024-eind 2030) en 300 (doorkijk) woningen over acht projecten; de gemeente telt vier sleutelprojecten (MEKO-terrein Wesepe, Wijhe Noord, scholenlocaties Wijhe, Olst Zuid). Over de extra opgave:

  > "Volgens de actuele Woondeal kan er in West-Overijssel een extra opgave ten opzichte van 2022 landen in de gemeenten Deventer, Hardenberg, Raalte, Staphorst en Olst-Wijhe. De nieuwe Woondeal betekent geen extra woningbouwopgave voor onze gemeente, omdat wij met onze Focus op Wonen (raadsbesluit 2022) al stevig hebben ingezet op het aantal nieuwe woningen, namelijk 1000-1200 woningen tot 2032."

  — Bron: B&W-besluitenlijst 8-4-2025 (geraadpleegd 2026-10-04); Woondeal p. 5: "[…] In een aantal van deze gemeenten (zoals Deventer, Hardenberg, Olst-Wijhe en Raalte) wordt zelfs onderzocht of er, bovenop de huidige programmering, kansen zijn om extra woningen te bouwen." (https://overijsselsewoonaanpak.nl/media/xhadtdva/20250325_524100_woondeal-west-overijssel-digitaal-toegankelijk.pdf). Beide uitspraken kloppen dus naast elkaar.
- Ruimte binnen de 80/20-richtlijn en een bewuste reservering voor initiatieven van derden: **niet gevonden** (vindplaats: Woondeal bijlage 1, Planmonitor/Dashboard Wonen, 1-op-1-gesprek provincie-gemeente-corporaties).

**Netcongestie (relevant voor elk woningbouwproject).** Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten gemeente Olst-Wijhe 2026: **Gemeenteblad 2026, 385444 / CVDR765519** (B&W 11-8-2026, in werking 14-8-2026). Het eerder genoemde gmb-2026-415179 is van Brunssum en gmb-2026-421329 van Lansingerland.

> "Artikel 5 […] 2. Het in het eerste lid bedoelde verzoek kan worden ingediend tot en met 27 augustus 2026 / 3. Opname van een project op de volgordelijst resulteert in een inspanningsverplichting van de gemeente […] zonder dat de gemeente de beschikbaarheid of toewijzing van prioritering en transportcapaciteit garandeert."

> "Artikel 9. Rangordebepaling volgordelijst […] Stap 1: start bouw / […] een project [wordt] hoger gerangschikt als de bouw eerder start. […] Stap 2: projectrijpheid […] 1 Er is een civielrechtelijke overeenkomst, en een onherroepelijk omgevingsvergunning voor een bouwactiviteit […] 2 […] onherroepelijk omgevingsplan of […] BOPA […] 3 Er is alleen een onherroepelijke omgevingsvergunning […] 4 Er is alleen een civielrechtelijke overeenkomst. 5 Er is alleen een omgevingsplan vastgesteld of vergunning voor een BOPA verleend […] 6 Er zijn andere bewijsstukken […] Stap 3: maatschappelijk belang […] a. de projectlocatie draagt substantieel bij (in termen van aantal woningen) aan de gemeentelijke focus op wonen. b. Het project draagt bij aan en evenwichtige spreiding van wooninitiatieven over de kernen. […] Stap 4: datum oplevering"

> "Artikel 10 […] Als twee of meer projecten […] dezelfde positie behalen, bepaalt de gemeente de onderlinge volgorde door middel van een openbare loting." Toelichting art. 6: "Woningbouw — collectieve woonvormen: 1. Bestuursverklaring (zie artikel 5); 2. Overeenkomst over collectieve woonvorm (primair) óf omgevingsplan (fallback)."

— Bron: https://lokaleregelgeving.overheid.nl/CVDR765519 (geraadpleegd 2026-10-04). **Volgordelijst:** voorlopig bekendgemaakt in Gemeenteblad 2026, 422235 (10-9-2026): 47 initiatieven met samen circa 1.400 woningen [BER, telling onderzoeker]; bezwaartermijn 10 dagen; aangepaste lijst vastgesteld eind september 2026 (31 projecten, circa 774 woningen [BER]; projecten met een toegekende vooraanmelding zijn verwijderd, o.a. Wengelerhoek, Klimboom, CPO Boerhaar, Hemelrijk-2, 't Kleiland, Holsthoek). Mandaat tot ondertekening van de bestuursverklaring voor de "47 woningbouwinitiatieven" (B&W 15-9-2026). Aanlevering bij de netbeheerder vanaf **1-10-2026** (gemeentepagina: "Wij moeten op 1 oktober 2026 een volgordelijst van woningbouwprojecten aanleveren bij de netbeheerder"); de netbeheerder wordt in de beleidsregels niet bij naam genoemd. De pagina meldt: "Het is niet meer mogelijk om een woningbouwproject aan te melden. De aanmeldtermijn is verstreken." Een **tweede aanmeldronde is niet aangekondigd** en in de beleidsregels niet geregeld; wijziging van de volgorde is alleen mogelijk zolang de lijst niet is ingediend (art. 14 lid 4). **[INT]** Een nieuw CPO-initiatief staat dus niet op de lijst en scoort bij een latere ronde laag op projectrijpheid (zonder overeenkomst of BOPA: categorie 6) en op aantal woningen. Een aparte subcategorie "collectieve woonvormen" met als bewijsstuk een "overeenkomst over collectieve woonvorm" bestaat wel. Relevante regels op de lijst (plan | locatie | start | projectrijpheid | woningen): Engeweg Elshof | 2027 | 6 | 8; CPO Herxen | Kromme Koeweg | 2027 | 6 | 3; **Wijlandhof** | Elshof 19a | 2027 | 6 | **12**; **De Brinkweiden** | Kappeweg 18 | Buitengebied | 2028 | 6 | **12**; Grolleman | Herxen 63 | 2027 | 4 | 15; Berkeserf II | Boskamp | 2027 | 2 | 18. Bronnen: Gemeenteblad 2026, 422235 (https://zoek.officielebekendmakingen.nl/gmb-2026-422235.html) en https://www.olst-wijhe.nl/samenleven/olst-wijhe-in-ontwikkeling/energietransitie/woningbouwproject-aanmelden-voor-prioritering-van-transportcapaciteit (geraadpleegd 2026-10-04/05). Contact: netcongestieow@olst-wijhe.nl.

---

## 6. Praktijkvoorbeelden (2024-2026)

| # | Voorbeeld | Datum | Bron | Relevantie voor ons concept |
|---|---|---|---|---|
| 1 | **Hemelrijk-2 / Erveweg, Welsum:** circa 18 koopwoningen van grondeigenaren op grond met agrarische en volkstuinbestemming aan de rand van Welsum; principebesluit met ketenpartners (o.a. provincie) als voorwaarde | B&W 10-3-2026; gemeentebericht 13-3-2026 | B&W-besluitenlijst 10-3-2026 punt 10 (https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten); Gmb 2026, 422235 | **Zeer hoog:** schaal 10-20 op agrarische grond aansluitend aan een kleine kern; college welwillend |
| 2 | **Engeweg, Elshof:** 8 woningen op twee agrarische percelen, BOPA, anterieure overeenkomst, kopers met binding, verkleinde spuitzone; "Ook de provincie heeft al ingestemd" | B&W 3-2-2026 | https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/2026/2/9/b-amp-w-besluiten-03-02-2026 ; https://www.salland1.nl/college-olst-wijhe-stemt-in-met-bouw-acht-woningen-op-de-elshof/ ; https://wonen.olst-wijhe.nl/engeweg | **Hoog:** agrarisch naar wonen bij een buurtschap, schaal 8; geen CPO |
| 3 | **CPO Boerhaar:** circa 22-24 starterswoningen (CPO-vereniging, 26 leden + 10 partnerleden); gemeente koopt schoollocatie en Boerhaar 18/18a; krediet € 200.000 + € 900.000; raad 26-5-2026 unaniem; motie CPO-prioriteit | vereniging 3-7-2025; raad 26-5-2026 | https://www.sallandcentraal.nl/2025/07/cpo-boerhaar-officieel-opgericht/ ; besluitenlijst raad 26-5-2026 (https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/8a11295f-c63c-4bd9-890c-5d94773657de) ; https://hierinsalland.nl/pvda-stelt-collegevragen-over-nieuwbouwprojecten-op-de-boerhaar/ | **Hoog:** grootste lopende CPO; laat gemeentelijke werkwijze zien (actief grondbeleid, tekort grondexploitatie max. ca. € 500.000, bouwclaimovereenkomst, Didam-1-op-1). Kritiek van initiatiefnemers: "de gemeente Olst-Wijhe is op dit moment niet klaar en niet geschikt voor burgerinitiatieven zoals dit" (HierinSalland, 10-5-2026; opiniestuk) |
| 4 | **CPO Herxen:** 3 woningen op onbebouwd perceel; **bestuursovereenkomst B&W-GS** voor "op voorhand in procedure brengen" in afwachting van het visietraject | B&W 2-6-2026; herxen.nl 22-9-2026 | B&W-besluitenlijst 2-6-2026 punt 08/09; https://www.herxen.nl/2026/09/22/woningbouw-en-woningvisie-herxen/ | **Hoog:** CPO op onbebouwde grond in een kleine kern, met provinciale voorkant |
| 5 | **'t Kleiland, Kleistraat Olst:** 20 woningen op perceel met functie 'Agrarisch'; bindend raadsadvies; BOPA | raad 9-2-2026; B&W 17-3-2026 | B&W-besluitenlijst 17-3-2026 punt 10; raadsvoorstel zaak 3882-2026 | Midden-hoog: route raad-advies → BOPA voor 20 woningen aan de rand van een grote kern |
| 6 | **Zandhuisweg 7, Wijhe:** 9 woningen (BOPA, 3 weken) en **Steunenbergerweg 6, Olst:** 7 woningen op een erf | 25-11-2025; raad 26-2-2024 | Gmb 2025, 486680 en 514083; Gmb 2024, 97300 | Midden-hoog: precedenten voor 7-9 woningen |
| 7 | **De Klimboom, Boskamp:** 17 woningen, waarvan 9 CPO (jonge Boskampers), 4 sociale huur, 4 via inschrijving; kavels CPO niet via openbare selectie | voornemen 26-3-2024; koopovereenkomsten 6-12-2024; verkoop restkavels 4-2026 | https://wonen.olst-wijhe.nl/deklimboomboskamp ; Gmb 2024, 142870 | Hoog: CPO-spoor op schaal 9 op gemeentegrond binnen de kern |
| 8 | **Olstergaard, Olst:** 72 woningen (48 koop in particulier opdrachtgeverschap, 13 huur, 11 appartementen Grijs en Groen Wonen); officieel afgerond 2-10-2026 | 2022-2026 | https://wonen.olst-wijhe.nl/olstergaard ; https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/samen-proosten-op-het-resultaat-olstergaard-officieel-afgerond | Hoog: collectief wonen op gemeentelijke uitleglocatie |
| 9 | **Lierderholthuisweg 3, Wijhe:** KGO, splitsing + 1 woning + 1,5 ha bos; vergunning 23-6-2026 | 20-1-2026 → 23-6-2026 | Gmb 2026, 169650 en 302246 | Midden: erftransformatie volgens KGO |
| 10 | **Vettewinkelweg 2, Wijhe:** 1 extra woning na sloop; vergunning 7-4-2025 | 23-1-2024 → 7-4-2025 | Gmb 2025, 154624 | Midden: provinciale toestemming in vooroverleg |
| 11 | **Grolleman, Herxen 63:** 15 woningen op bedrijfsterrein, BOPA, provincie positief | B&W 23-9-2025 | woonnieuws 26-9-2025 | Midden: transformatie in een kleine kern |
| 12 | **Woningsplitsing en kleinschalig:** 52 verzoeken (40 buiten de kom: 16 toegekend, 11 geweigerd, 12 lopend); 16 splitsingsverzoeken (14 buiten de kom); gemeente onderzoekt beperking buitengebied | 5-2024 t/m 11-2025; evaluatie 26-5-2026 | iBabs (evaluatie, RIB 26-5-2026); woonnieuws 28-5-2026 | Midden: toont terughoudendheid buitengebied |
| 13 | **Netcongestie-volgordelijst:** 47 → 31 projecten, o.a. De Brinkweiden en Wijlandhof (12 woningen elk) | 11-8 t/m 1-10-2026 | Gmb 2026, 385444 en 422235 | Hoog: bepaalt tempo van elk project; twee onbekende 12-woningeninitiatieven |
| 14 | **Boer met plan voor ouderenhuurwoningen op bijna 6.000 m² vrijkomende agrarische grond** (oppositie steunt; "De provincie […] is daar niet heel happig op") | 7-2026 | https://hierinsalland.nl/onze-man-in-wijhe-toon-schuiling-8/ (18-7-2026; column) | Midden: vergelijkbaar initiatief; locatie en initiatiefnemer onbekend |
| 15 | **Zienswijze B&W op ontwerp-Omgevingsvisie/-verordening Overijssel** (kritisch op zon- en windbeleid; verder "veel aansluiting op hoofdlijnen") | B&W 24-6-2025 | https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/2025/6/30/b-amp-w-besluiten-24-06-2025/ontwerp-omgevingsvisie-verordening-overijssel | Context provinciale verhouding |
| 16 | **Bokkelerweg, Wesepe:** zes plattelandskamers (recreatief, besluit uitgesteld) en splitsing Bokkelerweg 1 (KGO, B&W 11-11-2025) | 9-2026 | https://wijhecity.nl/2026/09/19/laadpalen-renovaties-en-nieuwe-woningen-voor-olst-wijhe/ | Laag; geen woningbouw |

---

## 7. Inventarisatie bestaande initiatieven

| Initiatief | Aantal woningen | Status (2026-10-05) | Relevantie |
|---|---|---|---|
| **Vriendenerf, Olst** (Ringmus 50; CPO 55+; Hunebouw, GroenBlauw, Building Community) | 12 koopwoningen + Deelhuis | Gerealiseerd 2016-2017 (opening 30-9-2017) | Exact onze schaal en collectief karakter; binnen de kern. "12 in totaal verdeeld over 4 blokjes; Een gemeenschappelijk, multifunctioneel 13e huis, ons Deelhuis" (https://www.vriendenerf.nl/hoe-wonen-wij-samen/) |
| **Grijs en Groen Wonen** (Olstergaard; CPO 50+, nu VvE) | 11 appartementen | Gebouwd 2023, bewoond sinds maart 2024 | CPO met gemeenschappelijke ruimten. **Ander project dan Vriendenerf.** https://www.grijsengroenwonen.nl/ |
| **Olstergaard** (particulier opdrachtgeverschap, natuurinclusief, tiny houses) | **72** (48 koop + 13 huur + 11 G&G) | Afgerond; feest 2-10-2026 | Collectief wonen op gemeentelijke uitleglocatie |
| **CPO Boskamp, De Klimboom** | 9 (van 17) | Bouw sinds zomer 2025; oplevering gepland vóór zomer 2026 (niet bevestigd) | CPO voor lokale starters; kern |
| **CPO Boerhaar** | circa 22-24 | Kredieten raad 26-5-2026; bouwclaim aannemer; projectrijpheid 4 (voorlopige lijst) | Grootste lopende CPO; kleine kern |
| **CPO Herxen** | 3 | Principebesluit B&W 2-6-2026 | Kleine kern; provinciale overeenkomst |
| **Aardehuizen, Olst** (ecologisch) | 23 + Middenhuis | Gerealiseerd (jaartal niet in bron; "2006" uit het eerdere concept niet teruggevonden) | Collectief precedent; CPO-vorm niet op de homepage; de Woonvisie noemt het een CPO-project (https://www.aardehuis.nl/) |
| **Engeweg, Elshof** (grondeigenaren, geen CPO) | 8 | Principebesluit 3-2-2026 | Agrarisch-naar-wonen |
| **Hemelrijk-2, Welsum** (grondeigenaren, geen CPO) | circa 18 | Principebesluit 10-3-2026 | Agrarisch-naar-wonen bij een kleine kern |
| **Wijlandhof, Elshof; De Brinkweiden, Kappeweg 18** | 12 elk | Alleen op volgordelijst; inhoud onbekend | Mogelijk dichtstbijzijnde analogie voor 10-12 woningen [INT] |
| **Stationsweg Wijhe: woon-zorginitiatief van ouders** | onbekend | Intentiebrief 3-2026 | Collectief woon-zorginitiatief (woonnieuws 12-3-2026) |
| **Flexwoningen (SallandWonen)** | 76 (50 Wengelerhoek + 26 Vink) | In gebruik sinds 2023 | Experimentele woonvorm (https://wonen.olst-wijhe.nl/flexwonen) |

Een CPO of collectief project **op agrarische grond in het open buitengebied** van Olst-Wijhe: **niet gevonden**. Wooncommunity De Ware (24 studio's, 13-3-2025) ligt in Raalte en wordt niet aan Olst-Wijhe toegerekend.

---

## 8. Huisvestingsverordening

**Aanwezig: nee.** In CVDR (alle 628 records van Olst-Wijhe, inclusief ingetrokken versies) en Gemeenteblad is geen huisvestingsverordening, urgentieverordening of woonruimteverdelingsregeling van Olst-Wijhe aangetroffen (de enige hit, Heerde "Huisvestingsverordening 2002", CVDR111196, is Gelders). Letterlijk, de gemeente zelf:

> "De gemeente Olst-Wijhe heeft momenteel (nog) geen Huisvestingsverordening. Op dit moment is Olst-Wijhe aangesloten bij de totstandkoming van de (regionaal geharmoniseerde) modelverordening binnen de regio West-Overijssel. Als de aanstaande 'Wet versterking regie volkshuisvesting' […] in werking treedt, dan moet ook de gemeente Olst-Wijhe een eigen Huisvestingsverordening vaststellen. […] Gemeenten kunnen bepalen of zij willen sturen, aan de hand van lokale bindingseisen, op de toewijzing van betaalbare koopwoningen. Dit is begrensd tot een absoluut maximum van 50% en is alleen van toepassing op nieuwbouw. […] In Olst-Wijhe wordt momenteel meer gebouwd dan louter de lokale behoefte, waardoor schaarste moeilijk aantoonbaar wordt."

— Bron: Raadsinformatiebrief 10-11-2025 (zaak 45292-2025, toezegging 55), p. 3, iBabs (geraadpleegd 2026-10-04); vergelijkbaar RIB 2-12/16-12-2025 (zaak 47794-2025, schaarste-onderzoek: "geen sprake is van lokale 'verdringing' binnen het betaalbare segment"). Een minimumpercentage sociale huur uit een verordening bestaat dus niet. De lokale-bindingspraktijk loopt via projectafspraken (Aberson, Weidebeek, Vosmanskamp: eerst aanbieden aan mensen met binding, daarna vrij). **Sociale-huurpercentage in beleid:** Woonvisie 2022: "minimaal 25% sociale huur bij nieuwbouw" en regionale ondergrens 30% sociale huur of betaalbare koop voor het totale programma; nieuwere lijn (Woondeal, Grondprijzenbrief 2026 bijlage, evaluatie 2026, Wvrv): 30% sociale huur, 40% middensegment, 30% vrij; bestuursakkoord: 70% van de nieuwbouw betaalbaar. Een nieuwe verordening is voorzien met het Volkshuisvestingsprogramma ("Uiteindelijk stelt u als raad ook de Huisvestingsverordening vast.") en is nog niet als ontwerp gepubliceerd. De huisvestingsverordening moet volgens [PB] §5 uiterlijk 1-1-2028 zijn herzien (bronnen verschillen). Een "Beleidsnota Inwoning" bestaat (CVDR410483, B&W 5-7-2016).

**Waar te vinden:** iBabs (raadsvoorstel Huisvestingsverordening), team Wonen, regionale modelverordening West-Overijssel.

---

## 9. Zelfbouwloket / contactpersoon

- **Zelfbouwloket:** de **Kavelwinkel** (https://wonen.olst-wijhe.nl/kavelwinkel) is het loket voor bouwkavels (zelfbouw en samenbouw onder CPO); een apart CPO-loket met benoemd aanspreekpunt is **niet gevonden**. Kavelinschrijving en woonnieuws: https://wonen.olst-wijhe.nl. Grondprijzenbrief: "team Ruimtelijke Realisatie (Grondzaken & Vastgoed)".
- **Wethouder wonen: Marcel Blind** (Gemeentebelangen; portefeuille volgens bestuursakkoord p. 23: wonen (incl. huisvesting vluchtelingen), duurzaamheid, openbare ruimte, mobiliteit, monumenten, **ruimtelijke ordening en omgevingsplannen**; kernenwethouder Olst, Eikelhof, Herxen, Middel). De pagina https://www.olst-wijhe.nl/marcelblind (2026-10-04) toont dezelfde portefeuille en: "Gegevens Marcel Blind 06-51241373 m.blind@olst-wijhe.nl"; persoonlijk spreken via de bestuurssecretaresse, 14 0570.
- **Wethouder Hans Olthof** (VVD): financiën, economische ontwikkeling, **toekomstbestendige kernen en buitengebied**, water buitendijks, vrijetijdseconomie, dienstverlening, **grondbeleid (wonen en bedrijven)**, evenementen, gebiedsgerichte aanpak, **Regio Zwolle**; kernenwethouder Wesepe, Elshof, Marle, Welsum. https://www.olst-wijhe.nl/hansolthof (2026-10-04): 06-21311887, h.olthof@olst-wijhe.nl. Kernenwethouder Wijhe, Boerhaar, Boskamp, Den Nul: Herman Engberink (CDA; sociaal domein, sport en cultuur, onderwijshuisvesting, maatschappelijk vastgoed).
- **Ambtelijk:** conceptverzoek (https://www.olst-wijhe.nl/vooroverlegomgevingsvergunning) en "toetsing schetsplan" (https://www.olst-wijhe.nl/toetsingschetsplan); algemeen 14 0570, gemeente@olst-wijhe.nl; netcongestie: netcongestieow@olst-wijhe.nl. In de stukken genoemd (zonder dat een CPO-loket bestaat): casemanager Britt Oostveen (adviesnota's Engeweg e.a.), Marchien Hoffer (bouwsteen/KGO), Alfons Ganzevles (woningsplitsing/evaluatie), programmamanager Wietze van der Ploeg (kernenbezoek Wijhe 9-9-2026, Salland Centraal 11-9-2026). Een eerder in het concept genoemde grondzaken-contactpersoon (2018) is verwijderd.
- **Erven:** Erfcoach Overijssel Yvonne in 't Veld (zie §4) en ervenconsulent Het Oversticht. **Provincie:** Overijssel Loket 038 499 88 99, overijsselloket@overijssel.nl, vab@overijssel.nl [PB]; de provinciale accounthouder is niet openbaar. Omgevingstafel IJsselland: https://www.odijsselland.nl/over/omgevingstafel.
- **Kernenwethouders** (https://www.olst-wijhe.nl/kernenwethouders) zijn per kern aanspreekpunt.

---

## 10. Bestuurlijk klimaat

**Coalitie in vorming op 2026-10-05: nee.** Het college Gemeentebelangen-CDA-VVD (11 van 17 zetels) is sinds 16-6-2026 geïnstalleerd. Positieve aanwijzingen (geraadpleegd 2026-10-04/05):

> "Aanwezig Mevrouw S.A.E. Poepjes, burgemeester; de heer S. van den Berg, gemeentesecretaris; de heer M. Blind, wethouder; de heer H. Olthof, wethouder; de heer H. Engberink, wethouder."

— Bron: B&W-besluitenlijst 22-9-2026, https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/b-amp-w-besluiten-22-09-2026. De gemeentelijke nieuwspagina (laatst gewijzigd 5-10-2026 09:29) toont geen bericht over formatie, crisis of aftreden. Regionale media (Salland1, Salland Centraal, Wijhe City, HierinSalland) meldden tussen 16-6 en 4-10-2026 geen crisis, ontslag, motie van wantrouwen of fractiebreuk. De raadsagenda van **5-10-2026** bevat de benoeming en beëdiging van raadslid Erik-Jan Post als opvolger van Gerjo van der Horst (die ontslag nam; fractie niet vermeld); dat verandert de verhoudingen niet zolang de zetelverdeling niet wijzigt (niet nagegaan welke fractie). Volgende raadsvergadering 26-10-2026. De Stentor was niet toegankelijk. De enige wijziging: de oppositiepartij "Pro Olst-Wijhe" heet sinds 23-6-2026 **Olst-Wijhe Vooruit** (GroenLinks, PvdA, D66; Salland1, 23-6-2026), in de raad genoemd als fractie "GroenLinks-PvdA-D66".

| Datum | Gebeurtenis | Bron |
|---|---|---|
| 9-3-2026 | Formatieprotocol: de grootste partij neemt het voortouw | HierinSalland, 19-4-2026 (opiniestuk) |
| 18-3-2026 | Gemeenteraadsverkiezingen | https://www.olst-wijhe.nl/bestuur/verkiezingen/gemeenteraadsverkiezingen-2026/definitieve-uitslag-gemeenteraadsverkiezingen-2026 |
| 26-3-2026 | Definitieve uitslag vastgesteld; installatie raad 31-3-2026 | idem |
| 7-4-2026 | Hester Scholten verkenner; gemeentebericht 17-4-2026: GB-CDA-VVD "enige combinatie" die als haalbaar wordt gezien; de grootste partij (GL/PvdA/D66) buitengesloten | https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/2026/4/17/coalitie-gemeentebelangen-cda-en-vvd-meest-kansrijke-richting-formatiegesprekken-starten-binnenkort |
| 24-4-2026 | Ellen Nauta-van Moorsel (burgemeester Hof van Twente) formateur; start 28-4-2026 | https://wijhecity.nl/2026/04/24/ellen-nauta-van-moorsel-aangesteld-als-formateur-in-olst-wijhe/ |
| 12-6-2026 | Datering bestuursakkoord "Betrouwbaar en bestendig: de basis op orde" | bestuursakkoord p. 5 |
| 16-6-2026 | Ondertekening en aanbieding; wethouders Blind, Olthof en Engberink door een unanieme raad benoemd | https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/2026/6/15/bestuursakkoord-olst-wijhe-op-dinsdag-16-juni-ondertekend-en-aangeboden |
| 23-6-2026 | "Pro Olst-Wijhe" wordt Olst-Wijhe Vooruit | https://www.salland1.nl/pro-olst-wijhe-verandert-naam-in-olst-wijhe-vooruit/ |
| 23-6 t/m 22-9-2026 | Het college neemt wekelijks besluiten | B&W-besluitenlijsten |

**Zetelverdeling (17 zetels, definitieve uitslag 26-3-2026):**

> "De 17 zetels in de gemeenteraad zijn als volgt verdeeld: GroenLinks / PvdA / D66 3.002 stemmen 6 zetels; Gemeentebelangen Olst-Wijhe 2.821, 5; CDA 1.733, 3; VVD 1.688, 3."

Proces-verbaal P 22-2: 15.511 kiesgerechtigden; 9.323 toegelaten kiezers; "Stemmen op kandidaten 9244 / Ongeldige stemmen 19 / Totaal uitgebrachte stemmen 9325". De som van de partijstemmen is 9.244 (sluit aan); opkomst **60,1%** (de eerder genoemde 9.242 en 59,6% waren onjuist). Bron: https://www.olst-wijhe.nl/bestuur/verkiezingen/gemeenteraadsverkiezingen-2026/definitieve-uitslag-gemeenteraadsverkiezingen-2026/proces-verbaal-p-22-2-verslag-uitslag-en-zetelverdeling (geraadpleegd 2026-10-04/05). De coalitie heeft 11 van 17 zetels; Olst-Wijhe Vooruit (6) vormt de oppositie.

**College 2026-2030** (bestuursakkoord p. 23, "Portefeuilleverdeling Olst-Wijhe 2026-2030"):

| Functie | Naam | Partij | Portefeuille (letterlijk uit het akkoord) |
|---|---|---|---|
| Burgemeester | Sietske Poepjes | n.v.t. | Algemene bestuurlijke zaken en coördinatie; openbare orde en veiligheid; omgevingsdienst; communicatie en participatie |
| **Wethouder wonen**, 1e loco | **Marcel Blind** | Gemeentebelangen | Wonen (incl. huisvesting vluchtelingen); duurzaamheid; openbare ruimte; mobiliteit; monumenten; **ruimtelijke ordening en omgevingsplannen**; kernenwethouder Olst, Eikelhof, Herxen, Middel |
| Wethouder, 3e loco | Hans Olthof | VVD | Financiën; economische ontwikkeling; **toekomstbestendige kernen en buitengebied**; water buitendijks; vrijetijdseconomie; dienstverlening; **grondbeleid (wonen en bedrijven)**; evenementenbeleid; gebiedsgerichte aanpak; Regio Zwolle; kernenwethouder Wesepe, Elshof, Marle, Welsum |
| Wethouder, 2e loco | Herman Engberink | CDA | Sociaal domein; volksgezondheid; beschermd wonen en maatschappelijke opvang; werk en inkomen; sport en cultuur; onderwijs(huisvesting); maatschappelijk vastgoed en vitale voorzieningen; kernenwethouder Wijhe, Boerhaar, Boskamp, Den Nul |

Het eerdere concept schreef "woon- en grondbeleid" bij Blind en "financiën, IJssel en buitengebied" bij Olthof; volgens het akkoord ligt **grondbeleid bij Olthof**. Herman Engberink was al sinds 26-11-2025 interim-wethouder (opvolger van Judith Compagner, CDA, portefeuillehouder Omgevingsvisie).

**Bestuursakkoord 2026-2030** (23 p.; GB, CDA en VVD; gedateerd 12-6-2026), https://www.olst-wijhe.nl/bestuursakkoord-1/bestuursakkoord-olst-wijhe-2026-2030 (bereikbaar via https://gemeenteraad.olst-wijhe.nl/bestuursakkoord; geraadpleegd 2026-10-04). De volledige tekst is doorzocht op wonen, woningbouw, buitengebied, erf, KGO, CPO, collectief, zelfbouw, experiment, kernen, grond, Wesepe en "+400". **CPO, collectief, zelfbouw, particulier opdrachtgeverschap, experiment(eel), KGO, erf, rood-voor-rood en VAB komen niet voor.** Relevante passages:

> "De afgelopen jaren lag onze focus nadrukkelijk op Wonen. We liggen op koers met de realisatie van onze ambitie om 1.000 tot 1.200 woningen te bouwen tot en met 2031. Er zijn in de afgelopen bestuursperiode bijna 450 woningen gerealiseerd." (p. 6)

> "Wonen: van huis naar thuis […] De afgelopen jaren laten zich op woongebied het beste omschrijven als: bouwen, bouwen, bouwen. Deze nieuwe bestuursperiode gaan we hier mee verder. […] In deze periode streven we naar gemiddeld 100 woningen per jaar er bij, dus in totaal zo'n 400 nieuwe woningen. • We zetten wonen in als instrument. […] • We willen voldoen aan de vraag vanuit starters, senioren en zorgvragers door passende woningen te bouwen. WAT GAAN WE DAARVOOR DOEN? • We ontwikkelen een Volkshuisvestingsprogramma. • We ontwikkelen Wesepe verder als derde kern in Olst-Wijhe […] • We zetten maximaal in op het bouwen van woningen die passen bij de lokale vraag. • We houden vast aan het uitgangspunt dat 70% van de nieuw te bouwen woningen betaalbaar zijn: sociale- en middenhuur en goedkope of betaalbare koop. • We werken actief samen met de woningcorporatie(s)." (p. 8)

> "Toekomstbestendige kernen en buitengebied: De komende jaren zal de transitie van het platteland onverminderd doorgaan. […] We willen een vitaal platteland, waar boeren, en de keten die daarmee verbonden is, toekomstperspectief hebben. […] • We willen in gebiedsontwikkelingen onze koers per kern of gebied vastleggen. In thematische beleidsplannen leggen we (inrichtings)keuzes vast waar meer duidelijkheid op nodig is. Als er al plannen ontwikkeld of vastgelegd zijn, gaan we daar op verder. […] • We adviseren boeren die hun bedrijf willen transformeren of willen stoppen." (p. 9)

> "We richten ons nadrukkelijker op uitvoering en dienstverlening. We maken geen nieuwe langjarige visies met langdurige (participatie)processen." (p. 20) / "Nieuwe projecten starten we vanuit een maatschappelijke behoefte." (p. 20)

"+400" betekent dus gemiddeld 100 woningen per jaar in de bestuursperiode en is geen extra opgave bovenop 1.000-1.200. De perskop "Minder plannen, minder papier en meer doen" is van Salland1 (19-6-2026); het motto "minder papier, méér doen" komt van GB-fractievoorzitter Ronnie Niemeijer.

**Politieke duiding voor CPO [INT]:** het college is pragmatisch en uitvoeringsgericht en wil woningen "die daadwerkelijk gebouwd" worden. In de vorige periode zijn CPO's gefaciliteerd (Klimboom, Olstergaard, Boerhaar-krediet) en in 2026 gaf het college positieve principebesluiten voor agrarische dorpsuitbreiding (Engeweg 8, Hemelrijk-2 circa 18) en een CPO (Herxen). Tegelijk ontraadde het college op 26-5-2026 de motie om CPO-initiatieven prioriteit te geven; Gemeentebelangen stemde tegen, de motie kreeg 11 stemmen (oppositie, VVD en twee CDA-raadsleden). Het draagvlak voor bottom-up-initiatieven is daarmee breder dan de oppositie. Initiatiefnemers van CPO Boerhaar en uit Boskamp en Wesepe uitten stevige kritiek op de gemeentelijke werkwijze. Het college staat onder financiële druk: structureel tekort van circa € 1,4 mln vanaf 2027 en een bezuinigingsopgave bedrijfsvoering (Salland Centraal, 9-9-2026; B&W 22-9-2026), wat de ambtelijke capaciteit voor initiatieven van derden kan beperken **[INT]**. De raadsverhoudingen zijn volgens de verkenner een aandachtspunt; de coalitie stemt niet altijd als blok (HierinSalland, 16-8-2026; opiniestuk). Context: in de enquête over een mogelijke fusie van Raalte en Olst-Wijhe waren 148 respondenten voor en 147 tegen (HierinSalland, 5-8-2026); een bestuurlijk fusietraject is niet gevonden. Provinciale Statenverkiezingen in maart 2027 [PB] kunnen accenten verschuiven.

---

## 11. Kostenverhaal en leges

**Kostenverhaal.** De anterieure overeenkomst is de **standaard**, ook voor 1-2 woningen in het buitengebied:

> "De gemeente Olst-Wijhe geeft er de voorkeur aan om kosten te verhalen, door middel van een intentie-/samenwerkingsovereenkomst (SOK) en/of anterieure overeenkomst (kostendekkend). De berekening hiervan is maatwerk per project. […] In anterieure overeenkomsten worden ook afspraken gemaakt over de vergoeding van eventuele toekomstige planschade (of nadeelcompensatie) door de ontwikkelaar aan de gemeente."

— Bron: Nota Grondbeleid 2023-2026, p. 11-12 (CVDR691005; geraadpleegd 2026-10-04). Een aparte **nota kostenverhaal** bestaat niet (CVDR en Gemeenteblad doorzocht); het kader is de Nota Grondbeleid. De gemeente publiceert systematisch zakelijke beschrijvingen: 

> "Het college van B en W heeft op 30 september 2024 een overeenkomst afgesloten voor de exploitatie van de locatie Vettewinkelweg 2 te Wijhe. Hiermee is het kostenverhaal van de voorgenomen ontwikkeling op deze locatie en de hiervoor benodigde planologische procedure verzekerd."

— Bron: Gemeenteblad 2024, 460019 (geraadpleegd 2026-10-04). Buitengebied-overeenkomsten 2024-2025 o.a. Scholtensweg 50, Elshagenweg 1, Lierderholthuisweg 12 en 13, Zonnenbergerweg 1, Herxen 77/77a, Boerlestraat 8-8a, Het Anem 18, Diepenveenseweg 2; voor kernlocaties Raalterweg 48-50 (81 woningen) en Wengelerhoek. De overeenkomst wordt gesloten vóór de aanvraag (Vettewinkelweg 2: overeenkomst 30-9-2024, aanvraag 24-12-2024). Bij Engeweg is de anterieure overeenkomst "een harde voorwaarde voor medewerking". **Kwaliteitsinvestering:** sloop, landschappelijke inpassing (erfinrichtingsplan Het Oversticht), bos (Lierderholthuisweg 3: provinciale subsidie "Meer bos in Overijssel"), bijdrage aan de Voorziening Ruimtelijke Kwaliteit; bankgarantie of andere afdwinging is niet gevonden; een vereveningsfonds is in overweging (raadssessie 28-9-2026).

**Leges 2026** (CVDR752237 is **Olst-Wijhe**: "Verordening op de heffing en de invordering van leges 2026"; raad **24-11-2025**, in werking 23-12-2025; tarieventabel in dezelfde regeling; https://lokaleregelgeving.overheid.nl/CVDR752237, geraadpleegd 2026-10-04/05). Letterlijk (Hoofdstuk 2, Omgevingswet):

> "Artikel 2.4 Conceptverzoek […] a. voor het beoordelen van een conceptverzoek in verband met het verkrijgen van een indicatie of een voorgenomen project of ontwikkeling vergunbaar is | € 306,00 | b. voor een richtinggevende uitspraak van het gemeentebestuur (principebesluit) of zij wil meewerken aan het planologisch faciliteren van een conceptverzoek dat niet past in het omgevingsplan […] | € 1.225,00"

> "Artikel 2.5 Bouwactiviteit (Technisch) […] c. bij bouwkosten van € 1.000.000,- of meer, van de bouwkosten 1,4% met een minimum van € 21.440,00 en een maximum van € 255.000,00" (b: € 50.000 tot € 1.000.000: 2,1% met een minimum van € 1.275,00)

> "Artikel 2.6 Bouwactiviteit (omgevingsplan) […] 4. voor een buitenplanse omgevingsplanactiviteit, niet zijnde een kleine buitenplanse omgevingsplanactiviteit € 8.850 vermeerderd met het volgende percentage van de bouwkosten boven € 150.000,- 1% met een totaal maximum van € 20.515,00"

> "Artikel 2.7 Afwijken van regels in het omgevingsplan […] (geen bouwactiviteit) […] 3. […] waarbij er geen (beoordeling van een) ruimtelijke motivering nodig is € 4.700,00 / 4. […] waarbij er een (beoordeling van een) ruimtelijke motivering nodig is € 7.800,00"

> "Artikel 2.21 Wijzigen van het omgevingsplan / Het tarief bedraagt voor het in behandeling nemen van een aanvraag tot het wijzigen van het omgevingsplan, waarbij geen sprake is van een bouwactiviteit: € 13.275,00"

> Overig: art. 2.24b uitgebreide procedure bij BOPA € 1.101,65; art. 2.25 beoordeling landschappelijk inpassingsplan of stedenbouwkundig plan elk € 396,20; art. 2.26 advies van de gemeenteraad (adviesrecht raad) € 521,70; art. 2.27 instemming door een ander bestuursorgaan: het bedrag dat dat orgaan zelf zou heffen; art. 2.28: 50% vermindering van de conceptverzoek-leges bij aanvraag binnen 12 maanden.

De eerder in het concept genoemde bedragen (€ 307,95, € 516,45 en € 4.755) komen niet in de tabel voor en zijn verwijderd. Vooroverleg kent geen eigen tarief; het loopt via het conceptverzoek (art. 2.4).

**[BER] Indicatieve berekening (door de onderzoeker, geen gemeentelijke opgave)** voor 10-12 woningen met een **veronderstelde bouwsom van € 3,5 mln**, route BOPA: bouwactiviteit technisch 1,4% × € 3.500.000 = € 49.000; BOPA met bouwactiviteit € 8.850 + 1% × € 3.350.000 = € 42.350, begrensd op het maximum **€ 20.515**; bindend raadsadvies € 521,70; beoordeling van vijf rapporten à € 396,20 = € 1.981; aftrek 50% van het conceptverzoek € 1.225 = − € 612,50; subtotaal omgevingsvergunning **≈ € 71.405**; conceptverzoek met principebesluit vooraf € 1.225; eventueel uitgebreide procedure + € 1.101,65. Indicatief totaal **≈ € 72.600-73.700**, circa € 6.000-7.300 per woning; ruim twee derde komt uit de technische bouwactiviteit. Provinciale instemming (art. 2.27) komt daar mogelijk bovenop (tarief onbekend). Alternatieve route via omgevingsplanwijziging (€ 13.275) plus binnenplanse vergunning (art. 2.6 lid 1: maximum € 20.000) ≈ € 82.275 plus rapporten; of art. 2.21 bij een gecombineerd plan wordt geheven is niet vastgesteld. Kostenverhaal (anterieure overeenkomst) en de kwaliteitsinvestering komen er nog bij.

**Leges 2027:** het raadsvoorstel "Voorstel tot verhoging kostendekkendheid leges" (zaak 55704-2026; B&W 22-9-2026; oordeelsvormend 5-10-2026):

> "Het beoogde resultaat is dat de niet wettelijk vastgestelde leges vanaf 2027 worden gebaseerd op volledige kostendekkendheid, voor zover dit juridisch mogelijk is." / "Voor hoofdstuk 2 betekent dit een forse tariefstijging: naast de trendmatige verhoging van 2,8% is gemiddeld circa 23% extra verhoging (gewogen gemiddelde) nodig."

— Bron: iBabs-bijlagen agenda raadsvergadering 5-10-2026 (geraadpleegd 2026-10-05). Het besluit is nog niet genomen; de tarieven 2026 gelden tot 31-12-2026.

---

## 12. Woningbehoefte en doelgroepen

- **Woonvisie 2022-2025 en Uitvoeringsprogramma:** groei met 1.000-1.200 woningen in tien jaar via inbreiding en uitbreiding bij Olst en Wijhe, daarnaast Wesepe en maatwerk in kleine kernen; betaalbaarheid; starters en senioren; lokale binding; wonen-zorg; woningsplitsing voor kleinere huishoudens; "70% betaalbaar waarvan 30% sociale huur" (Uitvoeringsprogramma p. 3-4). Betaalbaarheidsgrenzen: sociale koop I < € 267.000 (prijspeil 2026), betaalbaar < € 420.000 (2026; € 405.000 in 2025); Starterslening tot € 378.000, maximaal € 35.000 lening, met voorrang voor lokale starters (gemeentebericht 15-5-2026; raadsvoorstel Verordening Starterslening 2026 op de raadsagenda 5-10-2026).
- **Inwonerpanel wonen** (420 deelnemers; resultaten 19-5-2026):

  > "Van degenen die willen verhuizen, wil twee derde in Olst-Wijhe blijven. […] Met name in de kleinere kernen wordt een tekort aan voorzieningen ervaren (52%). […] Het merendeel van de deelnemers wil graag een koopwoning en meer dan twee derde staat open voor nieuwe woonvormen, waarbij 25% animo heeft voor zelfbouw. […] De resultaten nemen we mee in het nieuwe woonbeleid dat in de maak is."

  — Bron: gemeentebericht "Resultaten inwonerpanel over wonen in Olst-Wijhe bekend", 19-5-2026 (via archive.csv; losse URL geeft 404; geraadpleegd 2026-10-04). Dit is het sterkste lokale behoeftesignaal voor zelfbouw/CPO.
- **Herkomstanalyse:** "In de onderzochte periode (2020 t/m 2024) geen sprake is van lokale 'verdringing' binnen het betaalbare segment" (RIB 2-12/16-12-2025, zaak 47794-2025); "Op 1 januari 2025 stonden in de gemeente […] zo'n 8.260 woningen" (RIB 2-12-2025).
- **Prestatieafspraken 2025-2026** (SallandWonen, huurdersorganisaties, gemeenten Raalte en Olst-Wijhe): "De komende twee jaar worden ruim 200 sociale huurwoningen in Raalte en Olst-Wijhe nieuw gebouwd." (Bouwen in het Oosten, 10-12-2024, https://www.bouweninhetoosten.nl/samen-sterk-voor-goed-wonen-in-salland-prestatieafspraken-2025-2026/). De eerder genoemde "versneld 76 woningen" staat niet in dat artikel; het betreft waarschijnlijk de 76 flexwoningen van 2023. **Prestatieafspraken 2027-2028** zijn in voorbereiding (B&W 22-9-2026, punt 05); de pilot Wooncoaches wordt verlengd t/m 31-12-2027 en de provincie stopt daarna met cofinanciering.
- **Ouderen en zorg (A5):** de Omgevingsvisie noemt woonzorgconcepten op dekzandgronden en stimuleert dementievriendelijke woonvormen; geen lokale uitwerking van de West-Overijsselse woonzorgvisie gevonden. Senioren-CPO's zijn aanwezig (Vriendenerf 55+, Grijs en Groen Wonen 50+); er ligt een woon-zorginitiatief van ouders aan de Stationsweg (3-2026) en een boer met een ouderenhuurplan (7-2026). De regeling Langer zelfstandig wonen heeft de gemeente of een corporatie als aanvrager [PB].
- **Aansluiting CPO [INT]:** CPO's voor lokale starters en 50-plussers sluiten aan bij de benoemde doelgroepen (Klimboom, Boerhaar, Olstergaard, Herxen). Een cluster van 10-12 woningen buiten de kernen sluit minder aan; bouwen concentreert zich in Olst, Wijhe en Wesepe en de kleine kernen krijgen indicatief 5-10% groei tot 2050 (Herxen gemiddeld 2-4 woningen per jaar). Aansluiting is het sterkst bij een betaalbaar, lokaal gebonden koop-CPO bij een kern.

---

## Niet gevonden en openstaande punten (met vindplaats)
1. **Provinciale instemming als formeel besluit** bij Vettewinkelweg 2, Lierderholthuisweg 3 en Engeweg: niet gepubliceerd (Provinciaal blad publiceert instemmingen niet); zaakdossier gemeente/provincie. Engeweg: "Ook de provincie heeft al ingestemd" (vooroverleg); BOPA-aanvraag nog niet gepubliceerd.
2. **Inhoud en initiatiefnemers van Wijlandhof (Elshof 19a) en De Brinkweiden (Kappeweg 18)**, 12 woningen elk, alleen op de volgordelijst: team Ruimte en Samenleving, conceptverzoek, toekomstige B&W-lijsten.
3. **Contour bestaand bebouwd gebied en afstandszone kernrand:** Omgevingsprogramma landelijk gebied, bouwsteen (nov. 2026), integrale visiekaart (iBabs 34e53813-5c68-491b-8ea3-9f3d5997f769).
4. **Tekst van de bestuurlijke afspraken GS-B&W Herxen:** iBabs/B&W-archief 2-6-2026; afdeling RO; provincie.
5. **Plan van aanpak Volkshuisvestingsprogramma (niet-openbaar), een ontwerp-programma en voorbereiding op afschaffing van de ladder:** raadsinformatiebrief augustus 2026; programmamanager wonen.
6. **Gemeentelijk CPO-beleid, CPO-loket, CPO-grondprijs of -reservering in Olst Zuid/Wijhe Noord; uitvoering van de motie van 26-5-2026:** iBabs, Volkshuisvestingsprogramma, team Ruimtelijke Realisatie.
7. **Uitkomst raadssessie 28-9-2026 en bouwsteen (beoogd november 2026), opvolger Nota Grondbeleid (2027+), besluit leges 2027:** raadsagenda 26-10-2026 en verslag griffie.
8. **Tweede aanmeldronde netcongestie en feitelijke indiening bij de netbeheerder na 1-10-2026:** netcongestiepagina, nieuws oktober 2026.
9. **Beschikking subsidie 4.39 (en nummer in de stukken); partners intergemeentelijk programma:** regelen.overijssel.nl, vab@overijssel.nl.
10. **Harde/zachte plancapaciteit totaal, 80/20-ruimte en reservering voor initiatieven van derden:** Planmonitor/Dashboard Wonen, Woondeal bijlage 1.
11. **Uitkomst Klimboom-inschrijving 2026, oplevering CPO-woningen, raadsbesluit Holsthoek (7-9-2026), bedrag gebiedsaanpak Wesepe (€ 353.634 uit het eerdere concept niet teruggevonden):** kavelwinkel, iBabs, collegevoorstel zaak 17612-2025.
12. **Tuinkamer Olstergaard** (uit het eerdere concept): niet gevonden. **De Stentor-artikelen:** niet toegankelijk.
13. **Provinciale vooroverlegreacties of instemmingsbrieven** (Engeweg, Vettewinkelweg 2, Steunenbergerweg 6, 't Kleiland; bijlage 2 adviesnota Engeweg, zaak 32332-2025): zaakdossier gemeente (Woo-verzoek), Overijssel Loket.
14. **Zienswijzenota Omgevingsvisie/-verordening Overijssel (Statenstuk PS26-000033)**, de bijlage bij de gemeentelijke zienswijze van 24-6-2025 en een gemeentelijke zienswijze op het ontwerp-VHP Overijssel: Statenstukken Overijssel (13-5-2026), iBabs (lijst ingekomen stukken raad juni/juli 2025).
15. **Aantal en lijst van Olst-Wijhese dossiers op de Omgevingstafel IJsselland; cijfers uit het provinciale Dashboard Wonen (Tableau, niet programmatisch uitgelezen; de Planmonitor-laag is wel gebruikt):** OD IJsselland, https://overijsselsewoonaanpak.nl/dashboard-en-onderzoek/.

---

## Twee kernvragen

### 1. Wonen in het buitengebied: biedt het gemeentelijk beleid ruimte voor een cluster van 10-12 woningen buiten de bestaande woonkernen?
- **(a) Gemeente:** in het **open buitengebied geen ruimte voorzien**. De Omgevingsvisie concentreert bouwen in Wijhe, Olst en Wesepe en geeft de kleine kernen (Boerhaar, Boskamp, Den Nul, Welsum, Herxen) ruimte voor kleinschalige projecten, "open voor […] CPO", indicatief 5-10% groei tot 2050; de IJsselzone is gesloten, het kommenlandschap "nee, tenzij"; de Handreiking KGO kent circa 3 woningen per bouwblok en 2 bouwblokken per erf; het beleid voor kleinschalige initiatieven (1-5 woningen) geldt alleen binnen de bebouwde kom; de gemeente onderzoekt hoe woningbouw in het buitengebied verder kan worden beperkt en wil nieuwe woningen laten "landen" aan de kernranden. Positieve signalen: Engeweg Elshof (8 woningen, agrarisch, principebesluit), Hemelrijk-2 Welsum (circa 18, agrarisch) en 't Kleiland (20) bij kernen, CPO Herxen (3) met provinciale bestuursovereenkomst, CPO Boerhaar (circa 22-24) en de raadsmotie van 26-5-2026.
- **(b) Provincie [PB]:** "overige kern" (art. 4.4: alleen lokale behoefte en bijzondere doelgroepen), art. 4.5 (aansluiten op bestaand bebouwd gebied), redeneerlijn (art. 4.122), woonafspraken West-Overijssel, landbouwgebied-typologie (Engeweg: generiek, art. 4.124 lid 1), en bij een BOPA provinciale instemming volgens de Lijst BOPA. De provincie reageerde positief op de gemeentelijke visie en zegt voor Herxen "tegelijkertijd het landelijk gebied [te] beschermen".
- **(c) Eindoordeel:** een cluster van 10-12 woningen **in het open buitengebied is kansarm tot zeer kansarm**. **Aansluitend aan een kleine kern of buurtschap** (Welsum, Herxen, Boskamp, Elshof) is het een **reële maar voorwaardelijke route** (lokale binding, bindend raadsadvies bij > 3 woningen, provinciale instemming, spuitzone, netcongestie); **aansluitend aan een grote kern** (Olst, Wijhe, Wesepe) is het **kansrijkst** en past in "inbreiding voor uitbreiding" en het zoekgebied erfontwikkeling. Belangrijkste onzekerheden: uitkomst van de bouwsteen Erfontwikkeling (nov. 2026) en het Volkshuisvestingsprogramma (uiterlijk 1-7-2027), formele provinciale instemming, inhoud van De Brinkweiden en Wijlandhof, netcongestie en een mogelijke tweede ronde, de gemeentelijke capaciteit.

### 2. Agrarische herbestemming: biedt het gemeentelijk beleid ruimte voor de omzetting van agrarisch bestemde grond naar een bouw- of woonfunctie op deze schaal?
- **(a) Gemeente:** op een **erf** alleen kleinschalig (Handreiking KGO: sloop voor woning, tot circa 6 woningen per erf in theorie; het recht op een woning in ruil voor sloop is volgens de raadssessie van 28-9-2026 "niet meer houdbaar" en de Handreiking wordt vervangen). Op **grond met agrarische bestemming bij een kern** zijn wel principebesluiten genomen voor 8 (Engeweg), circa 18 (Hemelrijk-2) en 20 woningen ('t Kleiland, binnen de kom); voor 10-12 woningen op een erf in het open buitengebied is geen kader gevonden.
- **(b) Provincie [PB]:** KGO met kwaliteitsinvestering (art. 4.11), landbouwgebied-typologie (art. 4.123-4.124: generiek, geen beperking voor omliggende landbouw; gebiedsspecifiek, investering gericht op water, klimaat en natuur; in de gemeente ongeveer half-half), programmering (80/20), Lijst BOPA (advies en instemming), redeneerlijn en energieparagraaf (art. 4.122, 4.125).
- **(c) Eindoordeel:** op **onbebouwde** agrarische grond buiten een kern **zeer kansarm**; op een **bestaand erf** alleen kleinschalig realistisch; **bij een kern** (klein of groot) zijn 10-20 woningen op grond met agrarische bestemming via BOPA of omgevingsplanwijziging in de praktijk bespreekbaar gebleken, mits lokale behoefte, binding, sloop/landschappelijke inpassing en provinciale instemming. Onzekerheden: zie hierboven, plus de afwijkende gemeentelijke en provinciale gebiedsindeling (juridisch geldt de provinciale kaart).

---

## Overijssel-controlepunten (Bijlage A)

Status: gevonden / niet gevonden / niet van toepassing / tegenstrijdig. Alle bronnen geraadpleegd 2026-10-04/05 en gelezen.

### A. Positie in het provinciale kader en woonafspraken
| # | Bevinding | Status | Bron | Bij niet gevonden: waar te vinden |
|---|---|---|---|---|
| A1 | "Overige kern" onder art. 4.4 [PB]; grote kernen Olst, Wijhe, Wesepe (Wesepe groeikern, circa 200 woningen tot 2032; de provincie stelt in zienswijze 23 vragen over Wesepe als "hoofdkern"); kleine kernen Boerhaar, Boskamp, Den Nul, Welsum, Herxen. Regio Zwolle-lidmaatschap bevestigd ("Salland is zowel onderdeel van de Stedendriehoek als van Regio Zwolle", Prb 2026, 10885 p. 124-125); visiekaart provincie: Dagelijks Stedelijk Systeem Zwolle en/of Stedendriehoek per kern (Herxen en Marle alleen Zwolle; Olst, Boskamp, Wesepe, Welsum alleen Stedendriehoek; Wijhe, Boerhaar, Den Nul, Elshof beide); ontwerp-VHP: woningbouwregio en woningmarktregio West-Overijssel. Een bijzonder groeiprofiel (buiten de stationsomgevingen in de Regio Zwolle-strategie) is niet gevonden; de uittreding in 2023 betreft de arbeidsmarktregio | Gevonden (positie); bijzonder profiel niet gevonden | Omgevingsvisie p. 5, 18-19, 38; nota van beantwoording zienswijze 23; Prb 2026, 10885 en 11834; https://ruimtelijkeplannen.overijssel.nl (visiekaart) | Verstedelijkingsstrategie Regio Zwolle/DSS; Deventer B&W-nota 2023-543 (pdf 404) |
| A2 | West-Overijssel; Woondeal 2025-2030 (20-3-2025): 8 projecten/841 woningen 2024-2030, 300 doorkijk [PB]; gemeente: 4 sleutelprojecten en geen extra opgave (1.000-1.200 al toegezegd), Woondeal noemt onderzoek naar extra kansen; Planmonitor 1-1-2026: hard 244/zacht 770 (locatiebekend); Engeweg Elshof hard (8), CPO Herxen en Boerhaar niet opgenomen; 80/20-ruimte en post kleine kernen: niet gevonden | Gevonden (deels) | B&W 8-4-2025; Woondeal p. 5, bijlage 1; WFS Geodata Overijssel (B82 Planmonitor) | Dashboard Wonen; 1-op-1-gesprek provincie-gemeente-corporaties |
| A3 | Lokale betaalbaarheid: 70% betaalbaar; sociale huur min. 25% (Woonvisie) resp. 30% (Woondeal/Wvrv); sociale koop I < € 267.000, betaalbaar < € 420.000 (2026); lokale binding max. 50% van nieuwbouw < € 405.000/€ 420.000 (geen verordening); Leidraad woningcategorieën geborgd via omgevingsplan/BOPA-voorschriften/anterieure overeenkomst; Engeweg: deel tot € 420.000, 1 vrijstaande vrij. Aangescherpte koopgrens kleine kernen en toepassing op CPO 10-12: niet gevonden | Gevonden (deels) | Grondprijzenbrief 2026 bijlage 1; RIB 10-11-2025; adviesnota Engeweg | Volkshuisvestingsprogramma; prestatieafspraken SallandWonen |
| A4 | Geen vastgesteld of ontwerp-Volkshuisvestingsprogramma; plan van aanpak B&W 18-8-2026; vaststelling uiterlijk 1-7-2027; Woonvisie afgelopen per 1-1-2026; voorbereiding op afschaffing ladder niet gevonden | Niet gevonden (in voorbereiding) | B&W 18-8-2026 punt 04 | RIB augustus 2026; raadsagenda 2026-2027 |
| A5 | Geen lokale doorvertaling woonzorgvisie; Omgevingsvisie noemt woonzorgconcepten; senioren-CPO's aanwezig; geen huisvestingsverordening/urgentieregeling (regionale modelverordening in voorbereiding); Starterslening-verordening 2026 op raadsagenda 5-10-2026 | Deels gevonden | §8, §12; RIB 10-11-2025 | Woonvisie wonen-zorg; team Wonen; SallandWonen |

### B. KGO, rood-voor-rood en rekenmodellen
| # | Bevinding | Status | Bron | Bij niet gevonden: waar te vinden |
|---|---|---|---|---|
| B1 | Eigen kader: Handreiking KGO (B&W 28-5-2024) met rekenregels (§3a); geen CVDR/Gemeenteblad; **CVDR305226 is Tubbergen (vervallen)**; "Nota Ruimtelijke Kwaliteit" als eerder KGO-beleid genoemd (datum onbekend) | Gevonden (document); niet in register | iBabs ba55b732-4944-450f-ab35-046ed41b697d; CVDR305226 | Nota Ruimtelijke Kwaliteit (iBabs) |
| B2 | Per bouwblok maximaal 3 woningen/1.200 m³; maximaal 2 bouwblokken per erf; 10-12 niet voorzien; kleinschalig 1-5 woningen alleen binnen de bebouwde kom | Gevonden | §3a; beleid 24-5-2024 | Handreiking; bouwsteen |
| B3 | Handreiking tijdelijk; bouwsteen Erfontwikkeling beoogd nov. 2026 (vervanging Handreiking); omgevingsplan nog tijdelijk deel (alle versies technisch); aanpassing aan Actualisatie 2026 (art. 4.2a) niet gevonden; gemeente erkent afwijkende gebiedsindeling t.o.v. provincie | Gevonden (deels) | RIB 9-6-2026; raadssessie 28-9-2026; CVDR696503 | Raadsagenda 26-10-2026; omgevingsprogramma |
| B4 | Contour bestaand bebouwd gebied niet vastgelegd; "kernrandzone/zoekgebied erfontwikkeling" en dorpsrandzone 200-300 m in uitwerking; Engeweg behandeld als agrarisch (BOPA); 't Kleiland als binnen de kom | Niet gevonden (contour) | §2, §3 | Omgevingsprogramma; integrale visiekaart |
| B5 | Sloop, erfinrichtingsplan Het Oversticht, landschappelijke inpassing, bos, Voorziening Ruimtelijke Kwaliteit; anterieure overeenkomst met nadeelcompensatie als harde voorwaarde; bankgarantie: niet gevonden; vereveningsfonds in overweging | Gevonden (deels) | Handreiking; adviesnota's; Gmb 2024, 460019 | Anterieure overeenkomst per project |

### C. Locatie-overlays
| # | Bevinding | Status | Bron | Bij niet gevonden: waar te vinden |
|---|---|---|---|---|
| C1 | Typologie per locatie bevraagd (tabel §3a): Engeweg, Middel, Lierderholthuisweg, Kleistraat, Bokkelerweg generiek; Vettewinkelweg, Marle, Welsum, Den Nul, Elshagenweg gebiedsspecifiek; kernen buiten landbouwgebied; gemeente: 37,8% generiek, 38,2% gebiedsspecifiek | Gevonden | ruimtelijkeplannen.overijssel.nl API (nld@129); WFS Geodata Overijssel | — |
| C2 | Gebiedsvisie art. 4.124 lid 4: niet gevonden; Herxen-visietraject en bouwsteen zijn mogelijke voertuigen [INT]; Engeweg: afwijking spuitzone, afwijkingsgronden lid 4 niet genoemd in de adviesnota | Niet gevonden | §3 | Bouwsteenstukken; provinciale accounthouder |
| C3 | Natura 2000 Rijntakken ≤ 100-500 m (IJsselzone); NNN: Uiterwaarden IJssel en Landgoederen Salland, geen projectlocatie erin; grondwaterbeschermingsgebied Boerhaar (Vettewinkelweg erin); Nationaal Landschap niet van toepassing; raatakkers/karrensporen niet aanwezig; geen "uitgesloten/kansrijke zones" voor wonen in de verordeningskaart; boringsvrije zone Salland Diep, overstroombaar gebied 93% | Gevonden | WFS Geodata Overijssel; viewer verordening | — |
| C4 | Redeneerlijn en energieparagraaf: gemeentelijke standaardonderbouwing niet gevonden. Netcongestie: beleidsregels Gmb 2026, 385444; 47 → 31 projecten; geen tweede ronde; collectieve woonvormen als categorie | Gevonden (netcongestie) / niet gevonden (rest) | §5 | Ruimtelijke onderbouwing per BOPA |

### D. VAB en erftransformatie
| # | Bevinding | Status | Bron | Bij niet gevonden: waar te vinden |
|---|---|---|---|---|
| D1 | Doet mee aan provinciale subsidie (bouwsteen € 30.000 van € 40.000; activiteit A); Raalte en Deventer nemen deel; intergemeentelijk programma open voor eind 2026; "4.39" niet bij nummer in de stukken | Gevonden | B&W 28-10-2025 punt 7 | Beschikking: vab@overijssel.nl |
| D2 | Erfcoach Overijssel Yvonne in 't Veld (Dalfsen, Olst-Wijhe, Ommen, Hardenberg); ervenconsulent Het Oversticht; Niek Oude Scholten niet meer op de lijst; Atelier Overijssel/Rijkshandreiking niet gevonden | Gevonden | https://erfcoachoverijssel.nl/contact-met-de-erfcoaches/ | — |
| D3 | Beleid via Handreiking KGO, bouwsteen, Omgevingsvisie (sloopmeters); precedenten (§3b, §4); Buurtschappenbeleid; geen CPO-VAB-precedent; VAB als aparte opgave in het volkshuisvestingsprogramma: niet gevonden | Deels gevonden | §3-§4 | Volkshuisvestingsprogramma |

### E. Procedure en provinciale betrokkenheid
| # | Bevinding | Status | Bron | Bij niet gevonden: waar te vinden |
|---|---|---|---|---|
| E1 | Naam provinciale accounthouder niet openbaar. Vooroverleg met de provincie vóór het principebesluit (Vettewinkelweg 2; Engeweg: "Ook de provincie heeft al ingestemd"); regionale Omgevingstafel IJsselland "in sommige gevallen" (https://www.odijsselland.nl/over/omgevingstafel; de gemeente neemt de tafel op in haar werkwijze; welke Olst-Wijhese dossiers er zijn behandeld is niet gevonden); bestuursovereenkomst B&W-GS Herxen (2-6-2026); provinciale instemming als voorwaarde in minstens 13 principebesluiten (§3b); 1-op-1-gesprek met CPO/VAB op de agenda: niet gevonden | Gevonden (deels) | adviesnota's; B&W-besluitenlijsten 2024-2026; B&W 2-6-2026; Handreiking p. 10-11 | Afdeling RO; OD IJsselland (secretaris Omgevingstafel); Overijssel Loket; Woo-verzoek voor vooroverlegreacties |
| E2 | Route: BOPA (Lijst BOPA, Prb 2024 nr. 1348) met **bindend raadsadvies bij > 3 woningen buiten/> 12 binnen de bebouwde kom** (CVDR704153); omgevingsplanwijziging voor kernuitleg (IJsseldal, Wengelerhoek, Hemelrijk-2). Doorlooptijden: Zandhuisweg 7 ca. 3 weken (9 woningen), Lierderholthuisweg 3 ca. 11 weken, Vettewinkelweg 2 ca. 15 weken (alle regulier) | Gevonden | CVDR704153; Gmb 2025, 154624; Gmb 2026, 302246 | — |
| E3 | Geen Olst-Wijhes stuk over de Uitzonderingenlijst. [INT]: Olst, Wijhe en Boskamp (> 1.000 inwoners) vallen binnen ≤ 11 woningen in bestaand bebouwd gebied; buitengebied geen vrijstelling [PB] §4.2. De 12-woningengrens in het raadsbesluit 2022 koppelt aan de Ladder, niet aan de provincie | Niet gevonden (toepassing) | `provincie_overijssel.md` §4.2; raadsvoorstel 38288-2021 | Vooroverlegcorrespondentie in het zaakdossier |
| E4 | Provinciaal blad (69 treffers op "Olst-Wijhe", 2023-2026) en Gemeenteblad doorzocht: **geen provinciale zienswijze, aanwijzing of onthouden instemming** tegen Olst-Wijhese plannen; geen geweigerde BOPA voor wonen in de Gmb-lijst. Instemmingen en vooroverlegreacties worden niet gepubliceerd (beperkte negatieve bevinding). Wel een positieve provinciale zienswijze op de ontwerp-Omgevingsvisie (nr. 23) en de gemeentelijke zienswijze op de provinciale visie (B&W 24-6-2025) | Niet gevonden (conflict) / gevonden (zienswijze visie) | Prb/Gmb SRU; nota van beantwoording | Zaakdossiers; provincie |

### F. Financiering
| # | Bevinding | Status | Bron | Bij niet gevonden: waar te vinden |
|---|---|---|---|---|
| F1 | Gevonden: 4.39 activiteit A (€ 30.000, bouwsteen; alleen voor gemeenten); "Meer bos in Overijssel" (Lierderholthuisweg 3 en bos op 5 locaties, B&W 16-10-2025); Fysieke investeringen leefbaar platteland via Leader/De Kracht van Salland (clubhuis Boerhaar, B&W 20-5-2025); pilot Wooncoaches (provinciale cofinanciering stopt na de pilot); Regio Deal Regio Zwolle II (gebiedsaanpak Wesepe; Rijk/regio, niet provinciaal); provinciale subsidie haalbaarheidsonderzoek kerk Wijhe. Betaalbaar wonen in kleine steden en dorpen, Flexpools, Vitaliteit dorpen, Langer zelfstandig wonen, Woonplatforms en Bouwbrigade: niet gevonden in de B&W-besluiten 2024-2026. Geen regeling rechtstreeks toepasbaar op een particulier collectief | Deels gevonden | B&W 22-9-2026, 16-10-2025, 20-5-2025, 22-4-2025; B&W 20-1-2026 | regelen.overijssel.nl; B&W-subsidiebesluiten |

### Houdbaarheid (herverifiëren vóór gebruik)
- Provinciebestand: zie §6.1 in `provincie_overijssel.md` (Actualisatie 2026-2, PS-besluit december 2026; Besluit regie volkshuisvesting 1-1-2027; subsidie 4.39; Werkboek/Handreiking KGO; provinciaal volkshuisvestingsprogramma, ontwerp Prb 2026, 11834). Controleer de geconsolideerde Omgevingsverordening (CVDR706717) en de kaartlaag landbouwgebieden vóór het citeren van artikelnummers of gebiedstypen.
- **Lokaal kan snel wijzigen:** bouwsteen Erfontwikkeling en vervanging van de Handreiking KGO (college, november 2026); Volkshuisvestingsprogramma en huisvestingsverordening (uiterlijk 1-7-2027); opvolger Nota Grondbeleid; leges 2027 (+ circa 23% voorgesteld); netcongestie (tweede ronde?); omgevingsplan "dorpen en buurtschappen"; Herxen-visietraject (start rond de jaarwisseling).
- **Meld bij gebruik:** de uitkomsten bij B3, C1, C2 en C4 zijn afhankelijk van provinciale regels die per 1-7-2026 zijn gewijzigd (landbouwgebied-typologie, redeneerlijn, energiesysteem) en die nog kunnen wijzigen; E2 hangt af van de Lijst BOPA (Prb 2024 nr. 1348).

---

## Tegenstrijdigheden en onzekerheden: stand na verificatie

Alle twintig tegenstrijdigheden uit het concept zijn aan de brondocumenten getoetst. De bijbehorende kaders in de tekst zijn verwijderd.

| # | Onderwerp | Uitkomst | Basis |
|---|---|---|---|
| 1 | Reikwijdte maxima 5/10 woningen | **Opgelost:** 5 = bovengrens kleinschalige initiatieven/transformatie **binnen de bebouwde kom**; "10 bij betaalbare koop" bestaat niet; buitengebied = Handreiking KGO | §2, beleid 24-5-2024 |
| 2 | Grondprijzenbrief 2026; legestarieven | **Opgelost:** € 280-450/m² voor PO-kavels; CVDR752237 is Olst-Wijhe, raad 24-11-2025, tarieven geciteerd | §5, §11 |
| 3 | Vaststelling Omgevingsvisie 12 of 13 mei | **Opgelost: 12 mei 2025**, unaniem | Besluitenlijst raad 12-5-2025 |
| 4 | Handreiking KGO: orgaan, datum, motie, sloopeis | **Opgelost:** B&W 28-5-2024 (geen raad); motie 13-11-2023; 2 vrijstaande woningen 2.000 m², 2 woningen in één blok 1.000 m² | §3a |
| 5 | Omgevingsplan CVDR696503 versies | **Opgelost:** 1-1-2024 → 17-4-2024 → 6-6-2025 → **3-9-2026**; alle gemeentelijke versies technisch | CVDR wti; Gmb 2024, 169225; 2026, 416930 |
| 6 | Extra Woondeal-opgave | **Opgelost:** beide uitspraken waar (opgave "landt" mede in Olst-Wijhe, maar toegerekend aan de 1.000-1.200) | B&W 8-4-2025; Woondeal p. 5 |
| 7 | Plancapaciteit 161/339 | **Niet oplosbaar:** in geen enkele bron teruggevonden; verwijderd. Vervangen door Planmonitor (hard 244/zacht 770, locatiebekend) | §5 |
| 8 | Sociale huur 25% of 30% | **Opgelost:** 25% minimum nieuwbouw (Woonvisie 2022); 30% regionale ondergrens/Woondeal/Wvrv; recentste lijn 30% | §8 |
| 9 | Aantal kernen 7 of 12 | **Opgelost:** 12 kernen en buurtschappen (visie, akkoord); 7 = statistische indeling [INT] | Omgevingsvisie p. 5, 13; akkoord p. 23 |
| 10 | Verkiezingscijfers | **Opgelost:** 9.244 stemmen op kandidaten, 9.325 uitgebracht, opkomst 60,1% | Proces-verbaal P 22-2 |
| 11 | Olstergaard-aantallen | **Opgelost:** 72 woningen (48 + 13 + 11) | wonen.olst-wijhe.nl/olstergaard |
| 12 | Klimboom 17 of 17-18 | **Opgelost:** 17 woningen (9 CPO, 4 sociale huur, 4 via inschrijving); 4-5 betaalbare woningen in de verkoop 2026; netlijst 18 | Gmb 2024, 142870; gemeentepagina |
| 13 | Grijs en Groen Wonen en Vriendenerf | **Opgelost:** twee projecten (Olstergaard, 11 appartementen; Ringmus 50, 12 woningen) | §7; Prb 2026, 11834 |
| 14 | Landschapsbeschrijving oeverwal/dekzand | **Opgelost:** IJsselzone en kommenlandschap westelijk, dekzandgronden oostelijk; consistent | Omgevingsvisie p. 5; Gmb 2026, 70702 |
| 15 | CPO "vijf tot circa vijftig woningen" | **Niet gevonden in enige Olst-Wijhese bron; verwijderd** | §1 |
| 16 | Nota Grondbeleid 2023-2026 of 2024-2028 | **Opgelost:** alleen 2023-2026 (raad 12-12-2022); 2024-2027 is Harlingen | §5 |
| 17 | Gemeenteblad-nummers netcongestie | **Opgelost:** Gmb 2026, 385444 (beleidsregels) en 422235 (voorlopige lijst); 415179 = Brunssum, 421329 = Lansingerland | §5 |
| 18 | Portefeuille Blind | **Opgelost:** wonen en ruimtelijke ordening/omgevingsplannen; grondbeleid en buitengebied bij Olthof | Akkoord p. 23 |
| 19 | Engeweg-woningtypen | **Opgelost:** 3 twee-onder-een-kap (6) + 2 vrijstaand = 8 | Adviesnota Engeweg p. 2 |
| 20 | Systematisch: modelsamenvattingen | **Gemitigeerd:** alle genoemde punten zijn aan de brontekst getoetst; resterende onzekerheden staan onder "Niet gevonden en openstaande punten" | — |

**Niet oplosbaar blijft:** #7 (plancapaciteit 161/339: geen bron), #15 (CPO-bandbreedte: geen bron), en de inhoud van Wijlandhof/De Brinkweiden, het formele provinciale instemmingsbesluit en de vaststelling van de contour bestaand bebouwd gebied (zie "Niet gevonden en openstaande punten"). **Kleine resterende afwijkingen tussen bronnen:** Engeweg staat in de Planmonitor als *hard* plan terwijl de volgordelijst projectrijpheid 6 ("andere bewijsstukken") geeft; de bouwstart is "eind 2026" (Salland1, gemeentepagina) of 2027 (volgordelijst); de gemeentepagina noemt het principebesluit "januari 2026" terwijl de besluitenlijst 3-2-2026 vermeldt (besluitenlijst is leidend); het bestuursakkoord noemt "tot en met 2031" en de gemeentestukken "tot 2032" voor de 1.000-1.200 woningen.

## Aanbevolen vervolgstappen (prioriteit)
1. Plan een informeel voorgesprek: conceptverzoek bij team Ruimtelijke Realisatie/Ruimte en Samenleving met wethouders Blind (wonen, RO) en Olthof (buitengebied, grondbeleid) en de kernenwethouder van de beoogde kern; vraag naar de inhoud van De Brinkweiden en Wijlandhof en naar de uitwerking van de motie van 26-5-2026.
2. Volg de **bouwsteen Erfontwikkeling** (collegebesluit beoogd november 2026; Handreiking KGO wordt vervangen) en het **Volkshuisvestingsprogramma** (uiterlijk 1-7-2027); leg de provinciale en de gemeentelijke gebiedsindeling naast elkaar voor elke kandidaatlocatie.
3. Vraag voor een concrete locatie de provinciale kaartlagen op (typologie, grondwaterbescherming, NNN) en laat de provinciale instemming in vooroverleg bevestigen (Omgevingstafel IJsselland: https://www.odijsselland.nl/over/omgevingstafel; Overijssel Loket).
4. Onderzoek de netcongestie-positie vóór elke grondaankoop of planologische procedure (geen tweede ronde aangekondigd; collectieve woonvormen hebben een eigen subcategorie).
5. Houd de leges 2027 (+ circa 23% voorgesteld) en het opvolgende grondbeleid (Nota Grondbeleid loopt eind 2026 af) in de gaten.
6. Corrigeer in `provincie_overijssel.md` §2.3 (CVDR305226) en §4.2/§6.3 (Omgevingstafel-URL): in deze commit doorgevoerd.
