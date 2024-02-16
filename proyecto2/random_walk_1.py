from random import choice

class RandomWalk:
    #clase para generar caminos aleatorios
    def __init__(self, num_points=5000):
        #inicializa los atributos de un camino
        self.num_points = num_points

        #todos los caminos empiezan en (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        #calcula todos los puntos del camino

        #sigue dando pasos hasta que el camino alcanza la longitud deseada
        while len(self.x_values) < self.num_points:
            #decide en que direccion ir y cuanto avanza en esa direccion
            x_direccion = choice([1, -1])   #puede ser cualquiera de los dos valores
            x_distance = choice([0, 1, 2, 3, 4]) #aleatorio de la distancia que recorre cada paso
            x_step = x_direccion * x_distance   #distancia recorrida en ese sentido

            #decide en que direccion ir y cuanto avanza en esa direccion
            y_direccion = choice([1, -1])   #puede ser cualquiera de los dos valores
            y_distance = choice([0, 1, 2, 3, 4]) #aleatorio de la distancia que recorre cada paso
            y_step = y_direccion * y_distance   #distancia recorrida en ese sentido
    
            #rechaza movimientos que no van a ninguna parte
            if x_step == 0 and y_step == 0:
                continue

            #calcula la nueva posicion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

