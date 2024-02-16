# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:16:02 2023

@author: user
"""

from random import choice

lista = [4, 5, 8, 56, 89, 23 ,12, 87, 61, 90, 'a', 'g', 'i', 'p', 'z']
premio = []

class Sorteo:
    def __init__(self, lista):
        self.lista = lista
    
    def realizar_sorteo(self):       
        i = 0
        for i in range(0, 4):
            seleccionado = choice(self.lista)
            premio.append(seleccionado) 
            if i >= 4:
                break
            else:
                i = i + 1
                
    def muestra_premio(self):
        str2 = " . ".join(str(x) for x in premio)
        
        print(f"El boleto ganador es el que tenga los digitos : {str2}.")

sorteo = Sorteo(lista)
sorteo.realizar_sorteo()
sorteo.muestra_premio()
