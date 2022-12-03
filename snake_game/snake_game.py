from turtle import Turtle
from turtle import Screen
import random
game_screen = Screen()

game_screen.setup(600, 600)
game_screen.screensize(200, 200, "black")
game_screen.title("THE SNAKE GAME")

game_screen.tracer(0)

def calculate_prey_pos():
    x = random.randint(-150, 150)
    y = random.randint(-150, 150)
    return (x, y)

head = Turtle()
head.shape("square")

head.shapesize(0.5, 0.5, 0)
head.color("white")
head.penup()
head.pensize(11)

body1 = head.clone()

body2 = head.clone()

body_list = [body1, body2]
body1.setposition((head.xcor() - 11, head.ycor()))
body2.setposition((head.xcor() - 2 * 11, head.ycor()))
food = Turtle()
food.color("red")
food.shape("square")
food.shapesize(0.5,0.5,0.5)
food.speed(0)
food.penup()

pre_pos = calculate_prey_pos()

food.setposition(pre_pos)

print(game_screen.window_height() , game_screen.window_width())

def does_wall_cross(xcor, ycor, screen):
    if (xcor >= (screen.window_width() / 2 - 5) or xcor <= -(screen.window_width()/2 + 5)):
        return True
    if(ycor >= (screen.window_height() / 2 - 5) or ycor <= -(screen.window_height()/2 + 5)):
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
    


  
game_screen.onkeypress(move_left, "Left")
game_screen.onkeypress(move_right, "Right")
game_screen.onkeypress(move_up, "Up")
game_screen.onkeypress(move_down, "Down")
game_screen.listen()

head.speed(1)
score = 0 
not_game_over = True
while not_game_over:
    game_screen.update()
    empty_pos = head.pos()
    head.forward(10)

    if does_wall_cross(head.xcor(), head.ycor(), game_screen):
        print("GAME OVER")
        not_game_over = False
        print(head.xcor(), head.ycor(),game_screen.window_width(), game_screen.window_height())
        break

    for body in body_list:
        if head.pos() == body.pos():
            print("GAME OVER")
            not_game_over = False
            break
    

    for body in body_list:
        to_be_empty = body.pos()
        body.setpos(empty_pos)
        empty_pos = to_be_empty
    
    
    if (pre_pos[0] + 11)  >= int(head.pos()[0]) >= (pre_pos[0] - 11) and \
        (pre_pos[1] + 11) >= int(head.pos()[1]) >= (pre_pos[1] - 11):
        score+=1
        pre_pos = calculate_prey_pos()
        food.setposition(pre_pos)
        new_body = head.clone()
        last_body = body_list[len(body_list)-1]
        new_body.setpos(last_body.xcor() - 11 , last_body.ycor())
        body_list.append(new_body)



game_screen.exitonclick()
