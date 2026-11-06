# Kampen: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels, geen bronbestanden in deze notitie.

## Commando's
- `python3 -I tools/dso.py rp-info NL.IMRO.0166.00991134-VB01` -> Buitengebied 2014: vastgesteld 2014-03-06, besluit 14INT00181, regelStatus geldend, dossier "geheel onherroepelijk in werking".
- `python3 -I tools/dso.py pons gm0166` -> 1 pons-gebied (H21 Broekswetering), omgevingsplan versie 4, inwerking 2026-07-01. Rest van het buitengebied: tijdelijk deel geldt.
- `python3 -I tools/dso.py rp-tekst NL.IMRO.0166.00991134-VB01` (volledige planregels + toelichting, 570 kB, in scratchpad) en gerichte greps.
- `python3 -I tools/dso.py regelingen gm0166 [--ontwerp]`, `vergunningen gm0166`, `tekst /akn/nl/act/gm0166/2020/omgevingsplan --grep ...`.
- `python3 -I tools/dso.py rp-tekst NL.IMRO.0166.00991228-VB01` en `...00991363-VB01` (Zalk Erf 4 / Erf 5).
- Notubiz publieke API (organisatie 1499): `events`, `events/meetings/<id>`, `document/<id>/1` (eigen hulpscript in de scratchpad; pypdf voor pdf-tekst).
- `python3 -I tools/ori.py search ... --org kampen` -> 0 treffers: bron `kampen` staat in `/api/sources` op `implemented: false`.

## Bevindingen
1. **Woningaantal per erf (Buitengebied 2014) opgelost.** Regels: art. 4.9.1 onder a sub 8 I en art. 26.6 lid a onder 3: bij karakteristieke bedrijfswoning/woning van minimaal 1000 m3 mag het aantal woningen worden vergroot tot niet meer dan 2; art. 4.9.1 sub 5-6: een woning blijft, aantal neemt niet toe; art. 26.2.1 b: 1 woning per bouwvlak tenzij aanduiding 'maximum aantal wooneenheden'. Toelichting §3.4.2: "tot een maximum van twee woningen"; §5.2: "Meer dan twee wooneenheden staan we niet op voorhand al bij recht toe". Alleen §2.4.5 zegt "ten hoogste drie woningen" (beschrijvende passage).
   Uittreksel art. 4.9.1: "5. één (bedrijfs)woning gehandhaafd blijft; 6. het aantal woningen niet toeneemt; ... 8. ... I. wanneer er sprake is van een karakteristieke bedrijfswoning met aangebouwde bedrijfsruimten van tenminste 1000 m3, het aantal woningen binnen deze bebouwing mag worden vergroot tot niet meer dan 2".
2. Geen rood-voor-rood, geen CPO, geen stikstofregeling voor woningbouw in de regels (alleen stikstofneutrale uitbreiding dieren, art. 4.6).
3. **Broekswetering**: omgevingsplan art. 21.39 lid 2: "Het aantal wooneenheden dat mag worden gebruikt voor wonen bedraagt niet meer dan 68." Totaal klopt met beide verdelingen; verdeling blijft onopgelost.
4. **Zalk Erf 4/5**: toelichting Erf 4 "in totaal 12 woningen ... waarvan 2 tiny houses"; Erf 5 "in totaal 13 woningen"; AERIUS-paragraaf: "In totaal ... 26 woningen". Vier zienswijzen; provincie 22-2-2023 geen zienswijze; reactienota Bijlage 12 (Erf 4) / 11 (Erf 5). Vastgesteld 2024-01-18, besluit 76863-2023.
5. **Volkshuisvestingsprogramma**: raad 17-9-2026, agendapunt 9, algemene stemmen (25) startnotitie vastgesteld; volkshuisvestingsverordening 1-1-2028, college kijkt of sneller kan. Startnotitie zelf niet als bijlage gepubliceerd.
6. **Nieuwe vergunningen** (DSO `vergunningen gm0166`, Gmb): IJsseldijk 48 en 50 (functie bedrijfswoningen naar 2 reguliere woningen, Gmb 2026, 465697), Oudestraat 62 (BOPA 2 woningen, Gmb 2026, 487853), Zwolseweg 17B (BOPA woning, Gmb 2026, 510380), Plasweg 3A (woning, Gmb 2026, 136281), Noordwendigedijk 6A (Gmb 2025, 90041). Alleen metadata. Geen 10-12-woningenproject op agrarische grond.
7. **Ozon ontwerpen**: ontwerp-omgevingsplan 2026-06-19 en 2025-12-15 en Omgevingsprogramma Warmte; tekst via `tekst --ontwerp` leeg. 2026-06-19 waarschijnlijk niet woningbouw in buitengebied (raad 22-10-2026 behandelt wijziging Paviljoen IJsselkogge) [INT].
8. TAM-plan Kamperzeedijk 19 Grafhorst (NL.IMRO.0166.00993009-VS01, 2025-10-16, 3e wijziging TAM-omgevingsplan): RP-API geeft geen tekst.
9. Raad 22-10-2026: startnotitie Perspectief Verdichting en Omgevingskwaliteit (hamerstuk; geen concrete locaties); Raadsbrief "Vaststelling Prioritering woningbouwprojecten 2026" (College 58189-2026) niet gelezen.
10. Niet gevonden: uitkomst beroep Kamper Wetering (WebSearch, rechtspraak open data); document Uitvoeringskader VAB IJsseldelta.
