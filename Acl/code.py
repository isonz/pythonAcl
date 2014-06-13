#!/usr/bin/env python
# coding: utf-8

from config.urls import urls
from mods.Sessions import Sessions
import web

app = web.application(urls, globals())
sess = Sessions()
session = sess.init(app)
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
