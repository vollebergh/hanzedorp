import sys; sys.path.insert(0,'.')
from lib import Doc
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/8c2cda72-f653-4a4b-aefb-12cf46016d6b/scratchpad/wt-dalfsen/gemeente_dalfsen.md'
d=Doc(W)

d.sub('> **Status: geverifieerde versie (2026-10-04).**','> **Status: geverifieerde versie (2026-10-04; aangevuld 2026-10-05).**')

d.insert_after_line('  - Verificatieronde en herschrijving (2026-10-04):',
'  - Aanvulling (2026-10-05): Claude Sonnet 5.5 (`claude-sonnet-5-5`), effort-niveau niet expliciet ingesteld of bekend.')
d.insert_after_line('  - Stukken uit het raadsinformatiesysteem',
'  - Aanvulling 2026-10-05: kaartlagen van de provincie (WFS services.geodataoverijssel.nl) gecombineerd met de gemeentegrens (PDOK, CBS-gebiedsindelingen 2024), en Gemeenteblad en Provinciaal blad doorzocht via de SRU-zoekservice van overheid.nl (repository.overheid.nl/sru).')

d.insert_after_line('> 9. "Voorkeursrecht',
'''> 10. **Natura 2000 ligt niet in Dalfsen** (kaartlaag, §3.7): de conceptclaim dat het Vecht- en Beneden-Reggegebied "deels in Dalfsen" ligt is niet bevestigd. Beide gebieden grenzen aan de gemeentegrens (7 m en 41 m op de gegeneraliseerde grens) maar overlappen niet; bij de projectlocaties liggen ze 2,6-6,6 km weg.
> 11. **Sleutelprojecten Woondeal** zijn opgelost met Bijlage 1 van de Woondeal: 5 projecten, 1.039 woningen, met namen (§5). De "tegenstrijdigheid" met het VHP (4 projecten, 840-880 woningen) betrof een ouder peilmoment (Woondeal 2022).
> 12. **Vosserburen** is vergund via een omgevingsvergunning in de uitgebreide procedure met verklaring van geen bedenkingen van de raad: aanvraag 29-12-2023, besluit 20-12-2024 (§6).
> 13. **KGO-onderbouwing De Tuindershof gelezen:** genoemde investering ca. € 484.000 excl. btw (§6).
> 14. **Zetelverdeling 2026** uit een gelezen bron bevestigd (§10.1). "PRO Dalfsen" blijft niet geïdentificeerd.
> 15. **Het provinciale Volkshuisvestingsprogramma** (ontwerp, GS 30-6-2026) en het voorbeeld BuitenDelen (CPO op voormalig agrarisch erf, Lettele/Deventer) zijn nieuw gevonden; zie `provincie_overijssel.md` §5 en §2.4.''')

d.line_replace('| Woonregio |',
'| Woonregio | West-Overijssel; Woondeal 2025-2030 (Actualisatie 20-3-2025, Bijlage 1): Dalfsen 479 woningen gerealiseerd Q1 2022-Q4 2024; 5 sleutelprojecten 2024-2030 met 1.039 woningen (Nieuwleusen Centrum 250, Oosterdalfsen Noord 400, Waterinkweg 206, De Koele II 83, Het Engelland 100); doorkijk 2031-2035: 1.155 (o.a. Palthelanden 600, Het Engelland 400). Het VHP (oktober 2024) rekende nog met de vier sleutelprojecten van de Woondeal 2022 (840-880 woningen) |')

