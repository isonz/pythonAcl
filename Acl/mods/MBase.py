#!/usr/bin/env python
# coding: utf-8

import os
import sys
root = os.path.abspath('..')
sys.path.append(root)
from libs.DBS import DBS

class MBase(object):
    
    db = DBS()
    _db = DBS()._db
    tb_prefix = DBS().tb_prefix
    
    def __init__(self):
        pass
    

