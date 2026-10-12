from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_score_file()

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.store_high_score(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def read_score_file(self):
        with open("data.txt") as data:
            high_score = int(data.read())
            return high_score

    def store_high_score(self , score):
        with open("data.txt" , mode="w") as file:
            file.write(str(score))

    

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT,
    #                font=FONT)
