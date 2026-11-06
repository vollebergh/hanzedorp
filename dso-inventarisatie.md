# DSO-inventarisatie: wat de API alsnog kan opleveren (stand 2026-11-06)

Aanvulling op `openstaande-punten.md`. Hier staat alleen wat getest is en welke open punten daarmee bereikbaar worden. Het eigenlijke zoekwerk en het bijwerken van de rapporten volgen later, met Sonnet op high effort.

## 1. Testresultaat API-key (`dso.txt`, niet in git)

| API | Basis-URL | Resultaat |
|---|---|---|
| **Omgevingsdocumenten Presenteren v8** (Ozon), header `x-api-key` | `https://service.omgevingswet.overheid.nl/publiek/omgevingsdocumenten/api/presenteren/v8` | **Geldig** (200; zonder key 401). Regelingen, ontwerpregelingen, omgevingsvergunningen, documentstructuur (volledige regeltekst als STOP-XML), annotaties en zoeken op geometrie (RD, EPSG:28992) werken. |
| **Ruimtelijke Plannen opvragen v4** (Kadaster), header `X-Api-Key` | `https://ruimte.omgevingswet.overheid.nl/ruimtelijke-plannen/api/opvragen/v4` | Met `dso.txt`: ongeldig (401). Met **`rp.txt` (gitignored): geldig** (getest 2026-11-06). Plannen per gemeente, planteksten (XHTML), zoeken op geometrie en `_suggesties` werken. Zie §6. |
| ruimtelijkeplannen.nl documentpagina's (geen key) | `https://www.ruimtelijkeplannen.nl/documents/<IMRO-id>/r_<IMRO-id>.html` | **Werkt**, maar alleen met het volledige IMRO-id inclusief versie. Getest met Nunspeet Buitengebied 2023 `NL.IMRO.0302.BP01207-vg04`: de regels zijn volledig leesbaar. De ID's in de rapporten zonder versie-achtervoegsel (Ommen, Voorst, Oldebroek, Heerde) geven 404. |

**Gevolg:** met beide keys is het complete omgevingsplan programmatisch bereikbaar:
- via Ozon: het **nieuwe deel**, provinciale verordeningen, omgevingsvisies, programma's, ontwerpen en een deel van de vergunningen;
- via de RP-API: het **tijdelijk deel**, dus oude bestemmingsplannen, TAM-plannen en structuurvisies.

Daarmee zijn alle **J\***-punten in §3 nu gewoon **J**.

## 2. Nieuwe feiten uit de verkenning (nog niet in de rapporten)

Gevonden bij de inventaris per bevoegd gezag. Dit zijn alleen metadata; de inhoud is nog niet gelezen.

- **Omgevingsverordening Gelderland:** versie 10, **in werking volgens DSO 26-10-2026** (geregistreerd 16-10-2026). De rapporten en `provincie_gelderland.md` noemen 23-10-2026. Dit moet worden geverifieerd. De tekst bevat hoofdstuk 4a (stikstofreductiegebied) en netbewuste woningbouw.
- **Ontwerp "Gelders programma Wonen"** staat in DSO (bill pv25/2026, werk 16-10-2026). `provincie_gelderland.md` L3.1 zegt "geen ontwerp gevonden".
- **Ontwerp Volkshuisvestingsprogramma Overijssel 2026-2035** en **ontwerp Omgevingsverordening Overijssel 2026** (actualisatie 2026-2) staan in DSO. Een vastgestelde versie staat er nog niet.
- **Oldebroek:** ontwerp **Omgevingsprogramma Volkshuisvesting**.
- **Zwartewaterland:** **Omgevingsvisie in werking per 08-10-2026**.
- **Hellendoorn:** ontwerp **Omgevingsvisie Hellendoorn 2040 "Ruimte voor elkaar"**.
- **Raalte:** Programma **Groei, wonen en werken** (in werking 24-12-2025).
- **Harderwijk:** Gebiedsprogramma **Hierden dorp** (11-08-2026); Omgevingsprogramma **mens en maatschappij** (19-08-2026). Dat laatste bevat mogelijk het volkshuisvestelijk programma.
- **Voorst** (ontwerp-Omgevingsvisie + ontwerp-omgevingsplan), **Deventer** (ontwerp-Omgevingsvisie, ontwerp-Volkshuisvestingsprogramma), **Zwolle**, **Kampen**, **Elburg**, **Apeldoorn**: ontwerp-omgevingsvisies of -omgevingsplanwijzigingen staan met renvooi in DSO.
- **Gepubliceerde omgevingsvergunningen** per gemeente. Tussen haakjes: het aantal met "woning", "BOPA" of "functiewijziging" in de titel, gevolgd door het totaal:
  - Voorst (53/56), Epe (35/38), Dalfsen (37/93), Zwolle (24/40), Deventer (23/89), Olst-Wijhe (17/33), Kampen, Raalte en Hellendoorn (elk 12).
  - Bij Hattem, Oldebroek, Heerde en Nunspeet geeft de titel geen bruikbaar signaal.

  Dit is een bruikbare bron voor precedenten (functiewijziging naar wonen, splitsing van boerderijen), maar geen volledig register.

