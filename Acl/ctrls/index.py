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
        user = self.parent.auth()
        if user:
            data = {'error':'0','html':{"username":user['login']}}
            out = self.parent.json.dumps(data)
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
        captcha = None
        if 'username' in input:  login = input['username']
        if 'password' in input:  passwd = input['password']
        if 'captcha' in input:  captcha = input['captcha']
        session = self.parent.web.config._session

        if login is None or passwd is None or captcha is None: 
            out = {'error':'1', 'msg':'请填入用户名和密码'}
            return self.parent.json.dumps(out)
        
        if captcha.lower() != session.captcha.lower():
            out = {'error':'2', 'msg':'验证码不正确'}
            return self.parent.json.dumps(out)
        
        ip = self.parent.getIp()
        row = self.parent.Users.login(login, passwd, ip)
        
        if row: 
            session.user = {'login':login, 'site_id':row['site_id'], 'user_role_id':row['user_role_id'], 'last_login':row['last_login'], 'last_login_ip':row['last_login_ip']}
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
    
    
class Captcha(CBase):
    parent = None
    def __init__(self):
        self.parent = super(Captcha, self)
        return self.parent.__init__()
    
    def GET(self):
        session = self.parent.web.config._session
        self.parent.web.header('Content-Type', 'image/gif')
        captcha = self.parent.Captcha.set(70, 22, 16, 5, (102,102,102), (255,255,255), 'gif',(300,'#666666'))
        session.captcha = captcha[0]
        #print session.captcha
        return captcha[1].read()
    

if __name__ == "__main__":
    print Captcha().GET()
    
