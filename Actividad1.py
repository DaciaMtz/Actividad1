#TC001S.1 Actividad 1 PAINT GAME
"""Videojuego que permite al usuario dibujar lineas, cuadrados, rectángulos, 
círculos y triángulos y escoger entre 6 colores distintos"""

#Dacia Martínez Díaz A01733799
#Fernando Aguilar Acosta A00827677

from turtle import *
from freegames import vector

#Function to draw a line
def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

#Function to draw and fill a square
def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

#Function to draw and fill a circle
def drawcircle(start, end):
    "Draw circle from start to end."
    radius=((end.x-start.x)**2+(end.y-start.y)**2)**(1/2)/2
    up()
    goto(start.x+(end.x-start.x)/2, start.y+(end.y-start.y)/2-radius)
    down()
    begin_fill()
    circle(radius)
    end_fill()

#Function to draw and fill a rectangle
def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(2):
        forward(end.x-start.x)
        right(90)    
        forward(start.y-end.y)
        right(90)

    end_fill()

#Function to draw and fill a triangle
def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    for count in range(3):
        forward(end.x - start.x)
        left(120)
        
    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
#Commands to change color
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('purple'), 'P')
#Commands to change shape
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', drawcircle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()