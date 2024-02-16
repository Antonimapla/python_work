# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:20:16 2023

@author: user
"""

from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()