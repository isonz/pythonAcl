#!/usr/bin/env python
# coding: utf-8

from config.urls import urls
import web

app = web.application(urls, globals())
application = app.wsgifunc()

if __name__ == "__main__":
    app.run()