d.insert_after_line('  - Vechtdal Centraal: Vosserburen (juli 2026)',
'''- **Aanvullend gelezen op 2026-10-05:**
  - Woondeal West-Overijssel, Actualisatie 2025-2030, Bijlage 1 (sleutelprojecten); raadsmemo Actualisatie Woondeal (college 1-4-2025, raad 19-5-2025); Woonupdate 005 (raadsmemo, 8-7-2025).
  - KGO-onderbouwing De Tuindershof (Bureau voor Planvorming Advies, 14-2-2023) en de ruimtelijke onderbouwing (47 p.), RIS raad 16-3-2026 (bijlagen 7-1 en 7-3).
  - Gemeenteblad: Bijlage 1 (kaart) bij CVDR705154 / Gmb 2023, 513200 (exb-2023-56527); Vosserburen: Gmb 2024, 11999, 454253 en 541698; 9e Verzamelplan en Erfwonen: Gmb 2023, 559954 en Gmb 2025, 259478; Straatnaambesluit De Tuindershof: Gmb 2026, 337369.
  - Gemeentelijke webpagina's: https://www.dalfsen.nl/tiny-house-schuurwoningen-en-kleine-woningen-ruimtelijke-kwaliteit (met de drie beeldkwaliteitsplannen) en https://www.dalfsen.nl/vooroverleg-initiatiefnemer.
  - Prestatieafspraken Wonen Dalfsen 2025 (Vechtdal Wonen/VechtHorst).
  - Provincie: regeling 4.39 op regelen.overijssel.nl; Prb 2026, 11834 en 11967 (ontwerp Volkshuisvestingsprogramma Overijssel 2026-2035); Prb 2026, 11093 (subsidieplafonds); Omgevingstafel IJsselland (OD IJsselland); WFS-kaartlagen Provincie Overijssel.
  - Verkiezingsuitslag 2026: Vechtdal Centraal (2026-03) en DalfsenNet-analyse (2026-03).''')

d.insert_before_line('### 3.2 Procedure bij provincie en raad',
'''**Erfwonen: schuurwoningen, tiny houses en kleine woningen op het erf** (gelezen 2026-10-05):
- Het **9e Verzamelplan Buitengebied** (Chw-bestemmingsplan) is vastgesteld (Gmb 2025, 259478; ter inzage 18-6 t/m 30-7-2025; plan-ID NL.IMRO.0148.9eVerzamelplanBG-vs01). Het neemt 22 verleende projectafwijkingsbesluiten, 19 herzieningen en 5 wijzigingsplannen op. Het ontwerp lag ter inzage van 30-12-2023 t/m 9-2-2024 (Gmb 2023, 559954).
- Tegelijk zijn drie **beeldkwaliteitsplannen "Erfwonen Dalfsen"** vastgesteld (Het Oversticht; aanvulling op de welstandsnota), die plannen voor schuurwoningen, tiny houses en kleine woningen toetsen.
- **Schuurwoningen** (BKP december 2022): bestaande schuur transformeren of een nieuwe schuurwoning toevoegen, binnen Sloop voor kansen of rood-voor-rood; ervenconsulentenadvies vooraf. Bestemmingsplanregels: maximaal 750 m³ per woning, geen apart bijgebouw of carport, goothoogte maximaal 4,5 m, bouwhoogte maximaal 10 m, dakhelling 40-60°. **"Bij een wijziging op het bestemmingsplan om (een) schuurwoning(en) mogelijk te maken is sprake van maatwerk (inhoud, aantal woningen, goot- en nokhoogte, etc.)."**
- **Tiny houses:** maximaal 1 per erf, maximaal 50 m² incl. berging. **Kleine woningen:** maximaal 1 per erf, bijgebouw maximaal 50 m² (BKP versie 2-6-2025).
- **Relevantie [I]:** het BKP geeft het vormkader (schuurachtige gebouwen met meerdere woningen) waarmee De Tuindershof 11 kleinere woningen in twee schuurwoningen onderbracht. Het aantal woningen per schuurwoning is maatwerk, niet begrensd.
''')

