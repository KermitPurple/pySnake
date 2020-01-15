def bot_move(fruit, direction, height, width, tail, head):
    #create logic
    if head.y >= height and direction != 'a':
        return 'a'
    elif head.y <= 1 and direction != 'd':
        return 'd'
    elif head.x >= width and direction != 's':
        return 's'
    elif head.x <= 1 and direction != 'w':
        return 'w'
    else:
        return direction
