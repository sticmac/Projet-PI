#Lemaire Julien - Casagrande Guillaume - G2
#Module pour les objets.

from turtle import *
from random import *

#Différentes variables gérant la vie (nombre d'habitants encore en vie sur Terre).
nvie = 7266000000
vieEnleve = 100000000 #Le nombre de morts à chaque coup.
vieEnleveVirus = 1000000000 #Le nombre de morts à chaque fois qu'on découvre un virus.

#Compte le nombre d'objets différents découverts
nvirus = 0
nantidotes = 0
nbonus = 0

def virus():
    global nvie, vieEnleveVirus, nvirus
    write("Virus", False, align="center")
    nvie -= vieEnleveVirus
    nvirus += 1

def antidote():
    global nvie, vieEnleve, nantidotes
    write("Antidote", False, align="center")
    nvie -= vieEnleve
    nantidotes += 1

def bonus():
    global nvie, vieEnleve, nbonus
    write("Bonus", False, align="center")
    vieEnleve -= randint(1000000,6000000)
    nvie -= vieEnleve
    nbonus += 1

def plouf():
    global nvie, vieEnleve
    write("Plouf !", False, align="center")
    nvie -= vieEnleve

def getnvirus():
    return nvirus

def getnantidotes():
    return nantidotes

def getnbonus():
    return nbonus

def getnvie():
    return nvie

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
