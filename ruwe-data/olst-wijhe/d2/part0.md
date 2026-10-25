# Deelonderzoek 2: provinciaal-lokale toepassing, gemeente Olst-Wijhe (verificatieronde)

**Raadplegingsdata.** Reeds door eerdere runs opgehaalde bronnen: 2026-10-04. Nieuw opgehaald of opnieuw gecontroleerd in deze run: **2026-10-05** (elk citaat vermeldt zijn datum). Ruwe bestanden: `$S/d2/` (kaartbevragingen, WFS-uitvoer, planmonitor-uitvoer); hergebruikt: `$S/d1/`, `$S/d3/`, `$S/d4/`, `$S/ov.json`, `$S/ovisie.json`, `$S/caps.xml`, `$S/koers.txt`. De repo-bestanden zijn niet bewerkt. `$S` = `/tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad`.

Deelonderzoek 1 (bestuursinformatie) heeft de B&W-adviesnota's, de nota van beantwoording en de subsidie-4.39-stukken ook gelezen; waar dat het geval is verwijs ik ernaar en beperk ik mij tot de provinciale toepassing en wat daar nieuw bij komt.

## Samenvatting van de belangrijkste nieuwe bevindingen (leeswijzer)
1. **Kaartlagen zijn wel te bevragen** (concept: "niet geraadpleegd"). De provinciale viewer https://ruimtelijkeplannen.overijssel.nl heeft een open locatie-API op de geconsolideerde Omgevingsverordening (in werking per 1-7-2026, `nld@129`) en de Omgevingsvisie. Uitkomst: Engeweg/Elshof, Middel (Steunenbergerweg 6), Lierderholthuisweg 3, Bokkelerweg Wesepe, Prinshoeveweg en Kleistraat liggen in **landbouwgebied met generieke opgaven en kansen**; Vettewinkelweg 2, Marle, Welsum, Den Nul en Elshagenweg (Wesepe) in **landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur**. Over de hele gemeente is het agrarisch buitengebied ongeveer **50/50** verdeeld over beide typen (250 m-raster: 37,8% generiek, 38,2% gebiedsspecifiek van het gemeenteoppervlak). Kernen en buurtschappen (Olst, Wijhe, Wesepe, Boskamp, Herxen, Boerhaar, Elshof-kern) vallen buiten de landbouwgebieden. Vettewinkelweg 2 ligt **in** het grondwaterbeschermingsgebied Boerhaar. Zie §1.
2. **Provinciale Planmonitor (dataset "Harde en zachte woningbouwplannen (vlakken)", peildatum 1-1-2026) bevat "Engeweg Elshof" als _harde_ plancapaciteit (8 woningen, oplevering 2028)**, ook Zandhuisweg 7 (9 woningen), Steunenbergerweg 6 en Vettewinkelweg 2; "Grolleman, Herxen" (15) is zacht; het CPO Herxen (3) staat er niet in. Zie §1.6 en A2.
3. **Provinciale instemming:** in minstens 13 principebesluiten 2024-2026 staat de voorwaarde "provincie kan instemmen/akkoord/toestemming"; bij Engeweg staat letterlijk "Ook de provincie heeft al ingestemd met voorliggend plan", bij Vettewinkelweg 2 heeft de provincie in vooroverleg "aangegeven in te kunnen stemmen" en is de BOPA daarna verleend. Een formeel instemmingsbesluit is in geen register gepubliceerd (Prb publiceert dat niet). Zie §2.
4. **Omgevingstafel IJsselland: werkende URL is https://www.odijsselland.nl/over/omgevingstafel** (HTTP 200, 2026-10-05); de URL in `provincie_overijssel.md` §4.2 (`/omgevingstafel-ijsselland`) en ook `/omgevingstafel` geven 404. Zie §4.
5. **Gemeente en provincie hanteren bewust verschillende gebiedsindelingen** (RIB bouwsteen 9-6-2026). Dit is de kern van C1. Zie §1.7.
6. **Herxen:** B&W en GS hebben op 2-6-2026 een **bestuurlijke overeenkomst** gesloten (EUR 15.000 uitvoeringskosten 2026) waardoor initiatieven zoals het CPO Herxen alvast in procedure kunnen worden gebracht in afwachting van een visietraject tot 2050. Zie §5.1.
7. **E4 (provinciale zienswijzen/aanwijzingen/onthouden instemming 2023-2026): bevestigd negatief** voor concrete Olst-Wijhese plannen (Prb doorzocht door deelonderzoek 4, 69 treffers; ook ik vond niets), met de kanttekening dat instemmingen en vooroverlegreacties niet in het Prb staan. Wel is er een **positieve provinciale zienswijze** op de ontwerp-Omgevingsvisie Olst-Wijhe 2050 (zienswijze nr. 23) met een vraagteken bij Wesepe als hoofdkern. Zie §5.4.

