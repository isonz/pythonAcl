from CBase import CBase

class Index(CBase):
    def __init__(self):
        pass
    def GET(self):
       return super(Index, self).auth()
#
#        todos1 = db.select(tb, order='finished asc, id asc')
 #       todos2 = db.select(tb, order='finished asc, id asc')
#
 #       return render.index(todos1,todos2)

if __name__ == "__main__":
    print Index().GET()
