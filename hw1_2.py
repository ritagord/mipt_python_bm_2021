#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:13:24 2021

@author: rita
"""

alphabet = {x: y for x, y in zip(range(33), "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" )}
alphabet.update({-1: ' '})


string = input() 
words = []

while string != "End":
    num = int(string)
    
    words.append(alphabet[num])
    string = input()
    
print(*words)