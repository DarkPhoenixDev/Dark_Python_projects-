from turtle import Turtle,Screen
from pebbles import Pabble,Pabble2
from ball import Ball
import time
from score import Scoreboard
screen = Screen()
pabble = Pabble()
pabble2 = Pabble2()
score = Scoreboard()
ball = Ball()
screen.setup(width=800,height=600)
screen.title("welcome to my pong game")
screen.bgcolor("black")
screen.tracer(0)
pabble.create_pabble()
pabble2.create_pabble2()
ball.create_ball()
screen.listen()
screen.onkey(pabble.up,"Up")
screen.onkey(pabble2.up,"w")
screen.onkey(pabble2.down,"s")
screen.onkey(pabble.down,"Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor()>270 or ball.ycor()<-270:
        ball.bounce_y()
    if ball.distance(pabble) < 50 and ball.xcor() >320:
        ball.bounce_x()
    if ball.distance(pabble2) < 50 and ball.xcor() <-320:
        ball.bounce_x()
    if ball.xcor() >380 :
        ball.ball_reset()
        score.update_l()
       
    if ball.xcor() <-380:
        ball.ball_reset()
        score.update_r()
        
        
screen.exitonclick()