#!/usr/bin/env python
# coding: utf-8
import web

class CBase(object):
    "a base controller class"
     
    def __init__(self):
        pass
    
    def auth(self):
        return 1;