# Inspired in https://www.instagram.com/p/CCqMXpuA8Ip/

import turtle

my_turtle = turtle.Turtle()
screen = turtle.Screen()

my_turtle.pensize(2)
my_turtle.speed(0)
my_turtle.hideturtle()

screen.bgcolor("black")

colors = ["red", "magenta", "blue", "cyan", "green", "yellow", "white"]

for i in range(6):
  for color in colors:
    my_turtle.color(color)
    my_turtle.circle(100)
    my_turtle.left(10)

turtle.done()
