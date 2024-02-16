class Usuario:
    """clase para guardar datos de usuario"""
    def __init__(self, nombre, apellido, edad, sexo):
         self.nombre = nombre
         self.apellido = apellido
         self.edad = edad
         self.sexo = sexo
         
    def describir_usuario(self):
        print(f"Usuario : {self.nombre} {self.apellido} edad: {self.edad} sexo: {self.sexo}")
        
    def saludo(self):
        print(f"Hola {self.nombre} se le saluda.")
        
         

user1 = Usuario("Luis", "Perez", 34, "masculino")
user1.describir_usuario()
user1.saludo()
print("\n")
user2 = Usuario("Pedro", "Rico", 45, "masculino")
user2.describir_usuario()
user2.saludo()
print("\n")
user3 = Usuario("Maria", "Lopez", 28, "femenino")
user3.describir_usuario()
user3.saludo()