## 3. Open punten die met DSO alsnog te achterhalen zijn

Legenda: **J** = met de huidige key te doen; **J\*** = te doen als het volledige plan-ID via Gemeenteblad of planviewer wordt gevonden (ruimtelijkeplannen.nl-documentpagina); **L** = pas zinvol bij een concrete locatie (zoeken op geometrie); **N** = niet via DSO.

### Provinciaal

| Open punt (`openstaande-punten.md`) | DSO | Toelichting |
|---|---|---|
| Gelderland L1.1/L2.1/L3.2: definitieve tekst verordeningwijziging, artikelnummers 4a / 5.62a / 5.7.8 | **J** | Versie 10 volledig uitleesbaar. Kernklus: alle 9 Gelderse rapporten nalopen op verschoven artikelnummers en de datum 23-10 vs. 26-10 |
| Gelderland L3.3: kaart woningbouwregio's; L2.4/L1.6: begrenzing stikstofreductiegebied en overlays per gemeente | **J/L** | Via annotaties (gebiedsaanwijzingen/locaties); per gemeente indicatief, per perceel exact |
| Gelderland L3.1: Gelders programma Wonen | **J** | Ontwerp gevonden; inhoud nog te lezen (kleine kernen/buitengebied/CPO) |
| Gelderland L1.2: Omgevingsvisie | deels | Alleen ontwerp (20-04-2026) in DSO; definitief na PS 16-12-2026 |
| Gelderland L2.7: nationale landschappen in kaartlaag | **J** | Gebiedsaanwijzing in de verordening |
| Overijssel: provinciaal Volkshuisvestingsprogramma | **J** (ontwerp) | Vaststelling staat niet in DSO, dus nog niet vastgesteld |
| Overijssel: actualisatie 2026-2 verordening | **J** (ontwerp) | Inhoud nagaan op gevolgen voor KGO/wonen |
| Overijssel 6.2 punt 10 / gemeenten: Catalogus Gebiedskenmerken (Bijlage VII) | **J** | Onderdeel van de verordening |
| Overijssel: landbouwgebied-typologie art. 4.123 per locatie | **L** | Zoeken op geometrie geeft de gebiedsaanwijzingen |

### Per gemeente

