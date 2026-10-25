# Deelonderzoek 3 — Nieuws en actualiteit 2024-2026: gemeente Zwartewaterland (provincie Overijssel)

> **Status: rapport compleet (2026-10-11).** Alle 12 onderwerpen en alle Bijlage A-punten zijn afgewerkt vanuit het brontype "nieuws en actualiteit"; waar het nieuws naar brondocumenten verwijst (bestuursakkoord, Bouwsteen Visie Buitengebied, Omgevingsvisie, CVDR-regelingen, Raad van State) zijn die zelf gelezen en letterlijk geciteerd. Ruwe extracties staan in `raw/n3/`.

## Verantwoording
- **Raadplegingsdatum:** 2026-10-11 (bronnen met eigen datum waar die afwijkt).
- **Provincie en gebruikt provinciebestand:** Overijssel, `provincie_overijssel.md` (stand 2026-10-02); het Overijsselse regime is leidend. Bijlage A is van toepassing, Bijlage B (Gelderland) niet.
- **Model:** Claude Sonnet 5.5 (`claude-sonnet-5-5`), deelonderzoek 3 (nieuws en actualiteit); effort niet expliciet ingesteld.
- **Betrouwbaarheidsmarkering:** citaten zijn letterlijk uit de brontekst. **[PB]** = uit `provincie_overijssel.md`; **[TK]** = trainingskennis, niet live geverifieerd; **[INT]** = interpretatie van de samensteller; **[BER]** = eigen berekening; **[WF]** = via samenvatting/zoekresultaat gelezen, lager betrouwbaar; **[OCR]** = scan; **[ADV]** = advertorial/ingezonden mededeling (geen redactionele bron).
- **Bronnen en toegang:**
  - Gemeentelijke nieuwssite https://www.zwartewaterland.nl/gemeentenieuws (SIMsite/Drupal; bereikbaar met browser-user-agent; de lijst loopt terug tot 24-9-2025; oudere berichten staan in het webarchief https://zwartewaterland.archiefweb.eu, niet doorzocht).
  - Lokale nieuwssites van één uitgever met overlappende inhoud: **Genemuiden Actueel** (genemuidenactueel.nl), **Hasselt Actueel** (hasseltactueel.nl), **Zwartsluis Actueel** (zwartsluisactueel.nl). Via de WordPress REST API zijn alle berichten van 1-1-2024 t/m 10-10-2026 uitgelezen (7.900 unieke artikelen na ontdubbeling op titel; 2024: 2.638, 2025: 2.998, 2026: 2.264) en lokaal doorzocht. Daarnaast **Zwartewaterkrant.nl** (alleen gericht gelezen), **RTV Oost** (oost.nl) en **1Zwolle** (alleen via zoekresultaten gevonden en gericht gelezen).
  - Niet toegankelijk of niet doorzocht: De Stentor (betaalmuur; WebSearch-domeinfilter weigerde het domein), Dichtbij (HTTP 403), Zwolse Courant. De plaatselijke omroep is niet vastgesteld (1Zwolle bericht alleen over de omroep van Zwolle).
  - Raad van State: zoekfunctie raadvanstate.nl (`zoeken_term=Zwartewaterland`, 75 treffers, alle gelezen op datum); rechtspraak.nl (rechtbank Overijssel) was niet doorzoekbaar (zoek-API gaf een mededelingenpagina), dus rechtbankuitspraken zijn alleen via nieuws gevonden.
- **Naam- en plaatscontrole:** Zwartewaterland ≠ Zwolle/Kampen/Steenwijkerland/Staphorst. De Actueel-sites berichten ook over Steenwijkerland, Staphorst en Kampen (IJsselmuiden); die berichten zijn uitgesloten (bijv. "IJsselmuiden krijgt er 75 woningen bij" = Kampen; "Vollenhove ... zelfbouw" = Steenwijkerland; "Staphorster jeugd mag wonen op erf van familie" = Staphorst; "LTO Steenwijkerland ... spandoeken" gaat over de bufferzone Weerribben-Wieden, vermeld alleen als context). Raad van State-zaak 202205503/1/R3 (Zwolle) is een valse treffer (burgemeester van Zwartewaterland wordt slechts als eigenaar genoemd) en uitgesloten. **Kamperzeedijk** is een kern/linthoofdplaats in Zwartewaterland en niet te verwarren met Kampen.
- **Kernen en deelgebieden (Omgevingsvisie, CVDR767481 §2.1):** "Zwartewaterland is in vijf deelgebieden verdeeld: de kernen Genemuiden, Hasselt, Zwartsluis, Kamperzeedijk en het Buitengebied." In het buitengebied: onder meer Mastenbroek, Genne, Holten, Streukel, De Velde, Zwartewatersklooster, Cellemuiden. (Grafhorst en Kamperveen — in de briefing met een vraagteken genoemd — liggen niet in Zwartewaterland: Grafhorst en Kamperveen zijn kernen van de gemeente Kampen **[TK]**; niet via BAG/PDOK geverifieerd in dit deelonderzoek.)

## Samenvatting (belangrijkste bevindingen)
1. **Politiek is rond; er is géén coalitie in vorming.** Gemeenteraadsverkiezingen 18-3-2026: SGP 6, BGZ 6, ChristenUnie 4, CDA 1, PvdA 1, VVD 1 (19 zetels). Informateur Aart de Kruijf adviseerde 23-4-2026 SGP + BGZ (12 van 19 zetels); formateur Gert Wiegers (6 mei, acht gesprekken); bestuursakkoord "Wij werken samen, aan, met, voor Zwartewaterland" gepresenteerd 19-6-2026; college (Slingerland SGP, Muijsers-Lok BGZ, Van Marle SGP/BGZ) geïnstalleerd 25-6-2026. De ChristenUnie (coalitiepartner 2022-2026, met SGP en PvdA) is uit het college gezet en is oppositie; CDA, PvdA en VVD hebben elk 1 zetel.
2. **Wethouder Wonen = Maarten Slingerland (SGP)**, portefeuille "Wonen, landbouw, ruimtelijke ordening (inclusief stikstof)", ook economie, vergunningverlening, grondzaken (grex + pacht) en vastgoed, financiën; kernwethouder Genemuiden én buitengebied; lid bestuurlijk overleg Wonen West-Overijssel. Eén bestuurder heeft dus wonen, buitengebied, grond en stikstof in handen. Netcongestie/energietransitie ligt bij Van Marle.
3. **Het bestuursakkoord noemt CPO expliciet** (p. 14): "We geven ruimte aan groepen inwoners die samen betaalbare woningen willen bouwen en beheren, zoals via een Collectief Particulier Opdrachtgeverschap (CPO)." Ook: tiny houses/flexwoningen, "onder voorwaarden ... een extra woning op het erf of in de tuin", pilot doorstroming. Het is een intentie zonder uitwerking; in 7.900 lokale nieuwsartikelen 2024-2026 komt "CPO" niet één keer voor (buiten het akkoord zelf).
4. **Het gemeentelijk kader voor het buitengebied is streng en erfgebonden**: in de net vastgestelde Omgevingsvisie (raad 1-10-2026; in werking 8-10-2026; CVDR767481) staat tweemaal letterlijk "Het ontwikkelen van nieuwe erven in het buitengebied is niet toegestaan"; de Bouwsteen Visie Buitengebied (22-1-2026) noemt woningbouw op bestaande erven "maatwerk ... kleinschalige woningbouw passend bij de maat en schaal van het erf". Een cluster van 10-12 woningen op onbebouwde agrarische grond buiten de kernen past niet in dit kader; mogelijkheden liggen bij herontwikkeling van een agrarisch erf, aansluitend aan een kern (uitbreidingslocatie) of in Kamperzeedijk/Zwartsluis, waar actief naar locaties wordt gezocht.
5. **Praktijkvoorbeelden van de laatste twee jaar laten gemeentelijke regie zien, geen particulier collectief in het buitengebied**: Binnenveld Genemuiden (243 woningen, gemeentelijke grex, 18 vrije kavels, wacht op netaansluiting), Om de Weede (Hasselt), Malcorpshof, Aalvanger (18), Kamperzeedijk (Oostermaat/Westererf/Selles, 40 woningen, 2029-2030), Landgoed Stroombeek + Barsbeek (positief principebesluit 2-6-2026), De Molenwaard/Bodewes (recreatie → wonen, "uitzonderlijke situatie"). Het enige bestaande collectief initiatief is Knarrenhof De Tijlshof (Hasselt, 16 koopwoningen, opgeleverd 2022; initiatief uit 2013).
6. **Netcongestie is de dominante praktische rem**: Binnenveld staat op de Enexis-wachtlijst zonder aansluitdatum; sinds 1-7-2026 komen alle nieuwe aanvragen op een wachtlijst; de gemeente hanteert een volgordelijst "eerder aanvragen" (CVDR765999, in werking 25-8-2026; 44 projecten, ca. 1.007 woningen **[BER]**). Particuliere initiatiefnemers moesten zich vóór 1/22 augustus 2026 aanmelden en 20% van de aanlegkosten vooraf betalen.
7. **Geen provinciale zienswijzen of conflicten over woningbouw in het buitengebied gevonden** (2023-2026). Wel provinciale spanning over windturbines in polder Mastenbroek (zienswijze raad 7-3-2024). Raad van State-uitspraken 2024-2026 over Zwartewaterland betreffen Bodewes/Molenwaard (ongegrond, 14-2-2024), begraafplaats Hasselt, premixenfabriek en een bedrijfswoning-omzetting in Genemuiden (vernietigd maar in stand gelaten, 18-3-2026); geen enkele over CPO of woningbouw op agrarische grond.
8. **Tegenstrijdigheden/opvallend**: (a) het akkoord is positief over CPO, de Omgevingsvisie en Bouwsteen buitengebied zijn restrictief over nieuwe erven; (b) aanmeldtermijn netcongestielijst 1 augustus (nieuws) versus 22 augustus 2026 (CVDR765999); (c) "uitzonderlijke situatie" Molenwaard: gemeente benadrukt dat dit geen precedent is.

