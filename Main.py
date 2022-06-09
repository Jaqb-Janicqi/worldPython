
from world.World import World
from tkinter import *


class Frames(object):
    def game(self, restore):
        newwin = Toplevel(root)
        newwin.focus_set()
        worldSize = None
        newwin.title(f'WORLD')
        #newwin.attributes('-zoomed', True) # fullscreen depending on windows/linux
        newwin.state('zoomed')

        if(restore):
            world = World(10, 1)
            success = world.loadFromFile("save.txt")
            if(not success):
                world = World(20, 1)
                world.populate()
            worldSize = world.getSize()
        else:
            worldSize = int(self.query.get())
            if(worldSize < 10):
                worldSize = 10
            if(worldSize > 30):
                worldSize = 30
            world = World(worldSize, 1)
            world.populate()
            
        humanStrength = StringVar()
        humanStrength.set(str(world.human.getStrength()))
        tileMatrix = [[]*worldSize for i in range(worldSize)]

        @staticmethod
        def left_key(event):
            world.human.setDirectionY(-1)

        @staticmethod
        def right_key(event):
            world.human.setDirectionY(1)

        @staticmethod
        def up_key(event):
            world.human.setDirectionX(-1)

        @staticmethod
        def down_key(event):
            world.human.setDirectionX(1)

        @staticmethod
        def space_key(event):
            world.nextTurn()
            updateTiles()

        newwin.bind('<Left>', left_key)
        newwin.bind('<Right>', right_key)
        newwin.bind('<Up>', up_key)
        newwin.bind('<Down>', down_key)
        newwin.bind('<space>', space_key)

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
                tooltip_win((self.x, self.y))

            def create(self):
                self.button = Button(newwin, text='', command=self.button_command, height=1, width=3)
                self.button.grid(row=self.x, column=self.y)

        # create tiles
        for i in range(worldSize):
            for j in range(worldSize):
                tileMatrix[i].append(Tile(i, j))
                tileMatrix[i][j].create()
        updateTiles()

        def nextTurn():
            world.nextTurn()
            updateTiles()
            updateStrengthDisplay()

        def power():
            world.human.usePotion()
            updateStrengthDisplay()

        def save():
            world.saveToFile("save.txt")

        def load():
            world.loadFromFile("save.txt")
            updateTiles()

        def updateStrengthDisplay():
            humanStrength.set(str(world.human.getStrength()))

        def showEvents():
            events = world.getEvents()
            window = Toplevel(root)
            window.title('Events')
            window.geometry("300x300")
            for i in range(len(events)):
                label = Label(window, text=events[i])
                label.grid(row=i, column=0)

        nextTurnButton = Button(newwin, text="Next turn", command=nextTurn)
        nextTurnButton.grid(row=0, column=1 + worldSize)

        powerButton = Button(newwin, text="Use potion", command=power)
        powerButton.grid(row=1, column=1 + worldSize)

        saveButton = Button(newwin, text="Save", command=save)
        saveButton.grid(row=2, column=1 + worldSize)

        loadButton = Button(newwin, text="Load", command=load)
        loadButton.grid(row=3, column=1 + worldSize)

        showEventsButton = Button(newwin, text="Show events", command=showEvents)
        showEventsButton.grid(row=4, column=1 + worldSize)

        exitButton = Button(newwin, text="Exit", command=root.destroy)
        exitButton.grid(row=5, column=1 + worldSize)

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
                if i == "Human":
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
                newwin.focus_set()

    def mainFrame(self, root):
        self.query = StringVar()

        def newGame():
            self.game(False)
        
        def restoreGame():
            self.game(True)
                
        root.title('Main win')
        root.geometry("300x300")
        root.resizable(0, 0)

        label = Label(root, text='WorldInitializer')
        label.grid(row=0, column=0)

        button1 = Button(root, text="New game", command=newGame)
        button1.grid(row=1, column=1)

        entry1 = Entry(root, textvariable=self.query)
        entry1.grid(row=1, column=0)

        button2 = Button(root, text="Restore game", command=restoreGame)
        button2.grid(row=2, column=1)

if __name__ == "__main__":
    root = Tk()
    app = Frames()
    app.mainFrame(root)
    root.mainloop()