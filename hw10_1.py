#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  15 21:41:42 2021

@author: rita
"""

import argparse 
from multiprocessing import Pool


def prime_factorization(number):
    number = int(number)
    divisor = 2
    output = [number]

    
    while number != 1:       
        while number % divisor == 0:           
            number //= divisor            
            output.append(divisor)
        divisor += 1
        
    result = str(output[0]) + " : " + str(' '.join(map(str, output[1:])))
    return result

def Parser():
    parser  = argparse.ArgumentParser()
    parser.add_argument("input", nargs = "+")
    return parser

if __name__ == '__main__':
    parser = Parser()
    numbers = parser.parse_args()
    
    if numbers.input:
        pool = Pool(processes = len(numbers.input))
        results = pool.map(prime_factorization, numbers.input)
        print('\n'.join(map(str, results)))
    else:
        print("the program needs some input numbers to actually work")
    