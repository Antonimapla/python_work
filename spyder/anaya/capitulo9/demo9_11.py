# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 18:40:10 2023

@author: user
"""

from clases import *

user = Usuarios('juan', 'lopez', 35)
user.datos_usuario()

user1 = Admin('luis', 'sanchez', 27)
user1.datos_usuario()

user1.privilegio(['leer', 'editar', 'borrar'])