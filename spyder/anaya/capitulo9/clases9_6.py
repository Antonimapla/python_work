# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:43:53 2023

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
        

class CarritoDeHelados(Restaurante):
    #clase derivada de resturante
    def __init__(self,nombre,tipo,sabor):
        super().__init__(nombre, tipo)
        self.sabor = sabor

    def sabores(self):
        """describe diferentes sabores"""
        sabores = ['fresa', 'lima', 'nata']
        for gel in sabores:
            print(gel)

restaurante = Restaurante('Meson', 'mediterranea')
restaurante.describir_restaurante()
#restaurante.abrir_restaurante()  
helado = CarritoDeHelados('fresa', 'nata', 'lima')
helado.sabores()

