from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.fillcolor("white")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=1)
        self.x_move=10
        self.y_move=10
        self.move_speed=0.06


    def move_ball(self):

        xcor=self.xcor()+self.x_move
        ycor=self.ycor()+self.y_move
        self.goto(xcor,ycor)

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed=0.06
        self.bounce_x()

    def bounce_y(self):
        self.y_move*=-1

    def bounce_x(self):
        self.x_move*=-1
        self.move_speed*=0.9
