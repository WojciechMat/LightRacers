import sys
import turtle


class Player(turtle.Turtle):

    def __init__(self, direc, y, col, size, name):
        super().__init__()
        self.direction = direc
        self.init_direction = direc
        self.segments = []
        self.initial_x = 0
        self.initial_y = y
        self.color_var = col
        self.win_size = size
        self.speed(0)
        self.shape("square")
        self.color(col)
        self.shapesize(0.5)
        self.penup()
        self.goto(0, y)
        self.score = 0
        self.name = name

    def build(self):

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color(self.color_var)
        new_segment.shapesize(0.5)
        new_segment.penup()
        new_segment.goto(self.xcor(), self.ycor())
        self.__move()
        self.segments.append(new_segment)
        return

    def __move(self):

        if self.direction == "up":
            self.sety(self.ycor() + 10)
        if self.direction == "left":
            self.setx(self.xcor() - 10)
        if self.direction == "right":
            self.setx(self.xcor() + 10)
        if self.direction == "down":
            self.sety(self.ycor() - 10)
        return

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"
        return

    def go_right(self):
        if self.direction != "left":
            self.direction = "right"
        return

    def go_left(self):
        if self.direction != "right":
            self.direction = "left"
        return

    def go_down(self):
        if self.direction != "up":
            self.direction = "down"
        return

    def move_all(self):
        # catching an exception which occurs when closing the program during a main game-loop
        try:
            if self.direction != "stop":
                self.build()
        except turtle.Terminator:
            sys.exit()

    def isOut(self):
        return self.xcor() > self.win_size / 2 - 10 or \
               self.xcor() < -1 * self.win_size / 2 + 10 or \
               self.ycor() > self.win_size / 2 - 15 or \
               self.ycor() < -1 * self.win_size / 2 + 10

    def restart(self):

        self.goto(self.initial_x, self.initial_y)
        for segment in self.segments:
            segment.goto(1000, 1000)
            del segment
        self.segments.clear()
        self.direction = "stop"

        return
