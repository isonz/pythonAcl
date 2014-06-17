#!/usr/bin/env python
# coding: utf-8

import os
import sys
root = os.path.abspath('..')
sys.path.append(root)
from config import settings

class DBS(object):
    _db = settings.db
    tb_prefix = settings.tb_prefix

    def __init__(self):
        pass
    
    def insert(self, tb, data, seqname=None, _test=False,):
        if type(data) is not dict: return False
        return self._db.insert(self.tb_prefix+tb, data, seqname, _test)
    
    def update(self, tb, data, where, vars=None, _test=False):
        if type(data) is not dict: return False
        return self._db.update(self.tb_prefix+tb, where, data, vars, _test)
        
    def select(self, tb, vars={}, what='*', where=None, order=None, group=None, limit=None, offset=None, _test=False): 
        return self._db.select(self.tb_prefix+tb, vars, what, where, order, group, limit, offset, _test)

    def delete(self, tb, where, using=None, vars=None, _test=False):
        return self._db.delete(self.tb_prefix+tb, where, using, vars, _test)
    
    def query(self, sql_query, vars=None, processed=False, _test=False): 
        return self._db.query(sql_query, vars, processed, _test)
    
    
    def getRow(self, tb, vars={}, what='*', where=None, group=None, _test=False):
        row = self.select(self.tb_prefix+tb, vars, what, where, None, group, 1, None, _test)
        if row :
            return row[0]
        return None
    
    
if __name__ == "__main__":
    db = DB()
    #print db.insert('system_rbac_sessions', {'session_id':'qqqq', 'data':'{"a":"aa","b","bb"}'})
    #print db.update('system_rbac_sessions', {'data':'{"a":"aaaaca","b","bbbcb"}'}, 'session_id="qqqq"')
    '''
    rows = db.select('system_rbac_sessions', {'session_id':'qqqq'}, '*', 'session_id=$session_id')
    for row in rows:
        print row['session_id']
    '''
    #print db.delete('system_rbac_sessions', 'session_id=$session_id',  vars={'session_id':'qqqq'})
    '''
    rows = db.query('select * from system_rbac_sessions where session_id=$session_id', {'session_id':'qqqq'})
    for row in rows:
        print row['session_id']
    ''' 
    '''
    row = db.getRow('system_rbac_sessions', {'session_id':'qqqq'}, '*', 'session_id=$session_id')
    print row['data']
    '''
    '''
    row = db.getRow('system_rbac_users', {'login':'ison', 'status':'1'}, '*', 'login=$login AND status=$status')
    print row['passwd']
    ''' 
    
