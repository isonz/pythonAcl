#!/usr/bin/env python
# coding: utf-8

import web
import hashlib
from MBase import MBase

class Users(MBase):
    
    _table = 'system_rbac_users'
    _parent = None
    _db = None
    
    def __init__(self):
        self._parent = super(Users, self)
        return self._parent.__init__()
    
    def db(self):
        self._db = self._parent.getDb()
        return self._db
    
    def login(self, login, pwd):
        row = self.db().getRow(self.table(), {'login':login, 'status':'1'}, '*', 'login=$login AND status=$status')
        try:
            passwd = row['passwd']
            salt = row['salt']
            pwd = hashlib.md5(hashlib.md5(pwd).hexdigest()+salt).hexdigest()
            if passwd==pwd:
                session = web.config._session
                session.user = {'login':login, 'site_id':row['site_id'], 'user_role_id':row['user_role_id'], 'last_login':row['last_login'], 'last_login_ip':row['last_login_ip']}
                return True
            else:
                return False
        except:
            return False
        
        
    
    def table(self):
        return self._parent.getTbPrefix()+self._table

if __name__ == "__main__":
    pass
    #MBase.login('ison','zhang')