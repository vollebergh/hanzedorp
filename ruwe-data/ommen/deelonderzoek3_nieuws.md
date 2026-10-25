# Gemeente Ommen: Deelonderzoek 3, Nieuws en actualiteit 2024-2026

## Verantwoording
- **Raadplegingsdatum:** 2026-10-06 (alle bronnen, tenzij anders vermeld; bij elke bron staat de eigen datum van publicatie).
- **Provincie en kader:** Overijssel, `provincie_overijssel.md` (stand 2026-10-02). Bijlage A van toepassing, Bijlage B (Gelderland) niet.
- **Model:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), uitgevoerd als subagent (deelonderzoek 3). Effort/reasoning-niveau niet expliciet ingesteld voor deze subagent.
- **Markeringen:** citaten zijn letterlijk uit de brontekst. **[PB]** = uit `provincie_overijssel.md`; **[TK]** = trainingskennis, niet live geverifieerd; **[INT]** = interpretatie; **[BER]** = eigen berekening; **[NIET-GELEZEN]** = alleen als zoekresultaat gezien, brontekst zelf niet geopend; **[WF]** = tekst via WebFetch-samenvatting (een klein model vat de pagina samen; daarom lager betrouwbaar dan een eigen curl-lezing, en waar mogelijk gecontroleerd).
- **Opgeslagen extracties:** `scratchpad/ommen/raw/d3/` (o.a. `art/*.txt` = 84 artikelen van ommen.nl/actueel, `act_urls.txt` = lijst van 444 nieuwsberichten van ommen.nl/actueel (pagina 0-45), `coalitie_cols.txt`, `volgordelijst.txt`, `cpo_uitvoeringsregels.txt`, `vabeval.txt`).

