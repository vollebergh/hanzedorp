import sys; sys.path.insert(0,'.')
from lib import Doc
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/8c2cda72-f653-4a4b-aefb-12cf46016d6b/scratchpad/wt-dalfsen/provincie_overijssel.md'
d=Doc(W)

d.insert_after_line('- **Deze versie (actualisatie):**',
'- **Aanvulling:** 2026-10-05 — Claude Sonnet 5.5 (`claude-sonnet-5-5`); effort-niveau niet expliciet ingesteld/bekend. Verwerkt zijn de provinciale bevindingen uit de verificatie van `gemeente_dalfsen.md` (zie changelog, rijen 11-16).')
d.sub('- **Houdbaarheid:** dit bestand beschrijft de stand per **2026-10-02**.','- **Houdbaarheid:** dit bestand beschrijft de stand per **2026-10-02**; de onderdelen uit changelog-rijen 11-16 zijn bijgewerkt per **2026-10-05**.')

d.insert_after_line('| 10 | Woondeal Twente',
'''| 11 | Status provinciaal volkshuisvestingsprogramma onbekend | **Gevonden (2026-10-05):** ontwerp vastgesteld door GS op 30-6-2026 (Prb 2026 nr. 11834), ter inzage 16-7 t/m 26-8-2026 (Prb 2026 nr. 11967); vaststelling na de zienswijzen niet gevonden. Inhoud voor CPO/VAB: zie §5. |
| 12 | URL Omgevingstafel IJsselland gaf 404; "initiatiefnemer in beginsel niet aanwezig" | **Opgelost (2026-10-05):** https://www.odijsselland.nl/over/omgevingstafel. Volgens OD IJsselland kan de initiatiefnemer wél aanwezig zijn; omwonenden niet. §4.2 gecorrigeerd. |
| 13 | Kaartlaag landbouwgebied-typologie niet geraadpleegd | **Deels (2026-10-05):** de nieuwe typologie (art. 4.123) staat niet in de publieke WFS van de provincie; de voormalige ONW-zone wel (indicatie). Werkwijze in §6.2. |
| 14 | Status subsidie 4.39 en andere plafonds | 4.39 staat op 2026-10-05 nog open; plafond Flexpools verhoogd (Prb 2026 nr. 11093). Zie §3.1-3.2. |
| 15 | Dalfser sleutelprojecten niet met naam bekend | **Toegevoegd:** namen en aantallen uit Bijlage 1 Woondeal West-Overijssel (§1.5). |
| 16 | Gemeentelijke KGO-voorbeelden | **Aangevuld:** Dalfsen (sloop-m²-model, maximaal drie woningen, precedent De Tuindershof) in §2.3; BuitenDelen (Lettele) in het ontwerp-VHP als CPO op voormalig agrarisch erf in §2.4. |''')

d.insert_before_line('Opmerkelijk voor het CPO-concept:',
'''**Sleutelprojecten Dalfsen (Bijlage 1 West-Overijssel; gelezen 2026-10-05):** Nieuwleusen Centrum 250 (doorkijk na 2030: 35), Oosterdalfsen Noord 400 (70), Lemelerveld Waterinkweg 206 (50), Hoonhorst De Koele II 83 (nieuw), Dalfsen Het Engelland 100 (400, nieuw): samen **1.039** woningen in 2024-2030 en **1.155** in de doorkijk (inclusief Nieuwleusen Palthelanden 600, dat volledig na 2030 valt en daarom niet als sleutelproject is meegeteld). De bestaande projecten uit de Woondeal van 2022 telden 760 woningen. Het Dalfser Volkshuisvestingsprogramma (oktober 2024) rekende nog met vier projecten en 840-880 woningen (peildatum 2021): gemeentelijke documenten kunnen dus een oudere Woondeal-stand weergeven.
''')

