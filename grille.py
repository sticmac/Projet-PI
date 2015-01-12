#Lemaire Julien - Casagrande Guillaume - G2
#Module de fenetre.

from turtle import *
from random import *
from objets import *
from decor import *

#La valeur de ces variables globales est donnée plus tard. Pour l'instant, on ne fait que les déclarer sans les initialiser.
colonnes = 8
lignes = 8

cabu = Turtle() #Cabu sera chargée de dessiner la grille, les numéros de colonnes, de lignes, ainsi que le score et la barre de vie.
    
def dessinerFenetre(largeur, hauteur):
    global largeurColonne, largeurLigne #On veut pourvoir utiliser ces variables dans le reste du programme, notamment dans d'autres modules.
    #Dessine la fenetre en fonction du nombre de colonnes et de lignes du quadrillage ainsi que la largeur et la hauteur de la fenetre.
    setup(largeur, hauteur, 0, 0)
    setworldcoordinates(-100,window_height()+150,window_width()+100,-200) 

    #C'est ici que l'on initialise la largeur de chaque colonnes et lignes
    largeurColonne = (window_width())/colonnes
    largeurLigne = (window_height())/lignes

    cabu.hideturtle()
    
    cabu.up()
    #On empeche la turtle de bouger (permet de rendre le dessin de la grille instantané).
    cabu.speed(0)
    speed(0)
    tracer(0,0)

    decor()
    
    cabu.goto(0,0) #Turtle va à l'emplacement de départ.

    i = 0 #Compteur de colonne puis de lignes
    dessiner = True #Booléen qui permet de lancer les boucles de dessin de colonnes et de lignes.
    
    while dessiner: #Dessine les colonnes, s'arrête avant la bordure droite de la fenetre.
        cabu.down()
        cabu.left(90)
        cabu.forward(window_height())
        cabu.up()
        cabu.backward(window_height())
        cabu.right(90)

        if i != 8:
            #Le bord de la colonne est dessiné, on indique au milieu, légèrement plus haut, son numéro.
            cabu.forward(largeurColonne/2)
            cabu.right(90)
            cabu.forward(20)
            cabu.color("#FFC930")
            cabu.write(str(i))
            cabu.color("black")
            cabu.backward(20)
            cabu.left(90)
            i+=1 #La prochaine colonne aura une valeur incrémentée de 1
            cabu.forward(largeurColonne/2) #Avance jusqu'à l'emplacement du prochain bord.
        else:
            dessiner = False #Si on continue, on sort de la fenetre, donc on s'arrête.

    cabu.up()
    cabu.goto(0,0) #Turtle retourne à l'emplacement de départ.
    cabu.left(90)
    i = 0 #On repart de 0 pour les lignes.
    dessiner = True #On reprend le dessin, des lignes cette fois.
    
    while dessiner: #Dessine les lignes, s'arrête avant la bordure basse de la fenetre.
        cabu.down()
        cabu.right(90)
        cabu.down()
        cabu.forward(window_width())
        cabu.up()
        cabu.backward(window_width())
        cabu.left(90)

        if i != 8:
            #Le bord de la ligne est dessiné, on indique au milieu, légèrement plus à gauche, son numéro.
            cabu.forward((largeurLigne/2)+10)
            cabu.left(90)
            cabu.forward(20)
            cabu.color("#FFC930")
            cabu.write(str(i))
            cabu.color("black")
            cabu.backward(20)
            cabu.right(90)
            i+=1 #La prochaine colonne aura une valeur incrémentée de 1
            cabu.forward((largeurLigne/2)-10) #Avance jusqu'à l'emplacement du prochain bord.
        else:
            dessiner = False #Si on continue, on sort de la fenetre, donc on s'arrête.


    cabu.goto((largeurColonne/2),(largeurLigne/2))
    cabu.left(180)

    bgcolor("#9B9B9B")

