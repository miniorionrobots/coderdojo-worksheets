import random
import turtle
import time

pokemon = [
    {"name":"Pikachu", "type": "electric"},
    {"name":"Squirtle", "type": "water"},
    {"name":"Charmander", "type": "fire"},
    {"name":"Geodude", "type": "rock"},
    {"name":"Caterpie", "type": "bug"},
    {"name":"Rattata", "type": "normal"},
    ]


turtle.penup()

while True:
    item = random.choice(pokemon)

    turtle.write(
        item["name"],
        align = "center",
        font = ("Arial", 80, "normal")
        )
        
    ans = turtle.textinput("Pokemon", "What type is this Pokemon? ")

    if ans == item["type"]:
        turtle.pencolor("green")
    else:
        turtle.pencolor("red")

    turtle.setheading(-90)
    turtle.forward(100)

    turtle.write(
        item["type"],
        align = "center",
        font = ("Arial", 80, "normal")
        )
    time.sleep(3)
    turtle.clear()
    turtle.goto(0, 0)
    turtle.color("black")
