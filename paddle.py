from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.penup()
        self.goto(position)

    def move():
        pass
    def go_up(self):
        if(self.ycor()<260):
            new_y=self.ycor()+40
            self.goto(self.xcor(),new_y)


    def go_down(self):
        if(self.ycor()>-260):
            new_y=self.ycor()-40
            self.goto(self.xcor(),new_y)
        
    