#!/usr/bin/env python
# coding: utf-8

import web
import json

import os
import sys
root = os.path.abspath('..')
sys.path.append(root)
#print os.getcwd() 
from config import settings
from mods.Sessions import Sessions

class CBase(object):
    web = web
    json = json
    render = settings.render
    session = web.config.get('_session')

    def __init__(self):
        self.getSession()
        pass
    
    def getSession(self):
        if self.session is None:
            app = web.application('', globals())
            self.session = Sessions().init(app)
        return self.session
    
    def auth(self):
        if self.session.get('user') is None:
            return False
        else:
            return True
    
    def logout(self):
        return Sessions().kill()
        
        
