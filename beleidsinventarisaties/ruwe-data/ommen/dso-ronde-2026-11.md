# Ommen: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels of bronbestanden.

## Commando's
- `python3 -I tools/dso.py pons gm0175` -> omgevingsplan v4 (2026-01-23); geen pons. `regelingen gm0175 [--ontwerp]`: 3 ontwerp-wijzigingen (hele omgevingsplan); tekst via eigen wrapper (tool-bug `ontwerpDocumentComponenten`): "hoofdstuk 1-21 gelden als aanvulling op ... het tijdelijke deel ... en laten die regels ongewijzigd".
- `rp-plannen 0175 --alle ...`: moederplan 'Buitengebied 2012' (NL.IMRO.0175.buiten201200001) niet in RP-API (404 in alle versie-varianten); herzieningen buiten2012bp00xx verwijzen naar 'Buitengebied, herziening 2013-2' = NL.IMRO.0175.20131003006-vg01 (vastgesteld 2014-10-30, besluit 1069085, geldend). `rp-tekst` daarvan gelezen.
- `vergunningen gm0175`: geen publicaties.
- `ori.py search/get --org ommen`: Hammerflier, Grondprijsbrief, woningbehoefteonderzoek, burgemeester (vergadering 2026-10-08).

## Bevindingen
1. Art. 3.6.3: een compensatiewoning bij >= 850 m2 sloop; 750 m3; 150 m2 bijgebouwen; art. 3.6.7 Wonen - VAB; 3.6.10 vervolgfuncties (tabel 4). Art. 17.2.2: overige woningen "een, tenzij anders op de verbeelding aangegeven".
2. Rood-voor-Rood 2026 (CVDR757546): 850 m2 voor een, 2.000 m2 voor twee compensatiewoningen: beleidsregel gaat verder dan de wijzigingsbevoegdheid.
3. Burgemeestersprocedure: vacature sinds 2026-04-10; raadsvergadering 2026-10-08 "Bekendmaking aanbeveling"; naam niet vastgesteld.
4. Niet gevonden: woningbehoefteonderzoek 2024, grondprijsbrief, Hammerflier-besluit.
