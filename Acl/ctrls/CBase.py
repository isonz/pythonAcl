#!/usr/bin/env python
# coding: utf-8

import sys
import os
root = os.path.abspath('..')
sys.path.append(root)
#print os.getcwd() 

from config import settings

class CBase(object):
    render =  settings.render
    db = settings.db
    def __init__(self):
        pass
    
    def auth(self):
        return 'dddddddddd';
