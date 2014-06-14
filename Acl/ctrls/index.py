#!/usr/bin/env python
# coding: utf-8

from CBase import CBase

class Index(CBase):
    
    parent = None
    
    def __init__(self):
        self.parent = super(Index, self)
        return self.parent.__init__()
        
    def GET(self):
        input = self.parent.web.input()
        if self.parent.auth():
            li = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
            enjson = self.parent.json.dumps(li)
            if 'callback' in input:  enjson = input['callback']+'('+enjson+')'
            self.parent.web.header('Content-Type', 'application/json')
            return enjson;
        else:
            html = self.parent.render.index()
            out = {'error':'1','html':str(html)}
            out = self.parent.json.dumps(out)
            self.parent.web.header('Content-Type', 'application/json')
            if 'callback' in input:  out = input['callback']+'('+out+')'
            return out

    def POST(self):
        return 'login'



class Crossdomain(CBase):
    parent = None
    def __init__(self):
        self.parent = super(Crossdomain, self)
        return self.parent.__init__()
    
    def GET(self):
        f = open(self.parent.root+'/Acl/crossdomain.xml','r')
        xml = f.read()
        f.close()
        return xml
    
    
    

if __name__ == "__main__":
    print Index().GET()
    
