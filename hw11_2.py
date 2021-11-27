#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 18:11:23 2021

@author: rita
"""

import re

output = []
with open('/home/rita/Downloads/Python2021/text_11.txt') as text:
    for line in text:
        #output.append(re.findall('(?<=[\$€])\d+|\d+(?=\s₽)|\d+(?=₽)', line))
        output.append(re.findall('(?<=«)\w+ \w+(?=»)|(?<=«)\w+(?=»)|(?<=читал )\w+ \w+(?=!)', line))        
print(output)
