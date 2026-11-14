# Hellendoorn: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels of bronbestanden.

## Commando's
- `python3 -I tools/dso.py pons gm0163` -> omgevingsplan v11 (2026-08-07), geen pons. `regelingen gm0163 [--ontwerp]`: ontwerp-Omgevingsvisie 'Hellendoorn 2040: Ruimte voor elkaar'; voorbereidingsbesluiten raatakkers (2025-04-04) en karrensporen (2025-07-14).
- Ontwerp-visie tekst via eigen wrapper (tool-bug: `tools/dso.py tekst --ontwerp` leest `documentComponenten`, Ozon levert `ontwerpDocumentComponenten`). Volledige technischId nodig (de lijstuitvoer wordt in de console niet afgekapt, maar mijn eerste poging gebruikte een afgekapte id: 404).
- `rp-info/rp-tekst NL.IMRO.0163000095101-` (moederplan Buitengebied 2009): geen tekst. `rp-tekst NL.IMRO.0163.BPBURAAMSWEG6-VG01` en `…BPBUHAARLERVELDWG6-VG01`, `…BPBUAGRNWONEN22-VG01`.
- `rp-plannen 0163 --tam` -> leeg. `vergunningen gm0163`.
- `ori.py search/get --org hellendoorn`: concept college-uitvoeringsprogramma 2026-2030 (doc 17508030).

## Bevindingen
1. Raamsweg 6: art. 4.2.2 een woning per bouwvlak tenzij aanduiding; art. 9.1 extra zelfstandige woonruimte (<= 1.000 m3, dringende redenen); 9.2 bijgebouw. Geen wijzigingsbevoegdheid/rood-voor-rood in de herzieningen.
2. Ontwerp-visie §13.3: clusters van 5-10 woningen in de buurtschappen; drie-generatie-erven met randvoorwaarden. Kaartbijlagen niet opgehaald.
3. Concept CUP 2026-2030: buurtschappen in Routekaart 1.000 woningen; evaluatie rood-voor-rood (actie 68-69); geen CPO.
4. Niet gevonden: tekst moederplan Buitengebied 2009; kaartbijlagen; woningbehoefteonderzoek 2024; formele zienswijze op provinciale visie; Haarlerveldweg 12.
