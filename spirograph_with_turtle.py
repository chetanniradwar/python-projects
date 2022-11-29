import turtle
import random as rnd
t = turtle.Turtle()

t.speed(0)

def draw_circle(radius):
    # move
    t.penup()
    t.right(90)
    t.forward(radius)
    t.left(90)
    t.pendown()

    r = rnd.random()
    g = rnd.random()
    b = rnd.random()
    t.pencolor((r,g,b))
    # circle
    t.circle(radius)

    # move back
    t.penup()
    t.right(-90)
    t.forward(radius)
    t.left(-90)
    t.pendown()

for _ in range(int(360/5)):
    t.penup()
    t.circle(100, 5)
    draw_circle(100)

turtle.exitonclick()