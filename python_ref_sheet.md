# <div align = "center"> Python Ref Sheet
## General
| Command | Effect |
| ----------- | ----------- |
|`var = 1`|Create a variable called "var" with a value of 1|
|`list = []`|Create a list called "list"|
|`{"name": "Pheobe"}`|Create a dictionary correponding "name" to "Pheobe"|
|`while True:`|Create a loop that runs forever|
## Turtle
| Command | Effect |
| ----------- | ----------- |
|`import turtle`|Import Turtle into Python 3|
|`t = turtle.Turtle()`|Make a turtle called "t"|
|`turtle.tracer(0, 0)`|Turns off tracer animation - makes the turtle very fast|
|`turtle.done()`|Program finished, wait for window to close|
|`turtle.update()`|Make a screen update - handy when the turtle is fast|
|`turtle.clear`|Clear everything made by this turtle|
|`turtle.speed(0)`|Make this turtle fast|
|`turtle.penup()`|Pull the pen up - You stop drawing|
|`turtle.pendown()`|Put the pen down - You start drawing|
|`turtle.hideturtle()`|Hide your turtle|
|`turtle.showturtle()`|Show your turtle|
|`turtle.goto(x, y)`|Jump to position x, y. 0, 0 is the middle of the screen|
|`turtle.stamp()`|Stamp the colour turtle shape|
|`turtle.shape(“shape”)`|Set shape. Try “turtle”, “circle” or “square”|
|`turtle.shapesize(0, 1)`|Set the size of the shape|
|`turtle.color(“color”)`|Set colour. Don’t forget it’s the American spelling of colour. Try “red”, “green” or “blue”|
|`turtle.forward(100)`|Go forward 100 pixels|
|`turtle.left(90)`|Turn left 90 degrees|
|`turtle.right(45)`|Turn right 45 degrees|
|`turtle.bgcolor(“color”)`|Set screen background colour. Don’t forget it’s the American spelling of colour. Try “red”, “green” or “blue”|
|`turtle.window_height()`|Get the height of the window|
|`turtle.window_width()`|Get the width of the window|
|`turtle.setheading(90)`|Set the direction to 90 degrees
|`turtle.listen()`|Listens for overall input (EG: on key)
|`turtle.onkey(func, “Left”)`|If the “Left” arrow key, call func|
|`turtle.onscreenclick(func, 1)`|When left (Replace 1 with 2 or 3 for middle and right buttons respectively) mouse button clicked, call func|
|`turtle.write(arg, move, align, font)`|Arg = Text, Alignment, Font = fontname, fontsize, fonttype”|
|`turtle.textinput(name, input)`|name = name of the window, input = the question”|
## Random
| Command | Effect |
| ----------- | ----------- |
|`Import random`|Import random into Python 3|
|`random.randint(min, max)`|Get a random from min to max|
|`random.choice(list)`|Get a random item from a list|
|`list(range(6))`| Get a list from 0 to 5|
|`list(range(2, 10))`|Get a list from 2 to 9|
|`list(range(2, 10, 2))`|Get a list from 2 to 9 going up in 2s|
|`list(enumerate(range(2, 10)))`|Get a list from 2 to 9 numbered by index|
## Time
| Command | Effect |
| ----------- | ----------- |
|`Import time`|Import time into Python 3|
|`time.sleep(1)`|Get the program to wait for 1 second|