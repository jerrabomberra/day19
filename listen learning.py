import colorgram
from turtle import Turtle, Screen
import turtle as t

import turtle 
import random

t.colormode(255)
tim = Turtle()
screen = Screen()
screen.setup(width=600, height=600)

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)


tim.fd(100)
turtle.listen()

screen.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# tim.mainloop()


screen.exitonclick()
