import turtle

turtle.speed(0)
turtle.shape("turtle")
turtle.pensize(15)
turtle.listen()
tspeed = 10

def left():
    turtle.setheading(180)
    turtle.forward(tspeed)


def right():
    turtle.setheading(0)
    turtle.forward(tspeed)

def down():
    turtle.setheading(270)
    turtle.forward(tspeed)

def up():
    turtle.setheading(90)
    turtle.forward(tspeed)

turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")
turtle.onkeypress(up, "Up")
turtle.onkeypress(down, "Down")
turtle.mainloop()