#!/usr/bin/env python
# coding: utf-8

from CBase import CBase
import web
import json

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
        
        li = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
        enjson = json.dumps(li)
        i = web.input()
        enjson = i['callback']+'('+enjson+')'
        web.header('Content-Type', 'application/json')
        return enjson;
        #return self.parent.render.index('11', '222')

if __name__ == "__main__":
    print Index().GET()
