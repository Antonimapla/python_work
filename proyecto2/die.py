from random import randint

class Die:
    #clase que represnta un solo dado
    def __init__(self, num_sides=6):
        #asume que el dado tiene 6 caras
        self.num_sides = num_sides

    def roll(self):
        #devuelve un valor aleatorio entre el 1 y el numero de caras
        return randint(1, self.num_sides)