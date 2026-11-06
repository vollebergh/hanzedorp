# Openstaande punten per rapport (stand 2026-11-01)

Afgeleid uit de secties "Niet gevonden", "Open punten", "Lacunes" en "Houdbaarheid" van elk rapport.

> **Update 2026-11-06:** de DSO-API-key werkt (Presenteren v8). Welke punten hiermee alsnog te achterhalen zijn, staat in `dso-inventarisatie.md`.

**Haalbaarheid door Claude (zelf):**
- **A: Zelf te doen.** Openbare bron die ik met web, CVDR/SRU, Open Besluitvorming of PDOK/WFS kan bereiken.
- **B: Deels.** Ik heb hulp nodig bij toegang (browser met inlog, DSO-sleutel) of de bron is lastig machineleesbaar.
- **C: Alleen jij.** Niet openbaar, of alleen via de gemeente/provincie (Woo-verzoek, vooroverleg, persoonlijk contact).
- **T: Tijd.** Besluit of publicatie is er nog niet. Herverifiëren na de genoemde datum.

## 1. Terugkerende lacunes (komen in vrijwel elk rapport voor)

| Lacune | Gemeenten | Haalbaar | Wat ik nodig heb |
|---|---|---|---|
| Planregels / VAB-regels in het omgevingsplan (aantal woningen per erf, wijzigingsbevoegdheden) via DSO "Regels op de kaart" | alle | B | Een DSO-API-sleutel (gratis aan te vragen bij het Kadaster/DSO), of dat jij per kandidaatlocatie de regeltekst uit het Omgevingsloket kopieert |
| Provinciale kaartlagen per locatie (GOZ/GNN, stikstofreductiegebied, landbouwgebied-typologie art. 4.123) | alle | A, pas bruikbaar bij een concrete locatie | Een adres of kadastraal perceel. Alleen indicatief per gemeente; per kavel is het pas betrouwbaar |
| Correspondentie met de provincie: Regisseur Ruimte, accounthouder, GS-instemming bij BOPA's, Matrix-afspraken | alle | C | Woo-verzoek aan de provincie, of vooroverleg via Provincieloket (026 359 99 99) resp. Overijssel Loket (038 499 88 99). Ik kan de Woo-verzoeken opstellen; jij dient ze in |
| Anterieure overeenkomsten, omgevingstafelverslagen, collegestukken die niet openbaar zijn | alle | C | Woo-verzoek (concept door mij) |
| CPO-beleid, zelfbouwloket, kavelreservering, CPO-grondprijs | vrijwel alle | C | Een conceptverzoek/gesprek met de gemeente. Veelal bestaat er niets, wat ook een bevinding is |
| Volkshuisvestingsprogramma's (wettelijk uiterlijk 1-7-2027) | alle | T | Herverifiëren in 2027 |
| Uitkomsten van raadsbesluiten/stemmingen die na de laatste actualisatie plaatsvonden | zie §3 | A | Niets. Ik zoek ze op in Open Besluitvorming |
| Planmonitor/LMVW: harde en zachte plancapaciteit per gemeente | alle | B | De dashboards zijn deels Tableau/JS. Ik probeer ze; lukt dat niet, dan een export of screenshot van jou |
| Betaalmuurkranten (De Stentor, Tubantia, Gelderlander) en 403-pagina's | alle | B | Ik kan Chrome gebruiken als de extensie is verbonden en jij bent ingelogd. Alternatief: jij plakt de tekst |
| Partijprogramma's en collegeprogramma's 2026-2030 | diverse | A (T bij nog niet verschenen) | Niets |
| Jurisprudentie (Raad van State/rechtspraak.nl) | Elburg, Epe, Ermelo, Nunspeet, Voorst, Hardenberg, Kampen, Raalte | A | Niets |
| Scan-PDF's zonder tekstlaag | Hardenberg, Raalte, Ommen, Voorst, Zwartewaterland | A/B | Ik kan OCR proberen. Bij slechte kwaliteit heb ik een betere kopie nodig |

## 2. Provinciale referentiekaders