d.insert_after_line('- **Olst-Wijhe** (zoekgebied)',
'''- **Dalfsen, "Beleidsregels Ontwikkelen met Kwaliteit in het Buitengebied 2022" (raad 28-2-2022; CVDR674315) en Programma Landelijk Gebied (college 10-2-2026)** — Dalfsen valt binnen ons zoekgebied (zie `gemeente_dalfsen.md`). Geen percentage van de waardestijging maar een **sloop-m²-model**: voor een eerste woning (≤ 750 m³) 850 m² sloop met asbest of 1.000 m² zonder; voor drie woningen 4.250 resp. 5.000 m²; **maximaal drie extra woningen per erf**. De KGO buiten Sloop voor kansen is maatwerk ("een set met regels voor de toepassing is daarom niet te geven"). Een grotere ontwikkeling liep in 2023-2026 via KGO-maatwerk met provinciaal overleg: **De Tuindershof** (17 woningen op voormalige tuinderserven; kassen voor 60% meegeteld; genoemde investering ca. € 484.000 excl. btw; buitenplanse omgevingsplanactiviteit met bindend gemeentelijk raadsadvies). Bronnen: https://lokaleregelgeving.overheid.nl/CVDR674315/2 ; raadsvoorstel nr. 2064 en KGO-onderbouwing (RIS Dalfsen, raad 16-3-2026).''')

d.insert_after_line('*Interpretatie, nog niet getoetst:* rood-voor-rood',
'*Eerste toetsing (Dalfsen, 2026-10-05):* bevestigt (a) en (b): het Dalfser kader stopt bij drie extra woningen per erf; de enige gevonden ontwikkeling van meer dan 10 woningen (De Tuindershof, 17) liep via KGO-maatwerk met een gebiedsgerichte onderbouwing, zonder rekenformule en met bindend raadsadvies.')

d.insert_after_line('- **Praktijkvoorbeeld in zoekgebied:**',
'- **BuitenDelen als CPO bevestigd (2026-10-05):** het ontwerp-Volkshuisvestingsprogramma Overijssel 2026-2035 (Prb 2026 nr. 11834, bijlage II) noemt BuitenDelen in Lettele een "collectief particulier opdrachtgeverschap-project (CPO) op een voormalig agrarisch erf", met biobased woningbouw, collectieve faciliteiten en biodivers landschapsbeheer, dat "door gebruik te maken van verruimde provinciale en gemeentelijke kaders" een praktijkvoorbeeld is voor "moderne \'rood-voor-rood\' ontwikkelingen". Aantal woningen, juridische route en gemeentelijk kader (Deventer, "Kansen uit Buiten") zijn niet onderzocht: geschikt voor het Deventer-rapport.')

d.sub('**Status 2026-10-02: de regeling staat nog open voor aanvragen ("tot het budget bereikt is")**','**Status 2026-10-02 (bevestigd 2026-10-05): de regeling staat nog open voor aanvragen ("tot het budget bereikt is")**')
d.insert_after_line('Bron: https://regelen.overijssel.nl/Producten_en_diensten/Subsidies/Wonen_en_leefbaarheid/Beleid_transformatie',
'*Gebruik door gemeenten:* in de Dalfser verificatie (2026-10-05) is geen aanvraag van Dalfsen gevonden (eigen Programma Landelijk Gebied en Regisseur Landelijk Gebied); het aantal toegekende aanvragen elders is nog steeds niet gepubliceerd. De regeling vereist deelname aan het provinciale lerend netwerk en, bij activiteit B/C, een intergemeentelijk programma met onder meer ontwikkelperspectieven die de twee landbouwgebied-typen op kaart duiden.')

d.insert_after_line('**Wijzigingen Uitvoeringsbesluit subsidies Overijssel 2022 (Prb 2025 nr. 17163',
'''**Gebruik in de praktijk (Dalfsen, Woonupdate 005, 8-7-2025):** de **Adviespool Provincie Overijssel** (externe expertise tot € 50.000; maximaal tweemaal per gemeente) is door Dalfsen eenmaal gebruikt voor Het Engelland; het **Ondersteuningsteam Wonen Zorg** (2025) is gevraagd voor Palthelanden en Het Engelland; **Betaalbaar wonen in kleine steden en dorpen** wordt onderzocht (geen aanvraag); het rijksfonds NFBK (koperskorting tot € 405.000) en de rijksrealisatiestimulans (vanaf 2026) bestaan daarnaast. **Flexpools versnelling woningbouw:** het plafond voor 2023-2026 is verhoogd van € 3.678.017 naar € 3.955.017 (Prb 2026 nr. 11093, 3-7-2026; volgorde van ontvangst). Een latere wijziging van het Uitvoeringsbesluit (Prb 2025 nr. 21260, 19-12-2025) is niet gelezen.''')

