#Lemaire Julien - Casagrande Guillaume - G2
#Module de fenetre.

from turtle import *
from random import *
from objets import *

#La valeur de ces variables globales est donnée plus tard. Pour l'instant, on ne fait que les déclarer sans les initialiser.
colonnes = 8
lignes = 8
    
def dessinerFenetre(largeur, hauteur):
    global largeurColonne, largeurLigne #On veut pourvoir utiliser ces variables dans le reste du programme, notamment dans d'autres modules.
    #Dessine la fenetre en fonction du nombre de colonnes et de lignes du quadrillage ainsi que la largeur et la hauteur de la fenetre.
    setup(largeur, hauteur, 0, 0)
    setworldcoordinates(-50,window_height()+150,window_width()+50,-100) 

    #C'est ici que l'on initialise la largeur de chaque colonnes et lignes
    largeurColonne = (window_width())/colonnes
    largeurLigne = (window_height())/lignes
    
    up()
    #On empeche la turtle de bouger (permet de rendre le dessin de la grille instantané).
    speed(0)
    tracer(0, 0) 
    goto(0,0) #Turtle va à l'emplacement de départ.

    
    while xcor()+largeurColonne < window_width(): #Dessine les colonnes, s'arrête avant la bordure droite de la fenetre.
        forward(largeurColonne)
        left(90)
        down()
        forward(window_height())
        up()
        backward(window_height())
        right(90)

    up()
    goto(0,0) #Turtle retourne à l'emplacement de départ.
    left(90)
    
    while ycor()+largeurLigne < window_height(): #Dessine les lignes, s'arrête avant la bordure basse de la fenetre.
        forward(largeurLigne)
        right(90)
        down()
        forward(window_width())
        up()
        backward(window_width())
        left(90)

    goto((largeurColonne/2),(largeurLigne/2))
    left(180)

    bgcolor("#888888")
    tracer(1, 10) #La turtle peut à présent s'animer et bouger sur la grille.

def remplirCases():
    i = 0
    cases = []
    #Toutes les cases valent 0
    while i < colonnes:
        cases.append([])
        j = 0
        while j < lignes:
            cases[i].append(0)
            j+=1
        i+=1

    #Mets les virus en place (5 n°1)
    i = 0
    x = randint(0, colonnes-1)
    y = randint(0, lignes-1)
    while i < 5:
        while cases[x][y] != 0:
            x = randint(0, colonnes-1)
            y = randint(0, lignes-1)
        cases[x][y] = 1
        i+=1

    #Mets les antidotes en place (5 n°2)
    i = 0
    x = randint(0, colonnes-1)
    y = randint(0, lignes-1)
    while i < 5:
        while cases[x][y] != 0:
            x = randint(0, colonnes-1)
            y = randint(0, lignes-1)
        cases[x][y] = 2
        i+=1

    #Mets les bonus en place (10 n°3)
    i = 0
    x = randint(0, colonnes-1)
    y = randint(0, lignes-1)
    while i < 10:
        while cases[x][y] != 0:
            x = randint(0, colonnes-1)
            y = randint(0, lignes-1)
        cases[x][y] = 3
        i+=1
    
    print("Bienvenue dans <insert random name here> !\nLe monde est touché par une épidémie mondiale\nVous devez trouver les 5 antidotes pour éradiquer le virus, sans découvrir de nouveaux foyers... Bonne chance !")

    return cases

def score():
    #Affiche la vie, le score et les différents objets restants dans la fenetre.
    x = xcoor()
    y = ycoor()

    #Turtle instantannée
    tracer(0, 0)

    #Efface les anciennes valeurs en redessinant un rectangle blanc
    up()
    goto(25, window_height()+25)
    begin_fill()
    color("white","white")
    down()
    goto(window_width()-25,window_height()+25)
    backward(75)
    goto(25, window_height()+100)
    forward(50)
    end_fill()

    #Remet les parametres de base (noir, etc...)
    up()
    color("black")

    #Ecrit sur le rectangle blanc les différentes données necessaires pour le jeu.
    #Dans un premier temps, on écrit sur une première ligne la population mondiale restante ainsi que le score.
    left(90)
    forward(10)
    write("Population mondiale : "+str(getnvie()))
    forward(300)
    write("Score : ")
    backward(300)
    right(90)

    #Dans un deuxième temps, on écrit sur une deuxième ligne le nombre de virus restants, d'antidotes restants et de bonus amassés.
    backward(25)
    left(90)
    write("Virus restants : "+str(5-getnvirus()))
    forward(300)
    write("Antidotes restants : "+str(5-getnantidotes()))
    forward(300)
    write("Bonus : "+str(getnbonus()))
    backward(300)
    right(90)
    

    #Permet de refaire bouger la turtle
    tracer(1, 10)

    
