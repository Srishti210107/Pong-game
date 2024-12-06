from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen=Screen()
screen.bgcolor("Black")
screen.setup(width=800,height=600)
screen.title("Pong Game")

screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_down,"s")
screen.onkey(l_paddle.go_up,"w")
    
game_is_on=True


while(game_is_on):
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor()<-280 or ball.ycor()>280:
        ball.bounce()
    
    if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce2()
        
  
    if ball.xcor()>380 :
        ball.bounce2()
        ball.goto(0,0)
        ball.move_speed=0.06
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.goto(0,0)
        ball.bounce2()
        ball.move_speed=0.06
        scoreboard.r_point()

screen.exitonclick()
