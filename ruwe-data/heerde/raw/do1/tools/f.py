import sys,re,html,subprocess,urllib.parse
ua=open('/tmp/claude-1000/-home-nick-Claude-Hanzedorp/a92d4061-9456-4112-b4e0-c17a95facee8/scratchpad/heerde/raw/do1/ua.txt').read().strip()
def fetch(u,raw=False):
    r=subprocess.run(['curl','-sL','--max-time','60','-A',ua,u],capture_output=True)
    return r.stdout.decode('utf8','ignore')
def text(t):
    t=re.sub(r'(?is)<(script|style|noscript)[^>]*>.*?</\1>','',t)
    t=re.sub(r'(?i)<br\s*/?>|</(p|div|li|h\d|tr|table|section)>','\n',t)
    t=re.sub(r'<[^>]+>','',t)
    t=html.unescape(t)
    t=re.sub(r'[ \t\r\f]+',' ',t)
    t=re.sub(r'\n\s*\n+','\n\n',t)
    return t.strip()
if __name__=='__main__':
    u=sys.argv[1]
    t=fetch(u)
    if len(sys.argv)>2 and sys.argv[2]=='links':
        for l in sorted(set(re.findall(r'href="([^"#]+)"',t))): print(l)
    elif len(sys.argv)>2 and sys.argv[2]=='raw': print(t)
    else:
        x=text(t)
        i=x.find('\n Home\n')
        if i>0: x=x[i:]
        j=x.find('Neem contact op')
        if j>0: x=x[:j]
        print(re.sub(r'\n\s*\n','\n',x))
