# Dalfsen: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels of bronbestanden.

## Commando's en toegang
- `python3 -I tools/dso.py pons gm0148` -> omgevingsplan v3 (2025-04-10); geen pons. `regelingen gm0148 [--ontwerp]`: PLG in werking 2026-04-15; ontwerp-omgevingsplan 2024.
- `python3 -I tools/dso.py rp-plannen 0148 ...`: Buitengebied Dalfsen NL.IMRO.0148.BgemDalfsen-vs01 (2013) + 25 herzieningen en 9 verzamelplannen. `rp-tekst` levert voor dit plan alleen de toelichting; de regels zijn via https://ruimtelijkeplannen.nl/documents/NL.IMRO.0148.BgemDalfsen-vs01/r_NL.IMRO.0148.BgemDalfsen-vs01_2.3.html (Artikel 3 Agrarisch) gelezen.
- Vosserburen: `vb_NL.IMRO.0148.OmBVosserstg74en76-vs01.pdf` (19 p., pypdf), Gmb 2024, 541698 en 454253.
- `python3 -I tools/dso.py vergunningen gm0148 --grep ...` (93 publicaties).
- CVDR750709 (Legesverordening 2026) en CVDR674315 (Beleidsregels 2022) via lokaleregelgeving.overheid.nl.
- ORI: bron `dalfsen` (gemeenteoplossingen) 'implemented: false', 0 treffers. ris.dalfsen.nl: JS-beveiligingscontrole; geen toegang met curl.

## Bevindingen
1. Art. 3.8.1 d (wijziging naar wonen): Wonen, of Wonen met twee woningen door verbouwen bedrijfswoning > 1.000 m3 (uiterlijke verschijningsvorm gehandhaafd); 3.8.2 c: (bedrijfs)woning blijft gehandhaafd. Geen cluster-regeling.
2. Vosserburen: 13 tijdelijke transformatiewoningen, max. 20 jaar vanaf onherroepelijk; terugbouw naar schuur; huur tot huursubsidiegrens; min. 30% statushouders/Oekraiense ontheemden; Aerius 0,00; geen provincie-vvgb Wnb.
3. Vergunningen: Pijlriet 17-33 (9 CPO-woningen, 18-11-2025), Gerner Es 9-15 (4 woningen), Burg. Backxlaan 6-8 (5), compensatiewoningen Meeleweg 6, Ruitenveen 1, Dalmsholterweg 2A, BOPA splitsing woonboerderij G.W. van Marleweg.
4. "Boerenerf wonen": alleen in Legesverordening 2026 (CVDR750709) als categorie naast Sloop voor Kansen/VAB/KGO; geen aparte regeling gevonden; mogelijk Erfwonen (9e Verzamelplan, Gmb 2025, 259478).
5. Niet bereikbaar: motie 202604-uitwerking, Woonupdate 004, herziening Beleidsregels 2022 (RIS).