def decor():
    #Dessin du décor sur toute la fenetre.

    #Dessin des virus sur les bordures supérieures et inférieures de la fenêtre
    x = -90
    y = -190
    ecart = 45
    while x <= window_width()+100:
        drawvirus(x,y)
        x+=ecart
    x = -90
    y = 925
    while x <= window_width()+100:
        drawvirus(x,y)
        x+=ecart

    erlenmeyer(-50, -150, 80, "#2B2B2B")
    tubeaessai(window_width()+50, -150, 100, 5, "#2B2B2B")
    tetedemort(-50, window_height(), 100, 100)
    seringue(window_width()+50, window_height(), 100, 20, "#2B2B2B")

    up()
    goto(window_width()/2, -50)
    write("VIROUS",align="center",font=("Arial", "50", "normal"))

    #Remise de place des parametres de base
    seth(0)
    up()
    color("black")

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
    #Coordonnées aléatoires
    x = randint(0, colonnes-1)
    y = randint(0, lignes-1)
    while i < 5:
        while cases[x][y] != 0: #Pour ne pas "écraser" une case déjà remplie. On ne veut en changer la valeur QUE si elle est vide (0).
            x = randint(0, colonnes-1)
            y = randint(0, lignes-1)
        cases[x][y] = 1
        print("Virus :", x, y) #Cheat
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
        print("Antidote :", x, y) #Cheat
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
        print("Bonus :", x, y) #Cheat
        i+=1
    
    
    return cases

def afficherScore():
    #Affiche la vie, le score et les différents objets restants dans la fenetre.

    #Turtle instantannée et invisible
    hideturtle()
    speed(0)
    tracer(0, 0)

    xScore = 50

    #Efface les anciennes valeurs en redessinant un rectangle orange
    up()
    goto(xScore, window_height()+25)
    begin_fill()
    color("black","#F7A110")
    down()
    left(90)
    forward(600)
    right(90)
    backward(75)
    goto(xScore, window_height()+100)
    forward(75)
    backward(30)
    end_fill()

    #Remet les parametres de base (noir, etc...)
    up()
    color("black")

    #Ecrit sur le rectangle orange les différentes données necessaires pour le jeu.
    #Dans un premier temps, on écrit sur une première ligne la population mondiale restante ainsi que le score.
    left(90)
    forward(10)
    write("Population mondiale : "+decomposerNombre(getnvie()))
    forward(300)
    write("Score : "+decomposerNombre(getscore()))
    backward(300)
    right(90)

    #Dans un deuxième temps, on écrit sur une deuxième ligne le nombre de virus restants, d'antidotes restants et de bonus amassés.
    backward(25)
    left(90)
    write("Virus restants : "+str(5-getnvirus()))
    forward(300)
    write("Antidotes restants : "+str(5-getnantidotes()))
    forward(200)
    write("Bonus : "+str(getnbonus()))
    backward(200)
    right(90)

    barreDeVie(pourcentageVie(),xScore+650,window_height()+25) #Trace la barre de vie à coté du rectangle orange
    

    #Permet de refaire bouger la turtle et de la rendre visible
    showturtle()
    tracer(1, 10)

def barreDeVie(vie, x, y):
    #Dessine la barre de vie en partant du point O(x,y)
    #Pour cela on dessine un rectangle rouge de longueur 200 par dessus lequel on redessine un rectangle bleu, dont la longueur vaut le pourcentage de la populatrion mondiale restante multiplié par 2
    up()
    goto(x,y)
    seth(0)
    down()

    #Rectangle rouge
    color("black","#ba1717")
    begin_fill()
    forward(250)
    left(90)
    forward(75)
    left(90)
    forward(250)
    left(90)
    forward(75)
    end_fill()

    #Rectangle bleu
    left(90)
    color("black", "#9cdacc")
    begin_fill()
    forward(vie*2.5)
    left(90)
    forward(75)
    left(90)
    forward(vie*2.5)
    left(90)
    forward(75)
    end_fill()

    #Remise à zéro des paramètres de la tortue
    up()
    color("black")

def decomposerNombre(nombre):
    #Fonction permettant de découper un nombre en milliards, millions, milliers, etc...
    nombreStr = str(nombre) #Transforme le nombre en chaine de caractères
    i = 0
    decade = []
    while i < len(nombreStr):
        cran = len(nombreStr)-i-1 #Prend les caractères du nombre (chaine nombreStr) à partir de la fin
        decade.insert(0, nombreStr[cran]) #Et les insère au début d'une autre liste.
        if (i+1)%3 == 0 and cran != 0: #On veut rajouter un espace à chaque changement de "décade" (millions, milliards...) sauf pour le dernier cran de nombreStr (0%3 = 0)
            decade.insert(0, " ")
        i+=1
    nombreFinalStr = ''.join(decade) #Transforme notre liste en chaine de caractère.
    return nombreFinalStr