**Gelderland (`provincie_gelderland.md`)**
- L1.1/L2.1/L3.2: tekst van de verordeningwijziging die op 23-10-2026 in werking trad (Prb, nieuwe CVDR705323-versie). **A**: moet nu gepubliceerd zijn. Dit is de belangrijkste herverificatie, want artikelnummers (hoofdstuk 4a, art. 5.62a, par. 5.7.8) kunnen zijn verschoven. Alle 9 Gelderse rapporten citeren die nummers.
- L1.2/L1.3: definitieve Omgevingsvisie, PS-besluit 16-12-2026. **T**
- L3.1/L3.9/L3.10: Gelders programma wonen, KB termijnen, Besluit versterking regie volkshuisvesting (1-1-2027). **T**, tussentijds **A** voor de RvS-status.
- L3.4/L3.5: plancapaciteit per gemeente en toedeling van de 3.520 Stedendriehoek-woningen. **B**.
- L2.4/L1.6: begrenzing stikstofreductiegebieden en overlays per gemeente. **A** via de nieuwe kaartlaag, alleen indicatief.
- Subsidie Collectieve wooninitiatieven: resterend plafond (€ 250.000). **C**, alleen zichtbaar in het Subsidieportaal.
- Resultaten pilot "Wonen op de boerderij" (eind 2026). **T**

**Overijssel (`provincie_overijssel.md`)**
- Vaststelling provinciaal volkshuisvestingsprogramma (ontwerp tot 26-8-2026). **A**: kan inmiddels zijn vastgesteld.
- Nieuwe Handreiking/Werkboek KGO ("in de maak"). **A/T**
- Actualisatie 2026-2 Omgevingsverordening (PS december 2026). **T**
- Subsidie 4.39: plafond € 1.640.250, status vóór eind 2026. **A** (regelen.overijssel.nl) en **C** voor de Overijsselse deelnemerslijst.
- Aangenomen amendementen op de Omgevingsvisie. **A**: Statenstukken.
- Catalogus Gebiedskenmerken (Bijlage VII). **A**
- Accounthouders per gemeente. **C**

## 3. Per gemeente

### Overijssel

