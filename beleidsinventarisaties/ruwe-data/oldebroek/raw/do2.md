Gedaan: geodata-analyse overlays (gemeente, landbouw, kernenringen) uitgevoerd en hieronder vastgelegd (§GEO) / Nog te doen: puntcontroles locaties, OB-grep (zienswijzen, provincie, BOPA, 5.64), webonderzoek (processubsidie, Singelhof, Expertteam, Regisseur Ruimte, Kop van de Veluwe), Bijlage B-tabel, tegenstrijdigheden, toegang

# Deelonderzoek 2 - Provinciaal-lokale toepassing - gemeente Oldebroek (raadpleegdatum 2026-10-18)
Model: Claude Sonnet 5.5. Bronnen en scripts: raw/do2_src/, raw/do2_tools/.

## GEO. Geodata-analyse overlays Oldebroek [BER op basis van PRIMAIR geodata]
Methode: Gelderse WFS geoserver.gelderland.nl/geoserver/ngr_verordening/wfs (POVE_*), ngr_d (Pvbb_Stikstofemissie_beperkingengebied), ngr_a, ikn; PDOK Kadaster Bestuurlijke Gebieden (Gemeentegebied, code 0269), PDOK Natura2000, PDOK BRP gewaspercelen 2025 (excl. categorie Natuurterrein en Landschapselement), CBS Bevolkingskernen 2021. Scripts: raw/do2_tools/fetch_ov.py, fetch_gem.py, fetch_kernen.py, analyze.py; resultaat raw/do2_src/analyse_oldebroek.json/.txt; vrije grond raw/do2_src/analyse_oldebroek_free.geojson. Geraadpleegd 2026-10-18. Indicatief, geen juridische begrenzing.

Gemeentegebied (Kadaster) 9.883,5 ha; BRP-landbouwgrond 4.427,6 ha (grasland 3.723,0; bouwland 702,5; overig 2,1).
NB: provincie_gelderland.md §1.6.8 noemt 4.620 ha landbouwgrond (incl. mogelijk landschapselementen/andere filter); mijn filter geeft 4.427,6 ha. Gemeentebrede percentages komen exact overeen (GNN 33,3; GOZ 5,3; N2000 29,7; weidevogel 22,7; ganzenrust 11,4; NL Veluwe 91,1; streek Randmeerkust 69,1/Veluwe 30,9; stikstofstrook 39,5; waterwin+grondwaterbesch. 0,3/2,9).

| Overlay | ha gemeente | % gemeente | ha landbouw | % landbouw (4.427,6 ha) |
|---|---|---|---|---|
| Gelders natuurnetwerk (GNN) | 3.292,2 | 33,3 | 220,3 | 5,0 |
| Groene ontwikkelingszone (GOZ) | 525,3 | 5,3 | 267,1 | 6,0 |
| GNN of GOZ | 3.817,6 | 38,6 | 487,3 | 11,0 |
| Weidevogelgebied (verordening) | 2.248,4 | 22,7 | 1.944,1 | 43,9 |
| - Polder Oosterwolde | 1.651,0 | 16,7 | 1.418,0 | 32,0 |
| - Polder Oldebroek | 409,3 | 4,1 | 359,3 | 8,1 |
| - Broeklanden | 188,1 | 1,9 | 166,8 | 3,8 |
| Ganzenrustgebied (Randmeeroeverlanden) | 1.122,8 | 11,4 | 945,8 | 21,4 |
| Natura 2000 totaal (Veluwe 2.863,8 ha + Veluwerandmeren 68,8 ha) | 2.932,6 | 29,7 | 9,9 | 0,2 |
| Beperkingengebied stikstofemissie (voorbeschermingsregels, 500 m-strook) | 3.901,9 | 39,5 | 324,9 | 7,3 |
| Natuur- of vogeloverlay (GNN/GOZ/N2000/weidevogel/ganzenrust) | 5.849,5 | 59,2 | 2.297,4 | 51,9 |
| Idem + stikstofstrook + natte landnatuur | 6.731,5 | 68,1 | 2.602,8 | 58,8 |
| Nationaal landschap Veluwe | 9.007,2 | 91,1 | 4.412,9 | 99,7 |
| Gelderse streek Randmeerkust | 6.833,5 | 69,1 | 4.405,0 | 99,5 |
| Gelderse streek Veluwe | 3.050,0 | 30,9 | 22,7 | 0,5 |
| Gelderse streek IJsselvallei | 0 | 0 | 0 | 0 |
| Waterwingebied (Wezep (Boele), 5 mln m3 vergund, zeer kwetsbaar) | 26,1 | 0,3 | 0 | 0 |
| Grondwaterbeschermingsgebied | 286,1 | 2,9 | 0,6 | 0 |
| Intrekgebied | 306,4 | 3,1 | 4,2 | 0,1 |
| Kwetsbaar drinkwaterreserveringsgebied (ASV) Elburg-Wezep | 4.130,9 | 41,8 | 2.587,7 | 58,4 |
| Molenbiotoop (verordening, 2 objecten) | 50,2 | 0,5 | 21,5 | 0,5 |
| Ammoniakbuffergebied (extensivering; alleen niet-grondgebonden veehouderij) | 453,4 | 4,6 | 191,5 | 4,3 |
| Verbodsgebied windturbines Veluwe | 4.642,5 | 47,0 | 700,8 | 15,8 |
| Stiltegebied Noord-Oost Veluwe / beschermingszone natte landnatuur | 0 | 0 | 0 | 0 |

