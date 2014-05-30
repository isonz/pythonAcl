#!/usr/bin/env python
# coding: utf-8

import web

db = web.database(dbn='mysql', db='pythonacl', user='root', pw='admin888')

web.config.debug = True
render = web.template.render('templates/', cache=False)
web.template.Template.globals['render'] = render