d.sub('- **Kanttekening:** het raadsvoorstel De Tuindershof (2026) past op die locatie de grens "meer dan 11" toe. Of die locatie in bijlage 1 als "direct aangrenzend aan bestaand bebouwd gebied" is aangemerkt, is niet nagegaan (kaart niet geraadpleegd).',
'- **Bijlage 1 (kaart, gelezen 2026-10-05):** de kaart (datum 5-1-2022, schaal 1:80.000) toont per kern (Dalfsen, Lemelerveld, Nieuwleusen, Oudleusen, Hoonhorst) een compacte contour "bestaand bebouwd gebied" met een kleiner "centrumgebied"; al het overige is "buitengebied". Wat "direct aangrenzend" betekent is op de kaart niet gedefinieerd [I]. Het raadsvoorstel De Tuindershof (Ankummer Es, ten noorden van de kern Dalfsen) past de categorie "bebouwd gebied" toe (bindend advies bij **meer dan 11** woningen, 17 woningen): de gemeente rekent die locatie dus tot "in of direct aangrenzend aan bestaand bebouwd gebied". Voor een locatie op afstand van een kern geldt de buitengebiedgrens van meer dan 3 woningen.')

d.sub('\n---\n\n## 4. VAB-beleid',
'''
### 3.7 Gebiedskenmerken en overlays (kaartlagen, berekend 2026-10-05)
**Methode:** WFS-lagen van de Provincie Overijssel (services.geodataoverijssel.nl) doorsneden met de gemeentegrens van Dalfsen (PDOK/CBS gebiedsindelingen 2024, gegeneraliseerd; 166,5 km² land en water). Adrespunten zijn geocodeerd via de PDOK-Locatieserver.
**Let op:** de nieuwe provinciale **landbouwgebied-typologie** (art. 4.123, sinds 1-7-2026) staat niet in deze WFS. Als benadering voor "landbouwgebied met gebiedsspecifieke opgaven" is de **voormalige zone Ondernemen met Natuur en Water (ONW)** gebruikt; die vormt volgens `provincie_overijssel.md` §1.4 "grotendeels" dat type. Het is dus een indicatie, geen vaststelling.

| Laag | Oppervlak binnen Dalfsen | Aandeel van de gemeente |
|---|---|---|
| Voormalige ONW-zone (proxy gebiedsspecifiek landbouwgebied) | 9,2 km² | 5,5% |
| Natuurnetwerk Nederland (NNN) | 28,6 km² | 17,2% |
| Natura 2000 | 0 km² (Vecht- en Beneden-Reggegebied op 7 m, Uiterwaarden Zwarte Water en Vecht op 41 m van de grens) | 0% |
| Grondwaterbeschermingsgebied | 3,3 km² | 2,0% |
| Waterwingebied | 0,4 km² | 0,2% |
| Essen (provinciale laag) | 14,9 km² | 9,0% |
| Archeologische essen | 14,6 km² | 8,7% |
| Landgoederen (vlakken) | 32,7 km² | 19,6% |

[I] Voor het agrarische buitengebied buiten ONW, NNN en landgoederen ligt de generieke typologie ("landbouwgebied met generieke opgaven en kansen") het meest voor de hand. Dat is nog te toetsen op de definitieve provinciale kaartlaag.

**Ligging van de projectlocaties** (afstand tot de rand van de laag, in meters; "binnen" = in de laag):

| Locatie | Essen | Landgoed | NNN / ONW | Grondwaterbescherming | Natura 2000 |
|---|---|---|---|---|---|
| De Tuindershof (Ankummer Es 11) | binnen | 95 | 758 | 1.136 | 3.859 |
| Vosserburen (Vossersteeg 74) | 325 | binnen | 527 | 630 | 3.013 |
| Het Engelland (Engellandweg) | 346 | 523 | 1.563 / 1.906 | 2.475 | 5.000 |
| Waterinkweg, Lemelerveld | 1.831 | 2.585 | 1.246 | 10.936 | 2.615 |
| Oosterdalfsen Noord | binnen | 300 | 761 | 3.860 | 6.649 |

Controle: de plantoelichting Het Engelland noemt 4,5 km tot het dichtstbijzijnde stikstofgevoelige Natura 2000-gebied en NNN op 1,5 km; de zoekresultaten over de Waterinkweg melden 2,5 km tot het Vecht- en Beneden-Reggegebied. Beide komen overeen met de berekening (planrand tegenover adrespunt).

---

## 4. VAB-beleid''')

