#!/usr/bin/env python
# coding: utf-8

import web

db = web.database(dbn='mysql', host='', port='', db='pythonacl', user='root', pw='admin888')
tb_prefix = ''

render = web.template.render('views/', cache=False)

web.config.debug = False
web.config.session_parameters['cookie_name'] = 'PHPSESSID'
#web.template.Template.globals['render'] = render
