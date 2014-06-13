#!/usr/bin/env python
# coding: utf-8

import web
from MBase import MBase

class Sessions(MBase):
    
    _table = 'system_rbac_sessions'
    _parent = None
    
    def __init__(self):
        self._parent = super(Sessions, self)
        return self._parent.__init__()

    def init(self, app):        
        if web.config.get('_session') is None:
            store = web.session.DBStore(self._parent.getDb(), self._parent.getTbPrefix()+self._table)
            session = web.session.Session(app, store, initializer={'count': 0})
            web.config._session = session
        else:
            session = web.config._session
        return session
      
    def kill(self):
        web.config._session.kill()
        return ""

if __name__ == "__main__":
    pass
