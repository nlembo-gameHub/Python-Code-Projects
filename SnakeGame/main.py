# Libraries and Modules
from turtle import Screen
from snake import Snake
import time

# Screen Display Setup
screen = Screen()
s_width = 600
s_height = 600
s_color = "black"
s_title = "Nathan's Snake Game"

screen.setup(width=s_width, height=s_height)
screen.bgcolor(s_color)
screen.title(s_title)
screen.tracer(0)

# Snake Body Display
snake_shape = "square"
snake_color = "white"

snake = Snake(s_color=snake_color, s_shape=snake_shape)

# Game Conditions
game_is_on = True

# Listeners
screen.listen()
# Action Mapping
# Using a dictionary, we can set our list of actions and make or listeners more versatile
actions = {
    "Up": snake.up,
    "Down": snake.down,
    "Left": snake.left,
    "Right": snake.right,
}

# For loop that allows us to cycle through the action commands
for move_option in actions:
    screen.onkey(fun=actions[move_option], key=move_option)

# Main Game Logic
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

# Ending Code
screen.exitonclick()