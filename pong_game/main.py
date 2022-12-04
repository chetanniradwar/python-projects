from dice import Dice
from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
import random
import time



screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(1000, 600)
dice = Dice()
left_paddle = Paddle("yellow", "left")
right_paddle = Paddle("green", "right")


left_player_score = ScoreBoard("yellow", "left")
right_player_score = ScoreBoard("green", "right")


start = False
def start_the_game():
    global start
    start_angle = random.randint(0,360)
    if start_angle == 180 or start_angle == 270:
        pass
    dice.setheading(start_angle)
    start = True


screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")

screen.onkeypress(right_paddle.move_up, "i")
screen.onkeypress(right_paddle.move_down, "k")
screen.onkeypress(start_the_game, "space")
# screen.onkeypress(hi, "Up")


screen.listen()


def reset_dice_post():
    dice.home()

dice.speed(0)
while 1:

    screen.update()
    print(start)
    if not start:
        continue
    dice.forward(5)
    dice.reflect_the_dice(left_paddle, right_paddle)

    if dice.dice_missed_left_paddle(left_paddle):
        right_player_score.increment_the_score()
        start = False
        reset_dice_post()
    if dice.dice_missed_right_paddle(right_paddle):
        left_player_score.increment_the_score()
        start = False
        reset_dice_post()
    




screen.exitonclick()
