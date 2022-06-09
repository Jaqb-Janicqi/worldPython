
from world.organisms.animals.Animal import Animal


class CyberSheep(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Cyber Sheep"
        self.skin = "C"
        self.id = 6
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 11
        self.baseStrength = 11
        self.initiative = 4

    def moveTo(self, x, y):
        if(abs(self.x - x) > abs(self.y - y)):
            self.prevX = self.x
            if(self.x > x):
                self.x -= 1
            else:
                self.x += 1
        else:
            self.prevY = self.y
            if(self.y > y):
                self.y -= 1
            else:
                self.y += 1
        self.checkKraksa()

    def action(self):
        closestWeedPos = None
        closestWeedPos = self.world.findClosestWeed(self.x, self.y)
        if(closestWeedPos != None):
            self.moveTo(closestWeedPos[0], closestWeedPos[1])
            self.world.events.append("{} is tracking Sosnowsky Hogweed at x: {} y: {}".format(self.name, closestWeedPos[0], closestWeedPos[1]))
        else:
            self.world.events.append("{} has no Sosnowsky Hogweed to track".format(self.name))
            self.move()
