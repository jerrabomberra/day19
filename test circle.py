from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.listen()


def circs():
    tim.circle(50, 90)

screen.listen()
screen.onkey(key='a', fun=circs)



screen.exitonclick()