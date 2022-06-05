
import os
import random
from world.organisms.animals.species.Antelope import Antelope
from world.organisms.animals.species.CyberSheep import CyberSheep
from world.organisms.animals.species.Fox import Fox
from world.organisms.animals.species.Human import Human
from world.organisms.animals.species.Sheep import Sheep
from world.organisms.animals.species.Turtle import Turtle
from world.organisms.animals.species.Wolf import Wolf
from world.organisms.plants.species.Grass import Grass
from world.organisms.plants.species.Guarana import Guarana
from world.organisms.plants.species.SosnowskyHogweed import SosnowskyHogweed
from world.organisms.plants.species.SowThistle import SowThistle
from world.organisms.plants.species.Belladona import Belladona  ##from world.organism.plants.species import *


class World:
    def __init__(self, size, spawnProtectSize):
        self.size = size
        self.organisms = []
        self.events = []
        self.human = None
        self.spawnProtectSize = spawnProtectSize

    def getBoard(self):
        matrix = [[0]*self.size for i in range(self.size)]
        for organism in self.organisms:
            if(organism.isAlive()):
                matrix[organism.getx()][organism.gety()] = organism.draw()
        return matrix

    def getEvents(self):
        return self.events

    def isFree(self, x, y):
        if(x < 0 or y < 0 or x >= self.size or y >= self.size):
            return False
        for organism in self.organisms:
            if(organism.getx() == x and organism.gety() == y and organism.alive):
                return False
        return True

    def isFreeFromStronger(self, x, y, strength):
        if(x < 0 or y < 0 or x >= self.size or y >= self.size):
            return False
        for organism in self.organisms:
            if(organism.getx() == x and organism.gety() == y and organism.isAlive() and organism.getStrength() >= strength):
                return False
        return True

    def addOrganism(self, id, animal, x, y):
        newOrganism = None
        if(animal):
            if(id == 9999):
                if (self.human != None):
                    return
                newOrganism = Human(self, x, y)
                self.human = newOrganism
                for x in range(0, self.spawnProtectSize):
                    for y in range(0, self.spawnProtectSize):
                        if(self.isFree(self.human.getx() - x, self.human.gety() - y)):
                            if(self.human.getx() - x > 0 and self.human.gety() - y > 0):
                                if(self.human.getx() - x < self.size and self.human.gety() - y < self.size):
                                    self.addOrganism(1, False, self.human.getx() - x, self.human.gety() - y)
            elif(id == 1):
                newOrganism = Wolf(self, x, y)
            elif(id == 2):
                newOrganism = Sheep(self, x, y)
            elif(id == 3):
                newOrganism = Fox(self, x, y)
            elif(id == 4):
                newOrganism = Turtle(self, x, y)
            elif(id == 5):
                newOrganism = Antelope(self, x, y)
            elif(id == 6):
                newOrganism = CyberSheep(self, x, y)
        else:
            if(id == 1):
                newOrganism = Grass(self, x, y)
            elif(id == 2):
                newOrganism = SowThistle(self, x, y)
            elif(id == 3):
                newOrganism = Guarana(self, x, y)
            elif(id == 4):
                newOrganism = Belladona(self, x, y)
            elif(id == 5):
                newOrganism = SosnowskyHogweed(self, x, y)
        if(newOrganism != None):
            self.organisms.append(newOrganism)
            self.organisms.sort(key=lambda x: x.initiative, reverse=True)

    def addHuman(self, x, y):
        self.addOrganism(9999, True, x, y)

    def addWolf(self, x, y):
        self.addOrganism(1, True, x, y)

    def addSheep(self, x, y):
        self.addOrganism(2, True, x, y)

    def addFox(self, x, y):
        self.addOrganism(3, True, x, y)

    def addTurtle(self, x, y):
        self.addOrganism(4, True, x, y)

    def addAntelope(self, x, y):
        self.addOrganism(5, True, x, y)

    def addCyberSheep(self, x, y):
        self.addOrganism(6, True, x, y)

    def addGrass(self, x, y):
        self.addOrganism(1, False, x, y)

    def addSowThistle(self, x, y):
        self.addOrganism(2, False, x, y)

    def addGuarana(self, x, y):
        self.addOrganism(3, False, x, y)

    def addBelladona(self, x, y):
        self.addOrganism(4, False, x, y)

    def addSosnowskyHogweed(self, x, y):
        self.addOrganism(5, False, x, y)

    def spawnOrganism(self, id, animal):
        x = random.randint(0, self.size - 1)
        y = random.randint(0, self.size - 1)
        while(not self.isFree(x, y)):
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
        self.addOrganism(id, animal, x, y)

    def populate(self):
        for i in range (0, int(self.size/5)):
            self.spawnOrganism(9999, True)      #human
            
            self.spawnOrganism(1, True)       #add animals
            self.spawnOrganism(2, True)
            self.spawnOrganism(3, True)
            self.spawnOrganism(4, True)
            self.spawnOrganism(5, True)
            self.spawnOrganism(6, True)

            self.spawnOrganism(1, False)      #add plants
            self.spawnOrganism(2, False)
            self.spawnOrganism(3, False)
            self.spawnOrganism(4, False)
            self.spawnOrganism(5, False)

    def nextTurn(self):
        self.events.clear()
        for organism in self.organisms:
            if(organism.alive):
                organism.action()

        for organism in self.organisms:
            if(not organism.alive):
                if (organism.id == 9999):
                    self.human = None
                self.organisms.remove(organism)

    def saveToFile(self, fileName):
        file = open(fileName, "w")
        file.write(str(self.size) + "\n")
        file.write(str(self.spawnProtectSize) + "\n")
        for organism in self.organisms:
            if(organism.alive):
                file.write(str(organism.id) + " " + str(organism.animal) + " " + str(organism.x) + " " + str(organism.y) + " " + str(organism.strength) + "\n")
        file.close()

    def loadFromFile(self, fileName):
        if not os.path.isfile(fileName):
            return
        file = open(fileName, "r")
        self.size = int(file.readline())
        self.spawnProtectSize = int(file.readline())
        self.organisms = []
        self.events = []
        self.human = None
        for line in file:
            line = line.split(" ")
            self.addOrganism(int(line[0]), bool(line[1]), int(line[2]), int(line[3]))
            self.organisms[-1].strength = int(line[4])
        file.close()