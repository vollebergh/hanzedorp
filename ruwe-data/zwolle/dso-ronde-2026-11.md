# Zwolle: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels of bronbestanden.

## Commando's
- `python3 -I tools/dso.py pons gm0193` -> omgevingsplan v4, inwerking 2026-05-08, 1 pons-gebied van ca. 10x10 m.
- `python3 -I tools/dso.py regelingen gm0193 [--ontwerp]`; ontwerp-Omgevingsvisie technischId `_akn_nl_act_gm0193_2025_Regelingb23c8909e43f4bd9970e09bc2e91da74_akn_nl_bill_gm0193_2025_besluita7dfdf1bf9a248d8a5daf7ae853c1a45`.
  NB tool-bug: `tekst --ontwerp` geeft lege uitvoer omdat `tools/dso.py` de sleutel `documentComponenten` leest terwijl Ozon voor ontwerpen `ontwerpDocumentComponenten` levert. Eigen wrapper (scratchpad) gebruikt; tool niet gewijzigd.
- `python3 -I tools/dso.py rp-plannen 0193 --grep ...`, `--tam`; `rp-info` en `rp-tekst` voor NL.IMRO.0193.BP10016-0004 (Haerst/Tolhuislanden), BP10010-0004 (IJsselzone Windesheim), BP10009-0005 (Langenholte/Vecht), BV13001-0002 (Herfte/Wijthmen).
- `python3 -I tools/dso.py tekst /akn/nl/act/gm0193/2020/omgevingsplan` (850 kB; afdelingen 4.1-4.15 alleen structuur) en `vergunningen gm0193 --grep ...`.
- `python3 -I tools/ori.py search/get --org zwolle` (iBabs; zoek op KGO, Volkshuisvestingsprogramma, Huisvestingsverordening, Omgevingsvisie).
- CVDR: lokaleregelgeving.overheid.nl/CVDR726092 en CVDR744314; SRU `dcterms.creator="Zwolle"`.

## Bevindingen
1. Planregels tijdelijk deel (alle vier plannen geldend): art. 3.7.2 wijziging Agrarisch -> Wonen na bedrijfsbeeindiging: "e. een bedrijfswoning gehandhaafd blijft; f. het aantal woningen niet toeneemt"; art. 3.6.1 b: karakteristieke bedrijfswoning >= 1.000 m3 splitsen in 2 of 3 woningen. Zelfde in art. 4.8.2/5.8.2 (Agrarisch met waarden) en 4.6/5.6. Geen rood-voor-rood-artikel; toelichting: "Rood voor rood-woningen zijn dan ook niet toegestaan in het agrarisch landschap" en voor gemengd landelijk gebied "(clusters) van Rood voor rood woningen".
2. Raadsbrief actualisatie KGO-beleid (9-9-2026): definitief KGO-beleid voor zomer 2027 naar de raad; gebiedsgericht; KGO-fonds in onderzoek; EUR 40.000; scope omvat ervenclusters/erfdelen. Motie 5-6 "Huisje erbij als botsproef voor KGO" aangenomen 28-9-2026.
3. Omgevingsvisie niet vastgesteld: raad 9-2-2026 stelde alleen de Nota van zienswijzen (89 zienswijzen) vast; vaststelling pas na gebiedsvisies Vechtrand en Zwolle-Zuid/zuid. Raadsbesluit startnotities Vechtrand en Nieuw Zuthem 26-10-2026.
4. Ontwerp-Omgevingsvisie tekst: §6.10.1 en hfst 7 (KGO-principes, landschapsfonds) geciteerd in het rapport.
5. Volkshuisvestingsprogramma: nog in de maak (5-10-2026), besluitvorming tweede helft 2026 (Factsheets 29-6-2026).
6. Huisvestingsverordening: raad 7-10-2024 scenario 1 (vier bouwstenen); impactanalyse tussenrapportage 28-10-2025; bouwsteen lokale binding afgewezen; geen vastgestelde verordening.
7. CVDR726092 vervallen per 24-9-2025; opvolger CVDR744314: bindend advies > 5 woningen buitengebied, >= 20 woningen stedelijk gebied (met strijd met activiteit wonen).
8. Wijthmen: Dorpsplan (10-2-2025) 100-150 woningen; Startnotitie (3-12-2025): onderzoekt CPO/Casco; bereid 30-40-30 los te laten.
9. BOPA's (Ozon vergunningen, 40 publicaties): geen buitengebied-project met 10-12 woningen; Energieweg 30C-1 (6 woningen), Het Buyten bouwnummer 94.
10. Niet gevonden: interne Handreiking KGO (Woo), tekst Volkshuisvestingsprogramma, woningbehoefteonderzoek 2025 zelf, TAM-regeltekst.
