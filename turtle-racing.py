"""
https://docs.python.org/3/library/turtle.html

"""

import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'pink', 'orange', 'black', 'purple', 'brown', 'cyan', 'yellow']


def get_number_of_racers():
    racers = 0

    while True:
        racers = input('Enter the number of racers (2 - 10): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric. Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2 - 10. Try again!")


def race(colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]




def create_turtles(colors):
    turtles = []
    spasingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spasingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles



def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle racing!")
    screen.bgcolor('lightblue')


racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"Winner is the {winner} turtle!")

time.sleep(5)
