#Lemaire Julien - Casagrande Guillaume - G2
#Permet de gérer facilement tous les problèmes de coordonnées du curseur (la turtle).
#Repertorie également les tortues Cabu et Charb, utilisées pour dessiner tous les éléments de la grille et du décor ainsi que l'interface.
from turtle import *
import grille

cabu = Turtle()
charb = Turtle() #Charb est une turtle dessinera les images dans les différentes cases, quand on découvrira les objets

def coordonneesOK(coor):
    #Renvoie True si le curseur est toujours dans la grille.
    return not(coor[0] > (grille.colonnes)-1 or coor[0] < 0 or coor[1] > (grille.lignes)-1 or coor[1] < 0)

def setCoordonnees(coor):
    #Modifie la ligne et la colonne de la tortue.
    goto((grille.largeurColonne/2)+coor[0]*grille.largeurColonne, (grille.largeurLigne/2)+coor[1]*grille.largeurLigne)

def getCabu():
    return cabu

def getCharb():
    return charb
