#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 16:05:22 2021

@author: rita
"""

class Rational:
    def __init__(self, numenator, denumenator):
        self.numenator = numenator
        self.denumenator = denumenator
        
    def __add__(self, other):
        return Rational(numenator = self.numenator*other.denumenator + other.numenator*self.denumenator, denumenator = self.denumenator*other.denumenator)
    def __sub__(self, other):
        return Rational(numenator = self.numenator*other.denumenator - other.numenator*self.denumenator, denumenator = self.denumenator*other.denumenator)
    def __mul__(self, other):
        return Rational(numenator = self.numenator*other.numenator, denumenator = self.denumenator*other.denumenator)
    def __truediv__(self, other):
        return Rational(numenator = self.numenator*other.denumenator, denumenator = self.denumenator*other.numenator)

    def __eq__(self, other):
        if self.numenator == other.numenator and self.denumenator == other.denumenator:
            return True
        else:
            return False
        
    def __float__(self):
        return self.numenator/self.denumenator
    
    @classmethod
    def __from_string__(cls, string):
        read = string.split("/")
        num = int(read[0])
        denum = int(read[1])
        return Rational(numenator = num, denumenator = denum)
        
def test_operations():
    assert Rational(1, 2) + Rational(1, 2) == Rational(4, 4)
    assert Rational(6, 5) - Rational(1, 4) == Rational(19, 20)
    assert Rational(2, 5) * Rational(3, 7) == Rational(6, 35)
    assert Rational(15, 4) / Rational(5, 2) == Rational(30, 20)

def test_cast_to_float():
    assert float(Rational(5, 7))
    
def test_parse_from_string():
    assert Rational.__from_string__("3/4") == Rational(3, 4)


if __name__ == '__main__':
    test_operations()
    test_cast_to_float()
    test_parse_from_string()


