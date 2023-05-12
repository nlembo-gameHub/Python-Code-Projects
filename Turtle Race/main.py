# Importing Libraries & Modules
from turtle import Turtle, Screen
import random

# Screen Display Settings
screen = Screen()
canvas_width = 500
canvas_height = 400
background = "racetrack.png"
title_text = "Turtle Race! Place your Bets!"
prompt_text = "Which turtle will win the race? Enter a color here: "

# Screen Display
screen.setup(width=canvas_width, height=canvas_height)
screen.bgpic(background)
user_choice = screen.textinput(title=title_text, prompt=prompt_text)
print(user_choice)

# Turtle Object Settings
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
x_pos = canvas_width/2 - 20
y_pos = [-175, -110, -40, 32, 102, 175]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-x_pos, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

# Win Conditions
is_race_on = False
win_distance = canvas_width/2 - 20

# Game Logic Begin
if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > win_distance:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_choice:
                print(f"You've won.The winning color is {winning_color}")
            else:
                print(f"You've lost.The winning color is {winning_color}")
            break
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


# Keeping Screen Option until clicked
screen.exitonclick()