Vrije landbouwgrond (buiten GNN, GOZ, N2000, weidevogel, ganzenrust, stikstofstrook en natte landnatuur): 1.824,8 ha = 41,2% van de BRP-landbouwgrond. Buiten alleen GNN/GOZ/weidevogel/ganzenrust: 2.130,3 ha.
Lezing [INT]: "agrarisch Oldebroek" is praktisch geheel Nationaal Landschap Veluwe (99,7% van landbouwgrond) en geheel streek Randmeerkust (99,5%); de Gelderse streek Veluwe raakt vrijwel alleen natuur/bos (0,5% van landbouw). De GNN/GOZ-druk op landbouwgrond is laag (11%), de weidevogel- en ganzenrustdruk hoog (resp. 43,9% en 21,4%; samen ca. 52% overlay). Let op: kaartlaag "kwetsbaar drinkwaterreserveringsgebied ASV" (Elburg-Wezep, 58% van de landbouwgrond) is een reserveringsgebied (strategische voorraad), geen waterwin-/grondwaterbeschermingsgebied; de betekenis voor woningbouw is niet in de verordening-tekst gelezen [niet onderzocht].
De laag POVE_Glastuinbouw (100% dekking) is een generiek "buiten glastuinbouwontwikkelingsgebied"-vlak en niet informatief; Aardkundige waarde (68,8%; 64,7% van de landbouw) komt uit ngr_a (niet-verordening, "van provinciaal belang"); niet als verordeningsoverlay gebruiken.

