# Hardenberg: DSO/RP-aanvullingsronde 2026-11-06

Model: Claude Sonnet 5.5 (claude-sonnet-5-5), effort high. Geen sleutels of bronbestanden.

## Commando's
- `python3 -I tools/dso.py pons gm0160` -> omgevingsplan v4 (2026-08-07); geen pons. `regelingen gm0160 [--ontwerp]`: "Programma voor Gemeente Hardenberg" = energieprogramma (`tekst /akn/nl/act/gm0160/2020/programma_energie_hardenberg43`).
- `rp-plannen 0160 --tam` (38 TAM-plannen), `rp-plannen 0160 --grep Stobbenhaar --alle`, `rp-tekst NL.IMRO.0160.0000BP00165-VG03` (Buitengebied Hardenberg 2014; art. 3.6.4/3.6.5 e.a.), `rp-tekst NL.IMRO.0160.0000TAM0035-VG01` (§11.2.3 zienswijzen).
- `vergunningen gm0160 --grep ...`; `tekst /akn/nl/act/pv23/2023/omgevingsverordening` (art. 4.9, 4.10; Bijlage VII = PDF).
- `python3 -I tools/ori.py search/get --org hardenberg`: RIB grondbeleid 20-10-2026.

## Bevindingen
1. Art. 3.6.4 g: "het aantal woningen mag niet meer bedragen dan het bestaande aantal bedrijfswoningen". Art. 3.6.5: een extra vrijstaande woning bij sloop >= 850 m2 landschapsontsierende gebouwen (cumuleren max. twee erven), ruimtelijk kwaliteitsplan. Zelfde in art. 4.6.6/7, 5.6.5/6.
2. TAM0035-VG01 (alleen Stobbenhaarweg 4; vastgesteld 2026-10-06, besluit 1217283): sloop 1.611 m2; bedrijfswoning -> reguliere woning + 2 vrijstaande compensatiewoningen (389 m2 extra sloopmeters). Hofje nr. 1 (max. 20 woningen) uit plan na zienswijzen; plan gesplitst.
3. Nota grondbeleid 2020-2024 "gedateerd"; actualisatie loopt (RIB 2026-10-20).
4. Bestuurlijke Opdracht Hardenberg Buitengebied: niet in RIS.
5. Niet gevonden: rangordelijst netcongestie (xlsx), stemuitslag motie Erven met kwaliteit, inhoud zienswijzen.
