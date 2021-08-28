from turtle import Turtle
MOVING_DISTANCE = 20  # reminder that constants are in all caps
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # step 1: create a snake body, three snake squares lined up next to each other on screen
    # dimension of a square is 20 by 20
    # create_snake and add_segment will create the snake. extend_snake will be responsible for extending the snake
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())  # position of the last segment
        """
        Why doesn't the new segment appear on top of the previous last segment?
        When the snake gets extended, a new segment is added to the existing list of segments of the snake. 
        At the start this new segment will have, in fact, the same position as the previous last segment.
        Then, the move() method of Snake is called and in the for-loop each segment will move to a new position. 
        The new segment (which is now the last segment in the list) will not move (since it will have the same position 
        as the former last segment). 
        But the former last segment, which is now the second to last segment, will move to the position of the third to 
        last segment.
        So the new segment, which is now the last segment, will have a different position than the second to last 
        segment (formerly last segment), which means that they will not appear on top of each other.
        """

    # initialize the snake again back in the center
    def reset_snake(self):
        # before clearing, loop through each segment and relocate it to somewhere off the screen
        for segment in self.segments:
            segment.goto(x=1000, y=1000)
        self.segments.clear()   # remove all items from a list
        self.create_snake()
        self.head = self.segments[0]

    # step 2a: automatically move the snake
    # step 2b: create snake class for its behaviour and appearance
    def move(self):
        # loop from the last segment to the head segment
        # get the tail to follow where the head is going
        # get last segment to move to where the second-to-last segment is, then do the same for each segment to the head
        for segment_num in range(len(self.segments) - 1, 0, -1):  # range doesn't allow for keyword args to be used
            new_x = self.segments[segment_num - 1].xcor()  # x-coordinate of the segment ahead of the current one
            new_y = self.segments[segment_num - 1].ycor()  # y-coordinate of the segment ahead of the current one
            self.segments[segment_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVING_DISTANCE)

    # step 3: control the snake with keyboard controls
    # when one direction is chosen, ensure it cannot move in the opposite direction
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

