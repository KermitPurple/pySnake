import os, sys, time
import msvcrt
from colorama import init, Fore, Back, Style
init()

class coord:
    def __init__(self, xcoord = 1, ycoord = 1):
        self.x = xcoord
        self.y = ycoord

def gotoxy(x, y):
    sys.stdout.write("\033[%d;%dH" % (y, x))
    sys.stdout.flush()
    
def gotogamexy(x, y):
    gotoxy(x * 2 + 1, y + 1)

def print_board():
    os.system("cls")
    for i in range(1, height + 3):
        for j in range(1, width + 3):
            gotoxy(2 * j - 1, i)
            if not((i > 1 and i < height + 2) and (j > 1 and j < width + 2)):
                print(Back.WHITE + "  ")
    print(Style.RESET_ALL)

def print_head():
    gotogamexy(head.x, head.y)
    print(Back.RED + Fore.BLACK + "00")
    print(Style.RESET_ALL)

def kbin():
 if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'w':
            head.y -= 1
            if head.y < 1:
                head.y += 1
        if key == b'a':
            head.x -= 1
            if head.x < 1:
                head.x += 1
        if key == b's':
            head.y += 1
            if head.y > height:
                head.y -= 1
        if key == b'd':
            head.x += 1
            if head.x > width:
                head.x -= 1

height = 26
width = 30
head = coord(width / 2, height / 2)

print_board()
while True:
    print_head()
    kbin()


gotoxy(1, height + 3)
