from turtle import Turtle

import keyboard as keyboard

DISTANCE = 20
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(1, 6)
        self.penup()
        self.goto(0, -270)

    def move_left(self):
        if self.xcor() > -335:
            new_x = self.xcor() - DISTANCE
            self.goto((new_x, self.ycor()))


    def move_right(self):
        if self.xcor() < 325:
            new_x = self.xcor() + DISTANCE
            self.goto((new_x, self.ycor()))


    def continuous_movement(self):
        while True:
            if keyboard.is_pressed("Left"):
                self.move_left()
            if keyboard.is_pressed("Right"):
                self.move_right()