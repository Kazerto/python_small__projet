from tkinter import *
from random import randrange
#creation de petit cercle rouge
def damier():
    #dessin de ligne de carré avec decalage
    y=0
    while y < 10:
        if y%2 == 0:
            x = 0
        else:
            x = 1
        carre(x*c, y*c)
        y+=1

#creation des petits carrés
def carre(x,y):
    #dessiner une ligne de carre
    i=0
    while i<5:
        can.create_rectangle(x,y,x+c,y+c, fill = "navy")
        i+=1
        x+=c*2            #espacer les carres
        
    
    
def petit_rond_rouge(x,y,r,coul):
    can.create_oval(x-r,y-r,x+r,y+r, fill= coul)
    

    
def ajouter_pions():
    "dessiner un pion au hazard sur le damien"
    #tirer au hasaard des coordonnees
    x = c/2 + randrange(10) * c
    y = c/2 + randrange(10) * c
    petit_rond_rouge(x,y,c/3, "red")
       
    
c = 30                  #taille des carrés
    
 #programme principale
fen=Tk()
can=Canvas(fen, width = c*10, height= c*10, bg="ivory")
can.pack(side= TOP, padx = 5, pady = 5)
b1=Button(fen, text= "damier", command=damier)
b1.pack(side=LEFT, padx=3, pady=3)
b2=Button(fen, text= "pions", command = ajouter_pions  )
b2.pack(side=RIGHT, padx=3, pady=3)
b3=Button(fen, text="Quitte ce foutu jeu", command= fen.quit)
b3.pack(side= BOTTOM, padx=3, pady=3)
fen.mainloop()