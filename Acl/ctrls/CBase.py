#!/usr/bin/env python
# coding: utf-8

import web
import json

#import os
#import sys
#root = os.path.abspath('..')
#sys.path.append(root)
#print os.getcwd() 
# from config import settings

class CBase(object):
    web = web
    json = json
    render = web.template.render('views/', cache=False)
    db = settings.db
    def __init__(self):
        #self.web.template.Template.globals['render'] = self.render
        self.web.config.debug = True
        self.web.config.session_parameters['cookie_name'] = 'PHPSESSID'
    
    def auth(self):
        todos2 = self.db.select(tb, order='finished asc, id asc')
