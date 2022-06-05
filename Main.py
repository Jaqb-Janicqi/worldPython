
from cgitb import text
import tkinter
# import pygame
from world.World import World
import tkinter as tk
from tkinter import *


class Frames(object):
    
    def newFrame(self):
        newwin = Toplevel(root)
        worldSize = int(self.query.get())
        newwin.title(f'size: {worldSize}')
        size = 200*self.query.get()
        newwin.geometry(f"{100+int(size)}x{size}")
        world = World(worldSize, 2)
        world.populate()
        tileMatrix = [[]*worldSize for i in range(worldSize)]

        def updateTiles():
            board = world.getBoard()
            for i in range(worldSize):
                for j in range(worldSize):
                    if board[i][j] != 0:
                        tileMatrix[i][j].button['text']=board[i][j]
                    else:
                        tileMatrix[i][j].button['text']=''

        # navigate to choose organism tooltip window
        def tooltip_win(pos):
            chooseOrganism(pos[0], pos[1], world)

        root.withdraw()  # hide main menu
        position_log = []

        class Tile:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def button_command(self):
                # allows only one tooltip at the time (per tile)
                if position_log.count((self.x, self.y)) < 1:
                    tooltip_win((self.x, self.y))
                    position_log.append((self.x, self.y))

                print(position_log.count((self.x, self.y)))

            def create(self):
                self.button = Button(newwin, text='', command=self.button_command, height=1, width=3)
                self.button.grid(row=self.x, column=self.y)

        # create tiles
        for i in range(worldSize):
            for j in range(worldSize):
                tileMatrix[i].append(Tile(i, j))
                tileMatrix[i][j].create()
        updateTiles()

        def chooseOrganism(x, y, world):
            choose = Toplevel(root)
            choose.geometry('200x400')
            choose.title('Choose organism:')
            names = ['Human', 'Antelope', 'Fox', 'Sheep', 'Turtle', 'Wolf',
                    'Belladona', 'Grass', 'Guarana', 'Sosnowsky Weed', 'Sow Thistle', 'Cyber Sheep']
            for i in range(len(names)):
                button = Button(choose, text=names[i], command=lambda i=names[i]: byName(i))
                button.grid(row=i, column=0)

            def byName(i):
                if i == "Humman":
                    world.addHuman(x, y)
                elif i == "Antelope":
                    world.addAntelope(x, y)
                elif i == "Fox":
                    world.addFox(x, y)
                elif i == "Sheep":
                    world.addSheep(x, y)
                elif i == "Turtle":
                    world.addTurtle(x, y)
                elif i == "Wolf":
                    world.addWolf(x, y)
                elif i == "Belladona":
                    world.addBelladona(x, y)
                elif i == "Grass":
                    world.addGrass(x, y)
                elif i == "Guarana":
                    world.addGuarana(x, y)
                elif i == "Sosnowsky Weed":
                    world.addSosnowskyHogweed(x, y)
                elif i == "Sow Thistle":
                    world.addSowThistle(x, y)
                elif i == "Cyber Sheep":
                    world.addCyberSheep(x, y)            
                choose.destroy()
                updateTiles()

    def mainFrame(self, root):
        self.query = StringVar()  # passing parameter via query var

        def click():
            if len(self.query.get()) == 0:
                print('error')
            else:
                self.newFrame()
                
        root.title('Main win')
        root.geometry("300x300")
        root.resizable(0, 0)

        label = Label(root, text='WorldInitializer')
        label.grid(row=0, column=0)

        button1 = Button(root, text="New game", command=click)
        button1.grid(row=1, column=1)

        entry1 = Entry(root, textvariable=self.query)
        entry1.grid(row=1, column=0)

        button2 = Button(root, text="Restore game", command=click)
        button2.grid(row=2, column=1)


if __name__ == "__main__":
    root = Tk()
    app = Frames()
    app.mainFrame(root)
    root.mainloop()


# world = World(20, 2)
# world.addHuman(5, 5)
# world.human.usePotion()
# world.saveToFile("test3.txt")


# masz dostępne:
#     world = World(WorldSize, spawnProtectSize)    WorldSize musi być ustalany w oknie przed rozpoczęciem gry, spawnprot zostaw 2 i es
#     world.nextTurn()
#     world.saveToFile("saveFile.txt")
#     world.loadFromFile("saveFile.txt")
#     world.populate()                  przy odpaleniu nowej gry trzeba odpalić żeby jakieś organizmy tam były
#     world.addOrganism()
#     world.events                      lista eventów, możesz wyświetalć gdzieś w oknie np 5 ostatnich albo tak jak ja w java
#                                           że nowe okno z całą listą i elo

#     strzałkami klawiatury można ustalić kierunek ruchu         po odpaleniu nowej tury ziom juz sam sobie bedzie chodził
#     world.human.setDirectionX(INT)
#     world.human.setDirectionY(INT)
#     world.human.usePotion()

#     klikając na daną komórkę świata można dodać organizm (tak jak w javie, że lista się pokazuje)
#     masz do tego w world funkcje:
#     addHuman(x, y)
#     addWolf(x, y)
#     addSheep(x, y)
#     addFox(x, y)
#     addTurtle(x, y)
#     addAntelope(x, y)
#     addCyberSheep(x, y)
#     addGrass(x, y)
#     addSowThistle(x, y)
#     addGuarana(x, y)
#     addBelladona(x, y)
#     addSosnowskyHogweed(x, y)
