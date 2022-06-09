
import random
from world.organisms.Organism import Organism


class Animal(Organism):
    def __init__(self, world):
        super().__init__(world)
        self.animal = True

    def checkKraksa(self):
        for organism in self.world.organisms:
            if(organism.getx() == self.x and organism.gety() == self.y):
                if(organism != self):
                    organism.collision(self)
                    if(not self.alive):
                        return

    def move(self):
        if(random.random() < 0.5):
            if(random.random() < 0.5):
                if(self.world.isInBounds(self.x + 1, self.y)):
                    self.x += 1
                else:
                    self.x -= 1
            else:
                if(self.world.isInBounds(self.x - 1, self.y)):
                    self.x -= 1
                else:
                    self.x += 1
        else:
            if(random.random() < 0.5):
                if(self.world.isInBounds(self.x, self.y + 1)):
                    self.y += 1
                else:
                    self.y -= 1
            else:
                if(self.world.isInBounds(self.x, self.y - 1)):
                    self.y -= 1
                else:
                    self.y += 1
        self.checkKraksa()

    def action(self):
        if(self.alive):
            self.move()
