import subprocess,sys,os,re
W=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env=dict(os.environ,ORI_CACHE=W+"/ori_cache")
q=sys.argv[1]; df=sys.argv[2] if len(sys.argv)>2 else "2020-01-01"; lim=sys.argv[3] if len(sys.argv)>3 else "40"
r=subprocess.run(["python3","-I",W+"/tools/ori.py","search",q,"--org","harderwijk","--date-from",df,"--limit",lim,"--sort","date_desc"],capture_output=True,text=True,env=env,timeout=120)
txt=(r.stdout+"\n"+r.stderr).split("\n")
tot=[l for l in txt if l.startswith("totaal")]
print("## ",q,"|",tot[0] if tot else "")
for i,l in enumerate(txt):
    m=re.match(r'(\d{4}-\d\d-\d\d)\s+(\S+)\s+(\S+)',l)
    if m and i+1<len(txt):
        print(f"{m.group(1)} {m.group(2)[:3]} {m.group(3).split(':')[-1][:8]} | {txt[i+1].strip()[:150]}")
