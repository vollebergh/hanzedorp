import sys,json
sys.path.insert(0,'/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/scripts')
import sru
for q in sys.argv[1:]:
    try:
        o=sru.run(q)
    except Exception as e:
        print(q,'ERR',e); continue
    print('##',q,len(o))
    seen=set()
    for x in o:
        w=x['id'].split('_')[0]
        print(' ',x['id'],x['creator'],'|',x['title'][:100],'|',x['inw'],x['uitw'])
