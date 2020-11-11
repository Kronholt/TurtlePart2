from turtle import Turtle, Screen

t = Turtle()
screen = Screen()




def move_forward():
    t.forward(10)

def move_left():
    t.left(10)

def move_right():
    t.right(10)

def move_back():
    t.back(10)

def reset():
    t.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="c", fun=reset)









screen.exitonclick()
