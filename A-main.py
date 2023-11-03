from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(25)

def move_backwards():
    tim.backward(25)

def clockwise():
    tim.circle(25,-90)

def anti_clockwise():
    tim.circle(25,90)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

"""
w - forwards
s - backwards
a - counter clockwise curve
d - clockwise circle curve
c- clear 
"""




screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clockwise)
screen.onkey(key="d", fun=anti_clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
