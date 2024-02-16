# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 18:07:39 2023

@author: user
"""

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())            #impide que salga la ultima fila en blanco