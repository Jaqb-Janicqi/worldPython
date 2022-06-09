
import random
from world.organisms.Organism import Organism


class Plant(Organism):
    def __init__(self, world):
        super().__init__(world)
        self.alive = True
        self.strength = 0
        self.baseStrength = 0
        self.initiative = 0
        self.skin = None
        self.name = None
        self.directionX = None
        self.directionY = None
        self.animal = False
        self.sewRange = 1
        self.sewChance = 10

    def sew(self):
        freeSpaces = []
        for x in range(self.x - self.sewRange, self.x + self.sewRange+1):
            for y in range(self.y - self.sewRange, self.y + self.sewRange+1):
                if(self.world.isInBounds(x, y) and self.world.isFree(x, y)):
                    freeSpaces.append([x, y])

        if(len(freeSpaces) > 0):
            randomIndex = random.randint(0, freeSpaces.__len__() - 1)
            self.world.addOrganism(self.id, self.animal, freeSpaces[randomIndex][0], freeSpaces[randomIndex][1])

    def action(self):
        if(self.alive and random.randint(0, 100) < self.sewChance):
            self.sew()
