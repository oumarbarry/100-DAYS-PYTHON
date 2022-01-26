from random import randint
import turtle

screen = turtle.Screen()
screen.colormode(255)

franklin = turtle.Turtle()
franklin.pen(shown=False, speed=0, pendown=False)
franklin.goto(-240, -220)

def colorize():
    return ( randint(0, 255), randint(0, 255), randint(0, 255) )

def draw_line():
    for _ in range(10):
        franklin.dot(25, colorize())
        franklin.forward(50)

for _ in range(10):
    draw_line()
    franklin.goto(-240, franklin.ycor()+50)

screen.exitonclick()