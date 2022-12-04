from dice import Dice
from turtle import Screen
from paddle import Paddle
import random
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(1000, 600)
dice = Dice()
left_paddle = Paddle("yellow", "left")
right_paddle = Paddle("green", "right")



screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

screen.onkeypress(right_paddle.move_up, "i")
screen.onkeypress(right_paddle.move_down, "k")
# screen.onkeypress(hi, "Up")
screen.listen()

start_angle = random.randint(0,360)
if start_angle == 180 or start_angle == 270:
    pass
dice.setheading(start_angle)

dice.speed(0)
while 1:
    
    screen.update()
    dice.forward(5)
    dice.reflect_the_dice(left_paddle, right_paddle)
    
   



screen.exitonclick()
