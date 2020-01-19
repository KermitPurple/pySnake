from coord import coord

#TODO: create anti box software

def bot_move(fruit, direction, height, width, tail, head):
    if head.x < fruit.x:
        if desirable_move(fruit, direction, height, width, tail, head, 'd'):
            return 'd'
    if head.x > fruit.x:
        if desirable_move(fruit, direction, height, width, tail, head, 'a'):
            return 'a'
    if head.y < fruit.y:
        if desirable_move(fruit, direction, height, width, tail, head, 's'):
            return 's'
    if head.y > fruit.y:
        if desirable_move(fruit, direction, height, width, tail, head, 'w'):
            return 'w'
    if desirable_move(fruit, direction, height, width, tail, head, direction):
        return direction
    else:
        return panic_mode(fruit, direction, height, width, tail, head)

def create_new_pos(head, potential_direction):
    if potential_direction == 'w':
        new_pos = coord(head.x, head.y - 1)
    elif potential_direction == 'a':
        new_pos = coord(head.x - 1, head.y)
    elif potential_direction == 's':
        new_pos = coord(head.x, head.y + 1)
    elif potential_direction == 'd':
        new_pos = coord(head.x + 1, head.y)
    return new_pos

def desirable_move(fruit, direction, height, width, tail, head, potential_direction):
    if valid_move(fruit, direction, height, width, tail, head, potential_direction) and path_exists(fruit, direction, height, width, tail, head, potential_direction):
        return True

def valid_move(fruit, direction, height, width, tail, head, potential_direction):
    new_pos = create_new_pos(head, potential_direction)
    #test for moves
    if new_pos.y > height or new_pos.y < 1 or new_pos.x > width or new_pos.x < 1:
        return False
    for point in tail:
        if new_pos.x == point.x and new_pos.y == point.y:
            return False
    return True

def panic_mode(fruit, direction, height, width, tail, head):
    for potential_direction in ['w','a','s','d']:
        if desirable_move(fruit, direction, height, width, tail, head, potential_direction):
            return potential_direction
    return direction

def path_exists(fruit, direction, height, width, tail, head, potential_direction):
    path_head = create_new_pos(head, potential_direction)
    path = [""]
    first = ''
    while not valid_path(path_head, fruit, first):
        first = path.pop(0)
        for direct in ['w', 'a', 's', 'd']:
            if valid_move(fruit, direction, height, width, tail, path_head, direct):
                path.append(first + direct)
    return True

def valid_path(head, fruit, path):
    pos = coord(head.x, head.y)
    for ch in path:
        if ch == 'w':
            pos.y -= 1
        elif ch == 'a':
            pos.x -= 1
        elif ch == 's':
            pos.y += 1
        elif ch == 'd':
            pos.x += 1
    if int(pos.x) == fruit.x and int(pos.y) == fruit.y:
        return True
    return False