### Kernen: overlays op de kern zelf en op omringende landbouwgrond (ringen langs kernpolygoon CBS 2021)
Kernen (CBS 2021: inwoners / BAG-woningen): Wezep 11.450/4.835; Oldebroek 3.860/1.620; Hattemerbroek 770/315; Oosterwolde (Gld.) 750/255; 't Loo 595/225; Oldebroek-Noord (Noordeinde) 145/55. (Hoge Enk en 't Harde liggen in Elburg, niet meegeteld.)
Kolommen: landbouw ha in ring | %GNN | %GOZ | %weidevogel | %ganzenrust | %stikstofstrook | % "vrij" (buiten alle natuur/vogel/stikstof) | ha vrij. NL Veluwe en Randmeerkust zijn overal ca. 95-100% (zie boven).
| Kern | ring | landbouw ha | GNN | GOZ | WV | GR | N-strook | vrij % | vrij ha |
|---|---|---|---|---|---|---|---|---|---|
| Wezep | 0-250 m | 61,4 | 0,2 | 0 | 0 | 0 | 40,7 | 59,3 | 36,4 |
| Wezep | 250-500 | 75,2 | 0,8 | 0 | 0 | 0 | 27,1 | 72,9 | 54,8 |
| Wezep | 500-1000 | 192,5 | 3,2 | 0,6 | 0 | 0 | 15,9 | 84,0 | 161,7 |
| Wezep | 1000-2000 | 505,2 | 0,7 | 5,6 | 0,1 | 0 | 7,7 | 87,9 | 444,2 |
| Oldebroek | 0-250 | 81,6 | 0 | 0 | 18,1 | 0 | 0 | 81,9 | 66,8 |
| Oldebroek | 250-500 | 119,6 | 0 | 0 | 26,2 | 0 | 0 | 73,8 | 88,3 |
| Oldebroek | 500-1000 | 315,6 | 0 | 11,9 | 31,4 | 0 | 3,7 | 53,0 | 167,2 |
| Oldebroek | 1000-2000 | 528,8 | 0,2 | 24,1 | 7,6 | 0 | 27,2 | 41,1 | 217,3 |
| Hattemerbroek | 0-250 | 27,6 | 0 | 0 | 0 | 0 | 56,8 | 43,2 | 11,9 |
| Hattemerbroek | 250-500 | 44,7 | 0 | 0 | 0 | 0 | 26,8 | 73,2 | 32,7 |
| Hattemerbroek | 500-1000 | 21,4 | 0,2 | 0 | 0 | 0 | 17,4 | 82,6 | 17,7 |
| Hattemerbroek | 1000-2000 | 171,7 | 4,1 | 0 | 0 | 0 | 4,1 | 95,9 | 164,5 |
| Oosterwolde | 0-250 | 41,1 | 0 | 15,2 | 1,9 | 0 | 0 | 82,9 | 34,1 |
| Oosterwolde | 250-500 | 73,1 | 0 | 21,3 | 13,9 | 0 | 0 | 64,8 | 47,4 |
| Oosterwolde | 500-1000 | 247,0 | 0 | 18,3 | 23,5 | 0 | 0 | 58,2 | 143,8 |
| Oosterwolde | 1000-2000 | 813,9 | 0 | 15,6 | 62,4 | 1,2 | 0 | 22,0 | 179,0 |
| 't Loo | 0-250 | 5,7 | 0 | 0 | 0 | 0 | 100 | 0 | 0 |
| 't Loo | 250-500 | 21,8 | 0 | 0 | 0 | 0 | 98,3 | 1,7 | 0,4 |
| 't Loo | 500-1000 | 88,6 | 0,4 | 3,2 | 0 | 0 | 44,6 | 55,4 | 49,1 |
| 't Loo | 1000-2000 | 330,0 | 1,0 | 6,3 | 0 | 0 | 25,8 | 69,4 | 228,9 |
| Oldebroek-Noord | 0-250 | 34,4 | 0 | 22,8 | 3,5 | 0 | 0 | 73,7 | 25,4 |
| Oldebroek-Noord | 250-500 | 74,5 | 0 | 31,2 | 16,9 | 0 | 0 | 51,9 | 38,6 |
| Oldebroek-Noord | 500-1000 | 211,1 | 0 | 27,9 | 24,3 | 0 | 0 | 47,8 | 100,9 |
| Oldebroek-Noord | 1000-2000 | 701,5 | 0,1 | 10,7 | 26,6 | 0 | 9,9 | 52,7 | 369,9 |

Overlays op de kernen zelf (% van kernoppervlak): Wezep: stikstofstrook 49,4%; grondwaterbeschermingsgebied 23,1%; intrekgebied 15,7%; streek Randmeerkust 90,4%/Veluwe 9,6%; GOZ 3,0%; NL Veluwe 3,0%; GNN 0,5%. Oldebroek: streek Randmeerkust 100%; ASV-reservering 100%; weidevogel 0,0% (aan de rand); NL Veluwe 4,1%. Hattemerbroek: stikstofstrook 88,2%. 't Loo: stikstofstrook 100% (kern geheel binnen 500 m-strook), Veluwe-streek 4%, GNN 1%, N2000 2%. Oosterwolde: geen verordeningsoverlay op de kern (ASV 100%). Oldebroek-Noord (Noordeinde): molenbiotoop op 60,1% van de kernomvang.
Conclusie [INT]: voor een agrarische CPO-locatie liggen relatief "vrije" ruimtes (zonder natuur/vogel/stikstofoverlay) vooral rond Wezep (tot 1 km: 216 ha vrij) en Hattemerbroek (500 m-1 km); rond Oldebroek-kern en Oosterwolde/Noordeinde bepalen weidevogelgebied (Polder Oldebroek, Polder Oosterwolde) en GOZ de toets; rond 't Loo zijn de eerste 500 m geheel stikstofbeperkingsgebied. Een kleine bebouwing "in het weidevogelgebied" is bij art. 5.27-5.31 voorwaardelijk zonder ontheffingsroute (PB §1.6.4).
