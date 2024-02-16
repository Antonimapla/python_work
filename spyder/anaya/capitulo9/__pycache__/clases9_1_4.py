class Restaurante:
    #representacion de un restaurante
    def __init__(self, nombre, tipo):
        """inicializa atributos"""
        self.nombre_restaurante = nombre
        self.tipo_cocina = tipo
        
    def describir_restaurante(self):
        """describe nombre y tipo de cocina"""
        print(f"El nombre del restaurante es {self.nombre_restaurante}.")
        print(f"\nSu cocina es del tipo {self.tipo_cocina}.")
        
    def abrir_restaurante(self):
        """indica que el restaurante esta abierto"""
        print(f"\nEl restaurante {self.nombre_restaurante} esta abierto.")
        
class CarritoDeHelados(Restaurante):
    def __init__(self, nombre, tipo, sabor):
        super().__init__(nombre, tipo)
        self.sabores = sabor

    def muestra_sabores(self):
        self.sabor = ['fresa', 'nata', 'turron']
        for i in self.sabor:
            print(i)
           
gustos = CarritoDeHelados('fresa', 'nata', 'turron')
gustos.muestra_sabores()



restaurante = Restaurante('Meson', 'mediterranea')
restaurante.describir_restaurante()
restaurante.abrir_restaurante()        