# §5 sleutelprojecten
d.line_replace('> **Tegenstrijdige bevinding (sleutelprojecten Woondeal).**',
'''> **Opgeloste tegenstrijdigheid (sleutelprojecten Woondeal).** Bijlage 1 van de Actualisatie Woondeal West-Overijssel (20-3-2025; gelezen 2026-10-05) noemt voor Dalfsen:
>
> | Sleutelproject | Woondeal 2022 | 2024-2030 (na actualisatie) | Doorkijk na 2030 |
> |---|---|---|---|
> | Nieuwleusen Centrum | bestaand 250 | 250 | 35 |
> | Oosterdalfsen Noord | bestaand 340 | 400 | 70 |
> | Lemelerveld Waterinkweg | bestaand 170 | 206 | 50 |
> | Hoonhorst De Koele II | nieuw | 83 | - |
> | Dalfsen Het Engelland | nieuw | 100 | 400 |
> | Nieuwleusen Palthelanden | nieuw (niet meegeteld: volledig na 2030) | - | 600 |
> | **Totaal** | 760 | **1.039** | **1.155** |
>
> Het VHP (oktober 2024) telde nog vier projecten met 840-880 woningen (inclusief "Dalfsen Centrum 80", peildatum 2021) en is dus gebaseerd op de Woondeal 2022. Het provinciebestand (§1.5) volgt de actualisatie. De gemeente stemde in met de Woondeal 2022 op 21-12-2022; het college besloot over de Actualisatie op 1-4-2025 en de raad nam er op 19-5-2025 kennis van (raadsmemo). Het VHP is volgens dat memo op 2-12-2024 door de raad vastgesteld.''')

d.sub('- **Plancapaciteit (VHP bijlage II, peildatum 1-1-2024):**','- **Plancapaciteit (VHP bijlage II, peildatum 1-1-2024; bevestigd in de Woondeal-actualisatie 2025: 1.039 woningen sleutelprojecten):**')

