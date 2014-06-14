#!/usr/bin/env python
# coding: utf-8

import os
import sys
root = os.path.abspath('..')
sys.path.append(root)
from libs.DB import DB

class MBase(object):
    
    db = None
    tb_prefix = None
    
    def __init__(self):
        ndb = DB()
        self.db = ndb._db
        self.tb_prefix = ndb.tb_prefix
    
    def getDb(self):
        return self.db
    
    def getTbPrefix(self):
        return self.tb_prefix