### Toegang en bereik per mediabron
| Bron | Status |
|---|---|
| ommen.nl/actueel (gemeentelijk nieuws) | Volledig gelezen via curl met browser-UA (geen certificaatproblemen op www.ommen.nl op 2026-10-06). Alle 46 overzichtspagina's doorgenomen (444 berichten, ca. 2022-2026); 84 berichten met woon-/CPO-/buitengebied-/bestuurssleutelwoorden in volle tekst gelezen. |
| woneninommen.nl (gemeentelijk woonplatform) | Gelezen (CPO-beleid, projectpagina's). |
| Vechtdal Centraal (Regiobode BV; regionale krant, opvolger van de Dedemsvaartse Courant-lijn [INT]) | Gelezen (curl, 200). |
| RTV Vechtdal | Gelezen (curl, 200). |
| Ommen City (ommencity.nl), RondOmmen (rondommen.nl), De Ommenaar (ommenaar.nl) | Ommen City en RondOmmen gelezen; De Ommenaar alleen als zoekresultaat gezien [NIET-GELEZEN]. |
| De Toren Hardenberg (detoren.net) | curl gaf bij het eerste artikel 200, daarna meerdere keren 403 ("Toegang geweigerd", WAF). Daarom resterende artikelen via WebFetch gelezen ([WF]). |
| Oost (oost.nl, regionale omroep Overijssel, "RTV Oost") | Gelezen (curl, 200). |
| De Stentor (destentor.nl) | **Niet toegankelijk:** curl levert alleen de "DPG Media Privacy Gate"; zoekopdracht beperkt tot ds.nl gaf 0 resultaten. Dit is de in de brief genoemde betaalmuur. |
| Gemeentelijke partijsites en programma's (VOV, VVD) | Gelezen. PRO Ommen, CDA, LPO, CU, D66-programma's niet (zie "Niet onderzocht"). |

## Kernbevindingen (kort)
1. **Er is op 2026-10-06 géén coalitie in vorming.** Na de gemeenteraadsverkiezingen van maart 2026 is een nieuwe coalitie VOV + CDA + PRO Ommen gevormd (11 van 17 zetels [BER]). Akkoord "Krachtige keuzes voor een verbonden samenleving" is op 26-6-2026 vastgesteld; de drie wethouders zijn op 2-7-2026 geïnstalleerd. Het vorige college (LPO, CDA, ChristenUnie, 2022-2026) is afgetreden.
2. **Wethouder Wonen: Alice van den Nieuwboer (CDA)**, in het nieuwe college óók Ruimtelijke Ordening (inclusief omgevingsplannen); zij is dezelfde CDA-wethouder die in 2022-2026 Wonen deed en CPO heeft opgezet. Rood-voor-Rood/buitengebied valt bij Sonja Rasenberg (PRO Ommen; "Ontwikkelperspectieven landelijk gebied", "Plattelandsontwikkeling landbouw"); landbouw (economische kant) bij René de Koff (VOV).
3. **CPO is in Ommen een normaal, beleidsmatig verankerd instrument** (raadsmotie maart 2022, Addendum Woonvisie november 2023, Uitvoeringsregels CPO mei 2024, subsidie 70% begeleider tot € 20.000, voorschot € 15.000 architect). Vijf CPO-projecten gerealiseerd of lopend (Lemele, De Meerkoet, Beerzerveld, Erve Arriërflier, Vinkenbuurt), elk 4-8 woningen en alle binnen of aan de rand van een kern/buurtschap, op gemeentelijke grond. Het nieuwe coalitieakkoord noemt "inzet op collectief particulier opdrachtgeverschap" expliciet als te onderzoeken instrument. Er is **ook een regeling voor een collectief dat zelf eigenaar is van grond zonder woonbestemming** (CPO-fonds, voorschot tot € 50.000 + anterieure overeenkomst; Uitvoeringsregels §4): dat is de enige route die lijkt op het concept van dit onderzoek.
4. **Schaal:** alle Ommense CPO's zijn klein (4, 6, 8, 8, 7 woningen). Het grootste dorpse project, Beerzerveld, is 34 woningen op agrarische grond (omgevingsplanwijziging aan de kern, op gemeentelijke grond), waarvan 8 CPO. Voor Vinkenbuurt (buurtschap in agrarisch gebied) vond de provincie 11 woningen "aan de forse kant"; het plan is teruggebracht tot 8. Dat is het sterkste lokale signaal dat 10-12 woningen buiten een kern provinciaal gevoelig ligt.
5. **Provinciale conflicten:** geen formele zienswijze, aanwijzing of onthouden instemming 2023-2026 gevonden (E4). Wel drie documenteerde provinciale remmende signalen: Vinkenbuurt-centrumplan (2021) afgewezen om het ruimtelijk ontwerp; Vinkenbuurt-woningaantal (reactie op plan van nov. 2024); Lemele-visie (maart 2026: provincie "terughoudend" bij uitbreidingslocaties). Daarnaast een positief signaal: gemeente en provincie versnellen samen Kardoen/Fluitekruid, Guido de Brès en Julianaschool (april 2025).
6. **Netcongestie is voor Ommen reëel en nieuw:** Enexis-update 16-7-2026 meldt Ommen Dante (MS-netdelen 1 en 5, afname) als nieuw knelpunt (fase 1a); sinds 1-7-2026 komen ook woningaansluitingen op een wachtlijst. De gemeente heeft een *Volgordelijst woningbouwprojecten Ommen 2026* (definitief 17-9-2026, 29 projecten; aanmelddeadline was 10-9-2026) en beleidsregels (CVDR765864). In Beerzerveld schuift de bouwstart op naar half april 2027 mede door netversterking. Het coalitieakkoord wil in omgevingsplannen "off-gridmogelijkheden" bij nieuwe woonprojecten.
7. **Stikstof:** kabinetspakket van minister Van Essen (26-6-2026) leidde op 10-8-2026 tot een trekkerprotest bij het gemeentehuis van Ommen (ca. 150-250 trekkers volgens bron) en op 9-9-2026 tot een regionale brief van Ommen, Dalfsen, Hardenberg, Staphorst en Zwartewaterland ("heldere en uitvoerbare stikstofmaatregelen"). De brief noemt het weer op gang brengen van vergunningverlening voor woningbouw als gedeeld doel. Of een Natura 2000-zone van het pakket in Ommen valt: niet geverifieerd.
8. **Erfcoach:** twee erfcoaches (Hendry van Ittersum, Yvonne In 't Veld) actief in Ommen (bericht 3-2-2025); vanaf 2026 organiseert de provincie dit via *Boerenperspectief Overijssel* (volgens het Ommense VAB-evaluatierapport). Een Plattelandscoach staat in het nieuwe coalitieakkoord.
9. **VAB/erftransformatie:** Rood-voor-Rood beleidsregels 2026 zijn in werking (CVDR757546, geldend vanaf 26-2-2026): 1 compensatiewoning bij ≥ 850 m² sloop, 2 woningen bij ≥ 2.000 m², maximaal 750 m³ per woning, alternatieve woonvormen (2+ wooneenheden) alleen binnen die 750 m³. Een intergemeentelijk VAB-programma/subsidie 4.39: geen aanvraag of toekenning gevonden; wel is een plan van aanpak voor de provinciale VAB-routekaart aangekondigd (H2 2025).
10. **Politieke verhoudingen:** de partijen in de coalitie (VOV, CDA, PRO) zijn alle drie CPO-vriendelijk in hun eigen stukken (VOV-programma: "Ruimte voor nieuwe woonvormen (CPO, tiny houses, splitsen)", "Uitbreiding in kernen én buitengebied", "rood-voor-rood eenvoudiger maken"). De ChristenUnie, de initiatiefnemer van de CPO-motie in 2022 (volgens het verhaal van Startercollectief Ommen), zit nu in de oppositie. Wel is Vlierlanden fase 3 (375 woningen) politiek omstreden vanwege Arriën.

---

# §10 Bestuurlijk klimaat (eerst, vanwege de expliciete vraag naar coalitievorming)

## 10.1 Is er op het moment van onderzoek een coalitie in vorming? Nee.
Controle op 2026-10-06: de coalitievorming is afgerond. Het nieuwe college is op 2-7-2026 geïnstalleerd, de formatie is dus ruim 3 maanden voorbij. Geen tussentijdse val, fractiebreuk of heropende formatie gevonden in ommen.nl/actueel (nieuwsoverzicht tot en met 5-10-2026), Vechtdal Centraal, De Toren of RTV Vechtdal. Wel loopt een **burgemeestersprocedure** (zie 10.5), die los staat van de coalitie.

## 10.2 Verkiezingsuitslag en zetelverdeling
Bron: Gemeente Ommen, "Definitieve uitslag gemeenteraadsverkiezingen 2026", 26-3-2026, https://www.ommen.nl/actueel/definitieve-uitslag-gemeenteraadsverkiezingen-2026/ (geraadpleegd 2026-10-06):

> Het centraal stembureau heeft op 26 maart 2026 de definitieve uitslag van de gemeenteraadsverkiezingen vastgesteld. In de gemeente Ommen waren 15.453 stemgerechtigden. In totaal zijn 10.114 stemmen uitgebracht, waarvan 27 blanco stemmen en 17 ongeldige stemmen. De opkomst komt daarmee op 65,45%.

| Partij | Stemmen | Zetels |
|---|---|---|
| Volkspartij Ommen Vooruit (VOV-Ommen) | 3.076 | 5 |
| CDA | 2.179 | 4 |
| Lokale Partij Ommen (LPO) | 1.381 | 2 |
| ChristenUnie | 1.279 | 2 |
| GroenLinks / Partij van de Arbeid (PvdA) = **PRO Ommen** [INT, zie hieronder] | 933 | 2 |
| VVD | 674 | 1 |
| D66 | 548 | 1 |
| Totaal | | 17 |

- **PRO Ommen = de lijst "GroenLinks / PvdA":** het coalitieakkoord noemt "Hilbert Moerman (PRO Ommen)" als fractievoorzitter van de coalitie; op de officiële lijst van gekozenen staat Moerman, H. onder "GroenLinks / Partij van de Arbeid (PvdA)". GroenLinks-PvdA heeft zich landelijk hernoemd naar PRO [TK, bevestigd via zoekresultaten naar Joop/Binnenlands Bestuur, niet zelf gelezen]. Dit is [INT], maar goed gedekt.
- **Coalitie = 5 + 4 + 2 = 11 van 17 zetels** [BER]. Oppositie: LPO (2), ChristenUnie (2), VVD (1), D66 (1) = 6.
- VOV-nummer 8 Carles Bembom is volgens de VOV-site gekozen met 312 voorkeurstemmen maar heeft "zijn zetel niet aanvaard" (VOV, "VOV ploeg bekend", 30-3-2026, https://www.vov-ommen.nl/index.php/2026/03/30/vov-ploeg-bekend/, alleen op homepage-intro gelezen). De namenlijst van ommen.nl (26-3-2026) toont hem nog als gekozene. De exacte raadsbezetting kan dus afwijken in de naam, niet in aantal.

## 10.3 Formatieverloop (tijdlijn, alle data volgens genoemde bronnen)
| Datum | Gebeurtenis | Bron |
|---|---|---|
| maart 2026 | Gemeenteraadsverkiezingen. [TK: landelijke datum 18 maart 2026; niet in de gelezen bronnen genoemd] | |
| 26-3-2026 | Definitieve uitslag; **duidingsdebat**: VOV, als grootste partij, draagt oud-minister **Frank de Grave** voor als verkenner. De Grave voert gesprekken met alle fracties; uitkomsten worden op **7 april** in een openbare bijeenkomst besproken. | ommen.nl 26-3-2026 https://www.ommen.nl/actueel/de-volkspartij-ommen-vooruit-draagt-frank-de-grave-voor-als-verkenner/ ; RTV Vechtdal 27-3-2026 https://rtvvechtdal.nl/?asset=8125&type=detail ; VOV-site 27-3-2026 https://www.vov-ommen.nl/index.php/2026/03/27/vov-neemt-initiatief-in-vorming-nieuw-bestuur/ |
| 7-4-2026 | Openbare bespreking van het verkennersadvies. **Het advies zelf en de verslaglegging zijn niet gevonden.** | zie "Niet gevonden" |
| begin april 2026 | "Na intensieve onderhandelingen, die begin april van start gingen" (VOV, CDA, PRO Ommen). | Ommen City 2-6-2026 https://ommencity.nl/2026/06/02/coalitieakkoord-ommen-op-hoofdlijnen-bereikt/ |
| 18-5-2026 | ChristenUnie bereidt zich voor op oppositie ("De realiteit is dat de ChristenUnie zich aan het voorbereiden is op oppositie voeren"), onderhandelende partijen zijn "positief gestemd". | Politiek Verwoord, Vechtdal Centraal, mei 2026 https://www.vechtdalcentraal.nl/2026/05/politiek-verwoord-277/ |
| 2-6-2026 | Overeenstemming **op hoofdlijnen**; kandidaat-wethouders René de Koff (VOV), Alice van den Nieuwboer (CDA), Sonja Rasenberg (PRO Ommen). | Vechtdal Centraal https://www.vechtdalcentraal.nl/2026/06/vov-cda-en-pro-ommen-op-hoofdlijnen-eens-over-coalitieakkoord/ ; Ommen City (zie boven) |
| 26-6-2026 | Akkoord **definitief vastgesteld**: "Krachtige keuzes voor een verbonden samenleving", bestuursperiode 2026-2030, "een coalitieakkoord op hoofdlijnen. De verdere uitwerking vindt plaats in het uitvoeringsprogramma van het college." | ommen.nl 26-6-2026 https://www.ommen.nl/actueel/vov-cda-en-pro-ommen-sluiten-coalitieakkoord/ ; PDF https://openpub.ommen.nl/wp-content/uploads/2026/06/Coalitieakkoord-Ommen-2026-2030.pdf (36 p.) |
| 1-7-2026 | Raad neemt afscheid van wethouders Leo Bongers (LPO; acht jaar wethouder, gaat met pensioen) en Bert Boerman (ChristenUnie, wethouder sinds oktober 2024; stopt "omdat de ChristenUnie geen deel uitmaakt van de nieuwe coalitie"; neemt zitting in de raad). | ommen.nl 2-7-2026 https://www.ommen.nl/actueel/gemeente-ommen-neemt-afscheid-van-wethouders-leo-bongers-en-bert-boerman |
| 2-7-2026 | Behandeling akkoord en **installatie** De Koff, Van den Nieuwboer, Rasenberg in extra raadsvergadering. | De Toren 3-7-2026 https://www.detoren.net/nieuws/ommen/112511/nieuw-college-aan-de-slag-voor-gemeente-ommen |

De Toren (3-7-2026): "Voor René de Koff en Sonja Rasenberg is het hun eerste periode als wethouder in Ommen. De Koff was hiervoor wethouder in de gemeente Rijssen-Holten. Alice van den Nieuwboer begint aan haar tweede termijn als wethouder."

**Politieke duiding voor CPO/collectieve woonvormen [INT]:** de drijvende kracht achter CPO in Ommen, wethouder Van den Nieuwboer (CDA), zit nog in het college én heeft Ruimtelijke Ordening erbij gekregen. De ChristenUnie, volgens het verhaal van Startercollectief Ommen de partij waar de CPO-groep in 2022 steun vond, valt buiten de coalitie, maar het CPO-beleid heeft brede steun (zie 1). De LPO (die onder wethouder Bongers het ruimtelijk-ordeningsdossier deed) is nu oppositie. Er is dus geen koerswijziging richting CPO te verwachten; de coalitie wil het juist "onderzoeken" als extra instrument voor het koopsegment.

## 10.4 Coalitieakkoord 2026-2030, relevante passages (letterlijk, PDF https://openpub.ommen.nl/wp-content/uploads/2026/06/Coalitieakkoord-Ommen-2026-2030.pdf, gelezen 2026-10-06; tweekoloms PDF, passages per kolom geëxtraheerd)

**Wonen (p. 10-11):**

> Verruimen instrumentarium. Op korte termijn gaan we onderzoeken of het instrumentarium van de gemeente kan worden verruimd. We willen bijvoorbeeld kijken of Vechtdal Wonen wellicht extra (financiële) ruimte heeft voor de realisatie van een onderbouwde behoefte aan extra sociale huurwoningen. Ook in het koopsegment gaan wij onderzoeken of het instrumentarium verder kan worden ingezet met bijvoorbeeld: startersleningen; erfpacht; anti-speculatiebeding; leegstandsheffing; zelfbewoningsplicht; inzet op collectief particulier opdrachtgeverschap.

> We willen meer mogelijkheden voor woningsplitsing en maatwerk. Nieuwbouw moet voor minimaal 30% uit sociale huur bestaan en aansluiten bij de vraag in gemeente Ommen.

> Samen met de raad werken we aan een vernieuwde woonvisie met meer ambitie. [...] De speerpunten in de visie waar wij in ieder geval graag met de raad over in gesprek gaan, zijn: het versnellen en (langdurig) verhogen van de bouwproductie; de vorming van meer wijken met een mix van woningtypes; het bevorderen en mogelijk maken van doorstroming; een (t)huis voor iedereen, van jong tot oud; klimaatbestendigheid, duurzaamheid en toekomstbestendigheid.

> Wij willen een lokale voorrangsregeling invoeren bij de toewijzing van woningen en bouwkavels om de positie van eigen inwoners op de woningmarkt te versterken. [...] Binnen de kaders van de Huisvestingswet stellen wij een huisvestingsverordening op [...]

(Let op: een huisvestingsverordening is dus nog **op te stellen**; in CVDR heb ik geen Ommense huisvestingsverordening gevonden, zie §8.)

> Zolang er woningnood is, gaan wij samen met recreatieparken kijken naar mogelijkheden voor het semipermanent bewonen van recreatiewoningen. [...] dit passend binnen het 'Afwegingskader vitale vakantieparken'.

**Buitengebied en landbouw (p. 25-27):**

> Ook moet er ruimte zijn voor woningbouwontwikkeling naar behoefte in de kernen. Hierbij zetten we vooral in op starters- en seniorenwoningen.

> [Wij willen de agrariërs ondersteunen] door: [...] ruimte te bieden voor hergebruik van agrarische gebouwen voor wonen en natuur, de Rood voor Rood-regeling en ontwikkeling, woningsplitsing, visie Rood voor Groen-regeling; [...] beleid te ontwikkelen voor niet-agrarische bedrijven in het buitengebied;

> Natuur en groen in het buitengebied [...] Regelingen zoals Rood voor Rood en Rood voor Groen helpen daarbij.

> **Plattelandscoach** [...] willen we de komende periode een plattelandscoach aanstellen. Deze medewerker van de gemeente kent de agrarische sector als geen ander en is op de hoogte van wet- en regelgeving. Daarnaast kan deze persoon agrariërs adviseren over beschikbare subsidieregelingen. [...] in eerste instantie voor een periode van drie jaar [...] Na twee jaar is er een tussentijdse evaluatie.

**Duiding [INT]:** het akkoord is *kern-gericht* voor nieuwbouw ("woningbouwontwikkeling naar behoefte in de kernen", vooral starters en senioren) en *erf-/sloopgericht* voor het buitengebied (hergebruik agrarische gebouwen, Rood-voor-Rood, splitsing). Nieuwe, losse woningbouw op onbebouwde agrarische grond buiten de kernen wordt niet genoemd. CPO wordt genoemd als instrument in het koopsegment.

**Energie en netcongestie (p. 19-20):**

> In de omgevingsplannen willen wij ruimte bieden aan off-gridmogelijkheden bij de realisatie van nieuwe woonprojecten.

> bij windmolens en netcongestie blijven we ons actief inzetten om met de provincie en andere partners in gesprek te blijven;

**Drinkwater Hammerflier (p. 18-19), relevant voor het Vechtdal en de provinciale verhouding:**

> Gemeente Ommen kijkt samen met gemeente Twenterand, Vitens en Vechtstromen naar de drinkwateropgave in Hammerflier. We kiezen alleen voor uitbreiding van de drinkwaterwinning als eerst voldoende is ingezet op waterbesparing. Uitgangspunt is ook dat de voorwaarden voor landbouw, woningen, natuur en het winnen van drinkwater niet mogen verslechteren.

**Verkeer en ontsluiting (p. 14-15):** onderzoek met Provincie Overijssel, Rijkswaterstaat en gemeenten naar een aansluiting vanaf Vlierlanden op de N36 en een zuidelijke ontsluiting ("onderzochte tracévarianten [...] forse impact op landschap, leefbaarheid en omliggende kernen als Giethmen en Vilsteren"). Bij nieuwe woningbouwlocaties moet "de ontsluiting en verkeersafwikkeling vooraf aantoonbaar op orde zijn".

**Portefeuilleverdeling (p. 34, tabel, via pdfplumber-tabel):**
| Bestuurder | Relevante portefeuilles |
|---|---|
| Burgemeester (Annemiek Jetten, waarnemend) | Beleidscoördinatie, openbare orde en veiligheid, toezicht en handhaving incl. APV en bestuurlijke vertegenwoordiging Omgevingsdienst, samenwerkingen |
| René de Koff (VOV), 1e loco | Financiën; Economie inclusief Centrum en landbouw (agrarisch); Bedrijven en bedrijfsterreinen; Recreatie en toerisme; Verkeer en mobiliteit; Openbare ruimte |
| **Alice van den Nieuwboer (CDA), 2e loco** | **Ruimtelijke Ordening (inclusief omgevingsplannen); Volkshuisvesting, wonen**; (Jeugd)Zorg, volksgezondheid en inclusie; Cultuur; Vrijwilligerswerk en mantelzorg; Dienstverlening, bedrijfsvoering en organisatie (max 1 jaar) |
| Sonja Rasenberg (PRO Ommen), 3e loco | Onderwijs; Vitale kernen; Armoedebestrijding en Werk & inkomen; **Gemeentelijke eigendommen; Ontwikkelperspectieven landelijk gebied; Plattelandsontwikkeling landbouw**; Duurzaamheid, klimaat, natuurbeheer en water; Immigratie en integratie |

**Naam en portefeuille wethouder Wonen:** Alice van den Nieuwboer (CDA), "Volkshuisvesting, wonen" én "Ruimtelijke Ordening (inclusief omgevingsplannen)". Ze noemde zichzelf in een eerder interview "14 jaar inwoner" van Ommen en deed ook in 2022-2026 Wonen (ommen.nl 9-3-2026, 28-8-2025 en andere berichten noemen haar in die rol). Haar gemeentelijk contact: gemeente@ommen.nl, tel. 14 0529 (er is geen publiek e-mailadres per wethouder gevonden).

## 10.5 Burgemeester en college (context)
- Burgemeester **Hans Vroomen** (CDA) is "met ingang van 10 april 2026 eervol ontslagen" (ommen.nl 26-3-2026, https://www.ommen.nl/actueel/annemiek-jetten-waarnemend-burgemeester-in-ommen). Daarvoor was **Tjeerd van der Zwan** waarnemend burgemeester vanaf 20-12-2024 wegens ziekte van Vroomen (ommen.nl 19-12-2024, https://www.ommen.nl/actueel/tjeerd-van-der-zwan-waarnemend-burgemeester-in-ommen).
- **Annemiek Jetten** (PvdA) is per 16-4-2026 waarnemend burgemeester. De Rijksoverheid heeft de vacature opengesteld ("vacant sinds 10 april 2026", reageren vóór 8-8-2026); de raad heeft per 14-7-2026 een vertrouwenscommissie (CVDR764217, "Verordening op de vertrouwenscommissie gemeente Ommen 2026"). Stadindex (Stentor-regio-aggregator, kop van 12-8-2026): "36 sollicitanten willen burgemeester van Ommen worden". Geen voordracht gevonden per 2026-10-06 [niet gevonden].
- Vorig college (2022-2026): LPO, CDA, ChristenUnie, akkoord "Bouwen aan de toekomst" (7-6-2022, ommen.nl https://www.ommen.nl/actueel/lpo-cda-en-christenunie-sluiten-coalitieakkoord-in-ommen). Daarin stond al: "Ruimte bieden voor woningbouw in de kernen via onder meer CPO" en "Zorgen dat Ommenaren in Ommen of kernen terecht kunnen voor een woning (huur of koop). Het daartoe optimaal benutten van de mogelijkheden binnen de wettelijke kaders, zoals collectief particulier opdrachtgeverschap." (Coalitieakkoord 2022-2026, https://www.ommen.nl/wp-content/uploads/2022/09/Coalitieakkoord_op_hoofdlijnen_2022-2026.pdf, gelezen 2026-10-06), plus "Continueren erfcoaches" en "De recent vastgestelde rood-voor-rood regeling evalueren we conform het raadsbesluit in 2023".

## 10.6 Partijstandpunten (verkiezingsprogramma's)
- **VOV** (grootste partij), programma 2026 (https://www.vov-ommen.nl/wp-content/uploads/2026/02/VOV-VERKIEZINGSPROGRAMMA-2026.pdf, gelezen 2026-10-06):
> Betaalbaar wonen: Voorrang voor inwoners van de gemeente Ommen bij nieuwe woningen; Eerst woonbehoefte bepalen, dan bouwen; Uitbreiding in kernen én buitengebied; Gemeente pakt regie op woningbouw; Verplicht aandeel betaalbare woningen per project; Ruimte voor nieuwe woonvormen (CPO, tiny houses, splitsen); Mantelzorg-, flexwoningen en rood-voor-rood eenvoudiger maken

> Daarnaast dienen wij te kijken of meer CPO-projecten mogelijk zijn in de gemeente Ommen. [...] Wij steunen het rood-voor-roodbeleid als instrument om vervallen of ongebruikte agrarische bebouwing op te ruimen en daar passende woningen voor terug te brengen, rekening houdend met de omliggende bedrijven, behoud van het landschap en respect voor de omgeving.

> Oude stallen kunnen plaatsmaken voor woningen of worden omgebouwd voor nieuwe functies. Zo versterken we landbouw én de woningmarkt. (https://www.vov-ommen.nl/index.php/landbouw-en-natuur-in-balans/, gelezen 2026-10-06)

- **VVD Ommen** 2026-2029 (oppositie; https://www.vvd.nl/wp-content/uploads/sites/324/2026/02/VVD-Ommen-Verkiezingsprogramma-2026.pdf): "Tiny Houses of inwoning op eigen erf kan en is snel te regelen"; "Per kern 25 extra startersplekken in 12 maanden [...] Er zijn al enkele locaties aangemerkt als toekomstige uitbreidingslocaties in buitengebied. Inzet van flexwoningen is hier een prima mogelijkheid voor."; wil 2.000 nieuwe woningen tot 2040 in plaats van 1.250.
- CDA, PRO Ommen, LPO, ChristenUnie, D66: programma's niet gelezen.

**Indicatie ruimte voor initiatieven als CPO [INT]:** hoog voor kleine CPO's in of aan kernen en voor erfontwikkeling via Rood-voor-Rood; voor een cluster van 10-12 woningen op onbebouwde agrarische grond buiten een kern staat er in coalitieakkoord of programma's geen expliciete toezegging.

---

# §1 CPO-beleid (aanvulling vanuit nieuws en gemeentelijke publicaties)

## 1.1 Besluitvorming en beleidsstukken (volgens nieuwsberichten en gemeentelijke pagina's)
- **Maart 2022, raadsmotie:** "In de raadsvergadering van maart 2022 is een motie aangenomen die het bouwen in CPO moet stimuleren in Ommen." (ommen.nl 17-11-2023, "Oprichting Starters Collectief Ommen", https://www.ommen.nl/actueel/oprichting-starters-collectief-ommen)
- **Voorjaar 2023:** de gemeente wijst "drie locaties aan voor CPO-projecten"; **2024** "volgde goedkeuring van het nieuw beleid" (Startercollectief-verhaal, ommen.nl 20-12-2024).
- **November 2023, Addendum Woonvisie:** de CPO-uitvoeringsregels geven "invulling aan het vastgestelde woonaddendum november 2023 om bouwen door middel van CPO in de gemeente Ommen te stimuleren". Het addendum bevat een gemeentelijke woningbouwprogrammering (12 locaties; ca. 1.250 extra woningen voor de kern Ommen) (woneninommen.nl Erve Arriërflier; ommen.nl 12-12-2024 prestatieafspraken).
- **Mei 2024, Uitvoeringsregels CPO** (PDF 5 p., https://a.storyblok.com/f/284824/x/cfd69c0eea/uitvoeringsregels-cpo-gemeente-ommen_mei-2024.pdf, gelezen 2026-10-06; ook gelinkt vanaf https://woneninommen.nl/woonbeleid/cpo). Kernpunten, letterlijk:

> Voor elke CPO-locatie (de locaties die de gemeente beschikbaar stelt voor CPO), wordt er een kopersvereniging opgericht die bestaat uit evenveel leden als mogelijk aantal woningen/kavels. [...] De juridische entiteit "Vereniging met volledige rechtsbevoegdheid" stellen we verplicht [...] In de statuten dient de doelgroep benoemd te worden én de zelfbewoningsplicht c.q. plicht om de woning voor eigen gebruik te ontwikkelen te worden opgenomen. Verhuur en/of speculatie is niet toegestaan.

> De gemeente stelt de vereniging een subsidie ter beschikking voor het inhuren van de onafhankelijk procesbegeleider voor 70% van de geoffreerde kosten tot een maximum van €20.000,- [...] De gemeente stelt de vereniging een voorschot ter beschikking van €15.000,- om een deel voor te financieren voor het inhuren van een architect die is aangesloten bij BNA. Terugbetaling van dit voorschot geschiedt bij overdracht van de kavels. [...] De gemeente stelt per locatie een projectleider ter beschikking die aanspreekpunt zal zijn voor de vereniging

> Wanneer het college besluit CPO-kavels uit te geven, dan gebeurt dit door middel van een uitgifte via inschrijving. Hierbij worden de CPO-kavels als één geheel gereserveerd voor de vereniging [...]. Voor bepalen van de grondprijzen voor CPO-kavels is de geldende grondprijsbrief, welke is vastgesteld door het college, het uitgangspunt.

> **4. CPO-project zonder gemeentelijke gronduitgifte.** Het is mogelijk dat een CPO-collectief eigenaar is van een perceel waar op dit moment geen woonfunctie mogelijk is, maar waar de gemeente wel positief tegenover staat om de activiteit wonen mogelijk te maken. Hiervoor geldt dat de gemeente een budget beschikbaar stelt, met een maximum van €50.000. Het gaat hier om een CPO-fonds (in de vorm van een terug te betalen voorschot) om werkzaamheden (bijv. uitvoeren van onderzoeken) voor te financieren. De beschikbare middelen worden vastgelegd in een anterieure overeenkomst tussen collectief en gemeente Ommen.

> Het huidige StartersCollectiefOmmen is een overkoepelende vereniging en dient als kennis- en ervaringsplatform. (voetnoot)

  Doelgroepen: "(koop)starters, senioren en bijzondere wooninitiatieven". Welstand: "Het Oversticht". Participatieplicht: aangrenzende grondeigenaren in een straal van 300 meter informeren.
- **CPO-pagina Wonen in Ommen** (https://woneninommen.nl/woonbeleid/cpo, gelezen 2026-10-06): "Praktijkvoorbeelden laten zien dat het in 2025 nog steeds mogelijk is om een woning te bouwen binnen een VON-prijs van €220.000 tot €250.000."
- **CPO in het nieuwe akkoord:** zie 10.4.

## 1.2 Nuance voor ons concept [INT]
Het Ommense CPO-beleid is (a) ontworpen voor **gemeentelijke kavels binnen of aan kernen/buurtschappen**, (b) gericht op **lokale starters en senioren met binding**, (c) met **max. 1 woning per lid**, en (d) staat sinds mei 2024 ook open voor een collectief dat **eigen grond** inbrengt (§4), met een voorschot tot € 50.000. Er staat geen maximum aantal woningen in de uitvoeringsregels; de uitgegeven projecten zijn 4-8 woningen groot.

---

# §7 Inventarisatie bestaande initiatieven (CPO, collectief, zelfbouw)

| # | Initiatief | Woningen | Status per 2026-10-06 | Bron (datum) |
|---|---|---|---|---|
| 1 | **CPO LemeleWoont** (eerste Ommense CPO) | 4 (twee-onder-een-kappers) | Kavels in 2022 verkocht via de vereniging, bouw 2022 gestart. Drie starters en één doorstromer. Op inbreidingslocatie (voormalige speellocatie en groenstrook). Vervolg: ouderen aan de Bulmensteeg; "Kruispunt Bulmensteeg-Lemelerweg (CPO)", 8 woningen, staat op de Volgordelijst 2026 (positie 12). | ommen.nl 3-3-2022 https://www.ommen.nl/actueel/lemele-gaat-zelf-bouwen-voor-starters ; Volgordelijst 17-9-2026 |
| 2 | **Startercollectief Ommen, project De Meerkoet** (eerste groep via de nieuwe regels) | 6 woningen, 7 leden | Vereniging opgericht nov. 2023; koopovereenkomst kavel getekend 11-12-2024. Bouwstart/oplevering niet gevonden. | ommen.nl 17-11-2023 ; 20-12-2024 https://www.ommen.nl/actueel/startercollectief-ommen-pioniers-in-samen-bouwen-met-cpo ; woneninommen.nl/hoofdproject/meerkoet |
| 3 | **Vereniging CPO Beerzerveld** (Van Alewijkstraat) | 8 rijwoningen | Inschrijfprocedure juni 2025 (7-8 leden, binding Beerzerveld); samenwerkingsovereenkomst getekend 20-8-2025. Kavels naar verwachting bouwrijp dec. 2026; bouwstroom pas ± half april 2027 (zie §6/§11). | ommen.nl 10-6-2025, 28-8-2025, 1-9-2026 |
| 4 | **Starters Collectief Ommen, Erve Arriërflier** (Vlierlanden-noord) | **8** CPO-starterswoningen (de gemeente: 8 in de inschrijfprocedure en op de Volgordelijst; De Toren 25-11-2025 meldt "tien") van ca. 50-60 woningen | Samenwerkingsovereenkomst getekend 4-3-2026. Omgevingsplanwijziging gericht op definitief "halverwege 2026" (niet bevestigd in de bronnen dat dit gelukt is). Volgordelijst: "Vlierlanden Erve Arrierflier (CPO), 2x XL kavels, 8 CPO, 24 sociale verhuur, rest koop", 50 woningen, positie 18. | ommen.nl 9-3-2026 https://www.ommen.nl/actueel/cpo-verenigingen-erve-arrierflier-en-vinkenbuurt-zetten-volgende-stap-samenwerkingsovereenkomsten-ondertekend ; inschrijfprocedure https://a.storyblok.com/f/284824/x/68bc289a9c/inschrijfprocedure-cpo-erve-arrierflier.pdf ; De Toren [WF] 25-11-2025 |
| 5 | **Vereniging CPO Vinkenbuurt** (voormalige OBS, Koloniedijk 22a, buurtschap) | 7 CPO-rijwoningen + 1 vrije kavel (= 8) | Vereniging eind jan. 2026 bij notaris opgericht; samenwerkingsovereenkomst 4-3-2026; omgevingsplan "in het derde kwartaal van 2026 definitief" (doel). Zie §6 voor de provinciale terugkoppeling. Niet op de Volgordelijst. | ommen.nl 9-3-2026 ; inschrijfprocedure https://a.storyblok.com/f/284824/x/51e6798acc/inschrijfprocedure-cpo-vinkenbuurt.pdf ; woneninommen.nl/hoofdproject/vinkenbuurt |
| 6 | **Haven Oost hofwoningen** (jong + oud, geen CPO) | 11 seniorenwoningen + 4 jongerenwoningen, gemeenschappelijke binnentuin en ontmoetingsruimte | Opgeleverd 2024 (Vechtdal Wonen). Een "collectief-achtig" woonconcept, maar corporatiebouw. | ommen.nl 12-12-2024 |
| 7 | **Hof van Vlierlanden** | 20 levensloopbestendige hofwoningen rond een gezamenlijke hof + 12 starterswoningen | Gebouwd (IJsselland Ontwikkeling); in voorselectie Nationale Houtbouwprijs 2026 (stemmen t/m 13-11-2026). Geen CPO; ontwikkelaarsproject met collectief hof. | woneninommen.nl nieuws |
| 8 | **Vrije kavels (zelfbouw)** | Haven Oost 5 vrije kavels (inschrijving 10-28 nov. 2025); Beerzerveld 6 vrije kavels (2 vrijstaand, 4 twee-onder-een-kap, onder optie); Vlierlanden fase 2 C&D (nov. 2022) | Toewijzing via puntensysteem op het betaalde account van woneninommen.nl. | ommen.nl 24-10-2025, 20-10-2025, 7-11-2025 |
| 9 | **Flexwoningen Sportlaan** | 50 tijdelijke huurwoningen (15 jaar) | Eerste 17 opgeleverd en bewoond per 5-10-2026. | ommen.nl 5-10-2026 https://www.ommen.nl/actueel/nieuwe-bewoners-ontvangen-sleutel-van-hun-woning-aan-de-sportlaan |

Opmerking: in de gelezen bronnen is **geen cohousing- of "knarrenhof"-initiatief van burgers** gevonden. "Landgoed Junne" (9 woningen op de Volgordelijst) en "Lemmers Erve zorgontwikkeling (Stekkenkamp)" (55) zijn projecten van marktpartijen; hun aard (rood-voor-groen/landgoedregeling resp. zorgontwikkeling) is niet nader onderzocht.

---

# §6 Praktijkvoorbeelden 2024-2026 (chronologisch)

| Datum | Voorbeeld | Relevantie voor ons concept | Bron |
|---|---|---|---|
| 20-12-2024 | Startercollectief Ommen tekent koopovereenkomst De Meerkoet (6 woningen); wethouder: "We hopen dat dit meer mensen inspireert zelfstandig nieuwe woningen te ontwikkelen." | Bewijs dat een CPO-groep via de nieuwe regels grond kan kopen. | ommen.nl 20-12-2024 |
| 30-1-2025 | Raad stemt in met middelen voor woningbouw Vinkenbuurt (8-10 kleine woningen, starters, senioren, 1-2 personen). | Kleine woningbouw in een buurtschap. | woneninommen.nl "Betaalbare woningen in Vinkenbuurt" |
| 3-2-2025 | Erfcoaches Hendry van Ittersum en Yvonne In 't Veld gepresenteerd. | Gratis eerste gesprek over erf, Rood voor Rood, VAB. | ommen.nl 3-2-2025 https://www.ommen.nl/actueel/de-erfcoach-staat-voor-u-klaar |
| 25-2-2025 | Bouwclaimovereenkomst met Bemog; **gemeente koopt varkenshouderij Arriërveldsweg** voor Vlierlanden III (375 woningen). | Gemeente koopt agrarisch bedrijf om woongebied te maken; stikstof/agrarische omzetting op grote schaal bij een stadsrand. | ommen.nl 27-2-2025 |
| 2-4-2025 | Concept-beleidsnotitie woningsplitsing in buitengebied ter inzage (3-4 t/m 14-5-2025); vastgesteld okt. 2025 (CVDR745908). | Splitsen van bestaande (voormalig agrarische) woningen: geen nieuwbouw, wel extra woningen. | ommen.nl 2-4-2025 ; CVDR745908 |
| 16-4-2025 | Gemeente en provincie bekijken "versneld" bouwen op Kardoen/Fluitekruid; college verwijst naar de woondeal (28.200 woningen in Overijssel tot 2030; Ommen 508; 2022-2024: 290 gebouwd). | Positieve provinciale samenwerking; woonafspraken. | RTV Vechtdal 16-4-2025 https://rtvvechtdal.nl/?type=detail&asset=5717 |
| 18-4-2025 | "Verhit debat" in de raad over Vlierlanden 3 (375 woningen) met omwonenden van Arriën en de LPO-voorzitter; fractievoorzitters van CDA en VOV tonen begrip voor zorgen. | Politieke weerstand bij uitbreiding naast een agrarisch buurtschap. Let op: VOV en CDA zitten nu in de coalitie. | Ommen City 18-4-2025 https://ommencity.nl/2025/04/18/verhit-debat-over-woningbouwproject-vlierlanden-3/ |
| 8-5-2025 | Raadsvergadering gebiedsvisie Vlierlanden 3 (omwonendencollectief: "rammelt aan alle kanten"; wethouder Bongers draagt dossier over omdat hij zelf in het plangebied woont). | Idem. | Vechtdal Centraal 5/2025 https://www.vechtdalcentraal.nl/2025/05/bewoners-waarschuwen-gebiedsvisie-vlierlanden-fase-3-rammelt-aan-alle-kanten/ |
| 10-6-2025 | Uitgifte van 8 rijwoningen in Beerzerveld aan CPO-vereniging; 34 woningen op voormalig agrarische grond. | Zie §3/§7. | ommen.nl 10-6-2025 |
| 10-7-2025 | Raad stemt in met "eerste wijzigingsbesluit omgevingsplan" Beerzerveld: "34 nieuwe woningen te realiseren op de agrarische grond aan de Van Alewijkstraat". Onherroepelijk 20-10-2025. | **Dichtstbijzijnde precedent voor omzetting agrarische grond naar woningbouw op deze schaal** (34 in plaats van 10-12), maar gemeentelijke grond aan een kern, als expliciete uitbreidingslocatie. | ommen.nl 22-7-2025 https://www.ommen.nl/actueel/gemeenteraad-stemt-in-met-wijziging-omgevingsplan-voor-woningbouw-beerzerveld ; 20-10-2025 |
| 1-10-2025 | Ontwerp geactualiseerde Rood-voor-Rood beleidsregels + evaluatierapport ter inzage (t/m 12-11-2025). | VAB-beleid; zie §4. | ommen.nl 1-10-2025 |
| 14-10-2025 | College wil bebouwde kom Beerzerveld verleggen voor de nieuwbouw (snelheid 60 → 30). | Praktische inpassing van een uitbreiding. | De Toren [WF] 14-10-2025 |
| 25-11-2025 | Gemeente start aanbesteding CPO-starterswoningen Erve Arriërflier. Risico's genoemd: "Recente uitspraken van de Raad van State over stikstof zorgen voor enige onzekerheid bij latere vergunningprocedures." en "Ook bestaat het risico dat een CPO-vereniging tijdens het traject uiteenvalt; in dat geval kan de gemeente het perceel verkopen aan een projectontwikkelaar." | Stikstof en uiteenvallen CPO als risico's in het proces. | De Toren [WF] 25-11-2025 (Grietje Grendelman) |
| 27-11-2025 | Raad neemt LPO-motie aan voor actualisatie grondbeleid (herziene nota uiterlijk november 2027); doel o.a. "versnelling van woningbouw, betere regie op beschikbare gronden en het mogelijk maken van diverse woonvormen". | Grondbeleid wordt herzien in deze periode. | De Toren [WF] 27-11-2025 |
| 1-12-2025 | 130 inwoners bij conceptvisie Lemele (tot 2035 en verder, focus woningbouw). | Dorpsgerichte groei; zie §2. | ommen.nl 10-12-2025 |
| 19-12-2025 | Intentieovereenkomst met NGK Ommen voor nieuw kerkgebouw met zorggeschikte woningen aan de Trompstraat. | Zorgwoningen: aansluiting bij Bijlage A (A5). | ommen.nl 19-12-2025 |
| 13-1-2026 | Wethouder Bongers (LPO) kondigt aan te stoppen na de verkiezingen. | Politieke context. | ommen.nl 13-1-2026 |
| 30/31-1-2026, 25-3-2026 | MeeDenkDagen Vlierlanden fase 3 (375 woningen; > 350 bezoekers eerste ronde). | Participatie bij grote uitbreiding. | ommen.nl 15-1-2026 en 12-3-2026 |
| 11-2-2026 | Koop- en realisatieovereenkomst 20 woningen Beerzerveld (Vechtdal Wonen 10 sociale huur + Le Clercq/Nikkels 10 koop). | Mix van sociale huur, koop, CPO, kavels in een kleine kern. | ommen.nl 12-2-2026 |
| 18-2-2026 | Inschrijving CPO Vinkenbuurt gesloten. | Zie §7. | CPO-procedure |
| 26-2-2026 | Rood-voor-Rood Beleidsregels 2026 in werking (CVDR757546). | Zie §4. | CVDR |
| 4-3-2026 | Lemele-visie: ca. 80 woningen nodig tot 2031; college kiest voor uitbreiding naast inbreiding; **provincie "terughoudend"**. | Provinciale houding t.o.v. uitbreiding; zie E4. | Vechtdal Centraal 3/2026 https://www.vechtdalcentraal.nl/2026/03/stedenbouwkundige-visie-voor-lemele-wordt-leidraad-voor-nieuwe-woningbouw/ ; RTV Vechtdal asset 8012 |
| 4-3-2026 | Samenwerkingsovereenkomsten CPO Vinkenbuurt en Starters Collectief Arriërflier. | Zie §7. | ommen.nl 9-3-2026 |
| 26-6-2026 | Kabinetspakket stikstof (Van Essen). | Zie §9 hieronder. | |
| 10-8-2026 | Trekkerprotest bij gemeentehuis Ommen. | Stemming platteland. | stadindex.nl 10/11-8-2026 |
| 28-8-2026 | Beleidsregels prioriteit transportcapaciteit woningbouwprojecten Ommen 2026 (CVDR765864). | Netcongestie, zie C4. | CVDR |
| 1-9-2026 | Planning Beerzerveld gewijzigd. | Zie C4. | ommen.nl 1-9-2026 |
| 9-9-2026 | Regionale stikstofbrief met Dalfsen, Hardenberg, Staphorst en Zwartewaterland. | Zie boven. | ommen.nl 9-9-2026 |
| 5-10-2026 | Plaatselijk Belang Arriën: "onvoldoende kennis en onderzoek [...] over de locatie" Vlierlanden 3. Geen reactie van het college gerapporteerd. | Lopend lokaal verzet. | De Toren [WF] 5-10-2026 |
| 5-10-2026 | Eerste 17 flexwoningen Sportlaan opgeleverd. | | ommen.nl 5-10-2026 |

---

# Overige onderwerpen §1-§12 (voor zover dit brontype iets oplevert)

## §2 Openheid voor nieuwbouw buiten woonkernen
- **Gemeentelijke houding in de praktijk:** de gemeente breidt zowel de hoofdkern (Vlierlanden fase 3, 375 woningen aan de stadsrand tegen buurtschap Arriën; Erve Arriërflier; Haven Oost 110; Guido de Brès 56-60; Julianaschool 22-26) als de kleine kernen uit (Beerzerveld 34 op agrarische grond; Lemele: uitbreiding aan de zuidkant, 20-25 woningen/ha; Vinkenbuurt 8). Het college acht uitbreiding in Lemele nodig, "inbreiding vóór uitbreiding" is wel uitgangspunt ("De provincie Overijssel is terughoudend als het gaat om uitbreidingslocaties van dorpen als Lemele en ziet nieuwbouw liever binnen de bestaande kerngrenzen. Uitgangspunt is dan ook dat inbreiding vóór uitbreiding gaat. Maar daarmee kan niet in de volledige woningbehoefte worden voorzien", Vechtdal Centraal 3/2026, citaat uit de visie). Buiten kernen/buurtschappen: alleen via Rood-voor-Rood, splitsing, landgoed-/rood-voor-groen-regelingen (VOV-programma en coalitie).
- **Ladder/volkshuisvestingsprogramma:** geen (ontwerp-)volkshuisvestingsprogramma of ladderdiscussie gevonden in het nieuws. Het akkoord kondigt "een vernieuwde woonvisie met meer ambitie" aan, geen volkshuisvestingsprogramma. Waar te vinden: raadsagenda's via ommen.bestuurlijkeinformatie.nl (DO1).

## §3 Openheid voor agrarische herbestemming
Zie Beerzerveld (34 woningen op agrarische grond na omgevingsplanwijziging; mogelijk doordat de gemeente eigenaar was en het een als uitbreidingslocatie aangewezen locatie aan de kern is) en Vlierlanden III (gemeente koopt varkenshouderij). Voor *private* omzetting agrarische grond naar wonen op 10-12 woningen: geen voorbeeld gevonden in het nieuws. De dichtstbijzijnde indicatie is het provinciale oordeel over Vinkenbuurt (11 woningen te veel, 8 acceptabel). Dit is een [INT]-conclusie op basis van één geval.

## §4 VAB-beleid
- **Rood-voor-Rood Beleidsregels gemeente Ommen 2026** (CVDR757546, "Geldend van 26-02-2026 t/m heden", bij Ommen: tekst noemt uitsluitend gemeente Ommen en "buitengebied van de gemeente Ommen"; https://lokaleregelgeving.overheid.nl/CVDR757546/1, gelezen 2026-10-06):
> Om in aanmerking te komen voor het bouwen van een compensatiewoning, dient op de slooplocatie minimaal 850 m2 aan voormalige agrarische bedrijfsbebouwing te worden gesloopt. [...] Om in aanmerking te komen voor het bouwen van twee compensatiewoningen, dient op de slooplocatie minimaal 2.000 m2 aan voormalige agrarische bedrijfsbebouwing te worden gesloopt.

> Een compensatiewoning heeft een inhoud van maximaal 750 m3. In de plaats van een compensatiewoning mag ook worden gekozen voor alternatieve woonvormen waarbij binnen de maximale 750m3 er 2 of meer zelfstandige wooneenheden worden teruggebouwd.

  Er is een **sloopmeterregister** (bijlage 2; minimaal 150 m² per registratie) en verplaatsing naar de rand van een kern of buurtschap verlaagt de benodigde sloopmeters (100 m² per woning; 250 m² bij twee). **[INT/BER]** Het regime is gedimensioneerd op 1-2 woningen per slooplocatie; 10-12 woningen zouden bij de eigen sloopmeters ca. 5-6 locaties nodig hebben of het sloopmeterregister, en vallen niet onder de standaardregeling (afwijking via art. 10 mogelijk).
- **Evaluatierapport (ontwerp, sept. 2025)** (https://openpub.ommen.nl/wp-content/uploads/2025/09/1.-Ontwerp-rapport-Evaluatie-en-Actualisatie-VAB-beleid-gemeente-Ommen.pdf, 31 p., gelezen): 34 principeverzoeken 2021 t/m aug. 2025, 11 vervolgtrajecten, 7 onherroepelijk; 32 compensatiewoningen in 2021-2024, vrijwel allemaal één standaard 750 m³-woning; ca. 350 agrarische bedrijven (300 veehouderij), indicatie 75-100 stoppers de komende 10 jaar; Rood-voor-Rood kan in Overijssel niet worden gecombineerd met LBV+ (wel met andere beëindigingsregelingen); na 2025 tellen compensatiewoningen mee in de woondeal-aantallen en de 30-40-30-eis.
- **Woningsplitsing buitengebied:** Beleidsnotitie oktober 2025 (CVDR745908); splitswoningen ≥ 200 m³.
- Erfcoach: zie D2.

## §5 Grondbeleid
- **Uitgifte kavels:** puntensysteem op betaald account woneninommen.nl (iedere week één punt; punten bepalen toewijzing; MeeDenkDag-bezoek = 50 extra punten). Kavels CPO: één geheel gereserveerd voor de vereniging, prijs volgens "grondprijsbrief" (de brief zelf niet gevonden in dit deelonderzoek).
- **Grondposities / aankoop:** gemeente koopt varkenshouderij Arriërveldsweg (feb. 2025, bouwclaim Bemog, 375 woningen), is eigenaar van de Beerzerveld-kavel (ca. 1,2 ha, "agrarisch perceel" [WF-zoeksamenvatting]), Haven Oost (voorm. havengebied), Guido de Brès, Julianaschool.
- **Grondbeleid actualisatie:** raadsbesluit 27-11-2025; herziene nota uiterlijk november 2027 (De Toren [WF]). Het coalitieakkoord noemt "erpacht" en "anti-speculatiebeding" als te onderzoeken instrumenten.
- **Plancapaciteit/volgordelijst:** zie C4; de Volgordelijst (29 projecten; samen ca. 1.400 woningen [BER, som van kolom "Aantal huizen"]) is een momentopname van de harde en zachte planvoorraad met 'startjaar'. Positie 27 "Ontwikkeling Nieuwbouw Broekdijkje Ommen" (479 woningen, start 2029) en 23 "Vlierlanden fase 3" (375) zijn de grootste.

## §8 Huisvestingsverordening
- In de CVDR-lijst van de gemeente (540 records, doorlopen op 2026-10-06) staat **geen huisvestingsverordening**; het coalitieakkoord zegt "stellen wij een huisvestingsverordening op". Aannemelijk dat er nog geen is [INT]; definitief vast te stellen via CVDR/Gemeenteblad (DO4). Wel een *Verordening starterslening gemeente Ommen 2022* (CVDR679031) en een *Beleidsregel aanpak woonoverlast* (CVDR757684, 27-2-2026). Prestatieafspraken 2025 en 2026 met Vechtdal Wonen: o.a. 25 woningen gelabeld voor jongeren < 28 jaar (2025), pilot "Woningdelen" (2026).

## §9 Zelfbouwloket / contactpersoon
- Het functionele loket is het woonplatform **www.woneninommen.nl** (kavels, CPO, starterslening, verkoopprocedure), met contactformulier, **gemeente@ommen.nl**, tel. **14 0529**, Chevalleraustraat 2, 7731 EE Ommen (https://woneninommen.nl/contact). Per CPO-locatie stelt de gemeente een **projectleider** beschikbaar (Uitvoeringsregels 2.4c); inschrijvingen op CPO-locaties worden gestuurd naar gemeente@ommen.nl onder vermelding van de locatie. Voor netaanvragen: **eerderaanvragen@ommen.nl**. Wethouder: Alice van den Nieuwboer. Namen van projectleiders niet gevonden (wel Rob Bruns genoemd in een grondtransactie-bericht, ommen.nl 7-5-2025, niet specifiek voor CPO).

## §11 Kostenverhaal en leges
Niet in het nieuws gevonden. Wel: de Uitvoeringsregels CPO (voorschot, subsidie, anterieure overeenkomst voor CPO-fonds); Legesverordening 2026 (CVDR753504) bestaat (DO4).

## §12 Woningbehoefte en doelgroepen
- 1.250 extra woningen tot 2040 voor de kern Ommen (Omgevingsvisie "Ommen Jouw Toekomst"; 485 huurwoningen Vechtdal Wonen 2022-2030 = 39%; ommen.nl 12-12-2024). Lemele: ± 80 woningen tot 2031, vooral senioren en starters. Vinkenbuurt: enquête met "veel behoefte in Vinkenbuurt aan betaalbare woningen". Het akkoord wil minimaal 30% sociale huur in nieuwbouw en nieuwbouwfocus op starters en senioren in de kernen. Betaalbaarheidsgrenzen volgens college (16-4-2025): max. koopprijs € 405.000, max. huur € 1.184,82/maand. CPO-doelgroep: starters en senioren met binding (VON < NHG-grens bij Vinkenbuurt en Arriërflier).

---

# Bijlage A-controlepunten (primair voor DO3)

## D1. Intergemeentelijk VAB-/Erftransformatieprogramma en subsidie 4.39
**Status: niet gevonden (geen aanvraag of toekenning aangetroffen).**
- Het ontwerp-evaluatierapport (sept. 2025) schrijft: "De routekaart richt zich op het ondersteunen van gemeenten [...] Daarmee lijkt het vooralsnog logischer de routekaart te koppelen aan de uitwerking van de nog op te stellen ontwikkelperspectieven voor ons landelijk gebied, zoals voorzien in de Omgevingsvisie Ommen Jouw Toekomst. We zijn gestart met het opstellen van een plan van aanpak, zodat we in de 2e helft 2025 hiermee kunnen starten." Ook: "In het Vechtdal worden vanuit deze middelen [Maatregelenpakket NPLG] zes gebiedsprocessen ondersteund [...]. Deze gebiedsprocessen liggen in het Vechtdal allemaal geheel of gedeeltelijk in de gemeente Ommen. De verwachting is dat in deze gebiedsprocessen ook het VAB-beleid onderdeel is van de oplossing." Er is een werksessie met buurgemeenten gehouden. Partnergemeenten zijn niet benoemd.
- Het provinciale loket (https://regelen.overijssel.nl/Producten_en_diensten/Subsidies/Wonen_en_leefbaarheid/Beleid_transformatie_agrarische_bebouwing_erven_en_gronden, gelezen 2026-10-06) bevestigt de regeling: A = gemeentelijke bouwsteen, B = Intergemeentelijk VAB-programma, C = Intergemeentelijk Erftransformatie-programma; minimaal 2 en maximaal 5 gemeenten; adviesgesprek via vab@overijssel.nl; "Een gemeente kan maximaal 2 keer subsidie ontvangen". Het is niet te zien of Ommen is toegetreden.
- **Waar te vinden:** provincie Overijssel (vab@overijssel.nl; beschikkingen/subsidieregister; Statenbrief over VAB-routekaart), raadsinformatiebrief of collegebesluit Ommen (ommen.bestuurlijkeinformatie.nl), "Ontwikkelperspectieven landelijk gebied" (coalitie: portefeuille Rasenberg).
- Of er een "spelregelkader" (partiële functiewijziging van erven) is: niet gevonden.

## D2. Erfcoach en provinciale ondersteuning
**Status: gevonden.**
- ommen.nl, 3-2-2025, https://www.ommen.nl/actueel/de-erfcoach-staat-voor-u-klaar:
> In het buitengebied van Ommen staan erfcoaches Hendry van Ittersum en Yvonne In 't Veld klaar om met erfeigenaren mee te denken over de toekomst van de boerderij of het erf. [...] Gesprekken kunnen bijvoorbeeld gaan over: Agrarisch ondernemen [...]; Nieuwe functies in vrijkomende agrarische bebouwing; Woonvragen, zoals Rood voor Rood en mantelzorg; [...] Neem contact op met erfcoach Hendry van Ittersum of Yvonne In 't Veld voor een kosteloos keukentafelgesprek.
- Evaluatierapport: "Vanaf 2026 wordt deze ondersteuning ingericht vanuit Boerenperspectief Overijssel en bestaat deze ondersteuning uit sociaal economische begeleiders voor agrarische erven en erfcoaches voor de niet agrarische erven." De provincie bevestigt dat persoonlijke erf-ondersteuning in 2026 beschikbaar blijft ("Erfcoaches blijven beschikbaar voor het Overijsselse buitengebied", overijssel.nl, titel gezien, inhoud niet gelezen [NIET-GELEZEN]). Ommen heeft de Erfcoach in het coalitieakkoord 2022-2026 als doel ("Continueren erfcoaches") en in 2026-2030 de nieuwe **plattelandscoach** (gemeentelijk, 3 jaar, wethouder Rasenberg).
- Gebruik van **Atelier Overijssel** of de **Rijkshandreiking planologische concepten erftransformaties**: niet gevonden voor Ommen. [NIET-GELEZEN] Een zoekresultaat noemt een vacature "Sociaal-economische verbinder Vechtdal" (sept. 2026, 8 uur/week); niet zelf gelezen en niet als feit overgenomen.

## D3. Gemeentelijk VAB-beleid en precedenten (nieuwsdeel)
**Status: gedeeltelijk gevonden.**
- Beleid: zie §4 (Rood-voor-Rood 2026, woningsplitsing 2025, tijdelijk omgevingsplan VAB-regeling: "De gemeente faciliteert vanuit het tijdelijk omgevingsplan het hergebruik van leegkomende agrarische gebouwen").
- Maximumaantal woningen: 1 compensatiewoning per ≥ 850 m² sloop, 2 per ≥ 2.000 m²; alternatieve woonvormen (2+ eenheden) binnen max. 750 m³ in totaal; Ommen noemt zelf dat verplaatsing van de herontwikkeling naar een kernrand "wel benoemd [is] als mogelijkheid maar niet verder geïnstrumenteerd" en onderzoekt schuifrechten/sloopbewijzen.
- Precedenten (nieuws): uit het evaluatierapport 7 onherroepelijke principeverzoeken en één compensatieverzoek voor zorg/recreatie; de Volgordelijst bevat "Rood voor Rood, Wethouder Petteweg 6" (1 woning) en "Landgoed Junne" (9, aard onbekend). Collectieve/cohousing-precedenten op een erf: geen gevonden in Ommen. (Vergelijkingspunt in het provinciebestand: BuitenDelen in Lettele, gemeente Deventer.)
- Woonprogrammering: de Twente-woondeal noemt VAB-transformatie expliciet, de West-Overijssel-woondeal niet [PB]; in Ommen noemt het evaluatierapport dat compensatiewoningen "na 2025" meetellen in de aantallen/30-40-30. Een aparte VAB-opgave in de woonprogrammering is niet gevonden.

## C4. Redeneerlijn en energiesysteem, netcongestie (nieuwsdeel)
**Status: netcongestie gevonden, redeneerlijn-standaardonderbouwing niet gevonden.**
- **Enexis netcapaciteit-update 16-7-2026** (https://www.enexis.nl/nieuws/2026/07/update-netcapaciteit-juli, gelezen 2026-10-06), tabel onder kopje Overijssel bij "32 nieuwe knelpunten": Hardenberg MST netdeel 4 (afname), **Ommen Dante MST netdeel 1 (afname), Ommen Dante MST netdeel 5 (afname)**, Vroomshoop, Zwolle Hessenweg; "Deze gebieden gaan van congestiefase 0 naar 1a (oranje op de capaciteitskaart). Voor klanten aangesloten op de wachtlijst verandert niets." Andere maanden (okt. 2025 t/m sept. 2026) bevatten geen vermelding van "Ommen" in de pagina's. De claim in een zoekresultaat dat al in okt. 2025 stations "in Kampen en Ommen" vol waren, kon ik **niet** bevestigen [niet-bevestigd].
- Nieuwe regels vanaf 1-7-2026: "Nu komen ook huishoudens en bedrijven met een kleinverbruikaansluiting op een wachtlijst wanneer zij een nieuwe of zwaardere stroomaansluiting aanvragen." Overgangsregeling woningbouw: projecten ingediend 1-30 juni 2026 kunnen transportcapaciteit krijgen (Enexis augustus-update 17-8-2026).
- **Gemeente Ommen:** pagina "Aanvragen van netcapaciteit" (https://www.ommen.nl/direct-regelen/wonen-en-leefomgeving/duurzaamheid/eerder-aanvragen-van-netcapaciteit/): "Projecten die uiterlijk 10 september 2026 bij de gemeente Ommen waren aangemeld, zijn op een volgordelijst geplaatst. Hierop staan de projecten die de gemeente vanaf 1 oktober 2026 aanbiedt bij Enexis." Voorbehoud: "Het kan daarom nog steeds meerdere jaren duren voordat een aansluiting beschikbaar komt." **Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten Ommen 2026** (CVDR765864, geldend vanaf 28-8-2026; besluit van het college van Ommen; https://lokaleregelgeving.overheid.nl/CVDR765864/1). Rangorde: (1) maand van start bouw, (2) projectrijpheid 1-7 (hoogst: "civielrechtelijke overeenkomst en een onherroepelijke Omgevingsvergunning"; "omgevingsplan vastgesteld of vergunning voor een BOPA verleend" = categorie 5), (3) maatschappelijk belang (o.a. > 20% sociale huur/koop/middenhuur; bijzondere doelgroepen), (4) opleverdatum; daarna groter aantal woningen en loting.
- **Volgordelijst Ommen 2026, definitief 17-9-2026** (PDF 1 p.; https://openpdc.ommen.nl/wp-content/uploads/2026/08/Definitieve-Volgordelijst-woningbouwprojecten-Ommen-2026-dd-17-september-2026.pdf): 29 projecten, kolommen Positie / Plannaam / Dorp / Start bouw / Status categorie / Maatschappelijk belang / Aantal huizen. CPO-gerelateerd: positie 12 "Kruispunt Bulmensteeg-Lemelerweg (CPO)", Lemele, 8 huizen, categorie 6; positie 18 "Vlierlanden Erve Arrierflier (CPO), 2x XL kavels, 8 CPO, 24 sociale verhuur, rest koop", 50 huizen, categorie 5. **Niet op de lijst:** Beerzerveld Van Alewijkstraat en Vinkenbuurt (mogelijk reeds een aansluiting of nog niet aangemeld; niet te achterhalen [niet gevonden]). Aanmelddeadline voor nieuwe projecten was 10-9-2026; **een volgende ronde is niet aangekondigd** in de gelezen bronnen. Een nieuw CPO-project buiten de lijst zal dus een aansluiting moeten aanvragen bij Enexis via de normale (wachtlijst)route.
- **Concreet voor Beerzerveld (CPO, 8 woningen):** "Tot deze werkzaamheden zijn afgerond, is voor het hele project één bouwstroomaansluiting mogelijk. De CPO-groep en de projectontwikkelaar hebben deze aansluiting al aangevraagd." Hoofdleidingen: start week 7 van 2027, acht weken; "Dit hangt onder meer samen met werkzaamheden van Enexis om het elektriciteitsnet rond Beerzerveld te versterken." Bouwrijp: december 2026; bouwen met bouwstroom pas vanaf ± half april 2027 (ommen.nl 1-9-2026). Eerder werd bouwrijp 1e/2e kwartaal 2026 verwacht (ommen.nl 20-10-2025), dus ca. 6-9 maanden vertraging [BER].
- Station **Ommen-Dante**: uitbreiding Enexis (nieuwsbrief okt. 2023, "Het station moet worden gerenoveerd en uitgebreid"); brondocument kon niet worden geopend (404 op de PDF-URL via curl; de inhoud is alleen uit een zoeksamenvatting) [NIET-GELEZEN].
- Redeneerlijn (OF-WAAR-HOE, art. 4.122) en energieparagraaf (art. 4.125): geen standaardonderbouwing van de gemeente in nieuws gevonden. Wel het akkoord: "off-gridmogelijkheden bij de realisatie van nieuwe woonprojecten" en de lijn dat bij nieuwe locaties "ontsluiting en verkeersafwikkeling vooraf aantoonbaar op orde" moeten zijn. Waar te vinden: Omgevingsplan/Omgevingsvisie "Ommen Jouw Toekomst", raadsvoorstellen (DO1/DO2).
- **Drinkwater:** Hammerflier (Vitens, uitbreiding winning van ca. 1,6 tot 5 miljoen m³ per jaar volgens Vitens-documenten via zoeksamenvatting [NIET-GELEZEN]); standpunt gemeente zie 10.4. Beperking voor woningbouw: niet gevonden.

## E4. Provinciale zienswijzen of conflicten 2023-2026
**Status: formele conflicten niet gevonden; wel informele provinciale remmende signalen gevonden.**
1. **Vinkenbuurt, woningaantal (2024/2025).** Memo "Herzien stedenbouwkundig ontwerp Vinkenbuurt" (gemeente Ommen, 5 p.; https://a.storyblok.com/f/284824/x/0a74bfc87f/memo-herzien-stedenbouwkundig-ontwerp-vinkenbuurt.pdf; gelezen 2026-10-06; ongedateerd, plan "gepresenteerd in november 2024"):
> Naast de opmerkingen vanuit de omgeving, is er ook een reactie gekomen vanuit de provincie op het plan. Deze reactie richtte zich met name op een hoge woningdichtheid in relatie tot het agrarische gebied en de kenmerken van een buurtschap. Het woningaantal is volgens de provincie daarom aan de forse kant.

> Op deze locatie ging het voormalige plan uit van 11 woningen. Gezien de reacties vanuit de omgeving en vanuit de provincie, hebben we het woningaantal gereduceerd naar 8 woningen: 7 betaalbare woningen ondergebracht in een kapschuur volume en 1 vrijstaande woning.

   Eerdere scenario's: A = 11 woningen, B = 13 woningen bij verplaatsing buurthuis. Dit is een **informele provinciale reactie** (geen zienswijze) op een plan van ongeveer onze schaal (10-13 woningen) in een buurtschap in agrarisch gebied; het concept (7 rijwoningen in "kapschuurvolume") is de gemeentelijke compromisvorm.
2. **Vinkenbuurt, Centrumplan (2021).** "Het centrumplan is vanwege het ruimtelijk ontwerp afgewezen door de provincie." (woneninommen.nl, projectpagina Vinkenbuurt, gelezen 2026-10-06; jaar 2021 volgens dezelfde tekst, "Plaatselijk Belang Vinkenbuurt heeft voor de vernieuwing van de kern in 2021 een centrumplan opgesteld"; datum afwijzing zelf niet vermeld). Dit ligt vóór de gevraagde periode 2023-2026.
3. **Lemele (maart 2026).** Provincie "terughoudend" bij uitbreidingslocaties van dorpen als Lemele (zie §2); de visie wijkt hier bewust van af met onderbouwing. Het is niet bekend of de provincie een formele reactie heeft ingediend [niet gevonden].
4. **Natura 2000 Arriën (2023):** provinciaal natuurherstelproject "Vecht en Beneden-Regge", deelgebied Arriën (stroomdalgraslanden), inloopbijeenkomsten 13-7-2023 (ommen.nl 6-7-2023 en 25-7-2023). Geen conflict; wel relevant als overlay nabij Vlierlanden III (Arriën grenst eraan) [INT; C3 voor DO2].
5. **Positief:** versnelling Kardoen/Fluitekruid en "extra inzet van de provincie" bij Guido de Brès en Julianaschool (RTV Vechtdal 16-4-2025, college-brief aan raad: "Dankzij extra inzet van de provincie zijn we gestart met herontwikkeling van de Guido de Brés-locatie en de Julianaschool.").
6. **Stikstof, provinciale reactie:** Oost 3-9-2026 (https://www.oost.nl/nieuws/3691119/...): "Overijssel staat in grote lijnen achter de nieuwe stikstofaanpak van het Rijk, maar heeft nog veel vragen over de uitwerking."; "Rond negentien gebieden in Overijssel stelt het Rijk een zone van 500 meter voor. Bij twee gebieden gaat het om 1000 meter." Lijst van gebieden niet gelezen; of Vecht en Beneden-Regge erbij zit is **niet vastgesteld**. De provincie "weet nog niet" of de plannen voldoende zijn om vergunningverlening voor woningbouw weer mogelijk te maken.
- **Waar formele zienswijzen/BOPA-instemmingen te vinden:** Provinciaal blad (repository.overheid.nl, `dt.creator=Overijssel` + "Ommen"), Omgevingsloket/Planviewer, besluitenlijsten GS; raadsvoorstellen met "Reactienota" (DO1/DO4).

## F1. Provinciale regelingen waar de gemeente gebruik van maakt (nieuwsdeel)
**Status: nauwelijks gevonden.**
- Genoemd in nieuws: provinciale "extra inzet" voor Guido de Brès/Julianaschool (aard van de regeling niet vermeld); provinciale VAB-routekaart (zie D1); provinciale erfcoaches/Boerenperspectief (D2); de woondeal met de provincie (zie Bijlage-A-bijvangst); de provincie droeg het Natura 2000-natuurherstel in Arriën. Rijksregeling: Stimuleringsregeling Flex- en Transformatiewoningen (Ommen één van 13 gemeenten, ommen.nl 22-11-2022). Provinciale regelingen *Betaalbaar wonen in kleine steden en dorpen*, *Flexpools*, *Fysieke investeringen leefbaar platteland*, *Vitaliteit dorpen/steden*, *Langer zelfstandig wonen*: **niet gevonden voor Ommen** in het nieuws.
- Toepasbaarheid op particulier collectief: geen informatie in deze bronnen; de gemeentelijke CPO-subsidie (70% begeleider) en het voorschot zijn gemeentelijk.
- Waar te vinden: provincie Overijssel subsidieloket (regelen.overijssel.nl), Statenbrieven; gemeentebegroting en raadsinformatiebrieven.

---

# Bijvangst voor andere Bijlage A-punten
- **A1/A2 (woonregio, woonafspraken):** Ommen in woonregio West-Overijssel; Vlierlanden fase 3 en "binnenstedelijke woongebieden" zijn de sleutelprojecten (508 woningen, RTV Vechtdal 16-4-2025). "Vlierlanden fase 3 is aangemerkt als sleutelproject binnen de Woondeal West-Overijssel" (ommen.nl 27-6-2025). Lemele-visie: 30-40-30 evenwichtig verdelen over de locaties. Het coalitieakkoord zet daar "minimaal 30% sociale huur" bovenop.
- **A3 (30-40-30):** door de gemeente toegepast bij Vlierlanden 3, Beerzerveld (10 sociale huur van 20) en Arriërflier (24 sociale verhuur van 50); of de verdeling ook voor een CPO van 8 geldt: de CPO-woningen zijn "VON < NHG-grens" (betaalbare koop).
- **A5 (zorg, ouderen):** woonzorgvisie wordt voorbereid ("Vooruitlopend op de woonzorgvisie", ommen.nl 19-12-2025); coalitie "WOZO (Wonen, Ondersteuning en Zorg)" en "woonzorgcomplexen en generatiewonen".
- **B1/B2 (KGO/rood-voor-rood):** zie §4.
- **C1/C3 (overlays):** Natura 2000 Arriën, Hammerflier-drinkwater, Nationaal Landschap/Vechtdal en voorbereidingsbesluiten raatakkers/karrensporen/zonneparken/windenergie/datacentra in CVDR (gemeentelijke Voorbereidingsbesluiten van 2024-2026, bijgewerkt 21-7-2026) wijzen op provinciale overlays in het gemeentelijke buitengebied (DO2/DO4 uitwerken).
- **E1/E2:** geen informatie over Omgevingstafel of provinciale accounthouder in het nieuws. Vinkenbuurt: stedenbouwkundig plan "in samenwerking met de provincie opgesteld" (ommen.nl 9-3-2026), wat wijst op voorkantsamenwerking met de provincie.
- **E2/E3:** Beerzerveld is via een **wijziging van het omgevingsplan** gerealiseerd (geen BOPA); Vinkenbuurt en Arriërflier eveneens omgevingsplanwijziging door de gemeente (CPO-kavels gemeentelijk).

---

# Tegenstrijdigheden en onzekerheden
1. **Aantal CPO-woningen Erve Arriërflier:** 8 (inschrijfprocedure; Volgordelijst 17-9-2026) versus "tien CPO-starterswoningen" (De Toren 25-11-2025, kop en [WF]-samenvatting "ten plots"). Ik volg 8 (gemeentelijk document) en markeer 10 als journalistieke afwijking [tegenstrijdig].
2. **Zetelverdeling vs. namenlijst:** de VOV-site meldt dat Carles Bembom zijn zetel niet aanvaardde, de lijst van ommen.nl (26-3-2026) noemt hem nog. Aantallen kloppen (VOV 5).
3. **"Acting mayor":** een zoekresultaat (stadindex) noemt Alice van den Nieuwboer "locoburgemeester" bij de brandbrief van 10-8-2026; de ommen.nl-bronnen noemen Annemiek Jetten waarnemend burgemeester. Alice is 2e loco-burgemeester; Jetten was waarschijnlijk afwezig (zomer) [INT]. Geen echte tegenspraak.
4. **Aantal trekkers 10-8-2026:** "ongeveer 200 inwoners en ondernemers" (ommen.nl 9-9-2026), "bijna anderhalf honderd tractoren" (Stadindex), "ca. 250" in Ommen én Dalfsen samen (Vechtdal Centraal).
5. **Enexis en Ommen-Dante:** de eerste vermelding in de maandupdates is juli 2026 (fase 0 → 1a); een zoeksamenvatting suggereerde oktober 2025 "Kampen en Ommen". Niet bevestigd; ik volg de gelezen Enexis-pagina's.
6. **Beerzerveld "34 woningen"** (ommen.nl) versus één zoeksamenvatting die 4+6+12+12 = 34 aanduidt: consistent. De verdeling "20 + 8 CPO + 6 kavels" (ommen.nl 12-2-2026) telt 34.
7. **Provincie "terughoudend" (Lemele):** de bron is gemeentelijk en secundair (Vechtdal Centraal/RTV Vechtdal citeren de visie); de provinciale reactie zelf is niet gelezen.
8. **Vinkenbuurt-memo is ongedateerd;** de aanduiding "2024/2025" is afgeleid van "gepresenteerd in november 2024" en de raadsbesluit van 30-1-2025.
9. **Provinciebestand (§1.5, 508 woningen, 290 gerealiseerd 2022-2024):** bevestigd door RTV Vechtdal 16-4-2025.
10. [WF]-bronnen (De Toren) zijn samenvattingen door een klein model; kerncitaten zijn zoveel mogelijk gecontroleerd tegen een tweede bron (Vechtdal Centraal/RTV Vechtdal/ommen.nl), niet allemaal.

# Niet gevonden (met vindplaats)
- **Verkennersadvies Frank de Grave (7-4-2026)** en de verslaglegging van de openbare bespreking: ommen.nl/actueel heeft er geen bericht over; zoeken in ommen.bestuurlijkeinformatie.nl (raadsvergadering/duidingsdebat 26-3 en 7-4-2026) of de griffie.
- **Nieuwe burgemeester (voordracht):** Commissaris van de Koning/ministerie BZK, raadsagenda 2026.
- **Uitvoeringsprogramma coalitie 2026-2030** (wonen, buitengebied): in voorbereiding bij het college.
- **Grondprijsbrief Ommen, Addendum Woonvisie (nov. 2023), Omgevingsvisie "Ommen Jouw Toekomst", Ontwikkelperspectieven landelijk gebied, Woonvisie-opvolger/volkshuisvestingsprogramma:** bestuursinformatie (DO1).
- **Aanvraag/beschikking subsidie 4.39 (D1):** provincie vab@overijssel.nl; gemeentelijk collegebesluit.
- **Provinciale formele zienswijzen/BOPA-instemming (E4):** Provinciaal blad, Omgevingsloket.
- **Uitkomst volgende ronde Volgordelijst netcongestie:** gemeente (eerderaanvragen@ommen.nl).
- **Bouwstart De Meerkoet; status omgevingsplan Erve Arriërflier en Vinkenbuurt:** ommen.nl/actueel, woneninommen.nl, bekendmakingen (officielebekendmakingen.nl).

# Niet onderzocht, en waarom
- **De Stentor** (privacygate/betaalmuur, geen toegang).
- **RTV Oost-videobeeld/radio**, **Dedemsvaartse Courant** als zelfstandige titel (alleen Vechtdal Centraal gelezen, dat tot dezelfde uitgeversgroep (Regiobode BV) behoort [INT]), **De Ommenaar** (alleen zoekresultaat).
- **Sociale media** (Facebook/Instagram van gemeente en CPO-verenigingen): niet bereikbaar zonder inlog/niet doorzocht.
- **Partijprogramma's** van CDA, PRO Ommen, LPO, ChristenUnie, D66 (niet gevonden of niet gelezen); VOV en VVD wel.
- **Raadsvergaderingen en RIS** (iBabs): DO1.
- **Stikstofpakket-details per Natura 2000-gebied** en de exacte gevolgen voor Ommen: de bronnen noemen geen gebiedenlijst; zie Kamerbrief 26-6-2026 en AERIUS/provinciale gebiedsanalyse (DO2).
- **Natuurvergunning/stikstofruimte bij Vlierlanden III of Erve Arriërflier:** niet aangetroffen (alleen algemene risico-opmerking in De Toren 25-11-2025).
- **Dedicated redeneerlijn-/energieparagraaf van het Omgevingsplan:** DO1/DO2.

# Bronnenlijst (selectie, alle geraadpleegd 2026-10-06)
- ommen.nl/actueel (84 artikelen, o.a.): coalitieakkoord 26-6-2026; uitslag 26-3-2026; verkenner 26-3-2026; wethouders afscheid 2-7-2026; Leo Bongers stopt 13-1-2026; Jetten 26-3-2026; van der Zwan 19-12-2024; CPO-berichten 17-11-2023, 20-12-2024, 10-6-2025, 28-8-2025, 9-3-2026; Beerzerveld 26-5-2025, 22-7-2025, 20-10-2025, 7-11-2025, 12-2-2026, 19-3-2026, 1-9-2026; Vlierlanden 27-2-2025, 9-4-2025, 27-6-2025, 15-1-2026, 12-3-2026; Haven Oost 21-8-2025, 24-10-2025; Guido de Brès 12-6-2025 en 2-10-2025; Julianaschool 13-6-2025; Erfcoach 3-2-2025; woningsplitsing 2-4-2025; Rood voor Rood 1-10-2025; stikstofbrief 9-9-2026; flexwoningen 25-3-2026 en 5-10-2026; Lemele 10-12-2025; NGK 19-12-2025; prestatieafspraken 12-12-2024 en 2026.
- https://woneninommen.nl (CPO-beleid, Vinkenbuurt, Meerkoet, Erve Arriërflier, Haven Oost, Gebied Arriën-Ommen, Hof van Vlierlanden).
- https://openpub.ommen.nl/wp-content/uploads/2026/06/Coalitieakkoord-Ommen-2026-2030.pdf ; https://www.ommen.nl/wp-content/uploads/2022/09/Coalitieakkoord_op_hoofdlijnen_2022-2026.pdf
- https://a.storyblok.com/f/284824/x/cfd69c0eea/uitvoeringsregels-cpo-gemeente-ommen_mei-2024.pdf ; inschrijfprocedures CPO Vinkenbuurt en Erve Arriërflier; memo herzien stedenbouwkundig ontwerp Vinkenbuurt.
- https://lokaleregelgeving.overheid.nl/CVDR757546/1 (Rood voor Rood 2026), CVDR765864 (beleidsregels transportcapaciteit), CVDR745908 (woningsplitsing), CVDR764217 (vertrouwenscommissie).
- https://openpdc.ommen.nl/wp-content/uploads/2026/08/Definitieve-Volgordelijst-woningbouwprojecten-Ommen-2026-dd-17-september-2026.pdf
- https://openpub.ommen.nl/wp-content/uploads/2025/09/1.-Ontwerp-rapport-Evaluatie-en-Actualisatie-VAB-beleid-gemeente-Ommen.pdf
- https://www.enexis.nl/nieuws/2026/07/update-netcapaciteit-juli (en 2025/10, 2025/12-2026/09)
- Vechtdal Centraal (5/2025 Vlierlanden; 3/2026 Lemele; 5/2026 Politiek Verwoord; 5/2026 Arriën; 6/2026 coalitie; 9/2026 stikstof), RTV Vechtdal (16-4-2025; 27-3-2026), Ommen City (18-4-2025; 2-6-2026), De Toren (3-7-2026 en [WF]-artikelen), Oost (3-9-2026 en provinciale reactie), Stadindex (10/11-8-2026), RondOmmen (9-9-2026).
- https://regelen.overijssel.nl/.../Beleid_transformatie_agrarische_bebouwing_erven_en_gronden ; Dirk Zwager over stikstofpakket 26-6-2026 (https://www.dirkzwager.nl/kennis/artikelen/maatregelen-pakket-stikstof-wat-betekent-dit-voor-uw-project); VeeTeelt over zones.
- VOV-programma en -site; VVD-programma.

**Model dat dit deelonderzoek heeft uitgevoerd:** Claude Sonnet 5.5 (`claude-sonnet-5-5`).
