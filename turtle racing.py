import colorgram
import turtle 
import random
import time

HEIGHT = 500
WIDTH =  500
COLORS= ['red', 'black','green','blue', 'yellow','purple', 'pink','cyan','orange', 'cyan',
          "CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray"]

random.shuffle(COLORS)


def get_num_racers():
    """gets user input for the number of racers"""
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



def init_screen():
    """sets up screen size based on height and width above"""
    screen = turtle.Screen()
    screen.setup(HEIGHT,WIDTH)
    screen.title("Turtle Racing!!!")

colors = COLORS[:racers]

def create_turtles(colors):
    turtles = []
    spacing = WIDTH / (len(colors) +1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()    
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos()
        racer.pendown()
        turtles.append(racer)


racers = get_num_racers()
init_screen()
create_turtles(colors)       

print(spacing)
    

# screen.exitonclick()