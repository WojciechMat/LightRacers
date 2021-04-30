import turtle

# variables and common window
var_file = open("variables", 'r')
variables = var_file.read().splitlines()
var_file.close()
name1 = variables[0]
name2 = variables[1]
delay = float(variables[2])
win_size = 600

# game window
window = turtle.Screen()
window.title("Light Racers")
window.bgcolor("black")
window.setup(width=win_size, height=win_size)
window.tracer(0)
