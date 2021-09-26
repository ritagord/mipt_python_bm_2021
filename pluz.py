#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 15:28:22 2021

@author: rita
"""


def pluz(a, b):

    try :
        pluz = a+b
        return(pluz)
    except TypeError:
        pluz = int(a) + int(b)
        return(pluz)

    
print(pluz(1, "2"))
print(pluz(1, 2))
print(pluz("1", "2"))
print(pluz("1", 2))
print(pluz([1], [2]))
