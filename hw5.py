#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 11:30:14 2021

@author: rita
"""

class Human:
    def __init__(self, name, sex, year_of_birth, hair_length, nail_length, nail_color = "no color"):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        self.hair_length = hair_length
        self.nail_length = nail_length
        self.nail_color = nail_color

    def __str__(self):        
        return (self.name,
        self.sex,
        self.year_of_birth,
        self.hair_length,
        self.nail_length,
        self.nail_color)

import random        

class Manicurist:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
        
    def do_job(self, client):
        if client.nail_length >= 1:
            client.nail_length -= 1
        client.nail_color = random.choice(["red", "violet", "green"])
        
        
class Hairdresser:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
    
    def do_job(self, client):
        if client.hair_length >= 1:
            client.hair_length -= 1
      
    
class Barber:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.year_of_birth = year_of_birth
    
    def do_job(self, client):
        if client.sex == "M" and client.hair_length >= 1:
            client.hair_length -= 1
            
        if client.sex == "F":
            raise ValueError
        
      
    


neo = Human(
  name="Neo", sex="M", year_of_birth=1964,
  hair_length=10, nail_length=2
)

trinity = Human(
  name="Trinity", sex="F", year_of_birth=1967,
  hair_length=30, nail_length=5
)

manicurist = Manicurist(name="Samara", sex="F", year_of_birth=1992)
barber = Barber(name="Bob", sex="M", year_of_birth=1987)

manicurist.do_job(neo)
print(neo.__str__())
