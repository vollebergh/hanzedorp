import sys; sys.path.insert(0,'.')
from lib import Doc
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/8c2cda72-f653-4a4b-aefb-12cf46016d6b/scratchpad/wt-dalfsen/gemeente_dalfsen.md'
d=Doc(W)
print([l[:90] for l in d.t.split('\n')[142:152]])

d.line_replace('- **Raadsbesluit 27-11-2023 "Strategische keuzes Dalfsen West/Noord"**',
'''- **Raadsvoorstel "Strategische keuzes Dalfsen West/Noord"** (college 17-10-2023, nr. 1668; raad 27-11-2023; gelezen 2026-10-05, https://ris.dalfsen.nl/Vergaderingen/Gemeenteraad/2023/27-november/15-Strategische-keuzes-Dalfsen-West-Noord-RVS.pdf):
  - voorstel: **Dalfsen-Noord** (ca. 35 ha; ca. 566 woningen bij 45% uitgeefbaar) aanwijzen als volgende woningbouwlocatie voor de kern Dalfsen; voor **Dalfsen-West** (ca. 15 ha; ca. 213 woningen bij 40%) geen actieve grondpolitiek maar faciliteren ("uitnodigingsplanologie") met het landschappelijk karakter als toetsingscriterium; verwerken in Omgevingsvisie 2.0; grondverwerving Dalfsen-Noord uiterlijk 1-2-2025;
  - **provincie:** na gesprekken met de provincie bleek dat Dalfsen-West "op een es" ligt, nabij Ankum; "De provincie heeft aangegeven dat ontwikkelingen in Dalfsen-West moeten plaatsvinden binnen de aanwezige landschappelijke waarden", wat een uitbreidingswijk van ca. 300 woningen belemmert; de raad bevestigde dat standpunt in een motie;
  - voorkeursrecht (Wvg): Dalfsen-West vervalt 15-2-2024, Dalfsen-Noord 28-2-2025, geen verlenging meer mogelijk;
  - de raadsbehandeling zelf staat niet in dit stuk; nieuwsberichten melden dat de raad Dalfsen-Noord koos [Z].
  - **Dalfsen-Noord is dezelfde locatie als Het Engelland** (hieronder): plantoelichting Het Engelland noemt een gebied van ca. 35 ha, begrensd door Leemculeweg, Engellandweg, Koesteeg en Vossersteeg, en verwijst naar het raadsbesluit om "Dalfsen Noord als toekomstige nieuwbouwlocatie te kiezen". Het concept telde beide als aparte locaties.''')

d.line_replace('> 9. "Voorkeursrecht Het Engelland',
'> 9. "Voorkeursrecht Het Engelland afgelopen 28-2-2025" is niet bevestigd: het voorkeursrecht (gevestigd 2021) gold volgens de plantoelichting tot 28-2-2025, en het wijzigingsbesluit Het Engelland (3-2-2025) schept "voldoende grondslag voor verlenging". Of het is verlengd, is niet gevonden (§2.1).')
d.insert_after_line('> 15. **Het provinciale Volkshuisvestingsprogramma**',
'> 16. **Het Engelland en Dalfsen-Noord zijn dezelfde locatie** (ca. 35 ha; §2.1). Het concept telde ze in §5 als twee locaties; de rij Dalfsen-Noord is vervallen.')

d.line_replace('| Het Engelland / Vosserlanden |',
'| Het Engelland (= Dalfsen-Noord, ca. 35 ha; eerste deelplan Vosserlanden) | ca. 100 in Vosserlanden; op termijn ca. 600 (raadsvoorstel 2023: ca. 566) | Wijzigingsbesluit 3-2-2025; Vosserlanden: stedenbouwkundig plan raad 24-11-2025, verkoop tweede helft 2026, bouw medio 2027 (de in 2023 genoemde uitgifte "in 2033" is daarmee ingehaald) | Niet gevonden |')
d.line_replace('| Dalfsen-Noord | >500 [Z] |','')
# drop the now empty line from table (it leaves an empty line inside the table) 
d.t=d.t.replace('| Het Engelland (= Dalfsen-Noord','| Het Engelland (= Dalfsen-Noord')
d.save()
