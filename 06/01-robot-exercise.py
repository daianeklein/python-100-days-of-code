#https://www.udemy.com/course/100-days-of-code/learn/lecture/19115132#questions

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def turn_down():
    turn_left()
    turn_left()
    turn_left()
    move()
    
def move_robot():
    for i in range(0, 6):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_down()
        turn_left()

move_robot()
