#!/usr/bin/env python
# coding: utf-8

import time

class FUNC():
    def __init__(self):
        pass
    
    def getNow(self, Y=True, m=True, d=True, H=True, M=True, S=True):
        str = ''
        if Y: str += '%Y'
        if m: str += '-%m'
        if d: str += '-%d'
        if H: str += ' %H'
        if M: str += ':%M'
        if S: str += ':%S'
        return time.strftime(str,time.localtime(time.time()))
    
    def getDate(self):
        return self.getNow(H=False, M=False, S=False)
    
if __name__ == "__main__":
    print FUNC().getDate()