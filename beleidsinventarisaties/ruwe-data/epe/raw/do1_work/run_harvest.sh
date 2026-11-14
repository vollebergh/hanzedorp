#!/bin/bash
W=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/cbd7d9f0-97a4-45cc-923f-0df0e26b9a22/scratchpad/epe/raw/do1_work
export ORI_CACHE=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/cbd7d9f0-97a4-45cc-923f-0df0e26b9a22/scratchpad/epe/raw/do1_work/ori
cd /home/nick/Claude/Hanzedorp
python3 -I tools/ori.py --rate 50 harvest epe --naam 'buitengebied|functieverand|rood voor|ruimte voor ruimte|VAB|woonagenda|woonvisie|woondeal|volkshuis|stikstof|slath|zuukerenk|kerkenland|kopermolen|TOP |omgevingsplan|omgevingsvisie|collectie|cpo|zelfbouw|kavel|starters|ouderen|woonzorg|plancapaciteit|hogeland|anterieur|grondprijs|grondbeleid|erfpacht|toekomstplan|woonbehoefte|woningbehoefte|splitsing|beleidsregel|beleidskader|afwegingskader|herbestemming|woningbouw|wonen|recreatie|mantelzorg|landgoed|boerderij|agrarisch|erf|sloop|ladder|coalitie|legesverordening|huisvesting|netcongestie|woning' --sinds 2019-01-01 > $W/harvest1.log 2>&1
python3 -I tools/ori.py --rate 50 harvest epe --klasse 'Besluit|Beslisnota|Voorstel|Raadsvoorstel|Raadsinformatienota|Motie|Amendement|Antwoord|Vraag|Notulen|Notitie|Schriftelijke|Toezeggingen|Raaadsvoorstel' --sinds 2022-01-01 > $W/harvest2.log 2>&1
echo klaar > $W/harvest_done
