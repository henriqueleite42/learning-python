# Inspired in https://www.instagram.com/p/CC00H2Rgbjx/

import turtle
import time

my_turtle = turtle.Turtle()

my_turtle.pencolor('red')
my_turtle.pensize(5)

number_of_vertices = 3 # Start from Triangule

while number_of_vertices < 11: # Limit to a decagon
  my_turtle.clear()
  my_turtle.hideturtle()

  for i in range(number_of_vertices):
    my_turtle.forward(60)
    my_turtle.right(360 / number_of_vertices)

  number_of_vertices = number_of_vertices + 1

  my_turtle.penup()
  my_turtle.home()
  my_turtle.pendown()
  my_turtle.penup()
  my_turtle.home()
  my_turtle.pendown()
  my_turtle.ht()
  time.sleep(1)
  my_turtle.st()
