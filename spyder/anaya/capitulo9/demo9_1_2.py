class Car:
    """representacion de un coche"""
    
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """devuelve los datos en formato correcto"""
        long_name = f"{self.año} {self.marca} {self.modelo}."
        return long_name.title()
    
    def read_odometer(self):
        """imprime una oracion que indica el kilometraje del coche"""
        print(f"Este coche tiene {self.odometer_reading}Km.")
        
    def update_odometer(self, km):
        """actualiza los kms"""
        self.odometer_reading = km
        if km >= self.odometer_reading:
            self.odometer_reading = km
        else:
            print("No puedes retroceder kms.")
            
    def increment_odometer(self, kilos):
        """aumenta los kms del coche"""
        self.odometer_reading += kilos
        

class ElectricCar(Car):
    """representa aspectos propios de un coche electrico"""
    def __init__(self, marca, modelo, año):
        """inicializa los atributos de la clase base"""
        super().__init__(marca, modelo, año)
        self.battery = Battery()
        
    
class Battery:
    """intento de modelar una bateria de coche electrico"""
    def __init__(self, battery_size=75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        """imprime una frase con el tamaño de la bateria"""
        print(f"Este coche tiene una bateria de {self.battery_size} kwh.")
        
    def get_range(self):
        """imprime la autonomia de la baetria"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"Este coche tiene una autonomia de {range} Kms.")
        
        

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())    
print(my_tesla.battery.describe_battery())        
print(my_tesla.battery.get_range())

mi_auto = Car('seat', '850', 1965)
print(mi_auto.get_descriptive_name())
print(mi_auto.read_odometer())




