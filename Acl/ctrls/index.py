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

        todos1 = '111'
        todos2 = '222'
        return self.parent.render.index(todos1, todos2)

if __name__ == "__main__":
    print Index().GET()