---

## 1. Provinciale kaartlagen voor het buitengebied van Olst-Wijhe (C1, C3, B4, A1)

### 1.1 Gebruikte services en methode (nieuw, 2026-10-05)
| Service | Eindpunt | Inhoud | Gebruikt voor |
|---|---|---|---|
| Provinciale viewer Ruimtelijkeplannen Overijssel (open API achter de viewer; DSO-publicatie van de provincie) | `https://ruimtelijkeplannen.overijssel.nl/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044` (document "Omgevingsverordening provincie (in werking vanaf 1 juli 2026)", `eId` `/akn/nl/act/pv23/2023/omgevingsverordening/nld@129`) en `.../_locationSearch?x=<RD-x>&y=<RD-y>&distance=1` | Geometrische werkingsgebieden (gebiedsaanwijzingen) van de verordening, per punt opvraagbaar | Landbouwgebied-typologie (art. 4.123), Catalogus Gebiedskenmerken (art. 4.9), grondwaterbeschermingszone, NNN, bebouwde kom, boringsvrije zones |
| idem, Omgevingsvisie | `.../api/documents/ffe232e7-66a3-4286-a8ef-7d73d8a7d131` ("Omgevingsvisie 'Overijssel voor en met elkaar!' (in werking vanaf 1 juli 2026)", `nld@131`) | Visiekaart (o.a. Dagelijks Stedelijk Systeem, landbouwgebieden) | A1 (DSS-positie) en dubbelcheck typologie |
| Geodata Overijssel WFS 2.0 (GeoServer) | `https://services.geodataoverijssel.nl/geoserver/wfs` (GetFeature, `cql_filter=DWITHIN(SHAPE,POINT(x y),d,meters)`, EPSG:28992) | Lagen `B46_natuur_en_landschap:B46_Natuurnetwerk_Nederland` (filter `NATUURNETWERKNEDERLAND='Ja'`), `...:B4_Natura_2000-gebieden`, `B34_beheer_grondwater:B3_Grondwaterbeschermingsgebieden`, `...:B3_Waterwingebieden`, `B46_natuur_en_landschap:B4_Nationale_landschappen`, `B82_volkshuisvesting:B82_Harde_en_zachte_woningbouwplannen_vlakken` | Afstanden tot NNN, N2000, GWB, Nationaal Landschap; Planmonitor |
| PDOK Locatieserver | `https://api.pdok.nl/bzk/locatieserver/search/v3_1/free` | Adres naar RD-coördinaat | Coördinaten |

