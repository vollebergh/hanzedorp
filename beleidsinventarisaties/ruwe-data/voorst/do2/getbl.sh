#!/bin/bash
y=$1; w=$2
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
o=/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/do2/raw/bl/bl_${y}_$w.pdf
code=$(curl -sL -A "$UA" -o $o -w "%{http_code}" "https://www.voorst.nl/fileadmin/user_upload/Bestuur__organisatie/Organisatie/Besluitenlijsten/$y/Besluitenlijst_${y}_week_$w.pdf")
echo "$y $w $code $(stat -c %s $o)"
