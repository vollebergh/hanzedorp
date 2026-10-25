import sys; sys.path.insert(0,'.')
from lib import Doc
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/8c2cda72-f653-4a4b-aefb-12cf46016d6b/scratchpad/wt-dalfsen/gemeente_dalfsen.md'
d=Doc(W)

d.line_replace('- **Prestatieafspraken** Wonen Dalfsen 2025',
'- **Prestatieafspraken** Wonen Dalfsen 2025 (gelezen 2026-10-05; https://www.vechtdalwonen.nl/media/1720/prestatieafspraken-wonen-dalfsen-2025.pdf): de corporaties willen tot 2030 297 sociale huurwoningen toevoegen; de nieuwbouwopgave komt uit de Woondeal West-Overijssel; de corporaties constateren dat de realisatie van nieuwbouw onder druk staat. CPO, VAB en het buitengebied komen er niet in voor (tekstzoektocht).')
d.line_replace('- **Corporaties:** willen tot 2030 297',
'- **Corporaties:** willen tot 2030 297 sociale huurwoningen toevoegen (prestatieafspraken 2025, gelezen).')

d.line_replace('- **Algemeen:** 0529 48 83 88;',
'- **Algemeen:** 0529 48 83 88; Raadhuisstraat 1, 7721 AX Dalfsen (dalfsen.nl). Het nummer 14 0529 staat in Gemeenteblad-publicaties van de gemeente (2024-2025) en is daarmee bevestigd.\n- **Vooroverleg:** product "Vooroverleg initiatiefnemer" (conceptverzoek via het Omgevingsloket; € 371,10; sinds 1-1-2026 verrekend met de leges van een omgevingsvergunning of omgevingsplanwijziging die binnen 12 maanden volgt): https://www.dalfsen.nl/vooroverleg-initiatiefnemer.')

d.line_replace('- Overige zetels [Z]',
'- Zetels en opkomst gelezen in Vechtdal Centraal (definitieve uitslag, maart 2026; https://www.vechtdalcentraal.nl/2026/03/definitieve-uitslag-gemeenteraadsverkiezingen-gemeente-dalfsen/): opkomst 66,34% (2022: 62,7%). Analyse DalfsenNet (https://www.dalfsennet.nl/nieuws/538748/analyse-hoe-heeft-dalfsen-gestemd-en-hoe-gemeentebelangen-weer-wint.html): Gemeentebelangen 37,7% van de stemmen; Stand Organisatie Dalfsen (Rob Mud) nieuw met 1 zetel; ChristenUnie verloor een zetel; de raad groeide met twee zetels. De uitslagpagina op dalfsen.nl gaf op 2026-10-04 een 404.')
d.line_replace('| ChristenUnie | 2 [Z] |','| ChristenUnie | 2 (was 3) |')
d.line_replace('| GroenLinks-PvdA / PRO Dalfsen | 2 [Z] |','| GroenLinks-PvdA | 2 |')
d.line_replace('| D66 | 1 [Z] |','| D66 | 1 |')
d.line_replace('| VVD | 1 [Z] |','| VVD | 1 |')
d.line_replace('| Stand Organisatie Dalfsen | 1 [Z] |','| Stand Organisatie Dalfsen | 1 (nieuw) |')
d.line_replace('> **Toelichting PRO Dalfsen.**',
'> **Toelichting PRO Dalfsen.** Leander Broere staat in raadsstukken (besluitenlijsten) als fractievoorzitter van GroenLinks-PvdA en ondertekende motie 202604 (maart 2026) namens de PvdA; in september 2026 noemt Vechtdal Centraal hem "PRO-fractievoorzitter". PRO Dalfsen is daarmee vermoedelijk de nieuwe naam van de fractie GroenLinks-PvdA [I]; in geen gelezen bron bevestigd. De RTV Focus-kop "CDA stormt naar de winst in Dalfsen" [Z] past niet bij deze uitslag en is waarschijnlijk van een andere verkiezing; niet opgelost.')

