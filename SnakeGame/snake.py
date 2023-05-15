from turtle import Turtle
# Const Variables
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self, s_color, s_shape):
        self.segments = []
        self.color = s_color
        self.shape = s_shape
        self.create_snake()
        self.head = self.segments[0]

    # Creating the Snake
    def create_snake(self):
        # For loop that creates the snake's body segments
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    # Adding Segments to the body
    def add_segment(self, position):
        new_segment = Turtle(shape=self.shape)
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Extending the snake's body further
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Movement Function
    def move(self):
        # Cycle through the Loop in reverse order for user movement
        # Start = len(segments)-1, Stop = 0, Step = -1
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    # Movement Controls
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

