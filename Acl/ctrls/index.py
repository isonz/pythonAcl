from CBase import CBase

class Index(CBase):
<<<<<<< HEAD
    
    def GET(self):
        print 'ffffffffffff'
#        print CBase.auth(self)
=======
    def __init__(self):
        pass
    def GET(self):
       return super(Index, self).auth()
>>>>>>> f8b2740c59d67dd25a9e7c76ff6bc4b2fba0b0ef
#
#        todos1 = db.select(tb, order='finished asc, id asc')
 #       todos2 = db.select(tb, order='finished asc, id asc')
#
 #       return render.index(todos1,todos2)

if __name__ == "__main__":
    print Index().GET()
