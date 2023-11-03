import colorgram
import turtle 
import random
import time

HEIGHT = 600
WIDTH =  600
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
    # screen.exitonclick()

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x,y = racer.pos()
            if y >= HEIGHT // 2 -10:
                return colors[turtles.index(racer)]

            
def create_turtles(colors):
    """ make and set the turtles"""
    turtles = []
    spacing = WIDTH // (len(colors) +1)
    for i, color in enumerate(colors):
        racer=turtle.Turtle()    
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) *spacing, -HEIGHT//2 +20)
        racer.pendown()
        turtles.append(racer)
    return turtles




racers = get_num_racers()
init_screen()
   
colors = COLORS[:racers]

winner =race(colors)
print(f"The winner is the turtle colored '{winner}'.")
time.sleep(5)

