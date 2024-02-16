from random import choice

class RandomWalk:
    #una clase para generar caminos aleatorios
    def __init__(self, num_points=5000):
        #inicializa los atributos de un camino
        self.num_points = num_points

        #todos los caminos empiezan en (0,0)
        self.x_values=[0]
        self.y_values=[0]

    def fill_walk(self):
        #calcula todos los puntos del camino

        #sigue dando pasos hasta que el camino alcanza la longitud deseada
        while len(self.x_values) < self.num_points:

            #decide en que direccion y cuando avanzar en esa direccion
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #rechaza movimientos que no vam a ninguna parte
            if x_step == 0 and y_step ==0:
                continue

            #calcula la nueva posicion
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)