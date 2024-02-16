# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:15:08 2023

@author: user
"""

class Car:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.odometer_reader = 0
        
        
    def get_descriptive_name(self):
        descriptive_name = f"{self.año} {self.marca} {self.modelo}"
        return descriptive_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reader} miles on it.")
        
    def update_odometer(self, mileage):
        self.odometer_reader = mileage
        if mileage >= self.odometer_reader:
            odometer_reader = mileage
        elif mileage < self.odometer_reader: 
            print("No se pueden quitar kilometros")
        
    def increment_odometer(self, miles):
        self.odometer_reader += miles
        
        
class Battery:
    def __init__(self, battery_size = 75):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"Este coche tiene una bateria de {self.battery_size} kWh.") 
        
      
        
class Electric_Car(Car):
    def __init__(self, marca, modelo, año):
        super().__init__(marca, modelo, año)
        self.battery = Battery()
                   
    def get_range(self):
        if self.battery.battery_size == 75:
            range = 260
        elif self.battery.battery_size == 100:
            range = 315
        print(f"Este coche tiene una autonomia de {range} con la bateria a tope.")                
        
        
        
my_tesla = Electric_Car('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(3555)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.get_range()
"""
my_new_car = Car('seat', '600', '1810')
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(333)
my_new_car.read_odometer()
my_new_car.update_odometer(150)
my_new_car.read_odometer()
my_new_car.increment_odometer(500)
my_new_car.read_odometer()
"""







