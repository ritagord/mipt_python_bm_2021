#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 12:18:45 2021

@author: rita
"""

def author(_author):
    def inner(function):
        function.author = _author
        return function
    return inner

@author("Dany Longo")
def add2(num: int) -> int:
    return (num+2)

print(add2.author)