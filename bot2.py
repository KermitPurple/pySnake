from coord import coord

def bot_move(fruit, direction, height, width, tail, head):
    if head.x == 1:
        if head.y == 1:
            return 'd'
        return 'w'
    elif head.x == width:
        if head.y == height:
            return 'a'
        return 's'
    elif head.y == 1:
        return 'd'
    elif head.y == 2:
        if head.x % 2 == 1:
            return 'a'
        return 's'
    elif head.y == height:
        if head.x % 2 == 1:
            return 'w'
        return 'a'
    elif head.x % 2 == 1:
        return 'w'
    return 's'
