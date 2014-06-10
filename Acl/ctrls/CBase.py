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

class CBase(object):
    web = web
    json = json
    render = settings.render

    def __init__(self):
        pass
    
    def auth(self):
        todos2 = self.db.select(tb, order='finished asc, id asc')
