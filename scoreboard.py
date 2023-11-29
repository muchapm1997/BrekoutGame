from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score_value = 0
        self.live_value = 3
        self.score = self.inscription((0, 250))
        self.live = self.inscription((300, 250))
        self.update_score()
        self.update_lives()

    def inscription(self, pos):
        score = Turtle()
        score.color("white")
        score.penup()
        score.hideturtle()
        score.goto(pos)
        return score

    def update_score(self):
        self.score.clear()
        self.score.write(f"Score: {self.score_value}", align="center", font=("Arial", 28, "normal"))

    def update_lives(self):
        self.live.clear()
        self.live.write(f"Lives: {self.live_value}", align="center", font=("Arial", 28, "normal"))

    def add_score(self):
        self.score_value += 4
        self.update_score()

    def lost_live(self):
        self.live_value -= 1
        self.update_lives()