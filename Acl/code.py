#!/usr/bin/env python
# coding: utf-8

import web
from config.urls import urls
from mods.Sessions import Sessions

app = web.application(urls, globals())
application = app.wsgifunc()

Sessions().init(app)

if __name__ == "__main__":
    app.run()
