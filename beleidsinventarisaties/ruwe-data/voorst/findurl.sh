#!/bin/bash
# usage: findurl.sh pattern  (greps urls in vn_multi*.txt)
grep -h -i -E "$1" /tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/vn_multi*.txt | awk -F' [|] ' '{print $1}' | sort -u
