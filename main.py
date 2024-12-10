from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time
MAX_SCORE=3
screen=Screen()
screen.bgcolor("black")
screen.title("MY PONG GAME")
screen.setup(width=800,height=600)
screen.listen()
screen.tracer(n=0)
r_paddle=Paddle(350)
l_paddle=Paddle(-350)
screen.onkeypress(r_paddle.up_paddle, 'Up')
screen.onkeypress(r_paddle.down_paddle, 'Down')
screen.onkeypress(l_paddle.up_paddle, 'w')
screen.onkeypress(l_paddle.down_paddle, 's')
scoreboard=ScoreBoard()
ball=Ball()



game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()
    # collision with the wall
    if ( ball.ycor() > 280
            or ball.ycor() < -280):
        ball.bounce_y()

    #collision withe right paddle
    if (ball.distance(r_paddle)<50 and ball.xcor()>320
            or (ball.distance(l_paddle)<50 and ball.xcor()<-320)):
        ball.bounce_x()

    #c missing the ball right side
    if ball.xcor()>400 :
        scoreboard.left_score_increase()
        ball.reset_ball()
        time.sleep(1)
        ball.move_ball()
        if scoreboard.left_score==MAX_SCORE:
            scoreboard.game_over('Left')
            game_is_on=False
        #missing the ball left side
    elif ball.xcor()<-400:
        scoreboard.right_score_increase()
        ball.reset_ball()
        time.sleep(1)
        if scoreboard.right_score==MAX_SCORE:
            scoreboard.game_over('Right')
            game_is_on=False


        ball.move_ball()






























screen.exitonclick()