---

## 1. CPO-beleid

**Bevinding (nieuws + bestuursakkoord): CPO staat in het bestuursakkoord 2026-2030 als intentie, maar er is geen CPO-beleid, geen CPO-kavelreservering en geen lokaal CPO-project in het nieuws.**

- **Bestuursakkoord 2026-2030** (SGP + BGZ), "Programma 3. Wonen, werken en recreëren", §3.1 Wonen, p. 13-14. Bron: https://cuatro.sim-cdn.nl/zwartewaterland/uploads/bestuursakkoord-2026-2030.pdf (gelezen 2026-10-11; ook via https://www.zwartewaterland.nl/bestuursakkoord). Letterlijk:
  - p. 13: "De woonvraag verandert. Daarom zoeken we naar creatieve en nieuwe woonvormen, zoals flexwoningen en tiny houses. We willen dat woningen beter aansluiten bij de mensen die ze nodig hebben. Ook willen we dat mensen makkelijker kunnen doorstromen naar een woning die beter bij hen past. We starten hiervoor een pilot en stellen daar geld voor beschikbaar."
  - p. 14: "We willen voorkomen dat jongeren onze gemeente verlaten omdat er geen woonruimte is. Daarom maken we het onder voorwaarden mogelijk om een extra woning op het erf of in de tuin te bouwen. Samen met de raad stellen we daarvoor kaders op."
  - p. 14: "We geven ruimte aan groepen inwoners die samen betaalbare woningen willen bouwen en beheren, zoals via een Collectief Particulier Opdrachtgeverschap (CPO)."
  - p. 14: "We willen dat inwoners in onze gemeente kunnen blijven wonen. Samen met de raad kijken we welke instrumenten we hiervoor in kunnen zetten."
  - p. 4: "De meeste afspraken zijn beschreven als doelen. Hoe we deze doelen uitvoeren, werken we de komende periode verder uit."
- **Duiding [INT]:** de zin over CPO is een open uitnodiging ("geven ruimte aan groepen inwoners"), gekoppeld aan *betaalbare* woningen en *beheer* (collectief). Er staat geen locatie, aantal, kavelreservering, budget of verwijzing naar een beleidsregel. Het woord "zoeken" komt volgens Genemuiden Actueel 24 keer voor, 20-6-2026) en kenmerkt het hele akkoord.
- **Negatief bevinding (7.900 artikelen 1-1-2024 t/m 10-10-2026 op Genemuiden/Hasselt/Zwartsluis Actueel):** geen treffer op `CPO`, "collectief particulier opdrachtgeverschap", "particulier opdrachtgever(schap)"; "zelfbouw" alleen in berichten over Kampen (IJsselmuiden) en Steenwijkerland (Vollenhove) — niet Zwartewaterland. "Tiny house" komt uitsluitend voor in de schoolwedstrijd Tiny House Challenge (CWT) en in B&B-teksten, niet in beleid.
- **Waar het wel te vinden zou zijn:** Bouwsteen Wonen (2022; "In het najaar [2024] wordt de Bouwsteen Wonen aangepast", Genemuiden Actueel 18-7-2024; de aangepaste versie is niet gevonden), de aangekondigde Woonzorgvisie 2026 (Genemuiden Actueel 7-11-2025), het nog niet vastgestelde gemeentelijke volkshuisvestingsprogramma en de raadsbrede agenda 2026 (Gemeenteraad, griffie@zwartewaterland.nl). Deelonderzoek 1 (bestuursinformatie) is hier primair.
- **Omgevingsvisie (vastgesteld 1-10-2026; CVDR767481):** noemt geen CPO; wel "We bieden in elke kern ruimte voor de ontwikkeling van bijzondere woonvormen, zoals het wonen in hofjes" (§3.10.2) en "Als gemeente geven we ruimte aan inwoners om zelf initiatief te nemen." (§1.1), en bij Binnenveld "specifieke ontwikkelingen zoals vrijstaande kavels of appartementen" (§4.1). Bron: https://lokaleregelgeving.overheid.nl/CVDR767481 (gelezen 2026-10-11).
- **Bestaand collectief precedent (buiten 2024-2026, wel relevant):** Knarrenhof De Tijlshof, Hasselt, zie §7.

## 2. Openheid voor nieuwbouw buiten woonkernen

**Bevinding: voorkeur voor inbreiding; uitbreidingslocaties alleen aansluitend aan de kernen; "nieuwe erven" in het buitengebied zijn niet toegestaan; wel actief zoeken in Zwartsluis en op de Kamperzeedijk.**

