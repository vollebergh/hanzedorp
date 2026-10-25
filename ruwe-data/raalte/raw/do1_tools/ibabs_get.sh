#!/bin/bash
# usage: ibabs_get.sh name documentId agendaItemId
D=/home/nick/.local/share/hanzedorp-raalte/raw/do1/ris
UA="Mozilla/5.0 (X11; Linux x86_64) Chrome/130.0"
n=$1; f="$D/$n.pdf"
[ -s "$f" ] || curl -s -A "$UA" -m 300 "https://raalte.bestuurlijkeinformatie.nl/Document/LoadAgendaItemDocument/$2?agendaItemId=$3" -o "$f"
file -b "$f" | cut -c1-40
python3 -I /home/nick/.local/share/hanzedorp-raalte/raw/do1_tools/pdf2txt.py "$f"
