
from world.organisms.animals.Animal import Animal
import math


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

    def findWeeds(self):
        closestWeed = None
        closestDistance = None

        for organism in self.world.organisms:
            if(organism.getId() == 5 and not organism.isAnimal() and organism.isAlive()):
                p1 = [self.x, self.y]
                p2 = [organism.getx(), organism.gety()]
                if(closestWeed == None):
                    closestDistance = math.dist(p1, p2)
                    closestWeed = organism
                else:
                    if(math.dist(p1, p2) < closestDistance):
                        closestDistance = math.dist(p1, p2)
                        closestWeed = organism
        return closestWeed

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
        closestWeed = self.findWeeds()
        if(closestWeed != None):
            self.moveTo(closestWeed.getx(), closestWeed.gety())
            self.world.events.append("{} is tracking Sosnowsky Hogweed".format(self.name))
        else:
            self.world.events.append("{} has no Sosnowsky Hogweed to track".format(self.name))
            self.move()