- **Omgevingsvisie Zwartewaterland** (raad 1-10-2026; Omgevingsvisie geldend vanaf 8-10-2026 volgens CVDR767481; persbericht https://www.zwartewaterland.nl/gemeenteraad-stelt-omgevingsvisie-zwartewaterland-vast, 5-10-2026). §3.10.2, letterlijk:
  - "Woningbouw zoveel mogelijk binnen bestaand bebouwd gebied: We geven de voorkeur aan woningbouw op inbreidingslocaties wonen, dus binnen het bestaand bebouwde gebied, boven woningbouw op uitbreidingslocaties wonen. Zo houden we onze kernen compact en voegen we daar kwaliteit toe en blijft het buitengebied groen."
  - "Uitbreidingslocaties woningbouw: We wijzen uitbreidingslocaties aan bij de kernen. [...] Het ontwikkelen van nieuwe erven in het buitengebied is niet toegestaan."
  - Wording in §4.5.3 (Buitengebied): "We zoeken naar ruimte voor woningbouw in het buitengebied. We zien vooral mogelijkheden door herontwikkeling van agrarische bedrijven of het toevoegen van woningen op bestaande erven. Woningsplitsing behoort ook tot de mogelijkheden. Het ontwikkelen van nieuwe erven in het buitengebied is niet toegestaan." En: "Ruimte voor passende woningbouw voor de eigen behoefte, vooral voor starters en ouderen, om de lokale gemeenschap in stand te houden."
  - Woningbouwprogramma tot en met 2030 (tabel 1; bron KAW Woonbehoefteonderzoek 2024): behoefte 775 (Genemuiden 265, Hasselt 290, Zwartsluis 170, Kamperzeedijk 40, Buitengebied "eigen woningvraag"); te programmeren ± 1.010 (≈ 130%). "We bouwen tot 2030 minimaal 775 woningen, verdeeld over alle kernen. Tussen 2030 en 2040 willen we nog eens 610 – 745 woningen realiseren."
- **Bestuursakkoord p. 14:** "In Hasselt en Genemuiden is genoeg ruimte voor nieuwe woningen in de komende jaren. In Zwartsluis en op de Kamperzeedijk zoeken we actief naar nieuwe bouwlocaties. Voor de Kamperzeedijk onderzoeken we de verschillende locaties met een daaraan gekoppeld afwegingskader. In Zwartsluis willen we binnen 4 jaar een concrete woningbouwlocatie aanwijzen." En: "Nieuwe woningbouw moet passen bij het karakter en de identiteit van de verschillende kernen. Daarbij gaat inbreiding waar wenselijk vóór uitbreiding." Plus p. 26: "Grote bebouwing die niet past bij het dorpse karakter willen we voorkomen."
- **Inwonerspanel (Zwartewaterland Spreekt, juni 2026, 603 volledige reacties; factsheet https://zwartewaterlandspreekt.nl/j.a.m.b.o/public-files/Zwartewaterland_Factsheet_Ontwikkellocaties.pdf):** "We moeten nieuwe woningen zoveel mogelijk binnen bestaande kernen bouwen in plaats van aan de rand van kernen": helemaal eens 8%, eens 35%, oneens 47%, helemaal oneens 10% (dus 57% steunt bouwen aan de randen; reden: "Aan de randen is meer ruimte voor verschillende woningtypes: 66%"). "Bestaande groene plekken in de wijk kunnen voor een deel worden gebruikt voor woningbouw": 35% eens, 65% oneens. Het panel gaat niet over het buitengebied zelf; **[INT]** de steun voor uitbreiding aan de randen is er, steun voor bebouwing van open buitengebied is niet gemeten.
- **Ladder voor duurzame verstedelijking:** Raad van State 14-2-2024 (zaak 202201582/1/R3, ECLI:NL:RVS:2024:630, Bodewes/Hasselt): de Afdeling overwoog dat "Niet in geschil is dat het plan voorziet in een nieuwe stedelijke ontwikkeling, als bedoeld in artikel 3.1.6, tweede lid, van het Bro" (recreatiewoningen) en toetste behoefte, ongegrond. Bron: https://www.raadvanstate.nl/uitspraken/@141897/202201582-1-r3/ (volledige tekst gelezen 2026-10-11). Geen (ontwerp-)volkshuisvestingsprogramma gevonden: de Bouwsteen Visie Buitengebied (p. 8) zegt: "De Bouwsteen wonen wordt ingebracht in het Volkshuisvestingsprogramma." en de Omgevingsvisie spreekt over een "nog op te stellen huisvestingsverordening". Het woord "volkshuisvestingsprogramma" komt in de lokale nieuwsberichten 2024-2026 alleen voor bij Staphorst (niet Zwartewaterland).
- **Bouwsteen Ontwikkellocaties** (in de maak): "Op dit moment werkt de gemeente aan de bouwsteen Ontwikkellocaties, dit gaat over welke locaties in de toekomst geschikt zijn voor woningbouw en bedrijvigheid in Zwartewaterland. Richting het einde van het jaar zullen we de voorkeurslocaties delen en krijgen inwoners en ondernemers opnieuw de mogelijkheid om mee te denken." (gemeentenieuws 5-10-2026). De Omgevingsvisie met alle bouwstenen wordt "naar verwachting in het voorjaar van 2027 definitief vastgesteld". Voor CPO is dit het meest actuele inbrengmoment: voorkeurslocaties eind 2026 + inspraak.

## 3. Openheid voor agrarische herbestemming

### 3.1 Wettelijk/procedureel kader (zoals zichtbaar in nieuws en regelingen)
- **Route:** wijziging omgevingsplan of BOPA met bindend advies van de raad. De raad heeft per 21-3-2024 een Adviesrecht Omgevingswet (CVDR718739; in werking 26-4-2024; organisatie volgens SRU-metadata: gemeente Zwartewaterland): "Voor de verlening van een omgevingsvergunning van een buitenplanse omgevingsplanactiviteit [...] waarbij afgeweken wordt van het omgevingsplan wordt de raad vooraf geconsulteerd voor bindend advies, met uitzondering van de volgende categorieën" (kruimelgevallen e.d.). Dus elke BOPA voor 10-12 woningen buiten de kern gaat langs de raad. Voorbeeld uit nieuws: raad adviseert over vervanging/uitbreiding HS/MS-station De Velde (Zwartsluis Actueel 25-9-2026: "De raad wordt gevraagd een positief bindend advies te geven over de omgevingsvergunning. Het plan past niet volledig binnen het omgevingsplan.").
- **Kwaliteitsimpuls Groene Omgeving:** Omgevingsvisie §3.5: "Passen ruimtelijke ontwikkelingen in het buitengebied niet in het omgevingsplan? Dan wordt de afweging gemaakt of de ontwikkeling wenselijk en mogelijk is. Als dat het geval is, dan is het beleid Kwaliteitsimpuls Groene Omgeving van toepassing." De Bouwsteen Visie Buitengebied (p. 9-10): "We actualiseren de beleidsregel Kwaliteitsimpuls Groene Omgeving (KGO 2015) en passen deze waar nodig aan." Er is dus een eigen KGO (2015) met rekenmodel (zie Bijlage A, B1).
- **Beleidsregel extra woning in het buitengebied** (CVDR683809; college 8-11-2022; in werking 18-11-2022; SRU-creator Zwartewaterland): zie §4.

### 3.2 Gemeentelijke houding: concrete signalen 2024-2026
| # | Signaal | Datum | Bron | Duiding |
|---|---|---|---|---|
| 1 | Omgevingsvisie: "Het ontwikkelen van nieuwe erven in het buitengebied is niet toegestaan" (2x) | raad 1-10-2026 | CVDR767481 | Hardste gemeentelijke grens voor onbebouwde agrarische grond |
| 2 | Bouwsteen Visie Buitengebied: "Nieuwe erven in het buitengebied zijn niet toegestaan." en "We zetten, onder voorwaarden, in op inbreiding en transformatie van het bestaande erf." | vastgesteld 22-1-2026 | https://cuatro.sim-cdn.nl/zwartewaterland/uploads/bouwsteen_visie_buitengebied.pdf p. 12 | Toetsingskader voor ontwikkelingen in het buitengebied |
| 3 | Bijlage 7 Bouwsteen: "Woningbouw op bestaande erven in het buitengebied is maatwerk. Het gaat om kleinschalige woningbouw passend bij de maat en schaal van het erf." | idem | idem p. 53 | Maat en schaal van het erf begrenzen aantal |
| 4 | Gebiedsgerichte uitwerking (negen deelgebieden), rubriek "Wonen": De Wieden "Nee tenzij; het op een bestaand erf is ..."; Veldiger Binnenlanden "Ja mits; het op een bestaand erf is ..."; Zwarte Water/Zwarte Meer "Nee; we bouwen buitendijks en in N2000 geen woningen."; Zeekleipolders "Nee tenzij ..."; Dijken "Ja mits; het op een bestaand erf is [...] De kern Kamperzeedijk [...] biedt kansen voor het toevoegen van woningen"; Polder Mastenbroek "Ja mits [...] onder strikte voorwaarden meedenken over het toevoegen van een beperkt aantal woningen" rond kerk/school/dorpshuis; Zwartewatersklooster "Ja mits ..."; Genne-Holten-Streukel "Ja; [...] ruimte voor woningen op bestaande erven"; Gennegerbroek "Ja mits; het op een bestaand erf is, buiten het gebied aangewezen voor windenergie ligt ..." | 22-1-2026 | Bouwsteen p. 15-32 | In alle deelgebieden is "bestaand erf" de voorwaarde; geen deelgebied kent "onbebouwde grond" |
| 5 | Landgoed Stroombeek (Zwartsluis): intentieovereenkomst 2-6-2026 en "positief principebesluit"; woningen bij Barsbeek "op langere termijn" | 2-6-2026 | Zwartewaterkrant 12-6-2026; Zwartsluis Actueel 12-6-2026 | Rood-voor-groen-achtige landgoedroute (initiatiefnemer sinds 2013); "rekening [...] met de strenge stikstof-eisen" |
| 6 | Kamperzeedijk: Westererf, Oostermaat (achter), garage Selles — drie locaties, "op korte termijn niet gebouwd", afwegingskader | 4-3-2026 | Genemuiden Actueel 4-3-2026 | Gemeente wil dorpsuitbreiding; buurt verzet zich (zie §6) |
| 7 | Bodewes/Molenwaard: recreatie → wonen; gemeente "benadrukt dat het om een uitzonderlijke situatie gaat en dat dit niet automatisch betekent dat andere recreatiegebieden ook een woonbestemming krijgen" | jan. 2026 | Hasselt Actueel 22-1-2026 | Terughoudendheid tegen precedenten |
| 8 | Arbeidsmigranten in agrarisch gebied: "Huisvesten van arbeidsmigranten in het agrarisch gebied is toegestaan in geval van hergebruik van bestaand vastgoed" (beleidsafstand 150 m tot woningen van derden) | 2025-2026 | Genemuiden Actueel 15-4-2025, 1-4-2026, 19-5-2026 | Hergebruik bestaande bebouwing = route; grote afstandsregel |
| 9 | Landbouw: "Nieuwe functies op voormalige boerenerven mogen andere bedrijven in de omgeving niet onnodig beperken." | 19-6-2026 | Bestuursakkoord p. 19 | Beschermt omliggende landbouw |

### 3.3 Concreet stappenplan en indicatieve doorlooptijd (uit nieuws/regelingen) [INT]
1. **Vooroverleg / principeverzoek** bij het college (portefeuille wonen/ruimtelijke ordening: Slingerland). Voorbeeld: Schaapman (arbeidsmigranten Kamperzeedijk) diende ná weigeringen een principeverzoek in (college 7-7-2025). Landgoed Stroombeek: positief principebesluit pas na intentieovereenkomst (2-6-2026) na initiatief sinds 2013.
2. **Omgevingsgesprek met de buurt** is verplicht bij extra woning in het buitengebied (CVDR683809 art. 3.3 lid 3 en art. 4 lid 4) en participatiebeleid (CVDR700533).
3. **Ervenconsulent en beplantingsplan** (KGO) — CVDR683809 art. 3.3 lid 2.
4. **ETFAL-motivering** ("Evenwichtige toedeling van functies aan locaties") via de gemeentelijke "handreiking ETFAL motivatie kleine BOPA en wijziging omgevingsplan" (genoemd in CVDR738380 art. 4; handreiking zelf niet gevonden).
5. **Raad: bindend advies** (CVDR718739) of vaststelling omgevingsplanwijziging; Binnenveld-bestemmingsplan: raad 11-7-2024 "zeer positief"; Hasselt Malcorpslaan bestemmingsplan raad 4-4-2024.
6. **Netcongestie: eerder aanvragen / aanmelden** (CVDR765999) — zie §12/Bijlage A C4; aanmelding "betekent niet dat de gemeente akkoord is met het plan" (art. 12 lid 3).
7. **Provincie:** voorkantsamenwerking; BOPA-instemming bij nieuwe woningen in de Groene Omgeving **[PB]** §4 (provinciebestand); in nieuws geen aanwijzing van een provinciale rol bij concrete Zwartewaterlandse woningbouwplannen gevonden.
- **Doorlooptijd uit nieuws:** Tijlshof (Knarrenhof, kern Hasselt, gemeentegrond): initiatief 2013 → overeenkomst 8-5-2019 → bestemmingsplan raad 29-10-2020 → oplevering 10-11-2022 (≈ 9 jaar, waarvan ≈ 1 jaar vertraging door bezwaren van 14 adressen). Binnenveld: raad 11-7-2024 → voorbelasting 2026 → bouwrijp voorjaar 2027 → kavelverkoop najaar 2027 → bouw daarna (netaansluiting onzeker). Kamperzeedijk: eerst aangekondigd, locatiekeuze nog niet gemaakt, bouwstart voorlopig 1-6-2029 (volgordelijst).

### 3.4 Kansrijk vs. kansarm [INT, uit bovenstaande bronnen]
- **Kansrijk:** bestaand (agrarisch) erf met sloop/herontwikkeling; aansluitend aan een kern of lint (Kamperzeedijk, Zwartsluis, Mastenbroek rond kerk/school/dorpshuis); gemeentegrond met gemeentelijke regie; starters/senioren/eigen inwoners; geen belemmering voor omliggende agrarische bedrijven; stikstof- en netcongestieplan vooraf.
- **Kansarm:** onbebouwde agrarische grond buiten de kernen ("nieuwe erven" niet toegestaan); deelgebied De Wieden/Zeekleipolders/buitendijks/N2000-nabij ("Nee"/"Nee tenzij"); Polder Mastenbroek (Nationaal Landschap IJsseldelta, Belvedère, 2020 petitie >1.500 handtekeningen tegen bouw in De Driehoek); locaties zonder netaansluiting; projecten die "het dorpse karakter" overschrijden ("Grote bebouwing die niet past bij het dorpse karakter willen we voorkomen", akkoord p. 26).

### 3.5 Eindoordeel per schaalscenario (nieuws-gebaseerd, voorlopig) [INT]
| Scenario | Inschatting | Toelichting |
|---|---|---|
| 1-3 woningen op bestaand erf (extra woning/splitsing/sloop-terugbouw) | **Haalbaar** | Beleidsregel extra woning (2022) + Bouwsteen "Ja mits"; coalitie wil dit versoepelen ("kaders opstellen") |
| 3-6 woningen via herontwikkeling vrijkomend agrarisch erf | **Mogelijk, maatwerk** | "inbreiding en transformatie van het bestaande erf"; VAB-beleid wordt nog uitgewerkt (Bouwsteen p. 5, 13); voorbeeld Landgoed Stroombeek (1 + woningen bij Barsbeek is kern-uitbreiding) |
| 10-12 woningen op bestaand erf | **Onzeker/lastig** | "maat en schaal van het erf"; geen max aantal gevonden; zou volgens Bouwsteen "maatwerk" zijn; Overijssels KGO/typologie bepaalt (zie [PB]); geen precedent in nieuws gevonden |
| 10-12 woningen op onbebouwde agrarische grond buiten de kernen | **Kansarm** | "nieuwe erven ... niet toegestaan" (Omgevingsvisie 2x, Bouwsteen); wel mogelijk als uitbreidingslocatie *aansluitend* aan Kamperzeedijk/Zwartsluis/Hasselt/Genemuiden na opname in Bouwsteen Ontwikkellocaties |
| 10-12 woningen als CPO aansluitend aan een kern (uitbreidingslocatie) | **Meest realistisch** | Akkoord noemt CPO; volgordelijst netcongestie kent kleine projecten (Kamperzeedijk 30, Aalvanger 18, Mastenbroek 12); moet in voorkeurslocaties eind 2026 |

**Vervolgstap/contactpersoon (informeel voorgesprek):** wethouder Maarten Slingerland (SGP), kernwethouder Genemuiden en het buitengebied, m.slingerland@zwartewaterland.nl, tel. 14 038 (profielpagina https://www.zwartewaterland.nl/maarten-slingerland, 2026-10-11); voor inhoud ook omgevingsvisie@zwartewaterland.nl (Bouwsteen Ontwikkellocaties) en de erfcoach Noordwest-Overijssel (§4).

## 4. VAB-beleid (Vrijkomende Agrarische Bebouwing)

**Bevinding: geen vastgesteld VAB-beleid; de gemeente werkt eraan (Bouwsteen Visie Buitengebied, intergemeentelijk programma Noord-West Overijssel).** Het woord "VAB"/"vrijkomende agrarische bebouwing" komt in lokaal nieuws 2024-2026 niet voor, behalve in de Koninklijke-onderscheidingsbericht (andere betekenis, VAB = Vereniging).
- **Bouwsteen Visie Buitengebied (22-1-2026), p. 13:** "We zetten in op het invullen van vrijgekomen agrarische bebouwing (vab) en erftransformatie. We bieden ruimte aan verbreding met nevenactiviteiten voor agrariërs. Bij het uitwerken van het vab-beleid verkennen we hoe we dit kunnen borgen in het Omgevingsplan. / We evalueren het huidige vab-beleid en passen deze waar nodig aan. Indien mogelijk doen we dit samen en in afstemming met omringende gemeenten." En p. 5: "Zoals het uitwerken van beleid voor vrijkomende agrarische bebouwing, wonen, werken en recreatie en toerisme. De Kwaliteitsimpuls Groene Omgeving gaan we actualiseren." En p. 33 (concrete acties): "Na vaststelling van deze Bouwsteen trekken we het Landschapsontwikkelingsplan Zwolle-Zwartewaterland-Kampen (LOP) uit 2010 in."
- **Omgevingsvisie (CVDR767481), §3.5:** "Nieuwe functies in vrijkomende agrarische bebouwing en erven: We staan positief tegenover nieuwe functies in vrijkomende agrarische bebouwing en erven. In het omgevingsplan nemen we hiervoor uitgangspunten en randvoorwaarden op."
- **Intergemeentelijk programma (D1):** het college van Steenwijkerland (informatienota 2024_B&W_00465, 18-6-2024, https://steenwijkerland.bestuurlijkeinformatie.nl/Document/View/ff626622-86ae-4833-91a1-2294afaedfc9, gelezen 2026-10-11) schrijft: "De provincie Overijssel is bezig met het opstellen van een Programma Vrijkomende Agrarische Bedrijven (VAB). [...] De gemeenten Kampen, Staphorst, Steenwijkerland, Zwartewaterland en Zwolle werken samen met de provincie aan een invulling van het programma voor het gebied Noord-West Overijssel. Er wordt gekeken of er een raamwerk gemaakt kan worden waarin gezamenlijke uitgangspunten staan voor het ontwikkelen van VAB-locaties waarbij gemeenten zelf lokale of specifieke uitgangspunten kunnen toevoegen." Deelname aan subsidie 4.39 (activiteit B/C) of een lopende aanvraag door Zwartewaterland zelf is **niet** gevonden (waar: provincie Overijssel, loket subsidies 4.39; Uitvoeringsbesluit subsidies Overijssel 2022, CVDR679264 **[WF]**).
- **Erfcoach (D2):** gemeentepagina https://www.zwartewaterland.nl/erfcoaches (2026-10-11): "In het buitengebied van Noordwest Overijssel staat erfcoach Jan-Olaf Tjabringa klaar om met erfeigenaren mee te denken over de toekomst van het (boeren)erf." Onderwerpen: "Wonen op het erf en herontwikkeling van vrijkomende agrarische erven; Vergroening; Subsidies en regelingen". Contact: 06 27 09 56 40, tjabringa@cultuurland.com (vanuit provincie Overijssel); verwijzing naar www.erfcoachoverijssel.nl en www.boerenperspectiefoverijssel.nl; daarnaast Zorg om Boer en Tuinder (Gert Boesveld, 06 22 39 56 40). Erfcoach is dus actief in Zwartewaterland (financiering: [PB] 2026 verzekerd).
- **Precedent-/praktijkbeelden VAB-achtig:** voormalige boerderij Ter Wee (Hasselt, bij Om de Weede): gemeentelijk eigendom, volledige sloop sept./nov. 2026 (Hasselt Actueel 17-6-2026), toekomstige invulling in "Omgevingsplan en beeldkwaliteitsplan" (BKP Havezate Groot Terwee, CVDR748169, raad 29-11-2025); dossier met maatschap Knol afgerond met € 287.500 + € 115.000 dwangsommen (Hasselt Actueel 13-10-2025). Boerderij Dijkstra/"Hoeve de Roebol" (Cellemuiden): "Toekomst voor natuurvriendelijk boerenbedrijf veiliggesteld" (26-6-2025) — agrarisch, geen woningbouw.
- **Rijksregeling:** in de gemeente hebben zich bedrijven aangemeld voor Rijksuitkoopregelingen? Niet in Zwartewaterlandse berichten gevonden (Steenwijkerland noemt een tiental in de eigen gemeente).

## 5. Grondbeleid

- **Wethouder:** Slingerland heeft "Grondzaken (grex+pacht) en vastgoed" (profielpagina). Gemeente voert in de praktijk actief grondbeleid bij de grote locaties (Binnenveld, Om de Weede, Ter Wee/Havezate, Aalvanger-woningbouw via ontwikkelaar Heutink, Malcorpshof verkocht aan Koraal Vastgoed 10-2-2026). Nota Grond- en Vastgoedbeleid 2023 (CVDR702877, in werking 19-10-2023; SRU-creator Zwartewaterland) is niet inhoudelijk gelezen (alleen bijlage-verwijzing): deelonderzoek 1/4.
- **Grondposities in buitengebied:** gemeente verpacht agrarische gronden in geliberaliseerde pacht; nieuw pachtbeleid met loting/transparantie, raadsbesluit februari 2024 (Genemuiden Actueel 23-1-2024; uitkomst niet bevestigd). Overwaters/De Driehoek (Hasselt-Cellemuiden): gemeente kocht in 2005 grond, ruilde in 2006 met ontwikkelaar AM; plan 17 woningen, in 2020 politiek omstreden (RTV Oost 13-3-2020: ">1.500 handtekeningen" volgens Hasselt Actueel 28-2-2022; "Miljoenenstrop voorkomen"). In de Omgevingsvisie (2026) is "Overwaters, een kleinschalige landschappelijke woonlocatie langs de Cellemuiderdijk" opgenomen; volgordelijst: 17 woningen, bouwstart 1-4-2031.
- **Erfpacht:** niet gevonden in nieuws (waar: Nota Grond- en Vastgoedbeleid 2023).
- **Actueel kavelaanbod (gemeentesite, 2026-10-11):** Hasselt Om de Weede Veld 1: 19 kavels vrijstaand; Veld 2: 8 vrijstaand + 4 twee-onder-een-kap (laatste "inmiddels verkocht"); optie 8 weken kosteloos (+6 weken), contact vastgoed@zwartewaterland.nl / 14 038 (mw. G. van Dalfsen, medewerker Vastgoed); prijs per kavel staat in PDF-kavelpaspoorten (niet gelezen). Aanbod projectmatig "Langs de Weiden": VanWonen, 42 woningen. Tag West Genemuiden: vrije kavels via Ontwikkel Combinatie Genemuiden (www.tagwest.nl). Binnenveld: 18 vrije kavels, verkoop "ongeveer najaar 2027". Prijspunt (anekdotisch **[WF]**): "€ 1.000,- per m2 voor een bouwkavel in Zwartsluis" (X-bericht, Zwartsluis Actueel 20-8-2025).
- **Grote ontwikkellocaties met gemeentelijke grondpositie:** Binnenveld Genemuiden ± 243 woningen (18 vrije kavels, 16 rug-aan-rug starters, 78 zorgwoningen, 27 hofjeswoningen senioren, 62 seniorenappartementen, 42 starterappartementen; Genemuiden Actueel 12-7-2024); BinnenErf ± 80 zorgwoningen (Van der Steeg; bouw "binnenkort", 29-9-2026); Binnenveld II 215 woningen (2034-2035, volgordelijst). **Collectief/CPO gereserveerd: nergens gemeld.**
- **Plancapaciteit/tempo:** Omgevingsvisie: behoefte 775 tot 2030, programma ± 1.010 (≈ 130%). [PB] Woondeal West-Overijssel: gerealiseerd Q1 2022-Q4 2024: 244; sleutelprojecten 3 / 559; doorkijk 2031-2035: 77. Duiding [INT]: 244 = netto toename in 12 kwartalen (≈ 20 per kwartaal; consistent met RTV Oost 24-4-2025 "vorig jaar per kwartaal gemiddeld negentien"), 3/559 = drie sleutelprojecten (≥ 50 woningen) met samen 559 woningen 2024-2030, 77 = woningen in 2031-2035. **Q1 2025: slechts 2 woningen**, "de laagste score van alle Overijsselse gemeenten" (RTV Oost 24-4-2025, Slimster/CBS). Volgordelijst (CVDR765999-lijst, 44 projecten): ± 1.007 woningen **[BER]** met bouwstart 1-1-2027 t/m 2036; 8 projecten ≥ 30 woningen.
- **Ruimte voor derden (20%-regel):** niet expliciet in nieuws; "flexibiliteit in het woningbouwprogramma" en 130% (Omgevingsvisie). Buitengebied wordt niet geprogrammeerd ("eigen woningvraag").

## 6. Praktijkvoorbeelden (2024-2026)

| # | Voorbeeld | Datum | Bron (URL) | Relevantie voor ons concept |
|---|---|---|---|---|
| 1 | **Binnenveld Genemuiden**: bestemmingsplan 243 woningen; voorbelasting gestart sept. 2026; "Op dit moment hebben we van Enexis voor dit gebied helaas nog geen aansluiting [...] gekregen"; 18 vrije kavels | raad 11-7-2024; 29-9-2026 | https://www.genemuidenactueel.nl/2024/07/12/groen-licht-voor-243-nieuwbouwwoningen/ ; https://www.zwartewaterland.nl/vrachten-met-zand-als-basis-voor-de-nieuwe-woonwijk-in-binnenveld | Grote gemeentelijke uitleg bij kern; laat zien dat netaansluiting (niet beleid) de planning bepaalt; vrije kavels = enige "zelfbouw" |
| 2 | **BinnenErf / woonvoorziening Binnenveld**: ± 80 zorgappartementen, "lokaal initiatief van vier verschillende woongroepen" (Carendis, Helpende Handen, Akkerwinde, Op weg met de Ander) met Van der Steeg; jongerenwoningen "Stichting Thuis op het Binnenveld" | 4-2-2025; 24-10-2025 | https://www.genemuidenactueel.nl/2025/02/04/eerste-handtekeningen-gezet-voor-zorgcomplex-binnenveld/ | Collectief bewonersinitiatief binnen gemeentelijke wijk; model voor samenwerking met zorgpartijen |
| 3 | **Kamperzeedijk woningbouw**: Westererf (on hold) → Oostermaat gekozen door enquête/dorpsraad → buurtverzet ("Historische vergissing") → drie opties (Westererf/Oostermaat/Selles) | 1-10-2025; 10-10-2025; 4-3-2026 | https://www.genemuidenactueel.nl/2026/03/04/nieuw-onderzoek-naar-drie-woningbouwlocaties-kamperzeedijk/ | Het dichtst bij ons concept (kern in buitengebied; 40 woningen 2029-2030 op volgordelijst); draagvlak gevoelig; afwegingskader komt |
| 4 | **Landgoed Stroombeek + Barsbeek-uitbreiding (Zwartsluis)**: intentieovereenkomst, positief principebesluit | 2-6-2026 | https://zwartewaterkrant.nl/news/view/mogelijke-woningbouw-en-landgoed-in-zwartsluis-stapje-dichterbij | Landgoedroute buitengebied; "strenge stikstof-eisen"; moet passen in Bouwsteen Ontwikkellocaties |
| 5 | **Woningsplitsing + Mobiliteitsfonds** | raad 12-12-2024; beleidsregel 8-4-2025 | https://www.hasseltactueel.nl/2024/12/13/woningsplitsing-gemakkelijker-door-mobiliteitsfonds/ ; CVDR738380, CVDR735559 | Binnen bebouwde kom; max 20% per straat; 60 m2 per woning |
| 6 | **Bodewes/De Molenwaard** (Hasselt): recreatie → permanente woonbestemming "uitzonderlijke situatie" | VvE 17-1-2025; raad jan. 2026; RvS 14-2-2024 | https://www.hasseltactueel.nl/2026/01/22/toch-woningen-op-bodewesterrein/ | Agrarisch-achtige herbestemming buitengebied: alleen via bestaande feitelijke situatie; geen precedent |
| 7 | **Arbeidsmigranten Kamperzeedijk (Schaapman)**: omgevingsvergunning 24 personen in schuur geweigerd (150 m-regel, 85 m aanwezig); rechter eerder gemeente "huiswerk" gegeven; illegale bewoning aangetroffen; beleid "na vijf jaar een flop" | 15-4-2025; 1-4-2026; 19-5-2026 | https://www.genemuidenactueel.nl/2025/04/15/gemeente-weigert-opnieuw-vergunning-voor-arbeidsmigranten-kamperzeedijk/ | Hergebruik bestaand agrarisch vastgoed "toegestaan", maar buren en afstandsregels zwaar; rechtszaken; gemeente mikt op één functie per erf |
| 8 | **Malcorpshof** (Hasselt): 16 koopwoningen + begeleid wonen; koopovereenkomst Koraal Vastgoed | 10-2-2026 | https://www.zwartewaterland.nl/malcorpshof-nieuwe-woonlocatie-in-hasselt | Inbreiding, geen buitengebied |
| 9 | **Aalvanger-locatie** (Hasselt): 18 woningen (6 grondgebonden + 12 appartementen), Heutink | 23-6-2026 | https://www.hasseltactueel.nl/2026/06/23/woningbouw-voormalige-aalvangerlocatie-stap-dichterbij/ | Kleine inbreiding ≈ schaal 10-18 |
| 10 | **Frion-gebouw Zwartsluis**: 26 sociale huurappartementen; "primair bouwen voor onze eigen inwoners" | start 16-6-2025 | https://www.zwartsluisactueel.nl/2025/06/19/verbouw-van-friongebouw-officieel-van-start/ | Transformatie; lokale voorrang |
| 11 | **Buiten de Venepoort** (Hasselt): stedenbouwkundig kader; 52 woningen op volgordelijst | 27-1-2026 | https://www.zwartewaterland.nl/toekomstplannen-voor-buiten-de-venepoort-in-hasselt | Herontwikkeling garage |
| 12 | **Verkiezingsprogramma's wonen**: CDA "Een Sluuziger op een woning"; CU "In Mastenbroek en Kamperzeedijk moet passend gebouwd worden voor de eigen gemeenschap" [ADV]; PvdA focus Zwartsluis | feb.-mrt. 2026 | https://www.zwartsluisactueel.nl/2026/02/26/woningbouw-in-zwartsluis-belangrijk-voor-partijen-maar-locaties-noemen-ze-niet/ | Brede partijsteun voor kleinschalig bouwen voor eigen gemeenschap |
| 13 | **Tijlshof** (2022, ter vergelijking) | 10-11-2022 | https://www.hasseltactueel.nl/2022/11/10/tijlshof-feestelijk-opgeleverd/ | Referentie collectief project; ≈ 9 jaar |
| 14 | **De Driehoek/Overwaters** (2020-2022) | 13-3-2020; 28-2-2022 | https://www.oost.nl/nieuws/327106/protest-tegen-woningbouw-in-polder-mastenbroek-wees-zuinig-op-wat-je-hebt | Draagvlakrisico bouwen in open polder/NNN-nabij; coalitie én oppositie wilden in 2022 "een pas op de plaats" |

## 7. Inventarisatie bestaande initiatieven

| Initiatief | Aantal woningen | Status | Relevantie |
|---|---|---|---|
| **Knarrenhof De Tijlshof, Hasselt** (Vereniging Knarrenhof Zwartewaterland; Stichting Knarrenhof; bouwer Nikkels) | 16 koopwoningen + Hofhuys | Opgeleverd 10-11-2022; "6e hof [...] in Nederland"; initiatief 2013; gemeentegrond (voormalige gemeentewerf/politiebureau, sanering) | Enige gevonden collectief wooninitiatief; bewoners tekenen "sociaal contract" bij koopcontract (Hasselt Actueel 12-10-2022); wordt in 2025 genoemd als voorbeeld in Zwartewaterland (Zwartewaterkrant/Welzijn, 3-2-2025) |
| **BinnenErf Binnenveld** (4 woongroepen + Van der Steeg) | ± 80 appartementen (8 appartementen + 16 studio's Carendis) | Intentieovereenkomst dec. 2024; bouw "binnenkort" (29-9-2026) | Collectief zorginitiatief; geen CPO-vorm |
| **Woonvoorziening jongeren ASS/LVB, Binnenveld** (Stichting Thuis op het Binnenveld; vereniging Op weg met de Ander) | enkele appartementen ("nog maar enkele appartementen beschikbaar") | Informatieavond 27-11-2025 | Ouderinitiatief |
| **Landgoed Stroombeek** (particuliere initiatiefnemer) | 1 + 6 (Landgoed Stroombeek 2A) + 32 kavel(s) volgens volgordelijst | Intentieovereenkomst 2-6-2026 | Particulier initiatief buitengebied |
| **Tiny houses / flexwoningen** | — | Alleen intentie akkoord; schoolproject | Geen beleid |
| **Mastenbroek woningbouw** | 12 | Volgordelijst, start 1-1-2030 | Kleinkern; locatie rond kerk/school/dorpshuis |
- Dubbeltelling gecontroleerd: "Westererf" (locatie voor Oekraïense opvang, eigenaar particulier) en "Kamperzeedijk 40 woningen" zijn dezelfde plek als 'Westererf' op de volgordelijst; Oostermaat is een apart alternatief (beide 40 woningen, niet optellen).
- **Niet gevonden:** CPO-vereniging, CPO-kavels, zelfbouwcollectief. Waar: gemeente (vastgoed@zwartewaterland.nl), Platform31/Stichting CPO-netwerk **[TK]**.

## 8. Huisvestingsverordening

**Bevinding: nee, nog geen algemene huisvestingsverordening (woonruimteverdeling/urgentie) in werking.** SRU-doorzoek van alle 736 CVDR-records van Zwartewaterland: geen huisvestingsverordening; wel "Huisvesting van arbeidsmigranten in de gemeente Zwartewaterland" (CVDR668202, in werking 1-1-2022, beleidsregels).
- Omgevingsvisie §3.10.2: "We willen aan hun behoefte kunnen voldoen door middel van een nog op te stellen huisvestingsverordening."
- Bestuursakkoord p. 15: "We maken een huisvestingsverordening [voor arbeidsmigranten]."
- Raad 11-7-2024 (Genemuiden Actueel 12-7-2024): wethouder Rietman over de nieuwe Huisvestingswet (50% eigen inwoners): "in de gemeente [gaat] al ongeveer vijftig procent van de woningen naar eigen inwoners. In Genemuiden gaat het om tachtig procent".
- Sociale-huurpercentage: 30-40-30-regel (30% sociale huur; Omgevingsvisie tabel 2: sociale huur 30% ± 300 woningen; vergroting sociale voorraad 205-255 tot 2030). Starterslening: Verordening Starterslening (CVDR619790_3, raad 30-3-2023, verhoging CVDR693747).

## 9. Zelfbouwloket / contactpersoon

**Bevinding: geen zelfbouwloket of CPO-aanspreekpunt gevonden.** Wel:
- Wethouder Wonen/buitengebied: Maarten Slingerland, m.slingerland@zwartewaterland.nl, 14 038.
- Kavels Om de Weede: vastgoed@zwartewaterland.nl, 14 038 (mw. G. van Dalfsen, medewerker Vastgoed).
- Binnenveld: binnenveld@zwartewaterland.nl; netcongestie: netcongestie@zwartewaterland.nl; Omgevingsvisie/Bouwsteen: omgevingsvisie@zwartewaterland.nl; algemeen info@zwartewaterland.nl; bestuurssecretariaat secretariaat@zwartewaterland.nl.
- Erfcoach Jan-Olaf Tjabringa (06 27 09 56 40); kerncoördinatoren (gebiedsgericht werken): "Onze kerncoördinatoren denken graag mee over de mogelijkheden en over subsidies" (gemeentenieuws 28-9-2026).
- Waar het wel zou moeten staan: pagina "Huis kopen" / Nieuwbouwprojecten op zwartewaterland.nl; omgevingsloket-intake (Team vergunningen).

## 10. Bestuurlijk klimaat

### 10.1 Is er een coalitie in vorming? Nee.
Gecontroleerd 2026-10-11 op gemeentenieuws (t/m 8-10-2026) en de drie Actueel-sites (t/m 10-10-2026): formatie afgerond, college 25-6-2026 geïnstalleerd, eerste begroting 2027 gepresenteerd 8-10-2026 ("Het nieuwe college [...] presenteert zijn eerste begroting"; raad bespreekt in november). Geen tussentijdse val of fractiebreuk gevonden. Opvallende lopende kwesties: asielopvang (Rijk stelt gemeente per 1-10-2026 onder "actief toezicht", trede 3; 124 duurzame opvangplaatsen; Genemuiden Actueel 18-9-2026), nieuwe griffier (Ine Margriet Westhoff, 17-9-2026), burgemeester Judith Compagner (geïnstalleerd 20-11-2025).

### 10.2 Uitslag 18-3-2026 (voorlopig; opkomst 69,5% volgens AlleCijfers)
| Partij | Stemmen | Zetels |
|---|---|---|
| SGP | 3.748 | 6 |
| BGZ (Buitengewoon Zwartewaterland) | 3.251 | 6 |
| ChristenUnie | 2.598 | 4 |
| CDA | 1.066 | 1 |
| PvdA | 895 | 1 |
| VVD | 831 | 1 |
Bron: https://www.genemuidenactueel.nl/2026/03/19/zes-zetels-voor-zowel-sgp-als-bgz-verlies-voor-cda-en-pvda/ (19-3-2026, voorlopig); zetelverdeling bevestigd door informateursverslag (12 van 19 zetels voor SGP+BGZ). Definitieve uitslagpagina niet apart geraadpleegd.

### 10.3 Formatieverloop
| Datum | Gebeurtenis |
|---|---|
| 18-3-2026 | Verkiezingen |
| 20-3-2026 | SGP stelt informateur Aart de Kruijf (ex-wethouder Barneveld) voor; eerste keer een informateur in Zwartewaterland |
| 23-4-2026 | Verslag: advies SGP + BGZ, "politiek motorblok", drie wethouders (SGP, BGZ, gezamenlijk). ChristenUnie "teleurgesteld" (24-4) — minder voorspelbaar stemgedrag genoemd |
| 6-5-2026 | Formateur Gert Wiegers start formatie; 8 gesprekken |
| 11-6-2026 | Akkoord op hoofdlijnen, raadsbrede agenda (nieuw) |
| 19-6-2026 | Bestuursakkoord gepresenteerd |
| 25-6-2026 | College geïnstalleerd; afscheid Rietman (PvdA), Van der Poel (CU) |

### 10.4 College en portefeuilles (https://www.zwartewaterland.nl/samenstelling-college; profielpagina's, 2026-10-11)
- **Judith Compagner** (burgemeester): openbare orde, HR/communicatie, dienstverlening/participatie, bestuurlijke coördinatie; lid AB Regio Zwolle; thema gebiedsgericht werken.
- **Maarten Slingerland (SGP), 1e loco, kernwethouder Genemuiden en het buitengebied**: Economie; "Wonen, landbouw, ruimtelijke ordening (inclusief stikstof)"; Vergunningverlening; Grondzaken (grex+pacht) en vastgoed; Financiën. Thema's: Wonen, Omgevingsvisie, Vitaal gemeentehuis, Huisvesting vluchtelingen/asielzoekers/arbeidsmigranten, Visie zwembaden. Nevenfuncties: stuurgroep IJsselvechtdelta, platform ruimtelijk domein VNG Overijssel, portefeuilleoverleg ruimte Regio Zwolle, bestuurlijk overleg Wonen West-Overijssel.
- **Alijn Muijsers(-Lok) (BGZ), 2e loco, kernwethouder Hasselt**: sociaal domein, sport, cultuur/recreatie, beheer openbare ruimte.
- **Benjamin van Marle (SGP/BGZ), 3e loco, kernwethouder Zwartsluis**: onderwijs, water, klimaatadaptatie, **energietransitie/netcongestie**, mobiliteit/haven, monumenten, toezicht en handhaving.
- Vorig college (2022-2026): SGP, ChristenUnie, PvdA; wethouders wonen: Jan van der Poel (CU) en Harrie Rietman (PvdA, o.a. omgevingsvisie, Binnenveld).

### 10.5 Bestuursakkoord: relevante passages
Zie §1 (CPO, tiny houses, extra woning op erf), §2 (kernen/uitbreiding), en: netcongestie (§3.7, p. 17-18): "Of er genoeg stroomcapaciteit beschikbaar is, bepaalt steeds meer wat er mogelijk is op het gebied van woningbouw, bedrijven en voorzieningen. Daarom nemen we de beschikbaarheid van het elektriciteitsnet mee in al onze ruimtelijke keuzes." Stikstof/landbouw (§3.9, p. 18-19): "Agrarische bedrijven moeten de ruimte houden om economisch gezond en toekomstbestendig te kunnen ondernemen. Het buitengebied moet leefbaar blijven voor iedereen die er woont en werkt." Statushouders: "Sociale huurwoningen willen we zoveel mogelijk beschikbaar houden voor onze eigen inwoners." Arbeidsmigranten: "stimuleren we grootschalige huisvesting buiten de kernen" (p. 15; afwegingskader). Plattelandsgemeente: "Wij blijven bouwen aan sterke kernen, een vitaal buitengebied" (p. 3). Regionaal: "Zwartewaterland is een zelfstandige gemeente en dat willen we blijven" (p. 27).

### 10.6 Politieke duiding voor CPO [INT]
SGP (grootste) is lokaal-conservatief, ondernemers-/eigen-gemeenschap-gericht; BGZ (lokaal, sterk in Hasselt) benadrukt "lokaal beslissen" en kernen/buitengebied. Beide partijen ondertekenden CPO-zin. Spanningsveld: zowel partijen als inwoners verzetten zich tegen bouwen in open polder; ChristenUnie (oppositie, drijvende kracht achter bouwtempo) wilde "passend bouwen" in Mastenbroek/Kamperzeedijk. Raadsbrede agenda geeft oppositie meer invloed op grote vraagstukken (Zwartsluis-locatie, zwembaden, opvang). Vooral kans: kleinschalig voor eigen inwoners, jongeren en senioren, aansluitend aan kernen.

## 11. Kostenverhaal en leges

- Gemeentelijk kostenverhaal bij kleine ontwikkelingen: nadeelcompensatie-/planschadeovereenkomst verplicht bij woningsplitsing (CVDR738380 art. 5: "Er wordt geen medewerking verleend aan het initiatief wanneer geen overeenkomst nadeelcompensatie is getekend"); Mobiliteitsfonds (bijdrage "duizenden euro's", 10 jaar inzet; Verordening Mobiliteitsfonds CVDR735559, in werking 14-2-2025); KGO-kwaliteitsprestatie (ervenconsulent, beplantingsplan; CVDR683809). Anterieure overeenkomsten: niet in nieuws gevonden (waar: Nota Grondbeleid 2023, leges-/exploitatieregels).
- **Netcongestie-aanbetaling:** "Om op de prioriteringslijst te komen vraagt Enexis een aanbetaling van 20% van de aanlegkosten" (voorbeeld gemeentesite: 3 x 25A € 1.817 → € 363,40; 3 x 35A/3 x 50A € 2.245 → € 449,00; 3 x 63A € 2.687 → € 537,40, per woning). Bij gemeentelijke aanvraag: financiële afspraken met ontwikkelaar met "materiële zekerheid" (CVDR765999 art. 15 lid 2).
- Leges: Verordening leges 2025 (CVDR726980_2) en 2026 (CVDR747704, raad 25-11-2025) bestaan (SRU-creator Zwartewaterland); tarieven BOPA/omgevingsplanwijziging niet gelezen: deelonderzoek 4.

## 12. Woningbehoefte en doelgroepen

- **Woonbehoefteonderzoek 2024** (gemeente + Wetland Wonen; 830 respondenten; Genemuiden Actueel 18-7-2024): "tot en met 2030 in Zwartewaterland 660 tot 850 woningen"; "Jongeren zijn vooral op zoek naar betaalbare koopwoningen [...] rij- en hoekwoningen"; vraag het grootst in Hasselt, dan Genemuiden, Zwartsluis; groei senioren, zorggeschikte woningen. Omgevingsvisie (KAW 2024): 775 tot 2030.
- **Prioriteiten:** kleine woningen < 80 m², starters en senioren, 30-40-30, sociale huur +205-255, levensloopbestendig/geclusterd/zorggeschikt, "bijzondere woonvormen, zoals het wonen in hofjes"; coalitie: starters, jongeren, ouderen, alleenstaanden, "nestverlaters".
- **Sluit CPO aan? [INT]** Ja voor een compact, betaalbaar, senioren-/starterscluster voor eigen inwoners (hofje); minder voor ruimtelijk grote, vrijstaande kavels in het buitengebied. Een CPO van 10-12 woningen telt als "overige plancapaciteit"; sleutelprojecten zijn ≥ 50 woningen [PB].
- Prestatieafspraken Wetland Wonen 2026-2029 (ondertekend 25-11-2025): "nieuwe locaties [...] om het tekort aan sociale huurwoningen terug te dringen"; Woonzorgvisie 2026 aangekondigd.

---

## Twee kernvragen

### 1. Wonen in het buitengebied: ruimte voor een cluster van 10-12 woningen buiten de bestaande woonkernen?
- **(a) Gemeentelijk:** Beperkt. Nieuwe erven niet toegestaan; woningen op bestaande erven als maatwerk ("maat en schaal van het erf"); extra woning/splitsing wel. Wel expliciet zoeken naar uitbreiding in Kamperzeedijk (40 woningen tot 2030) en Zwartsluis, en in Mastenbroek "een beperkt aantal woningen" rond kerk/school/dorpshuis. Akkoord noemt CPO welwillend.
- **(b) Provinciaal [PB]:** Overijssels concentratiebeginsel (overige kern: lokale behoefte), woonafspraken West-Overijssel (80%/20%), BOPA-instemming bij nieuwe woningen Groene Omgeving, KGO; geen provinciale conflicten in nieuws gevonden.
- **(c) Eindoordeel:** Cluster van 10-12 woningen *in het open buitengebied*: kansarm. Cluster aansluitend aan Kamperzeedijk/Zwartsluis/Hasselt/Genemuiden als CPO: kansrijk maar afhankelijk van opname in Bouwsteen Ontwikkellocaties (voorkeurslocaties eind 2026) en netaansluiting. Belangrijkste onzekerheden: netcongestie, stikstof (Weerribben-Wieden/Zwarte Water), draagvlak.

### 2. Agrarische herbestemming: ruimte voor omzetting van agrarisch bestemde grond naar bouw-/woonfunctie op deze schaal?
- **(a) Gemeentelijk:** Alleen via herontwikkeling van bestaande agrarische bedrijven/erven; omzetting van onbebouwde agrarische grond niet, tenzij uitbreidingslocatie bij een kern. VAB-beleid nog in uitwerking.
- **(b) Provinciaal [PB]:** landbouwgebied-typologie en KGO-investering; verdere toets door deelonderzoek 2.
- **(c) Eindoordeel:** schaal 10-12 vraagt bijna zeker een kern-uitbreidingslocatie of grotere erftransformatie; informele toets bij wethouder Slingerland nu en inbreng in de Bouwsteen Ontwikkellocaties zijn de logische stappen.

---

## Bijlage A-controlepunten (Overijssel)

| # | Bevinding | Status | Bron | Waar te vinden bij 'niet gevonden' |
|---|---|---|---|---|
| A1 | Gemeente = "overige kern" [PB]; Omgevingsvisie: natuurlijke groei van kernen, regionale instroom meegeteld; Zwartewaterland deel Regio Zwolle/NOVEX | gevonden (deels) | CVDR767481; [PB] | verstedelijkingsstrategie Regio Zwolle (deelonderzoek 1/2) |
| A2 | West-Overijssel; 244 / 3-559 / 77 = gerealiseerd 2022-2024 / sleutelprojecten 2024-2030 / doorkijk 2031-35 [PB]; programma ±1.010 voor behoefte 775; 130%; Q1 2025 slechts 2 woningen; Planmonitor-positie CPO niet vastgesteld | gevonden (deels) | CVDR767481 §3.10; RTV Oost 24-4-2025 | Planmonitor Wonen provincie; gemeente (afdeling ruimtelijke ontwikkeling) |
| A3 | 30-40-30; sociale huur 30%; starterslening; lokaal aangescherpte grens niet gevonden; prestatieafspraken 2026-2029 | gevonden (deels) | CVDR767481; Genemuiden Actueel 28-11-2025 | prestatieafspraken op wetlandwonen.nl |
| A4 | Geen (ontwerp-)volkshuisvestingsprogramma gevonden; Bouwsteen wonen wordt daarin ingebracht; ladder toegepast door RvS 2024 op recreatiewoningen | niet gevonden | Bouwsteen p. 8 | gemeenteraad/RIS Zwartewaterland; deelonderzoek 1 |
| A5 | Woonzorgvisie 2026 aangekondigd; zorgwoningen Binnenveld ± 80; Tijlshof; huisvestingsverordening "nog op te stellen" | gevonden (deels) | Genemuiden Actueel 7-11-2025; CVDR767481 | woonzorgvisie (RIS) |
| B1 | Eigen KGO 2015 met rekenmodel ("rekenmodel [...] sloop-/terugbouw"), wordt geactualiseerd; beleidsregel extra woning (CVDR683809); beleidslijn inhoudsmaat woningen (CVDR745446: 600→750 m³, 900 m³ met KGO-investering). Formule zelf niet gelezen | gevonden (deels) | Bouwsteen p. 9-10; CVDR745446 | KGO 2015 document (gemeentesite/RIS) |
| B2 | Geen maximum aantal gevonden; "maatwerk ... passend bij de maat en schaal van het erf"; extra woning op erf: 2 woningen binnen één bouwvolume; "nieuw woonerf niet toegestaan" | gevonden | CVDR683809 art. 3; Bouwsteen p. 53 | — |
| B3 | KGO-actualisatie aangekondigd; omgevingsplan nog "Bestemmingsplan Buitengebied" (tijdelijk deel); beleidsrijke wijziging na Bouwsteen verwacht | gevonden | CVDR745446; Bouwsteen p. 5 | omgevingsplan op Regels op de kaart |
| B4 | Uitbreidingslocaties "bij de kernen" aangewezen via Bouwsteen Ontwikkellocaties; contour niet gelezen | niet gevonden (contour) | CVDR767481 | visie- en waardenkaart Omgevingsvisie |
| B5 | Ervenconsulent, beplantingsplan, aanvullende prestatie; gebiedsfonds ("bijdrage aan het gebiedsfonds") bij overschrijding inhoudsmaat; anterieure overeenkomst niet gevonden | gevonden (deels) | CVDR683809; CVDR745446 | KGO 2015 |
| C1 | Typologie niet in nieuws; Bouwsteen gebruikt eigen deelgebieden (9) | niet gevonden | — | verordening-viewer provincie (deelonderzoek 2/4) |
| C2 | Geen toepassing art. 4.124 lid 4 gevonden | niet gevonden | — | deelonderzoek 1/2 |
| C3 | Natura 2000 (Weerribben-Wieden, Olde Maten & Veerslootslanden), NNN, Nationaal Landschap IJsseldelta, Belvedère Polder Mastenbroek, windzoekgebied Genne-Holten, buitendijks; stikstof "strenge" (Landgoed Stroombeek) | gevonden (deels) | Bouwsteen p. 15-32; Zwartewaterkrant 12-6-2026 | provinciale kaartlagen |
| C4 | Netcongestie: Enexis-wachtlijst; ACM-prioritering per 1-7-2026; gemeentelijke volgordelijst (CVDR765999; 44 projecten); aanbetaling 20%; Binnenveld op wachtlijst, Om de Weede heeft stroom; "water en bodem sturend" in akkoord; OF-WAAR-HOE-standaardonderbouwing niet gevonden (ETFAL-handreiking wel genoemd) | gevonden | gemeentesite /netcongestie; CVDR765999; Genemuiden Actueel 17-7-2026 | ETFAL-handreiking (gemeentesite) |
| D1 | Betrokken bij programma VAB Noord-West Overijssel (Kampen, Staphorst, Steenwijkerland, Zwartewaterland, Zwolle); subsidie-aanvraag 4.39 niet gevonden | gevonden (deels) | Steenwijkerland B&W 18-6-2024 | provincie loket 4.39 |
| D2 | Erfcoach actief (Tjabringa); Atelier Overijssel/rijkshandreiking niet genoemd | gevonden | zwartewaterland.nl/erfcoaches | — |
| D3 | VAB-beleid in uitwerking; geen max woningen/VAB-erf; "past bij omliggende agrarische bedrijven" wel; collectief precedent: Tijlshof (kern) | gevonden (deels) | Bouwsteen p. 13; akkoord p. 19 | omgevingsplan-herziening |
| E1 | Accounthouder niet openbaar; provincie overleg 2x/jaar over verkeersknelpunten (akkoord p. 18); geen Omgevingstafel gevonden | niet gevonden | akkoord p. 18 | provincie Overijssel (voorkantsamenwerking) |
| E2 | Raad: bindend advies bij BOPA (CVDR718739); extra woning via omgevingsvergunning BOPA; doorlooptijd uit nieuws | gevonden (deels) | CVDR718739 | — |
| E3 | Uitzonderingenlijst-toepassing niet gevonden | niet gevonden | — | provincie |
| E4 | Geen provinciale zienswijzen/conflicten over woningbouw buitengebied 2023-2026; wel provincie ↔ raad over windturbines polder Mastenbroek (zienswijze 7-3-2024); RvS-uitspraken geen provinciaal element | niet gevonden (voor woningbouw) | Genemuiden Actueel 16-2 en 8-3-2024; raadvanstate.nl | Provinciaal blad (deelonderzoek 4) |
| F1 | Geen gebruik van provinciale regelingen in nieuws; wel: Verrijk je Wijk (gemeente, € 425.000) en provinciale subsidie voor inwonersinitiatief jeu-de-boules; "Overijssel trekt € 10 mln uit voor zorggeschikte en geclusterde woonvormen" (28-1-2025, algemeen) | niet gevonden | Genemuiden Actueel 28-1-2025 | Loket provincie (deelonderzoek 4) |

## Geverifieerde CVDR-nummers
Verificatie via SRU (zoekservice.overheid.nl, `dcterms.creator=Zwartewaterland`; creator-veld = overheidsorganisatie; 736 records) en kop van lokaleregelgeving.overheid.nl, 2026-10-11.

| Nummer | Organisatie volgens kop/SRU | Titel | Geldig |
|---|---|---|---|
| CVDR683809 | Zwartewaterland | Beleidsregel extra woning in het buitengebied van de gemeente Zwartewaterland | 18-11-2022 t/m heden |
| CVDR745446 | Zwartewaterland | Beleidslijn voor het afwijken van de inhoudsmaat van een woning in het buitengebied | 16-10-2025 t/m heden |
| CVDR738380 | Zwartewaterland | Beleidsregel woningsplitsing in Zwartewaterland (Gmb-2025-174054) | 8-4-2025 t/m heden |
| CVDR735559 | Zwartewaterland | Verordening Mobiliteitsfonds Zwartewaterland 2024 | 14-2-2025 t/m heden |
| CVDR765999 | Zwartewaterland | Beleidsregels eerder aanvragen transportcapaciteit woningbouwprojecten gemeente Zwartewaterland 2026 | 25-8-2026 t/m heden (niet verwarren met CVDR765864 Ommen en CVDR765519 Olst-Wijhe) |
| CVDR767481 | Zwartewaterland | Omgevingsvisie gemeente Zwartewaterland | 8-10-2026 t/m heden |
| CVDR718739 | Zwartewaterland | Adviesrecht Omgevingswet (raad 21-3-2024) | 26-4-2024 t/m heden |
| CVDR696513 | Zwartewaterland | Omgevingsplan gemeente Zwartewaterland | versie 2 vanaf 26-6-2024 |
| CVDR702877 | Zwartewaterland | Nota Grond- en Vastgoedbeleid 2023 | 19-10-2023 t/m heden |
| CVDR668202 | Zwartewaterland | Huisvesting van arbeidsmigranten in de gemeente Zwartewaterland | 1-1-2022 t/m heden |
| CVDR726980 / CVDR747704 | Zwartewaterland | Verordening leges 2025 / 2026 | 2025 / vanaf 2026 |
| CVDR748169 | Zwartewaterland | Beeldkwaliteitsplan Havezate Groot Terwee | 29-11-2025 |
| CVDR619790 | Zwartewaterland | Verordening Starterslening | v3 vanaf 30-3-2023 |
Niet toegeschreven: CVDR725503 (Oirschot), CVDR663985 (CPO-beleidsregels andere gemeente) uit zoekresultaten — andere gemeenten.

## Onzekerheden/tegenstrijdigheden
1. **CPO-intentie vs. restrictief beleid:** akkoord (SGP/BGZ) positief; Omgevingsvisie/Bouwsteen: geen nieuwe erven. Nog geen uitwerking (kaders met de raad).
2. **Termijn netcongestielijst:** nieuws "tot 1 augustus 2026"; CVDR765999 art. 5 "tot en met 22 augustus 2026". Beleidsregels gelden als leidend.
3. **Installatiedatum college:** gemeente 25-6-2026; zoekresultaat noemde 20 juni (waarschijnlijk 19/20 juni akkoord/presentatie) **[WF]**.
4. **Verkiezingsuitslag voorlopig;** opkomst 69,5% (AlleCijfers).
5. **Omgevingsvisie:** vastgesteld 1-10-2026 (gemeentenieuws), geldend vanaf 8-10-2026 (CVDR); bouwstenen (Ontwikkellocaties) nog niet toegevoegd; definitief voorjaar 2027.
6. **Bouwsteen Wonen (2022; update najaar 2024)**: de PDF-URL gaf geen document; inhoud alleen via zoeksamenvatting [WF]: niet gebruikt voor conclusies.
7. **Wethouder wonen vóór juni 2026** wisselde (Van der Poel CU, Rietman PvdA); huidige portefeuille bij Slingerland.
8. **Advertorials [ADV]** (CU, BGZ, "Alles over wonen in ...") zijn niet als feitelijke bron gebruikt.
9. Pagina's De Stentor/Dichtbij niet bereikbaar; mogelijk aanvullende berichten.
10. Beoordeling van kernvragen is voorlopig en moet met deelonderzoeken 1, 2 en 4 samengevoegd worden.
