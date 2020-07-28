# Inspired in https://www.instagram.com/p/CDJtShLgAp7/

import turtle

my_turtle = turtle.Turtle()

my_turtle.hideturtle()
my_turtle.screen.bgcolor('orange')
my_turtle.screen.title('Fractal Tree')
my_turtle.left(90)
my_turtle.speed(200)
my_turtle.color('white')
my_turtle.pensize(5)

def draw_fractal(blen):
  if blen < 10:
    return
  else:
    my_turtle.forward(blen)
    my_turtle.left(30)
    draw_fractal((3 * blen) / 4)

    my_turtle.right(60)
    draw_fractal((3 * blen) / 4)

    my_turtle.left(30)
    my_turtle.backward(blen)

draw_fractal(80)
turtle.done()
