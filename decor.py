#Lemaire Julien - Guillaume Casagrande

from turtle import *

def drawvirus(x, y):
    up()
    goto(x,y)
    begin_fill()
    seth(90)
    backward(12)
    right(90)
    down()
    circle(12)
    up()
    left(90)
    forward(12)
    down()
    end_fill()
    
    up()
    goto(x,y)
    seth(90)
    backward(10)
    left(90)
    forward(10)
    right(90)
    down()
    dessinePolygone(4,20,"purple")

    up()
    goto(x,y)
    backward(14.2)
    left(45)
    down()
    dessinePolygone(4,20,"purple")
    goto(x,y)

def dessinePolygone(nbCotes, lCote, couleur="black"):
    i=0
    color(couleur)
    begin_fill()
    while i < nbCotes:
        forward(lCote)
        right(360/nbCotes)
        i+=1
    end_fill()

