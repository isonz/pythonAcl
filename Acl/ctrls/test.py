#!/usr/bin/env python
# coding: utf-8

import web
web.config.debug = True

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        i = web.input(name=None)
        return self.parent.render.index('11', '222')

if __name__ == "__main__":
    print Index().GET()
    