d.sub('IJsselland: https://www.odijsselland.nl/omgevingstafel-ijsselland — deze URL gaf op 2026-10-02 een 404, de pagina is mogelijk verplaatst). Bij de Omgevingstafel is de initiatiefnemer in beginsel niet aanwezig; de gemeente beslist wanneer ketenpartners (waterschap, GGD, veiligheidsregio) worden betrokken.',
'IJsselland: https://www.odijsselland.nl/over/omgevingstafel, gelezen 2026-10-05). Volgens OD IJsselland bepaalt de gemeente of een initiatief aan de regionale tafel komt (bij grotere impact en advies van twee of meer ketenpartners: GGD, Waterschap Drents Overijsselse Delta, Veiligheidsregio, Omgevingsdienst, Provincie, Rijkswaterstaat); de initiatiefnemer "kan en mag" aanwezig zijn, omwonenden niet (participatie is een gemeentelijke taak). *Correctie op de versie van 2026-10-02, die stelde dat de initiatiefnemer in beginsel niet aanwezig is.* Gemeenten kunnen daarnaast een eigen "Omgevingstafel" als principeverzoekroute met leges hanteren (Dalfsen 2026: eenvoudig € 577,40, complex € 1.233,10).')

d.insert_before_line('- **Instructieregels onder Actualisatie 2026 (art. 4.2a):**',
'- **Gemeentelijk raadsadvies (art. 16.15a lid 1 sub b Ow) is iets anders dan de provinciale Lijst BOPA** en verschilt per gemeente. Dalfsen (CVDR705154, geldend sinds 1-1-2024) vraagt bindend raadsadvies bij meer dan 3 nieuwe woningen in het buitengebied en bij meer dan 11 in of direct aangrenzend aan bestaand bebouwd gebied, en verplichte participatie al bij één nieuwe woning. Een zoekresultaat met vrijwel dezelfde titel (CVDR727504) bleek van Montfoort te zijn; controleer altijd de uitgevende gemeente.')

d.sub('(GS-besluit werd rond de zomer van 2026 beoogd; **niet gevonden of dit is vastgesteld**)','(zie hieronder: ontwerp vastgesteld door GS op 30-6-2026; vaststelling nog niet gevonden)')
d.insert_after_line("- **Termijnen volkshuisvestingsprogramma's:**",
'''- **Ontwerp Volkshuisvestingsprogramma Overijssel 2026-2035** (GS 30-6-2026; Prb 2026 nr. 11834; kennisgeving Prb 2026 nr. 11967; ter inzage 16-7 t/m 26-8-2026; gelezen 2026-10-05). Vrijwillig programma op grond van art. 3.4-3.5 Ow dat na inwerkingtreding van de Regiewet geldt als het programma in de zin van die wet. Artikel I van het besluit noemt "2026-2032", de titel "2026-2035". Voor een CPO op een erf relevant:
  - **Drie ruimtelijke woonstrategieën:** Stedelijk, Centraal en **Ontspannen wonen**; de accenten zijn "niet kaderstellend" maar bedoeld als "inspiratie met ruimte voor eigen invulling".
  - **Ontspannen wonen** (dorpen, buitengebied): bouwen voor de lokale behoefte; een kern kan meer bouwen dan de lokale behoefte bij regionale toegevoegde waarde; "het is een pre als gemeenten hebben nagedacht over de woningbouwprogrammering in de kleine kernen". **"Collectieve woonvormen passen hier goed bij: ze versterken de sociale cohesie én helpen de lokale woningvraag te vervullen."** Transformatie van vrijkomende agrarische bebouwing kan "in sommige gevallen" een kans bieden, "mits deze in de directe nabijheid van een dorp ligt".
  - **VAB-uitgangspunten:** de herbestemming belemmert de bedrijfsvoering van omliggende agrarische bedrijven niet; stimuleren om "gebiedsgericht geclusterd" te ontwikkelen; woningbouw draagt bij aan behoud en versterking van landschap, natuur en cultuurhistorie; de ligging biedt passende woonmogelijkheden voor de doelgroep(en).
  - **Woonvormen:** de provincie stimuleert meergeneratiewoningen en geclusterd wonen en ondersteunt "projecten die zulke innovatieve toekomstbestendige woonoplossingen opschalen". Ouderenhuisvesting (nultrede, geclusterd, zorggeschikt) komt in de provinciale planmonitor. Voorbeeld BuitenDelen (Lettele): zie §2.4.
  - Bronnen: https://zoek.officielebekendmakingen.nl/prb-2026-11834.html ; https://zoek.officielebekendmakingen.nl/prb-2026-11967.html.''')

