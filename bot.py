from coord import coord

def bot_move(fruit, direction, height, width, tail, head):
    #create logic
    if head.x < fruit.x:
        if valid_move(fruit, direction, height, width, tail, head, 'd'):
            return 'd'
    if head.x > fruit.x:
        if valid_move(fruit, direction, height, width, tail, head, 'a'):
            return 'a'
    if head.y < fruit.y:
        if valid_move(fruit, direction, height, width, tail, head, 's'):
            return 's'
    if head.y > fruit.y:
        if valid_move(fruit, direction, height, width, tail, head, 'w'):
            return 'w'
    else:
        if valid_move(fruit, direction, height, width, tail, head, 'w'):
            return direction
        else:
            panic_mode(fruit, direction, height, width, tail, head)


def valid_move(fruit, direction, height, width, tail, head, potential_direction):
    if potential_direction == 'w':
        new_pos = coord(head.x, head.y - 1)
    elif potential_direction == 'a':
        new_pos = coord(head.x - 1, head.y)
    elif potential_direction == 's':
        new_pos = coord(head.x, head.y + 1)
    elif potential_direction == 'd':
        new_pos = coord(head.x + 1, head.y)
    if new_pos.y > height or new_pos.y <= 1 or new_pos.x > width or new_pos.y <= 1:
        return False
    for point in tail:
        if new_pos.x == point.x and new_pos.y == point.y:
            return False
    return True

def panic_mode(fruit, direction, height, width, tail, head):
    pass
