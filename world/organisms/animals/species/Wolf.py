
from world.organisms.animals.Animal import Animal


class Wolf(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Wolf"
        self.skin = "W"
        self.id = 1
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 9
        self.baseStrength = 9
        self.initiative = 5