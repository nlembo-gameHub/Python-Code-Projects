# Libraries and Modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen Display Setup
screen = Screen()
s_width = 600
s_height = 600
canvas_length = s_width/2 - 20
s_color = "black"
s_title = "Nathan's Snake Game"

screen.setup(width=s_width, height=s_height)
screen.bgcolor(s_color)
screen.title(s_title)
screen.tracer(0)

# Snake Body Appearance
snake_shape = "square"
snake_color = "white"

# Creating Objects from Snake, Food, & Scoreboard Class
snake = Snake(s_color=snake_color, s_shape=snake_shape)
food = Food(_distance=canvas_length)
scoreboard = ScoreBoard(_distance=canvas_length)

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

    # Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect Collision with wall.
    if (snake.head.xcor() > canvas_length or snake.head.xcor() < -canvas_length) or \
            (snake.head.ycor() > canvas_length or snake.head.ycor() < -canvas_length):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    # If the head collides with any segment in the tail we need to trigger a game over
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


# Ending Code
screen.exitonclick()
