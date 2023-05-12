from turtle import Turtle, Screen


# Object Vars
turtle = Turtle()
screen = Screen()


# Movement functions
def move_forwards():
    turtle.forward(10)


def move_backwards():
    turtle.backward(10)


def move_left():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)


def move_right():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def clear_screen():
    turtle.reset()


# Action Mapping
# Using a dictionary, we can set our list of actions and make or listeners more versatile
actions = {
    "w": move_forwards,
    "s": move_backwards,
    "a": move_left,
    "d": move_right,
    "c": clear_screen,
}

# Listeners
screen.listen()
# For loop that allows us to cycle through the action commands
for move_option in actions:
    screen.onkey(fun=actions[move_option], key=move_option)

screen.exitonclick()