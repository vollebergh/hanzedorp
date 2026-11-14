import json,sys
d=json.load(open('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/d1/ov/ontwerp_pages.json'))
for part in sys.argv[1].split(','):
    if '-' in part: a,b=map(int,part.split('-')); r=range(a,b+1)
    else: r=[int(part)]
    for n in r: print(f'######## PAGE {n}\n{d[str(n)]}')
