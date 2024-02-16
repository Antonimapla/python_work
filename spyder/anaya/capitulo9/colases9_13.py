# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:26:34 2023

@author: user
"""
from random import randint

#hacemos una clase dado de 6 caras
class Dado:
    def __init__(self, caras = 6):
        self.caras = caras
        
    def tirar_dado(self):
        dado = randint(1, self.caras)
        print(dado)
        
dado_6_caras = Dado()
tirada = dado_6_caras.tirar_dado()