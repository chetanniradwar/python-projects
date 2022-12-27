from turtle import Turtle
from turtle import Screen
import random
import time

start_game = False


def start_the_game():
    global start_game
    start_game = True


# screen setup
game_screen = Screen()
game_screen.setup(600, 600)
game_screen.screensize(200, 200, "black")
game_screen.title("THE SNAKE GAME")
game_screen.tracer(0)

# snake head setup
head = Turtle()
head.shape("square")
head.shapesize(0.5, 0.5, 0)
head.color("white")
head.penup()
head.pensize(11)
head.speed(1)

#snake body setup
body1 = head.clone()
body2 = head.clone()
body_list = [body1, body2]

body1.setposition((head.xcor() - 11, head.ycor()))
body2.setposition((head.xcor() - 2 * 11, head.ycor()))


def calculate_food_pos():
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    return (x, y)


# snake food setup
food = Turtle()
food.color("red")
food.shape("square")
food.shapesize(0.5, 0.5, 0.5)
food.speed(0)
food.penup()
food_pos = calculate_food_pos()
food.setposition(food_pos)


def does_wall_cross(xcor, ycor, screen):
    if (xcor >= (screen.window_width() / 2 - 5)
            or xcor <= -(screen.window_width() / 2 + 5)):
        return True
    if (ycor >= (screen.window_height() / 2 - 5)
            or ycor <= -(screen.window_height() / 2 + 5)):
        return True

    return False


def move_left():
    if int(head.heading()) == 0:
        return

    if int(head.heading()) != 180:
        head.speed(0)
        head.setheading(180)
        head.speed(1)


def move_right():
    if int(head.heading()) == 180:
        return
    if int(head.heading()) != 0:
        head.speed(0)
        head.setheading(0)
        head.speed(1)


def move_up():

    if int(head.heading()) == 270:
        return
    if int(head.heading()) != 90:
        head.speed(0)
        head.setheading(90)
        head.speed(1)


def move_down():
    if int(head.heading()) == 90:
        return
    if int(head.heading()) != 270:
        head.speed(0)
        head.setheading(270)
        head.speed(1)


# key press capture
game_screen.onkeypress(move_left, "Left")
game_screen.onkeypress(move_right, "Right")
game_screen.onkeypress(move_up, "Up")
game_screen.onkeypress(move_down, "Down")
game_screen.onkeypress(start_the_game, "space")
game_screen.listen()

score = 0
not_game_over = True

# main loop
while not_game_over:  
    game_screen.update()

    if start_game is False:
        continue

    empty_pos = head.pos()
    head.forward(10)

    # check if snake head crossed wall or not
    if does_wall_cross(head.xcor(), head.ycor(), game_screen):
        print("GAME OVER")
        print(f"YOUR SCORE IS {score}")
        not_game_over = False
        break

    # check if snake crossed his own body
    for body in body_list:
        if head.pos() == body.pos():
            print("GAME OVER")
            print(f"YOUR SCORE IS {score}")
            not_game_over = False
            break

    # all body should follow the head
    for body in body_list:
        to_be_empty = body.pos()
        body.setpos(empty_pos)
        empty_pos = to_be_empty

    # increase the score by 1
    # increase the snake body length
    # setup the new random position of the food
    # after food is eaten
    if (food_pos[0] + 11)  >= int(head.pos()[0]) >= (food_pos[0] - 11) and \
        (food_pos[1] + 11) >= int(head.pos()[1]) >= (food_pos[1] - 11):
        score += 1
        food_pos = calculate_food_pos()
        food.setposition(food_pos)
        new_body = head.clone()
        last_body = body_list[len(body_list) - 1]
        new_body.setpos(last_body.xcor() - 11, last_body.ycor())
        body_list.append(new_body)

game_screen.exitonclick()
