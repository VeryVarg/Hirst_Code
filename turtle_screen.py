from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forw():
    tim.forward(10)

def back():
    tim.back(10)

def left():
    tim.left(30)

def right():
    tim.right(30)

def reset():
    tim.reset()


screen.listen()

screen.onkey(fun = forw, key="w")
screen.onkey(fun = back, key="s")
screen.onkey(fun = left, key="a")
screen.onkey(fun = right, key="d")
screen.onkey(fun = reset, key="c")

screen.exitonclick()
