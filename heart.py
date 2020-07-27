# Inspired in https://www.instagram.com/p/CDDV7gxgK_c/

import turtle

FORWARD = 111.65

turtle.bgcolor('black')
turtle.pensize(2)

def curve():
  for i in range(200):
    turtle.right(1)
    turtle.forward(1)

def line():
  for i in range(111):
    turtle.forward(1)

  turtle.forward(0.65)


turtle.hideturtle()

turtle.speed(0)
turtle.color('red', 'pink')

# Left
turtle.begin_fill()
turtle.left(140)
line()

# Top
curve()
turtle.left(120)
curve()

# Right
line()

# End
turtle.end_fill()
turtle.done()
