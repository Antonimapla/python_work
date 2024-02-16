class Restaurante:
    """clase para definir un restaurante y su cocina"""
    
    def __init__(self, nombre_restaurante, tipo_cocina):
        self.nombre_restaurante = nombre_restaurante
        self.tipo_cocina = tipo_cocina
        
    def describir_restaurante(self):
        print(f"Nombre del restaurante {self.nombre_restaurante}")
        print(f"Tipo de cocina {self.tipo_cocina}.")

    def abrir_restaurante(self):
        print("El restaurante esta abierto.")







restaurant = Restaurante("El mimo", "cocina gallega")
restaurant.describir_restaurante()
#restaurant.abrir_restaurante()
print("\n")
restaurant1 = Restaurante("el borinot", "comida catalana")

restaurant2 = Restaurante("el pato loco", "asado de pato")

restaurant1.describir_restaurante()
print("\n")
restaurant2.describir_restaurante()