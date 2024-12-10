from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.goto(x,0)


    def up_paddle(self):
        if self.ycor() < 235:
            new_y=self.ycor()+20
            self.goto(self.xcor(),new_y)

    def down_paddle(self):
        if self.ycor() > -235:
            new_y = self.ycor() -20
            self.goto(self.xcor(), new_y)
