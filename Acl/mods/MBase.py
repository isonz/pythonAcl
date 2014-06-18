#!/usr/bin/env python
# coding: utf-8

import os
import sys
root = os.path.abspath('..')
sys.path.append(root)
from libs.DBS import DBS
from libs.FUNC import FUNC

class MBase(object):
    
    db = DBS()
    _db = DBS()._db
    tb_prefix = DBS().tb_prefix
    
    func = FUNC()
    
    def __init__(self):
        pass
    

