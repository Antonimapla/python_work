# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:16:02 2023

@author: user
"""
from random import choice

lista = [4, 5, 8, 56, 89, 23 ,12, 87, 61, 90, 'a', 'g', 'i', 'p', 'z']
premio = []
boleto = []
aciertos = 0
class Sorteo:
    def __init__(self, lista):
        self.lista = lista
    
    def realizar_sorteo(self):       
        i = 0
        for i in range(0, 4):
            seleccionado = choice(self.lista)
            premio.append(seleccionado) 
            if i >= 4:
                break
            else:
                i = i + 1
                
    def muestra_premio(self):
        str2 = " . ".join(str(x) for x in premio)
        print(f"El boleto ganador es el que tenga los digitos : {str2}.")
        return str2
        
    def mi_boleto(self):   #creamos un boleto para participar en el sorteo 
       n = 0
       for n in range(0, 4):
           seleccionado1 = choice(self.lista)
           boleto.append(seleccionado1) 
           if n >= 4:
               break
           elif n == 4:
               return boleto
           else:
               n = n + 1 
               
    def muestra_boleto(self):
        str3 = " . ".join(str(y) for y in boleto)
        print(f"Su boleto es : {str3}.")
        
class Ganador(Sorteo):
#comparamos el boleto con los numeros salidos en el sorteo    
    def __init__(self,premio, boleto):
        self.premio = premio
        self.boleto = boleto

    def compara(self, premio, boleto):   #comparamos listas individualmente
        aciertos = 0
        print(premio, boleto)
        for i in range(0, 4):            #numeros del boleto
            for x in range(0, 4):        #numeros del premio
                if boleto[i] == premio[x]:
                    aciertos = aciertos + 1
                    print(aciertos)
                elif aciertos == 4:
                    print(f"Su boleto esta premiado {boleto}.")
               
           
sorteo = Sorteo(lista)                       #creamos instancia de la clase Sorteo
sorteo.realizar_sorteo()                     #realizamos el sorteo 
numero_premiado = sorteo.muestra_premio()    #mostramos la convinacion ganadora
                                               #y la guardamos en numero_premiado
sorteo.mi_boleto()                           #confeccionamos mi boleto
mi_numero = boleto.copy()

sorteo.muestra_boleto() 

premiado = Ganador(premio, boleto)                     #mostramos mi boleto
premiado.compara(premio, boleto)







