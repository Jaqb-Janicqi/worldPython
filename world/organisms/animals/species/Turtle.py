
import random
from world.organisms.animals.Animal import Animal


class Turtle(Animal):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "Turtle"
        self.skin = "T"
        self.id = 4
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 2
        self.baseStrength = 2
        self.initiative = 1

    def action(self):
        if(self.alive and random.random() < 0.25):
            self.move()
        else:
            self.notMoved()

    def collision(self, organism):
        if(self.id == organism.getId() and self.animal == organism.isAnimal()):
            self.spawnNewOrganism(self)
        else:
            if(5 > organism.getStrength()):
                organism.moveBack()
                self.world.addEvent("{} reflected attack of {}".format(self.name, organism.getName()))
            else:
                self.kill()
                self.world.addEvent("{} died to {}".format(self.name, organism.getName()))
