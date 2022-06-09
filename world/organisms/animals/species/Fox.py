
import random
from world.organisms.animals.Animal import Animal


class Fox(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Fox"
        self.skin = "F"
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 3
        self.baseStrength = 3
        self.initiative = 7
        self.id = 3

    def move(self):
        freeSpaces = []
        for x in range(self.x - 1, self.x + 1):
            for y in range(self.y - 1, self.y + 1):
                if(self.world.isInBounds(x, y) and self.world.isFreeFromStronger(x, y, self.strength)):
                    if(x != y):
                        freeSpaces.append([x, y])

        if(len(freeSpaces) > 0):
            randomIndex = random.randint(0, freeSpaces.__len__() - 1)
            self.prevX = self.x
            self.prevY = self.y
            self.x = freeSpaces[randomIndex][0]
            self.y = freeSpaces[randomIndex][1]
            self.checkKraksa()