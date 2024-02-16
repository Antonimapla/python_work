# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 20:02:16 2023

@author: user
"""

class Car:
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
        
        
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(60)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outbak', '2015')
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(22_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()






