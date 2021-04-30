import sys
import turtle
import common
from Game import Game


def change_vars(fname, sname, dl):
    var_file = open("variables", 'w')
    var_file.write(fname + '\n' + sname + '\n' + str(dl))


# main menu of the game
class Menu:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.penup()
        self.pen.color("white")
        self.pen.speed(0)
        self.__show_options()
        self.game = Game()
        common.window.listen()
        common.window.onclick(self.__click)
        common.window.onkeypress(self.get_back, "Escape")

    def __button(self, y1):
        self.pen.goto(-200, y1)
        self.pen.pendown()
        self.pen.goto(-200, y1 + 70)
        self.pen.goto(200, y1 + 70)
        self.pen.goto(200, y1)
        self.pen.goto(-200, y1)
        self.pen.penup()

    def __game_destroyer(self):
        self.game.__del__()
        common.window.update()

    def __show_options(self):
        self.pen.clear()
        self.pen.goto(0, 210)
        self.pen.write("Light Racers", align="center", font=("Courier", 50, "bold"))
        self.pen.goto(0, 140)
        self.pen.write("Start Game", align="center", font=("Courier", 40, "normal"))
        self.__button(140)
        self.pen.goto(0, 60)
        self.pen.write("Set Player Names", align="center", font=("Courier", 30, "normal"))
        self.__button(50)
        self.pen.goto(0, -40)
        self.pen.write("Set Speed", align="center", font=("Courier", 40, "normal"))
        self.__button(-40)
        self.pen.goto(0, -130)
        self.pen.write("Controls", align="center", font=("Courier", 40, "normal"))
        self.__button(-130)
        self.pen.goto(0, -220)
        self.pen.write("Exit", align="center", font=("Courier", 40, "normal"))
        self.__button(-220)
        self.pen.goto(-290, -290)
        self.pen.write("v.1.0 by @WojciechMat", align="left", font=("Courier", 10, "normal"))

    def get_back(self):
        self.__show_options()
        common.window.onclick(self.__click)
        self.__game_destroyer()
        self.game.pen.clear()

    def __get_speed(self):
        self.pen.clear()
        self.pen.goto(0, 150)
        self.pen.write("Normal", align="center", font=("Courier", 40, "normal"))
        self.__button(150)
        self.pen.goto(0, 50)
        self.pen.write("Fast", align="center", font=("Courier", 40, "normal"))
        self.__button(50)
        self.pen.goto(0, -40)
        self.pen.write("Impossible", align="center", font=("Courier", 40, "normal"))
        self.__button(-40)
        common.window.onclick(self.__click_speed_menu)

    def __get_names(self):
        name1 = common.window.textinput("Set Names", "Player1:")
        name2 = common.window.textinput("Set Names", "Player2:")
        if name1 is None or name1 == "":
            name1 = "Player1"
        if name2 is None or name2 == "":
            name2 = "Player2"
        common.name1 = name1
        common.name2 = name2
        change_vars(common.name1, common.name2, common.delay)
        common.window.onkeypress(self.get_back, "Escape")


    def __click(self, x, y):
        if -200 < x < 200 and 140 < y < 210:
            self.pen.clear()
            common.window.onclick(None)
            self.game = Game()
            self.game.begin()
            return
        if -200 < x < 200 and 50 < y < 120:
            self.__get_names()
            return
        if -200 < x < 200 and -40 < y < 30:
            self.__get_speed()
            return
        if -200 < x < 200 and -130 < y < -60:
            common.window.onclick(None)
            self.__show_controls()
        if -200 < x < 200 and -220 < y < -150:
            sys.exit()

    def __click_speed_menu(self, x, y):
            if -200 < x < 200 and 150 < y < 220:
                self.pen.clear()
                common.delay = 0.07
                change_vars(common.name1, common.name2, str(common.delay))
                self.get_back()
                return
            if -200 < x < 200 and 50 < y < 120
                self.pen.clear()
                common.delay = 0.05
                change_vars(common.name1, common.name2, str(common.delay))
                self.get_back()
                return
            if -200 < x < 200 and -40 < y < 30:
                self.pen.clear()
                common.delay = 0.02
                change_vars(common.name1, common.name2, str(common.delay))
                self.get_back()
                return

    def __show_controls(self):
        self.pen.clear()
        self.pen.goto(-150, 220)
        self.pen.color("red")
        self.pen.write("Player1", align="center", font=("Courier", 30, "normal"))
        self.pen.goto(150, 220)
        self.pen.color("blue")
        self.pen.write("Player2", align="center", font=("Courier", 30, "normal"))
        self.pen.color("red")
        self.pen.goto(-220, 160)
        self.pen.write("Up", align="left", font=("Courier", 24, "normal"))
        self.pen.goto(-220, 110)
        self.pen.write("Left", align="left", font=("Courier", 24, "normal"))
        self.pen.goto(-220, 60)
        self.pen.write("Down", align="left", font=("Courier", 24, "normal"))
        self.pen.goto(-220, 10)
        self.pen.write("Right", align="left", font=("Courier", 24, "normal"))
        self.pen.goto(0, 160)
        self.pen.color("white")
        self.pen.write("move up", align="center", font=("Courier", 24, "normal"))
        self.pen.goto(0, 110)
        self.pen.write("move left", align="center", font=("Courier", 24, "normal"))
        self.pen.goto(0, 60)
        self.pen.write("move right", align="center", font=("Courier", 24, "normal"))
        self.pen.goto(0, 10)
        self.pen.write("move down", align="center", font=("Courier", 24, "normal"))
        self.pen.color("blue")
        self.pen.goto(220, 160)
        self.pen.write("w", align="right", font=("Courier", 24, "normal"))
        self.pen.goto(220, 110)
        self.pen.write("a", align="right", font=("Courier", 24, "normal"))
        self.pen.goto(220, 60)
        self.pen.write("s", align="right", font=("Courier", 24, "normal"))
        self.pen.goto(220, 10)
        self.pen.write("d", align="right", font=("Courier", 24, "normal"))
        self.pen.goto(0, -50)
        self.pen.color("purple")
        self.pen.write("Esc = main menu", align="center", font=("Courier", 30, "normal"))
        self.pen.color("white")
        common.window.listen()
