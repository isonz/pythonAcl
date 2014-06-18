#!/usr/bin/env python
# coding: utf-8

from CBase import CBase

class Index(CBase):
    
    parent = None
    
    def __init__(self):
        self.parent = super(Index, self)
        return self.parent.__init__()
        
    def GET(self):
        self.parent.web.header('Content-Type', 'application/json')
        input = self.parent.web.input()
        user = self.parent.auth()
        if user:
            html = self.parent.render.user(user)
            out = {'error':'0','html':str(html)}
            out = self.parent.json.dumps(out)
            if 'callback' in input:  out = input['callback']+'('+out+')'
            if 'logout' in input:
                if self.parent.logout():
                    return self.parent.json.dumps({'error':'0'})
            return out;
        else:
            out = {'error':'1','html':'不正确'}
            out = self.parent.json.dumps(out)
            if 'callback' in input:  out = input['callback']+'('+out+')'
            return out

    def POST(self):
        self.parent.web.header('Content-Type', 'application/json')
        input = self.parent.web.input()
        
        out = {'error':'1', 'msg':'不正确'}
        return self.parent.json.dumps(out)

    
    

if __name__ == "__main__":
    print Index().GET()
    
