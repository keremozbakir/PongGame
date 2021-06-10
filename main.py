from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = Scoreboard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
screen.listen()
screen.onkeypress(right_paddle.move_down, "Down")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(left_paddle.move_up, "w")
game_is_on = True
# ball.start_moving()

while game_is_on:
    screen.update()
    #ball.speed_ball()

    # print(f"x:{ball.xcor()} Y: {ball.ycor()}")
    # print(ball.xcor())
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.xcor() > 360:
        # print("ball out!!")
        scoreboard.score_left()
        ball.reset_ball()
        time.sleep(3)
        ball.bounce_x()

        # ball.bounce_x()
    if ball.xcor() < -380:
        # ball.bounce_x()
        scoreboard.score_right()
        screen.update()
        ball.reset_ball()
        time.sleep(3)
        ball.bounce_x()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    if ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    ball.move()
    time.sleep(ball.move_speed)

    # screen.update()

screen.exitonclick()
