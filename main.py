# Import required modules
from turtle import Screen, Turtle

# Instantiate screen object
screen = Screen()

# Define the attributes of the screen object
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Instantiate turtle object
paddle = Turtle()

# Define attributes of paddle object
paddle.penup()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.teleport(350, 0)

# Define methods of paddle object

def go_up():
    paddle.sety(paddle.ycor() + 20)

def go_down():
    paddle.sety(paddle.ycor() - 20)

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")

# Refresh screen while game engine is running
game_on = True
while game_on:
    screen.update()

# Exit screen on event
screen.exitonclick()