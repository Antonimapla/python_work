# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 21:25:53 2023

@author: user
"""

class Usuarios:
    """creamos datos de usuario"""
    def __init__(self, nombre, apellido, edad):
        """inicializamos atributos"""
        self.nombre_usuario = nombre
        self.apellido_usuario = apellido
        self.edad_usuario = edad
        self.intentos_inicio = 0
        
    def datos_usuario(self):
        """imprimimos los datos de usuario"""
        print(f"Nombre de usuario: {self.nombre_usuario}.\n")
        print(f"Apellido usuario: {self.apellido_usuario}.\n")
        print(f"Edad usuario: {self.edad_usuario}.\n")
        
    def saludo_usuario(self):
        """imprimimos un saludo para el usuario"""
        print(f"Hola {self.nombre_usuario} como estas?\n")
        
    def incrementar_intentos_inicio(self, numero):
        """incrementamos los intentos de inicio"""
        self.intentos_inicio += numero
        print(f"Intentos de inicio {self.intentos_inicio}")
        
    def reestablecer_intentos_inicio(self, num):
        """ponemos a 0 el contador de intentos de inicio"""
        self.intentos_inicio = num
        print(f"Intentos de inicio reestablecido {self.intentos_inicio}")
       
usuario = Usuarios('Pedro', 'Lopez', '36')
usuario.datos_usuario()
usuario.saludo_usuario()
usuario.incrementar_intentos_inicio(0)
usuario.reestablecer_intentos_inicio(0)

usuario1 = Usuarios('juan', 'martinez', '55')
usuario1.datos_usuario()
usuario1.saludo_usuario()
usuario1.incrementar_intentos_inicio(0)
usuario1.reestablecer_intentos_inicio(0)

usuario2 = Usuarios('luis', 'gomez', '27')
usuario2.datos_usuario()
usuario2.saludo_usuario()
usuario2.incrementar_intentos_inicio(0)
usuario2.reestablecer_intentos_inicio(0)




