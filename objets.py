#Lemaire Julien - Casagrande Guillaume - G2
#Module pour les objets.

from turtle import *
from tortue import *
from random import *

#Différentes variables gérant la vie (nombre d'habitants encore en vie sur Terre).
vieTotale = 7266000000 #Population mondiale en début de partie.
nvie = vieTotale
vieEnleve = 100000000 #Le nombre de morts à chaque coup.
vieEnleveVirus = 1000000000 #Le nombre de morts à chaque fois qu'on découvre un virus.

#Compte le nombre d'objets différents découverts
nvirus = 0
nantidotes = 0
nbonus = 0

#Liste des avatars d'antidotes et de bonus
score = 0

charb = getCharb() #On récupère Charb, initalisée dans le module Tortue, qui dessinera les images dans les différentes cases de la grille.

def images():
    #Initialise Charb et inclut les différentes images des différents objets dans la bibliothèque des shapes.
    #Initialise également les listes aAntidotes et aBonus, qui servent au choix aléatoire de l'image lorsque l'on tombe sur un antidote ou un bonus.
    global aAntidotes, aBonus
    aAntidotes = [1,2,3,4,5]
    aBonus = [1,1,2,2,3,3,4,4,5,5]
    charb.up()
    charb.hideturtle()
    charb.speed(0)
    for i in aAntidotes:
        addshape("fiole"+str(i)+".gif")
        addshape("cadeau"+str(i)+".gif") #On utilise aAntidotes, car la liste ne continent qu'une seul fois les numeros, ce qui est plus pratique (on ne voudrait pas intégrer deux fois la même image dans la liste des shapes...)
    addshape("virus.gif")
    addshape("plouf.gif")

def dessineCharb(image):
    #Définit le shape (la forme) de Charb pour l'imprimer (stamp) sur la fenetre turtle
    charb.goto(xcor()+0.75,ycor()) #Charb va au même endroit que la turtle principale
    charb.shape(image) #Change le shape de Charb
    charb.stamp() #Imprime le shape de Charb sur l'écran turtle graphics
    
def virus():
    global nvie, vieEnleveVirus, nvirus
    dessineCharb("virus.gif")
    nvie -= vieEnleveVirus
    nvirus += 1

def antidote():
    global nvie, vieEnleve, nantidotes, score
    i = randint(0,4-nantidotes) #Pioche aléatoirement le numero de la fiole que l'on prendra comme image (on prendra "fiolei.gif")
    dessineCharb("fiole"+str(aAntidotes[i])+".gif") #Dessine la fiole correspondante
    aAntidotes.remove(aAntidotes[i]) #On ne veut pas repiocher deux fois le même nombre...
    score += 100
    nvie -= vieEnleve
    nantidotes += 1

def bonus():
    #Un bonus peut avoir deux effets :
    #Soit il diminue le nombre de morts par tour, soit il augmente le score
    global nvie, vieEnleve, nbonus, score
    categorie = randint(0,1) #Pioche le bonus de vie (0) ou le bonus de score (1)
    i = randint(0,9-nbonus) #Pioche aléatoirement le numero du cadeau que l'on prendra comme image (on prendra "cadeaui.gif")
    if categorie == 0:
        vieEnleve -= randint(1000000,6000000)
        dessineCharb("cadeau"+str(aBonus[i])+".gif") #Dessine la fiole correspondante
    else:
        score += randint(10,200)
        dessineCharb("cadeau"+str(aBonus[i])+".gif") #Dessine la fiole correspondante
    aBonus.remove(aBonus[i]) #On ne veut pas repiocher deux fois le même nombre...
    nvie -= vieEnleve
    nbonus += 1

def plouf():
    global nvie, vieEnleve
    dessineCharb("plouf.gif")
    nvie -= vieEnleve

def pourcentageVie():
    return (nvie/vieTotale)*100

def getscore():
    return score

def getnvirus():
    return nvirus

def getnantidotes():
    return nantidotes

def getnbonus():
    return nbonus

def getnvie():
    return nvie

def getvieTotale():
    return vieTotale

def setscore(nvscore):
    global score
    score = nvscore

def setnvirus(virus):
    global nvirus
    nvirus = virus

def setnantidotes(antidotes):
    global nantidotes
    nantidotes = antidotes

def setnbonus(bonus):
    global nbonus
    nbonus = bonus

def setnvie(vie):
    global nvie
    nvie = vie

def setvieTotale(vieT):
    global vieTotale
    vieTotale = vieT
    
