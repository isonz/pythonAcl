#!/usr/bin/env python
# coding: utf-8

from CBase import CBase

class Index(CBase):
    
    parent = None
    
    def __init__(self):
        self.parent = super(Index, self)
        return self.parent.__init__()
        
    def GET(self):
        self.parent.web.header('Content-Type', 'application/json')
        input = self.parent.web.input()
        if self.parent.auth():
            li = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
            li = {'error':'0','html':li}
            out = self.parent.json.dumps(li)
            if 'callback' in input:  out = input['callback']+'('+out+')'
            return out;
        else:
            html = self.parent.render.index()
            out = {'error':'1','html':str(html)}
            out = self.parent.json.dumps(out)
            if 'callback' in input:  out = input['callback']+'('+out+')'
            return out

    def POST(self):
        self.parent.web.header('Content-Type', 'application/json')
        input = self.parent.web.input()
        login = None
        passwd = None
        if 'username' in input:  login = input['username']
        if 'password' in input:  passwd = input['password']

        if login is None or passwd is None: 
            out = {'error':'1', 'msg':'请填入用户名和密码'}
            return self.parent.json.dumps(out)
        
        row = self.parent.Users.login(login, passwd)
        
        if row: 
            session = self.parent.web.config._session
            session.user = {
                            'login':login, 'site_id':row['site_id'], 
                            'user_role_id':row['user_role_id'], 
                            'last_login':row['last_login'], 
                            'last_login_ip':row['last_login_ip']
                            }
            out = {'error':'0', 'msg':'登入成功'}
            return self.parent.json.dumps(out)
        else:
            out = {'error':'1', 'msg':'用户名或密码不正确'}
            return self.parent.json.dumps(out)


class Crossdomain(CBase):
    parent = None
    def __init__(self):
        self.parent = super(Crossdomain, self)
        return self.parent.__init__()
    
    def GET(self):
        f = open(self.parent.root+'/Acl/crossdomain.xml','r')
        xml = f.read()
        f.close()
        self.parent.web.header('Content-Type', 'application/xml')
        return xml
    
    
    

if __name__ == "__main__":
    print Index().GET()
    
