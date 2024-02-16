# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:03:01 2023

@author: user
"""

from random import randint

#hacemos una clase dado de 6 caras
class Dado:
    def __init__(self, caras = 6):
        self.caras = caras
        
    def tirar_dado(self):      #☻tirada aleatoria del dado
        dado = randint(1, self.caras)
        print(dado)
        
dado_6_caras = Dado()         #tiramos el daado de 6 caras 10 veces
tiradas = 10
while tiradas:
    dado_6_caras.tirar_dado()
    tiradas = tiradas - 1
    
dado_10_caras = Dado(10)       #tiramos el dado de 10 caras 10 veces
tiradas = 10
while tiradas:
    dado_10_caras.tirar_dado()
    tiradas = tiradas - 1

dado_20_caras = Dado(20)      #tiramos el dado de 20 caras 10 veces
tiradas = 10
while tiradas:
    dado_20_caras.tirar_dado()
    tiradas = tiradas - 1