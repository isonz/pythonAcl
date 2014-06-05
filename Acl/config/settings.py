#!/usr/bin/env python
# coding: utf-8

import web

db = web.database(dbn='mysql', db='pythonacl', user='root', pw='admin888')
render = web.template.render('../views/', cache=False)

#web.template.Template.globals['render'] = render
web.config.debug = True
