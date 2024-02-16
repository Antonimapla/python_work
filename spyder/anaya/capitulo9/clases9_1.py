# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 17:43:48 2023

@author: user
"""

class Restaurante:
    #representacion de un restaurante
    def __init__(self, nombre, tipo):
        """inicializa atributos"""
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
        
    def describir_restaurante(self):
        """describe nombre y tipo de cocina"""
        print(f"El nombre del restaurante es {self.nombre_restaurante}.")
        print(f"\nSu cocina es del tipo {self.tipo_cocina}.")
        
    def abrir_restaurante(self):
        """indica que el restaurante esta abierto"""
        print(f"\nEl restaurante {self.nombre_restaurante} esta abierto.")
        
restaurante = Restaurante('Meson', 'mediterranea')
restaurante.describir_restaurante()
restaurante.abrir_restaurante()        
        