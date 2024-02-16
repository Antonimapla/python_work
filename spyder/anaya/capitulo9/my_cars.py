# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 14:58:59 2023

@author: user
"""

from car import Car, ElectricCar

my_beetle = Car('volkswagwn', 'beetle', 2019)

print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)

print(my_tesla.get_descriptive_name())