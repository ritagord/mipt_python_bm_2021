#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 16:19:05 2021

@author: rita
"""

import argparse
import json

pars = argparse.ArgumentParser()
pars.add_argument("--name", required = True, type = str)
pars.add_argument("--country", required = True, type = str)
pars.add_argument("--petal-colour", required = True, type = str, choices = ["R", "W", "Y", "V", "B"] )
pars.add_argument("--stem-length", required = True, type = int)
pars.add_argument("--with-thorns", required = False, action = "store_true")
pars.add_argument("--companion-plants", required = False, default = None, nargs = "*")

with open("./journal.txt", "a") as output_file:
    json.dump(vars(pars.parse_args()), output_file)