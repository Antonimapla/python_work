# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 18:39:25 2023

@author: user
"""

class Car:      #clase base
    """intento de representar un coche"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """devuelve un nombre descriptivo con el formato adecuado"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """imprime una frase con el kilometraje del coche"""
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        """configura el kilometraje con el valor dado"""
        """rechaza el cambio si se intenta retroceder el cuentakilometros"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No esta permitido retroceder el cuentakilometros.")
            
    def increment_odometer(self, miles):
        """añade una cantidad dada al cuentakilometros"""
        self.odometer_reading += miles
        
        
class ElectricCar(Car):    #clase derivada
    """representamos aspectos propios de vehiculos electricos"""
    def __init__(self, make, model, year):
        """inicializa los atributos de la clase base"""
        super().__init__(make, model, year)
        self.battery = Battery()
        
        
       
class Battery:
    """intento de modelar una bateria para coche electrico"""
    def __init__(self,battery_size=75):
        """inicializa los atributos de la bateria"""
        self.battery_size = battery_size
        
       
    def describe_battery(self):
        """Imprime una frase que describe el tamaño de la bateria"""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """imprime una frase sobre la autonomia de la bateria"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge.")
        
        
        
my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()





