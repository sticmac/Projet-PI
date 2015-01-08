#Lemaire Julien - Casagrande Guillaume - G2
#Projet de programmation impérative

#chargement des modules
from turtle import *
from grille import *
from tortue import *
from objets import *
from tkinter import messagebox

coordonneesTortue = [0,0]
capturer = True #Si ce booléen vaut True, alors on peut executer les évenements liés aux touches du clavier.

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
    
    if coordonneesOK(coordonneesTortue) and capturer:
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[1]+=1

def bas():
    coordonneesTortue[1]+=1
        
    if coordonneesOK(coordonneesTortue) and capturer:
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[1]-=1

def droite():
    coordonneesTortue[0]+=1
        
    if coordonneesOK(coordonneesTortue)and capturer:
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[0]-=1

def gauche():
    coordonneesTortue[0]-=1
        
    if coordonneesOK(coordonneesTortue) and capturer:
        setCoordonnees(coordonneesTortue)
    else:
        coordonneesTortue[0]+=1
        
def selectionner():
    capturer = False
    #On fixe les valeurs de la case où la fonction d'applique (pour éviter les bugs)
    x = coordonneesTortue[0]
    y = coordonneesTortue[1]

    #Execute les commandes des fonctions correspondante à l'objet trouvé, situées dans le module "objets"
    #0 = Plouf, 1 = Virus, 2 = Antidote, 3 = Bonus
    objet = objetsCases[x][y]
    if objet == 0:
        plouf()
    elif objet == 1:
        virus()
    elif objet == 2:
        antidote()
    elif objet == 3:
        bonus()
    objetsCases[x][y] = -1

    if getnvie() <= 0 or getnvirus() == 5: #Game Over
        print("La population mondiale est éradiquée, vous avez perdu.")
        if not messagebox.askokcancel("Game Over", "Recommencer"):
            bye()
    elif getnantidotes() == 5: #Victoire
        print("Vous avez sauvé l'humanité ! Bravo !")
        if not messagebox.askokcancel("Victoire !", "Recommencer"): 
            bye()
    else: #Déroulement habituel du jeu
        score()
        setCoordonnees(coordonneesTortue)
    capturer = True

def gameover():
    iftkMessageBox.askokcancel("Game Over", "Recommencer")
    

dessinerFenetre(1000,800)
objetsCases = remplirCases()
        
score() #Affiche les valeurs initiales du score, de la vie, etc...
setCoordonnees(coordonneesTortue)

#Lancement de la boucle principale : passage en programmation événementielle (tout ne peut-être changé que par pression de touche par exemple).
deplacements()
listen()
mainloop()
