from coord import coord
import queue
from enum import Enum

class State(Enum):
    UNREACHABLE = 1
    REACHABLE = 2
    BLOCKED = 3

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
    for potential_direction in ['w','a','s','d']:
        if valid_move(fruit, direction, height, width, tail, head, potential_direction):
            return potential_direction
    return direction

def path_exists(fruit, direction, height, width, tail, head, potential_direction):
    board = valid_spaces(height, width, tail, head)
    q = queue.Queue()
    potential_head = create_new_pos(head, potential_direction)
    q.put(potential_head)
    board[int(potential_head.y-1)][int(potential_head.x-1)] = State.REACHABLE
    while not q.empty():
        front = q.get()
        for direct in ['w','a','s','d']:
            new_pos = create_new_pos(front, direct)
            if not(new_pos.x < 1 or new_pos.x > width or new_pos.y < 1 or new_pos.y > height or (new_pos.x == head.x and new_pos.y == head.y)):
                if new_pos == fruit:
                    return True
                if board[int(new_pos.y-1)][int(new_pos.x-1)] == State.UNREACHABLE:
                    board[int(new_pos.y-1)][int(new_pos.x-1)] = State.REACHABLE
                    q.put(new_pos)
    return False

def valid_spaces(height, width, tail, head):
    spaces = []
    for i in range(height):
        spaces.append([])
        for j in range(width):
            point = coord(j+1, i+1)
            for tail_point in tail:
                if point.x == tail_point.x and point.y == tail_point.y:
                    spaces[i].append(State.BLOCKED)
                    break
            else:
                spaces[i].append(State.UNREACHABLE)
    return spaces
