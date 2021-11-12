#!/usr/bin/env python3
import turtle

# Setup
screen = turtle.Screen()
screen.setup(1024, 768)
turtle.delay(0)

fritz = turtle.Turtle(shape='turtle')
fritz.color('red', 'green')
fritz.speed(1)

# Code
fritz.width(5)
fritz.penup()
fritz.hideturtle()
fritz.goto(0, -300)
fritz.pendown()
fritz.showturtle()

angle = 30


def y(sz, level):
    if level > 0:
        turtle.colormode(255)

        # splitting the rgb range for green
        # into equal intervals for each level
        # setting the colour according
        # to the current level
        fritz.pencolor(0, 255 // level, 0)
        fritz.width(4)

        # drawing the base
        fritz.fd(sz)

        fritz.rt(angle)

        # recursive call for
        # the right subtree
        y(0.8 * sz, level - 1)

        fritz.pencolor(0, 255 // level, 0)

        fritz.lt(2 * angle)

        # recursive call for
        # the left subtree
        y(0.8 * sz, level - 1)

        fritz.pencolor(0, 255 // level, 0)

        fritz.rt(angle)
        fritz.fd(-sz)


fritz.right(-90)
# tree of size 140 and level 12
y(150, 15)

# Loop
turtle.mainloop()
