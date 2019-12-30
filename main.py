import os, sys, time, cursor
from random import randrange
from msvcrt import getch, kbhit
from colorama import init, Fore, Back, Style
init()
cursor.hide()

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
    print(Back.RED + Fore.YELLOW + "00")
    print(Style.RESET_ALL)

def print_tail():
    gotogamexy(tail[0].x, tail[0].y)
    print(Back.RED + Fore.YELLOW + "()")
    print(Style.RESET_ALL)

def delete_tail():
    gotogamexy(tail[-1].x, tail[-1].y)
    print("  ")

def loss():
    if head.y < 1 or head.y > height or head.x < 1 or head.x > width:
            return True
    for point in tail:
        if point.x == head.x and point.y == head.y:
            return True
    return False

def move():
    global length_to_add
    global direction
    tail.insert(0, coord(head.x, head.y))
    if length_to_add != 0:
        length_to_add -= 1
    else:
        _ = tail.pop()
    if direction == 'w':
        head.y -= 1
    if direction == 'a':
        head.x -= 1
    if direction == 's':
        head.y += 1
    if direction == 'd':
        head.x += 1

def kbin():
    global direction
    if kbhit():
        key = getch()
        if key == b'w':
            direction = 'w'
        elif key == b'a':
            direction = 'a'
        elif key == b's':
            direction = 's'
        elif key == b'd':
            direction = 'd'
        elif key == b'q':
            for point in tail:
                print(point.x, ",", point.y)

def detect_coin_collect():
    global coin
    if coin.x == head.x and coin.y == head.y:
        return True
    return False

def new_coin():
    global coin
    coin = coord(randrange(1, width), randrange(1, height))
    gotogamexy(coin.x, coin.y)
    print(Back.GREEN + "  ")
    print(Style.RESET_ALL)

height = 26 # Make these values even or the spawnpoint will not be on a square usable in the game
width = 30 # ^^^^^^^^^^^^^^^^^^^^^
head = coord(width / 2, height / 2)
coin = coord(1, 1)
tail = [coord(head.x, head.y)]
length_to_add = 10
direction = 'a'
score = 0
print_board()
new_coin()
while True:
    print_head()
    print_tail()
    delete_tail()
    kbin()
    move()
    if loss(): break
    if detect_coin_collect(): new_coin()
    time.sleep(0.1)
gotoxy(1, height + 3)
cursor.show()
