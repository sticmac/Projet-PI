#Lemaire Julien - Casagrande Guillaume - G2
#Permet de gérer facilement tous les problèmes de coordonnées du curseur (la turtle).

from turtle import *
import grille

def coordonneesOK(coor):
    #Renvoie True si le curseur est toujours dans la grille.
    return not(coor[0] > (grille.colonnes)-1 or coor[0] < 0 or coor[1] > (grille.lignes)-1 or coor[1] < 0)

def setCoordonnees(coor):
    #Modifie la ligne et la colonne de la tortue.
    goto((grille.largeurColonne/2)+coor[0]*grille.largeurColonne, (grille.largeurLigne/2)+coor[1]*grille.largeurLigne)


