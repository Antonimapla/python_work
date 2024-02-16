# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 21:08:11 2023

@author: user
"""

class Restaurante:
    #representacion de un restaurante
    def __init__(self, nombre, tipo):
        """inicializa atributos"""
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
        self.numero_servido = 0
        
    def describir_restaurante(self):
        """describe nombre y tipo de cocina"""
        print(f"El nombre del restaurante es {self.nombre_restaurante}.")
        print(f"\nSu cocina es del tipo {self.tipo_cocina}.")
        
    def abrir_restaurante(self):
        """indica que el restaurante esta abierto"""
        print(f"\nEl restaurante {self.nombre_restaurante} esta abierto.")
        
    def servicios_servidos(self, servicios):
        """contamos los servicios efectuados"""
        self.numero_servido = servicios
        print(f"Numero de servicios efectuados {self.numero_servido}")
        
    def incrementar_servicios(self, numero):
        """añadimos servicios a los efectuados"""
        self.numero_servido += numero
        print(f"Sericios totales {self.numero_servido}")
        
restaurante = Restaurante('Meson', 'mediterranea')
restaurante.describir_restaurante()
restaurante.abrir_restaurante()  
restaurante.servicios_servidos(18)
restaurante.incrementar_servicios(10)
