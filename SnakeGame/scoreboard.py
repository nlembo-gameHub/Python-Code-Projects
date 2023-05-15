from turtle import Turtle

# Consts
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self, _distance):
        super().__init__()
        self.score = 0
        self.color("chartreuse")
        self.penup()
        self.hideturtle()
        self.height = _distance - 10
        self.goto(0, self.height)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()