d.line_replace('| Provinciaal volkshuisvestingsprogramma Overijssel |','| Provinciaal volkshuisvestingsprogramma Overijssel | ontwerp ter inzage tot 26-8-2026 (Prb 2026 nr. 11967); GS-vaststelling niet gevonden; beide Woondeals worden daarin uitgewerkt |')
d.line_replace('| Subsidie 4.39 (VAB/erftransformatie) |','| Subsidie 4.39 (VAB/erftransformatie) | plafond € 1.640.250, verplichting vóór eind 2026; nog open op 2026-10-05 |')

d.line_replace('2. **Kaartlaag "ontwikkelingsperspectieven landbouwgebieden"**','2. **Kaartlaag "ontwikkelingsperspectieven landbouwgebieden"** (art. 4.123): de nieuwe typologie is niet in de publieke WFS van de provincie (services.geodataoverijssel.nl/geoserver/ows) gevonden; de voormalige zone Ondernemen met Natuur en Water (laag IKN_Zone_Ondernemen_met_Natuur_en_Water) is wel beschikbaar en kan als indicatie dienen (in Dalfsen 5,5% van het oppervlak). Per kandidaatlocatie blijft controle op de definitieve kaartlaag nodig (https://omgevingswet.overheid.nl/regels-op-de-kaart). Werkwijze: WFS-lagen (o.a. NNN, Natura 2000, grondwaterbescherming, essen, landgoederen) doorsnijden met de gemeentegrens (PDOK gebiedsindelingen) en adressen (PDOK-Locatieserver); zie `gemeente_dalfsen.md` §3.7.')
d.line_replace('8. **Provinciaal volkshuisvestingsprogramma Overijssel**','8. **Provinciaal volkshuisvestingsprogramma Overijssel:** ontwerp gepubliceerd (zie §5); vaststelling na de zienswijzentermijn (tot 26-8-2026) niet gevonden.')
d.insert_after_line('10. De catalogus gebiedskenmerken',
'''11. **Gemeentelijke adviesrecht-lijsten (raad) en leges** verschillen sterk per gemeente (Dalfsen: meer dan 3 woningen in het buitengebied; Montfoort: andere lijst); verwar ze niet met de provinciale Lijst BOPA.
12. **Zoektechniek:** Gemeenteblad en Provinciaal blad zijn doorzoekbaar via de SRU-service van de officiële publicaties (https://repository.overheid.nl/sru, x-connection=officielepublicaties) en de CVDR via https://zoekservice.overheid.nl/sru (x-connection=cvdr). Gemeentelijke raadsinformatiesystemen met een browsercheck (Anubis) vergen een gewone browser.''')

d.insert_before_line('**Niet (meer) bereikbaar tijdens dit onderzoek**',
'''**Aanvullend geraadpleegd op 2026-10-05**
- https://zoek.officielebekendmakingen.nl/prb-2026-11834.html (ontwerp Volkshuisvestingsprogramma Overijssel 2026-2035) en https://zoek.officielebekendmakingen.nl/prb-2026-11967.html (kennisgeving)
- https://zoek.officielebekendmakingen.nl/prb-2026-11093.html (subsidieplafonds, 3-7-2026)
- https://regelen.overijssel.nl/Producten_en_diensten/Subsidies/Wonen_en_leefbaarheid/Beleid_transformatie_agrarische_bebouwing_erven_en_gronden (regeling 4.39, nog open)
- https://www.odijsselland.nl/over/omgevingstafel (Omgevingstafel IJsselland)
- https://services.geodataoverijssel.nl/geoserver/ows (WFS-lagen) en https://service.pdok.nl/cbs/gebiedsindelingen/2024/wfs/v1_0 (gemeentegrenzen)
- Woondeal West-Overijssel, Bijlage 1 (sleutelprojecten per gemeente), zie hierboven
- Dalfsen: https://lokaleregelgeving.overheid.nl/CVDR674315/2 en RIS Dalfsen (raad 16-3-2026; raadsmemo Woonupdate 005 en Actualisatie Woondeal)
''')
d.line_replace('- https://www.odijsselland.nl/omgevingstafel-ijsselland — 404','- https://www.odijsselland.nl/omgevingstafel-ijsselland — 404 (2026-10-02); de werkende pagina is https://www.odijsselland.nl/over/omgevingstafel (2026-10-05).')
d.save(); print('ok')
