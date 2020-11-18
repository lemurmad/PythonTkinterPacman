# Code here for pacman :)
# Ran using the loader to prevent having to always update for easy usage :D
# Pacman in python.
# 16 / 11 / 20

# -----< Modules >-----

# import tkinter as Tk
#import threading as Threading
import sys as Sys

# ---< Variables >---

Grid = [
        "████████████████████████████",
        "█●●●●●●●●●●●●██●●●●●●●●●●●●█",
        "█●████●█████●██●█████●████●█",
        "█■████●█████●██●█████●████■█",
        "█●████●█████●██●█████●████●█",
        "█●●●●●●●●●●●●●●●●●●●●●●●●●●█",
        "█●████●██●████████●██●████●█",
        "█●████●██●████████●██●████●█",
        "█●●●●●●██●●●●██●●●●██●●●●●●█",
        "██████●█████░██░█████●██████",
        "░░░░░█●█████░██░█████●█░░░░░",
        "░░░░░█●██░░░░░░░░░░██●█░░░░░",
        "░░░░░█●██░███▓▓███░██●█░░░░░",
        "██████●██░█░░░░░░█░██●██████",
        "░░░░░░●░░░█░░░░░░█░░░●░░░░░░",
        "██████●██░█░░░░░░█░██●██████",
        "░░░░░█●██░████████░██●█░░░░░",
        "░░░░░█●██░░░░░░░░░░██●█░░░░░",
        "░░░░░█●██░████████░██●█░░░░░",
        "██████●██░████████░██●██████",
        "█●●●●●●●●●●●●██●●●●●●●●●●●●█",
        "█●████●█████●██●█████●████●█",
        "█●████●█████●██●█████●████●█",
        "█●●●██●●●●●●●░░●●●●●●●██●●●█",
        "███●██●██●████████●██●██●███",
        "███●██●██●████████●██●██●███",
        "█●●●●●●██●●●●██●●●●██●●●●●●█",
        "█●██████████●██●██████████●█",
        "█●██████████●██●██████████●█",
        "█●●●●●●●●●●●●●●●●●●●●●●●●●●█",
        "████████████████████████████",
       ]

# █ Wall | ▓ Ghost Door | ● Pellet | ░ Air | ■ Big Pellet

CubeSize = [10, 10]
PelletSize = [10, 10]

# ------< Data >------

Walls = []
Pellets = []
Ghosts = []
BigPellets = []
KeyPressed = [0, 0, 0, 0, 0]    # W, A, S, D, SPACE
PMan = None

print("[TEST]")
"""
# ---< Init Screen >---

Screen = Tk.Tk()
Screen.geometry("200x200")
Screen.config(bg = "black")

# -----< Classes >-----

class Wall():
    def __init__(self, P, C):
        Walls.append(self)
        F = Tk.Frame(Screen, height = CubeSize[0], width = CubeSize[1])
        F.config(bg = "#{0:02x}{1:02x}{2:02x}".format(C[0], C[1], C[2]))
        F.place(x = (P[0] * CubeSize[0]), y = (P[1] * CubeSize[1]))

class Blinky():    # Blinky AI
    Position = [0, 0]
    LastDirection = 0    # 1 Up, 2 Left, 3 Down, 4 Right
    TargetPosition = [0, 0]
    def __init__(self, Position):
        self.Position = Position
    def UpdatePosition(Position):
        self.Position = Position
    def GoTo(self, Why):
        pass    # Why?

class Pacman():
    Position = [0, 0]
    C = None
    def __init__(self, P):
        self.Position = [P[0] * CubeSize[0], P[1] * CubeSize[1]]
        self.C = Tk.Frame(Screen, height = CubeSize[0], width = CubeSize[1])
        self.C.config(bg = "yellow")
        self.C.place(x = self.Position[0], y = self.Position[1])

    def Update(P):
        self.Position = [P[0] * CubeSize[0], P[1] * CubeSize[1]]
        self.C.place(x = self.Position[0], y = self.Position[1])

# ----< Functions >----

def Close():
    Screen.destroy()

def KeyPress(Key):
    Key = Key.char
    if Key == "w":
        KeyPressed[0] = 1
    elif Key == "a":
        KeyPressed[1] = 1
    elif Key == "s":
        KeyPressed[2] = 1
    elif Key == "d":
        KeyPressed[3] = 1
    elif Key == " ":
        KeyPressed[4] = 1

def KeyRelease(Key):
    Key = Key.char
    if Key == "w":
        KeyPressed[0] = 0
    elif Key == "a":
        KeyPressed[1] = 0
    elif Key == "s":
        KeyPressed[2] = 0
    elif Key == "d":
        KeyPressed[3] = 0
    elif Key == " ":
        KeyPressed[4] = 0

def Main():
    global PMan, CubeSize
    
    Screen.geometry("%sx%s" % (len(Grid[0]) * CubeSize[0], len(Grid) * CubeSize[1]))
    Y = 0
    for String in Grid:
        for X in range(0, len(String)):
            if String[X] == "█":
                Wall([X, Y], [0, 0, 255])
        Y += 1

    PMan = Pacman([13.5, 23])

# -------< Main >------

Threading.Thread(target=Main).start()
Screen.protocol("WM_DELETE_WINDOW", Close)
Screen.bind("<KeyPress>", KeyPress)
Screen.bind("<KeyRelease>", KeyRelease)
Screen.mainloop()

# --------< End >-------

print("Closed.")
"""