# §6 De Tuindershof
d.line_replace('> **Opgeloste tegenstrijdigheid (De Tuindershof).**',
'''> **Opgeloste tegenstrijdigheid (De Tuindershof).** Aantal woningen: 19 (zoeksamenvatting raadscommissie 2023) versus 17 (raad 2026). De KGO-notitie van 14-2-2023 telt 18 woningen (15 op het erf Stel, 2 Van Keulen, 1 Jansen); het raadsvoorstel 2026 telt 17 (11 daarvan in twee schuurwoningen); het VHP (peildatum 1-1-2024) telde 15. Het plan is tussen 2023 en 2026 gewijzigd; 17 is de actuele stand.

**Toelichting De Tuindershof** (KGO-onderbouwing 14-2-2023, Bureau voor Planvorming Advies; ruimtelijke onderbouwing; raadsvoorstel nr. 2064):
- **Ontstaan:** de eigenaar van tuinderij Stel (Ankummer Es 11) stopte; er was geen bedrijfsopvolging. Het eerste plan was sloop van de opstallen en 5 vrijstaande woningen. De gemeente vroeg de overige ondernemers (Van Keulen, Jansen) mee te doen en het landschap in één keer te herstellen, en vroeg op het erf Stel meer en kleinere eenheden voor starters en senioren (15 in plaats van 5).
- **Rekensom (raadsvoorstel):** kassen tellen voor 60% mee in plaats van 20% (vanwege de asbesthoudende kit en dus hogere sloopkosten); 1.000 m² sloop per woonvolume; resultaat 8 woonvolumes van 750 m³ (Stel 4,5; Van Keulen ruim 2,5; Jansen krap 1). De 17 woningen komen daarmee overeen met dit totaal doordat 11 kleinere woningen in twee "schuurwoningen" zijn ondergebracht. De kleinere eenheden brengen minder op; die maatschappelijke meerwaarde telt mee in de KGO-balans.
- **Investering (KGO-notitie 2023, excl. btw):** sloop kassen Stel € 103.750; sloop kassen Van Keulen en Jansen € 60.450; afwaardering grondwaarde € 182.044; beplanting € 25.000*; aanleg wegen en paden € 75.000; onderhoud wegen en paden 10 jaar € 25.000*; realisatie circulaire kas (bedrag niet ingevuld); onderhoud circulaire kas 10 jaar € 12.500* (*schatting). Opgeteld € 483.744, ongeveer € 28.500 per woning bij 17 woningen [I: eigen optelling].
- **Maatschappelijke bijdrage:** ommetjes en opengesteld groen (ook buiten het plangebied), educatie, streekwinkel en kas; de initiatiefnemer wil Dalfsenaren en doorstromers uit sociale huur voorrang geven bij verkoop.
- **Procedure en toetsing:**
  - buitenplanse omgevingsplanactiviteit (art. 5.1 lid 1 onder a Ow), met bindend raadsadvies bij de aanvraag (17 > 11);
  - de provincie is "in overleg" betrokken en haar opmerkingen over de openheid van de es zijn verwerkt;
  - de ladder is volgens de ruimtelijke onderbouwing niet van toepassing: het plan "voorziet niet in het toestaan van extra bebouwingsmogelijkheden" (verplaatsing/vermindering van bebouwing, "Ruimte voor ruimte");
  - milieu: stikstof (AERIUS), flora en fauna, bodem, archeologie; een spuitvrije zone van 50 m volgens jurisprudentie bij gevoelige functies naast agrarische percelen;
  - straatnaambesluit "De Tuindershof" 15-7-2026 (Gmb 2026, 337369).
- **Plek in het landschap:** essenlandschap in het deelgebied Variatie rond de Vecht; kassen "op een es" zijn volgens de huidige kaders niet meer mogelijk; sloop herstelt een deel van de openheid van de es.

**Toelichting Vosserburen** (Gemeenteblad):
- Vossersteeg 74, aanvraag "het realiseren van 13 transformatiewoningen" (zaak Z/24/712762), ingekomen 29-12-2023 (Gmb 2024, 11999).
- **Route:** omgevingsvergunning in de uitgebreide procedure met een verklaring van geen bedenkingen van de raad. Ontwerpbesluit 6 weken ter inzage vanaf 30-10-2024 (Gmb 2024, 454253). Besluit van het college 20-12-2024, ter inzage 27-12-2024 t/m 6-2-2025, beroep bij de Rechtbank Overijssel (Gmb 2024, 541698). Plan-ID NL.IMRO.0148.OmBVosserstg74en76-vs01.
- **Doorlooptijd:** ongeveer 12 maanden tussen aanvraag en besluit. De duur van 20 jaar (tijdelijkheid) volgt uit nieuwsberichten, niet uit de publicatie.
- De locatie stond al in de VHP-plancapaciteit (Vossersteeg 74, De Ruimte: 12 woningen).
- In 2026 is blijkens Gemeenteblad-titels het milieudeel/de IPPC-vergunning (varkenshouderij) ingetrokken (Gmb 2026, 144738, 181677 en 290248) [I: betreft dit erf; de titels zijn afgekapt].

**Regionaal vergelijkingsvoorbeeld (niet Dalfsen):** het ontwerp Volkshuisvestingsprogramma Overijssel noemt **BuitenDelen in Lettele** (gemeente Deventer) als CPO-project op een voormalig agrarisch erf, met biobased woningbouw, collectieve voorzieningen en landschapsbeheer; "door gebruik te maken van verruimde provinciale en gemeentelijke kaders" een praktijkvoorbeeld voor "moderne rood-voor-rood ontwikkelingen" (zie `provincie_overijssel.md` §2.4 en §5). Het aantal woningen en de procedure zijn niet onderzocht; geschikt voor het Deventer-rapport.''')

d.save(); print('ok')
