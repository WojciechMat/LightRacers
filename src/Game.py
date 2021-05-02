import tkinter
import turtle
import common
from Player import Player
import time


class Game:
    def __init__(self):
        self.win_size = common.win_size
        self.win_size = common.win_size
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.hideturtle()
        self.pen.penup()
        var_file = open("variables", 'r')
        variables = var_file.read().splitlines()
        var_file.close()
        self.player1 = Player("stop", -1 * self.win_size / 2 + 70, "red", self.win_size, variables[0])
        self.player2 = Player("stop", self.win_size / 2 - 70, "blue", self.win_size, variables[1])
        self.init_delay = float(variables[2])
        self.delay = self.init_delay
        self.player1.hideturtle()
        self.player2.hideturtle()
        self.started = False
        self.aborted = False
        self.style = ("Courier", 12, "normal")

    def __del__(self):
        # catching an exception which occurs when closing the program during a main game-loop
        try:
            self.player1.hideturtle()
            self.player2.hideturtle()
            self.player1.restart()
            self.player2.restart()
            self.started = False
            self.pen.clear()
            self.aborted = True
            del self
        except tkinter.TclError:
            pass

    def draw_scores(self):
        self.pen.clear()
        self.pen.color("red")
        self.pen.goto(-200, 280)
        self.pen.write("{} : {}".format(self.player1.name, self.player1.score), align="center",
                       font=self.style)
        self.pen.color("blue")
        self.pen.goto(200, 280)
        self.pen.write("{} : {}".format(self.player2.name, self.player2.score), align="center",
                       font=self.style)
        if self.aborted:
            self.pen.clear()

    def tie(self):
        self.pen.goto(0, 0)
        self.pen.clear()
        self.pen.color("white")
        self.pen.write("Tie!", align="center", font=("Courier", 50, "normal"))
        time.sleep(1)
        self.pen.clear()

    def first_wins(self):
        self.pen.goto(0, 0)
        self.pen.clear()
        self.pen.color("white")
        self.pen.write("{} wins!".format(self.player1.name), align="center", font=("Courier", 50, "normal"))
        time.sleep(1)
        self.pen.clear()
        self.player1.score += 1

    def second_wins(self):
        self.pen.goto(0, 0)
        self.pen.clear()
        self.pen.color("white")
        self.pen.write("{} wins!".format(self.player2.name), align="center", font=("Courier", 50, "normal"))
        time.sleep(1)
        self.pen.clear()
        self.player2.score += 1

#   countdown before starting main game loop
    def countdown(self):
        # catching an exception which occurs when closing the program during a countdown
        try:
            if not self.started and not self.aborted:
                self.started = True
                self.pen.clear()
                cd = turtle.Turtle()
                cd.speed(0)
                cd.color("purple")
                cd.hideturtle()
                cd.penup()
                cd.goto(0, 0)
                cd.write("3", align="center", font=("Courier", 50, "normal"))
                time.sleep(0.5)
                cd.clear()
                cd.write("2", align="center", font=("Courier", 50, "normal"))
                time.sleep(0.5)
                cd.color("white")
                cd.clear()
                cd.write("1", align="center", font=("Courier", 50, "normal"))
                time.sleep(0.5)
                cd.color("green")
                cd.clear()
                cd.write("GO!", align="center", font=("Courier", 50, "normal"))
                time.sleep(0.5)
                cd.clear()
                self.draw_scores()
                self.player2.direction = "down"
                self.player1.direction = "up"
                self.main()
                if self.aborted:
                    self.pen.clear()
        except tkinter.TclError:
            pass

#   starting game-screen
    def begin(self):
        if self.aborted:
            return
        self.delay = self.init_delay
        self.pen.penup()
        self.pen.hideturtle()
        self.player1.showturtle()
        self.player2.showturtle()
        common.window.update()
        common.window.bgcolor("black")

        self.pen.clear()
        self.draw_scores()
        self.started = False
        self.pen.goto(0, 0)
        self.pen.color("purple")
        if not self.aborted:
            self.pen.write("Press enter to start", align="center", font=self.style)
        if not self.started and not self.aborted:
            common.window.listen()
            common.window.onkeypress(self.countdown, "Return")
        if self.aborted:
            self.pen.clear()

    def main(self):
        if self.aborted:
            return

        # controls
        common.window.listen()
        common.window.onkeypress(self.player1.go_up, "Up")
        common.window.onkeypress(self.player1.go_down, "Down")
        common.window.onkeypress(self.player1.go_left, "Left")
        common.window.onkeypress(self.player1.go_right, "Right")
        common.window.onkeypress(self.player2.go_up, "w")
        common.window.onkeypress(self.player2.go_down, "s")
        common.window.onkeypress(self.player2.go_left, "a")
        common.window.onkeypress(self.player2.go_right, "d")
        self.draw_scores()

        # main game loop
        while self.started is True and not self.aborted:
            delay_changer = 0.0
            common.window.update()
            self.player1.clicked = False
            self.player2.clicked = False
            first_wins_var = False
            second_wins_var = False
            if self.player1.isOut():
                second_wins_var = True
            if self.player2.isOut():
                first_wins_var = True

            self.player1.move_all()
            self.player2.move_all()
            if len(self.player1.segments) % 12 == 0 and self.delay > 0.0013:
                self.delay -= 0.0012
            for segment in self.player1.segments:
                if segment.distance(self.player2) < 10:
                    first_wins_var = True
                if segment.distance(self.player1) < 10:
                    second_wins_var = True

            for segment in self.player2.segments:
                if segment.distance(self.player1) < 10:
                    second_wins_var = True
                if segment.distance(self.player2) < 10:
                    first_wins_var = True

            if (first_wins_var and second_wins_var) or self.player1.distance(self.player2) < 5:
                self.tie()
                time.sleep(1)
                self.player1.restart()
                self.player2.restart()
                self.begin()
            elif second_wins_var:
                self.second_wins()
                time.sleep(1)
                self.player1.restart()
                self.player2.restart()
                self.begin()
            elif first_wins_var:
                self.first_wins()
                time.sleep(1)
                self.player1.restart()
                self.player2.restart()
                self.begin()

            time.sleep(self.delay)

