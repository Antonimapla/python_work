# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 17:51:50 2023

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
       

class Admin(Usuarios):
    """creamos la clase admin que hereda de usuarios"""
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        privilegios = ['Añadir comentarios', 'borrar comentarios', 'vetar usuarios']
        self.privilegios = privilegios
        
    def show_privileges(privilegios):
        """muestra los privilegios del admin"""
        
        for i in privilegios:
            print(i)




#usuario = Usuarios('Pedro', 'Lopez', '36')
#usuario.datos_usuario()
#usuario.saludo_usuario()
#usuario.incrementar_intentos_inicio(0)
#usuario.reestablecer_intentos_inicio(0)
privilegios = ['Añadir comentarios', 'borrar comentarios', 'vetar usuarios']
Administrador = Admin('jose', 'lopez', '34')

Admin.show_privileges(privilegios)










