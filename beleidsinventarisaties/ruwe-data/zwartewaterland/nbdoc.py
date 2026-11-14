import requests, sys, os, pdfplumber, io, json
os.chdir('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/34361c4d-784d-4fc5-9800-df53eb03a520/scratchpad/zwartewaterland/raw')
H={'User-Agent':'Mozilla/5.0 Chrome/124'}
def fetch(i):
    fn=f'docs/{i}.pdf'
    if not os.path.exists(fn):
        m=requests.get(f'https://api.notubiz.nl/document/{i}',params={'format':'json','version':'1.17.0'},headers=H,timeout=60).json()['document']
        ver=m.get('version',1)
        r=requests.get(f'https://api.notubiz.nl/document/{i}/{ver}',headers=H,timeout=180)
        open(fn,'wb').write(r.content)
    tf=f'docs/{i}.txt'
    if not os.path.exists(tf):
        try:
            with pdfplumber.open(fn) as pdf:
                out=[f'\n=====PAGE {k+1}=====\n'+(p.extract_text() or '') for k,p in enumerate(pdf.pages)]
            open(tf,'w').write(''.join(out))
        except Exception as e:
            open(tf,'w').write('ERR '+str(e))
    return tf
if __name__=='__main__':
    for i in sys.argv[1:]:
        tf=fetch(int(i)); print(tf, os.path.getsize(tf))
