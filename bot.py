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
    spaces = valid_spaces(height, width, tail, head)
    return True

def valid_spaces(height, width, tail, head):
    spaces = []
    for i in range(height):
        for j in range(width):
            valid_spot = True
            point = coord(j+1, i+1)
            if point.x < 1 or point.x > width or point.y < 1 or point.y > height or (point.x == head.x and point.y == head.y):
                valid_spot = False
            else:
                for tail_point in tail:
                    if point.x == tail_point.x and point.y == tail_point.y:
                        valid_spot = False
                        break
            if valid_spot:
                spaces.append(point)