# Bijlage A rows
d.line_replace('| A2 |','| A2 | Deels gevonden | Woondeal West-Overijssel (Actualisatie 20-3-2025, Bijlage 1): 479 gerealiseerd (Q1 2022-Q4 2024); 5 sleutelprojecten 2024-2030 = 1.039 woningen (Nieuwleusen Centrum 250, Oosterdalfsen Noord 400, Waterinkweg 206, De Koele II 83, Het Engelland 100); doorkijk 2031-2035: 1.155 (o.a. Palthelanden 600, Het Engelland 400). Raad nam kennis op 19-5-2025 (college 1-4-2025); Woondeal 2022 ondertekend 21-12-2022. Plancapaciteit 783 vóór 2030 (VHP bijlage II, 1-1-2024; buitengebied 40), streven 130%. Gerealiseerd 2023: 129, 2024: 138, 2025: 167. Telling CPO/VAB apart, 80/20-regel en post kleine kernen: niet gevonden | Woondeal Bijlage 1; raadsmemo Actualisatie Woondeal; VHP; Woonupdate 006 | Dashboard Wonen (GIS-portaal Overijssel); beleidsadviseur wonen |')
d.line_replace('| B4 |','| B4 | Gevonden (kaart) | Bijlage 1 bij de regeling adviesrecht (kaart 5-1-2022): compacte contouren "bestaand bebouwd gebied" per kern, rest buitengebied; "direct aangrenzend" niet gedefinieerd. De Tuindershof (Ankummer Es) wordt als "bebouwd gebied" behandeld (17 > 11). Het Engelland is een omgevingsplanwijziging met motivering van art. 4.4, 4.5 en 4.11; het PLG behandelt kern-randzones. Notitie Inbreidingslocaties 2023 is relevant voor locaties in de kern | CVDR705154 Bijlage 1; raadsvoorstel nr. 2064; Gmb 2025, 74695 | — |')
d.line_replace('| C1 |','| C1 | Deels gevonden | Provinciale typologie (kaartlaag art. 4.123) niet in de publieke WFS. Proxy: de voormalige ONW-zone beslaat 5,5% van Dalfsen (§3.7); de projectlocaties liggen 0,5-1,9 km van die zone [I: waarschijnlijk "generiek landbouwgebied"]. Gemeentelijk: Weids Platteland en het heideontginningsdeel van Landelijk Lemelerveld zijn "agrarisch focusgebied" (PLG) | WFS Provincie Overijssel; PLG §5.2.3, §5.6.3 | https://omgevingswet.overheid.nl/regels-op-de-kaart (definitieve kaartlaag) |')
d.line_replace('| C3 |','| C3 | Gevonden (kaartlaag) | Natura 2000 ligt **niet** in Dalfsen (Vecht- en Beneden-Reggegebied op 7 m, Uiterwaarden Zwarte Water en Vecht op 41 m van de gegeneraliseerde gemeentegrens); bij de projectlocaties 2,6-6,6 km. NNN 17,2%, landgoederen 19,6%, essen 9,0%, grondwaterbeschermingsgebied 2,0% (§3.7). Het eerdere "deels in Dalfsen" ([Z]) is niet bevestigd. Stikstof: Vechtdal is een gebied van de Gebiedsgerichte Aanpak Stikstof [Z]. Drinkwater: Vitens-winning en beschermingsgebied in de Marshoek/Vechterweerd (PLG); Salland Diep (provincie bevoegd): voorkeursvariant en MER eind 2027, vergunningaanvragen eind 2028 volgens Vitens. Nationaal Landschap: niet van toepassing. Raatakkers/karrensporen: niet onderzocht | Kaartberekening (WFS + PDOK); PLG §5.4.3.1.3, §5.6.15; https://www.vitens.nl/over-water/projecten/overijssel/salland | geoportaal Overijssel |')
d.line_replace('| D1 |','| D1 | Niet gevonden | Regeling 4.39 staat op 2026-10-05 nog open ("tot het budget bereikt is"; alleen voor gemeenten; adviesgesprek via vab@overijssel.nl; maximaal 2× per gemeente). Geen aanvraag of deelname van Dalfsen gevonden; Dalfsen heeft een eigen PLG en een Regisseur Landelijk Gebied. Het PLG noemt provinciale gebiedsprocessen "Toekomst voor ons Platteland" in Parels in het landschap en Landelijk Lemelerveld | https://regelen.overijssel.nl/Producten_en_diensten/Subsidies/Wonen_en_leefbaarheid/Beleid_transformatie_agrarische_bebouwing_erven_en_gronden | vab@overijssel.nl; besluitenlijst B&W |')
d.line_replace('| E1 |','| E1 | Deels gevonden | Omgevingstafel IJsselland (OD IJsselland): de gemeente bepaalt of een initiatief aan de regionale tafel komt; ketenpartners zijn GGD, waterschap, veiligheidsregio, omgevingsdienst, provincie en RWS; de initiatiefnemer "kan en mag aanwezig zijn", omwonenden niet. Dalfsen heeft daarnaast gemeentelijke "Omgevingstafels" als principeverzoek-route met leges (eenvoudig € 577,40; complex € 1.233,10). Provincie betrokken bij De Tuindershof (KGO-overleg, openheid van de es) en bij de locatiekeuze (DSS). Accounthouder: niet openbaar | https://www.odijsselland.nl/over/omgevingstafel ; Legesverordening 2026 ; raadsvoorstel nr. 2064 | Gemeentelijke RO-afdeling; Overijssel Loket |')
d.line_replace('| E4 |','| E4 | Niet gevonden | Provinciaal blad 2023-2026 doorzocht via de SRU-zoekservice (169 publicaties noemen Dalfsen): uitsluitend vergunningen, natuur, wegen en generieke provinciale besluiten; geen zienswijze, aanwijzing of onthouden instemming over Dalfser woningbouw of omgevingsplannen. Geen provinciale zienswijze op het PLG herkenbaar. Provincie wel betrokken (De Tuindershof, DSS) | repository.overheid.nl/sru (officielepublicaties, Prb) ; Nota van zienswijzen PLG | Provincie (accounthouder); zienswijzenoverzicht Het Engelland (niet gevonden) |')
d.line_replace('| F1 |','| F1 | Deels gevonden | Dalfsen gebruikte de **Adviespool Provincie Overijssel** (expertise-inhuur tot € 50.000, maximaal 2×) voor Het Engelland en zoekt een tweede mogelijkheid; vroeg het **Ondersteuningsteam Wonen Zorg** om steun voor Palthelanden en Het Engelland; onderzoekt de regeling **Betaalbaar wonen in kleine steden en dorpen** (nog geen aanvraag); noemt het rijksfonds NFBK en de rijksrealisatiestimulans. Flexpool en Langer zelfstandig wonen: niet gevonden. Vosserburen: Stimuleringsregeling Flex- en Transformatiewonen en Leader [Z] | Woonupdate 005 (8-7-2025); https://www.vechtdalcentraal.nl/2026/07/dertien-sociale-woningen-in-het-buitengebied-dertien-keer-een-thuis/ | regelen.overijssel.nl |')

