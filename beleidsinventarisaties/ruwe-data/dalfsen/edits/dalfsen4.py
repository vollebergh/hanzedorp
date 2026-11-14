import sys; sys.path.insert(0,'.')
from lib import Doc
W='/tmp/claude-1000/-home-nick-Claude-Hanzedorp/8c2cda72-f653-4a4b-aefb-12cf46016d6b/scratchpad/wt-dalfsen/gemeente_dalfsen.md'
d=Doc(W)
d.sub('Woonupdate 005 (raadsmemo, 8-7-2025).','Woonupdate 005 (raadsmemo, 8-7-2025); raadsvoorstel "Strategische keuzes Dalfsen West/Noord" (17-10-2023); toelichting 9e Verzamelplan Buitengebied (commissie 19-5-2025, 70 p., globaal doorzocht).')
d.line_replace('| 10 | **9e Verzamelplan',
'| 10 | **9e Verzamelplan Buitengebied:** verzameling van afzonderlijke projectafwijkingsbesluiten, herzieningen en wijzigingsplannen (o.a. een schuurwoning aan de Koelmansstraat 73) | Commissie 19-5-2025; vastgesteld, ter inzage 18-6 t/m 30-7-2025 (Gmb 2025, 259478) | https://ris.dalfsen.nl/Vergaderingen/Raadscommissie/2025/19-mei/19:30/9e-Verzamelplan-Buitengebied/4-2-2-9e-Verzamelplan-Buitengebied-Toelichting.pdf (globaal doorzocht) | Laag-matig: individuele woningen per erf |')
d.sub('de toelichting van het 9e Verzamelplan zelf niet','de toelichting (70 p.) is alleen globaal doorzocht (verzameling van afzonderlijke projecten)')
d.sub('| 6 | Vosserburen: vergunning','| 6 | Vosserburen: vergunning') if False else None
d.save(); print('ok')
