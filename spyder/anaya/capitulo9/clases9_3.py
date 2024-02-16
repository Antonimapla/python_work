# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 18:28:20 2023

@author: user
"""

class Usuarios:
    """creamos datos de usuario"""
    def __init__(self, nombre, apellido, edad):
        """inicializamos atributos"""
        self.nombre_usuario = nombre
        self.apellido_usuario = apellido
        self.edad_usuario = edad
        
    def datos_usuario(self):
        """imprimimos los datos de usuario"""
        print(f"Nombre de usuario: {self.nombre_usuario}.\n")
        print(f"Apellido usuario: {self.apellido_usuario}.\n")
        print(f"Edad usuario: {self.edad_usuario}.\n")
        
    def saludo_usuario(self):
        """imprimimos un saludo para el usuario"""
        print(f"Hola {self.nombre_usuario} como estas?\n")
       
usuario = Usuarios('Pedro', 'Lopez', '36')
usuario.datos_usuario()
usuario.saludo_usuario()

usuario1 = Usuarios('juan', 'martinez', '55')
usuario1.datos_usuario()
usuario1.saludo_usuario()

usuario2 = Usuarios('luis', 'gomez', '27')
usuario2.datos_usuario()
usuario2.saludo_usuario()
