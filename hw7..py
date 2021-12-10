#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:36:20 2021

@author: rita
"""
import random 
from abc import ABC, abstractmethod

class polynucleotide_chain(ABC):
    
    @abstractmethod
    def printing(self):
        pass
    def complementary_chain(self):
        pass
    def index(self):
        pass
    def __add__(self, other):
        pass
    def __mul__(self, other):
        pass
    def __eq__(self, other):
        pass

class DNA(polynucleotide_chain):
    
    def __init__(self, first_chain):        
        if set(first_chain).issubset({"A", "T", "G", "C"}):            
            self.first_chain = first_chain
        else:
            raise Exception
     
    def complementary_chain(self):
        complementary = {"A": "T", "T": "A", "G": "C", "C": "G"}
        second_chain = []
        for i in self.first_chain:
            second_chain.append(complementary[i])
        s_chain = ''.join(second_chain)
        return s_chain
    
    def index(self, i = int):
        second_chain = self.complementary_chain()
        return print(self.first_chain[i], second_chain[i])
        
    def __add__(self, other):
        second_chain_1 = self.complementary_chain()
        second_chain_2 = other.complementary_chain()
        f_chain = self.first_chain + other.first_chain
        s_chain = second_chain_1 + second_chain_2         
        return print(f_chain, s_chain)
    
    def __mul__(self, other):
        fst_chain = []
        chains = [self.first_chain, other.first_chain]
        longer_chain = max(chains, key = len)
        shorter_chain = min(chains, key = len)
                
        for i in range(len(shorter_chain)):
            chain = random.choice(chains)            
            fst_chain.append(chain[i])
            
        for i in range(len(shorter_chain)+1, len(longer_chain)):
            fst_chain.append(longer_chain[i])
            
        frst_chain = ''.join(fst_chain)
        f_chain = DNA(frst_chain)
        s_chain = f_chain.complementary_chain()       
        return print(frst_chain, s_chain)
    
    def __eq__(self, other):
        #"первую и вторую цепочки днк можно проверять на равенство 
        # днк1 = днк2 вне зависимости от порядка цепочек?
        second_chain = self.complementary_chain()
        if self.first_chain == other.first_chain or second_chain == other.first_chain:
            return print("TRUE")
        
    def printing(self):
        return print(self.first_chain)
    
class RNA:
    def __init__(self, chain):
        if set(chain).issubset({"A", "U", "G", "C"}):            
            self.chain = chain
        else:
            raise Exception
    
    def index(self, i = int):
        return print(self.chain[i])
    
    def __add__(self, other):
        new_chain = self.chain + other.chain         
        return print(new_chain)
    
    def __mul__(self, other):
        new_chain = []
        chains = [self.chain, other.chain]
        longer_chain = max(chains, key = len)
        shorter_chain = min(chains, key = len)
                
        for i in range(len(shorter_chain)):
            chain_ch = random.choice(chains)            
            new_chain.append(chain_ch[i])
            
        for i in range(len(shorter_chain)+1, len(longer_chain)):
            new_chain.append(longer_chain[i])
            
        n_chain = ''.join(new_chain)
        n_chain = RNA(n_chain)
        return print(n_chain)
    
    def __eq__(self, other):
        if self.chain == other.chain:
            return print("TRUE")
        
    def printing(self):
        return print(self.chain)
    
    def complementary_DNA(self):
        complementary = {"A": "T", "U": "A", "G": "C", "C": "G"}
        first_chain = []
        for i in self.chain:
            first_chain.append(complementary[i])
        fst_chain = ''.join(first_chain)
        f_chain = DNA(fst_chain)
        s_chain = f_chain.complementary_chain()
        return print(fst_chain, s_chain)
        