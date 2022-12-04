from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, color, player):
        super().__init__()
        self.score = 0
        self.color(color)
        self.penup()
        self.hideturtle()


        if player == "left":
            self.goto((-80, 200))
        else:
            self.goto((50, 200))
        
        
        
        self.write(str(self.score), move=False, font=('Arial', 80, 'normal'))

    def increment_the_score(self):
        self.clear()
        self.score = self.score + 1
        self.write(str(self.score), move=False, font=('Arial', 80, 'normal'))
