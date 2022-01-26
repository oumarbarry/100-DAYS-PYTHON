import turtle

screen = turtle.Screen()
franklin = turtle.Turtle()

def right():
    franklin.right(0); franklin.forward(50)
    
def left():
    franklin.left(180); franklin.forward(50)

screen.onkey(right, "Right")
screen.onkey(left, "Left")

screen.listen()
screen.exitonclick()