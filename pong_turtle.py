"""
    Python 3 Pong game created with turtle module
    Author: Jennifer Sun
"""

import turtle
import os

window = turtle.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("0 | 0", align="center", font=("Courier", 24, "normal"))
for i in range(260, -301, -40):
    pen.goto(0, i)
    pen.write("|", align="center", font=("Courier", 24, "normal"))
pen.goto(0, 260)

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -250:
        y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -250:
        y -= 20
    paddle_b.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")
window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Left and right
    if ball.xcor() > 380:
        score_a += 1
        pen.clear()
        pen.write(f"{score_a} | {score_b}", align="center", font=("Courier", 24, "normal"))
        for i in range(260, -301, -40):
            pen.goto(0, i)
            pen.write("|", align="center", font=("Courier", 24, "normal"))
        pen.goto(0, 260)
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -380:
        score_b += 1
        pen.clear()
        pen.write(f"{score_a} | {score_b}", align="center", font=("Courier", 24, "normal"))
        for i in range(260, -301, -40):
            pen.goto(0, i)
            pen.write("|", align="center", font=("Courier", 24, "normal"))
        pen.goto(0, 260)
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1

    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
