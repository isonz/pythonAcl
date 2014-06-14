#!/usr/bin/env python
# coding: utf-8

import web

db = web.database(dbn='mysql', host='', port='', db='pythonacl', user='root', pw='admin888')
tb_prefix = ''

render = web.template.render('views/', cache=False)

web.config.debug = False
web.config.session_parameters['cookie_name'] = 'PHPSESSID'
web.config.session_parameters['timeout'] = 600 
#web.config.session_parameters['cookie_domain'] = None
#web.config.session_parameters['ignore_change_ip'] = True
#web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
#web.config.session_parameters['expired_message'] = 'Session expired'
#web.config.session_parameters['ignore_expiry'] = True

#web.template.Template.globals['render'] = render
