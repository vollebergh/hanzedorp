import sys,subprocess
from bs4 import BeautifulSoup
UA=open('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/ua.txt').read().strip()
for cid in sys.argv[1:]:
    url=f"https://lokaleregelgeving.overheid.nl/{cid}"
    h=subprocess.run(['curl','-sL','-A',UA,'--max-time','60',url],capture_output=True).stdout.decode('utf8','replace')
    s=BeautifulSoup(h,'html.parser')
    for t in s(['script','style']): t.decompose()
    txt=s.get_text('\n',strip=True)
    i=txt.find('Regeling tekst')
    open(f"/tmp/claude-1000/-home-nick-Claude-Hanzedorp/89226ac6-9e27-452b-898b-8505799276fa/scratchpad/voorst/d1/cvdr/{cid.replace('/','_')}.txt",'w').write(txt)
    print(cid,len(txt))
