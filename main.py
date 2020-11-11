from turtle import Turtle, Screen
import random


screen = Screen()
is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="What color turtle will win? Enter a color: ")
y_positions = [120, 70, 20, -30, -80, -130]
turtle_list = []
colors = ["red", "orange", "yellow", "blue", "purple", "green"]

for turtle_index in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[turtle_index])
    turtle.penup()
    turtle.goto(x=-240, y=y_positions[turtle_index])
    turtle_list.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
        if turtle.xcor() > 230:
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {turtle.pencolor()} turtle finished first!")
            else:
                print(f"You lost. The {turtle.pencolor()} turtle finished first.")
            is_race_on = False










screen.exitonclick()


#Etch-a-Sketch code
#
# def move_forward():
#     t.forward(10)
#
# def move_left():
#     t.left(10)
#
# def move_right():
#     t.right(10)
#
# def move_back():
#     t.back(10)
#
# def reset():
#     t.reset()
#
# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_back)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=reset)