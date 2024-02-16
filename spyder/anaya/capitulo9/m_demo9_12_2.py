# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:07:50 2023

@author: user
"""

class Admin(Usuarios):
    def __init__(self, nombre, apellido, edad, privilegios):
        super().__init__(nombre, apellido, edad)
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.privilegios = privilegios
        
    def lista_privilegios(self):
        privilegios = ['leer', 'escribir' , 'editar', 'anotar']
        for i in privilegios:
            print(i)