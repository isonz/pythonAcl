#!/usr/bin/env python
# coding: utf-8

import hashlib
from MBase import MBase

class Users(MBase):
    
    _table = 'system_rbac_users'
    _parent = None
    _db = None
    
    def __init__(self):
        self._parent = super(Users, self)
        return self._parent.__init__()
    
    def login(self, login, pwd, ip):
        row = self.db().getRow(self.table(), {'login':login, 'status':'1'}, '*', 'login=$login AND status=$status')
        try:
            passwd = row['passwd']
            salt = row['salt']
            pwd = hashlib.md5(hashlib.md5(pwd).hexdigest()+salt).hexdigest()
            if passwd==pwd:
                last_login = self._parent.func.getNow()
                self.db().update(self.table(), {"last_login":last_login, "last_login_ip":ip}, 'login="'+login+'"')
                return row
            else:
                return False
        except:
            return None
        
        
    def db(self):
        if self._db is None:
            self._db = self._parent.db
        return self._db
    
    def table(self):
        return self._parent.tb_prefix+self._table

if __name__ == "__main__":
    user = Users()
    print user.login('ison','zhang')




