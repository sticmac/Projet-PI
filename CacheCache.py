#Lemaire Julien - Casagrande Guillaume - G2
#Projet de programmation impérative

#chargement des modules
from turtle import *
from grille import *
from tortue import *
from objets import *

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

    print(20*'-')
    if getnvie() <= 0 or getnvirus() == 5: #Game Over
        bye()
        print("La population mondiale est éradiquée, vous avez perdu.")
    elif getnantidotes() == 5: #Victoire
        print("Vous avez sauvé l'humanité ! Bravo !")
        bye()
    else: #Déroulement habituel du jeu
        #Renvoie le nombre de personnes encore en vie, le nombre de virus, antidotes restants, et le nombre de bonus ammassés.
        #(On utilise les fonctions "assesseurs" (get) présentes dans le module objets pour cela).
        #print("Il reste",getnvie(),"habitants en vie")
        #print("Il reste",5-getnvirus(),"virus et",5-getnantidotes(),"antidotes.\nVous avez ramassé",getnbonus(),"bonus.")
        score()
        print(xcor(),ycor())
        setCoordonnees(coordonneesTortue)
    capturer = True

dessinerFenetre(800,600)
objetsCases = remplirCases()
        
score() #Affiche les valeurs initiales du score, de la vie, etc...
setCoordonnees(coordonneesTortue)

#Lancement de la boucle principale : passage en programmation événementielle (tout ne peut-être changé que par pression de touche par exemple).
deplacements()
listen()
mainloop()
