# Deelonderzoek 1 — Gemeentelijke bestuursinformatie: gemeente Zwartewaterland (Overijssel)

> **Status: afgerond (2026-10-11/12).** Rapport voor het CPO-onderzoek Hanzedorp (cluster 10-12 woningen, collectief particulier opdrachtgeverschap, agrarische grond buiten de kernen).

## Verantwoording
- **Raadplegingsdatum:** 2026-10-11 en 2026-10-12 (alle bronnen live gelezen tenzij anders vermeld).
- **Provinciebestand:** `provincie_overijssel.md` (stand 2026-10-02); Bijlage A van `prompt.md`.
- **Model:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), deelonderzoek 1; effort niet expliciet ingesteld. Eerste run afgebroken door sessielimiet; hervat met hergebruik van `raw/`.
- **Markering:** **[PB]** uit provinciebestand; **[TK]** trainingskennis/niet geverifieerd; **[INT]** interpretatie; **[BER]** eigen berekening; **[WF]** via zoeksamenvatting, lager betrouwbaar; **[OCR]** scan, niet leesbaar gemaakt.
- **Bronnen en toegang:** zwartewaterland.nl (sitemap 673 URL's; relevante pagina's gelezen); RIS = Notubiz (`https://zwartewaterland.raadsinformatie.nl`, organisatie-id 438), via de open API volledig geïndexeerd: 233 vergaderingen 2021-2026, 2.098 agendapunten, 3.106 documenten; 2.421 documenten 2022-2026 gedownload en doorzocht (`raw/notubiz/`). CVDR via SRU (736 records, 665 unieke nummers). 7 documenten niet te downloaden, 88 niet-PDF; enkele scans [OCR] (o.a. brief college 28-5-2024 "Stand van zaken wonen 2024", doc 14310480).
- **Kernen/plaatsen:** Genemuiden, Hasselt, Zwartsluis en Kamperzeedijk (de gemeente noemt in de Omgevingsvisie §4 "Gebieden": Genemuiden, Hasselt, Zwartsluis, Kamperzeedijk, Buitengebied). Buurtschappen/polders: Genne, Holten, Streukel, Zwartewatersklooster, De Velde, Mastenbroek, Barsbeek, Cellemuiden. BAG-woonplaatsen niet apart geverifieerd [TK]. Grafhorst en Kamperveen (genoemd in briefing) komen in de gemeentelijke stukken **niet** als kern voor (Kamperveen ligt in gemeente Kampen) [TK].
- **Woonregio:** West-Overijssel (Woondeal West-Overijssel); verstedelijking Regio Zwolle (NOVEX-gebied). Regio overschrijdt de provinciegrens niet voor wonen.
- **Basisgegevens §1.5 provinciebestand uitgelegd:** 244 = netto gerealiseerd Q1 2022–Q4 2024; 3 / 559 = aantal sleutelprojecten / woningen 2024-2030; 77 = doorkijk 2031-2035 [PB]. Let op: de gemeente rekent zelf met "300 woningen toegevoegd in 2022-2024" (Bouwsteen Wonen 2025, p. 19) — ander definitie/telling; verschil van 56 niet verklaard in de bronnen.

---

## Samenvatting (kernbevindingen)
1. **Bestuur:** coalitie SGP + BGZ (12 van 19 zetels), bestuursakkoord 2026-2030 vastgesteld/besproken 25-6-2026, college geïnstalleerd 25-6-2026. **Geen coalitie in vorming.** Wethouder wonen/ruimtelijke ordening/landbouw/grondzaken: **Maarten Slingerland (SGP)**. Het akkoord is het eerste Zwartewaterlandse coalitiedocument dat CPO noemt: "We geven ruimte aan groepen inwoners die samen betaalbare woningen willen bouwen en beheren, zoals via een Collectief Particulier Opdrachtgeverschap (CPO)."
2. **CPO in de praktijk:** er zijn **twee CPO-kavels in het gemeentelijk project Binnenveld (Genemuiden, 243 woningen totaal)**, één CPO staat "aan de start"; netcongestie en stikstof vertragen. Grondprijzenbrieven (2022 en 2026) noemen CPO expliciet (korting/opslag bij afname groot gebied).
3. **Buitengebied is dicht voor nieuwe erven:** Omgevingsvisie 2026 en Bouwsteen Visie Buitengebied (22-1-2026): "Het ontwikkelen van nieuwe erven in het buitengebied is niet toegestaan." Woningen alleen via herontwikkeling van agrarische bedrijven/bestaande erven, woningsplitsing, extra woning op erf (Beleidsregel 2022; akkoord 2026 wil dit "onder voorwaarden" verruimen). Grootste precedent in de stukken: **2 woningen** (Topweg 1 Genemuiden, Gennerdijk 6 Hasselt), plus "beperkt aantal woningen" rond kerk/school Mastenbroek (positieve grondhouding college).
4. **Eigen KGO-rekenmodel** (Beleidsregel KGO, versie 1.2, 19-1-2015): nieuwe burgerwoning = 20% impactpercentage; impact > 20% = aanvullende kwaliteitsprestatie (percentage x taxatiewinst). Actualisatie aangekondigd.
5. **Planning:** Omgevingsvisie (beleidsluw) door raad 1-10-2026, in werking 8-10-2026 (CVDR767481); tweede herziening met bouwsteen Ontwikkellocaties (voorkeurslocaties wonen/werken eind 2026) en plan-MER naar verwachting voorjaar 2027. Volkshuisvestingsprogramma nog niet vastgesteld.
6. **Praktische drempels:** netcongestie (Enexis-wachtlijst; aanmeldperiode gemeentelijke volgordelijst 1-7 t/m 22-8-2026 verstreken), stikstof/Natura 2000, Nationaal Landschap IJsseldelta, veenweide/weidevogels.

---

