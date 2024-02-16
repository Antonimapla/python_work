# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 16:17:59 2023

@author: user
"""

filename = 'programming.txt'

with open(filename, 'r') as file_object:
    lines = file_object.readlines()
    print(lines)
