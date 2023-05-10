# Libraries & Modules
import colorgram
import turtle as turtle_module
import random

# Setting up the empty list for the rgb colors
rgb_colors = []
# Extracting the colors from the image using the colorgram function
colors = colorgram.extract('image.jpg', 30)
# Loop through the list of Color objects
for color in colors:
    if color.proportion < 0.1:
        # Add the individual color object rgb values
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        # Create our tuple to store our r, g, and b values
        new_color = (r, b, g)
        rgb_colors.append(new_color)

color_list = rgb_colors

# Turtle Objects
screen = turtle_module.Screen()
turtle = turtle_module.Turtle()

# Turtle Appearance
turtle_module.colormode(255)
turtle.hideturtle()
turtle.penup()
number_of_dots = 100

# Turtle Speed
turtle.speed("fastest")

# Turtle Initial Direction
x = -255
y = -255
turtle.goto(x, y)

# Turtle Move Logic
for dot_count in range(1, number_of_dots + 1):
    turtle.dot(20, random.choice(color_list))
    turtle.forward(50)
    # Go to a new row after each 10 dots have been filled per row
    if dot_count % 10 == 0:
        y += 50
        turtle.goto(x, y)

# Ensure code runs until user clicks on the screen
screen.exitonclick()
