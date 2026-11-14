#!/bin/bash
cd /tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/src
for k in "$@"; do ../vns.sh "$k"; done | grep -E '^==|202[4-6] (Algemeen|Gemeente|Sport)' 
