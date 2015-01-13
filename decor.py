#Lemaire Julien - Casagrande Guillaume - G2
#Module responsable du dessin des éléments du décor.

from turtle import *
from tortue import *
from math import *

cabu = getCabu() #Pour simplifier le code, on récupère la tortue Cabu du module grille, et on la place dans une nouvelle variable du meme nom pour simplifier le code.
#Cabu dessinera également le décor.

def debutDessin(x, y, angle, couleur):
    #Fixe les parametres de la tortue pour chaque dessin
    cabu.up()
    cabu.goto(x,y)
    cabu.seth(angle)
    cabu.color(couleur)
    cabu.begin_fill()

def drawvirus(x, y, longueurCoteCarre):
    #Dessine un cercle de centre O(x,y) et de rayon 12
    debutDessin(x,y,90,"#2B2B2B")
    cabu.backward(longueurCoteCarre*0.6)
    cabu.right(90)
    cabu.down()
    cabu.circle(longueurCoteCarre*0.6)
    cabu.up()
    cabu.left(90)
    cabu.forward(longueurCoteCarre*0.6)
    cabu.down()
    cabu.end_fill() #On remplit ce que l'on vient de dessiner.

    #Dessine un premier carré de coté 20 et de centre O
    debutDessin(x,y,90,"#2B2B2B") 
    cabu.backward(longueurCoteCarre/2)
    cabu.left(90)
    cabu.forward(longueurCoteCarre/2)
    cabu.right(90)
    cabu.down()
    dessinePolygone(4,longueurCoteCarre)
    cabu.end_fill()

    #Dessine un deuxième carré de coté 20 et de centre O, mais incliné de 45 degrés
    cabu.up()
    cabu.goto(x,y)
    cabu.backward(cos(pi/4)*longueurCoteCarre)
    cabu.left(45)
    cabu.down()
    cabu.begin_fill()
    dessinePolygone(4,longueurCoteCarre)
    cabu.end_fill()
    cabu.goto(x,y)

def dessinePolygone(nbCotes, lCote):
    #Dessine un polygone de nbCotes cotés de longueur lCote
    i=0
    while i < nbCotes:
        cabu.forward(lCote)
        cabu.right(360/nbCotes)
        i+=1

def erlenmeyer(x, y, longueur, couleur="purple"):
    #Le premier point sur lequel on se place n'est pas le centre, mais la partie supérieure gauche de l'erlenmeyer.
    #On se situe donc en haut à gauche de la "tige" de l'erlenmeyer.
    debutDessin(x,y,90,couleur)
    cabu.down()
    
    cabu.forward(longueur/3)
    cabu.right(degrees(pi/6))
    cabu.forward((longueur-(longueur/3))/cos(pi/6))
    cabu.left(degrees(2*pi/3))
    cabu.forward(longueur)
    cabu.left(degrees(2*pi/3))
    cabu.forward((longueur-(longueur/3))/cos(pi/6))
    cabu.right(degrees(pi/6))
    cabu.forward(longueur/3)
    cabu.goto(x,y)
    
    cabu.end_fill()

def tubeaessai(x, y, longueur, largeur, couleur="black"):
    #Le premier point sur lequel on se place est le point superieur gauche du tube.
    debutDessin(x,y,90,couleur)
    cabu.down()

    cabu.forward(longueur)
    cabu.circle(largeur,180)
    cabu.forward(longueur)
    cabu.left(90)
    cabu.forward(largeur)
    cabu.end_fill()

def seringue(x, y, longueur, largeur, couleur="black"):
    #Le premier point sur lequel on se place est le point superieur gauche de la seringue.
    debutDessin(x,y,0,couleur)
    cabu.down()

    #Partie gauche de la seringue
    cabu.forward(largeur)
    cabu.left(90)
    cabu.forward(longueur/12)
    cabu.left(90)
    cabu.forward(largeur/3)
    cabu.right(90)
    cabu.forward(longueur/12)
    cabu.right(90)
    cabu.forward(largeur/3)
    cabu.left(90)
    cabu.forward(longueur/12)
    cabu.left(90)
    cabu.forward(largeur/3)
    cabu.right(90)
    cabu.forward(longueur/2)
    cabu.left(degrees(atan((longueur/12)/(largeur/2)))) #Relation trigonométrique
    cabu.forward(sqrt(pow(longueur/12,2)+pow(largeur/2,2))) #Théorème de Pythagore
    cabu.right(degrees(atan((longueur/12)/(largeur/2))))
    cabu.forward(longueur/6)

    #Partie droite de la seringue
    cabu.backward(longueur/6)
    cabu.right(degrees(atan((longueur/12)/(largeur/2))))
    cabu.backward(sqrt(pow(longueur/12,2)+pow(largeur/2,2)))
    cabu.left(degrees(atan((longueur/12)/(largeur/2))))
    cabu.backward(longueur/2)
    cabu.right(90)
    cabu.backward(largeur/3)
    cabu.left(90)
    cabu.backward(longueur/12)
    cabu.left(90)
    cabu.backward(largeur/3)
    cabu.right(90)
    cabu.backward(longueur/12)
    cabu.right(90)
    cabu.backward(largeur/3)
    cabu.left(90)
    cabu.backward(longueur/12)

    cabu.end_fill()

def tetedemort(x, y, longueur, largeur, couleur="black"):
    #Le point de départ du dessin est le haut de la tete.
    debutDessin(x,y,0,couleur)
    
    cabu.down()
    cabu.forward(largeur/4)
    cabu.circle(largeur/4,180)
    cabu.right(90)
    cabu.forward(longueur-(largeur/2))
    cabu.left(90)
    cabu.forward(largeur/2)
    cabu.left(90)
    cabu.forward(longueur-(largeur/2))
    cabu.right(90)
    cabu.circle(largeur/4,180)
    cabu.forward(largeur/4)
    
    cabu.up()
    cabu.backward(largeur/4)
    
    cabu.end_fill()
    
    cabu.color("red")
    cabu.up()
    cabu.goto(x-(largeur/4),y+(largeur/3))
    cabu.seth(180)
    cabu.down()
    cabu.begin_fill()
    cabu.circle(largeur/10)
    cabu.end_fill()
    cabu.up()
    cabu.backward(largeur/2)
    cabu.down()
    cabu.begin_fill()
    cabu.circle(largeur/10)
    cabu.end_fill()
