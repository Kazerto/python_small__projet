from turtle import *

def carre(taille,couleur,angle):
    color(couleur)
    c= 0
    while c<4:
        forward(taille)
        right(angle)
       
        c = c + 1

def triangle(taille, couleur, angle):
    color(couleur)
    c= 0
    while c<4:
        forward(taille)
        left(angle)
        forward(taille)
        
        c = c + 1
