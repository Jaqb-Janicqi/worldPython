
import random
from world.organisms.plants.Plant import Plant


class SowThistle(Plant):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "SowThistle"
        self.skin = ","
        self.id = 2
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 0
        self.baseStrength = 0
        
    def action(self):
        for i in range (3):
            if(self.alive and random.randint(0, 100) < self.sewChance):
                self.sew()