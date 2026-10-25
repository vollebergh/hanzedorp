import re
class Doc:
    def __init__(self,path):
        self.path=path; self.t=open(path,encoding='utf-8').read()
    def save(self): open(self.path,'w',encoding='utf-8').write(self.t)
    def sub(self,old,new,count=1):
        n=self.t.count(old)
        assert n==count, f"expected {count} got {n} for: {old[:80]!r}"
        self.t=self.t.replace(old,new)
    def line_replace(self,prefix,new,count=1):
        lines=self.t.split('\n'); idx=[i for i,l in enumerate(lines) if l.startswith(prefix)]
        assert len(idx)==count, f"prefix {prefix[:60]!r}: {len(idx)} matches"
        for i in idx: lines[i]=new
        self.t='\n'.join(lines)
    def insert_after_line(self,prefix,text):
        lines=self.t.split('\n'); idx=[i for i,l in enumerate(lines) if l.startswith(prefix)]
        assert len(idx)==1, f"prefix {prefix[:60]!r}: {len(idx)} matches"
        lines[idx[0]+1:idx[0]+1]=text.split('\n'); self.t='\n'.join(lines)
    def insert_before_line(self,prefix,text):
        lines=self.t.split('\n'); idx=[i for i,l in enumerate(lines) if l.startswith(prefix)]
        assert len(idx)==1, f"prefix {prefix[:60]!r}: {len(idx)} matches"
        lines[idx[0]:idx[0]]=text.split('\n'); self.t='\n'.join(lines)
    def replace_section(self,start_prefix,end_prefix,new):
        lines=self.t.split('\n')
        s=[i for i,l in enumerate(lines) if l.startswith(start_prefix)]; e=[i for i,l in enumerate(lines) if l.startswith(end_prefix)]
        assert len(s)==1 and len(e)==1, (start_prefix,len(s),end_prefix,len(e))
        assert s[0]<e[0]
        lines[s[0]:e[0]]=new.split('\n'); self.t='\n'.join(lines)
