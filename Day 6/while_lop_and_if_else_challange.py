def turn_right():
    turn_left()
    turn_left()
    turn_left()


def one_cycle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


# hard level in while loop
while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
