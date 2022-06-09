
from world.organisms.plants.Plant import Plant

class SosnowskyHogweed(Plant):
    def __init__(self, world, x, y):
        super().__init__(world)
        self.name = "SosnowskyHogweed"
        self.skin = "!"
        self.id = 5
        self.x = x
        self.y = y
        self.prevX = x
        self.prevY = y
        self.strength = 10
        self.baseStrength = 10

    def action(self):
        for organism in self.world.organisms:
            if (organism.isAlive() and organism.isAnimal()):
                if(abs(organism.getx() - self.x) <= 1 and abs(organism.gety() - self.y) <= 1):
                    if(organism.getStrength() < self.strength):
                        organism.kill()
                        self.world.events.append("{} has killed {}".format(self.name, organism.getName()))
