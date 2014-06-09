#!/usr/bin/env python
# coding: utf-8

import web

class MBase:
    db = web.database(dbn='mysql', db='pythonacl', user='root', pw='admin888')
    
    def __init__(self):
        pass
    
    def login(self,login,passwd):
        print 'login'