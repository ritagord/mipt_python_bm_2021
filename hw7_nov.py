#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 11:36:20 2021

@author: rita
"""
import random 
from abc import ABC, abstractmethod

class PolynucleotideChain(ABC):
    
    @abstractmethod
    def __str__(self):
        raise NotImplementedError()
    def __getitem__(self):
        raise NotImplementedError()
    def __add__(self, other):
        raise NotImplementedError()
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
        return frst_chain
        
    def __eq__(self, other):
        raise NotImplementedError()

class DNA(PolynucleotideChain):
    global complementary_DNA     
    complementary_DNA = {"A": "T", "T": "A", "G": "C", "C": "G"}
    global nucleotides_DNA
    nucleotides_DNA = {"A", "T", "G", "C"}    
    
    def __init__(self, first_chain):        
        if set(first_chain).issubset(nucleotides_DNA):            
            self.first_chain = first_chain
        else:
            raise Exception
     
    def complementary_chain(self):
        second_chain = []
        for i in self.first_chain:
            second_chain.append(complementary_DNA[i])
        s_chain = ''.join(second_chain)
        return s_chain
    
    def __getitem__(self, i = int):
        second_chain = self.complementary_chain()
        return self.first_chain[i], second_chain[i]
        
    def __add__(self, other):
        second_chain_1 = self.complementary_chain()
        second_chain_2 = other.complementary_chain()
        f_chain = self.first_chain + other.first_chain
        s_chain = second_chain_1 + second_chain_2         
        return f_chain, s_chain
    
    def __mul__(self, other):
        frst_chain = super().__mul__(other)    
        f_chain = DNA(frst_chain)
        s_chain = f_chain.complementary_chain()       
        return frst_chain, s_chain
    
    def __eq__(self, other):
        second_chain = self.complementary_chain()
        if self.first_chain == other.first_chain or second_chain == other.first_chain:
            return True
        
    def __str__(self):
        return print(self.first_chain)
    
class RNA(PolynucleotideChain):
    global complementary_RNA 
    complementary_RNA = {"A": "T", "U": "A", "G": "C", "C": "G"}
    global  nucleotides_RNA 
    nucleotides_RNA = {"A", "U", "G", "C"}  
    
    def __init__(self, first_chain):
        if set(first_chain).issubset(nucleotides_RNA):            
            self.first_chain = first_chain
        else:
            raise Exception
    
    def __getitem__(self, i = int):
        return self.first_chain[i]
    
    def __add__(self, other):
        new_chain = self.first_chain + other.first_chain         
        return new_chain
    
    def __mul__(self, other):
        n_chain = super().__mul__(other)
        return n_chain
    
    def __eq__(self, other):
        if self.first_chain == other.first_chain:
            return True
        
    def __str__(self):
        return print(self.first_chain)
    
    def complementary_DNA(self):
        first_chain_DNA = []
        for i in self.chain:
            first_chain_DNA.append(complementary_RNA[i])
        fst_chain = ''.join(first_chain_DNA)
        f_chain = DNA(fst_chain)
        s_chain = f_chain.complementary_chain()
        return fst_chain, s_chain
 
     