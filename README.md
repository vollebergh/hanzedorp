# Hanzedorp

Hanzedorp is een initiatief voor een klein dorp van 10 à 12 woningen op agrarische grond, gerealiseerd als collectief particulier opdrachtgeverschap (CPO): toekomstige bewoners ontwikkelen en bouwen hun woningen samen, zonder tussenkomst van een projectontwikkelaar.

Meer over het initiatief: [hanzedorp.nl](https://hanzedorp.nl)

## Deze repository

Agrarische grond omzetten naar woningbouw hangt sterk af van lokaal en provinciaal beleid. Deze repository bevat het onderzoek dat dat beleid in kaart brengt voor gemeenten in Overijssel en Gelderland.

| Bestand | Inhoud |
|---|---|
| `prompt.md` | Masterprompt voor het onderzoek |
| `tools/ori.py` | Client voor de Open Besluitvorming-API (raadsstukken doorzoeken; zie `tools/README.md`) |
| `tools/README.md` | Gebruiksaanwijzing van de tools |
| `provincie_overijssel.md` | Provinciaal referentiekader Overijssel (actualisatie 2026-10-18 via RIS) |
| `provincie_gelderland.md` | Provinciaal referentiekader Gelderland |
| `gemeente_zwolle.md` | Beleidsinventarisatie gemeente Zwolle (actualisatie 2026-10-18 via RIS) |
| `gemeente_kampen.md` | Beleidsinventarisatie gemeente Kampen (geverifieerd aan brondocumenten, 2026-10-05; raadsstukken in het RIS niet toegankelijk) |
| `gemeente_dalfsen.md` | Beleidsinventarisatie gemeente Dalfsen |
| `gemeente_olst-wijhe.md` | Beleidsinventarisatie gemeente Olst-Wijhe (geverifieerd aan brondocumenten, 2026-10-05) |
| `gemeente_deventer.md` | Beleidsinventarisatie gemeente Deventer (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-14; vervangt de stub van 2026-10-05; actualisatie 2026-10-18 via RIS) |
| `gemeente_ommen.md` | Beleidsinventarisatie gemeente Ommen (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-11; vervangt het concept van 2026-10-02; actualisatie 2026-10-18 via RIS) |
| `gemeente_zwartewaterland.md` | Beleidsinventarisatie gemeente Zwartewaterland (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-12; actualisatie 2026-10-18 via RIS) |
| `gemeente_raalte.md` | Beleidsinventarisatie gemeente Raalte (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-15; actualisatie 2026-10-18 via RIS) |
| `gemeente_hardenberg.md` | Beleidsinventarisatie gemeente Hardenberg (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-15; actualisatie 2026-10-18 via RIS) |
| `gemeente_hattem.md` | Beleidsinventarisatie gemeente Hattem (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-16; actualisatie 2026-10-18 via RIS) |
| `gemeente_hellendoorn.md` | Beleidsinventarisatie gemeente Hellendoorn (vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-16; actualisatie 2026-10-18 via RIS) |
| `gemeente_voorst.md` | Beleidsinventarisatie gemeente Voorst (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-18; alle onderzoeken op Sonnet 5.5) |
| `gemeente_oldebroek.md` | Beleidsinventarisatie gemeente Oldebroek (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-18; alle onderzoeken op Sonnet 5.5) |
| `gemeente_nunspeet.md` | Beleidsinventarisatie gemeente Nunspeet (Gelderland; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-19; alle onderzoeken op Sonnet 5.5) |
| `gemeente_heerde.md` | Beleidsinventarisatie gemeente Heerde (Gelderland, woondealregio Stedendriehoek; buiten de 19 gemeenten van het oorspronkelijke zoekgebied; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-21; alle onderzoeken op Sonnet 5.5) |
| `gemeente_elburg.md` | Beleidsinventarisatie gemeente Elburg (Gelderland, woondealregio Noord-Veluwe; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-25; alle onderzoeken op Sonnet 5.5) |
| `gemeente_ermelo.md` | Beleidsinventarisatie gemeente Ermelo (Gelderland, woondealregio Noord-Veluwe; vier deelonderzoeken samengevoegd met verificatieronde, 2026-10-27; alle onderzoeken op Sonnet 5.5) |
| `ruwe-data/` | Gefilterde ruwe deelonderzoeksdata (deelrapporten, scripts, kleine tabellen) per gemeente; zie `ruwe-data/README.md` |

## Doel van prompt.md

`prompt.md` stuurt een LLM aan om per gemeente in het zoekgebied (19 gemeenten rond Zwolle, Deventer, Apeldoorn en de Veluwerand) een volledig naslagwerk samen te stellen. Het onderzoek verloopt in twee fasen:

1. **Provinciaal kader:** eenmalig per provincie, omdat Overijssel en Gelderland verschillend beleid voeren.
2. **Gemeentelijk onderzoek:** per gemeente 12 vaste onderwerpen, zoals CPO-beleid, openheid voor nieuwbouw buiten de kernen, agrarische herbestemming, VAB-beleid en grondbeleid.

Elk rapport noemt bronnen met URL en raadpleegdatum en sluit af met twee kernvragen: biedt het beleid ruimte voor 10-12 woningen buiten de kernen, en voor omzetting van agrarische grond naar woonfunctie op die schaal?

De rapporten zijn bedoeld als referentie voor zowel mensen als LLM's.

## Werkwijze

De repository wordt beheerd door één persoon. Er wordt niet met branches of pull requests gewerkt: commits gaan direct naar `main`, en elke gemeente krijgt een eigen rapport (`gemeente_<naam>.md`).
