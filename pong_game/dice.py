from turtle import Turtle
class Dice(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(0.5,0.5)     
    
    def reflect_the_dice(self , left_paddle , right_paddle):
        current_heading = self.heading()
        self.speed(0)
        top_boundary_y = 290
        bottom_boundary_y = -290
        left_paddle_boundary = -485
        right_paddle_boundary = 475
        if self.ycor() >= top_boundary_y:
            self.setheading(360 - current_heading)
        if self.ycor() <= bottom_boundary_y:
            self.setheading(360 - current_heading)

        if self.dice_hits_left_paddle(left_paddle):
            self.setheading(540 - current_heading)
        if self.dice_hits_right_paddle(right_paddle):
            self.setheading(540 - current_heading)


        self.speed(6)

    def dice_hits_left_paddle(self, paddle):
        if self.xcor() <= (paddle.xcor() + 20):
            if (paddle.ycor()+ 20) > self.ycor() > (paddle.ycor() -  20):
                return True
            
        return False

    def dice_hits_right_paddle(self, paddle):
        if self.xcor() >= (paddle.xcor() - 30):
            if (paddle.ycor()+ 20) > self.ycor() > (paddle.ycor() -  20):
                return True
        
        return False

    def dice_missed_left_paddle(self, paddle):
        if self.xcor() < paddle.xcor():
            return True
        return False

    def dice_missed_right_paddle(self, paddle):
        if self.xcor() > paddle.xcor():
            return True
        return False



        
        
        


