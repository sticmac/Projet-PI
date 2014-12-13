#Projet de programmation impérative

#chargement des modules
from turtle import *
from grille import *
from tortue import *

coordonneesTortue = [0,0]

#Gestion des événements
def deplacements():
    onkey(haut, "Up")
    onkey(bas, "Down")
    onkey(droite, "Right")
    onkey(gauche, "Left")

def haut():
    coordonneesTortue[1]-=1
    if coordonneesOK(coordonneesTortue):
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[1]+=1

def bas():
    coordonneesTortue[1]+=1
    
    if coordonneesOK(coordonneesTortue):
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[1]-=1

def droite():
    coordonneesTortue[0]+=1
    
    if coordonneesOK(coordonneesTortue):
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[0]-=1

def gauche():
    coordonneesTortue[0]-=1
    
    if coordonneesOK(coordonneesTortue):
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[0]+=1
    

dessinerFenetre(800,600)
deplacements()

#Lancement de la boucle principale : passage en programmation événementielle (tout ne peut-être changé que par pression de touche par exemple).
listen()
mainloop()
