from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Great Game of Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score_board = Turtle()
score_board.hideturtle()
score_board.color("white")
score_board.penup()
score_board.goto(0, 250)
score = 0

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    score_board.clear()
    score_board.write(f"Score: {score}", align="center", font=("ariel", 24, "bold"))
    ball.move()

    # Detect collisions with ceiling
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collisions with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() < 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        score += 1

    # Detect out of bounds
    if ball.xcor() > 380 or ball.xcor() < -380:
        pen = Turtle()
        pen.penup()
        pen.goto(0, 0)
        pen.color("red")
        pen.write("GAME OVER MAN!!!", align="center", font=("ariel", 48, "bold"))
        game_is_on = False


screen.exitonclick()