from turtle import Turtle
ALIGNMENT='center'
FONT=('Courier',20,'bold')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0,270)
        self.right_score=0
        self.left_score=0

        self.update_score()


    def update_score(self):
        self.write(f"Score: {self.left_score}     Score: {self.right_score}",align=ALIGNMENT,font=FONT)

    def left_score_increase(self):
        self.clear()
        self.left_score+=1
        self.update_score()

    def right_score_increase(self):
        self.clear()
        self.right_score+=1
        self.update_score()

    def reset_score(self):
        self.right_score = 0

        self.left_score = 0

    def  game_over(self, winner):
        self.goto(0, 50)
        self.write(f"GAME OVER! {winner} player has won!", align=ALIGNMENT, font=FONT)


