# Hanzedorp

Hanzedorp is een initiatief voor een klein dorp van 10 à 12 woningen op agrarische grond, gerealiseerd als collectief particulier opdrachtgeverschap (CPO): toekomstige bewoners ontwikkelen en bouwen hun woningen samen, zonder tussenkomst van een projectontwikkelaar.

Meer over het initiatief: [hanzedorp.nl](https://hanzedorp.nl)

## Deze repository

Agrarische grond omzetten naar woningbouw hangt sterk af van lokaal en provinciaal beleid. Deze repository bevat het onderzoek dat dat beleid in kaart brengt voor gemeenten in Overijssel en Gelderland.

| Bestand | Inhoud |
|---|---|
| `prompt.md` | Masterprompt voor het onderzoek |
| `provincie_overijssel.md` | Provinciaal referentiekader Overijssel |
| `provincie_gelderland.md` | Provinciaal referentiekader Gelderland |
| `gemeente_zwolle.md` | Beleidsinventarisatie gemeente Zwolle |
| `gemeente_kampen.md` | Beleidsinventarisatie gemeente Kampen (geverifieerd aan brondocumenten, 2026-10-05; raadsstukken in het RIS niet toegankelijk) |
| `gemeente_dalfsen.md` | Beleidsinventarisatie gemeente Dalfsen |
| `gemeente_olst-wijhe.md` | Beleidsinventarisatie gemeente Olst-Wijhe (geverifieerd aan brondocumenten, 2026-10-05) |
| `gemeente_deventer.md` | Stub gemeente Deventer (BuitenDelen); volledig onderzoek volgt |
| `gemeente_ommen.md` | Beleidsinventarisatie gemeente Ommen (concept, nog aan te vullen: bronnen waren niet rechtstreeks raadpleegbaar, bevindingen rusten op zoeksamenvattingen; onderzoek opnieuw uitvoeren met toegang tot ommen.nl, CVDR, officielebekendmakingen.nl en planviewer.nl) |

## Doel van prompt.md

`prompt.md` stuurt een LLM aan om per gemeente in het zoekgebied (19 gemeenten rond Zwolle, Deventer, Apeldoorn en de Veluwerand) een volledig naslagwerk samen te stellen. Het onderzoek verloopt in twee fasen:

1. **Provinciaal kader:** eenmalig per provincie, omdat Overijssel en Gelderland verschillend beleid voeren.
2. **Gemeentelijk onderzoek:** per gemeente 12 vaste onderwerpen, zoals CPO-beleid, openheid voor nieuwbouw buiten de kernen, agrarische herbestemming, VAB-beleid en grondbeleid.

Elk rapport noemt bronnen met URL en raadpleegdatum en sluit af met twee kernvragen: biedt het beleid ruimte voor 10-12 woningen buiten de kernen, en voor omzetting van agrarische grond naar woonfunctie op die schaal?

De rapporten zijn bedoeld als referentie voor zowel mensen als LLM's.

## Werkwijze

De repository wordt beheerd door één persoon. Er wordt niet met branches of pull requests gewerkt: commits gaan direct naar `main`, en elke gemeente krijgt een eigen rapport (`gemeente_<naam>.md`).
