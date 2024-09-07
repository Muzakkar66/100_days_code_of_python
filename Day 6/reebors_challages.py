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


for jump in range(6):
    one_cycle()