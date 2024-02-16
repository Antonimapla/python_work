# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:29:57 2023

@author: user
"""

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"El perro {self.name} se sienta")
        
    def roll_over(self):
        print(f"el perro {self.name} hace la croqueta")
        
        
my_dog = Dog('braco', '7')
your_dog = Dog('boby', '5')

print(f"Mi perro {my_dog.name} tiene {my_dog.age} años")
print(f"Tu perro {your_dog.name} tiene {your_dog.age} años")
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()
        