#!/usr/bin/env python
# coding: utf-8

from MBase import MBase

class Sessions(MBase):
    
    _table = 'system_rbac_sessions'
    _parent = None
    
    def __init__(self):
        self._parent = super(Sessions, self)
        return self._parent.__init__()

    def init(self, app):
        store = self._parent.web.session.DBStore(self._parent.getDb(), self._parent.getTbPrefix()+self._table)
        return self._parent.web.session.Session(app, store, initializer={'count': 0})
        

if __name__ == "__main__":
    pass