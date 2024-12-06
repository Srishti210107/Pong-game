from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.r_score=0
        self.l_score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center", font=("Courier",70,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center", font=("Courier",70,"normal"))

    def l_point(self):
        self.l_score+=1
        self.update()
    def r_point(self):
        self.r_score+=1
        self.update()