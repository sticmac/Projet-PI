#Lemaire Julien - Guillaume Casagrande - G2
#Module responsable du dessin des éléments du décor.

from turtle import *
from math import *

def debutDessin(x, y, angle, couleur):
    #Fixe les parametres de la tortue pour chaque dessin
    up()
    goto(x,y)
    seth(angle)
    color(couleur)
    begin_fill()

def drawvirus(x, y):
    #Dessine un cercle de centre O(x,y) et de rayon 12
    debutDessin(x,y,90,"#2B2B2B")
    backward(12)
    right(90)
    down()
    circle(12)
    up()
    left(90)
    forward(12)
    down()
    end_fill() #On remplit ce que l'on vient de dessiner.

    #Dessine un premier carré de coté 10 et de centre O
    debutDessin(x,y,90,"#2B2B2B") 
    backward(10)
    left(90)
    forward(10)
    right(90)
    down()
    dessinePolygone(4,20)
    end_fill()

    #Dessine un deuxième carré de coté 10 et de centre O, mais incliné de 45 degrés
    up()
    goto(x,y)
    backward(14.2)
    left(45)
    down()
    begin_fill()
    dessinePolygone(4,20)
    end_fill()
    goto(x,y)

def dessinePolygone(nbCotes, lCote):
    #Dessine un polygone de nbCotes cotés de longueur lCote
    i=0
    while i < nbCotes:
        forward(lCote)
        right(360/nbCotes)
        i+=1

def erlenmeyer(x, y, longueur, couleur="purple"):
    #Le premier point sur lequel on se place n'est pas le centre, mais la partie supérieure gauche de l'erlenmeyer.
    #On se situe donc en haut à gauche de la "tige" de l'erlenmeyer.
    debutDessin(x,y,90,"#2B2B2B")
    down()
    
    forward(longueur/3)
    right(degrees(pi/6))
    forward((longueur-(longueur/3))/cos(pi/6))
    left(degrees(2*pi/3))
    forward(longueur)
    left(degrees(2*pi/3))
    forward((longueur-(longueur/3))/cos(pi/6))
    right(degrees(pi/6))
    forward(longueur/3)
    goto(x,y)
    
    end_fill()

def tubeaessai(x, y, longueur, largeur, couleur="black"):
    #Le premier point sur lequel on se place est le point superieur gauche du tube.
    debutDessin(x,y,90,"#2B2B2B")
    down()

    forward(longueur)
    circle(largeur,180)
    forward(longueur)
    left(90)
    forward(largeur)
    end_fill()

def seringue(x, y, longueur, largeur, couleur="black"):
    #Le premier point sur lequel on se place est le point superieur gauche de la seringue.
    debutDessin(x,y,0,"#2B2B2B")
    down()

    #Partie gauche de la seringue
    forward(largeur)
    left(90)
    forward(longueur/12)
    left(90)
    forward(largeur/3)
    right(90)
    forward(longueur/12)
    right(90)
    forward(largeur/3)
    left(90)
    forward(longueur/12)
    left(90)
    forward(largeur/3)
    right(90)
    forward(longueur/2)
    left(degrees(atan((longueur/12)/(largeur/2)))) #Relation trigonométrique
    forward(sqrt(pow(longueur/12,2)+pow(largeur/2,2))) #Théorème de Pythagore
    right(degrees(atan((longueur/12)/(largeur/2))))
    forward(longueur/6)

    #Partie droite de la seringue
    backward(longueur/6)
    right(degrees(atan((longueur/12)/(largeur/2))))
    backward(sqrt(pow(longueur/12,2)+pow(largeur/2,2)))
    left(degrees(atan((longueur/12)/(largeur/2))))
    backward(longueur/2)
    right(90)
    backward(largeur/3)
    left(90)
    backward(longueur/12)
    left(90)
    backward(largeur/3)
    right(90)
    backward(longueur/12)
    right(90)
    backward(largeur/3)
    left(90)
    backward(longueur/12)

    end_fill()

def tetedemort(x, y, longueur, largeur, couleur="black"):
    #Le point de départ du dessin est le haut de la tete.
    debutDessin(x,y,0,couleur)
    down()
    forward(largeur/4)
    circle(largeur/4,180)
    right(90)
    forward(longueur-(largeur/2))
    left(90)
    forward(largeur/2)
    left(90)
    forward(longueur-(largeur/2))
    right(90)
    circle(largeur/4,180)
    forward(largeur/4)

    up()
    backward(largeur/4)

    end_fill()

    color("red")
    up()
    goto(x-(largeur/4),y+(largeur/3))
    seth(180)
    down()
    begin_fill()
    circle(largeur/10)
    end_fill()
    up()
    backward(largeur/2)
    down()
    begin_fill()
    circle(largeur/10)
    end_fill()

