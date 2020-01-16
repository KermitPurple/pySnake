from coord import coord

def bot_move(fruit, direction, height, width, tail, head):
    #create logic
    if head.x < fruit.x and direction != 'd' and direction != 'a':
        if valid_move(fruit, direction, height, width, tail, head, 'd'):
            return 'd'
    elif head.x > fruit.x and direction != 'd' and direction != 'a':
        if valid_move(fruit, direction, height, width, tail, head, 'a'):
            return 'a'
    elif head.y < fruit.y and direction != 'w' and direction != 's':
        if valid_move(fruit, direction, height, width, tail, head, 's'):
            return 's'
    elif head.y > fruit.y and direction != 'w' and direction != 's':
        if valid_move(fruit, direction, height, width, tail, head, 'w'):
            return 'w'
    else:
        return direction

def valid_move(fruit, direction, height, width, tail, head, potential_direction):
   # if potential_direction == 'w':
   # elif potential_direction == 'a':
   # elif potential_direction == 's':
   # elif potential_direction == 'd':
   # for point in tail:

    return True
