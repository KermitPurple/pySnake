import os, sys, time, cursor
from coord import coord
from random import randrange
from msvcrt import getch, kbhit
from colorama import init, Fore, Back, Style
from bot import bot_move
init()
cursor.hide()

def gotoxy(x, y):
    sys.stdout.write("\033[%d;%dH" % (y, x))
    sys.stdout.flush()
    
def gotogamexy(x, y):
    gotoxy(x * 2 + 1, y + 1)

def menu():
    print("1) Play")
    print("2) Bot")
    print("3) Bot V.2")
    print("4) Exit")
    while(True):
        ch = getch()
        if ch == b'1':
            return 0
        elif ch == b'2':
            return 1
        elif ch == b'3':
            return 2
        elif ch == b'4':
            exit()

def print_score():
    global score
    gotoxy(8, height + 3)
    print(score)

def print_board():
    os.system("cls")
    for i in range(1, height + 3):
        for j in range(1, width + 3):
            gotoxy(2 * j - 1, i)
            if not((i > 1 and i < height + 2) and (j > 1 and j < width + 2)):
                print(Back.WHITE + "  ")
    print(Style.RESET_ALL)
    gotoxy(1, height + 3)
    print("Score:")
    print_score()

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

def pause():
    global paused
    paused = not paused

def kbin():
    global direction
    if kbhit():
        key = getch()
        if key == b'w':
            if direction != 's':
                direction = 'w'
        elif key == b'a':
            if direction != 'd':
                direction = 'a'
        elif key == b's':
            if direction != 'w':
                direction = 's'
        elif key == b'd':
            if direction != 'a':
                direction = 'd'
        elif key == b'p':
            pause()
        elif key == b'\xe0': #special key
            key = getch()
            if key == b'H':
                if direction != 's':
                    direction = 'w'
            elif key == b'K':
                if direction != 'd':
                    direction = 'a'
            elif key == b'P':
                if direction != 'w':
                    direction = 's'
            elif key == b'M':
                if direction != 'a':
                    direction = 'd'

def detect_fruit_collect():
    global fruit
    global score
    global length_to_add
    if fruit.x == head.x and fruit.y == head.y:
        score += 1
        length_to_add += 3
        print_score()
        return True
    return False

def new_fruit():
    global fruit
    while True:
        fruit = coord(randrange(1, width), randrange(1, height))
        fruit_in_tail = False
        for point in tail:
            if fruit.x == point.x and fruit.y == point.y:
                fruit_in_tail = True
                break
        if fruit.x == head.x and fruit.y == head.y:
            fruit_in_tail = True
        if not fruit_in_tail: break
    gotogamexy(fruit.x, fruit.y)
    print(Back.GREEN + "  ")
    print(Style.RESET_ALL)

def main():
    global fruit, score, length_to_add, paused, direction, height, width, tail, head
    height = 28 # Make these values even or the spawnpoint will not be on a square usable in the game
    width = 28 # ^^^^^^^^^^^^^^^^^^^^^
    head = coord(width / 2, height / 2)
    fruit = None
    tail = [coord(head.x, head.y)]
    length_to_add = 3
    direction = 'a'
    score = 0
    paused = False
    user = menu()
    if user == 0:
        sleep_frequency = 0.1
    else:
        sleep_frequency = 0.003
    print_board()
    new_fruit()
    while True:
        if user == 0:
            kbin()
        elif user == 1:
            direction = bot_move(fruit, direction, height, width, tail, head)
        elif user == 2:
            direction = bot_move(fruit, direction, height, width, tail, head)
        if not paused:
            print_head()
            print_tail()
            delete_tail()
            move()
            time.sleep(sleep_frequency)
            if loss(): break
            if detect_fruit_collect(): new_fruit()
    gotoxy(1, height + 3)
    cursor.show()

if __name__ == "__main__":
    main()
