#!/usr/bin/env python
# coding: utf-8

import web

db = web.database(dbn='mysql', db='pythonacl', user='root', pw='admin888')

render = web.template.render('views/', cache=False)

web.config.debug = True
web.config.session_parameters['cookie_name'] = 'PHPSESSID'
#web.template.Template.globals['render'] = render