| Gemeente | Met DSO te achterhalen | Niet via DSO (blijft zoals in `openstaande-punten.md`) |
|---|---|---|
| **Zwolle** | Gebiedsspecifieke VAB-regels in het omgevingsplan (nieuw deel, **J**; tijdelijk deel **J\***); ontwerp-Omgevingsvisie (status, contour stadsrand) **J**; Zwolse BOPA-praktijk (24 vergunningen) **J** | Handreiking KGO, volkshuisvestingsprogramma, grondprijzen |
| **Kampen** | Ow-BOPA's 2025-2026 identificeren (**J**); ontwerp-omgevingsplanwijzigingen 2025/2026 op VAB-uitwerking (**J**); Buitengebied 2014-regels **J\*** (de tegenstrijdigheid 2 vs. 3 woningen staat in de plantekst zelf en is alleen te duiden, niet op te lossen) | RIS-stukken, provinciale reactie, beroep Kamper Wetering |
| **Dalfsen** | Ontwerp-omgevingsplanwijziging (mogelijk buitengebied) **J**; vergunningen o.a. Vosserburen (metadata en verwijzing naar het Gemeenteblad) **J** | Herziening Beleidsregels 2022 (CVDR), vragen aan de gemeente |
| **Deventer** | Ontwerp-Volkshuisvestingsprogramma en ontwerp-Omgevingsvisie (contour, stads-/dorpsrand, intrekking Woonvisies) **J**; regeltekst VAB/splitsing (D125a) en Combiplannen 5-9 **J\***; typologie per locatie **L** | Vaststellingsbesluiten in de raad, BuitenDelen, Compensatiefonds |
| **Hardenberg** | "Programma voor Gemeente Hardenberg" (inhoud onbekend) **J**; 5 ontwerp-omgevingsplanwijzigingen (mogelijk Stobbenhaarweg) **J**; Catalogus Gebiedskenmerken **J** | Bestuurlijke Opdracht Buitengebied, rangordelijst, Nota grondbeleid |
| **Ommen** | VAB-regel moederplan Buitengebied **J\*** (plan-ID met versie nodig); Catalogus **J**; ontwerp-omgevingsplannen **J** | Ruimtelijke Visie 2040 (niet openbaar), Woningbehoefteonderzoek |
| **Raalte** | Programma Groei, wonen en werken (mogelijk de Groeibeelden en de koers voor het buitengebied) **J**; ontwerp-omgevingsplanwijzigingen 2026 **J**; vergunningen (plattelandswoning, functiewijziging) **J** | Wisselerf/Neppelenbroek, volgordelijst, beroep Raarhoeksweg |
| **Hellendoorn** | Ontwerp-Omgevingsvisie 2040 inclusief kaartbijlagen (deelgebied "de Buurtschappen") **J**; Bijlage III raatakkers/karrensporen (voorbeschermingsregels) **J**; motivering Nieuwstadweg 5a (bijlage omgevingsplan) **J**; plantoelichtingen Raamsweg 6/Haarlerveldweg 12 **J\*** | Woningbehoefteonderzoek, formele zienswijze, accounthouder |
| **Olst-Wijhe** | Ontwerp-Omgevingsvisie (contour bestaand bebouwd gebied) **J**; gepubliceerde BOPA's Vettewinkelweg 2 / Lierderholthuisweg 3 / Engeweg **J** (metadata; geen provinciale instemming) | Wijlandhof/De Brinkweiden, Herxen-afspraken, instemmingsbrieven |
| **Zwartewaterland** | Omgevingsvisie (in werking 08-10-2026) lezen **J**; Buitengebied 2013-regels **J\***; Catalogus **J** | CPO-beleid, Binnenveld, KGO-besluit 2015 |
| **Apeldoorn** | Omgevingsvisie (in werking 22-12-2025; ringen rond kernen, contour) **J**; omgevingsplan nieuw deel **J**; "Programma voor Gemeente Apeldoorn" **J**; BOPA's Molenstraat/Zwolseweg/Engeland 5 **J** | Wegingsmodel-versies, raadsuitslagen, kavelprijzen |
| **Elburg** | Omgevingsvisie bijlagen 9-10 (kostenverhaal) **J**; omgevingsplan nieuw en tijdelijk deel **J/J\***; definitieve stikstofreductiegebied-tekst en GO bij Doornspijk (**J**, in de verordening) | VAB-beleid, 't Hasenest, kavelprijzen |
| **Epe** | 35 BOPA's (o.a. splitsing woonboerderij, functiewijziging naar wonen) als precedenten **J**; 4 ontwerp-omgevingsplanwijzigingen (o.a. Kopermolen?) **J**; Herstelplan Buitengebied 2020 **J\*** | Omgevingsvisie 2021 (geen DSO-regeling), VAB-evaluatie, CPO-beleid |
| **Ermelo** | Tijdelijk deel / TAM-plannen Garderenseweg 60 / De Beek 77 (GOZ-punten in de toelichting) **J\***; stikstofstrook volgens de definitieve verordening **J**; ontwerp-omgevingsplanwijzigingen **J** | Afwegingskader-collegebesluit, recherche-onderzoek, anterieure overeenkomsten |
| **Harderwijk** | Volkshuisvestelijk omgevingsprogramma (waarschijnlijk in "mens en maatschappij") **J**; Gebiedsprogramma Hierden dorp **J** (Hierden buiten niet aangetroffen); rood-voor-rood in het omgevingsplan **J/J\*** | Beoordelingsregels boerenerven, Bindend Advieslijst, ranglijst net |
| **Hattem** | Chw-plan Buitengebied incl. bijlage 21 (provinciale vooroverlegreactie) en de verwijzing naar het functieveranderingsbeleid **J\*** | Geldersedijk 28, 80-woningenplafond, Programma Wonen |
| **Heerde** | Planregels Buitengebied West/Oost en TAM-plannen **J\*** (plan-ID's 00000800/-900 zonder versie geven 404); stikstofkaart **J** | Notitie Functieverandering 2011 e.a. (archief), themaraad |
| **Nunspeet** | Planregels Buitengebied 2023 art. 44.1.4: **J, al bevestigd** (pagina leesbaar; art. 44.1.4 nog op te zoeken) | Functieveranderingsbeleid 2026-2028 (college), Zwolse Hofje, stikstofbeleidsregel |
| **Oldebroek** | Ontwerp-Omgevingsprogramma Volkshuisvesting **J** (mogelijk ook de 250-woningenreserve); programma's Wezep Oost / Oldebroek Oost / Broeklanden III **J**; Structuurvisie 2017 **J\*** | Zuiderzeestraatweg 342, PVPO, afwegingskader |
| **Voorst** | Ontwerp-Omgevingsvisie integraal **J**; ontwerp-omgevingsplanwijziging (mogelijk sociale koop/huur) **J**; 53 BOPA's (o.a. Rood voor Groen-toepassingen) **J**; tijdelijk deel Buitengebied 2013/2014/2019 en Paraplu Kwaliteitsbepalingen **J\*** | Verlenging Rood voor Groen (collegebesluit), Hessenlaan, Twello-Noord |

**Per locatie (alle gemeenten), L:** zodra er een kandidaatperceel is, geeft `POST /onderwerpen/_zoek` met een RD-punt of -vlak alle geldende regelingen, activiteiten en gebiedsaanwijzingen van gemeente, provincie en Rijk op dat punt. Daarmee zijn overlays, stikstofstrook, GOZ/GNN en de landbouwtypologie exact te bepalen.

## 4. Grenzen van DSO

- Beleidsregels, verordeningen buiten de Omgevingswet, collegebesluiten en raadsuitslagen staan niet in DSO. Die blijven via CVDR, Gemeenteblad en Open Besluitvorming lopen.
- Omgevingsvergunningen in DSO zijn alleen de via DSO gepubliceerde. Dat is geen volledig register; de volledige tekst staat in het Gemeenteblad (publicatieID-link).
- Niet-openbare stukken (Woo-categorie) blijven buiten bereik.

## 5. Wat ik van je nodig heb

1. ~~Ruimtelijke Plannen-key~~: staat in `rp.txt` en werkt (zie §6).
2. Optioneel: een kandidaatlocatie (adres of perceel) voor de **L**-punten.
3. Akkoord op de volgorde. Mijn voorstel:
   1. de Gelderse verordening (raakt 9 rapporten);
   2. de nieuw gevonden programma's en visies (Gelders programma Wonen, VHP Overijssel, Oldebroek, Harderwijk, Zwartewaterland, Hellendoorn, Raalte);
   3. de BOPA-precedenten;
   4. het tijdelijk deel.

## 6. Ruimtelijke Plannen-API: wat de `rp.txt`-key extra ontsluit, en hoe actueel dat is

### 6.1 Status van "ruimtelijkeplannen": deprecated, maar juridisch nog relevant

Bron: *Uitfasering services en diensten Ruimtelijkeplannen.nl en alternatieven vanuit DSO-LV* (Kadaster/RPnl, september 2024), https://www.ruimtelijkeplannen.nl/web-roo/docs/Uitfasering_services_en_diensten_RPnl_en_alternatieven_vanuit-DSO-LV.pdf

**Wat is uitgefaseerd:**
- de WFS/WMS-afnemersservices van ruimtelijkeplannen.nl (per 1-7-2024);
- delen van de viewer, zoals "alle plankaarten tonen".

**Wat blijft:** de **Ruimtelijke Plannen API v4 (Informatiehuis Ruimte)**. Dit is de officiële "overbruggingsfunctie" waarmee DSO (ook "Regels op de kaart") het tijdelijk deel toont. Zolang gemeenten nog een tijdelijk deel hebben, blijft deze API in gebruik. Ik heb geen einddatum voor de API gevonden.

**Overgangsrecht:**
- Wro-plannen die vóór 1-1-2024 in ontwerp waren, en TAM-IMRO-plannen die vóór 1-1-2026 in procedure waren, staan alleen in IHR/RP. Ozon bevat ze niet.
- Gemeenten hebben tot **1-1-2032** om ze om te zetten. Tot dan is het omgevingsplan "hybride": nieuw deel in Ozon, tijdelijk deel in RP.
- Een bestemmingsplan verliest zijn werking pas als het in het nieuwe deel is opgenomen of daar met een **pons** buiten werking is gesteld.

**Actualiteit van de harvest:** volgens de Kadaster-documentatie (Uitleg RP API v4, 2021) staat een plan na publicatie doorgaans binnen enkele minuten in IHR, uiterlijk binnen 24 uur. De meest recente plannen in de inventaris zijn TAM-plannen van 16-07-2026 (Apeldoorn) en 08-07-2026 (Ermelo, Zwolle, Harderwijk). De data lopen dus gewoon mee. Er komen alleen geen nieuwe soorten plannen meer bij.

### 6.2 Is het tijdelijk deel in onze gemeenten nog geldig? (pons-check in Ozon, 2026-11-06)

| Gemeente | Pons in het nieuwe omgevingsplan | Betekenis |
|---|---|---|
| Kampen | 1 gebied (H21 Broekswetering, sinds 01-07-2026) | Alleen daar is het bestemmingsplan vervangen |
| Zwolle | 1 zeer klein gebied (ca. 10×10 m) | Verwaarloosbaar |
| Epe | 4 gebieden (2026), ten westen en noordoosten van Epe/Vaassen | Lokaal vervangen; per locatie controleren |
| Zwartewaterland, Dalfsen, Hardenberg, Ommen, Raalte, Hellendoorn, Olst-Wijhe, Deventer, Hattem, Oldebroek, Nunspeet, Elburg, Harderwijk, Ermelo, Voorst | geen | Het tijdelijk deel (RP) is overal nog het geldende planologische regime voor het buitengebied |
| Apeldoorn, Heerde | niet vastgesteld (Ozon gaf een time-out) | Opnieuw controleren |

**Conclusie:** voor een CPO op agrarische grond is het **RP-tijdelijk deel in alle 20 gemeenten nog het geldende kader**. Het is niet outdated. Uitzondering zijn enkele geponste gebieden in Kampen, Zwolle en Epe. Het nieuwe deel in Ozon bevat vooral bruidsschat, TAM-opvolgers en losse projectregels.

Let op: een geldend bestemmingsplan kan **beleidsmatig** wel verouderd zijn (Oldebroek "Buitengebied 2007", Heerde 2012/2013, Voorst 2013). Dat het juridisch nog geldt, zegt niets over de vraag of de gemeente er nog naar handelt. Dat moet blijken uit beleidsregels en omgevingsvisies.

### 6.3 Inventaris per gemeente (geldende plannen, `regelStatus=geldend`)

Het moederplan buitengebied is het geldende basisplan voor het landelijk gebied. Partiële herzieningen en TAM-plannen komen daar per perceel overheen.

| Gemeente | Geldende plannen | waarvan TAM | Laatste plan | Moederplan(nen) buitengebied (IMRO-id) |
|---|---|---|---|---|
| Kampen | 234 | 1 | 08-04-2026 | `NL.IMRO.0166.00991134-VB01` Buitengebied 2014 |
| Zwolle | 227 | 9 | 08-07-2026 | (geen plan met "buitengebied" in de naam; deelgebiedsplannen, nog te identificeren) |
| Zwartewaterland | 91 | 5 | 04-06-2026 | `NL.IMRO.1896.BP0035-VS01` Buitengebied Zwartewaterland (2013) |
| Dalfsen | 44 | 0 | 20-04-2026 | `NL.IMRO.0148.BgemDalfsen-vs01` Buitengebied Dalfsen (2013) |
| Hardenberg | 601 | 35 | 30-06-2026 | `NL.IMRO.0160.0000BP00165-VG03` Buitengebied Hardenberg (2014); Buitengebied Gramsbergen (2011) |
| Ommen | 205 | 1 | 10-07-2025 | `NL.IMRO.0175.20131003003-va01` Buitengebied rood voor rood (2013); serie `buiten2012bp00xx` herzieningen (moederplan nog te bevestigen) |
| Raalte | 385 | 16 | 14-04-2026 | `NL.IMRO.0177.BP20090046-0003` Buitengebied (2012) |
| Hellendoorn | 200 | 0 | 27-01-2026 | Buitengebied 2009 (moeder-ID nog te bepalen; herzieningen `BPBU…`) |
| Olst-Wijhe | 186 | 0 | 22-04-2024 | `NL.IMRO.1773.BP2009001001-0301` Buitengebied (2012) + 1e/2e herziening |
| Deventer | 196 | 23 | 17-06-2026 | `NL.IMRO.0150.D125-VG02` Buitengebied Deventer (2012) + Combiplannen |
| Hattem | 47 | 1 | 01-06-2026 | `NL.IMRO.0244.bpChwBuitengebied-0003` Chw Buitengebied (2023) |
| Oldebroek | 318 | 0 | 24-12-2024 | `NL.IMRO.0269.BG101-0004` Buitengebied 2007 (2009) |
| Nunspeet | 277 | 12 | 28-05-2026 | Buitengebied 2010/2015/2016/2018 en `NL.IMRO.0302.BP01207-vg04` Buitengebied 2023 |
| Elburg | 135 | 0 | 10-03-2026 | `NL.IMRO.0230.BPBUITENGEB2018-VST1` Buitengebied Elburg 2012, actualisatie 2018 |
| Harderwijk | 259 | 0 | 08-07-2026 | `NL.IMRO.0243.BP00054-0004` Buitengebied 2014 |
| Ermelo | 225 | 13 | 08-07-2026 | (nog te identificeren; TAM-plannen o.a. De Beek 77, Looweg 2) |
| Epe | 150 | 1 | 21-05-2026 | `NL.IMRO.0232.BG028Buitengebied-VBP1` Buitengebied Epe (2017) + herstelplan 2019 |
| Voorst | 309 | 0 | 08-06-2026 | `NL.IMRO.0285.20100-VS00` Buitengebied (2013) |
| Apeldoorn | 588 | 17 | 16-07-2026 | Buitengebied Noord-Oost `bp1044-vas2` (2014), Het Woud `bp1052-vas1` (2013) + herziening 2 (2024) |
| Heerde | 133 | 2 | 30-06-2025 | `NL.IMRO.0246.00000800-va01` Buitengebied West (2012), `…00000900-va01` Buitengebied Oost (2013) |

De correcte IMRO-ID's met versie-achtervoegsel lossen de 404's uit §1 op. Voorbeeld: Heerde `-va01` in plaats van zonder achtervoegsel.

### 6.4 Wat de RP-key concreet extra ontsluit

| Ontsloten informatie | Open punten die daarmee te beantwoorden zijn |
|---|---|
| **Planregels van de moederplannen buitengebied** (`/plannen/{id}/teksten`, `/artikelen/_zoek`): bestemming Agrarisch, wijzigingsbevoegdheden naar wonen, VAB/functieverandering, rood-voor-rood, woningaantal per erf | Zwolle, Kampen (2 vs. 3 woningen), Ommen, Voorst, Heerde, Oldebroek, Zwartewaterland, Nunspeet (art. 44.1.4), Harderwijk (rood-voor-rood), Deventer (D125a), Elburg, Ermelo: alle "regels tijdelijk deel / DSO-regeltekst"-lacunes |
| **TAM-plannen 2024-2026** (159 stuks in deze gemeenten) met toelichting: de feitelijke recente buitengebiedtransformaties onder de Omgevingswet | Precedenten voor functieverandering en woningbouw op erven. Concreet: Ermelo (De Beek 77, Looweg 2, Garderenseweg: GOZ-punten in de toelichting), Hardenberg (Collendoornerdijk 1f-1g, Stobbenhaarweg), Raalte, Deventer (22r/22s/22y), Apeldoorn (22bf Veldhuizen e.a.), Nunspeet, Epe (Ledderweg) |
| **Structuurvisies (IMRO)** | Oldebroek Structuurvisie 2017, Ermelo Structuurvisie Functieverandering, Epe en Heerde structuurvisies, Olst-Wijhe (3) |
| **Omgevingsvergunningen (IMRO-afwijkingen) en projectbesluiten** | Aanvullende precedenten naast de Ozon-vergunningen; Voorst (67), Oldebroek (121), Raalte (109), Hardenberg (89) |
| **Bekendmakingen en gerelateerde plannen** (`/bekendmakingen`, `/gerelateerde-plannen`) | Vaststellingsdata en relaties tussen moederplan en herzieningen; lost datumtegenstrijdigheden op (o.a. Ermelo Zandkampweg 21, Garderenseweg 184) |
| **Bijlagen en toelichting van plannen** (o.a. vooroverlegreacties provincie) | Hattem Chw-plan bijlage 21; Hellendoorn Raamsweg 6/Haarlerveldweg 12; Kampen Zalk Erf 4/5 (reactienota's); Deventer Combiplannen 5-9 |
| **Zoeken op locatie** (`/plannen/_zoek` met `_geo`; planobjecten per punt) | Per kandidaatperceel: welk bestemmingsplan, welke bestemming, bouwvlak, maatvoering en aanduidingen gelden; in combinatie met Ozon-`/onderwerpen/_zoek` het volledige juridische beeld |

### 6.5 Valkuilen voor de Sonnet-runs

- Filter altijd op `regelStatus=geldend`. Paginering loopt via `_links.next`; er is geen `totalElements`.
- Controleer per locatie de **pons** in Ozon (`_expand=true` op het omgevingsplan). Waar een pons ligt, geldt RP niet meer.
- De RP-API waarschuwt dat er "oefencontent" in IHR kan staan. Neem alleen plannen met een herkenbaar vaststellingsbesluit of een bekendmaking op.
- Ozon gaf bij grote verzoeken met `_expand` af en toe een 504. Doe kleinere batches en herhaal bij een fout.
