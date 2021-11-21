#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 17:37:28 2021

@author: rita
"""

from os import listdir
from os.path import isfile, join
import argparse 
import threading

def thread_job(file_name):
    start = "/{}"
    chosen_lines = []
    thepath = file_path  + start.format(file_name)
    
    with open(thepath, "r") as file:
        for line in file:
            if thestring in line:
                chosen_lines.append(line)
                
    return(print(file_name, ":",  '\n'.join(map(str, chosen_lines))))


def run_threads(onlyfiles):
    threads = [
        threading.Thread(target=thread_job, args=(i,))
        for i in onlyfiles
    ]
    for thread in threads:
        thread.start()  




def Parser():
    parser  = argparse.ArgumentParser()
    parser.add_argument("string", nargs = "+")
    return parser

if __name__ == '__main__':
    parser = Parser()
    string_input = parser.parse_args()
    
    if string_input.string:
        file_path = string_input.string.pop()
        thestring = ' '.join(map(str, string_input.string))
        print(thestring)
        
        onlyfiles = [f for f in listdir(file_path) if isfile(join(file_path, f))]

    else:
        print("the program needs some input text to actually work")
 
    
run_threads(onlyfiles)
