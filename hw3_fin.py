#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 10:08:40 2021

@author: rita
"""

import os
import csv

with open("./vitamins.csv", "w") as output:
    writer = csv.writer(output)
    writer.writerow(["vitamin", "vitamers", "solubility", "daily_requirement", "deficiency_diseases"])

    for filename in os.listdir("./vitamins"):
        with open(os.path.join("./vitamins", filename), 'r') as input_fileA:
            strippedA = (line.strip() for line in input_fileA)
            linesA = (line.split(",") for line in strippedA if line)
            writer.writerow(linesA)
            
import json

characteristics = { "vitamin", "vitamers", "solubility", "daily_requirement", "deficiency_diseases" }
res_dict = dict.fromkeys(characteristics)

with open("./vitamins.json", "w") as out_file:    
    for filename in os.listdir("./vitamins"):
        with open(os.path.join("./vitamins", filename), 'r') as input_fileA:
            for line, character in zip(input_fileA, characteristics):
                strippedA = line.strip()       
                res_dict[character] = strippedA            
            json.dump(res_dict, out_file, indent = 6)
            
