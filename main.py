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

def move(direction):
    if direction == 'w':
        head.y -= 1
        if head.y < 1:
            running = False
    if direction == 'a':
        head.x -= 1
        if head.x < 1:
            running = False
    if direction == 's':
        head.y += 1
        if head.y > height:
            running = False
    if direction == 'd':
        head.x += 1
        if head.x > width:
            running = False


def kbin(previous_direction):
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'w':
            return 'w'
        elif key == b'a':
            return 'a'
        elif key == b's':
            return 's'
        elif key == b'd':
            return 'd'
        else:
            return previous_direction
    else:
        return previous_direction

height = 26
width = 30
head = coord(width / 2, height / 2)

previous_direction = ' '
running = True
print_board()
while running:
    print_head()
    direction = kbin(previous_direction)
    previous_direction = direction
    move(direction)
    time.sleep(0.1)


gotoxy(1, height + 3)
