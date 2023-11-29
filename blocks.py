from turtle import Turtle


class Blocks(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.speed("fastest")
        self.shapesize(2, 5)
        self.penup()
        self.goto(position)

