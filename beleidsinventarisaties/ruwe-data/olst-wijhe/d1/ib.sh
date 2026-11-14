#!/bin/bash
# ib.sh id name
cd /tmp/claude-1000/-home-nick-Claude-Hanzedorp/20e4dc6f-20bf-4570-b50d-60a8552277a5/scratchpad/d1
curl -s -L --max-time 120 -A "Mozilla/5.0" "https://api2.ibabs.biz/publicdownload.aspx?site=OlstWijhe&id=$1" -o "$2"
python3 ext.py "$2"
