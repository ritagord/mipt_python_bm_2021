#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 17:08:13 2021

@author: rita
"""

class FileIterator:
    def __init__(self, file_path: str, lines_read: int = -1, num_times: int = 0):
        self.file_path = file_path        
        self.lines_read = lines_read
        
        with open(self.file_path, "r") as file:        
            self.num_times = len(file.readlines())

    def __iter__(self):                    
        return self
    
    def __next__(self):        
        if self.lines_read + 2 <= self.num_times:
            self.lines_read += 1            
            
            with open(self.file_path, "r") as file:                
                line = file.readlines()[self.lines_read]                
                return line                    
        else:
            raise StopIteration
    
first_letters = list()

for line in FileIterator("./iteration.txt"):
    stripped_line = line.strip()
    first_letters.append(stripped_line[0])
    
possibly_some_encrypted_message = ''.join(first_letters)
print("First letters of the file's lines make up the following text: ", possibly_some_encrypted_message)

del FileIterator
    