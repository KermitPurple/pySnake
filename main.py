import os
from colorama import init, Fore
init()

class coord:
    def __init__(self, xcoord, ycoord):
        self.x = xcoord
        self.y = ycoord

def gotoxy(x, y):
    print("\033[%d;%dH" % (y, x))


head = coord(9,5)

os.system("cls")
print("test")
gotoxy(head.x, head.y)
print("test")