| Rapport | Voornaamste open punten | Haalbaar | Wat ik nodig heb |
|---|---|---|---|
| **Zwolle** | Gebiedsspecifieke VAB-regels in het omgevingsplan; Handreiking KGO Zwolle (intern); Volkshuisvestingsprogramma (gepland Q3 2026); uitkomst huisvestingsverordening; woningbehoefteonderzoek 2025; grondprijzenbrief 2026 (volledige PDF); zwolle.nl geeft 403 | A (programma, verordening, onderzoek), B (403-pagina's, DSO), C (interne Handreiking: Woo) | Chrome-sessie of tekst van de 403-pagina's; Woo-verzoek voor de Handreiking |
| **Kampen** | RIS niet toegankelijk (startnotitie Volkshuisvestingsprogramma, Woningbehoefteonderzoek, moties CPO/VAB); Uitvoeringskader VAB IJsseldelta; uitkomst beroep Kamper Wetering; reactienota's Zalk Erf 4/5; 13 resterende tegenstrijdigheden (o.a. Broekswetering-aantallen, woningaantal per erf 2 vs. 3) | B (RIS via browser of ORI; nu mogelijk via ORI), A (rechtspraak), C (Uitvoeringskader, vragen aan vooroverleg@kampen.nl) | Chrome-sessie voor kampen.raadsinformatie.nl; jij stuurt de vooroverlegvraag (concept door mij) |
| **Dalfsen** | Uitwerking motie 202604 en PLG-kaders (Q4 2026); herziening Beleidsregels 2022 (Sloop voor kansen/VAB); "Boerenerf wonen" in de Legesverordening; vergunningtekst Vosserburen; Woonupdate 004; vijf vragen aan de gemeente (burgercollectief via VHP-maatregel 8, CPO op erf via KGO, accounthouder, plancapaciteit) | A (RIS-stukken), T (herziening), C (vijf vragen) | Jouw akkoord om de vragen aan de gemeente te sturen |
| **Deventer** | Vaststelling Volkshuisvestingsprogramma; Omgevingsvisie 2040 (raadsbesluit 18-11 of 16-12-2026); collegeprogramma 2026-2030; regeltekst VAB/splitsing; Compensatiefonds; BuitenDelen (status, KGO-bedragen); Combiplannen 5-9; legestarieven na 1-7-2026 | A (RIS), T (Omgevingsvisie), C (BuitenDelen: contact met de coöperatie; anterieure overeenkomst) | Contact met buitendelenlettele@gmail.com is aan jou, of geef toestemming |
| **Hardenberg** | Hofje Stobbenhaarweg 1 (vaststelling, zienswijzen); Bestuurlijke Opdracht "Hardenberg Buitengebied" en overeenkomst met de provincie; Nota grondbeleid; stemuitslag motie "Erven met kwaliteit" (scan); rangordelijst netcongestie (xlsx); prijzen CPO-kavels Kloosterhaar | A (nota, rangordelijst, RIS), B (scan met OCR), C (Bestuurlijke Opdracht: griffie of Woo) | Niets voor A. Woo-concept voor de Bestuurlijke Opdracht |
| **Ommen** | Ruimtelijke Visie 2040 (niet openbaar); Woningbehoefteonderzoek 2024; grondprijsbrief; VAB-regel in het moederplan Buitengebied; Strategieboek Regio Zwolle (PDF leeg); Hammerflier-besluit; uitkomst burgemeestersprocedure; stikstof/opschorting natuurvergunningen | A (merendeel), B (DSO-regel, PDF), C (niet-openbare visie) | DSO-sleutel of regeltekst van jou |
| **Raalte** | "Wisselerf" Broekland en Neppelenbroek (aard onbekend); waarom 15 posities van de volgordelijst vervielen; beroep Raarhoeksweg 47; Groeibeelden-documenten en "Analyse wonen buitengebied" (grote beeld-PDF's); Nota Grondprijsbeleid en notitie Collectief Opdrachtgeverschap (niet in RIS); sloopverhoudingstabel (afbeelding) | A (rechtspraak, deel PDF's), B (beeld-PDF's via OCR), C (Wisselerf, volgordelijst: stroomnet@raalte.nl, ruimtecoach@raalte.nl) | Mail naar de gemeente (concept door mij) |
| **Hellendoorn** | Woningbehoefteonderzoek 2024; plan Marle; formele zienswijze op de provinciale Omgevingsvisie; kaartbijlagen; deelname regeling 4.39 en West-Twentse intentieovereenkomst; plantoelichtingen Raamsweg 6/Haarlerveldweg 12 | A (merendeel; digitaleplannen.nl), B (Tubantia), C (accounthouder) | Niets voor A |
| **Olst-Wijhe** | Wijlandhof en De Brinkweiden (12 woningen, alleen op de volgordelijst); contour bebouwd gebied; bestuurlijke afspraken Herxen; uitwerking motie 26-5-2026 (CPO); bouwsteen Erfontwikkeling (nov. 2026); Holsthoek (7-9-2026); Klimboom-uitkomst; provinciale instemmingsbrieven (Woo) | A (iBabs-uitkomsten), T (bouwsteen nov. 2026), C (zaakdossiers en instemmingen: Woo) | Woo-concepten; voorgesprek met team Ruimtelijke Realisatie |

### Gelderland

| Rapport | Voornaamste open punten | Haalbaar | Wat ik nodig heb |
|---|---|---|---|
| **Apeldoorn** | Wegingsmodel raadsversie vs. collegeversie; uitslag raadsbesluiten Uddelerveen 72 en Garderenseweg (24-09-2026); Volkshuisvestingskader per project (30%-regel?); Legesverordening 2026 (2e wijziging); kavelprijzen Zuidbroek (beeld-PDF); rekensysteem GOZ vs. Verordening Groene Balans (bespreken in voorgesprek); 10.400 vs. 8.838 | A (uitslagen, leges, besluiten), B (kavelpaspoort: OCR), C (GOZ vs. Groene Balans: vraag aan gemeente; kavelprijzen: kavelsenpanden@apeldoorn.nl) | Jouw akkoord op de vraag aan de gemeente |
| **Elburg** | Nieuw VAB- en buitengebiedbeleid met afwegingsmatrix (verwacht Q1 2026, nog niet gevonden); evaluatie november 2026; uitkomst 't Hasenest; antwoorden CU/CDA-vragen; kavelprijzen Gerichtenweg Hoge Enk; bijlagen 9-10 Omgevingsvisie (kostenverhaal); jurisprudentie; gemeenteraadslijsten/burgemeester | A (RIS, bijlagen, rechtspraak), T (evaluatie nov. 2026), C (kavelprijzen via makelaar; omgevingstafelverslagen: Woo) | Niets voor A |
| **Epe** | Uitkomst raadsbesluit Kopermolen (15-10-2026); stemuitslag amendement VAB-staffel; VAB-evaluatie; Epe-zienswijze op ontwerp-Omgevingsvisie; origineel GO-toets Gortelseweg 18; ECLI:NL:RVS:2026:608; CPO-beleid ontbreekt; collegebesluitenlijsten | A (alle genoemde stukken), C (CPO-beleid: wethouder Tibben/Hans Stijf) | Niets voor A |
| **Ermelo** | Collegebesluit afwegingskader 2024-2026 en Bijlage 1; herziening functieveranderingsbeleid; Prestatieafspraken 2026; GOZ-puntenaantallen Garderenseweg 60 en De Beek 77 (volledige TAM-plannen); uitkomst recherche-onderzoek (medio nov. 2026); Raadsbesluit Tonnenberg 8; Raad van State De Beek 77; Ermelo's Weekblad | A (TAM-plannen via RIS, besluiten, ERS), T (recherche, Programma Wonen eind 2026), C (anterieure overeenkomsten) | Niets voor A. Woo-concept voor overeenkomsten |
| **Harderwijk** | Tekst Volkshuisvestelijk omgevingsprogramma (2025); Gebiedsprogramma Hierden buiten; aantal woningen per erf in Beoordelingsregels boerenerven; Bindend Advieslijst; rood-voor-rood in omgevingsplan (DSO); ranglijst netaansluiting (na 1-10-2026); Nota grondbeleid; collegeprogramma 2026-2030; stemuitslag amendement 27-05-2021 | A (RIS, bijlagen), B (DSO), T (collegeprogramma, ranglijst) | DSO-sleutel voor de omgevingsplantekst |
| **Hattem** | Functieveranderingsbeleid (welk document?); toetsingskader woningbouwinitiatieven; stand 80-woningenplafond; weigeringsgronden Geldersedijk 28; zienswijze op ontwerp-Omgevingsvisie Gelderland; provinciale vooroverlegreactie Chw-plan; bijlage 3 raadsvoorstel Veenwal-Apeldoornseweg; Nota Grondbeleid; Prestatieafspraken 2025-2028 | A (de meeste), C (functieverandering: team Leefomgeving; 80-woningenplafond) | Niets voor A. Vraag aan team Leefomgeving over het document en het plafond |
| **Heerde** | Notitie Functieverandering 2011, Leidraad 2014, Uitvoeringsparagraaf 6.0 (2019) met vereveningsbedragen, Woonvisie 2015-2025 (archief); nota van uitgangspunten functieverandering; themaraad 05-10-2026; Planregels Buitengebied West/Oost; zetelverdeling (CSB-uitslag); regionale zienswijzen | A (RIS, ruimtelijkeplannen, CSB), C (archiefstukken: Woo bij heerde.nl) | Woo-concept voor archiefstukken |
| **Nunspeet** | Planregels Buitengebied 2023 (art. 44.1.4); College-vaststellingsbesluit Functieveranderingsbeleid 2026-2028 (formele werking per 2026-10-19 niet geverifieerd); uitslag raad Zwolse Hofje (29-10-2026); RvS 't Hul-Noord (zitting 01-10-2026); WOM-ronde 2026/27; stikstofbeleidsregel gemeente; prestatieafspraken | A (uitslagen sinds 29-10), B (DSO), C (stikstofbeleid) | DSO-sleutel |
| **Oldebroek** | PVPO-programmatekst en Structuurvisie 2017 (NL.IMRO.0269.SV104-VG01); Programma kostenverhaal; volgordelijst netcongestie; uitkomst Zuiderzeestraatweg 342; of een CPO onder de 250-woningenreserve valt; status afwegingskader onder nieuw college | A (stukken), C (drie vragen aan wonen@oldebroek.nl) | Jouw akkoord op de vraag aan de gemeente |
| **Voorst** | Verlenging Rood voor Groen / Programma Ruimtelijke Kwaliteit (geen raadsbesluit gevonden); Volkshuisvestingsprogramma (ontwerp); raadsvoorstel 9-3-2026; vereveningstabel boven 10 woningen; tijdelijk deel (Buitengebied 2013/2014/2019, Paraplu Kwaliteitsbepalingen 2022); raadsbesluit BOPA Wilp-Achterhoek; ABRvS Twello-Noord (herstelbesluit 13-7-2026); winnaar CPO-groep Hessenlaan; 94-p. ontwerp-Omgevingsvisie niet integraal gelezen | A (RIS/Notubiz, rechtspraak), B (ruimtelijkeplannen/DSO), C (Hessenlaan: Grondzaken J. Beer; collegebesluit Rood voor Groen: afdeling Ruimte) | Niets voor A. Vragen aan de gemeente voor C |
| **Zwartewaterland** | CPO-/zelfbouwbeleid (niet gevonden); huisvestingsverordening/urgentie (niet vastgesteld); aantal woningen per CPO in Binnenveld; KGO-beleidsregel 2015 (vaststellingsbesluit); Buitengebied 2013 buiten art. 3.2/3.8/23; Catalogus Gebiedskenmerken; brief college 28-5-2024 (scan) | A/B, C (Binnenveld: binnenveld@zwartewaterland.nl) | Niets voor A |

## 4. Tegenstrijdigheden die alleen de gemeente kan oplossen

Een groot deel van de "tegenstrijdigheden" (koopprijsgrenzen, woningaantallen per project, opgave-aantallen) komt voort uit verschillende peildata of definities. Ik kan ze nalopen, maar bij een kandidaatlocatie komt het neer op één vraag aan de gemeente: welk document geldt nu? Voorbeelden: Elburg (bindend adviesrecht 5 vs. 2), Ermelo/Epe/Apeldoorn (koopprijsgrens), Kampen (woningaantal per erf 2 vs. 3).

## 5. Wat ik van jou nodig heb (samengevat)

1. **Beslissing over locatiebepaling.** Alle "per locatie"-lacunes (kaartlagen, planregels, stikstof) kan ik pas goed invullen met een kandidaatlocatie of voorkeurskernen. Zonder dat blijft het indicatief per gemeente.
2. **Toegang tot browser-only bronnen.** Chrome-extensie verbonden en zo nodig ingelogd (Stentor, Tubantia) voor RIS/403-pagina's (Kampen, Zwolle), of de tekst van jou.
3. **DSO-API-sleutel** (optioneel) voor automatische omgevingsplantekst. Zonder sleutel plak jij de regeltekst per locatie uit het Omgevingsloket.
4. **Woo-verzoeken en vooroverleg.** Ik schrijf de concepten (provincie: Regisseur Ruimte/accounthouder/instemming BOPA; gemeenten: anterieure overeenkomsten, interne Handreikingen, archiefstukken). Jij dient ze in of geeft akkoord dat ik ze via jouw kanaal stuur.
5. **Vragen aan gemeenten.** De vragen over CPO-mogelijkheden (Dalfsen, Oldebroek, Kampen, Apeldoorn, Hattem e.a.) stuur jij, of jij geeft aan dat ik ze in een mailconcept zet.
6. **Prioriteit.** Welke gemeenten vallen af of staan bovenaan? Ik stel voor eerst de herverificatie van de Gelderse verordening (23-10-2026) en de uitslagen van raadsbesluiten sinds de laatste actualisatie uit te voeren.
