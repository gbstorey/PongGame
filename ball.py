from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.fillcolor("pink")
        self.penup()
        self.speed("fastest")

    def reflect(self):
        new_angle = 180 - self.heading()
        self.setheading(new_angle)
        self.forward(10)

    def screen_bounce(self):
        if self.ycor() > 250 or self.ycor() < -250:
            new_angle = 360 - self.heading()
            self.setheading(new_angle)

    def comp_goal(self):
        if self.xcor() > 360:
            return True

    def player_goal(self):
        if self.xcor() < -360:
            return True

    def restore(self):
        self.goto(0, 0)
        self.setheading(0)
