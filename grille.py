#Module de fenetre.

from turtle import *

#La valeur de ces variables globales est donnée plus tard. Pour l'instant, on ne fait que les déclarer sans les initialiser.
colonnes = 8
lignes = 8
    
def dessinerFenetre(largeur, hauteur):
    global largeurColonne, largeurLigne #On veut pourvoir utiliser ces variables dans le reste du programme, notamment dans d'autres modules.
    #Dessine la fenetre en fonction du nombre de colonnes et de lignes du quadrillage ainsi que la largeur et la hauteur de la fenetre.
    setup(largeur, hauteur, 0, 0)
    setworldcoordinates(0,window_height(),window_width(),0) 

    #C'est ici que l'on initialise la largeur de chaque colonnes et lignes
    largeurColonne = (window_width())/colonnes
    largeurLigne = (window_height())/lignes
    
    up()
    speed(0)
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

