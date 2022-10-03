from turtle import Screen
from paddles import Player, Computer
from ball import Ball
import time
import random
from scoreboard import Scoreboard, Square, Score

screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=800)
screen.colormode(255)
screen.tracer(0, 1)

player = Player()
computer = Computer()
ball = Ball()
scoreboard = Scoreboard()
square = Square()
score = Score()

playing = True
play_height = 210
ball_speed = 20

computer_score = 0
player_score = 0
score.score(player_score, computer_score)

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

while playing:
    screen.update()
    time.sleep(0.05)
    player.forward(0.75*ball_speed)
    ball.forward(ball_speed)
    computer.forward(0.5*ball_speed)

    if computer.ycor() - ball.ycor() > 1:
        pass
    else:
        if computer.ycor() > ball.ycor():
            computer.setheading(270)
        elif computer.ycor() < ball.ycor():
            computer.setheading(90)

    ball.screen_bounce()
    computer.hit_roof()
    player.hit_roof()

    if player.ycor() + 60 >= ball.ycor() >= player.ycor() - 60 and \
            player.xcor() + 15 >= ball.xcor() >= player.xcor() - 15:
        ball.reflect()
        if player.heading() == 90:
            ball.setheading(ball.heading() - random.randint(0, 40))
        if player.heading() == 270:
            ball.setheading(ball.heading() + random.randint(0, 40))

    if computer.ycor() + 60 >= ball.ycor() >= computer.ycor() - 60 and \
            computer.xcor() + 15 >= ball.xcor() >= computer.xcor() - 15:
        ball.reflect()

    if ball.comp_goal():
        computer_score += 1
        score.score(player_score, computer_score)
        ball.restore()
    elif ball.player_goal():
        player_score += 1
        score.score(player_score, computer_score)
        ball.restore()

screen.exitonclick()
