from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.fillcolor("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(350, 0)
        self.speed("fastest")
        self.setheading(90)

    def move_down(self):
        self.setheading(270)

    def move_up(self):
        self.setheading(90)
