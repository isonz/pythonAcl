#!/usr/bin/env python
# coding: utf-8

import os
import sys
root = os.path.abspath('..')
sys.path.append(root)
from config import settings

class DB(object):
    __db = settings.db

    def __init__(self):
        pass
    
    def insert(self, tb, data):
        if tb is None: return False
        if type(data) is not dict or data is None: return False
        self.__db.insert(tb, 'session_id=qqqq', data)
        #self.__db.update(tb, 'session_id="qqqq"', data)
    
if __name__ == "__main__":
    db = DB()
    print db.insert('system_rbac_sessions', {'session_id':'qqqq','data':'{"a":"aa","b","bb"}'})
    #print db.insert('system_rbac_sessions', {'data':'{"a":"aaaaca","b","bbbcb"}'})