Opmerking over WMS/GetFeatureInfo: de viewer gebruikt een eigen `_locationSearch`-API (equivalent aan GetFeatureInfo; geeft de id's van de geometrieën waarin het punt valt, die via de annotaties in het document naar naam, type en artikel zijn te herleiden). De WFS van Geodata Overijssel is op onderdelen ouder (de metadata van de NNN-laag noemt nog "Zone Ondernemen met Natuur en Water" en "Omgevingsverordening PS/2009/407"); de **verordeningskaarten van de viewer zijn voor art. 4.123 en art. 4.9 leidend**, de WFS is gebruikt voor afstanden en de Planmonitor. De WFS-capabilities (`$S/caps.xml`, 438 lagen) bevatten **geen** laag voor de landbouwgebied-typologie; die staat alleen in de viewer/DSO-publicatie. Een tweede DSO-route (omgevingswet.overheid.nl "Regels op de kaart") is niet nodig gebleken en niet apart bevraagd.

Welke artikelen verwijzen naar welke gebiedsaanwijzing (herleid uit de annotaties in `$S/d2/ov_2610.json`): "Landbouwgebied met generieke opgaven en kansen" naar art. **4.123, 4.124**; "Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur" naar art. **4.123, 4.124, 4.41**; "Natuurnetwerk Nederland (NNN)" naar art. 4.56-4.63; "grondwaterbeschermingszone" naar o.a. art. 3.23-3.55 en 4.67-4.80; "boringsvrije zone Salland Diep" naar o.a. art. 3.23-3.26, 4.69, 5.16-5.20; "bebouwd gebied" naar art. **4.13** (regionaal perspectief water en bodem, lid 3 sub d; dit is **niet** het "bestaand bebouwd gebied" van art. 4.5); "bebouwde kom" naar art. 2.5 ("de gebieden die een overwegende woon- en verblijffunctie hebben door de mate van concentratie van bebouwing"); de landschapsnamen (o.a. "Dekzandvlakte en dekzandrug", "oude hoevenlandschap", "Beekdal en natte laagte", "maten- en flierenlandschap", "rivierengebied", "kernrandzone", "dorp of buurtschap") naar art. **4.9** (Catalogus Gebiedskenmerken, Bijlage VII).

Letterlijk, art. 4.123:
> "Artikel 4.123 (werkingsgebieden ontwikkelingsperspectieven landbouwgebieden) In Overijssel worden de volgende ontwikkelingsperspectieven landbouwgebieden aangewezen en als zodanig geometrisch begrensd: a. landbouwgebied met generieke opgaven en kansen; b. landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur."

— Bron: Omgevingsverordening Overijssel, geconsolideerd, https://ruimtelijkeplannen.overijssel.nl/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044 (opgehaald 2026-10-05; byte-identiek aan de kopie van 2026-10-04)

### 1.2 Uitkomst per locatie (punt-in-gebied, nieuw 2026-10-05)
RD = EPSG:28992 (PDOK-geocodering van het adres; bij wegen het wegcentroïde). "Afstand" = afstand tot het dichtstbijzijnde object in stappen (1 / 100 / 250 / 500 / 1.000 / 2.000 / 3.000 / 5.000 / 10.000 m): "<= 500 m" betekent: tussen 250 en 500 m; "binnen" = punt ligt erin. NNN = alleen begrensde NNN. DSS = "Dagelijks Stedelijk Systeem" volgens de visiekaart.

| Locatie (plan) | PDOK-adres | RD x,y | Landbouwgebied (art. 4.123) | In grondwaterbeschermingszone (verordening) | Afstand GWB-gebied (WFS) | Afstand NNN | Afstand Natura 2000 | Overstroombaar gebied | DSS (visiekaart) | Catalogus Gebiedskenmerken (art. 4.9) |
|---|---|---|---|---|---|---|---|---|---|---|
@@TABLE1@@

Bron voor alle rijen: `_locationSearch` van https://ruimtelijkeplannen.overijssel.nl/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044 en `.../ffe232e7-66a3-4286-a8ef-7d73d8a7d131`; WFS https://services.geodataoverijssel.nl/geoserver/wfs (geraadpleegd 2026-10-05). Voorbeeld van een volledige aanroep: `https://ruimtelijkeplannen.overijssel.nl/api/documents/55d637e6-8ff6-4083-a824-a0e77027a044/_locationSearch?x=210365&y=489138&distance=1` (Engeweg 8). Eerdere run (2026-10-04) leverde voor Engeweg 2, Vettewinkelweg 2, Lierderholthuisweg 3, Herxen, Wesepe, Middel, Marle en Boskamp dezelfde typologie (`$S/ls_out.txt`).

**Lezing van de tabel**
- **Elshof/Engeweg (8 woningen, B&W 3-2-2026):** beide Engeweg-percelen liggen in **landbouwgebied met generieke opgaven en kansen** (art. 4.124 lid 1: nieuwe functies mogen "geen beperking opleveren voor de ontwikkeling van de landbouw in de omgeving"). Engeweg 8 ligt in dekzandvlakte/oude hoevenlandschap, Engeweg 10a in "Beekdal en natte laagte" en "maten- en flierenlandschap". De buurtschapskern Elshof (Elshof 6c) valt in "bebouwd gebied"/"dorp of buurtschap" en is dus **geen** landbouwgebied. De adviesnota zegt dat de percelen "direct ten zuidoosten van buurtschap Elshof" liggen en dat het verzoek "in strijd [is] met het Omgevingsplan ... functie 'Agrarisch'": dat past bij de kaart. De in de adviesnota gesignaleerde belemmering van omliggende landbouw (spuitzone 50 m, op twee zijden slechts 30 m haalbaar, drie zijden grenzen aan agrarische percelen) is precies het type "beperking" waarover art. 4.124 lid 1 gaat; de afwijkingsgronden van lid 4 (feitelijk geen ontwikkelmogelijkheden; of samenhangende gebiedsvisie) worden in de adviesnota niet genoemd. Zie §2.2.
- **Vettewinkelweg 2:** **gebiedsspecifiek** landbouwgebied, **in** de grondwaterbeschermingszone (WFS-object "Boerhaar", `LEGENDA` "grondwaterbeschermingsgebied", `KWO` "niet toegestaan") en "Beekdal en natte laagte". Dit sluit aan op de adviesnota 23-1-2024: "dubbelbestemmingen 'Waarde - Archeologie - 1' en 'Waterstaat - Intrekgebied' en gebiedszone 'Milieuzone - Grondwaterbeschermingsgebied'". Voor art. 4.124 lid 3 (extra kwaliteitsinvestering gericht op klimaat, natuur en water) is dit het strengere regime; het besluit (vergunning 7-4-2025) dateert van **vóór** de typologie (1-7-2026).
- **Lierderholthuisweg 3:** generiek; NNN op <= 2 km; oude hoevenlandschap. De adviesnota zegt zelf "De locatie ligt in het 'oude hoevenlandschap'": **bevestigd** door de kaart.
- **Steunenbergerweg 6 (Middel), Prinshoeveweg 1, Kleistraat, Bokkelerweg:** generiek (Kleistraat ook "kernrandzone"); Prinshoeveweg ligt op <= 500 m van het grondwaterbeschermingsgebied.
- **Herxen (CPO achter nr. 7a; Grolleman nr. 63), Wijhe, Olst, Wesepe, Boskamp, Boerhaar, Zandhuisweg 7:** de punten vallen in de kaartlagen "bebouwd gebied" en "bebouwde kom" en dus **niet** in een landbouwgebied; Herxen is in de Catalogus "dorp of buurtschap" en "Kern aan de IJssel, Vecht of in de Delta" (rivierengebied). **Let op:** "bebouwd gebied" op deze kaart is de water-en-bodem-aanduiding van art. 4.13 en niet een provinciale contour van "bestaand bebouwd gebied" voor art. 4.5 (de provincie begrenst dat bewust "verbaal", `provincie_overijssel.md` §1.2); de kaart toont wel dat de provincie Herxen en Elshof als "dorp of buurtschap" typeert. Het CPO-perceel Herxen 7a is volgens B&W 2-6-2026 een "onbebouwd perceel"; op de verordeningskaart valt het binnen "bebouwde kom"/"bebouwd gebied". **Zandhuisweg 7** (9 woningen, vergunning 25-11-2025) ligt dus binnen de kaartbegrenzing "bebouwde kom" van Wijhe: dit bevestigt de vermoeden van deelonderzoek 4 ("kernrandlocatie") en verklaart waarom het in drie weken kon, zie §2.3.
- **Marle (Marledijk 33), Welsum (Erveweg 8, Kloosterhoekweg), Den Nul, Elshagenweg 1 (Wesepe):** **gebiedsspecifiek**. Marle, Welsum en Den Nul liggen in de IJsselzone (NNN en Natura 2000 Rijntakken op <= 100-500 m).
- **Nationaal Landschap:** geen enkel punt valt in een Nationaal Landschap (WFS-laag `B4_Nationale_landschappen` kent alleen "IJsseldelta" en "Noordoost Twente"; dichtstbij Marle op 5 tot 10 km). Het concept ("Nationaal Landschap IJsseldelta: vermoedelijk niet van toepassing [TK]") is hiermee **bevestigd** (niet van toepassing).

### 1.3 Aandeel van de typen in de gemeente (rasterbevraging, 250 m, 1.883 punten)
Methode: raster van 250 m over de gemeentegrens (PDOK/CBS-vlak `$S/gem.json`, 118,4 km², inclusief IJssel en uiterwaarden), elk celmiddelpunt bevraagd via `_locationSearch` op de verordening (nieuw 2026-10-05, 0 mislukte aanroepen; een grovere 500 m-run van 2026-10-04 gaf hetzelfde beeld: 38,3% generiek, 38,3% gebiedsspecifiek).

| Kaartlaag (verordening, nld@129) | Punten | Aandeel gemeenteoppervlak (ca.) |
|---|---|---|
| Landbouwgebied met generieke opgaven en kansen | 711 | 37,8% (circa 44,5 km²) |
| Landbouwgebied met gebiedsspecifieke opgaven en kansen voor water, klimaat en natuur | 719 | 38,2% (circa 45,1 km²) |
| Geen van beide (NNN, uiterwaarden/water, kernen en buurtschappen, overig) | 453 | 24,1% |
| waarvan "bebouwd gebied" | 105 | 5,6% |
| NNN (begrensd, alle overlappen) | 294 | 15,6% |
| Grondwaterbeschermingszone | 100 | 5,3% (waarvan 71 in gebiedsspecifiek, 28 in generiek) |

Er is **geen overlap** tussen beide landbouwtypen (0 punten in beide). Van het agrarisch buitengebied valt dus ongeveer **de helft in generiek en de helft in gebiedsspecifiek**. Beantwoording C1 ("hoeveel valt onder welk type"): zie bovenstaande tabel. De "boringsvrije zone Salland Diep" ligt over vrijwel de hele gemeente (100% in het 500 m-raster).

### 1.4 Natura 2000, NNN, grondwaterbeschermingsgebied (Boerhaar), Catalogus (C3)
- **Natura 2000:** alleen **Rijntakken** (IJsselzone/uiterwaarden) raakt de gemeente (op <= 500 m van Welsum, Den Nul, Marle en Wijhe-centrum; <= 1.000 m van Olst); **Boetelerveld** ligt op 5 tot 10 km van Wesepe. De gemeente schrijft in de RIB bouwsteen (9-6-2026): "In de IJsselzone (onderdeel van N2000-gebied Rijntakken), zijn nauwelijks ontwikkelingen op erfniveau mogelijk vanwege beperkingen die daar gelden in verband met waterveiligheid." (`$S/d1/ib_rib_bouwsteen_jun.pdf.txt`, geraadpleegd 2026-10-04). De concept-vermelding "Veluwe circa 8,5 km" valt buiten de Overijsselse WFS (Gelderland) en is niet gecontroleerd.
- **NNN:** twee deelgebieden: "Uiterwaarden IJssel en IJsselmonding" (IJsselzone) en "Landgoederen Salland" (o.a. rond Boskamp, Middel, Lierderholthuisweg). Geen van de getoetste projectlocaties ligt **in** NNN; Herxen 7a ligt op <= 100 m, Boskamp en Middel op <= 500 m. De gemeente weet dat NNN-aantasting provinciale instemming vergt (B&W 23-4-2024, Holsto Tuinen, Rijksstraatweg 12a: "Om hier medewerking aan te kunnen verlenen is instemming van de Provincie noodzakelijk", `$S/d1/bw_all.txt` r. 16564).
- **Grondwaterbeschermingsgebied Boerhaar** (WFS `NAAM` "Boerhaar", `NR_GRWBES` 29, `SALL_DIEP` 1): ligt rond de Boerhaar/Vettewinkelweg; Vettewinkelweg 2 ligt erin; Boerhaar 43 en Zandhuisweg 7 (kernrand Wijhe) op <= 100 m resp. <= 1.000 m; Prinshoeveweg op <= 500 m. Vitens-winning Boerhaar en het plan CPO Boerhaar: zie `deelonderzoek_3.md` §2.2.
- **Catalogus Gebiedskenmerken:** zie laatste kolom van de tabel; art. 4.9 en 4.10 vragen onderbouwing en inpassing op basis van de landschapstypen. Voor Elshof/Engeweg: "Dekzandvlakte en dekzandrug" en "oude hoevenlandschap" (Engeweg 8), "Beekdal en natte laagte" en "maten- en flierenlandschap" (Engeweg 10a), in "Salland", met de belevingslagen "bakens in de tijd" en "donkerte" (heel de gemeente).
- **Uitgesloten/kansrijke zones (C3):** in de kaartlagen van de verordening is geen aanwijzing "uitgesloten" of "kansrijk" voor wonen gevonden; de verordening kent in Olst-Wijhe wel o.a. "werkingsgebied peilbesluiten", "primaire waterkeringen", "overstroombaar gebied" (93% van de gemeente in het 500 m-raster) en "Leefgebied weidevogels" (3,6%, o.a. rond Marle/Lierderbroek). De gemeentelijke "zoekgebied erfontwikkeling" (kernranden) is een gemeentelijk begrip en staat niet in de provinciale kaart (§1.7).
- **Raatakkers/karrensporen (art. 4.126-4.131):** in de kaartlagen van het 500 m-raster **geen** treffer in Olst-Wijhe (die komen alleen voor in natuurgebieden elders).

### 1.5 Lijst van gebiedsaanwijzingen in de gemeente (500 m-raster, 475 punten, 2026-10-04)
Volledig in `$S/grid_out.json`. Relevante aandeel-cijfers: bakens in de tijd, boringsvrije zone en primaire waterkeringen 100%; donkerte 97,5%; overstroombaar gebied 93,1%; Salland 65,5%; Dekzandvlakte en dekzandrug 54,7%; zandgrond 40,6%; oude hoevenlandschap 38,5%; landgoed of buitenplaats 17,7%; NNN 15,4%; maten- en flierenlandschap 14,1%; Rivierenlandschap 11,4%; Beekdal en natte laagte 10,9%; kernrandzone 6,7%; jonge heide- en broekontginningen 6,7%; Kern aan de IJssel, Vecht of in de Delta 5,1%; dorp of buurtschap 5,1%; zeer kwetsbare natuurgebieden 2,5%; essenlandschap 1,1%. Visiekaart: "Dagelijks Stedelijk Systeem regio Stedendriehoek" 89,1% van de punten en "regio Zwolle" 60,6% (overlappend; zie A1 in §6).

### 1.6 Provinciale Planmonitor: Olst-Wijhe (nieuw, WFS 2026-10-05)
Laag `B82_volkshuisvesting:B82_Harde_en_zachte_woningbouwplannen_vlakken` (aanroep: `https://services.geodataoverijssel.nl/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeNames=B82_volkshuisvesting:B82_Harde_en_zachte_woningbouwplannen_vlakken&outputFormat=application/json&srsName=EPSG:28992&cql_filter=GEMEENTE='Olst-Wijhe'`; 37 vlakken). Metadata (WFS-laagabstract):
> "Gemeenten brengen daarom elk jaar de harde en (wanneer mogelijk) de zachte woningbouwplannen in beeld via een online webapplicatie (Planregistratie). Dit vlakkenbestand geeft deze plancapaciteit weer per 1-1-2026. Let op: voor een aantal plannen is locatie is niet bekend; deze zijn hier niet weergegeven. Daarom kan de totale plancapaciteit niet worden afgeleid van dit bestand."

— Bron: WFS-capabilities https://services.geodataoverijssel.nl/geoserver/wfs?request=GetCapabilities (laagabstract; metadata https://metadata.geodataoverijssel.nl/metadata/dataset/9ca02f6f-22f8-499b-a97e-5ec968476c53.xml), geraadpleegd 2026-10-04 (`$S/caps.xml`) en 2026-10-05 (lagen opnieuw bevraagd)

Olst-Wijhe, status volgens de provincie (kolom `NOG_TE_BOUWEN_VANAF_2026` = nog te bouwen vanaf 1-1-2026; som voor locatiebekende plannen: **hard 244, zacht 770** = 1.014):

| Status | Plan (woonplaats, plantype) | Nog te bouwen | Oplevering |
|---|---|---|---|
| hard | **Engeweg Elshof** (Wijhe, "Uitbreiding overig") | **8** | 2028 |
| hard | **Zandhuisweg 7** (Wijhe, "Verdichting") | **9** | 2027-2028 |
| hard | Steunenbergerweg 6 (Olst, "Uitbreiding uitleg") | 3 (sloop 0) | 2023-2026 |
| hard | Vettewinkelweg 2 (Wijhe, "Transformatiegebied") | 1 | 2026 |
| hard | Lierderholthuisweg 12-16 (Wijhe, "Transformatiegebied") | 3 | 2027-2028 |
| hard | 't Kleiland (Olst) | 20 | 2027 |
| hard | Schoollocatie Klimboom (Olst) | 18 | 2026-2028 |
| hard | IJsseldal (Wesepe) | 81 | 2027-2030 |
| hard | Tellegenpark (Wijhe) | 25 | 2026 |
| hard | Langstraat 19 (Wijhe, "Pand transformatie") | 18 | 2026-2027 |
| hard | Abersoncomplex (Olst) | 19 | 2023-2028 |
| hard | Raalterweg 28/28a (10), 37 (5), 9-9a (2) (Wesepe) | 17 | 2026-2027 |
| hard | overige kleine plannen (Eikelhofweg 5: 3; Hooiberglaan woonwagenstandplaatsen: 3; Kleistraat 17: 1; Leugenshorst 4: 1; Mengerweg 11: 1; Olstergaard: 2; Oranjelaan 2: 5; Veldweg 4: 1; Weidebeek I: 2; Weth.W.A. Boerkampweg: 3) | 22 | 2023-2028 |
| zacht | **Grolleman, Herxen** (Wijhe, "Transformatiegebied") | **15** | 2029 |
| zacht | Wijhe Noord (Uitbreiding uitleg) | 300 | 2028-2035 |
| zacht | Wengelerhoek (Uitbreiding uitleg) | 138 | 2027-2032 |
| zacht | Olst Zuid (Uitbreiding uitleg) | 90 | 2028-2030 |
| zacht | Dorpshart Boskamp (Transformatiegebied) | 80 (sloop -24) | 2028-2031 |
| zacht | Schoollocaties Olst (59), Schoolloc. Matzer (44), Schoollocatie de Holsthoek (18) | 121 | 2027-2031 |
| zacht | Hof van Polletje (10), Kerkstraat 1 (6), Kippenmarkt (5), Scholtensweg 50 (3), Zonnenbergerweg 1 (2) | 26 | 2027-2029 |

Volledige uitvoer: `$S/d2/planmonitor_ow.json`. **Niet in de provinciale Planmonitor:** het CPO Herxen (3 woningen, B&W 2-6-2026; op de gemeentelijke volgordelijst "Kromme Koeweg") en CPO Boerhaar. Dit beantwoordt de A2-vraag "staat het project in de Planmonitor": **Engeweg Elshof: ja, als harde plancapaciteit** (8 woningen; 'hard' ondanks dat de BOPA nog niet is aangevraagd: de gemeente heeft het als hard geregistreerd); **Grolleman Herxen: zacht**; **CPO Herxen: niet**. Waarschuwing: de provinciale vlakkenlaag is zelf niet leidend voor het totaal ("kan de totale plancapaciteit niet worden afgeleid"); voor de som 244 hard + 770 zacht gaat het dus om een ondergrens voor locatiebekende plannen. Het gemeentelijke bericht "161 woningen plancapaciteit binnen bestaand stedelijk gebied/339 totaal" (tegenstrijdigheid 7) is hiermee **niet** verklaard.

### 1.7 Gemeentelijke versus provinciale gebiedsindeling (C1, B3)
> "Bij het vaststellen van de gemeentelijke omgevingsvisie heeft de raad destijds gekozen voor bovenstaande gebiedsindeling en daarmee is bewust afgeweken van de gebiedsindeling zoals die in de Provinciale omgevingsvisie is vastgelegd. In de Provinciale visie wordt een onderscheid gemaakt tussen generieke landbouwgebieden en gebieden met gebiedsspecifieke opgaven. In de generieke landbouwgebieden is meer ruimte voor de landbouw, in de gebieden met gebiedsspecifieke opgaven ook ruimte voor andere ontwikkelingen. De gebiedsindeling van de provincie en de gemeente komt niet overeen. In de praktijk betekent dit dat het in bepaalde gebieden zo kan zijn dat we als gemeente ontwikkelingen toestaan, terwijl de provincie deze niet toestaat en andersom. In de bouwsteen zoeken we naar een oplossing om met deze verschillen om te gaan."

— Bron: Raadsinformatiebrief voortgang bouwsteen Erfontwikkeling en -transformatie, 9-6-2026, p. 1-2 (`$S/d1/ib_rib_bouwsteen_jun.pdf.txt`; ook adviesnota B&W 11-6-2026, zaak 24972-2026) (geraadpleegd 2026-10-04)

De gemeentelijke Koers team landelijk gebied (B&W 4-11-2025 punt 6) voegt toe:
> "Wat hierbij meespeelt is een verschil in uitwerking van het water- en bodemsturende principe in de omgevingsvisie van de gemeente en de provincie. Door een verschillend onderliggend wetenschappelijk kader (bij de gemeente de Sponsstrategie, bij de provincie het document 'Agrarisch Overijssel 2050 landbouw en natuur in balans') is de uitwerking voor welke ontwikkelingen waar in het landelijk gebied voorrang krijgen, verschillend. Dit kan in de toekomst conflicten opleveren over wat we waar wel en niet toestaan."

— Bron: Koers team landelijk gebied, Gemeente Olst-Wijhe 2025 en 2026, p. 9 (`$S/koers.txt`; bijlage `koersdocument-landelijk-gebied-1.pdf` bij B&W-besluiten 04-11-2025, https://www.olst-wijhe.nl/bestuur/besluiten-van-raad-en-college/b-amp-w-besluiten/2025/11/17/b-amp-w-besluiten-04-11-2025/koersdocument-landelijk-gebied-1.pdf) (geraadpleegd 2026-10-04)

**Gevolg voor de locatiebeoordeling [INT]:** de provinciale typologie (kaart) is een juridische instructieregel (art. 4.124); de gemeentelijke driedeling (IJsselzone, kommenlandschap, dekzandgebied) is visiebeleid. Voorbeelden uit de punttabel: Elshof/Engeweg, Middel en Bokkelerweg liggen in het gemeentelijke dekzandgebied (gemeente "ja, mits") maar provinciaal in **generiek** landbouwgebied (strengere regel: geen beperking voor omliggende landbouw); Vettewinkelweg 2 en Elshagenweg liggen provinciaal in **gebiedsspecifiek** gebied. Voor een kandidaatlocatie moet dus altijd beide kaarten worden gelegd; de bouwsteen (vaststelling beoogd november 2026, RIB 9-6-2026) moet dit verschil oplossen.

