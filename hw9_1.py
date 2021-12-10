#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:39:50 2021

@author: rita
"""


def computing():
    count = 0
    summa = 0
    sq_sum = 0

    while True:
        try:
            number = yield
            
            count += 1
            summa += number
            sq_sum += number**2
        
            print("количество элементов:", count, 
              "среднее:", summa/count, 
              "дисперсия:", (sq_sum - (summa/count)**2) )
            
        except GeneratorExit as exception:
            print("computing stopped")
            raise exception
        
coroutine = computing()
next(coroutine)

# тестовый вариант набора чисел
test = [1, 2, 5, 6, 3]
for number in test:
    coroutine.send(number)