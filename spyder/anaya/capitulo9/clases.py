# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:47:17 2023

@author: user
"""
class Usuarios:
    """creamos datos de usuario"""
    def __init__(self, nombre, apellido, edad,):
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





            
privilegios = ['leer', 'escribir' , 'editar', 'anotar']
#lista_privilegios(privilegios)
Admin.lista_privilegios(privilegios)            
    




