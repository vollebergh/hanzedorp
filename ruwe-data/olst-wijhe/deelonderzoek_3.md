# Deelonderzoek 3: Nieuws en actualiteit 2024-2026, gemeente Olst-Wijhe (verificatieronde)

- **Raadplegingsdatum:** 2026-10-04 (alle bronnen hieronder zijn op die datum zelf geopend: curl/WebFetch, HTML gestript of PDF via pdfplumber geëxtraheerd).
- **Brontype:** regionale nieuwsmedia (Salland1, Salland Centraal, Wijhe City, HierinSalland/De Sallandse Geus, herxen.nl, Nieuwe Oogst, Bouwen in het Oosten), gemeentelijke nieuwsberichten en woonnieuws, en de bijbehorende gemeentelijke stukken die in die berichten worden aangehaald (bestuursakkoord, volgordelijst netcongestie, B&W-besluitenlijsten, proces-verbaal verkiezingsuitslag).
- **Werkwijze en vindplaatsen:**
  - Gemeentelijk nieuws: het volledige nieuwsarchief 2024 t/m 1-10-2026 (727 berichten) is gedownload via `https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/archive.csv`. Het woonnieuws (170 berichten, 2017 t/m 19-8-2026) via `https://wonen.olst-wijhe.nl/woonnieuws/woonnieuws/archive.csv`. De B&W-besluitenlijsten (113 lijsten, 9-1-2024 t/m 22-9-2026) via `https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/archive.csv`. Citaten uit deze archieven noemen titel en publicatiedatum. **Let op:** veel losse bericht-URL's uit het concept (bijv. `.../nieuwsberichten/2026/6/2/gezamenlijke-visie-voor-woningbouw-in-herxen`, `.../2026/5/19/resultaten-inwonerpanel...`, `wonen.olst-wijhe.nl/woonnieuws/woonnieuws/2026/2/6/...`) gaven op 2026-10-04 een **404**. De inhoud staat wel in de archiefbestanden. Werkende URL's zijn waar mogelijk vermeld.
  - Regionale media (WordPress-sites): doorzocht via hun REST-API (`/wp-json/wp/v2/posts?search=…&after=…`) op o.a. "wethouder", "Olst-Wijhe Vooruit", "Pro Olst-Wijhe", "formateur", "verkenner", "Boerhaar", "Herxen", "Elshof", "Klimboom", "Olstergaard", "CPO", "collectief", "tiny", "woningsplitsing", "KGO", "erfcoach", "Brinkweiden", "Wijlandhof", "Kappeweg". Elk aangehaald artikel is daarna volledig gelezen.
  - De Stentor: **niet toegankelijk** (WebSearch weigert het domein; betaalmuur). RTV Oost/Oost: alleen via zoeken, geen relevant bericht over 2026.
- **Hoofdconclusies in één oogopslag:**
  1. **Op 2026-10-04 is er géén coalitie in vorming.** College GB-CDA-VVD (11 van 17 zetels) is geïnstalleerd op 16-6-2026 en was voltallig aanwezig bij B&W op 22-9-2026. Er is geen wethoudersontslag, motie van wantrouwen of fractiebreuk gevonden. De enige "wijziging" is een **naamswijziging van de oppositie: Pro Olst-Wijhe heet sinds 23-6-2026 "Olst-Wijhe Vooruit"** (GL/PvdA/D66, 6 zetels).
  2. **Tegenstrijdigheid 10 (verkiezingscijfers) is opgelost** met het proces-verbaal P 22-2: 9.244 stemmen op kandidaten, 9.325 uitgebrachte stemmen, 15.511 kiesgerechtigden, opkomst 60,1%.
  3. **Engeweg/Elshof telt wél op tot 8** (3 twee-onder-een-kapwoningen = 6 woningen, plus 2 vrijstaande) → tegenstrijdigheid 19 opgelost.
  4. **Grote omissies in het concept** (CPO-relevant): **CPO Boerhaar** (vereniging opgericht 3-7-2025, circa 22-24 woningen op de vrijkomende schoollocatie plus Boerhaar 18/18a, kredietvoorstel € 1,1 mln aan de raad, raad 26-5-2026); **Erveweg/Hemelrijk-2 Welsum** (circa 18 koopwoningen van grondeigenaren op grond met agrarische bestemming aan de rand van Welsum, principebesluit B&W 10-3-2026); **'t Kleiland, Kleistraat Olst** (20 woningen op grond met agrarische bestemming, BOPA verleend B&W 17-3-2026); **Grolleman Herxen 63** (15 woningen); het **buurtschappenbeleid Herxen/Elshof** (provinciaal concept uit 2004, lokaal 2007/2010/2020); **De Brinkweiden, Kappeweg 18 (12 woningen, "Buitengebied")** en **Wijlandhof, Elshof (12 woningen)** op de volgordelijst netcongestie; een **boer die op bijna 6.000 m2 vrijkomende agrarische grond ouderenhuurwoningen wil bouwen** (juli 2026); het inwonerpanel (25% animo voor zelfbouw); en de motie die de raad aannam om meer aandacht te geven aan bouwinitiatieven van inwoners (11 tegen 6).
  5. **De Gemeenteblad-nummers voor netcongestie in het concept (gmb-2026-415179 en gmb-2026-421329) zijn van Brunssum en Lansingerland.** De juiste nummers zijn **Gmb 2026, 385444** (beleidsregels, 13-8-2026) en **Gmb 2026, 422235** (voorlopige volgordelijst, 10-9-2026).
  6. **Portefeuilles volgens het bestuursakkoord:** *Grondbeleid (wonen en bedrijven)* en *Toekomstbestendige kernen en buitengebied* liggen bij **Hans Olthof (VVD)**; *Wonen* en *Ruimtelijke ordening en omgevingsplannen* bij **Marcel Blind (GB)**.

---

## Prioriteit 1: Coalitie, formatie, uitslag, college en bestuursakkoord (§10)

### 1.1 Is er op 2026-10-04 een coalitie in vorming? Nee.

**Bevinding.** Ik heb het gemeentelijk nieuwsarchief, de B&W-besluitenlijsten en vier regionale nieuwssites over de periode 16-6 t/m 4-10-2026 doorzocht. Er is geen bericht over een coalitiecrisis, wethoudersontslag, motie van wantrouwen, fractiebreuk of collegewijziging. Positieve aanwijzingen dat het college ongewijzigd functioneert:

> "Aanwezig
> Mevrouw S.A.E. Poepjes, burgemeester;
> de heer S. van den Berg, gemeentesecretaris;
> de heer M. Blind, wethouder;
> de heer H. Olthof, wethouder;
> de heer H. Engberink, wethouder."

— Bron: B&W besluiten 22-09-2026 (gepubliceerd 28-9-2026), https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/b-amp-w-besluiten-22-09-2026 (via archive.csv) (geraadpleegd 2026-10-04)

> "Twaalf jaar dezelfde coalitie, elf van de zeventien zetels en één oppositiepartij."

— Bron: De Sallandse Geus Olst-Wijhe: Wegen zonder te zeggen, HierinSalland, 15-9-2026, https://hierinsalland.nl/de-sallandse-geus-olst-wijhe-wegen-zonder-te-zeggen/ (geraadpleegd 2026-10-04)

> "Gemeente Olst-Wijhe verwacht vanaf 2027 jaarlijks ongeveer 1,4 miljoen euro meer uit te geven dan er binnenkomt. […] Wethouder financiën, Hans Olthof: 'Door bewust keuzes te maken én te blijven investeren houden we de basis op orde. […]'"

— Bron: Olst-Wijhe verwacht structureel tekort van 1,4 miljoen, Salland Centraal, 9-9-2026, https://www.sallandcentraal.nl/2026/09/olst-wijhe-verwacht-structureel-tekort-van-14-miljoen/ (geraadpleegd 2026-10-04)

**Enige "wijziging": naamswijziging van de oppositiepartij (geen breuk).**

> "De lokale politieke samenwerking van GroenLinks, PvdA en D66 in Olst-Wijhe gaat verder onder de naam Olst-Wijhe Vooruit. De naamswijziging volgt op het besluit van de landelijke partijen GroenLinks en PvdA om gezamenlijk verder te gaan onder de naam PRO."

— Bron: Pro Olst-Wijhe verandert naam in Olst-Wijhe Vooruit, Salland1, 23-6-2026, https://www.salland1.nl/pro-olst-wijhe-verandert-naam-in-olst-wijhe-vooruit/ (geraadpleegd 2026-10-04); zelfde strekking: https://www.sallandcentraal.nl/2026/06/pro-olst-wijhe-gaat-verder-als-olst-wijhe-vooruit/

**Spanningen die geen crisis zijn (duiding voor §10):**
- De verkenner constateerde verstoorde verhoudingen. Op het besluit om de grootste partij uit te sluiten kwam veel kritiek (petitie, ingezonden brieven, kritische columns van "De Sallandse Geus" over een "Haagse achterkamer"). Die kritiek leidde niet tot een crisis.
- De coalitie stemt niet als blok:

> "Gemeentebelangen diende diezelfde avond een amendement in over vastgoedmanagement binnen de bestaande formatie. Verworpen. Tegen stemden CDA, VVD en Olst-Wijhe Vooruit. […] Dit is geen raad van twee blokken. Dit is een raad die per onderwerp opnieuw gaat zitten."

— Bron: De Sallandse Geus Olst-Wijhe: Wiens profiel verbleekte?, HierinSalland, 16-8-2026, https://hierinsalland.nl/de-sallandse-geus/ (geraadpleegd 2026-10-04). *Opiniestuk; de genoemde stemmingen (raad 29-6-2026) zijn niet in de besluitenlijst zelf gecontroleerd.*

- In juni 2026 nam de raad tegen het advies van het college in een motie aan over bouwinitiatieven van inwoners. Deze motie is direct CPO-relevant:

> "Onze motie, waarin wij het college oproepen om méér en betere aandacht te schenken aan (bouw) activiteiten uit de samenleving, haalde het. Die motie hadden wij gemaakt naar aanleiding van de stevige kritiek van de Boskamp, van de Boerhaar en uit Wesepe op B. en W. Het college herkende zich niet in die kritiek – komt vaker voor – en ontraadde de motie. Mooi niet, zo vond de raad en met 11 tegen 6 stemmen werd de motie aanvaard. Naast mijn fractie stemden ook voltallige VVD fractie en twee van de drie CDA raadsleden vóór."

— Bron: Onze Man in Wijhe Toon Schuiling (column van raadslid Olst-Wijhe Vooruit), HierinSalland, 13-6-2026, https://hierinsalland.nl/onze-man-in-wijhe-toon-schuiling-6/ (geraadpleegd 2026-10-04). *Datum van de raadsvergadering en motietitel niet in de column; zoeken in iBabs.*

