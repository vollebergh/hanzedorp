#!/bin/bash
D=$(dirname "$0"); /home/nick/.venv/bin/python3 -I $D/page2.py "$1" > $D/web/$2.txt 2>&1; wc -c $D/web/$2.txt
