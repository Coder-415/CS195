#Write a program one statement long that displays the curvature of a sinusoid on the terminal

from turtle import Turtle, Screen
from math import pi, sin as sine

screen = Screen()
screen.setworldcoordinates(0, -1.25, 2 * pi, 1.25)

turtle = Turtle()

angle = 0

while angle < 2 * pi:
    turtle.goto(angle, sine(angle))
    angle += 0.1

