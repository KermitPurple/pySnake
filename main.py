import os, sys
from colorama import init, Fore
init()

class coord:
    def __init__(self, xcoord = 1, ycoord = 1):
        self.x = xcoord
        self.y = ycoord

def gotoxy(x, y):
    sys.stdout.write("\033[%d;%dH" % (y, x))
    sys.stdout.flush()
    
def gotogamexy(x, y):
    #TODO: adjust this for grid once it is made
    gotoxy(x * 2, y)

head = coord()


os.system("cls")
print("test")
gotoxy(head.x, head.y)
print("test")
gotoxy(head.x, head.y)
print("test")