d.insert_after_line('- **Kavelaanbod en projectstanden**',
'''- **Provinciaal Volkshuisvestingsprogramma Overijssel 2026-2035:** ontwerp ter inzage 16-7 t/m 26-8-2026; vaststelling door GS niet gevonden. Kan de Overijsselse kaders voor VAB, collectieve woonvormen en kleine kernen verduidelijken.
- **Landbouwgebied-typologie:** definitieve provinciale kaartlaag (art. 4.123) en toepassing op de Dalfser locaties.
- **Subsidie 4.39** staat op 2026-10-05 nog open voor aanvragen.''')

new13='''## 13. Lacunes en aanbevelingen voor vervolgonderzoek

**Stand van de leesopdrachten uit het concept (2026-10-02 → 2026-10-05):**

| # | Opdracht (concept) | Status | Resultaat |
|---|---|---|---|
| 1 | CVDR674315 (/1 en /2) lezen: sloopmaten, maximaal drie woningen, KGO-formule, wijzigingsdatum versie /2 | **Afgehandeld** | Sloopmaten en drie-woningengrens bevestigd (§3.1); KGO is maatwerk zonder formule; vaststelling raad 28-2-2022, in werking 16-3-2022; versie /2 vanaf 10-6-2022 wijzigt alleen het begrip "bestaand erf" |
| 2 | PLG (CVDR760428/1; uitgever; Nota van zienswijzen; provinciale reactie) | **Afgehandeld** | Uitgever Dalfsen (gm0148); college 10-2-2026, geldend 15-4-2026; raad nam kennis 16-3-2026 met moties; geen zienswijze van de provincie herkenbaar; Sloop voor kansen en VAB worden los van het PLG herzien |
| 3 | VHP 2025-2029, Woonupdates 004-006, raadsmemo Actualisatie Woondeal | **Afgehandeld, op Woonupdate 004 na** | VHP, Woonupdates 005 en 006 en het raadsmemo Actualisatie Woondeal gelezen; de sleutelprojecten zijn met Bijlage 1 van de Woondeal opgelost (§5). Woonupdate 004 (en eerder) niet gelezen; inhoudelijk ingehaald door 005 en 006 |
| 4 | Coalitieakkoord 2026-2030 en bericht 1-10-2026 | **Afgehandeld** | Geen CPO/zelfbouw/erven in het akkoord; 800 woningen; sociale erfpacht; PLG uitvoeren. Bericht: raad 30-9-2026, overschot naar reserve, versnelling voorbereiding woningbouwlocaties |
| 5 | De Tuindershof (KGO-onderbouwing; raad 16-3-2026) en 5e Verzamelplan | **Afgehandeld** | KGO-onderbouwing, ruimtelijke onderbouwing en raadsvoorstel gelezen (§6). Het "5e Verzamelplan" bleek niet de relevante stap: het 9e Verzamelplan en de Erfwonen-beeldkwaliteitsplannen zijn via Gemeenteblad en gemeentesite gelezen (§3.1); de toelichting van het 9e Verzamelplan zelf niet |
| 6 | Het Engelland (Gmb 2025-74695; zienswijzen); Notitie Inbreidingslocaties; Notitie adviesrecht | **Afgehandeld** | Het Engelland, Inbreidingsnotitie en de Dalfser regeling adviesrecht (CVDR705154) gelezen, inclusief de kaart in Bijlage 1; het concept-nummer CVDR727504 is Montfoort. Een zienswijzenoverzicht bij Het Engelland is niet gevonden |
| 7 | Nota Grondbeleid 2026, grondprijzenbrief 2026, Legesverordening 2026; Gemeenteblad/Provinciaal blad (E4) | **Afgehandeld** | Nota, grondprijzen (webpagina) en leges gelezen; de grondprijzenbrief-PDF is niet apart geopend (webpagina geeft dezelfde tabel). E4: Provinciaal blad systematisch doorzocht, geen zienswijze of onthouden instemming gevonden |
| 8 | Vosserburen: vergunning en juridische route | **Afgehandeld voor de route** | Omgevingsvergunning in de uitgebreide procedure met verklaring van geen bedenkingen; ca. 12 maanden (§6). De vergunningtekst en de precieze voorwaarden (20 jaar) zijn niet gelezen |
| 9 | Kaartlagen | **Grotendeels** | Provinciale WFS-lagen (voormalige ONW-zone, NNN, Natura 2000, grondwaterbescherming, waterwin, essen, landgoederen) doorsneden met de gemeentegrens (§3.7); Natura 2000 ligt niet in Dalfsen. De nieuwe landbouwgebied-typologie (art. 4.123) is niet publiek via de WFS; Dashboard/Planmonitor Wonen niet bevraagd |
| 10 | Niet onderzocht: D1/D2/F1; Hoonhorst/Ankum/Oudleusen; De Stentor/RTV Oost; Platform31/Het Kan Wel; coalitiecrisis; Engbertsdijksvenen; Vilsteren/'t Laer | **Afgehandeld, met rest** | D1: regeling 4.39 open, geen Dalfser aanvraag; F1: Adviespool, Ondersteuningsteam, Betaalbaar wonen (zie Bijlage A). Hoonhorst en Oudleusen via Woonupdate 006 en de CPO-lijst (§7). Coalitiestabiliteit gecontroleerd tot 30-9-2026. Landgoed Vilsteren ligt in Ommen (PDOK-adresregister), niet in Dalfsen; Engbertsdijksvenen is niet als woonplaats in Dalfsen terug te vinden. Niet gedaan: De Stentor (betaalmuur), RTV Oost, Platform31, Het Kan Wel, 't Laer |
| 11 | Vragen aan de gemeente | **Open** | Alleen bij de gemeente te beantwoorden; zie hieronder |

**Resterende lacunes en aanbevelingen:**
1. **Uitwerking motie 202604 en PLG-kaders** voor "alternatieve woonvormen op vrijkomende erven" en Rood-voor-Groen/Blauw. Volgen in het RIS rond Q4 2026; ook het eerste jaarlijkse Uitvoeringsplan PLG.
2. **Herziening Beleidsregels 2022** (Sloop voor kansen/VAB) en het nieuwe omgevingsplan voor het buitengebied: planning opvragen.
3. **Definitieve provinciale kaartlaag landbouwgebied-typologie** (art. 4.123) voor de kandidaatlocatie; de proxy in §3.7 is alleen indicatief.
4. **Provinciaal Volkshuisvestingsprogramma Overijssel:** vaststelling door GS afwachten en kaders voor VAB en collectieve woonvormen toetsen.
5. **"Boerenerf wonen"** (begrip in de Legesverordening 2026): navragen of hiervoor een aparte regeling of werkwijze bestaat.
6. **Vergunningtekst Vosserburen** (voorwaarden, 20 jaar, tijdelijkheid) en de toelichting van het 9e Verzamelplan.
7. **Woonupdate 004**, het Woningbehoefteonderzoek (in voorbereiding) en de grondprijzenbrief 2027 (december 2026).
8. **BuitenDelen (Lettele, Deventer)** als CPO op voormalig agrarisch erf: onderzoeken in het Deventer-rapport.
9. **Vragen aan de gemeente:**
   - kan een bestaand burgercollectief (geen individuele loting) via VHP-maatregel 8 een plek krijgen op een uitleglocatie of in een projectmatige uitgifte;
   - is een CPO van 10-12 woningen op een vrijkomend erf in Variatie rond de Vecht of Parels in het landschap bespreekbaar via KGO;
   - welke provinciale accounthouder is betrokken;
   - telt zo'n plan mee in de buitengebiedpost van de plancapaciteit;
   - wat is de status van de herziening van de Beleidsregels 2022 en van de uitwerking van motie 202604.

---
'''
d.replace_section('## 13. Lacunes en aanbevelingen voor vervolgonderzoek','## Overijssel-controlepunten (Bijlage A)',new13)
d.save(); print('ok')
