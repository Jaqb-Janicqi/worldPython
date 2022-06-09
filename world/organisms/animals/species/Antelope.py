
import random
from world.organisms.animals.Animal import Animal


class Antelope(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Antelope"
        self.skin = "A"
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 4
        self.baseStrength = 4
        self.initiative = 4
        self.id = 5

    def move(self):
        if(random.random() < 0.5):
            moveRange = 1
        else:
            moveRange = 2

        if(random.random() < 0.5):
            if(random.random() < 0.5):
                if(self.world.isInBounds(self.x + moveRange, self.y)):
                    self.x += moveRange
                else:
                    self.x -= moveRange
            else:
                if(self.world.isInBounds(self.x - moveRange, self.y)):
                    self.x -= moveRange
                else:
                    self.x += moveRange
        else:
            if(random.random() < 0.5):
                if(self.world.isInBounds(self.x, self.y + moveRange)):
                    self.y += moveRange
                else:
                    self.y -= moveRange
            else:
                if(self.world.isInBounds(self.x, self.y - moveRange)):
                    self.y -= moveRange
                else:
                    self.y += moveRange
        self.checkKraksa()

    def collision(self, organism):
        if(self.id == organism.getId() and self.animal == organism.isAnimal()):
            self.spawnNewOrganism(self, organism, self.world)
            return
        if(random.random() < 0.5):
            self.kill()
            self.world.events.append("{} died to {}".format(self.name, organism.getName()))
            return
        if(random.random() < 0.5):
            moveRange = 1
        else:
            moveRange = 2
        
        freeSpaces = []
        for x in range(self.x - moveRange, self.x + moveRange+1):
            for y in range(self.y - moveRange, self.y + moveRange+1):
                if(self.world.isInBounds(x, y) and self.world.isFreeFromStronger(x, y)):
                    if(x != y):
                        freeSpaces.append([x, y])

        if(len(freeSpaces) > 0):
            randomIndex = random.randint(0, freeSpaces.__len__() - 1)
            self.prevX = self.x
            self.prevY = self.y
            self.x = freeSpaces[randomIndex][0]
            self.y = freeSpaces[randomIndex][1]
            self.world.events.append("{} escaped from {}".format(self.name, organism.getName()))
        else:
            self.kill()
            self.world.events.append("{} died to {}".format(self.name, organism.getName()))