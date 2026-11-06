# Deventer: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels of bronbestanden.

## Commando's
- `python3 -I tools/dso.py pons gm0150` -> omgevingsplan versie 5 inwerking 2026-11-04; geen pons (tijdelijk deel geldt overal).
- `python3 -I tools/dso.py rp-plannen 0150 --grep 'D125|Buitengebied|Combi|TAM'` (moederplan NL.IMRO.0150.D125-VG02; 1e herziening D125a-VG02, geldend; Combiplannen 1-7 + TAM006/TAM020; ca. 25 TAM-plannen 2024-2026).
- `python3 -I tools/dso.py rp-tekst NL.IMRO.0150.D125a-VG02` (art. 3.7.5, 4.8, 5.8, 21.2, 49.1), `…TAM018-VG01`, `…TAM020-VG01`, `…TAM025-VG01`.
- `python3 -I tools/dso.py vergunningen gm0150 --grep 'woning|BOPA|...'`.
- `python3 -I tools/ori.py search/get --org deventer` (Notubiz): raadstafel 11-11-2026, besluitenlijst raad 4-11-2026, amendement 5A.1.
- CVDR748764 (leges 2026, /2 vanaf 2026-06-19); coalitieakkoord-PDF van deventer.nl (pypdf, lokaal).

## Bevindingen
1. D125a-VG02 art. 3.7.5 p: "het aantal woningen mag niet toenemen"; sloop-terugbouw 250 m2 (max 850 m2); art. 49.1 woningsplitsing karakteristiek pand: 2 woningen > 1.000 m3; 3 woningen > 1.500 m3; geen toename bouwvolume. Art. 21.2: 1 woning per bouwvlak tenzij maatvoeringaanduiding.
2. TAM018 Gorsselseweg 27 Bathmen: 15 woningen, vastgesteld 2026-06-10 (besluit 2026-287), 40% betaalbaar tot EUR 405.000 v.o.n., bestaand bebouwd gebied; 2 zienswijzen. TAM025 Landgoed De Bannink: provincie positief, anterieure exploitatieovereenkomst sept. 2025. TAM020 Combiplan 9: Aanvangsweg 2, 2 woningen na sloop.
3. Omgevingsvisie: raadstafel 28-10 niet afgerond, vervolg 11-11-2026; besluit nog niet genomen (december 2026 volgens eerder rapport).
4. Compensatiefonds: raadsmededeling 19-5-2026 (via perspectiefnota/nieuw beleid); amendement 5A.1 (EUR 100.000 Salland Loont 2027) unaniem aangenomen 2026-11-04.
5. VHP: niet vastgesteld; coalitieakkoord p. 10 (CPO/zelfbouw in dorpen en buitengebied) en p. 13-14 (VAB, woningen in ruil voor natuur/landschap) bevestigd.
6. Leges: CVDR748764/2, art. 2.6 lid 2 "EUR 00,00"-bepaling letterlijk.
7. Niet gevonden: collegeprogramma 2026-2030, vaststelling VHP, BuitenDelen-status, anterieure overeenkomsten.
