import time
from turtle import Screen
import keyboard
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
from blocks import Blocks

blocks_position = []
x = -315

screen = Screen()
screen.title("BreakOut")
screen.bgcolor("black")
screen.setup(800, 600)

scoreboard = Scoreboard()
paddle = Paddle()

for i in range(7):
    y = 180
    for j in range(3):
        blocks_position.append((x, y))
        y -= 45
    x += 105

blocks_list = [Blocks(position) for position in blocks_position]

ball = Ball()

game_on = True
while game_on:
    if scoreboard.live_value > 0 and len(blocks_list) > 0:
        ball.move()
        screen.update()
        if ball.ycor() < -300:
            scoreboard.lost_live()
            ball.hideturtle()
            ball.clear()
            ball = Ball()
        if ball.ycor() > 300:
            ball.y_bounce()
        if ball.xcor() > 390 or ball.xcor() < -390:
            ball.x_wall_bounce()
        if ball.ycor() < paddle.ycor() + 5 and ball.ycor() > paddle.ycor() - 5 and ball.distance(paddle) < 50:
            ball.x_bounce()
            ball.y_bounce()
        for i in range(len(blocks_list)):
            if blocks_list[i].isvisible() and ball.distance(blocks_list[i]) < 60 and abs(
                    ball.ycor() - blocks_list[i].ycor()) < 10:
                blocks_list[i].hideturtle()
                blocks_list[i].clear()
                ball.x_bounce()
                ball.y_bounce()
                scoreboard.add_score()
        if keyboard.is_pressed("Left"):
            paddle.move_left()
        if keyboard.is_pressed("Right"):
            paddle.move_right()
    time.sleep(0.01)


screen.exitonclick()