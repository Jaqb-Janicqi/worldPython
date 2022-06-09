
from world.organisms.animals.Animal import Animal


class Human(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.id = 9999
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 5
        self.baseStrength = 5
        self.initiative = 4
        self.alive = True
        self.skin = "H"
        self.name = "Human"
        self.directionX = 0
        self.directionY = 0

    def setDirectionX(self, directionX):
        self.directionX = directionX
        self.directionY = 0

    def setDirectionY(self, directionY):
        self.directionY = directionY
        self.directionX = 0

    def usePotion(self):
        self.strength = 10
        self.world.events.append("{} has used a potion".format(self.name))

    def getStrength(self):
        return self.strength

    def action(self):
        if(self.strength == self.baseStrength):
            self.world.events.append("{} has a potion".format(self.name))
        else:
            self.strength -= 1
        self.world.events.append("{} has {} strength".format(self.name, self.strength))
        if(self.x + self.directionX < 0 or self.x + self.directionX >= self.world.size or self.y + self.directionY < 0 or self.y + self.directionY >= self.world.size):
            self.directionX = self.directionX*-1
            self.directionY = self.directionY*-1
            self.x += self.directionX
            self.y += self.directionY
            self.world.events.append("{} has no way forwards and is going backwards".format(self.name))
        else:
            self.x += self.directionX
            self.y += self.directionY
            self.world.events.append("{} has moved to x:{} y:{}".format(self.name, self.x, self.y))
        self.checkKraksa()
