from CBase import CBase

class Index:
    
    def GET(self):
        print CBase.auth(self)
#
#        todos1 = db.select(tb, order='finished asc, id asc')
 #       todos2 = db.select(tb, order='finished asc, id asc')
#
 #       return render.index(todos1,todos2)