## 1. CPO-beleid
- **Bestuursakkoord 2026-2030** (PDF, https://cuatro.sim-cdn.nl/zwartewaterland/uploads/bestuursakkoord-2026-2030.pdf, p. 14; ook https://www.zwartewaterland.nl/bestuursakkoord): "We geven ruimte aan groepen inwoners die samen betaalbare woningen willen bouwen en beheren, zoals via een Collectief Particulier Opdrachtgeverschap (CPO)." Verder p. 13: "We zoeken naar creatieve en nieuwe woonvormen, zoals flexwoningen en tiny houses." **[PB niet nodig; brontekst]**
- **Geen CPO-beleidsregel, geen CPO-kavelbeleid** gevonden: niet in CVDR (665 nummers doorzocht), niet in Bouwsteen Wonen 2025 (0 treffers op CPO/collectief/zelfbouw), niet in Omgevingsvisie 2026. Wel: Omgevingsvisie §3.10.2 "in elke kern ruimte voor de ontwikkeling van bijzondere woonvormen, zoals het wonen in hofjes"; Bouwsteen Wonen p. 32: prijsvraag "vernieuwende woonconcepten voor senioren en starters".
- **Coalitieakkoord 2022-2026** (SGP-CU-PvdA; RIS doc 11472962, 12-5-2022): noemt CPO/collectief niet; wel "Knarrenhof Hasselt" en "Nieuwe erven in het buitengebied zijn niet wenselijk."
- **Woonbehoefteonderzoek KAW (3-7-2024; RIS doc 14802411, p. 85)**: "Meer betaalbare koop toevoegen ... Overweeg ook CPO. Daarmee bouw je (vaak) voor je eigen inwoners en druk je de ontwerp- en ontwikkelkosten." En: "Denk bijvoorbeeld aan boerderijwoningen waar ouderen gezamenlijk in kunnen wonen ... Makelaars geven aan dat een invulling van die vraag het beste bij Hasselt past."
- **Memo starterspakket (9-2-2023; doc 12389386):** "de grondrentesystematiek is wellicht voor (collectief) particulier opdrachtgeverschap een goede optie."
- **Grondprijzenbrief 2026** (https://cuatro.sim-cdn.nl/zwartewaterland/uploads/DEF%20Grondprijzenbrief%202026.pdf, p. 15): "kan het college besluiten een extra korting of opslag te berekenen ... als er sprake is van innovatieve initiatieven waarbij in één keer een grote hoeveelheid grond wordt afgenomen (bijvoorbeeld bij CPO-projecten)". Idem Grondprijzenbrief 2022 (doc 11349115).
- **Wooncoöperaties:** brief college 10-11-2022 (doc 12112333) over landelijk fonds wooncoöperaties, voor kennisgeving aangenomen.
- Hasselt om de Weede 1B (raadsvoorstel 2-6-2022, doc 11508164): "Het plan biedt ruimte voor Collectief Particulier Opdrachtgeverschap." Binnenveld: zie §7.

## 2. Openheid voor nieuwbouw buiten woonkernen
- **Kader:** Omgevingsvisie 2026 §3.10.2: "We geven de voorkeur aan woningbouw op inbreidingslocaties ... boven woningbouw op uitbreidingslocaties wonen. Zo houden we onze kernen compact ... en blijft het buitengebied groen." "We wijzen uitbreidingslocaties aan bij de kernen. ... Het ontwikkelen van nieuwe erven in het buitengebied is niet toegestaan."
- §4.5.3 Buitengebied: "We zoeken naar ruimte voor woningbouw in het buitengebied. We zien vooral mogelijkheden door herontwikkeling van agrarische bedrijven of het toevoegen van woningen op bestaande erven. Woningsplitsing behoort ook tot de mogelijkheden." Ook: "Ruimte voor passende woningbouw voor de eigen behoefte, vooral voor starters en ouderen" en "Realisatie van uitbreidingslocatie wonen Overwaters, een kleinschalige landschappelijke woonlocatie langs de Cellemuiderdijk tussen Hasselt en Genemuiden."
- **Programma** (tabel 1): Genemuiden 265 (programmeren +/-345), Hasselt 290 (380), Zwartsluis 170 (220), Kamperzeedijk 40 (50), Buitengebied "eigen woningvraag"; totaal 775 / 1.010 tot 2030; 2030-2040 nog 610-745.
- **Bestuursakkoord:** "In Hasselt en Genemuiden is genoeg ruimte ... In Zwartsluis en op de Kamperzeedijk zoeken we actief naar nieuwe bouwlocaties." / "inbreiding waar wenselijk vóór uitbreiding."
- **Ladder:** gemeentelijke ruimtelijke onderbouwingen 2024-2026 toetsen nog aan de Ladder (o.a. Topweg 1, Genemuiden: §2.2; "niet meer dan 11 woningen ... niet als stedelijke ontwikkeling", doc 16902261). Volkshuisvestingsprogramma: Bouwsteen Wonen 2025 p. 7: "Met de Bouwsteen Wonen sorteert de gemeente voor op het volkshuisvestingsprogramma ... Zodra ook de Bouwsteen Ontwikkellocaties ... gereed is, stelt de gemeente op basis van beide bouwstenen het volkshuisvestingsprogramma op." Jaarverantwoording 2025 (doc 17066204): programma "dat in de loop van 2026 door de raad kan worden vastgesteld" — **tegenstrijdig** met de volgorde (Ontwikkellocaties eind 2026/voorjaar 2027). Nog geen ontwerp gevonden.
- **Nota Reikwijdte en Detailniveau** (doc 16356294): bouwsteen Ontwikkellocaties zoekt extra ruimte, "in het bijzonder in Zwartsluis"; "De huidige, planologisch vastgelegde ontwikkellocaties bieden onvoldoende ruimte" (voor werklocaties).
- [PB] Overijssel: Zwartewaterland is "overige kern" (art. 4.4): alleen lokale behoefte + bijzondere doelgroepen. Past bij de gemeentelijke formulering "eigen woningvraag" voor het buitengebied.

## 3. Openheid voor agrarische herbestemming
**Wettelijk/procedureel kader (gemeentelijk)**
- Omgevingsplan: tijdelijk deel = bestemmingsplan "Buitengebied Zwartewaterland" (raad 10-10-2013) + Paraplubestemmingsplan Wonen (raad 14-10-2021, arbeidsmigranten) + bruidsschat (CVDR696513). Omgevingsplan fase 1 (beleidsluwe omzetting) voorzien eind 2026 (raadsvoorstel 17421189; presentatie 9-10-2025, doc 16077809). **Het volledige tijdelijk deel en de regels over VAB uit het bestemmingsplan 2013 zijn niet gelezen** (ruimtelijkeplannen.nl-regels niet opvraagbaar; zie §4 "niet gevonden").
- Wijziging omgevingsplan (raad) of BOPA (college, met bindend advies raad). Gemeentewebsite: "Als uw initiatief niet past binnen het omgevingsplan ... buitenplanse omgevingsplan (BOPA) of wijziging omgevingsplan ... evenwichtige toedeling van functies aan locaties ... handreiking" (https://www.zwartewaterland.nl/omgevingsplan; /wilt-u-het-omgevingsplan-wijzigen; templates "kleine BOPA" en "grote BOPA").
- **Adviesrecht raad** (CVDR718739, raad 21-3-2024): voor buitenplanse omgevingsplanactiviteiten wordt de raad geconsulteerd voor **bindend advies**, behalve kruimelgevallen en "ruimtelijke initiatieven" die niet in strijd zijn met een door de raad vastgesteld kader én ≤ 2 woningen ("Het toestaan van meer woningen is mogelijk wanneer het project niet in strijd is met [het raadskader]"). [INT] Een cluster van 10-12 woningen in het buitengebied valt gezien "nieuwe erven niet toegestaan" in de praktijk onder bindend advies of onder raadsbesluit (TAM-omgevingsplan).
- **KGO-beleid** (gemeentelijk rekenmodel, 2015; zie Bijlage A B1) en **Beleidsregel extra woning** (CVDR683809).
- **Provinciaal kader** [PB]: KGO-art., landbouwgebied-typologie, redeneerlijn, woonafspraken (art. 4.14-4.15), Lijst BOPA. De gemeente vermeldt in haar reactie op de provinciale zienswijze (Reactienota Omgevingsvisie, doc 17421192): "het grootste deel van het landelijk gebied ligt binnen het landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur en een relatief klein deel in het gebied met generieke opgaven" **[WF; kaartlaag niet zelf doorgesneden — deelonderzoek 2/4]**.

**Gemeentelijke houding**
- Positief over *herontwikkeling van bestaande agrarische erven* (Omgevingsvisie §3.5.2: "We staan positief tegenover nieuwe functies in vrijkomende agrarische bebouwing en erven."), negatief over *nieuwe erven*. Bestuursakkoord p. 19: "Nieuwe functies op voormalige boerenerven mogen andere bedrijven in de omgeving niet onnodig beperken."
- Bouwsteen Visie Buitengebied, deelgebieden (wonen): Genne-Holten-Streukel "Ja; ... geschikt voor woningen. Er is ruimte voor woningen op bestaande erven"; Dijken, Mastenbroek, Veldiger Binnenlanden, Zwartewatersklooster, Gennegerbroek "Ja mits; het op een bestaand erf is"; De Wieden en Zeekleipolders "Nee tenzij; het op een bestaand erf is ..."; Zwarte Water/Zwarte Meer "Nee". Bijlage 7: "Woningbouw op bestaande erven in het buitengebied is maatwerk. Het gaat om kleinschalige woningbouw passend bij de maat en schaal van het erf."
- Precedenten: zie §6.

**Stappenplan (gemeentelijke praktijk)**
1. Vooroverleg/conceptverzoek (omgevingstafel; leges 2026: indicatie en wenselijkheid € 0; haalbaarheid € 750, art. 2.4 CVDR747704); doorlooptijd ca. 6 weken (raadspresentatie 30-11-2023, doc 13552982).
2. Principeverzoek aan college, ca. 12 weken; bij "bestuurlijk gevoelige ontwikkelingen" betrekt het college de raad (informerend of besluitvormend). Voor agrarische grond voor woningbouw: de gemeente ziet aanbod als "strategische aankoop ... 10+ jaren" (Oostermaat, doc 14160646).
3. Eventueel provinciaal vooroverleg / Regionale Omgevingstafel (Aalvanger-principeverzoek, Jaarverantwoording 2025).
4. Ruimtelijke onderbouwing (ETFAL, KGO-berekening, ervenconsulent, omgevingsgesprek, onderzoeken stikstof/water/netcongestie); ontwerp 6 weken ter inzage; raad (TAM-omgevingsplan) of BOPA met raadsadvies; uitgebreide procedure ca. 35 weken; leges buitenplanse activiteit uitgebreid € 4.152 + toetsing € 273 / € 1.539 (≤ 2 woningen "niet complex") / € 5.130 (overige) + bouwleges.
5. Anterieure overeenkomst (kostenverhaal), netcapaciteit via gemeentelijke volgordelijst (CVDR765999).

**Kansrijk vs. kansarm** [INT op basis van bronnen]
- Kansrijk: bestaand agrarisch erf, bedrijfsbeëindiging zonder opvolger, sloop van ontsierende bebouwing (rood-voor-rood), 1-2 woningen, lokale starters/senioren, streekeigen, "past bij omliggende agrarische bedrijven" (spuitzone 50 m genoemd in Topweg 1), buiten Natura 2000/buitendijks.
- Kansarm: onbebouwde agrarische grond, nieuw erf, cluster > 2 woningen buiten kern, Mastenbroek-polder weidevogelgebied, De Wieden, buitendijks gebied, gebied zonder netcapaciteit, "luxere woningen"-profiel (Overwaters-ervaring 2022).

**Eindoordeel per schaalscenario** [INT]
| Scenario | Beoordeling |
|---|---|
| 1-2 woningen op bestaand erf (sloop/KGO) | haalbaar (precedent Topweg 1, Gennerdijk 6) |
| 3-6 woningen, bestaand erf | onzeker; geen kader/precedent; "maatwerk"; raad beslist; mogelijk via VAB-herziening die de gemeente aankondigt |
| 10-12 woningen op bestaand erf | in huidig beleid niet voorzien; alleen via maatwerk/herziening VAB-beleid; hoog risico |
| 10-12 woningen op onbebouwde agrarische grond buiten kern | **niet toegestaan** ("nieuwe erven niet toegestaan"); alleen via kern/uitbreidingslocatie (Ontwikkellocaties, voorkeurslocaties eind 2026) of gemeentegrond (Overwaters, Binnenveld) |
| 10-12 woningen aansluitend aan kern als uitbreidingslocatie | mogelijk, via bouwsteen Ontwikkellocaties en raadsbesluit; CPO-kavels in Binnenveld als bestaand voorbeeld |
Vervolgstap: vooroverleg met gemeente (info@zwartewaterland.nl, 14 038), team ruimtelijke ontwikkeling/vastgoed; zie §9.

## 4. VAB-beleid
- **Geen aparte VAB-beleidsregel in CVDR.** Wel: Bouwsteen Visie Buitengebied §4.4.3: "We zetten in op het invullen van vrijgekomen agrarische bebouwing (vab) en erftransformatie ... Bij het uitwerken van het vab-beleid verkennen we hoe we dit kunnen borgen in het Omgevingsplan. We evalueren het huidige vab-beleid en passen deze waar nodig aan. Indien mogelijk doen we dit samen en in afstemming met omringende gemeenten." Reactienota (doc 16455457): "We hebben beleid voor extra woningen in het buitengebied ... Hierin is wel expliciet opgenomen dat we geen 'plattelandswoningen' bouwen."
- **Beleidsregel extra woning in het buitengebied** (CVDR683809, college 8-11-2022, geldend 18-11-2022): extra bedrijfswoning op agrarisch bedrijfserf alleen als twee-onder-één-dak met beide huishoudens bedrijfsmatig gebonden; op woonerf: twee woningen in bestaand volume, extra woning in bijgebouw of herontwikkeling volledig erf; "Een nieuwe vrijstaande woning op een bestaand erf toevoegen is niet wenselijk, tenzij ... gebiedspassende ruimtelijke compensatie"; "Het realiseren van een nieuw woonerf is niet toegestaan." Voorwaarden: KGO (ervenconsulent, beplantingsplan), omgevingsgesprek, milieudeskundige onderbouwing.
- **Beleidslijn inhoudsmaat** (CVDR745446, geldend 16-10-2025): 600 m³, afwijking 750; tot 1.200 m³ met sloopmeters (1 m² asbest of 1,5 m² zonder asbest per m³ boven 900) of € 150/m³ landschapsfonds. (De 2026-ruimtelijke onderbouwing Topweg 1 citeert een nieuwere formulering 750/900 m³ — versie in omgevingsplan nog niet geharmoniseerd [INT].)
- **Provinciale regeling 4.39 / Erfcoach:** Erfcoach Noordwest-Overijssel Jan-Olaf Tjabringa (06 27 09 56 40, tjabringa@cultuurland.com) vermeld op https://www.zwartewaterland.nl/erfcoaches; deelname aan intergemeentelijk VAB-programma/4.39 niet gevonden.
- **Bestuursakkoord p. 14:** "maken we het onder voorwaarden mogelijk om een extra woning op het erf of in de tuin te bouwen. Samen met de raad stellen we daarvoor kaders op."

## 5. Grondbeleid
- **Nota Grond- en Vastgoedbeleid 2023** (CVDR702877, raad 19-10-2023; RIS doc 13305428): "We passen actief of faciliterend beleid het meest toe. We sluiten samenwerking niet uit"; kostenverhaal privaatrechtelijk via anterieure overeenkomst; voorkeursrecht ja, onteigening niet; Didam: verkoop kavels particuliere woningbouw mits actueel gepubliceerd op de website zonder verdere publicatie; overige verkoop via selectie. Uitgifte in erfpacht mogelijk; **Grondrente Nieuwe Stijl** (erfpacht als financieringsinstrument, sinds 2017). Nota minimaal eens per vier jaar. Pachtbeleid 2024 (raad 15-2-2024).
- **Grondposities (Jaarverantwoording 2025, doc 17066204, p. 128-133):** exploitaties Binnenveld (einde 2031), Hasselt om de Weede (2032), Zevenhont Oost (2028); strategische grond Binnenveld, Diamanten Bolwerk Hasselt; **Overwaters**: in 2022 teruggekocht van particuliere ontwikkelaar (AM) voor € 3 mln (ca. 11 ha landerijen en erf, raadsvoorstel doc 11818215); taxatie maart 2026 € 1.985.000, afwaardering € 1.015.000; "concrete voortgang ... bemoeilijkt door stikstofproblematiek, netcongestie en ... in/grenzend aan Natura 2000"; "Eind 2025 ... geen concrete ruimtelijke ontwikkeling op korte termijn". Voorontwerp bestemmingsplan (dec. 2021) 17 vrijstaande woningen (2 vervangend) en motie 3-3-2022 (BGZ/CDA/VVD) verworpen; raad vroeg andere varianten [WF voor aantallen uit zoekresultaat; motietekst gelezen: "17 woningen komen, waarvan twee als vervanging"].
- **Kavelaanbod (https://www.zwartewaterland.nl/kavels-hodw, 2026-10-11):** Hasselt om de Weede veld 1: 19 vrijstaande kavels; veld 2: 8 vrijstaand (4 twee-onder-één-kap verkocht) — "31 kavels" in documentatie; optie 8 weken kosteloos (+6 weken); contact vastgoed@zwartewaterland.nl, 14 038 (op de pagina: "Mw. G. van Dalfsen, medewerker Vastgoed"; raadsvoorstel feb. 2026: Jolina Kassanda). Prijzen 2026: vrijstaand EUR 335-345/m² (eerste 500 m²), EUR 250 daarboven; "De Weederanden" EUR 345-375 / EUR 260; 10% opslag bijzondere ligging. Projectmatig "Langs de Weiden" (VanWonen, 42 woningen). Tag West Genemuiden: vrije kavels via Ontwikkel Combinatie Genemuiden (OCG, www.tagwest.nl). Binnenveld: geen kavels beschikbaar; "Voor de vrije kavels en beide CPO's zal een eigen marktstrategie bepaald worden ... in 2026".
- **Productie en plancapaciteit:** Bouwsteen Wonen 2025: 2022-2024 300 woningen toegevoegd, nodig ca. 130/jaar; programma 1.010 (130%). KAW (peil mid-2024, doc 14802411 p. 94): harde plannen 550, zachte 455 tegenover behoefte 775 (675-850): Genemuiden hard 180 / zacht 265 (te veel zacht), Hasselt 265/55 (match), Zwartsluis 50/55 (te weinig, minstens 45 erbij), Kamperzeedijk 0/40 (zacht omzetten). Regionale opgave West-Overijssel [PB]. Ruimte voor derden: Omgevingsvisie "flexibiliteit in het woningbouwprogramma"; niet als aparte reserve vastgelegd [INT].
- **Ontwikkelaar-/derde-initiatieven Kamperzeedijk:** Westererf (Koraal Vastgoed, on hold), Oostermaat (ontwikkelaar + gemeente onderzoek, college 8-10-2025), Selles (autobedrijf).

## 6. Praktijkvoorbeelden (2024-2026)
| Voorbeeld | Datum/bron | Relevantie |
|---|---|---|
| Topweg 1 Genemuiden: ruimte-voor-ruimte, 2 vrijstaande woningen (900 m³), sloop 1.214 m², KGO-impact 2,35% < 20% → basisinspanning | TAM-omgevingsplan H22b, raad 4-6-2026 zonder stemming (doc 16962118; besluitenlijst doc 17178791) | Meest recente toepassing KGO-rekenmodel; schaal 2 woningen |
| Gennerdijk 6 Hasselt: provincie herontwikkelt agrarisch erf voor natuur, sanering opstallen, 2 nieuwbouwwoningen (KGO) | raad 14-11-2024 (doc 14757191) | provinciale rol; "past binnen plancapaciteit" |
| Zwolsedijk 9 Hasselt: functiewijziging agrarisch → wonen, geen nieuwe woningen, buitenplanse afwijking | omgevingsvergunning 22-10-2024 (ruimtelijkeplannen.nl NL.IMRO.1896.OV0046-VS01) | functiewijziging zonder toevoeging |
| Mastenbroek: positieve houding college voor "beperkt aantal woningen rond de kerk en de school", voorwaarden, uitwerking gevraagd | Reactienota Visie Buitengebied (doc 16455457) | enige buitengebied-clusterachtige houding; schaal onbekend |
| Principeverzoek Oostermaat (agrarische gronden aanbieden aan gemeente voor woningbouw) | raadsbijeenkomst 16-5-2024 (doc 14160646); college 8-10-2025 | agrarische grond → woningbouw bij kern; traag, "strategische aankoop 10+ jaar" |
| Aalvanger (Hasselt, voormalige boerderij, Heutink): principeverzoek via regionale omgevingstafel; waterschap: structureel overstromingsgevaar | Jaarverantwoording 2025 | agrarische erf-herontwikkeling afgeschoten/aangepast door water |
| De Molenwaard en Bodewes: principe-medewerking recreatie → wonen, "niet voor ongewenst precedent" | raad 19-2-2026 (doc 16507740) | raad pragmatisch; geen agrarisch |
| Overwaters terugkoop, afwaardering | 2022; jaarrekening 2025 | zie §5 |
| Kamperzeedijk procesaanpak € 76.000 | raad 7-5-2026 (doc 16856604) | initiatieven langs afwegingskader |

## 7. Inventarisatie bestaande initiatieven
- **Binnenveld Genemuiden** (gemeentelijk project, ca. 243 woningen; bestemmingsplan medio 2024 onherroepelijk; o.a. 80 zorgappartementen "BinnenErf", vrije kavels, rug-aan-rug, **2 CPO's**): CPO Innoblox ingekomen stuk raad 22-6-2023 (nr. 16, "In handen stellen van het college", doc 12850579); infoavond 30-10-2023: "Kavel uitgifte CPO"; Jaarverantwoording 2025: "Het initiatief van het CPO staat nog aan de start van hun plannen en ideeën ... Het CPO Binnenveld gaat als pilotproject deelnemen aan het provinciale onderzoek naar mini-warmtenetten" (startgesprek provincie 5-3-2026). Aantal woningen per CPO niet gevonden. Bouw wacht op netaansluiting (Enexis-wachtlijst) en stikstof; voorbelasting gestart half september 2026 (nieuws 29-9-2026).
- Hasselt om de Weede 1B (205 woningen, "ruimte voor CPO"), geen concreet CPO gevonden.
- Knarrenhof Hasselt (genoemd in coalitieakkoord 2022; status niet onderzocht) [TK].

## 8. Huisvestingsverordening
- **Niet aanwezig** (CVDR: alleen "Huisvesting van arbeidsmigranten in de gemeente Zwartewaterland", CVDR668202, beleid o.b.v. Paraplubestemmingsplan, geldend 1-1-2022). Bouwsteen Wonen p. 30: huisvestingsverordening met urgentieregeling "wordt verplicht"; **lokale-bindingsvoorrang (50%) bewust niet opgenomen**: "Hierbij kunnen we ook hoger gaan dan 50 procent [via projectafspraken]". Omgevingsvisie: "nog op te stellen huisvestingsverordening"; bestuursakkoord: "We maken een huisvestingsverordening" (arbeidsmigranten). Raadsinformatieavond 19-9-2024 (doc 14536318). Minimumpercentage sociale huur in verordening: n.v.t.; programmeringsdoel 24% (lange termijn 30%) in Bouwsteen.
- Waar te vinden: raad (RIS), regionale afstemming West-Overijssel/provincie, team Wonen.

## 9. Zelfbouwloket / contactpersoon
- **Geen zelfbouwloket of CPO-aanspreekpunt** gevonden. Dichtstbijzijnde: team Vastgoed (kavels): vastgoed@zwartewaterland.nl, 14 038; Binnenveld: binnenveld@zwartewaterland.nl; Omgevingsvisie: omgevingsvisie@zwartewaterland.nl; netcapaciteit: netcongestie@zwartewaterland.nl; algemeen info@zwartewaterland.nl; Telvorenstraat 2, Hasselt.
- Ambtelijk genoemd in raadsvoorstellen 2026: Henk van Dalfsen (h.vandalfzen@zwartewaterland.nl) en Ivonne Bieleman (i.bieleman@) (ruimtelijke ontwikkeling); Dirk IJzereef (d.ijzereef@); opgaveregisseurs Marcel Exterkate en Ine Margriet Westhoff; Remco Kok (presentaties omgevingsplan/vergunningverlening). Functietitels niet vastgesteld.
- Erfcoach: zie §4.

## 10. Bestuurlijk klimaat
- **Verkiezingen 18-3-2026 (CSB-proces-verbaal):** SGP 3.745 stemmen/6 zetels; BGZ 3.253/6; ChristenUnie 2.601/4; CDA 1.065/1; PvdA 900/1 (sinds 1-10-2026 fractie "PRO Zwartewaterland"); VVD 832/1 = 19 zetels. Coalitie SGP+BGZ = 12 zetels; ChristenUnie (coalitiepartij 2022-2026 met SGP en PvdA) nu oppositie.
- **Formatie:** fractievoorzitters stelden informateur A. de Kruijf aan; verslag 23-4-2026; motie 2026-02 opdracht formatie (SGP/BGZ); gespreksleider/formateur Gert Wiegers; start 6-5-2026, acht gesprekken; akkoord 11-6/19-6-2026; benoeming wethouders 25-6-2026. **Geen coalitie in vorming, geen tussentijdse val.** Wijzigingen raad: S. Hartman ontslag, M. Van der Voort toegelaten 1-10-2026 (partij niet gevonden).
- **College:** burgemeester Judith Compagner; wethouders Maarten Slingerland (SGP; 1e loco; kernwethouder Genemuiden en buitengebied; **Economie; Wonen, landbouw, ruimtelijke ordening (incl. stikstof); Vergunningverlening; Grondzaken (grex+pacht) en vastgoed; Financiën**; thema's Wonen, Omgevingsvisie), Alijn Muijsers-Lok (BGZ; sociaal domein, cultuur, recreatie), Benjamin van Marle (SGP/BGZ; water, energie/netcongestie, monumenten, mobiliteit, handhaving). Vorig college: H. Rietman (PvdA, ruimtelijke ordening/projecten) en J. van der Poel (CU, wonen/volkshuisvesting). Bron: https://www.zwartewaterland.nl/maarten-slingerland e.a., geraadpleegd 2026-10-11.
- **Bestuursakkoord** (relevant): zie §1-§3; "Raadsbrede agenda" met alle fracties; "Voor het duurzaam opwekken van energie gebruiken we liever geen landbouw- of natuurgronden."; "Nieuwe woningbouw moet passen bij het karakter ... van de kernen"; "Grote bebouwing die niet past bij het dorpse karakter willen we voorkomen."
- **Indicatie ruimte CPO:** coalitie-expliciet positief over CPO en extra woning op erf; tegelijk behoud agrarisch/"nieuwe erven niet toegestaan" en confessioneel-conservatief profiel (zondagsrust); gemeenteraad heeft in 2022 en 2026 (Willem Egbertsstraat) gevoelige inbreiding teruggedraaid en Overwaters afgeremd. [INT] Ruimte voor CPO bij/in kernen op gemeentegrond; weinig voor nieuwbouw in open buitengebied.

## 11. Kostenverhaal en leges
- **Kostenverhaal:** Nota Grond- en Vastgoedbeleid 2023: verplicht kostenverhaal bij particuliere (integrale) initiatieven privaatrechtelijk (anterieure overeenkomst); publiekrechtelijk alleen als sluitend; "financiële bijdrage voor ontwikkelingen ter verbetering van de kwaliteit van de fysieke leefomgeving ... wordt wel als een bruikbaar instrument beschouwd". Exploitatieplan bij kleine initiatieven: geen (raadsvoorstellen: "voor te stellen geen exploitatieplan vast te stellen"). Aparte nota kostenverhaal/planschaderegeling onder de Omgevingswet niet gevonden.
- **Leges 2026 (CVDR747704, raad 13-11-2025):** conceptverzoek haalbaarheid € 750; beoordeling afwijking omgevingsplan: € 963 (binnenplans) / € 273 (Bijlage II eenvoudig) / € 1.539 (Bijlage III: o.a. "maximaal twee woningen") / € 5.130 (overig, tijdelijk deel); uitgebreide procedure buitenplanse activiteit € 4.152; bouwleges oplopend tot 3,34% van bouwkosten boven € 500.000; advies gemeenteraad € 0. Leges 2025: principeverzoek met collegebesluit € 971 (doc 14689058).
- Tarief voor "wijziging omgevingsplan op verzoek" niet apart gevonden → via anterieure overeenkomst/onderzoekskosten.

## 12. Woningbehoefte en doelgroepen
- KAW 2024: behoefte t/m 2030 775 (675-850), 2030-2040 600-750; inwoners 23.368 (2023), 8.929 huishoudens; autonome groei; vergrijzing; Genemuiden jong, Hasselt/Zwartsluis oudere kernen.
- Programma: 30% sociale huur (24% nu), 5% middenhuur, 15% goedkope koop (< € 328.000), 20% middeldure koop (€ 328.000-405.000; 2026 landelijke grens € 420.000), 30% vrij; woningen vooral < 80 m² voor starters en senioren; 140 nultreden, 140 geclusterd, 40 zorggeschikt tot 2030.
- Kamperzeedijk: 35-45 woningen; vooral levensloopbestendig/grondgebonden betaalbaar en middelduur; "Appartementen passen niet bij de schaal van dit dorp".
- **Aansluiting CPO:** CPO-cluster van 10-12 woningen sluit aan bij betaalbare koop voor starters/senioren, geclusterd en hofjes/boerderijwonen (KAW); sluit niet aan bij locatie "buitengebied" (behoefte per kern; buitengebied = eigen woningvraag).

---

## Bijlage A-controlepunten
| # | Bevinding | Status | Bron | Waar te vinden |
|---|---|---|---|---|
| A1 | "Overige kern" (art. 4.4 [PB]); NOVEX-gebied Regio Zwolle; geen bijzonder groeiprofiel voor een kern gevonden; Hasselt/Zwartsluis genoemd als zoekruimte | gevonden (deels) | Omgevingsvisie 2026; Reactienota (doc 17421192); [PB] | Regio Zwolle verstedelijkingsstrategie (RIS brief 29-11-2022) |
| A2 | West-Overijssel; Woondeal 2025-2030 actualisatie ingekomen 15-4-2025; realisatie 244 (Woondeal) vs 300 (gemeente); plancapaciteit hard 550/zacht 455 (mid-2024), 130%-programmering 1.010; CPO-telling in programmering niet gevonden; Planmonitor-opname niet gecontroleerd | gevonden/deels | Bouwsteen Wonen 2025; KAW 2024 | Provinciale Planmonitor/Dashboard Wonen; Domiportal (gemeente) |
| A3 | 30-40-30 op programmaniveau, "niet per project"; 24% sociale huur; goedkope koop < € 328.000; lokale grens gekoppeld aan startersleningplafond; prestatieafspraken met Wetland Wonen (opgave 230 sociale huur + 200 2030-2040); CPO-specifiek niet geregeld | gevonden | Bouwsteen Wonen p. 23-24; themabijeenkomst 29-1-2026 | Prestatieafspraken (gemeente/Wetland Wonen) |
| A4 | Geen (ontwerp-)VHP; opstelling na Bouwsteen Ontwikkellocaties; ladder nog in gebruik | gevonden (negatief) | Bouwsteen Wonen p. 7, 20; Jaarverantwoording 2025 | RIS 2026-2027 |
| A5 | 140/140/40; woonzorgvisie West-Overijssel (2024-2026), lokale woonzorgvisie in voorbereiding | gevonden | Bouwsteen Wonen p. 26 | Lokale woonzorgparagraaf in VHP |
| B1 | Eigen KGO-beleid "Beleidsregel KGO" v1.2, 19-1-2015 (geen CVDR-nummer); formule: impact% = f(bebouwing: 0,02%/m² eerste 500 m², 0,015% 500-1.500, 0,010% >1.500; factoren 0,7/1/1,3; erf 0,004%/m² ± parameters; zichtlocatie x2; buitenopslag 0,015%/m²; woning +20% burger/10% bedrijf); > 20% = aanvullende prestatie = % x taxatiewinst | gevonden | https://cuatro.sim-cdn.nl/zwartewaterland/uploads/kgo-beleid-zwartewaterland.pdf | gemeentelijk beleid-pagina; CVDR-registratie ontbreekt |
| B2 | Geen maximumaantal expliciet; precedenten 1-2 woningen; nieuwe erven niet toegestaan; model 0-100% | gevonden (impliciet) | CVDR683809; Topweg 1 | Visie Buitengebied vervolg/VAB-herziening |
| B3 | KGO 2015 "actualiseren" aangekondigd; omgevingsplan nog niet aangepast; verwijst nog naar Omgevingsvisie Overijssel/verordening | gevonden | Visie Buitengebied §4.1.3 | Tweede herziening Omgevingsvisie begin 2027 |
| B4 | Kernen: uitbreidingslocaties bij kernen; buitengebied: erftransformatie; Overwaters als "uitbreidingslocatie wonen" in buitengebied; komgrenzenbesluit jan. 2025 (stukken niet gelezen) | gevonden/deels | Omgevingsvisie §3.10.2, §4.5.3 | Komgrenzenbesluit (RIS 23-1-2025) |
| B5 | Sloop (1:1,5 m²), landschapsfonds € 150/m³, ervenconsulent, beplantingsplan, anterieure overeenkomst | gevonden | CVDR683809/745446 | — |
| C1 | Gemeente: groot deel gebiedsspecifiek, klein deel generiek (provinciale zienswijze) | gevonden [WF] | Reactienota doc 17421192 | Provinciale verordening-viewer (deelonderzoek 2/4) |
| C2 | Geen gebiedsvisie art. 4.124 lid 4 gevonden; Visie Buitengebied is gebiedsgericht | niet gevonden | — | Tweede herziening Omgevingsvisie |
| C3 | Nationaal Landschap IJsseldelta, Natura 2000 (De Wieden, Olde Maten, Zwarte Meer), weidevogelleefgebied, veenweide, buitendijks/waterkeringen, NNN | gevonden | Visie Buitengebied; Omgevingsvisie §4.5.2 | WFS provincie |
| C4 | Geen standaard redeneerlijn-onderbouwing; ruimtelijke onderbouwingen toetsen aan Omgevingsverordening (§2.4 Topweg 1); netcongestie: beleidsregels CVDR765999 (1-7/22-8-2026), Enexis-wachtlijst Binnenveld | gevonden/deels | Topweg 1; CVDR765999 | netcongestie@zwartewaterland.nl |
| D1 | Deelname VAB-/erftransformatieprogramma of 4.39: niet gevonden | niet gevonden | — | Provincie subsidieregister; RIS |
| D2 | Erfcoach J.-O. Tjabringa actief | gevonden | /erfcoaches | erfcoachoverijssel.nl |
| D3 | Beleid verspreid (Beleidsregel 2022, Visie Buitengebied, bestemmingsplan 2013); VAB als opgave in Bouwsteen Wonen (p. 22: "vrijgekomen agrarische bebouwing" in woningbouwopgave) | gevonden | zie §4 | Regels bestemmingsplan Buitengebied (ruimtelijkeplannen.nl) |
| E1 | Regionale Omgevingstafel gebruikt; namen accounthouder niet openbaar | gevonden/deels | Jaarverantwoording 2025; Zomernota 2022 | provincie |
| E2 | Raad voor wijziging omgevingsplan; BOPA met bindend advies raad; termijnen 6/12/35 weken | gevonden | doc 13552982; CVDR718739 | — |
| E3 | Gemeentelijk: ≤ 2 woningen eenvoudig; > 2 raadskader; ladder: ≤ 11 woningen geen stedelijke ontwikkeling | gevonden | CVDR747704 Bijlage III | Provinciale Uitzonderingenlijst [PB] |
| E4 | Alleen zienswijze provincie op Omgevingsvisie (weidevogels e.d.); geen zienswijzen/instemming-onthouding op woning-BOPA gevonden | niet gevonden | doc 17421192 | Provinciaal blad (deelonderzoek 4) |
| F1 | Bouwsteen: Aanjaagteam, flexpool en subsidies "waar nodig"; CPO Binnenveld in provinciaal mini-warmtenet-onderzoek | gevonden/deels | Bouwsteen Wonen; Jaarverantwoording 2025 | provincie Overijssel wonen |

## Geverifieerde CVDR-nummers
Organisatie = SRU-creator "Zwartewaterland" (gemeente); tekst/kop gelezen waar vermeld.
| Nummer | Organisatie | Titel | Geldig |
|---|---|---|---|
| CVDR767481 | Zwartewaterland (raad) | Omgevingsvisie gemeente Zwartewaterland (Gmb-2026-466871) | vanaf 8-10-2026 |
| CVDR696513 | Zwartewaterland | Omgevingsplan gemeente Zwartewaterland (bruidsschat; versie 21-7-2026) | geldend |
| CVDR683809 | Zwartewaterland (college) | Beleidsregel extra woning in het buitengebied | vanaf 18-11-2022 |
| CVDR745446 | Zwartewaterland | Beleidslijn afwijken inhoudsmaat woning buitengebied | vanaf 16-10-2025 |
| CVDR702877 | Zwartewaterland | Nota Grond- en Vastgoedbeleid 2023 | geldend |
| CVDR747704 | Zwartewaterland | Legesverordening 2026 | 2026 |
| CVDR718739 | Zwartewaterland | Adviesrecht Omgevingswet (raad 21-3-2024) | vanaf 26-4-2024 |
| CVDR765999 | Zwartewaterland (college) | Beleidsregels eerder aanvragen transportcapaciteit woningbouwprojecten 2026 | vanaf 25-8-2026 |
| CVDR738380 | Zwartewaterland | Beleidsregel woningsplitsing | vanaf 8-4-2025 |
| CVDR668202 | Zwartewaterland | Huisvesting arbeidsmigranten | vanaf 1-1-2022 |
| CVDR481054 | Zwartewaterland | Nota Grondbeleid 2017-2021 | vervallen |
| CVDR708882, 713328, 714056, 708613 | **niet gemeentelijk** (akn: provincie/ministerie) | Voorbereidings-/voorbeschermingsbesluiten in omgevingsplan | niet als gemeentelijk beleid gebruikt |
**Niet in CVDR gevonden:** KGO-beleid 2015, Bouwsteen Wonen, Bouwsteen Visie Buitengebied, Grondprijzenbrief 2026, bestuursakkoord.

## Onzekerheden/tegenstrijdigheden
1. Realisatie 244 (Woondeal, Q1 2022-Q4 2024 netto) vs 300 (Bouwsteen, 2022-2024).
2. Volkshuisvestingsprogramma "in de loop van 2026" (Jaarverantwoording) vs na Bouwsteen Ontwikkellocaties (Bouwsteen Wonen; voorjaar 2027).
3. Omgevingsvisie §4.5.3 "Realisatie ... Overwaters" vs jaarrekening: geen ontwikkeling op korte termijn, afgewaardeerd.
4. Inhoudsmaat: CVDR745446 (600/750/1.200) vs samenvatting in Topweg 1 (750/900); beleidslijn mogelijk herzien.
5. Gemeentelijke Visie Buitengebied "vastgesteld 22-1-2026" maar nog niet in Omgevingsvisie (pas tweede herziening).
6. Contactpersoon Vastgoed (website vs RIS).
7. Niet gelezen/gedownload: regels bestemmingsplan Buitengebied 2013 (VAB-regels), brief 28-5-2024 [OCR], komgrenzenbesluit, prestatieafspraken, Binnenveld-CPO details (aantal woningen).
8. Zoekresultaten-gebaseerde punten [WF]: Overwaters 76 ha en aantal woningen, Binnenveld 165/78.

## Twee kernvragen
**1. Wonen in het buitengebied (cluster 10-12 woningen buiten de kernen)**
(a) Gemeente: nee voor nieuwe locaties/erven ("niet toegestaan"); alleen kleinschalig op bestaande erven; clusters via kernen/uitbreidingslocaties; coalitie wil CPO en extra woning op erf mogelijk maken.
(b) Provincie [PB]: concentratiebeginsel (overige kern), woonafspraken West-Overijssel, KGO/typologie (grotendeels gebiedsspecifiek), Natura 2000/IJsseldelta.
(c) Eindoordeel: **niet haalbaar** als zelfstandig cluster in open buitengebied; **mogelijk** als CPO-kavel op/bij gemeentegrond in een kern (Binnenveld) of uitbreidingslocatie na bouwsteen Ontwikkellocaties (voorkeurslocaties eind 2026). Onzekerheden: netcongestie, stikstof, bouwsteen uitkomst.

**2. Agrarische herbestemming op deze schaal**
(a) Gemeente: functiewijziging van bestaande agrarische erven en rood-voor-rood (1-2 woningen, KGO-model) ja; omzetting onbebouwde agrarische grond naar woningbouw buiten kern: alleen als uitbreidingslocatie bij kern, op initiatief/regie gemeente (Oostermaat-route, 10+ jaar).
(b) Provincie: BOPA-instemming/KGO, ladder/redeneerlijn, woonafspraken, landbouwgebied-typologie.
(c) Eindoordeel: **laag** voor 10-12 woningen op agrarische grond; **middel** als kleiner schaalscenario of via kern. Concrete vervolgstap: vooroverleg met team ruimtelijke ontwikkeling/vastgoed (info@zwartewaterland.nl, 14 038), en Erfcoach voor bestaand erf.
