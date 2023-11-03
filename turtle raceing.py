import colorgram
import turtle as t
from turtle import Screen
from turtle import Turtle
import random

HEIGHT = 500
WIDTH =  500

t.colormode(255)
tim = Turtle()


def get_num_racers():
    racers = input("Enter the number of turtles to race (2-10): ")
    while True:
        if racers.isdigit():
            racers = int(racers)
            if 2 <= racers <= 10:
                return racers
            else:
                print("Value not suitable for race track.")
                continue
        else:
            print("Please enter a numeric value between 2 and 10")

racers = get_num_racers()
print(racers)


def screen_setup():
    screen = Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title("Turtle Racing!!!")



# screen.exitonclick()