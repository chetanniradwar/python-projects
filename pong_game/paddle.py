from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, color, position):
        super().__init__()
        self.speed(0)
        self.shape("square")
        self.color(color)
        self.penup()
        self.left(90)
        self.shapesize(stretch_len=3, stretch_wid=0.5)

        if position == "left":
            self.goto(-485, 0)
        else:
            self.goto(475, 0)

    def move_up(self):
        
        self.forward(20)

    def move_down(self):
        
        self.backward(20)
        