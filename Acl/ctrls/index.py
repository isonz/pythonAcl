#!/usr/bin/env python
# coding: utf-8

from CBase import CBase

class Index(CBase):
    
    parent = None
    
    def __init__(self):
        self.parent = super(Index, self)
        return self.parent.__init__()
        
    def GET(self):
#        return self.parent.auth()
#
#       todos1 = db.select(tb, order='finished asc, id asc')
#       todos2 = db.select(tb, order='finished asc, id asc')

        #print self.parent.getSession()
        #print self.parent.logout()
        #print self.parent.auth()
        
        li = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
        enjson = self.parent.json.dumps(li)
        i = self.parent.web.input()
        if 'callback' in i:  enjson = i['callback']+'('+enjson+')'
        self.parent.web.header('Content-Type', 'application/json')
        return enjson;
        #return self.parent.render.index('11', '222')

if __name__ == "__main__":
    print Index().GET()
    
