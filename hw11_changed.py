#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:44:20 2021

@author: rita
"""
import re

output = []
with open('/home/rita/Downloads/Python2021/text_11.txt') as text:
    for line in text:
        output.append(re.findall('(?<=[\$€])\d+|\d+(?=\s₽)|\d+(?=₽)', line))
print(output)
