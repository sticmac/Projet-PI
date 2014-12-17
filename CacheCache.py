#Projet de programmation impérative

#chargement des modules
from turtle import *
from grille import *
from tortue import *

coordonneesTortue = [0,0]

#Gestion des événements
def deplacements():
    #Applique les fonctions événementielles aux touches directionnelles
    onkey(haut, "Up")
    onkey(bas, "Down")
    onkey(droite, "Right")
    onkey(gauche, "Left")
    #Touche de selection de case
    onkey(selectionner, "space")

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

def selectionner():
    #On fixe les valeurs de la case où la fonction d'applique (pour éviter les bugs)
    x = coordonneesTortue[0]
    y = coordonneesTortue[1]

    #Ecrit le message correspondant à la valeur de la case
    #0 = Plouf, 1 = Virus, 2 = Antidote, 3 = Bonus
    objet = objetsCases[x][y]
    if objet == 0:
        write("Plouf !", False, align="center")
    elif objet == 1:
        write("Virus", False, align="center")
    elif objet == 2:
        write("Antidote", False, align="center")
    elif objet == 3:
        write("Bonus", False, align="center")
    objetsCases[x][y] = -1

    print("Il reste",vie,"habitants en vie")
    

dessinerFenetre(800,600)
objetsCases = remplirCases()

vie = 7000000000


#Lancement de la boucle principale : passage en programmation événementielle (tout ne peut-être changé que par pression de touche par exemple).
deplacements()
listen()
mainloop()
