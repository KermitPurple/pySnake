import os
from colorama import init, Fore

init()

def gotoxy(x, y):
    print("\033[%d;%dH" % (y, x))



os.system("cls")
print("test")
gotoxy(9,9)
print("test")
