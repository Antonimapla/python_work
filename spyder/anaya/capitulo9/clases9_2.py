# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 18:21:46 2023

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
        print(f"\nSu cocina es del tipo {self.tipo_cocina}.\n")
        
    def abrir_restaurante(self):
        """indica que el restaurante esta abierto"""
        print(f"\nEl restaurante {self.nombre_restaurante} esta abierto.\n")
        
restaurante = Restaurante('Meson', 'mediterranea')
restaurante.describir_restaurante()
restaurante.abrir_restaurante()      

restaurante1 = Restaurante('El Pla', 'tipica')

restaurante2 = Restaurante('oxido', 'peix')

restaurante3 = Restaurante('el oso', 'carn')

restaurante1.describir_restaurante()

restaurante2.describir_restaurante()

restaurante3.describir_restaurante()