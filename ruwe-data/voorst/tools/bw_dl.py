import re,subprocess,os,sys
UA=open('ua.txt').read().strip()
t=open('d1/pg/www_voorst_nl_bestuur_organisatie_college_van_bw_besluitenlijsten.txt').read().split('--- LINKS ---')[1]
links=[]
for l in t.split('\n'):
    m=re.search(r'\|\s*(/fileadmin/\S+\.pdf)',l)
    if m and re.search(r'/(2023)/',m.group(1)): links.append(m.group(1))
print(len(links))
import concurrent.futures as cf
def dl(p):
    name=os.path.basename(p)
    out=f'd1/bw/{name}'
    if os.path.exists(out+'.txt'): return
    subprocess.run(['curl','-sL','-A',UA,'--max-time','60','-o',out,'https://www.voorst.nl'+p])
    try:
        import pdfplumber
        with pdfplumber.open(out) as pdf:
            txt='\n'.join((pg.extract_text() or '') for pg in pdf.pages)
    except Exception as e:
        txt='ERR '+str(e)
    open(out+'.txt','w').write(txt)
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(dl,links))
