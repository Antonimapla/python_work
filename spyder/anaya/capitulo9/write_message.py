# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 15:59:03 2023

@author: user
"""

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("i love programing mucho antes de dormir.\n")
    file_object.write("el amor es infinito pero cuando se acaba finito.\n")
    file_object.write("\tEsto es un añadido al antiguo texto")
    file_object.write("\n\n Y esto tambien.")