- Context, geen crisis: in de enquête van Salland1/HierinSalland (juni 2026) over een mogelijke **fusie van Raalte en Olst-Wijhe** waren 148 respondenten voor en 147 tegen (https://hierinsalland.nl/enquete-uitslag-sallanders-tot-op-het-bot-verdeeld-over-fusie-raalte-en-olst-wijhe/, 5-8-2026). Een bestuurlijk fusietraject is niet gevonden.

**Correctie op het concept (§10, eerste alinea):** wijzig "Coalitie in vorming op 2026-10-02: nee (voor zover vast te stellen)" in: **"Coalitie in vorming op 2026-10-04: nee.** Het college GB-CDA-VVD is sinds 16-6-2026 geïnstalleerd en was voltallig aanwezig in de B&W-vergadering van 22-9-2026. In het gemeentelijk nieuwsarchief en de regionale media (Salland1, Salland Centraal, Wijhe City, HierinSalland) zijn tussen 16-6 en 4-10-2026 geen berichten gevonden over een crisis, ontslag, motie van wantrouwen of fractiebreuk. De oppositiepartij heet sinds 23-6-2026 Olst-Wijhe Vooruit (voorheen Pro Olst-Wijhe)." Vervang overal "Pro Olst-Wijhe" door "Olst-Wijhe Vooruit (tot juni 2026 Pro Olst-Wijhe; kandidatenlijst 'GroenLinks / PvdA / D66')". Voeg toe dat de oppositie (6 zetels) en twee coalitiepartijen in juni 2026 tegen het collegeadvies in een motie aannamen voor meer aandacht voor bouwinitiatieven van inwoners. Dat is een relevant signaal voor CPO.

### 1.2 Formatiechronologie (geverifieerd)

| Datum | Gebeurtenis | Bron (geraadpleegd 2026-10-04) |
|---|---|---|
| 9-3-2026 | Lijsttrekkers van GB, CDA, VVD en Pro Olst-Wijhe tekenen een formatieprotocol ("de grootste partij neemt het voortouw") | HierinSalland, 19-4-2026, https://hierinsalland.nl/haagse-achterkamer-olst-wijhe/ (opiniestuk) |
| 18-3-2026 | Verkiezingen; voorlopige opkomst 60,11% | Gemeente, "Voorlopige uitslag gemeenteraadsverkiezingen 2026", 18-3-2026 (archive.csv) |
| 26-3-2026 | Centraal stembureau stelt de definitieve uitslag vast | https://www.olst-wijhe.nl/bestuur/verkiezingen/gemeenteraadsverkiezingen-2026/definitieve-uitslag-gemeenteraadsverkiezingen-2026 |
| 31-3-2026 | Installatie nieuwe raad en duidingsdebat | Gemeente, "Reactie lijsttrekkers op uitslag verkiezingen Olst Wijhe", 23-3-2026 (archive.csv) |
| 7-4-2026 | Hester Scholten verkenner | https://hierinsalland.nl/hester-scholten-verkenner-in-olst-wijhe/ (titel) |
| 12-4-2026 | Verslag verkenner (volgens HierinSalland) | https://hierinsalland.nl/de-sallandse-geus/ |
| 17-4-2026 | Gemeentebericht: GB-CDA-VVD "enige combinatie" | https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/2026/4/17/coalitie-gemeentebelangen-cda-en-vvd-meest-kansrijke-richting-formatiegesprekken-starten-binnenkort (200) |
| 24-4-2026 | Ellen Nauta-van Moorsel (burgemeester Hof van Twente) formateur; start 28-4 | https://wijhecity.nl/2026/04/24/ellen-nauta-van-moorsel-aangesteld-als-formateur-in-olst-wijhe/ |
| 12-6-2026 | Datering van het bestuursakkoord ("Olst-Wijhe, 12 juni 2026") | Bestuursakkoord p. 5 |
| 16-6-2026 | Ondertekening, aanbieding en installatie wethouders (15 van 15 aanwezige stemmen per wethouder) | Gemeente 15-6 en 19-6-2026; HierinSalland 16-8-2026 |
| 23-6-2026 | Pro Olst-Wijhe heet voortaan Olst-Wijhe Vooruit | Salland1 / Salland Centraal 23-6-2026 |

Kerncitaten:

> "Uit de gesprekken van verkenner Hester Scholten met alle fracties blijkt dat een samenwerking tussen Gemeentebelangen Olst-Wijhe, CDA en VVD op dit moment de enige combinatie is die door de betrokken partijen als haalbaar en constructief wordt gezien. Hoewel GroenLinks/PvdA/D66 als grootste partij heeft aangegeven open te staan voor inhoudelijke gesprekken, is tijdens de verkenning naar voren gekomen dat er bij zowel Gemeentebelangen Olst-Wijhe, het CDA als de VVD op dit moment te weinig ruimte wordt gezien om dergelijke gesprekken te voeren […]. De verkenner merkt tot slot op dat het versterken van onderling vertrouwen en een respectvolle samenwerking binnen de raad wenselijk is […]."

— Bron: Coalitie Gemeentebelangen, CDA en VVD meest kansrijke richting; formatiegesprekken starten binnenkort, gemeente Olst-Wijhe, 17-4-2026, URL hierboven (geraadpleegd 2026-10-04)

> "Gemeentebelangen Olst-Wijhe, CDA en VVD hebben unaniem gekozen voor drs. Ellen Nauta-van Moorsel om het proces te begeleiden. Nauta is sinds 2013 burgemeester van de gemeente Hof van Twente […]. De formatie gaat officieel van start op dinsdag 28 april […]."

— Bron: Wijhe City, 24-4-2026, URL hierboven (geraadpleegd 2026-10-04)

> "De onderhandelaars van de politieke partijen van Gemeentebelangen Olst-Wijhe, CDA en VVD ondertekenen op dinsdag 16 juni om 20.00 uur in de raadszaal van het gemeentehuis in Wijhe het bestuursakkoord 'Betrouwbaar en bestendig: de basis op orde'. Daarna overhandigt formateur Ellen Nauta het akkoord aan de voorzitter van de raad, burgemeester Sietske Poepjes. Vervolgens vindt de installatie van de wethouders plaats."

— Bron: Bestuursakkoord Olst-Wijhe op dinsdag 16 juni ondertekend en aangeboden, gemeente, 15-6-2026 (archive.csv) (geraadpleegd 2026-10-04)

> "Pro Olst-Wijhe deed niet mee aan de coalitieonderhandelingen. Zij staat niet achter het akkoord. Met de presentatie werden ook meteen de wethouders geïnstalleerd, dit zijn opnieuw Marcel Blind, Hans Olthof en Herman Engberink."

— Bron: Coalitieakkoord en installatie wethouders Olst-Wijhe: "Minder plannen, minder papier en meer doen", Salland1, 19-6-2026, https://www.salland1.nl/coalitieakkoord-en-installatie-wethouders-olst-wijhe-minder-plannen-minder-papier-en-meer-doen/ (geraadpleegd 2026-10-04)

**Correctie §10-tabel:** de datum "april 2026 (advies 17-4)" is de datum van het gemeentebericht. Het verkennersverslag is volgens HierinSalland van 12-4-2026 (verslag zelf niet gezien). Voeg toe: formatie gestart 28-4-2026; akkoord gedateerd 12-6-2026. Context: Herman Engberink (CDA) was al sinds 26-11-2025 interim-wethouder als opvolger van Judith Compagner ("Herman Engberink aangedragen als nieuwe (interim) wethouder", gemeente, 17-10-2025). Compagner was portefeuillehouder voor de Omgevingsvisie.

### 1.3 Definitieve uitslag 18-3-2026 (tegenstrijdigheid 10 opgelost)

> "Het centraal stembureau heeft op 26 maart 2026 tijdens de openbare zitting de definitieve uitslag vastgesteld. De 17 zetels in de gemeenteraad zijn als volgt verdeeld: GroenLinks / PvdA / D66 3.002 [stemmen] 6 [zetels]; Gemeentebelangen Olst-Wijhe 2.821 5; CDA 1.733 3; VVD 1.688 3."

— Bron: Definitieve uitslag, gemeente Olst-Wijhe, URL hierboven (geraadpleegd 2026-10-04)

Uit het **proces-verbaal P 22-2** (PDF-bijlage op dezelfde pagina, scan met OCR; metadata 26-3-2026):

> "15511 Kiesgerechtigden […] 8620 Stempassen / 703 Volmachtbewijzen […] 9323 Totaal toegelaten kiezers (A+B) […] Stemmen op kandidaten 9244 / Ongeldige stemmen 19 / Totaal uitgebrachte stemmen 9325"

— Bron: Proces-verbaal P 22-2 verslag, uitslag en zetelverdeling, https://www.olst-wijhe.nl/bestuur/verkiezingen/gemeenteraadsverkiezingen-2026/definitieve-uitslag-gemeenteraadsverkiezingen-2026/proces-verbaal-p-22-2-verslag-uitslag-en-zetelverdeling (geraadpleegd 2026-10-04). De OCR mist de regel met blanco stemmen; afgeleid: 9.325 − 9.244 − 19 = **62 blanco** [INT].

**Correctie (§10 en tegenstrijdigheid 10):** 3.002 + 2.821 + 1.733 + 1.688 = **9.244 stemmen op kandidaten**. Dit klopt precies met het proces-verbaal. Het getal "9.242 uitgebracht" in het concept is fout. Totaal uitgebrachte stemmen 9.325; kiesgerechtigden 15.511; opkomst **60,1%** (9.325/15.511 = 60,12%; de voorlopige gemeentelijke opkomst was 60,11%). De "59,6%" in het concept is 9.244/15.511, dus het aandeel geldige stemmen op kandidaten en niet de opkomst. **Status: opgelost.**

### 1.4 College en portefeuilles (tegenstrijdigheid 18 opgelost; correctie §9/§10)

Bestuursakkoord p. 23, "Portefeuilleverdeling Olst-Wijhe 2026-2030" (letterlijk, per kolom geëxtraheerd):

> "Wethouder en 1e loco-burgemeester Marcel Blind • Wonen (inclusief huisvesting vluchtelingen) • Duurzaamheid (inclusief milieu, afval, energietransitie) • Openbare ruimte (inclusief klimaatadaptatie, water binnendijks) • Mobiliteit (openbaar vervoer, verkeersveiligheid) • Monumenten • Ruimtelijke ordening en omgevingsplannen • Kernenwethouder: Olst, Eikelhof, Herxen, Middel"
>
> "Wethouder en 3e loco-burgemeester Hans Olthof • Financiën • Economische ontwikkeling (inclusief detailhandel, werklocaties en bedrijventerreinen) • Toekomstbestendige kernen en buitengebied • Water buitendijks (inclusief Hoogwaterbeschermingsprogramma en Kaderrichtlijn water) • Vrijetijdseconomie (recreatie en toerisme) • Dienstverlening • Grondbeleid (wonen en bedrijven) • Evenementenbeleid • Gebiedsgerichte aanpak • Regio Zwolle • Kernenwethouder: Wesepe, Elshof, Marle, Welsum"
>
> "Wethouder en 2e loco-burgemeester Herman Engberink • Sociaal domein (Jeugdzorg en Wmo) • Volksgezondheid • Beschermd wonen en maatschappelijke opvang • Vluchtelingenopvang (welzijn) • Werk en inkomen […] • Sport & Cultuur • Maatwerk vervoer • Onderwijs(huisvesting) • Maatschappelijk vastgoed en vitale voorzieningen • Kernenwethouder: Wijhe, Boerhaar, Boskamp, Den Nul"
>
> "Burgemeester - Sietske Poepjes • Algemene bestuurlijke zaken en coördinatie • Openbare orde en veiligheid • Omgevingsdienst • Communicatie en participatie […]"

— Bron: Bestuursakkoord 2026-2030 "Betrouwbaar en bestendig: de basis op orde", https://www.olst-wijhe.nl/bestuursakkoord-1/bestuursakkoord-olst-wijhe-2026-2030 (PDF, 24 p.; gelinkt vanaf https://gemeenteraad.olst-wijhe.nl/bestuursakkoord) (geraadpleegd 2026-10-04)

**Correcties:**
- §10-tabel college: Blind = "Wonen; ruimtelijke ordening en omgevingsplannen; duurzaamheid; openbare ruimte; mobiliteit; monumenten". **Niet** "woon- en grondbeleid": **grondbeleid ligt bij Olthof**. Olthof = "financiën; economie; *toekomstbestendige kernen en buitengebied*; water buitendijks; recreatie; *grondbeleid (wonen en bedrijven)*; *gebiedsgerichte aanpak*; *Regio Zwolle*". Engberink: zoals in het concept, plus maatschappelijk vastgoed en onderwijshuisvesting.
- §3(e) "Concrete vervolgstap" en §9: voor een CPO op agrarische grond zijn **twee wethouders** aanspreekpunt. Blind (wonen, RO en omgevingsplannen) en **Olthof (buitengebied, grondbeleid, gebiedsgerichte aanpak)**. Daarnaast de kernenwethouder van de betreffende kern (zie tabel hierboven).
- Tegenstrijdigheid 18: **opgelost** (portefeuille volgens het akkoord van juni 2026).
- Tegenstrijdigheid 9 (aantal kernen): de kernenwethouder-indeling in het akkoord noemt **12 kernen/dorpen**: Olst, Eikelhof, Herxen, Middel, Wesepe, Elshof, Marle, Welsum, Wijhe, Boerhaar, Boskamp en Den Nul. Ook HierinSalland citeert Gemeentebelangen: "Olst-Wijhe kent twaalf sterke en leefbare kernen" (9-1-2026). **Opgelost: 12** (bestuurlijke indeling). Het getal 7 is waarschijnlijk een CBS-statistische indeling [INT].
- A1-aanvulling: "Regio Zwolle" is expliciet een portefeuille (Olthof). De gebiedsaanpak Wesepe wordt ingediend bij de "Regio Deal Regio Zwolle II" (B&W 22-4-2025). Dit wijst op lidmaatschap van Regio Zwolle, maar het lidmaatschap zelf is niet in een bron bevestigd.

### 1.5 Bestuursakkoord: passages over wonen, buitengebied, CPO, "+400" en Wesepe

> "De afgelopen jaren lag onze focus nadrukkelijk op Wonen. We liggen op koers met de realisatie van onze ambitie om 1.000 tot 1.200 woningen te bouwen tot en met 2031. Er zijn in de afgelopen bestuursperiode bijna 450 woningen gerealiseerd. De volgende periode zit er opnieuw groei in het aantal op te leveren nieuwbouwwoningen in de gemeente." (p. 6)

> "Wonen: van huis naar thuis […] De afgelopen jaren laten zich op woongebied het beste omschrijven als: bouwen, bouwen, bouwen. Deze nieuwe bestuursperiode gaan we hier mee verder. […] WAT WILLEN WE BEREIKEN? • Het realiseren van woningen blijft een speerpunt. In deze periode streven we naar gemiddeld 100 woningen per jaar er bij, dus in totaal zo'n 400 nieuwe woningen. • We zetten wonen in als instrument. […] • We willen voldoen aan de vraag vanuit starters, senioren en zorgvragers door passende woningen te bouwen.
> WAT GAAN WE DAARVOOR DOEN? • We ontwikkelen een Volkshuisvestingsprogramma. • We ontwikkelen Wesepe verder als derde kern in Olst-Wijhe met daarbij passende faciliteiten en voorzieningen. • We zetten maximaal in op het bouwen van woningen die passen bij de lokale vraag. • We houden vast aan het uitgangspunt dat 70% van de nieuw te bouwen woningen betaalbaar zijn: sociale- en middenhuur en goedkope of betaalbare koop. • We werken actief samen met de woningcorporatie(s)." (p. 8)

> "Toekomstbestendige kernen en buitengebied […] WAT GAAN WE DAARVOOR DOEN? • We willen in gebiedsontwikkelingen onze koers per kern of gebied vastleggen. In thematische beleidsplannen leggen we (inrichtings)keuzes vast waar meer duidelijkheid op nodig is. Als er al plannen ontwikkeld of vastgelegd zijn, gaan we daar op verder. • We zetten in op een groene, klimaatadaptieve leefomgeving. • We ondersteunen programma's en projecten die bijdragen aan toekomstbestendige kernen en het buitengebied. • We adviseren boeren die hun bedrijf willen transformeren of willen stoppen." (p. 9)

> "De ruimtelijke en maatschappelijke ontwikkeling van Wesepe als derde grote kern pakken we deze bestuursperiode verder op." (p. 4)

— Bron: Bestuursakkoord 2026-2030, URL hierboven (geraadpleegd 2026-10-04)

**De akkoordtekst doorzocht op CPO-termen:** "CPO", "collectie(f)", "zelfbouw", "tiny", "opdrachtgever", "experiment", "woonvorm", "erf", "VAB", "binding" en "kleinschalig" komen **niet** voor.

Persbericht van de gemeente:

> "De drie coalitiepartijen geloven erin dat inwoners meer hebben aan een woning die daadwerkelijk gebouwd wordt dan aan een extra visie over woningbouw." […] "Concreet betekent dit onder andere: Blijvende inzet op woningbouw: +400 woningen; Sterke voorzieningen in alle kernen en dorpen […]; Meer recreatiemogelijkheden langs de IJssel; […]" […] "De wethouders Marcel Blind (GB, ruimtelijk domein en wonen), Herman Engberink (CDA, sociaal domein, sport & cultuur) en Hans Olthof (VVD, financiën, IJssel en buitengebied) werden gisteravond door een unanieme raad benoemd […]."

— Bron: Bestuursakkoord Olst-Wijhe: nadruk op uitvoerbaarheid en dichtbij inwoners, gemeente, 19-6-2026 (archive.csv) (geraadpleegd 2026-10-04)

Kritiek van de oppositie (Pro Olst-Wijhe, kort vóór de naamswijziging):

> "'Als dezelfde partijen al twaalf jaar besturen, dan is het logisch om te vragen waarom die basis nu pas op orde moet worden gebracht,' aldus fractievoorzitter André Smit. […] Tegelijkertijd ziet Pro Olst-Wijhe positieve punten in het akkoord, zoals de aandacht voor leefbaarheid en sterke kernen."

— Bron: HierinSalland, 25-6-2026, https://hierinsalland.nl/pro-olst-wijhe-stelt-vragen-bij-titel-bestuursakkoord/ (geraadpleegd 2026-10-04)

**Correcties §10 "Bestuursakkoord 2026-2030":**
- Het akkoord is gelezen. URL: `https://www.olst-wijhe.nl/bestuursakkoord-1/bestuursakkoord-olst-wijhe-2026-2030`. De concept-URL `gemeenteraad.olst-wijhe.nl/bestuursakkoord` is een overzichtspagina met een link.
- **"+400 woningen"** betekent volgens het akkoord: "gemiddeld 100 woningen per jaar er bij, dus in totaal zo'n 400 nieuwe woningen" in de periode 2026-2030. Het hoort bij de ambitie "1.000 tot 1.200 woningen te bouwen **tot en met 2031**". Gemeentelijke berichten zeggen "tot 2032".
- **Wesepe:** p. 4 "derde grote kern", p. 8 "derde kern".
- **Buitengebied/CPO:** het akkoord bevat **geen** passage over CPO, collectieve of experimentele woonvormen of agrarische herbestemming. Wel: koers per kern of gebied vastleggen in gebiedsontwikkelingen, "We adviseren boeren die hun bedrijf willen transformeren of willen stoppen", "woningen die passen bij de lokale vraag", 70% betaalbaar en een Volkshuisvestingsprogramma. De zin "Passages over buitengebied, CPO … niet gevonden (alleen via de akkoordtekst te controleren)" kan worden vervangen door: "gecontroleerd in de akkoordtekst: geen vermelding van CPO of collectief wonen".
- Het motto "minder papier, méér doen" komt van GB-fractievoorzitter Ronnie Niemeijer (gemeentebericht 19-6). De kop "Minder plannen, minder papier en meer doen" is van Salland1.
- **Politieke duiding [INT]:** de partijen die CPO in de raad actief aankaarten (Toon Schuiling, PvdA/Olst-Wijhe Vooruit: schriftelijke vragen over CPO Boerhaar en de motie over bouwinitiatieven uit de samenleving) zitten in de oppositie. De motie kreeg echter steun van de VVD en van twee CDA-raadsleden. Het draagvlak voor bottom-up-initiatieven is daarmee breder dan de oppositie. Wethouder Blind (GB) presenteert lokale initiatieven op agrarische grond zelf positief (Elshof, Welsum, Herxen: "Elke woning telt").

---

## Prioriteit 2: Praktijkvoorbeelden (§3b, §6, §7)

### 2.1 Engeweg, Elshof: 8 woningen (tegenstrijdigheid 19 opgelost)

> "BESLUIT In te stemmen met: In principe (en onder voorwaarden) medewerking verlenen aan het verzoek tot wijziging van de functie van agrarisch naar wonen en realisatie van 8 woningen (3 tweekappers en 2 vrijstaande) conform inrichtingsschets met als doel kopers te vinden met een binding met de Elshof; Het verder in procedure brengen van de formele aanvraag middels een omgevingsvergunning voor een buitenplanse omgevingsplanactiviteit (BOPA) mits wordt voldaan aan een evenwichtige toedeling van functies aan deze locatie (Etfal); Er wordt een anterieure overeenkomst opgesteld die door de initiatiefnemer moet worden ondertekend; Het erfinrichtingsplan van Het Oversticht dient nader te worden uitgewerkt en akkoord bevonden door de gemeente; Het participatieproces dient voortgezet te worden […]. In te stemmen met een verkleining van de normafstand met betrekking tot spuitzonering op basis van het opgestelde locatiespecifiek onderzoek.
> SAMENVATTING Er is een principeverzoek ingediend voor de realisatie van 8 woningen (3 twee-onder-één-kap en 2 vrijstaande) op twee percelen aan de Engeweg, direct ten zuidoosten van buurtschap Elshof. Het plan voorziet in een dorpsuitbreiding die aansluit bij de woningbehoefte in Elshof en draagt bij aan de leefbaarheid van het buurtschap. Het verzoek is in strijd met het Omgevingsplan Olst-Wijhe, waarin de functie 'Agrarisch' geldt."

— Bron: B&W besluiten 03-02-2026, agendapunt 14 (gepubliceerd 9-2-2026; archive.csv) (geraadpleegd 2026-10-04)

> "Het college van burgemeester en wethouders van Olst-Wijhe heeft ingestemd met een lokaal initiatief voor de bouw van acht nieuwe woningen op De Elshof eind 2026. Het gaat om drie twee onder een kapwoningen en twee vrijstaande woningen aan de Engeweg, aan de zuidoostkant van het dorp. […] De gemeente zet de komende jaren sterk in op kleinschalige projecten. 'Die zijn belangrijk voor de leefbaarheid in onze kernen en leveren samen een flinke bijdrage aan onze woningopgave: richting 2030 willen we 1000 tot 1200 woningen realiseren. Elke woning telt.' […] De initiatiefnemers zijn grondeigenaren Hans Dijk en Gino Schrijver. […] Tijdens een ledenvergadering van Plaatselijk Belang Elshof haalden zij wensen op bij dorpsbewoners […]."

— Bron: College Olst-Wijhe stemt in met bouw acht woningen op De Elshof, Salland1, 9-2-2026, https://www.salland1.nl/college-olst-wijhe-stemt-in-met-bouw-acht-woningen-op-de-elshof/ (geraadpleegd 2026-10-04). Gemeentelijk woonnieuws "Extra woningen dankzij lokaal initiatief de Elshof", 6-2-2026 (archive.csv), met dezelfde inhoud: "voor het jaar 2032 zo'n 1000 tot 1200 woningen realiseren. Want elke woning is er één!"

Op de definitieve volgordelijst netcongestie: "Engeweg Elshof | Engeweg | 2027 | [projectrijpheid] 6 | 8 [woningen] | Elshof".

**Correctie §3b/§6/§7:** "3 twee-onder-een-kapwoningen en 2 vrijstaande woningen volgens de zoeksamenvatting, wat niet optelt tot 8" moet worden: **3 twee-onder-een-kapwoningen (= 6 woningen) + 2 vrijstaande = 8**. Aanvullen: grondeigenaren Hans Dijk en Gino Schrijver; erfinrichtingsplan door Het Oversticht; **verkleining van de normafstand voor spuitzonering op basis van locatiespecifiek onderzoek** (een precedent voor art. 4.124 en de landbouw-woonfunctie-spanning); beoogde bouw "eind 2026" (Salland1) of start bouw 2027 (volgordelijst). Projectrijpheid 6 op de volgordelijst betekent "andere bewijsstukken": er was op dat moment nog geen civielrechtelijke overeenkomst of vergunning. Of de provincie al heeft ingestemd: **niet gevonden**. **Tegenstrijdigheid 19: opgelost.**

### 2.2 CPO Boerhaar: ontbreekt in het concept, zeer relevant

> "BOERHAAR – Op donderdag 3 juli is de vereniging CPO Boerhaar officieel opgericht door Mark Journee, Sem Schutte, Chris Beltman, Gerard Slinkman, Ben van den Berg en Koen Jansen. […] De kersverse vereniging heeft tot doel om een woningbouwproject te realiseren voor haar leden op de vrijkomende schoollocatie op de Boerhaar. Dit in samenwerking met de gemeente Olst-Wijhe, die na het vertrek van Mijnplein in januari 2027 eigenaar wordt van de schoollocatie. Door tussenkomst van de CPO-vereniging kan worden geregeld dat de woningen in dit project terechtkomen bij mensen die sociaal of economische binding met de Boerhaar hebben. […] 'in tegenstelling tot de vrijkomende schoollocatie aan de Stationsweg in Wijhe, is er voor het project in de Boerhaar nog geen gemeentelijk projectleider aangesteld en heeft de gemeenteraad nog geen voorbereidingskrediet beschikbaar gesteld'."

— Bron: CPO Boerhaar officieel opgericht, Salland Centraal, 14-7-2025, https://www.sallandcentraal.nl/2025/07/cpo-boerhaar-officieel-opgericht/ (geraadpleegd 2026-10-04)

> "Inmiddels is er op de Boerhaar een enthousiaste vereniging Collectief Particulier Opdrachtgeverschap (CPO Boerhaar) actief. De vereniging telt 26 leden en 10 partnerleden, allen met binding met de Boerhaar. Dit zijn hoofdzakelijk starters op de woningmarkt. […] Uw college, zo vernamen wij, heeft de CPO Boerhaar medio juli 2025 toegezegd om nog dit jaar 2025 schriftelijk de intentie uit te spreken het woningbouwproject op de Boerhaar samen op te pakken. Met deze intentieverklaring kan de CPO Boerhaar externe gelden aan trekken."

— Bron: PvdA stelt collegevragen over nieuwbouwprojecten op de Boerhaar (brief Toon Schuiling, 17-12-2025), HierinSalland, 27-12-2025, https://hierinsalland.nl/pvda-stelt-collegevragen-over-nieuwbouwprojecten-op-de-boerhaar/ (geraadpleegd 2026-10-04)

> "4. Aanvraag kredieten voor woningbouw Boerhaar BESLUIT: De raad voor te stellen om: Een voorbereidingskrediet beschikbaar te stellen van € 200.000,- voor de definitie- en ontwerpfase van het project. […] Een krediet van maximaal € 900,000,- beschikbaar te stellen voor dekking van de aankoopkosten incl. onderzoeken van het perceel inclusief opstallen Boerhaar 18/18a. […] SAMENVATTING Het is onze ambitie om tot 2032 1000 tot 1200 woningen te bouwen. Het merendeel in de dorpen Olst, Wijhe en Wesepe, maar ook ruimte voor woningbouw in de kleinere kernen, zoals op de Boerhaar. […] Om na sluiting van schoolgebouw De Bongerd over te gaan op sloop en nieuwbouw van starterswoningen."

— Bron: B&W besluitenlijst 12-05-2026 (gepubliceerd 18-5-2026; archive.csv) (geraadpleegd 2026-10-04). *HierinSalland noemt 21-4-2026 als datum van het raadsvoorstel.*

> "Het college van burgemeester en wethouders van de gemeente Olst-Wijhe (het College) heeft het voornemen om bouwrijpe kavels op (een gedeelte van) de percelen kadastraal bekend gemeente Wijhe, sectie E, nummer 1858, 2196 en 2197 aan Gebr. Meijer Bouwbedrijf B.V. (Bouwbedrijf Meijer) te verkopen en te leveren. De percelen zijn gelegen in het plangebied Boerhaar 18-20 te Wijhe en bestemd voor woningbouw. […] er [is] sprake van een uitzonderingspositie die een 1-op-1 uitgifte rechtvaardigt."

— Bron: Kennisgeving voornemen tot verkoop en levering van diverse percelen grond aan Gebr. Meijer Bouwbedrijf B.V. […] Boerhaar 18-20, gemeente, 15-5-2026 (archive.csv); ook Wijhe City, 15-5-2026, https://wijhecity.nl/2026/05/15/voornemen-verkoop-bouwgrond-boerhaar-18-20-wijhe/ (geraadpleegd 2026-10-04)

> "Er staan 39 inwoners van CPO Boerhaar te wachten op een handtekening […]. En er ligt een raadsvoorstel voor 26 mei waarin de gemeente Olst-Wijhe aan de raad vraagt om € 1,1 miljoen krediet […]. De ontwikkeling kent een verwacht tekort op de grondexploitatie van maximaal € 500.000. […] het concept schetsplan ca. 22 woningen bevat (in werkelijkheid laat het verkavelingsplan van Nonon Architectuur 23 of 24 woningen zien) […]. De aannemer voor het Boerhaar-project is Bouwbedrijf Meijer uit Raalte, zoals De Stentor op 9 april 2026 publiceerde."

— Bron: De Sallandse Geus: Boerhaar krijgt zijn handtekening, maar wie krijgt de bouwopdracht? (met rectificatie 11-5-2026), HierinSalland, 10-5-2026, https://hierinsalland.nl/boerhaar-aannemer-zonder-naam/ (geraadpleegd 2026-10-04). *Opiniestuk. De CPO-voorzitter zegt daarin: "de gemeente Olst-Wijhe is op dit moment niet klaar en niet geschikt voor burgerinitiatieven zoals dit."*

Op de voorlopige volgordelijst netcongestie (Gmb 2026, 422235, 10-9-2026): "CPO Boerhaar | Boerhaar 18, 18a, 20 | Boerhaar | 2027 | [projectrijpheid] 4 | 24 [woningen]". Projectrijpheid 4 betekent "Er is alleen een civielrechtelijke overeenkomst". Op de definitieve, aangepaste lijst ontbreekt het project, omdat projecten met een toegekende vooraanmelding (overgangsregeling) zijn verwijderd. Het definitieve raadsbesluit van 26-5-2026 over het krediet is **niet gevonden** in de nieuwsbronnen. Projectrijpheid 4 in september 2026 duidt erop dat er een overeenkomst ligt en dus waarschijnlijk dat het krediet is verleend [INT]. Controleren in iBabs (besluitenlijst raad 26-5-2026).

**Correctie §1, §6, §7:** toevoegen als **belangrijkste lopende CPO in Olst-Wijhe**: CPO Boerhaar, circa 22-24 starterswoningen. De locatie is de vrijkomende schoollocatie (Mijnplein/De Bongerd, leeg in 2027) plus de door de gemeente aan te kopen percelen Boerhaar 18/18a (voormalige discotheek). Bouwer is Bouwbedrijf Meijer (Raalte) via een bouwclaimovereenkomst. Het gaat om een kleine kern of buurtschap tegen Wijhe aan, niet om agrarische grond. De relevantie voor ons concept is hoog: de gemeente faciliteert hier een CPO met grondaankoop, maar volgens de initiatiefnemers moeizaam en traag. **Kansen-/risicoduiding [INT]:** CPO is mogelijk, maar vraagt bestuurlijke druk (raadsvragen, insprekers) en een professionele partner.

### 2.3 De Klimboom, Boskamp (tegenstrijdigheid 12)

> "Op de plek van de voormalige basisschool De Klimboom en het naastgelegen trapveldje komen 17-18 nieuwe woningen. […] Nieuwbouw: 9 koopwoningen door lokale CPO-groep (4 2-onder-1-kappers en 5 rijwoningen); 4 (sociale) huurwoningen; 4-5 betaalbare woningen. […] Zij laten hun woningen bouwen door bouwbedrijf Vosman uit Raalte. […] In de zomer van 2025 is er gestart met de bouw van de woningen voor de CPO-groep. Volgens plan zijn hun woningen voor de zomer (2026) klaar. SallandWonen is in september 2025 gestart met de bouw […]. De 4-5 betaalbare woningen worden aansluitend gebouwd. […] stuur dan een mail naar de CPO-groep via cpo.boskamp@hotmail.com"

— Bron: De Klimboom | Boskamp, https://wonen.olst-wijhe.nl/deklimboomboskamp (geraadpleegd 2026-10-04)

> "Maar liefst negen woningen worden gebouwd door jonge Boskampenaren […]. Vrijdag 6 december zetten zij samen met de gemeente Olst-Wijhe hun handtekeningen onder de koopovereenkomsten. […] Tom van Vreden is voorzitter van de CPO-vereniging Boskamp […]. 'Als gemeente ondersteunen we dit project van harte, omdat dit project 1-op-1 voortkomt uit de Gebiedsagenda Boskamp […]'"

— Bron: Jonge Boskampenaren bouwen samen eigen woningen, woonnieuws 6-12-2024 (archive.csv) (geraadpleegd 2026-10-04)

> "De bouwgrond ligt aan de Hyacinthstraat, op de locatie van voormalige basisschool De Klimboom. Er is hier plek voor 4-5 betaalbare woningen met een tuin. Op deze locatie worden op dit moment 9 woningen gebouwd door een lokale CPO-groep en er komen 4 nieuwe huurwoningen van SallandWonen. Wie kan meedoen? De verkoopprocedure staat open voor aannemers, ontwikkelaars en CPO-groepen(*). […] Bij meerdere inschrijvingen wordt er geloot."

— Bron: Verkoop bouwgrond op locatie De Klimboom van start, gemeente, 8-4-2026 (archive.csv) (geraadpleegd 2026-10-04). Inschrijving 10-4 t/m 1-5-2026.

Het uitgifteprotocol (B&W, archive.csv, 2024) noemt: "9 kavels aan de CPO-vereniging voor jongeren uit Boskamp, 4 aan SallandWonen voor sociale huur en 4 als beneden-/bovenwoningen via inschrijving". Voorlopige volgordelijst (10-9-2026): "Klimboom Boskamp | Hyacintstraat | Boskamp | 2027 | 1 | 18". De kavelwinkel meldt op 2026-10-04: "Op dit moment zijn er geen kavels te koop." De uitkomst van de inschrijving of loting van april-mei 2026 is **niet gevonden**.

**Correctie / tegenstrijdigheid 12:** de gemeentelijke bron zegt zelf "17-18": 9 CPO + 4 sociale huur + 4-5 betaalbaar. De "restkavels" zijn geen CPO-restkavels. Het gaat om 4-5 betaalbare woningen, verkocht via inschrijving en loting, open voor aannemers, ontwikkelaars én CPO-groepen. Het uitgifteprotocol 2024 noemde 4 beneden-/bovenwoningen. Op de netlijst staat 18. De CPO-woningen zouden volgens planning vóór de zomer van 2026 klaar zijn; de feitelijke oplevering is niet gevonden. **Status: opgelost voor zover de bronnen dat toelaten** (17 of 18 hangt af van 4 of 5 betaalbare woningen).

### 2.4 Olstergaard (tegenstrijdigheid 11) en Grijs & Groen / Vriendenerf (tegenstrijdigheid 13)

> "48 koopwoningen, gebouwd in opdracht van bewoners; 13 (sociale) huurwoningen; 11 appartementen van bewonersgroep 'Grijs & Groen Wonen'. De wijk is ontwikkeld door, voor en met toekomstige bewoners en omwonenden. De 72 woningen zijn een mix van vrijstaande woningen, twee-onder-een-kapwoningen en rijwoningen. […] Inmiddels zijn bijna alle woningen gebouwd en verkocht of verhuurd. In 2025 en 2026 hebben we de definitieve wegen aangelegd en het openbaar groen ingericht."

— Bron: Olstergaard | Olst, https://wonen.olst-wijhe.nl/olstergaard (geraadpleegd 2026-10-04)

> "Samen met bewoners, samenwerkingspartners vieren we vrijdag 2 oktober de afronding van duurzame en natuur inclusieve woonwijk Olstergaard in Olst. […] Marcel Blind, wethouder Wonen: 'Olstergaard is een bijzondere wijk geworden. […]'"

— Bron: Samen proosten op het resultaat: Olstergaard officieel afgerond, gemeente, 29-9-2026, https://www.olst-wijhe.nl/bestuur/nieuws/nieuwsberichten/samen-proosten-op-het-resultaat-olstergaard-officieel-afgerond (geraadpleegd 2026-10-04)

> "Grijs & Groen Wonen heeft in 2023 een kleinschalig woonproject voor actieve 50 plussers gebouwd in de Olstergaard. We hebben op twee naast elkaar liggende kavels twee gelaagde woongebouwen gerealiseerd voor 11 appartementen […] en een aantal gemeenschappelijke ruimtes. […] We bouwden als CPO (Collectief Particulier Opdrachtgeverschap). […] Inmiddels zijn we een VVE geworden. […] 22 maart 2026, we wonen 2 jaar in de Olstergaard!"

— Bron: https://www.grijsengroenwonen.nl/ (geraadpleegd 2026-10-04)

> "Een eigen, grondgebonden energieneutraal koophuis, 12 in totaal verdeeld over 4 blokjes; Een gemeenschappelijk, multifunctioneel 13e huis, ons Deelhuis […]" — "Een project ontwikkelen in Collectief Particulier Opdrachtgeverschap. […] 2012 Afspraken met gemeenten, vereniging oprichten […] 2016 Ondertekening koopaktes, start bouw; Mei 2017 Oplevering eerste huizen […]; 30 September 2017 Officiële opening […]. Onze partners: Architect GroenBlauw; Bouwbedrijf Hunebouw; Projectbegeleiding Building Community" — "© Vereniging Vriendenerf, Ringmus 50, 8121 JL Olst"; speerpunt: "Kleinschalige woongemeenschap voor 55+".

— Bron: https://www.vriendenerf.nl/hoe-wonen-wij-samen/ en https://www.vriendenerf.nl/hoe-is-vriendenerf-tot-stand-gekomen/ en https://www.vriendenerf.nl/ (geraadpleegd 2026-10-04)

De Woondeal West-Overijssel, Bijlage 1, noemt "Olst-Wijhe Olst Olstergaard Bestaand 80 104 -": 80 woningen in Woondeal 2022 en 104 in de periode 2024-eind 2030. Dat is een sleutelprojectcijfer, waarschijnlijk inclusief omgeving of flexwoningen [INT]. Bron: https://overijsselsewoonaanpak.nl/media/xhadtdva/20250325_524100_woondeal-west-overijssel-digitaal-toegankelijk.pdf

**Correcties:**
- **Tegenstrijdigheid 11: opgelost.** Gemeentelijke bron: **72 woningen** = 48 koopwoningen in particulier opdrachtgeverschap + 13 (sociale) huurwoningen + 11 CPO-appartementen van Grijs & Groen. Grijs & Groen spreekt van "ca. 50 kavels". De cijfers 74-78 of 75 zijn niet bevestigd. De wijk is officieel afgerond op 2-10-2026. Tiny houses komen voor ("Van Tiny House in Olstergaard … Ingrid vertelt", HierinSalland 24-1-2026; de eerste bewoner kwam in december 2021). De "Tuinkamer in ontwerp" is in mijn bronnen **niet gevonden**.
- **Tegenstrijdigheid 13: opgelost: twee projecten.** Vriendenerf (Ringmus 50, Olst; CPO 2012-2017; 12 koopwoningen + Deelhuis; 55+; Hunebouw/GroenBlauw/Building Community) en Grijs & Groen Wonen (Olstergaard; CPO, gebouwd in 2023, bewoond sinds maart 2024; 11 appartementen; 50+; nu VvE). §7 kan de zin "Of Grijs en Groen Wonen en Vriendenerf hetzelfde project zijn … niet vastgesteld" schrappen. Precisering: Vriendenerf vermeldt "voor 55+" (titel: "vijftigplussers"); bewoond sinds september 2017.
- Kritische noot (opinie): "Klein Lowlands in Olst, hoe Olstergaard de woningnood vergat" (De Sallandse Geus, 16-1-2026, https://hierinsalland.nl/de-sallandse-geus-klein-lowlands-in-olst-hoe-olstergaard-de-woningnood-vergat/) noemt ook 72 woningen en tiny houses. Het stuk illustreert dat experimentele woonvormen lokaal ook weerstand oproepen.

### 2.5 Herxen: CPO van 3 woningen, Grolleman (15 woningen) en visietraject met de provincie

> "08 Voorstel over ondertekenen bestuurlijke overeenkomst aangaande visietraject Herxen BESLUIT: In te stemmen met bijgaande bestuurlijke afspraken tussen het college van B&W van de gemeente Olst-Wijhe en Gedeputeerde Staten van de Provincie Overijssel, en daarmee; De € 15.000 uitvoeringskosten van 2026 […]. SAMENVATTING Om de groei van Herxen in goede banen te leiden is op aangeven van de provincie Overijssel een bestuursovereenkomst voorbereid. Deze overeenkomst ziet op het op voorhand in procedure kunnen brengen van ruimtelijke initiatieven zoals het CPO Herxen in afwachting van een visietraject. Dit visietraject heeft betrekking op hoe woningbouw in Herxen moet gaan landen in de periode tot 2050.
> 09 Voorstel principetoezegging CPO Herxen op het adres Herxen achter 7a in Wijhe BESLUIT: In principe (en onder voorwaarden) medewerking te verlenen aan het verzoek drie woningen te realiseren in Herxen achter nummer 7a in Herxen; Het verder in procedure brengen van de formele aanvraag mits kan worden aangetoond dat er wordt voldaan aan een evenwichtige toedeling van functies aan deze locatie (Etfal); Onderdeel hiervan is dat de aanvrager een overeenkomst in het kader van nadeelcompensatie ondertekent; Er moet een erfinrichtingsplan worden opgesteld […]. SAMENVATTING Voor een onbebouwd perceel achter Herxen 7a in Herxen is een verzoek ingediend voor het realiseren van drie woningen als onderdeel van een C(ollectief) P(articulier) O(pdrachtgeverschap)."

— Bron: B&W besluiten 02-06-2026, punten 08 en 09 (gepubliceerd 5-6-2026; archive.csv) (geraadpleegd 2026-10-04)

> "Wethouder Wonen Marcel Blind: 'Er zijn op dit moment twee mooie initiatieven voor woningbouw in Herxen. […] Wat ons betreft kan Herxen de komende jaren met gemiddeld zo'n 2 tot 4 woningen per jaar groeien. Om te voorkomen dat er her en der plukjes woningen worden gebouwd, gaan we samen met de provincie én de inwoners van Herxen kijken waar woningbouw kan komen en waar niet.' Gedeputeerde Liesbeth Grijsen vult aan: '[…] Herxen is onder meer zo aantrekkelijk vanwege de omgeving en daarom willen we tegelijkertijd het landelijk gebied beschermen. […]' […] Transportbedrijf Grolleman stopt binnen enkele jaren met de werkzaamheden in Herxen. Op de plek van de bedrijfslocatie komen op termijn 15 nieuwe woningen. Daarnaast is er een CPO-initiatief (Collectief Particulier Opdrachtgeverschap) voor 3 nieuwe woningen aan de kant van de spoorlijn Deventer-Zwolle. […] Naar verwachting start het gezamenlijke visietraject rond de jaarwisseling."

— Bron: Gezamenlijke visie voor woningbouw in Herxen, gemeente, 2-6-2026 (archive.csv; de URL `/2026/6/2/…` gaf op 2026-10-04 een 404); zelfde tekst op https://wijhecity.nl/2026/06/02/gezamenlijke-visie-voor-woningbouw-in-herxen/ (geraadpleegd 2026-10-04)

> "Plaatselijk Belang Herxen kreeg het verzoek van de provincie om in hun dorpsvisie het onderdeel ´wonen´ een update te geven. De bedoeling van deze vraag is om in één klap aan te geven waar Herxenaren vinden dat er in de toekomst eventueel gebouwd mag worden. Het grote voordeel is dat dan niet bij elke nieuwe woning het omgevingsplan (vroeger bestemmingsplan) hoeft te worden aan gepast. […] Er is nog geen werkgroep en er is nog geen planning."

— Bron: Woningbouw en woningvisie Herxen, herxen.nl, 22-9-2026, https://www.herxen.nl/2026/09/22/woningbouw-en-woningvisie-herxen/ (geraadpleegd 2026-10-04)

> "Het plan voorziet in 9 grondgebonden koopwoningen en 6 koopappartementen in een appartementengebouw, verdeeld over twee erven. Het college van B&W heeft besloten om middels een omgevingsvergunning voor een buitenplanse omgevingsplanactiviteit de herontwikkeling mogelijk te maken." […] "Ook de provincie heeft aangegeven dat ze positief is over de verandering van bedrijvenlocatie naar woningbouw."

— Bron: B&W besluiten 23-09-2025, punt 4 (archive.csv); woonnieuws "College Olst-Wijhe positief over plan nieuwbouw Herxen", 26-9-2025 (archive.csv) (geraadpleegd 2026-10-04)

Volgordelijst (definitief): "CPO Herxen | Kromme Koeweg | 2027 | 6 | 3 | Herxen" en "Grolleman Woningen | Herxen 63 | 2027 | 4 | 15 | Herxen".

**Correctie §2 en §6 (Herxen):** de bron van het concept is bevestigd. Aanvullen: de principetoezegging voor CPO Herxen is van **B&W 2-6-2026**. Het gaat om een **onbebouwd perceel achter Herxen 7a** (op de volgordelijst: Kromme Koeweg), met voorwaarden (ETFAL, nadeelcompensatie, erfinrichtingsplan). Op dezelfde dag sloot B&W **bestuurlijke afspraken met GS van Overijssel** (€ 15.000 voor 2026) die het mogelijk maken initiatieven als CPO Herxen **al in procedure te brengen in afwachting van het visietraject (horizon 2050)**. Dit is een uniek precedent voor provinciale voorkantsamenwerking (E1) bij een CPO op een onbebouwd perceel in een kleine kern. Grolleman: 15 koopwoningen (9 grondgebonden + 6 appartementen) via een BOPA, principebesluit B&W 23-9-2025, provincie positief.

### 2.6 Buurtschappenbeleid Herxen en Elshof: ontbreekt in het concept

Gevonden via een zoekresultaat en daarna gelezen (raadsvoorstel; overlapt met deelonderzoek 1):

> "Het buurtschap Elshof wordt beschouwd als buitengebied, waar nieuwe woningen in principe niet toegestaan zijn, tenzij sprake is van vervanging van een woning, van de bouw van een agrarische bedrijfswoning of gebruik wordt gemaakt van het KGO-beleid. […] Echter, in 2004 heeft de provincie het buurtschappenbeleid ontwikkeld om, in bijzondere situaties, tegemoet te komen aan de dringende behoefte om een nieuwe woningen te mogen bouwen in het buitengebied. Deze regeling geeft gemeenten de ruimte om zelf incidenteel nieuwe woningen, passend in het buurtschappenbeleid, toe te staan. […] In de gemeente Olst-Wijhe is in 2007 voor de buurtschappen Herxen en Elshof het buurtschappenbeleid ingevoerd, in 2010 is het beleid nog eens geactualiseerd en in 2020 zijn de kaders wat verruimd. […] A. Aanvrager dient een starter, doorstarter of senior te zijn en een bijzondere binding met het buurtschap te hebben."

— Bron: Raadsvoorstel "Voorstel tot vaststelling bestemmingsplan Elshof, Elshof 6c, 6d en 6e" (raad 19-9-2022; zaak 37706-2022), https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/f561bc20-c863-45fc-ae1f-f6d03d7ab205 (geraadpleegd 2026-10-04). Het precedent: **3 woningen op een perceel met agrarische bestemming** in Elshof voor drie starterskoppels (principeverzoek 11-10-2021).

**Correctie §2, §3b, §4:** toevoegen dat Olst-Wijhe **sinds 2007 een buurtschappenbeleid** heeft voor Herxen en Elshof (geactualiseerd 2010, verruimd 2020). Het staat nieuwe woningen in het buitengebied van die buurtschappen toe voor starters, doorstarters of senioren met een bijzondere binding. Elshof 6c-e (3 woningen, 2022), Engeweg (8 woningen, 2026) en CPO Herxen (3 woningen, 2026) liggen alle drie in deze twee buurtschappen. De beleidstekst zelf (versie 2020) is **niet gelezen**. Vindplaats: CVDR, iBabs, team Ruimte.

### 2.7 Erveweg / Hemelrijk-2, Welsum (circa 18 woningen op grond met agrarische bestemming): ontbreekt in het concept

> "10. Principebesluit ontwikkeling Erveweg (Hemelrijk-2) Welsum BESLUIT In principe medewerking te verlenen aan het wijzigen van het omgevingsplan voor de locatie met agrarische en volkstuinen bestemming ten noorden van Erveweg 8 te Welsum ten behoeve van woningbouw en bijbehorende voorzieningen, onder de voorwaarde dat: In overeenstemming met de gemeente een woningbouwprogramma wordt ontwikkeld dat voorziet in de behoefte van het dorp; […] De ketenpartners van de gemeente (o.a. provincie, waterschap, omgevingsdienst, veiligheidsregio) in kunnen stemmen met het plan […]; Een omgevingsvergunning voor buitenplanse omgevingsplan-activiteit voor de percelen in procedure te brengen onder voorwaarde dat er niet eerder wordt gestart met de planologische procedure, voordat een intentie- en anterieure overeenkomst zijn gesloten met de initiatiefnemer(s). SAMENVATTING In Welsum is lokaal het initiatief ontstaan voor de nieuwbouw van circa 18 woningen aan de rand van het dorp Wesepe [sic]. Het gaat om twee vrijstaande woningen, vier twee onder een kap woningen en 12 rijwoningen. Het initiatief komt van grondeigenaren. De locatie is een logische uitbreidingslocatie, grenzend aan de bestaande kern van Welsum."

— Bron: B&W besluiten 10-03-2026, punt 10 (archive.csv) (geraadpleegd 2026-10-04). In de samenvatting staat "Wesepe" waar Welsum bedoeld is (fout in de bron).

> "Op dit moment is er vanuit het dorp een plan voor de bouw van circa 18 woningen aan de westkant van Welsum. […] De nieuwbouwplannen bestaan uit 2 vrijstaande woningen, 4 twee-onder-een-kappers en 12 rijwoningen. Alle 18 koopwoningen. De plannen zijn een lokaal initiatief van de grondeigenaren en hun adviseur. Wethouder wonen Marcel Blind: 'Dit initiatief is een welkome en logische aanvulling op het dorp Welsum. Het zijn deels woningen met een lagere prijs […]'"

— Bron: Nieuw lokaal initiatief voor woningbouw in Welsum, woonnieuws 13-3-2026 (archive.csv) (geraadpleegd 2026-10-04)

Voorlopige volgordelijst: "Hemelrijk 2 | Hemelrijk 2 | Welsum | 2027 | 1 | 18". Het project staat niet op de definitieve lijst, waarschijnlijk door de vooraanmelding [INT].

**Belang:** dit is het **meest vergelijkbare precedent voor ons concept**: circa 18 woningen op grond met (deels) **agrarische** bestemming, als initiatief van grondeigenaren, aansluitend aan een kleine kern, met positief principebesluit en provinciale instemming als voorwaarde. **Toevoegen aan §3b, §3e (scenario "aansluitend aan een kleine kern"), §6 en §7.**

### 2.8 't Kleiland, Kleistraat Olst (20 woningen op grond met agrarische bestemming)

> "Medewerking te verlenen aan de aanvraag omgevingsvergunning voor het realiseren van twintig woningen voor de ontwikkeling 'T Kleiland in Olst door een omgevingsvergunning af te geven. SAMENVATTING Op 19 december 2025 is een aanvraag omgevingsvergunning ingediend voor het planologisch toestaan van 20 woningen aan de Kleistraat (naast nummer 1) in Olst. […] De gemeenteraad heeft op 9 februari 2026 een positief bindend advies voor deze aanvraag uitgebracht."

— Bron: B&W besluiten 17-03-2026, punt 10 (archive.csv) (geraadpleegd 2026-10-04)

> "Omdat deze locatie nog de bestemming 'agrarisch' heeft, is dit collegebesluit nodig om woningbouw toe te staan. Met dit collegebesluit kan initiatiefnemer Holleman Ontwikkeling de woningbouwplannen verder uitwerken. […] Het woningbouwplan voor 't Kleiland bestaat uit 20 woningen: 5 sociale huurwoningen, 8 sociale koopwoningen en 7 woningen in de vrije sector, waarvan er 2 levensloopbestendig zijn."

— Bron: Eerste vergunning voor 't Kleiland in Olst verleend, woonnieuws 20-3-2026 (archive.csv) (geraadpleegd 2026-10-04)

**Correctie §5/§6:** "Kleistraat (principebesluit circa 20 woningen, B&W 7-1-2025)" aanvullen met: BOPA-omgevingsvergunning (eerste fase, planologisch) verleend op 17-3-2026 na een **bindend advies van de raad op 9-2-2026**. Het is een project van een ontwikkelaar (Holleman), geen gemeentegrond. De locatie had de bestemming "agrarisch". Dit is een precedent voor de route raad-bindend-advies → BOPA voor 20 woningen aan de rand van een grote kern.

### 2.9 Lierderholthuisweg 3, Vettewinkelweg 2, Kloosterhoekweg 3, Bokkelerweg 1 en Engeweg 10/10A (erven onder KGO)

- **Lierderholthuisweg 3, Wijhe:** de B&W-tekst bevestigt het concept: "omzetting van de agrarische functie naar woonfunctie, splitsing van de bestaande karakteristieke woning, realisatie van één extra woning via sloop van voormalige agrarische bebouwing en aanleg van 1,5 hectare bos en omzetting naar natuur"; route BOPA; voorwaarden ETFAL, **overeenkomst nadeelcompensatie**, erfinrichtings- en beplantingsplan, participatieverslag. — B&W besluiten 20-01-2026, punt 6 (archive.csv).
- **Vettewinkelweg 2, Wijhe:** "Er moet toestemming worden verkregen van de provincie voor deze herontwikkeling, omdat er een provinciaal belang is. […] voordat de anterieure overeenkomst is gesloten met de initiatiefnemer." "De initiatiefnemer wil met toepassing van de KGO-regeling de agrarische bedrijfsbebouwing slopen en ter compensatie een extra woning realiseren." — B&W besluiten 23-01-2024, punt 3 (archive.csv). De concepttekst "de provincie gaf in vooroverleg aan te kunnen instemmen" staat **niet** in deze besluittekst. Die zin komt mogelijk uit de bijlage-PDF, die ik niet heb gelezen.
- **Kloosterhoekweg 3, Welsum (2 woningen, KGO/"rood voor rood"):** "Op de locatie aan de Kloosterhoekweg is het door beperkte ruimte binnen het plangebied, niet mogelijk om de 50 meter spuitzone aan te houden. Voor deze locatie hebben we een locatiespecifiek onderzoek ontvangen […]. Voorwaarde bij dit advies is dat: de initiatiefnemer van de ontwikkeling vooraf duidelijk door ons als gemeente geïnformeerd is over de juridische en gezondheidsrisico's die hij neemt […]." — B&W besluiten 21-04-2026, punt 05 (archive.csv). **Nieuw kansarm-/kansrijkfactor voor §3d:** de **spuitzone van 50 m** (gewasbeschermingsmiddelen) is in 2026 een expliciet toetspunt. Afwijken kan alleen met een locatiespecifiek onderzoek en informatieplicht.
- **Bokkelerweg 1, Wesepe:** "In principe medewerking te verlenen aan het splitsen van de woning in twee wooneenheden in het kader van de 'Handreiking KGO' […]. Met toepassing van de Handreiking Kwaliteitsimpuls Groene Omgeving (KGO) kan voor niet-karakteristieke panden de splitsing worden gerealiseerd, mits zij voldoen aan bepaalde voorwaarden." — B&W besluiten 11-11-2025, punt 10. Daarnaast meldt Wijhe City op 19-9-2026: "in Wesepe [komen] plannen van de grond voor zes nieuwe plattelandskamers aan de Bokkelerweg, al heeft de gemeente meer tijd nodig voor dit besluit" (https://wijhecity.nl/2026/09/19/laadpalen-renovaties-en-nieuwe-woningen-voor-olst-wijhe/). **Correctie §6 nr. 11:** het gaat niet om "zes landelijke woningen": het zijn **plattelandskamers** (recreatief), een lopend besluit. Daarnaast is er de woningsplitsing van Bokkelerweg 1 (11-11-2025). Een "energiemolen" komt in de geraadpleegde bronnen niet voor.
- **Engeweg 10/10A, Wijhe:** splitsing van een niet-karakteristieke woning onder de Handreiking KGO, via BOPA. — B&W besluiten 21-04-2026, punt 06.
- **Marledijk 33/31a (LBV+):** omzetting van de tweede bedrijfswoning naar regulier wonen (B&W 18-3-2025). Wijhe City 19-9-2026: "Aan de Marledijk 33 in Marle verandert de huidige bedrijfswoning in een gewone burgerwoning."

### 2.10 Overige kernprojecten (context, §5/§6)

| Project | Bevinding (letterlijk/kern) | Bron (geraadpleegd 2026-10-04) |
|---|---|---|
| IJsseldal / MEKO, Wesepe | "IJsseldal bestaat uit 81 woningen voor starters, gezinnen en senioren. Later dit jaar worden de eerste woningen opgeleverd." Start bouw op 4-3-2026 | Woonnieuws "Start bouw IJsseldal in Wesepe", 4-3-2026 (archive.csv) |
| Olst Zuid | "nieuwbouw van zo'n 90 woningen aan de zuidkant van Olst […] tussen het spoor en de Vink. In 2023 kocht de gemeente de grond […]. Als alles naar verwachting verloopt, start in 2027 de aanleg van de bouwwegen en de verkoop van de woningen." Volgordelijst: Olst Zuid, start bouw 2030, 90 woningen | Woonnieuws 7-2-2025 (archive.csv); volgordelijst |
| Mijnpleinschool (Matzerschool) Wijhe, Molenstraat 31 | "circa 44 levensloopbestendige sociale huurappartementen" door SallandWonen, principebesluit B&W 2-12-2025, route BOPA; voorlopige volgordelijst "Schoollocatie Matzer … 40" | B&W 02-12-2025 punt 10; woonnieuws 3-12-2025 |
| Scholenlocaties Olst (IJsselwijs/Opwaardz) | "59 nieuwe woningen"; anterieure overeenkomst met Nikkels getekend 13-11-2025; bouw "naar verwachting eind 2027" | Woonnieuws 13-11-2025 (archive.csv) |
| Holsthoek, Den Nul | Collegevoorstel 11-8-2026: verbouw buurthuis + **19 woningen** (variant 2: 28); raadsbesluit op 7-9-2026 gepland (uitkomst niet gevonden); voorlopige volgordelijst: 19 | https://wijhecity.nl/2026/08/18/den-nul-krijgt-19-nieuwe-woningen-en-vernieuwd-buurthuis/ |
| Stationsweg Wijhe | Intentiebrief met twee particuliere initiatiefnemers, o.a. een "initiatief van ouders die voor hun kinderen met een beperking een woon-zorgcomplex willen realiseren" (een collectief woon-zorginitiatief!); voorlopige volgordelijst 22 + 12 + 10 | Woonnieuws 12-3-2026 (archive.csv) |
| Wengelerhoek Wijhe | 135 woningen (Roosdom Tijhuis); voorlopige volgordelijst 135 | Wijhe City 14-9-2026; Gmb 2026, 422235 |
| Wijhe Noord | "zo'n 300 woningen"; definitieve volgordelijst 207 (start bouw 2030), voorlopige lijst 309 | Woonnieuws 28-5-2025; volgordelijsten |
| Flexwonen | "76 flexw[o]ningen […] 50 flexwoningen staan op de nieuwbouwlocatie Wengelerhoek aan de zuidkant van Wijhe […]. En 26 woningen staan op de locatie Vink aan de zuidkant van Olst, tussen Olstergaard, de Aardehuizen en het spoor. Alle flexwoningen zijn sociale huurwoningen" | https://wonen.olst-wijhe.nl/flexwonen |
| Aardehuizen | "Aan de zuidrand van Olst ligt een bijzondere ecologische woonwijk met 23 woningen en een gezamenlijk Middenhuis." | https://www.aardehuis.nl/ |

**Correcties:** §7 "Flexwonen Wengelerhoek, Wijhe: aantal onbekend; omgevingsvergunning B&W 20-12-2022" wordt: **76 flexwoningen (50 Wengelerhoek Wijhe + 26 Vink Olst), sociale huur via SallandWonen, in gebruik genomen in 2023**. Het jaartal "2006" voor de Aardehuizen is in de geraadpleegde bron niet gevonden; wel bevestigd zijn 23 woningen + Middenhuis aan de zuidrand van Olst. De CPO-vorm van de Aardehuizen staat niet op de homepage. "Wooncommunity De Ware" (24 studio's, geopend 13-3-2025) ligt **in Raalte** (Hartkampweg). Het is een gezamenlijk project van Raalte en Olst-Wijhe, geen Olst-Wijhes woonproject.

### 2.11 Nieuwe initiatieven uit de volgordelijst die het concept mist (buitengebied/kleine kernen)

Uit de definitieve, aangepaste volgordelijst (PDF, aangemaakt 25-9-2026) en de voorlopige lijst (Gmb 2026, 422235):

| Plannaam | Locatie | Kern volgens lijst | Start bouw | Projectrijpheid* | Woningen |
|---|---|---|---|---|---|
| **De Brinkweiden** | Kappeweg 18 | **Buitengebied** | 2028 | 6 | **12** |
| **Wijlandhof** | Elshof (nabij) 19a | Elshof | 2027 | 6 | **12** |
| CPO Boerhaar (alleen voorlopige lijst) | Boerhaar 18, 18a, 20 | Boerhaar | 2027 | 4 | 24 |
| Overmars | Boerhaarseweg 4 | Buitengebied | 2026 | 2 | 2 |
| Kappeweg 1 | Kappeweg 1a, 1b in aanvraag | Buitengebied | 2027 | 4 | 3 |
| Weth. M. van Doorninckweg 20 | idem | Buitengebied | 2027 | 6 | 2 |
| Lierderholthuisweg 12a en b | idem | Buitengebied | 2029 | 1 | 2 |
| Kletterstraat 7 | idem | Buitengebied | 2027 | 2 | 1 |
| Kloosterhoekweg 3 rood voor rood | idem | Welsum | 2027 | 3 | 2 |
| Grolleman Woningen | Herxen 63 | Herxen | 2027 | 4 | 15 |
| Berkeserf II | Boskamp | Boskamp | 2027 | 2 | 18 |
| Hof van Polletje (alleen voorlopige lijst) | Jan Hooglandstraat 34 | Olst | 2027 | 6 | 10 |
| De Zorgster | Overkempe, Koekoeksweg 100 | Olst | 2028 | 1 | 24 |

*Projectrijpheid volgens art. 9 van de beleidsregels: 1 = civielrechtelijke overeenkomst + onherroepelijke bouwvergunning; 2 = overeenkomst + onherroepelijk omgevingsplan of BOPA; 3 = alleen onherroepelijke omgevingsvergunning; 4 = alleen civielrechtelijke overeenkomst; 5 = alleen omgevingsplan of BOPA; 6 = andere bewijsstukken.

— Bron: Aangepaste volgorde lijst netcongestie, https://www.olst-wijhe.nl/samenleven/olst-wijhe-in-ontwikkeling/energietransitie/woningbouwproject-aanmelden-voor-prioritering-van-transportcapaciteit/aangepaste-volgorde-lijst-netcongestie (PDF); Gmb 2026, 422235, https://zoek.officielebekendmakingen.nl/gmb-2026-422235.html (geraadpleegd 2026-10-04)

**Niet gevonden:** inhoud of initiatiefnemer van **De Brinkweiden (Kappeweg 18, 12 woningen, buitengebied)** en **Wijlandhof (Elshof, 12 woningen)**. Ik heb gezocht in het gemeentelijk nieuwsarchief, woonnieuws en de B&W-archieven 2024-2026, Salland1, Salland Centraal, Wijhe City, HierinSalland en via WebSearch. Gezien schaal en ligging zijn dit **potentieel de dichtstbijzijnde analogieën voor 10-12 woningen in het buitengebied** [INT]. Projectrijpheid 6 betekent dat er nog geen overeenkomst of planologische toestemming is. **Waar te vinden:** team Ruimte en Samenleving (netcongestieow@olst-wijhe.nl, 14 0570), zaakdossier, eventueel een principeverzoek in de B&W-lijsten na 22-9-2026.

### 2.12 Boer met plan voor ouderenhuurwoningen op agrarische grond (juli 2026)

> "Twee weken geleden meldde zich daar een oudere boer. Dit met het fijne plan om op zijn vrijkomende agrarische grond (bijna 6000 m2) een complex met huur woningen voor ouderen te realiseren. […] Maar zo gemakkelijk is het niet. Bouwen in het buitengebied ligt ingewikkeld. De provincie, om maar eens wat te noemen, is daar niet heel happig op. Als Olst-Wijhe Vooruit vinden wij dat zo'n lokaal initiatief, mits passend in het landschap én met het behoud van het dorpse karakter, een kans moet krijgen. Boerenerven zijn misschien wel de buurtschappen van de toekomst."

— Bron: Onze Man in Wijhe Toon Schuiling, HierinSalland, 18-7-2026, https://hierinsalland.nl/onze-man-in-wijhe-toon-schuiling-8/ (geraadpleegd 2026-10-04). Locatie en initiatiefnemer niet genoemd. Relevant als signaal: de oppositie steunt collectieve of seniorenwoningbouw op vrijkomende agrarische grond.

---

## Prioriteit 3: KGO 10 jaar, woningsplitsing, omgevingsvisie (§3, §2)

### 3.1 "10 jaar KGO-beleid": artikel van 9-2-2021

> "In de gemeente Olst-Wijhe wordt inmiddels 10 jaar gewerkt met het KGO-beleid […]. Als de ruimtelijke kwaliteit niet voldoende wordt verhoogd, kan de initiatiefnemer ook nog een bedrag storten in de Voorziening Ruimtelijke Kwaliteit, een soort fonds dat projecten financiert die de ruimtelijke kwaliteit in de gemeente Olst-Wijhe verbeteren. […] Het KGO-principe is toegepast op 65 erven in Olst-Wijhe. De erven zijn landschappelijk ingepast. Er is maar liefst 63.000 m2 aan landschapsontsierende bedrijfsbebouwing gesloopt. […] Zo zijn er door het KGO-beleid 93 nieuwe woningen gebouwd. […] Wethouder Herman Engberink: 'Het meest belangrijk van het KGO-beleid is dat we hiermee verrommeling van ons buitengebied tegengaan. […]'"

— Bron: 10 jaar KGO-beleid: wat heeft het opgeleverd?, Salland1, **gepubliceerd 9-2-2021** (gewijzigd 2-1-2025), https://www.salland1.nl/10-jaar-kgo-beleid-wat-heeft-het-opgeleverd/ (geraadpleegd 2026-10-04)

**Correctie §3a:** voeg de datum toe (**9-2-2021**, dus de periode ca. 2011-2021, vóór de Handreiking KGO 2024). De cijfers 65 erven, 63.000 m2 en 93 woningen zijn bevestigd. "Gemiddeld 1,4 per erf" staat niet in het artikel en is een afgeleide (93/65) [INT]. Het fonds heette in 2021 "**Voorziening Ruimtelijke Kwaliteit**". Bij Salland Loont spreekt B&W in 2025 van een "gemeentelijke fonds ruimtelijke kwaliteit". "Ruimtelijke Kwaliteitsprovisie" komt niet uit mijn bronnen.

### 3.2 Woningsplitsing

> "Sinds voorjaar 2024 kunnen huiseigenaren in onze gemeente kiezen voor woningsplitsing. […] Een motie van de raad was destijds de aanleiding voor het nieuwe beleid. In de periode medio mei 2024 tot eind vorig jaar kregen we in totaal 16 verzoeken voor woningsplitsing; 14 buiten de bebouwde kom en 2 binnen de bebouwde kom. […] Er zijn heldere beleidsregels wat kan en wat niet kan."

— Bron: Animo voor woningsplitsing, woonnieuws 28-5-2026 (archive.csv; URL uit het concept gaf 404) (geraadpleegd 2026-10-04)

> "Wethouder Marcel Blind: 'Als mensen plannen hebben om hun (koop)woning op te splitsen, staan we daar in de basis positief tegenover. Want elke woning die we extra beschikbaar hebben, is er één. […]' […] 'Voor het buitengebied werkt het net wat anders, omdat we daar te maken hebben met het inpassen van wonen in een landelijke omgeving. In de basis zeggen we ook daar 'ja' tegen woningsplitsing als aan een aantal voorwaarden wordt voldaan.'"

— Bron: Salland1, 7-6-2024, https://www.salland1.nl/gemeente-olst-wijhe-ziet-kansen-voor-woningsplitsing-elke-woning-die-we-extra-beschikbaar-hebben-is-er-een/ (geraadpleegd 2026-10-04)

**Correctie §3a:** de cijfers (16 verzoeken, waarvan 14 buiten de bebouwde kom, periode medio mei 2024 tot eind 2025) zijn bevestigd. De maxima "5/10 woningen" staan **niet** in deze nieuwsbronnen (tegenstrijdigheid 1 blijft open voor deelonderzoek 1). Het Salland Centraal-bericht "Bewoners zoeken 'lotgenoten' inzake woningsplitsing" (15-6-2026) gaat over **Raalte/Luttenberg** en niet over Olst-Wijhe. Niet gebruiken.

### 3.3 Omgevingsvisie: vastgesteld op 12 mei 2025 (tegenstrijdigheid 3 opgelost) en amendement

> "De gemeenteraad van de Overijsselse gemeente Olst-Wijhe heeft de definitieve omgevingsvisie vastgesteld. […] LTO Noord-afdeling Salland diende vorig jaar al een zienswijze in over de conceptomgevingsvisie. Daarbij ging het vooral over de zonering van 1 kilometer rondom woonkernen waarbinnen geen nieuwe, milieubelastende activiteiten zouden mogen plaatsvinden. Dat werd later aangepast in 'een nader te bepalen afstand'. […] In februari sprak LTO Noord-afdeling Salland in tijdens de oordeelsvormende raadsvergadering. Daarna dienden VVD en Gemeentebelangen een amendement in. Hierover werd in april gestemd. Maar doordat de stemmen staakten, werd het onderwerp opnieuw geagendeerd voor de raadsvergadering van maandag 12 mei. Hierin werd een gewijzigd amendement ingediend door CDA, gesteund door VVD, Gemeentebelangen en de Partij voor de Sport. […] 'Om nadelige milieu- en gezondheidseffecten te voorkomen, zijn we over het algemeen terughoudend in het toestaan van nieuwe milieubelastende bedrijfsactiviteiten in een nog nader te definiëren zone rondom de kleine kernen. Deze zonering geldt niet voor (uitbreiding van) bestaande bedrijven, mits passend in de geldende wet- en regelgeving.' Mede door de positieve appreciatie van wethouder Judith Compagner (CDA) ontstond brede steun voor dit amendement en werd het unaniem aangenomen."

— Bron: Omgevingsvisie Olst-Wijhe kan op goedkeuring landbouwsector rekenen, Nieuwe Oogst (Tys Hallema), 14-5-2025, https://www.nieuweoogst.nl/nieuws/2025/05/14/omgevingsvisie-olst-wijhe-kan-op-goedkeuring-landbouwsector-rekenen (geraadpleegd 2026-10-04)

Aanvullend (B&W 26-05-2026, punt 6): "Bij de oordeelsvormende raadsvergadering over het vaststellen van de omgevingsvisie op 24 februari 2025 […]". De gemeente meldt dat er een publieksvriendelijke samenvatting is gepubliceerd.

**Correctie §2 en tegenstrijdigheid 3:** vastgesteld in de **raadsvergadering van maandag 12 mei 2025**. De oordeelsvormende vergadering was op 24-2-2025; in april 2025 staakten de stemmen over het eerste amendement. **Status: opgelost (nieuwsbron).** Nuance bij het amendement: de nieuwe tekst gaat over een "nog nader te definiëren zone rondom de **kleine** kernen" met een uitzondering voor (uitbreiding van) bestaande bedrijven. De 1 km zat al in de conceptversie en was in het ontwerp al vervangen door "een nader te bepalen afstand". Het eerste amendement kwam van VVD en GB; het aangenomen gewijzigde amendement van het CDA (gesteund door VVD, GB en Partij voor de Sport) en werd **unaniem** aangenomen. Duiding [INT]: de zone beperkt **nieuwe** milieubelastende activiteiten nabij kleine kernen. Omgekeerd vormen bestaande bedrijven een beperking voor nieuwe woonfuncties via milieuzonering en de spuitzone.

---

## Prioriteit 4: Netcongestie (§5; C4)

**Bevinding: beleidsregels en procedure**

> "Het college van burgemeester en wethouders stelde op 11 augustus de beleidskaders hiervoor vast. Initiatiefnemers en ontwikkelaars kregen tot 27 augustus de tijd om hun plannen in te dienen bij de gemeente, wat ruim veertig aanvragen opleverde. […] Deze volgordelijst staat overigens nadrukkelijk los van het wel of niet verlenen van omgevingsvergunningen […]. De gemeente heeft donderdag 10 september de concept-volgordelijst gepubliceerd op www.olst-wijhe.nl/netcongestie. Vanaf de publicatiedatum hebben initiatiefnemers tien kalenderdagen de tijd om bezwaar te maken over hun positie op de lijst. […] Vanaf 1 oktober 2026 start de gemeente met het indienen van de transportaanvragen bij de netbeheerder."

— Bron: Gemeente Olst-Wijhe stelt prioriteitenlijst woningbouwplannen op vanwege netcongestie, Salland Centraal, 12-9-2026, https://www.sallandcentraal.nl/2026/09/gemeente-olst-wijhe-stelt-prioriteitenlijst-woningbouwplannen-op-vanwege-netcongestie/ (geraadpleegd 2026-10-04; via de WordPress-API, de webpagina gaf 403)

> "De regeling is bedoeld voor woningbouwprojecten in Olst-Wijhe die naar verwachting binnen tien jaar gerealiseerd worden. Onder woningbouwprojecten vallen ook plannen voor één nieuwe woning of bijvoorbeeld een splitsing van een woning waarvoor een extra aansluiting nodig is. […] Het is niet meer mogelijk om een woningbouwproject aan te melden. De aanmeldtermijn is verstreken. […] Als we de eventuele zienswijzen hebben verwerkt, stellen wij de definitieve lijst vast. Deze wordt op 25 september gepubliceerd. We leveren de definitieve lijst op 1 oktober aan bij de netbeheerder. De volgordelijst woningbouwprojecten is vastgesteld."

— Bron: Woningbouwproject aanmelden voor prioritering van transportcapaciteit, https://www.olst-wijhe.nl/netcongestie (→ `/samenleven/olst-wijhe-in-ontwikkeling/energietransitie/woningbouwproject-aanmelden-voor-prioritering-van-transportcapaciteit`) (geraadpleegd 2026-10-04)

**Criteria (art. 9 Beleidsregels):**

> "Stap 1: start bouw. Als eerste stap vindt een rangschikkingsplaats op basis van de maand van start bouw, waarbij een project hoger wordt gerangschikt als de bouw eerder start. […] Stap 2: projectrijpheid [rangorde 1-6, zie §2.11] […] Stap 3: maatschappelijk belang […] a. de projectlocatie draagt substantieel bij (in termen van aantal woningen) aan de gemeentelijke focus op wonen. b. Het project draagt bij aan en evenwichtige spreiding van wooninitiatieven over de kernen. […] Stap 4: datum oplevering […]." Art. 10: loting bij gelijke positie. Art. 13: bezwaar binnen tien kalenderdagen, daarna kort geding binnen tien dagen. "Aldus vastgesteld in de vergadering van 11 augustus 2026."

Voor collectieve woonvormen staat in de toelichting een aparte subfunctie: "Woningbouw — collectieve woonvormen: 1. Bestuursverklaring (zie artikel 5); 2. Overeenkomst over collectieve woonvorm (primair) óf omgevingsplan (fallback)."

— Bron: Beleidsregels aanvraag prioriteit transportcapaciteit woningbouwprojecten gemeente Olst-Wijhe 2026 (PDF, 17 p.), op de netcongestiepagina; officieel gepubliceerd als **Gmb 2026, 385444 (13-8-2026)** (geraadpleegd 2026-10-04)

> "09. Vaststellen format Bestuursverklaring prioriteit toekenning transportcapaciteit […] Teamleider Ruimte en Samenleving mandaat te verlenen om deze bestuursverklaring te ondertekenen voor de 47 woningbouwinitiatieven die zich voor prioritering hebben aangemeld. […] Dit kan vanaf 1 oktober aanstaande."

— Bron: B&W besluiten 15-09-2026, https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/b-amp-w-besluiten-15-09-2026 (geraadpleegd 2026-10-04)

**Definitieve ("aangepaste") lijst, eind september 2026:**

> "Netcongestie: Aangepaste volgordelijst woningbouw vastgesteld. Deze week heeft het college de aangepaste volgordelijst vastgesteld. […] heeft vanaf 10 september open gestaan voor bezwaar. Dit heeft geleid tot enkele bezwaren en verzoeken tot rectificatie. Op basis hiervan is de lijst aangepast. Daarnaast zijn alle projecten die in het kader van de vooraanmelding (zie hieronder) zijn toegekend, uit de lijst verwijderd. […] Voor een aantal projecten is al voor 1 juli een vooraanmelding ingediend in het kader van een overgangsregeling. […] Voor de meeste projecten is dit het geval. […] Op basis daarvan zijn deze woningbouwinitiatieven uit de volgordelijst verwijderd."

— Bron: Aangepaste volgorde lijst netcongestie (PDF, metadata 25-9-2026), URL in §2.11 (geraadpleegd 2026-10-04)

**Kerncijfers [eigen telling]:** de voorlopige lijst (Gmb 2026, 422235) bevat **47 regels met samen 1.400 woningen**. De definitieve lijst bevat **31 projecten met samen 774 woningen**, na verwijdering van projecten met een toegekende vooraanmelding, zoals Wengelerhoek (135), Klimboom (18), CPO Boerhaar (24), Hemelrijk-2 (18), Kleiland (20), Matzer (40) en Holsthoek (19).

**Na 1-10-2026:** in het gemeentelijk nieuwsarchief (laatste bericht 1-10-2026) en de regionale media is **geen bericht gevonden** over de feitelijke indiening bij Enexis of de reactie van de netbeheerder. Ter vergelijking een buurgemeente: "Voorlopig geen stroomaansluiting voor 90 nieuwe woningen in Heeten" (Raalte, Salland Centraal/Salland1 25-9-2026).

**Correcties §5 en C4:**
- "beleidsregels in het Gemeenteblad; nummer onzeker" wordt **Gmb 2026, 385444** (beleidsregels, vastgesteld door B&W op 11-8-2026, gepubliceerd 13-8-2026). Voorlopige lijst: **Gmb 2026, 422235** (10-9-2026). **Tegenstrijdigheid 17 opgelost:** gmb-2026-415179 is van **Brunssum** en gmb-2026-421329 van **Lansingerland** (DC.creator gecontroleerd). Niet gebruiken.
- "47 woningbouwinitiatieven" is bevestigd (B&W 15-9-2026). Salland Centraal spreekt van "ruim veertig aanvragen". De criteria zijn nu bekend (start bouw → projectrijpheid → maatschappelijk belang en spreiding over kernen → oplevering → loting).
- **Een tweede aanmeldronde:** niet gevonden. De pagina meldt alleen "De aanmeldtermijn is verstreken". **Gevolg voor ons concept [INT]:** een nieuw CPO-initiatief staat niet op de lijst. Bij een latere ronde scoort het laag op stap 2 (projectrijpheid) zolang er geen overeenkomst of BOPA is, en op stap 3a (weinig woningen). Positief: er is een aparte prioriteringscategorie "collectieve woonvormen" in de systeemcode, met een "overeenkomst over collectieve woonvorm" als bewijsstuk.
- Concept §6 nr. 9 ("aug.-okt. 2026"): de definitieve lijst is gepubliceerd rond 25-9-2026 en ingediend vanaf 1-10-2026.

---

## Prioriteit 5: Erfcoach, Salland Loont, Wesepe, inwonerpanel, Focus op Wonen, prestatieafspraken, VHP, Woondeal

### 5.1 Erfcoach (D2)

> "Yvonne in 't Veld – Erfcoach – Werkzaam in de gemeenten: Dalfsen, Olst-Wijhe, Ommen en Hardenberg. Mobiel Telefoonnummer: 06 10 98 22 76 – Mail direct: ygw.in.t.veld@overijssel.nl" […] "Karin Jansen – Erfcoach – Werkzaam in de gemeenten: Deventer en Raalte. […] karin.jansen@pratensis.nl"

— Bron: Contact met de erfcoaches, Erfcoach Overijssel, https://erfcoachoverijssel.nl/contact-met-de-erfcoaches/ (geraadpleegd 2026-10-04). Niek Oude Scholten staat **niet** (meer) op deze lijst.

> "In het buitengebied van Olst-Wijhe staan erfcoaches Yvonne In 't Veld en Niek Oude Scholten klaar om met erfeigenaren mee te denken over de toekomst van hun boerderij of erf. […] woonvragen, zoals Rood voor Rood en mantelzorg […] nieuwe functies in agrarische gebouwen die niet meer worden gebruikt"

— Bron: De erfcoach staat voor u klaar, gemeente, 15-9-2025 (archive.csv) (geraadpleegd 2026-10-04)

De pagina van De Kracht van Salland van 8-5-2026 ("Terugblik Online Café: BoerenPerspectief & Erfcoach", https://www.dekrachtvansalland.nl/actueel/actueel/2026/5/8/terugblik-online-caf-boerenperspectief-amp-erfcoach) noemt geen namen van erfcoaches. De concept-URL uit 2024 (`…/2024/2/4/erfcoach-staat-ook-dit-jaar-voor-je-klaar`) gaf op 2026-10-04 een **404**.

**Correctie §4 (D2) en §9:** "Erfcoach Salland (Deventer, Olst-Wijhe, Raalte): Niek Oude Scholten (Pratensis)" is **verouderd**. Actueel (2026-10-04): **Erfcoach Overijssel Yvonne in 't Veld** (werkgebied Dalfsen, Olst-Wijhe, Ommen, Hardenberg; 06 10 98 22 76; ygw.in.t.veld@overijssel.nl). In september 2025 noemde de gemeente nog In 't Veld én Oude Scholten. Status D2: **gevonden**. Daarnaast organiseert De Kracht van Salland op 8-10-2026 de informatie- en netwerkavond "Grond voor toekomst in Salland" bij Logtenberg op de Boerhaar voor grondeigenaren, met de gemeente en de erfcoaches (gemeente, 23-9-2026, archive.csv).

### 5.2 Salland Loont

> "Op 30 juni 2025 heeft de raad unaniem de motie 'Salland Loont' aangenomen. […] De bestuurlijke aanjagersrol hebben wij als gemeente zeker genomen. Dit doen we samen met gemeenten Raalte en Deventer. […] We hebben als gemeente vorig jaar 17.000 euro aan Salland Loont toegekend voor het opstarten van de organisatie. Ook Raalte en Deventer hebben dit bedrag aan Salland Loont doen toekomen. Vanuit ons gemeentelijke fonds ruimtelijke kwaliteit hebben we daarnaast eenmalig een bijdrage van 75.000 euro toegezegd aan Salland Loont voor het belonen van groen-blauwe diensten."

— Bron: B&W besluiten 28-10-2025, punt 10 "Afdoening motie Salland Loont" (archive.csv) (geraadpleegd 2026-10-04). **Aanvulling §4.**

### 5.3 Gebiedsaanpak Wesepe

> "Een integrale gebiedsaanpak Wesepe te starten. De financiële middelen via een separaat collegevoorstel in te dienen bij de Regio Deal Regio Zwolle II (17612-2025) […], waarbij de gebiedsaanpak Wesepe in Gebiedsarrangement Salland één van de drie projecten is die Olst-Wijhe (mede) indient. […] Wesepe is in de omgevingsvisie aangewezen als groeikern vanwege de gunstige ligging."

— Bron: B&W besluiten 22-04-2025, punt 10 (archive.csv) (geraadpleegd 2026-10-04). Volgordelijst: "Gebiedsaanpak Wesepe | Meerdere locaties | 2029 | 6 | 88". Het bedrag van € 353.634 uit het concept is in mijn bronnen **niet gevonden**. Raadpleeg het separate collegevoorstel (zaak 17612-2025).

### 5.4 Inwonerpanel wonen (19-5-2026)

> "Maar liefst 420 inwoners hebben de vragenlijst ingevuld. […] Van degenen die willen verhuizen, wil twee derde in Olst-Wijhe blijven. […] Met name in de kleinere kernen wordt een tekort aan voorzieningen ervaren (52%). […] Het merendeel van de deelnemers wil graag een koopwoning en meer dan twee derde staat open voor nieuwe woonvormen, waarbij 25% animo heeft voor zelfbouw. Onder ouderen is ook draagvlak voor appartementen. […] Onder jongeren is dit minder het geval; zij staan wel meer open voor bijvoorbeeld woningsplitsing. […] De resultaten nemen we mee in het nieuwe woonbeleid dat in de maak is."

— Bron: Resultaten inwonerpanel over wonen in Olst-Wijhe bekend, gemeente, 19-5-2026 (archive.csv; URL uit het concept gaf 404) (geraadpleegd 2026-10-04). Het panel liep tot 15-3-2026 (gemeente 17-2 en 9-3-2026).

**Correctie §12:** toevoegen dat **meer dan twee derde openstaat voor nieuwe woonvormen en 25% animo heeft voor zelfbouw**. Dit is het sterkste lokale behoeftesignaal voor CPO of zelfbouw.

### 5.5 "Focus op Wonen werpt vruchten af" (13-3-2026)

> "In 2022 besloot onze raad om tot 2032 1000 tot 1200 woningen te bouwen. Onze Focus op Wonen werpt z'n vruchten af en dat wordt ook landelijk opgemerkt. Zoals onlangs door de NOS en Oost. En deze week in een bericht van Vereniging Eigen Huis. […] 'Zo vindt in de gemeente Olst Wijhe 41 procent van de huiseigenaren dat de gemeente genoeg doet voor betaalbare koopwoningen.'"

— Bron: woonnieuws 13-3-2026 (archive.csv) (geraadpleegd 2026-10-04). Jaarrekening 2025: "Zo zijn er in 2025 ruim 70 woningen gerealiseerd, waarvan een groot deel in het betaalbare segment." (gemeente, 29-5-2026). Bestuursakkoord: "bijna 450 woningen" in de bestuursperiode 2022-2026.

### 5.6 Prestatieafspraken SallandWonen

> "De komende twee jaar worden ruim 200 sociale huurwoningen in Raalte en Olst-Wijhe nieuw gebouwd. Dat hebben woningcorporatie SallandWonen, Huurdersvereniging Salland, Huurdersbelangen Salland en de gemeenten Raalte en Olst-Wijhe vastgelegd in de nieuwe prestatieafspraken voor de periode 2025-2026. […] zetten de gemeenten Raalte en Olst-Wijhe, SallandWonen en de provincie samen de komende jaren in op het project Wooncoach […]."

— Bron: Samen sterk voor goed wonen in Salland: Prestatieafspraken 2025 – 2026, Bouwen in het Oosten, 10-12-2024, https://www.bouweninhetoosten.nl/samen-sterk-voor-goed-wonen-in-salland-prestatieafspraken-2025-2026/ (geraadpleegd 2026-10-04)

> "De pilot Wooncoaches met SallandWonen en de gemeente Raalte te verlengen voor de duur van één jaar (t/m 31 december 2027). […] De provincie Overijssel stopt na de pilotperiode met cofinanciering, omdat sprake was van een 'aanjaag-/innovatiesubsidie'. […] Het verlengen van de pilot Wooncoaches is onderdeel van de nieuwe Prestatieafspraken voor 2027-2028."

— Bron: B&W besluiten 22-09-2026, punt 05 (archive.csv) (geraadpleegd 2026-10-04)

**Correctie §12:** "'versneld 76 woningen' in Olst-Wijhe" staat **niet** in het artikel van Bouwen in het Oosten. Waarschijnlijk is het verward met de **76 flexwoningen** die gemeente en SallandWonen in 2023 "versneld" bouwden (https://wonen.olst-wijhe.nl/flexwonen). Schrappen of herformuleren. Aanvullen: er komen **nieuwe prestatieafspraken 2027-2028** (in voorbereiding, B&W 22-9-2026). De inhoud daarvan is niet gevonden.

### 5.7 Volkshuisvestingsprogramma en nieuwe betaalbaarheidslijn (A3/A4)

> "De oude Woonvisie van de gemeente is begin dit jaar verlopen. Daarom werkt het college nu aan een nieuw Volkshuisvestingsprogramma. Dit plan moet uiterlijk in de zomer van 2027 klaar zijn. […] Minstens twee derde van al deze nieuwe huizen moet namelijk betaalbaar zijn. Dat houdt in dat de koopprijs op dit moment maximaal 420.000 euro mag zijn. Ook moet dertig procent van alle woningen in de gemeente bestaan uit sociale huur."

— Bron: Betaalbaar wonen en minder afval in Olst-Wijhe, Wijhe City, 24-8-2026, https://wijhecity.nl/2026/08/24/betaalbaar-wonen-en-minder-afval-in-olst-wijhe/ (geraadpleegd 2026-10-04). Dit is een journalistieke samenvatting van de B&W-besluiten van 18-8-2026.

Lokale binding, starters en CPO als instrument:

> "Het stellen van lokale bindingseisen mag alleen bij nieuwbouwwoningen tot de betaalbaarheidsgrens (< € 405.000) en bij maximaal 50% van de nieuwbouw worden toegepast. Er moet dan sprake zijn van aantoonbare schaarste. Als gemeente zetten we nu vooral in op andere instrumenten zoals de Starterslening, […] het regelen van betaalbare woningbouw (onder andere 30% sociale huur en koopwoningen tot € 260.000) en het gebruikmaken van het instrument CPO (collectief particulier opdrachtgeverschap)."

— Bron: B&W besluiten 11-11-2025, punt 12 "Beantwoording vragen VVD fractie aangaande erfpacht en lokale bindingseisen bij nieuwbouw koopwoningen" (archive.csv) (geraadpleegd 2026-10-04). **Belangrijk voor §1:** het college noemt **CPO expliciet als instrument** voor lokale binding (november 2025).

> "Om in aanmerking te komen voor de lening moet het de eerste keer zijn dat de aanvrager een woning koopt èn kost de woning maximaal € 378.000,- (prijspeil 2026). Het leenbedrag via de Starterslening is maximaal € 35.000,-. […] Daarnaast willen we lokale starters helpen; mensen die in Olst-Wijhe wonen of gewoond hebben."

— Bron: Olst-Wijhe stuurt op lokale binding bij Starterslening voor kopen van huis, woonnieuws 15-5-2026 (archive.csv); B&W 02-06-2026 punt 3 (voorstel "Verordening Starterslening gemeente Olst-Wijhe 2026", € 350.000 per jaar voor 2026 en 2027). Het raadsbesluit is **niet gevonden**.

### 5.8 Woondeal: extra opgave voor Olst-Wijhe? (tegenstrijdigheid 6)

> "Tegelijkertijd zijn er ook West-Overijsselse gemeenten die juist een sterke woningbouwproductie laten zien. In een aantal van deze gemeenten (zoals Deventer, Hardenberg, Olst-Wijhe en Raalte) wordt zelfs onderzocht of er, bovenop de huidige programmering, kansen zijn om extra woningen te bouwen. Dankzij deze bijdragen blijft de regio als geheel goed op koers […]."

— Bron: Actualisatie Woondeal West-Overijssel 2025 t/m eind 2030 (20-3-2025), p. 5, https://overijsselsewoonaanpak.nl/media/xhadtdva/20250325_524100_woondeal-west-overijssel-digitaal-toegankelijk.pdf (geraadpleegd 2026-10-04)

> "In de Woondeal voor de regio West-Overijssel wordt onze gemeente genoemd, naast de gemeenten Deventer, Hardenberg, Raalte en Staphorst, om de woningbouwopgave voor elkaar te krijgen. Met het besluit van de raad (2022) om tot 2032 zo'n 1000 tot 1200 woningen te bouwen, zijn wij volgens de provincie al goed op streek. Goede opsteker: vier van onze nieuwbouwprojecten zijn aangewezen als sleutelproject […]. De vier sleutelprojecten zijn MEKO-terrein in Wesepe, Wijhe Noord in Wijhe, de vrijkomende scholenlocaties in Wijhe en Olst Zuid in Olst."

— Bron: Nieuwe Woondeal voor West-Overijssel, woonnieuws 15-4-2025 (archive.csv) (geraadpleegd 2026-10-04)

Woondeal Bijlage 1 (Olst-Wijhe): "Olst Aberson terrein Bestaand 65 66 / Olst scholenlocatie Bestaand 65 66 / Olst Olstergaard Bestaand 80 104 / Wijhe scholenlocaties Bestaand 25 124 / Wijhe Wengelerhoek Bestaand 200 200 / Wijhe Noord Nieuw - 100 300 / Olst-Zuid Project Nieuw - 100 - / Wesepe (Meko-Locatie) Nieuw - 81 - / Totaal Olst-Wijhe 435 841 300". Kolommen: woningen volgens Woondeal 2022; woningen 2024-eind 2030; doorkijk na 2030.

**Tegenstrijdigheid 6, beoordeling:** het gemeentebericht van 15-4-2025 zegt **niet letterlijk "geen extra opgave"**. Het zegt "al goed op streek". De Woondeal legt **geen vaste extra aantallen per gemeente** op. Olst-Wijhe is wel een van de gemeenten waar "onderzocht [wordt] of er, bovenop de huidige programmering, kansen zijn om extra woningen te bouwen". **Opgelost voor zover de Woondeal reikt:** er is geen formele extra opgave, wel een onderzoeksafspraak. Of de Zwolse beslisnota van 14-4-2025 een aantal noemt, valt buiten mijn brontype. Verder telt de gemeente "vier sleutelprojecten" (de nieuwe en uitgebreide) en de Woondeal-bijlage **acht**. Beide kloppen, omdat de Woondeal ook de bestaande projecten meetelt [INT]. Corrigeer §5, waar het concept "sleutelprojecten (namen uit samenvattingen)" noemt: de volledige lijst staat hierboven.

---

## Prioriteit 6: Overige recente berichten (juli-oktober 2026)

- **Volgordelijst netcongestie** (zie prioriteit 4).
- **Olstergaard officieel afgerond** op 2-10-2026 (gemeente, 29-9-2026).
- **Holsthoek Den Nul:** 19 woningen, raadsbesluit gepland op 7-9-2026; de uitkomst is niet gevonden.
- **Boer met plan voor ouderenhuurwoningen op bijna 6.000 m2 vrijkomende agrarische grond** (HierinSalland, 18-7-2026; §2.12).
- **Marledijk 33 (LBV+) en Rijksstraatweg 4 (LBV):** stoppende veehouderijen; "Agrarische bedrijven maken plaats voor wonen" (Wijhe City, 19-9-2026).
- **"Grond voor toekomst in Salland"**, informatie- en netwerkavond voor grondeigenaren op 8-10-2026 op de Boerhaar (gemeente, 23-9-2026).
- **Kernenbezoek Wijhe op 9-9-2026 met woningbouw als thema:** "Daarom bouwt de gemeente Olst-Wijhe tot 2032 ruim duizend nieuwe woningen verspreid over de gemeente. […] programmamanager Wietze van der Ploeg [laat] op een digitale kaart zien welke woningbouwprojecten er zijn" (Salland Centraal, 11-9-2026, https://www.sallandcentraal.nl/2026/09/woningbouw-centraal-tijdens-kernenbezoek-wijhe/). Wietze van der Ploeg is een **ambtelijk aanspreekpunt (programmamanager wonen)** voor §9. Contactgegevens zijn niet gevonden.
- **Sterappel 12, Olst (Olstergaard):** "plannen ingediend voor de bouw van de rechterhelft van een twee-onder-een-kapwoning" (Wijhe City, 19-9-2026).
- **Begroting 2027:** structureel tekort van € 1,4 mln ("sommige plannen later worden uitgevoerd of in een andere vorm doorgaan"; Salland Centraal, 9-9-2026) en een raadsinformatiebrief over de "voortgang structurele bezuinigingsopgave bedrijfsvoering" na een gesprek met de provincie (B&W 22-9-2026, punt 07). Risico [INT]: minder ambtelijke capaciteit voor initiatieven van derden.
- **Legesverordening 2027 op basis van 100% kostendekkendheid** (B&W 22-9-2026, punt 08): "Vast te stellen dat de niet wettelijk vastgestelde leges vanaf 2027 worden gebaseerd op 100% kostendekkendheid […]". Relevant voor §11. Doorgeven aan deelonderzoek 1/4.
- **Tiny houses:** alleen in Olstergaard gevonden. Geen nieuw tiny-house- of kavelbeleid gevonden. De kavelwinkel heeft op 2026-10-04 geen kavels.

---

## Tabel A: Praktijkvoorbeelden (§6)

| # | Naam / omschrijving | Datum | Bron-URL (geraadpleegd 2026-10-04) | Relevantie voor ons concept |
|---|---|---|---|---|
| 1 | **Erveweg / Hemelrijk-2, Welsum:** circa 18 koopwoningen (2 vrijstaand, 4 2^1-kap, 12 rij) van grondeigenaren op grond met agrarische en volkstuinbestemming aan de rand van Welsum; omgevingsplanwijziging/BOPA; instemming van provincie en ketenpartners als voorwaarde | B&W 10-3-2026; woonnieuws 13-3-2026 | B&W-archief (archive.csv) en woonnieuws (archive.csv); voorlopige lijst Gmb 2026, 422235 | **Zeer hoog:** schaal 10-20 op agrarische grond aansluitend aan een kleine kern; college positief |
| 2 | **Engeweg, Elshof:** 8 woningen (3×2^1-kap + 2 vrijstaand) op twee agrarische percelen; BOPA, anterieure overeenkomst, Oversticht-erfplan, verkleinde spuitzone; grondeigenaren Dijk en Schrijver; kopers met binding | B&W 3-2-2026; Salland1 9-2-2026 | https://www.salland1.nl/college-olst-wijhe-stemt-in-met-bouw-acht-woningen-op-de-elshof/ | **Hoog:** agrarisch naar wonen in een buurtschap, schaal 8 |
| 3 | **CPO Boerhaar:** circa 22-24 starterswoningen (vereniging van 26-39 leden), schoollocatie + Boerhaar 18/18a; krediet € 1,1 mln; bouwclaim met Bouwbedrijf Meijer | 3-7-2025 t/m 9-2026 | https://www.sallandcentraal.nl/2025/07/cpo-boerhaar-officieel-opgericht/ ; https://hierinsalland.nl/pvda-stelt-collegevragen-over-nieuwbouwprojecten-op-de-boerhaar/ ; https://hierinsalland.nl/boerhaar-aannemer-zonder-naam/ ; https://wijhecity.nl/2026/05/15/voornemen-verkoop-bouwgrond-boerhaar-18-20-wijhe/ | **Hoog:** grootste CPO in de gemeente; laat de gemeentelijke werkwijze zien (traag, krediet, bouwclaim, Didam-1-op-1) |
| 4 | **CPO Herxen:** 3 woningen op een onbebouwd perceel achter Herxen 7a (Kromme Koeweg) + **bestuurlijke afspraken B&W–GS** om dit in procedure te brengen vóór het visietraject | B&W 2-6-2026; herxen.nl 22-9-2026 | gemeente 2-6-2026 (archive.csv) / https://wijhecity.nl/2026/06/02/gezamenlijke-visie-voor-woningbouw-in-herxen/ ; https://www.herxen.nl/2026/09/22/woningbouw-en-woningvisie-herxen/ | **Hoog:** CPO op onbebouwde grond in een kleine kern, met provinciale voorkant |
| 5 | **Grolleman, Herxen 63:** 15 koopwoningen op een vrijkomend bedrijfsterrein, BOPA, provincie positief | B&W 23-9-2025 | woonnieuws 26-9-2025 (archive.csv) | Midden-hoog: transformatie in een kleine kern, schaal 15 |
| 6 | **'t Kleiland, Kleistraat Olst:** 20 woningen (5 sociale huur, 8 sociale koop, 7 vrij) op grond met agrarische bestemming; raad bindend advies 9-2-2026, BOPA 17-3-2026 | 2025-2026 | woonnieuws 20-3-2026 (archive.csv) | Midden-hoog: route raad-advies → BOPA voor een uitleglocatie |
| 7 | **De Klimboom, Boskamp:** 9 CPO-woningen (jonge Boskampenaren, Vosman) + 4 sociale huur + 4-5 betaalbaar (inschrijving open voor CPO-groepen, april 2026) | 2024-2026 | https://wonen.olst-wijhe.nl/deklimboomboskamp | Hoog: gemeentelijk CPO-spoor op schaal 9, op gemeentegrond |
| 8 | **Buurtschappenbeleid / Elshof 6c-e:** 3 starterswoningen op agrarisch perceel | principe 9-11-2021; raad 19-9-2022 | https://olstwijhe.bestuurlijkeinformatie.nl/Document/View/f561bc20-c863-45fc-ae1f-f6d03d7ab205 | Midden-hoog: beleidsbasis voor wonen met binding in buurtschappen |
| 9 | **Volgordelijst netcongestie:** 47 → 31 projecten; o.a. **De Brinkweiden (Kappeweg 18, 12 won., buitengebied)** en **Wijlandhof (Elshof, 12 won.)** | 11-8 t/m 1-10-2026 | https://zoek.officielebekendmakingen.nl/gmb-2026-422235.html ; netcongestiepagina | **Hoog:** bepaalt het tempo; toont twee onbekende 12-woningeninitiatieven |
| 10 | **Kloosterhoekweg 3, Welsum:** 2 woningen rood-voor-rood; maatwerk spuitzone < 50 m | B&W 21-4-2026 | B&W-archief | Midden: spuitzone als toetspunt |
| 11 | **Lierderholthuisweg 3, Wijhe:** splitsing + 1 extra woning na sloop + 1,5 ha bos; BOPA | B&W 20-1-2026 | B&W-archief | Midden: erftransformatie onder KGO |
| 12 | **Vettewinkelweg 2, Wijhe:** 1 extra woning na sloop; provinciale toestemming vereist | B&W 23-1-2024 | B&W-archief | Midden |
| 13 | **Woningsplitsing:** 16 verzoeken (14 buiten de bebouwde kom), mei 2024-eind 2025; Bokkelerweg 1 en Engeweg 10/10A (KGO-splitsing) | 2024-2026 | woonnieuws 28-5-2026; https://www.salland1.nl/gemeente-olst-wijhe-ziet-kansen-voor-woningsplitsing-elke-woning-die-we-extra-beschikbaar-hebben-is-er-een/ | Midden |
| 14 | **Boer met plan voor ouderenhuurwoningen op circa 6.000 m2 vrijkomende agrarische grond** (oppositie steunt) | 7-2026 | https://hierinsalland.nl/onze-man-in-wijhe-toon-schuiling-8/ | Midden: vergelijkbaar initiatief; provincie "niet heel happig" |
| 15 | **Motie "meer en betere aandacht voor (bouw)activiteiten uit de samenleving"**, aangenomen 11-6 tegen collegeadvies | 6-2026 | https://hierinsalland.nl/onze-man-in-wijhe-toon-schuiling-6/ | Midden-hoog: politiek draagvlak voor bottom-up |
| 16 | **Omgevingsvisie vastgesteld 12-5-2025**, amendement over de zone rond kleine kernen | 12-5-2025 | https://www.nieuweoogst.nl/nieuws/2025/05/14/omgevingsvisie-olst-wijhe-kan-op-goedkeuring-landbouwsector-rekenen | Context |
| 17 | IJsseldal (81), Olst Zuid (circa 90), scholenlocaties Olst (59), Matzer/Mijnpleinschool (circa 44 sociaal), Holsthoek (19), Wengelerhoek (135), Wijhe Noord (circa 300) | 2025-2026 | woonnieuws (archive.csv); Wijhe City | Laag/context |
| 18 | Bokkelerweg Wesepe: **6 plattelandskamers** (geen woningen), besluit uitgesteld | 9-2026 | https://wijhecity.nl/2026/09/19/laadpalen-renovaties-en-nieuwe-woningen-voor-olst-wijhe/ | Laag |

## Tabel B: Bestaande initiatieven (§7)

| Initiatief | Aantal woningen | Status (2026-10-04) | Citaat / bron |
|---|---|---|---|
| **Vriendenerf, Olst** (Ringmus 50; CPO 55+; Hunebouw/GroenBlauw/Building Community) | 12 koopwoningen + Deelhuis | Gerealiseerd 2016-2017 (opening 30-9-2017); open dag 31-10-2026 | "12 in totaal verdeeld over 4 blokjes; Een gemeenschappelijk, multifunctioneel 13e huis, ons Deelhuis" (vriendenerf.nl) |
| **Grijs & Groen Wonen, Olstergaard** (CPO 50+, nu VvE) | 11 appartementen + gemeenschappelijke ruimten ("De Pit") | Gebouwd 2023, bewoond sinds maart 2024 | "We bouwden als CPO […]. Inmiddels zijn we een VVE geworden." (grijsengroenwonen.nl) |
| **Olstergaard, Olst** (particulier opdrachtgeverschap, natuurinclusief; tiny houses) | 72 (48 koop PO + 13 huur + 11 G&G) | Afgerond; feest op 2-10-2026 | "De 72 woningen zijn een mix van vrijstaande woningen, twee-onder-een-kapwoningen en rijwoningen." (wonen.olst-wijhe.nl/olstergaard) |
| **CPO Boskamp, De Klimboom** | 9 (van 17-18) | Bouw sinds zomer 2025; oplevering gepland vóór zomer 2026 (niet bevestigd) | "9 koopwoningen door lokale CPO-groep (4 2-onder-1-kappers en 5 rijwoningen)" |
| **CPO Boerhaar** | circa 22-24 | Krediet € 1,1 mln voorgelegd aan raad 26-5-2026 (uitkomst niet gevonden); bouwclaim met Meijer; projectrijpheid 4 op voorlopige netlijst | "De vereniging telt 26 leden en 10 partnerleden, allen met binding met de Boerhaar." (PvdA-vragen, 17-12-2025) |
| **CPO Herxen** | 3 | Principetoezegging B&W 2-6-2026; aanvullende gegevens opgevraagd | "drie woningen als onderdeel van een C(ollectief) P(articulier) O(pdrachtgeverschap)" |
| **Aardehuizen, Olst** (ecologisch, Earthship) | 23 + Middenhuis | Gerealiseerd (jaartal niet in bron) | "ecologische woonwijk met 23 woningen en een gezamenlijk Middenhuis" (aardehuis.nl) |
| **Engeweg, Elshof** (grondeigenaren, geen CPO) | 8 | Principebesluit 3-2-2026; BOPA en anterieure overeenkomst volgen | zie §2.1 |
| **Erveweg/Hemelrijk-2, Welsum** (grondeigenaren, geen CPO) | circa 18 | Principebesluit 10-3-2026 | zie §2.7 |
| **De Brinkweiden, Kappeweg 18** | 12 | Op de volgordelijst (start 2028, projectrijpheid 6); inhoud onbekend | volgordelijst |
| **Wijlandhof, Elshof (19a)** | 12 | Op de volgordelijst (start 2027, projectrijpheid 6); inhoud onbekend | volgordelijst |
| **Stationsweg Wijhe: woon-zorginitiatief van ouders** (collectief) | onbekend (gebiedsplan) | Intentiebrief maart 2026; plan eind 2026 | woonnieuws 12-3-2026 |
| **Flexwoningen** (SallandWonen) | 76 (50 Wengelerhoek + 26 Vink) | In gebruik sinds 2023 | wonen.olst-wijhe.nl/flexwonen |
| *Wooncommunity De Ware* | 24 studio's | Geopend 13-3-2025, **in Raalte** | gemeente 14-3-2025: niet aan Olst-Wijhe toerekenen |

Een CPO of collectief project **op agrarische grond in het open buitengebied** is ook in deze ronde **niet gevonden**. De dichtstbijzijnde analogieën zijn Hemelrijk-2 (18 woningen, rand Welsum), Engeweg (8 woningen, Elshof), CPO Herxen (3 woningen, onbebouwd perceel in een kleine kern) en de nog onbekende De Brinkweiden (12 woningen, "buitengebied").

---

## Tegenstrijdigheden (concept, lijst 1-20): status vanuit dit brontype

| Nr. | Status | Toelichting / citaat |
|---|---|---|
| 1 (maxima 5/10) | Niet oplosbaar met nieuwsbronnen | De nieuwsberichten over woningsplitsing noemen geen maxima. Beleidspagina lezen (deelonderzoek 1). |
| 3 (vaststelling Omgevingsvisie) | **Opgelost: 12 mei 2025** | Nieuwe Oogst: "raadsvergadering van maandag 12 mei", amendement unaniem. |
| 6 (extra Woondeal-opgave) | **Grotendeels opgelost** | Geen vaste extra opgave; Olst-Wijhe is wel genoemd als gemeente waar "onderzocht [wordt] of er, bovenop de huidige programmering, kansen zijn om extra woningen te bouwen" (Woondeal p. 5). Gemeente: "al goed op streek". |
| 7 (plancapaciteit 161/339) | Niet opgelost | Nieuwe kengetallen: voorlopige volgordelijst 47 regels/1.400 woningen; definitief 31/774 (excl. vooraanmeldingen). Dit is geen plancapaciteitsdefinitie. |
| 9 (aantal kernen) | **Opgelost: 12** | Kernenwethouder-indeling in het bestuursakkoord p. 23; GB: "twaalf sterke en leefbare kernen". |
| 10 (verkiezingscijfers) | **Opgelost** | 9.244 stemmen op kandidaten (= som partijen), 9.325 uitgebracht, 15.511 kiesgerechtigden, opkomst 60,1% (P 22-2). |
| 11 (Olstergaard) | **Opgelost: 72** | 48 + 13 + 11 (wonen.olst-wijhe.nl/olstergaard). Woondeal-sleutelprojectcijfers (80/104) zijn een andere grootheid. |
| 12 (Klimboom) | **Opgelost** | 17-18 = 9 CPO + 4 sociale huur + 4-5 betaalbaar; netlijst 18. |
| 13 (Grijs & Groen / Vriendenerf) | **Opgelost: twee projecten** | Ringmus 50 (2017, 12 + Deelhuis) versus Olstergaard (2023, 11 appartementen). |
| 15 (CPO "5 tot circa 50") | Niet gevonden in nieuwsbronnen | Niet gebruiken. |
| 16 (Nota Grondbeleid 2023-2026 versus 2024-2028) | Niet opgelost | Grondbeleid valt nu onder Olthof (akkoord); verder geen nieuws gevonden. |
| 17 (Gmb-nummers netcongestie) | **Opgelost** | 415179 = Brunssum, 421329 = Lansingerland; juist: **385444** (beleidsregels, 13-8-2026) en **422235** (voorlopige lijst, 10-9-2026). |
| 18 (portefeuille Blind) | **Opgelost** | Blind: Wonen, RO en omgevingsplannen e.a.; **Olthof: grondbeleid, toekomstbestendige kernen en buitengebied, gebiedsgerichte aanpak, Regio Zwolle**. |
| 19 (Engeweg-woningtypen) | **Opgelost** | 3 tweekappers = 6 woningen + 2 vrijstaand = 8. |
| 20 (systematisch) | Deels verholpen | Alle bovenstaande citaten zijn uit de brontekst zelf. |

---

## Bijlage A-punten die dit brontype raakt

| # | Bevinding | Status | Bron (geraadpleegd 2026-10-04) |
|---|---|---|---|
| A1 | Olst-Wijhe valt onder "overige kern" [PB]. Bestuursakkoord: "Wesepe als derde grote kern". "Regio Zwolle" is een portefeuille van Olthof; de gebiedsaanpak Wesepe wordt ingediend bij de "Regio Deal Regio Zwolle II" | Deels gevonden | Bestuursakkoord p. 4, 23; B&W 22-4-2025 |
| A2 | Woondeal: 8 sleutelprojecten/841 woningen (bijlage), gemeente telt er 4. Geen vaste extra opgave, wel onderzoek naar extra kansen. Volgordelijst: 47 initiatieven/1.400 woningen (voorlopig). Harde/zachte plancapaciteit, 80/20-ruimte en CPO in de planmonitor: niet gevonden | Deels gevonden | Woondeal p. 5, Bijlage 1; woonnieuws 15-4-2025; Gmb 2026, 422235 |
| A3 | Nieuwe lijn: ≥ 2/3 betaalbaar, koop ≤ € 420.000, 30% sociale huur (Wijhe City 24-8-2026). Akkoord: 70% betaalbaar. Lokale binding alleen < € 405.000 en ≤ 50% van de nieuwbouw; "koopwoningen tot € 260.000"; Starterslening ≤ € 378.000 met binding. **CPO door college genoemd als instrument** (11-11-2025). Prestatieafspraken 2025-2026 (> 200 sociale huurwoningen Raalte + Olst-Wijhe); 2027-2028 in voorbereiding | Deels gevonden | zie §5.6-5.7 |
| A4 | Volkshuisvestingsprogramma "uiterlijk in de zomer van 2027 klaar" (Wijhe City 24-8-2026); akkoord: "We ontwikkelen een Volkshuisvestingsprogramma." Geen ontwerp gevonden | Niet gevonden (in voorbereiding) | Wijhe City 24-8-2026; akkoord p. 8 |
| A5 | Pilot Wooncoaches (55-85 jaar) verlengd t/m 2027; provincie stopt met cofinanciering. Inwonerpanel: senioren willen in eigen woning blijven; draagvlak voor appartementen. De Ware ligt in Raalte | Deels gevonden | B&W 22-9-2026; gemeente 19-5-2026 |
| C4 | **Netcongestie:** beleidsregels Gmb 2026, 385444; criteria art. 9; 47 aangemeld; definitieve lijst eind september 2026 (31 projecten); indiening vanaf 1-10-2026; aparte categorie "collectieve woonvormen"; tweede ronde niet gevonden | Gevonden | netcongestiepagina; Gmb 2026, 385444 en 422235; B&W 15-9-2026 |
| D1 | Deelname aan subsidie 4.39 of een intergemeentelijk programma: niet gevonden in nieuws. Wel Salland Loont (Raalte, Deventer, Olst-Wijhe; € 17.000 + € 75.000 uit het fonds ruimtelijke kwaliteit) en "Grond voor toekomst in Salland" (8-10-2026) | Niet gevonden (4.39) | B&W 28-10-2025; gemeente 23-9-2026 |
| D2 | **Erfcoach: Yvonne in 't Veld** (Dalfsen, Olst-Wijhe, Ommen, Hardenberg; 06 10 98 22 76; ygw.in.t.veld@overijssel.nl). Niek Oude Scholten staat niet meer op de lijst. Akkoord: "We adviseren boeren die hun bedrijf willen transformeren of willen stoppen." Atelier Overijssel/Rijkshandreiking niet gevonden | Gevonden | erfcoachoverijssel.nl/contact-met-de-erfcoaches/ |
| D3 | Precedenten: Lierderholthuisweg 3, Vettewinkelweg 2, Kloosterhoekweg 3 (rood voor rood, spuitzone), Engeweg 10/10A en Bokkelerweg 1 (KGO-splitsing), Marledijk 33/31a (LBV+). **Buurtschappenbeleid Herxen/Elshof** (2007/2010/2020). Een boer met ouderenhuurplan (juli 2026). Geen collectief VAB-precedent | Deels gevonden | B&W-archief; raadsvoorstel Elshof 6c-e |
| E1 | **Bestuurlijke afspraken B&W–GS over het visietraject Herxen** (2-6-2026; CPO Herxen kan al in procedure); gedeputeerde Grijsen betrokken. Provincie positief over Grolleman. Vettewinkelweg: "toestemming […] van de provincie". Naam van de accounthouder niet gevonden | Deels gevonden | B&W 2-6-2026, 23-9-2025, 23-1-2024 |
| E4 | Geen provinciale zienswijze, onthouden instemming of aanwijzing gevonden in het nieuws 2024-2026. Wel een signaal: "De provincie […] is daar niet heel happig op" (raadslid, juli 2026) | Niet gevonden | HierinSalland 18-7-2026 |
| F1 | Provinciale cofinanciering van Wooncoaches (stopt na 2026); Regio Deal Regio Zwolle II (gebiedsaanpak Wesepe); Leader (pluktuin; wethouder Olthof is LAG-voorzitter volgens HierinSalland 21-8-2026). Toepasbaarheid op een CPO: niet gevonden | Deels gevonden | B&W 22-9-2026, 22-4-2025 |

---

## Correcties per paragraaf van `gemeente_olst-wijhe.md` (samengevat)

- **Verantwoording:** concept-URL's van het type `.../nieuwsberichten/2026/m/d/slug` en `wonen.olst-wijhe.nl/woonnieuws/woonnieuws/2026/m/d/slug` gaven op 2026-10-04 meestal een 404. Verwijs naar de archive.csv-bestanden of de maandoverzichten.
- **Kernen:** 12 (zie tegenstrijdigheid 9).
- **§1:** CPO Boerhaar en CPO Herxen toevoegen. College 11-11-2025: "het gebruikmaken van het instrument CPO". De verkoop van Klimboom-kavels stond open voor CPO-groepen. Het akkoord noemt CPO niet.
- **§2:** omgevingsvisie vastgesteld 12-5-2025 (unaniem); details van het amendement. Volkshuisvestingsprogramma uiterlijk zomer 2027. Herxen: B&W 2-6-2026 met bestuurlijke afspraken met GS. Buurtschappenbeleid toevoegen.
- **§3a:** KGO-artikel van 9-2-2021; fonds "Voorziening Ruimtelijke Kwaliteit"; "1,4 per erf" is eigen afleiding.
- **§3b:** Engeweg = 3×2^1-kap + 2 vrijstaand (8), met verkleinde spuitzone. Hemelrijk-2 Welsum (circa 18) en Kleiland (20, agrarisch) toevoegen. Vettewinkelweg: in de besluittekst staat "toestemming … van de provincie", niet "provincie gaf in vooroverleg aan te kunnen instemmen".
- **§3d:** de spuitzone van 50 m (gewasbeschermingsmiddelen) is een kansarm-factor. Afwijken kan met een locatiespecifiek onderzoek (Engeweg, Kloosterhoekweg).
- **§3e/§9:** contact zowel Blind (wonen, RO) als **Olthof (buitengebied, grondbeleid, gebiedsgerichte aanpak)**; kernenwethouder per kern. Ambtelijk: programmamanager wonen Wietze van der Ploeg; netcongestie: netcongestieow@olst-wijhe.nl.
- **§4:** Erfcoach: Yvonne in 't Veld. Salland Loont-bedragen toevoegen.
- **§5:** netcongestie-nummers en -criteria (Gmb 385444/422235); 47 → 31 projecten; De Brinkweiden en Wijlandhof (12 woningen elk). Kleistraat = 't Kleiland, BOPA 17-3-2026. Lijst sleutelprojecten Woondeal (8).
- **§6/§7:** tabellen A en B hierboven. Grijs & Groen en Vriendenerf zijn twee projecten. Flexwonen 76 (50 + 26). De Ware ligt in Raalte. "Bokkelerweg" gaat over plattelandskamers.
- **§10:** geen coalitie in vorming; naamswijziging Olst-Wijhe Vooruit; uitslag/opkomst; portefeuilles; akkoordpassages; "+400" = gemiddeld 100 per jaar; motie bouwinitiatieven 11-6.
- **§11:** legesverordening 2027 op basis van 100% kostendekkendheid (B&W 22-9-2026).
- **§12:** inwonerpanel: 25% animo voor zelfbouw, > 2/3 open voor nieuwe woonvormen. "Versneld 76" schrappen; prestatieafspraken 2027-2028 in voorbereiding.

---

## Niet gevonden (met vindplaats)

1. **Coalitiecrisis of collegewijziging na 16-6-2026:** niet gevonden. Dit is een negatieve bevinding na doorzoeking van het gemeentelijk nieuws, de B&W-lijsten t/m 22-9-2026, Salland1, Salland Centraal, Wijhe City en HierinSalland. De Stentor was niet toegankelijk. Controle: https://gemeenteraad.olst-wijhe.nl en iBabs (raadsvergaderingen september/oktober 2026).
2. **Raadsbesluit 26-5-2026 over het Boerhaar-krediet (€ 1,1 mln):** niet gevonden. Vindplaats: iBabs, besluitenlijst raad 26-5-2026.
3. **De Brinkweiden (Kappeweg 18, 12 woningen, buitengebied) en Wijlandhof (Elshof, 12 woningen):** inhoud en initiatiefnemer niet gevonden. Vindplaats: team Ruimte en Samenleving / netcongestieow@olst-wijhe.nl, toekomstige B&W-lijsten.
4. **Feitelijke indiening bij Enexis na 1-10-2026 en de reactie van de netbeheerder; een tweede aanmeldronde:** niet gevonden. Vindplaats: netcongestiepagina, nieuws van oktober 2026.
5. **Uitkomst van de Klimboom-inschrijving (april-mei 2026) en de oplevering van de CPO-woningen:** niet gevonden. Vindplaats: kavelwinkel, woonnieuws.
6. **Raadsbesluit Holsthoek (gepland 7-9-2026) en Verordening Starterslening 2026:** niet gevonden. Vindplaats: iBabs.
7. **Bedrag gebiedsaanpak Wesepe (€ 353.634):** niet gevonden. Vindplaats: collegevoorstel zaak 17612-2025, Regio Deal Regio Zwolle II.
8. **"Tuinkamer" Olstergaard:** niet gevonden. Vindplaats: projectpagina en bewonersvereniging Olstergaard.
9. **Inhoud van de prestatieafspraken 2027-2028:** niet gevonden (in voorbereiding). Vindplaats: SallandWonen, raadsinformatiebrief.
10. **Initiatiefnemer en locatie van het plan van de boer met circa 6.000 m2 (juli 2026):** niet gevonden. Vindplaats: fractie Olst-Wijhe Vooruit (spreekuur Hendrik Droststraat 22a, Olst).
11. **Bestuursakkoord over CPO, collectief, zelfbouw, tiny houses, erf of VAB:** gecontroleerd, komt niet voor.
12. **De Stentor-artikelen** (o.a. 9-4-2026 over de Boerhaar-aannemer; "vader en moeder van Olst-Wijhe"): niet toegankelijk.
