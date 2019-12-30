import os, sys, time, cursor
import msvcrt
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
    gotogamexy(tail[length].x, tail[length].y)
    print("  ")

def loss():
    if head.y < 1 or head.y > height or head.x < 1 or head.x > width:
        return True
    return False

def move(direction):
    tail[length].x = head.x
    tail[length].y = head.y
    if direction == 'w':
        head.y -= 1
    if direction == 'a':
        head.x -= 1
    if direction == 's':
        head.y += 1
    if direction == 'd':
        head.x += 1

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
tail = [coord(head.x, head.y)] * 100
length = 0
length_to_add = 0

previous_direction = ' '
print_board()
while True:
    print_tail()
    delete_tail()
    print_head()
    direction = kbin(previous_direction)
    previous_direction = direction
    move(direction)
    if loss(): break
    time.sleep(0.1)


gotoxy(1, height + 3)
cursor.show()
