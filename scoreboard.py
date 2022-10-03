from turtle import Turtle


class Square(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.setpos(-360, 270)
        self.pendown()
        self.forward(720)
        self.right(90)
        self.forward(540)
        self.right(90)
        self.forward(720)
        self.right(90)
        self.forward(540)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.pendown()
        self.pencolor("white")
        self.write("PONG!", align='center', font=('Bauhaus 93', 80, 'normal'))


class Score(Turtle):
    def __init__(self):
        super().__init__()

    def score(self, player_score, computer_score):
        self.clear()
        self.shape("square")
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, -330)
        self.pendown()
        self.write(f"You: {player_score} Computer: {computer_score}", align='center', font=('Arial', 40, 'normal'))
