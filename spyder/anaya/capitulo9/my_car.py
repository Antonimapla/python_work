# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:20:16 2023

@author: user
"""

from car import ElectricCar

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.descrive_battery()
#my_tesla.battery.get_range()