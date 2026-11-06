# Hanzedorp

Hanzedorp is een initiatief voor een klein dorp van 10 à 12 woningen op agrarische grond, gerealiseerd als collectief particulier opdrachtgeverschap (CPO): toekomstige bewoners ontwikkelen en bouwen hun woningen samen, zonder tussenkomst van een projectontwikkelaar.

Meer over het initiatief: [hanzedorp.nl](https://hanzedorp.nl)

## Deze repository

Agrarische grond omzetten naar woningbouw hangt sterk af van lokaal en provinciaal beleid. Deze repository bevat het onderzoek dat dat beleid in kaart brengt voor gemeenten in Overijssel en Gelderland.

| Bestand | Inhoud |
|---|---|
| `prompt.md` | Masterprompt voor het onderzoek |
| `openstaande-punten.md` | Openstaande taken en ontbrekende kennis per rapport (stand 2026-11-01) |
| `dso-inventarisatie.md` | Wat de DSO/RP-API aanvullend ontsluit, status van ruimtelijkeplannen en pons-check per gemeente (2026-11-06) |
| `tools/ori.py` | Client voor de Open Besluitvorming-API (raadsstukken doorzoeken; zie `tools/README.md`) |
| `tools/dso.py` | Client voor DSO-Ozon (Presenteren v8) en de Ruimtelijke Plannen-API (v4); sleutels in `dso.txt`/`rp.txt` (niet in git) |
| `tools/README.md` | Gebruiksaanwijzing van de tools |
| `provincie_overijssel.md` | Provinciaal referentiekader Overijssel (actualisatie 2026-10-18 via RIS) |
| `provincie_gelderland.md` | Provinciaal referentiekader Gelderland |
| `gemeente_zwolle.md` | Beleidsinventarisatie gemeente Zwolle (actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_kampen.md` | Beleidsinventarisatie gemeente Kampen (geverifieerd aan brondocumenten, 2026-10-05; raadsstukken in het RIS niet toegankelijk); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_dalfsen.md` | Beleidsinventarisatie gemeente Dalfsen; aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_olst-wijhe.md` | Beleidsinventarisatie gemeente Olst-Wijhe (geverifieerd aan brondocumenten, 2026-10-05); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_deventer.md` | Beleidsinventarisatie gemeente Deventer (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-14; vervangt de stub van 2026-10-05; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_ommen.md` | Beleidsinventarisatie gemeente Ommen (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-11; vervangt het concept van 2026-10-02; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_zwartewaterland.md` | Beleidsinventarisatie gemeente Zwartewaterland (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-12; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_raalte.md` | Beleidsinventarisatie gemeente Raalte (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-15; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_hardenberg.md` | Beleidsinventarisatie gemeente Hardenberg (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-15; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_hattem.md` | Beleidsinventarisatie gemeente Hattem (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-16; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_hellendoorn.md` | Beleidsinventarisatie gemeente Hellendoorn (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-16; actualisatie 2026-10-18 via RIS); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_voorst.md` | Beleidsinventarisatie gemeente Voorst (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-18; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_oldebroek.md` | Beleidsinventarisatie gemeente Oldebroek (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-18; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_nunspeet.md` | Beleidsinventarisatie gemeente Nunspeet (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-19; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_heerde.md` | Beleidsinventarisatie gemeente Heerde (Gelderland, woondealregio Stedendriehoek; buiten de 19 gemeenten van het oorspronkelijke zoekgebied; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-21; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_elburg.md` | Beleidsinventarisatie gemeente Elburg (Gelderland, woondealregio Noord-Veluwe; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-25; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_ermelo.md` | Beleidsinventarisatie gemeente Ermelo (Gelderland, woondealregio Noord-Veluwe; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-27; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_harderwijk.md` | Beleidsinventarisatie gemeente Harderwijk (Gelderland, woondealregio Noord-Veluwe; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-29; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_apeldoorn.md` | Beleidsinventarisatie gemeente Apeldoorn (Gelderland, woondealregio Stedendriehoek; vier deelonderzoeken samengevoegd, 2026-10-31; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `gemeente_epe.md` | Beleidsinventarisatie gemeente Epe (Gelderland, woondealregio Stedendriehoek; vier deelonderzoeken samengevoegd met toetsronde, 2026-11-01; alle onderzoeken op Sonnet 5.5); aanvulling DSO/RP-ronde 2026-11-06 (planregels tijdelijk deel, Ozon; Sonnet 5.5, effort high) |
| `ruwe-data/` | Gefilterde ruwe deelonderzoeksdata (deelrapporten, scripts, kleine tabellen) per gemeente; zie `ruwe-data/README.md` |

## Doel van prompt.md

`prompt.md` stuurt een LLM aan om per gemeente in het zoekgebied (19 gemeenten rond Zwolle, Deventer, Apeldoorn en de Veluwerand) een volledig naslagwerk samen te stellen. Het onderzoek verloopt in twee fasen:

1. **Provinciaal kader:** eenmalig per provincie, omdat Overijssel en Gelderland verschillend beleid voeren.
2. **Gemeentelijk onderzoek:** per gemeente 12 vaste onderwerpen, zoals CPO-beleid, openheid voor nieuwbouw buiten de kernen, agrarische herbestemming, VAB-beleid en grondbeleid.

Elk rapport noemt bronnen met URL en raadpleegdatum en sluit af met twee kernvragen: biedt het beleid ruimte voor 10-12 woningen buiten de kernen, en voor omzetting van agrarische grond naar woonfunctie op die schaal?

De rapporten zijn bedoeld als referentie voor zowel mensen als LLM's.

## Werkwijze

De repository wordt beheerd door één persoon. Er wordt niet met branches of pull requests gewerkt: commits gaan direct naar `main`, en elke gemeente krijgt een eigen rapport (`gemeente_<naam>.md`).
