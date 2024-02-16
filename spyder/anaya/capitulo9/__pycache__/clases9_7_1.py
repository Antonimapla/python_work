class Usuario:
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
    
    def mostrar_privilegios(self):
        print(self.privilegios)
"""
usuario = Usuario('Pedro', 'Lopez', '36')
usuario.datos_usuario()
usuario.saludo_usuario()
usuario.mostrar_privilegios()
"""

class Admin(Usuario):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        self.privilegios = ['leer', 'beber', 'vomitar']

    def show_privilegios(self):
        print(self.privilegios)



user = Admin('jose', 'pepe', 'pep')
user.show_privilegios()
