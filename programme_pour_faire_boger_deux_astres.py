from tkinter import *
from math import *

#distance
def distance(x1,y1,x2,y2):
    d= sqrt((x2-x1)**2+(y2-y1)**2)
    return d

#calcul de la force
def force(m1,m2, di ):
    return m1*m2*(6.67*10**-11)/di**2
#fonction avance
def avance(n, gd, hb):
    global x, y, step
    #nouvelles coordonnées
    x[n], y[n] = x[n] +gd, y[n] + hb
    #deplacement du dessin dans le canevas
    can.coords(astre[n], x[n]-10, y[n]-10, x[n]+10, y[n]+10)
    #calcul nouvel interdistance
    di = distance( x[0],y[0],x[1], y[1])
    #conversion de la distance ecran en distance astronomique
    diA = di*1e9
    #calcul de la force gravitationnelle
    f= force(m1, m2, diA)
    #affichage nouvelle valeur de distance
    valDis.configure(text= "Distance = " +str(diA)+"m")
    valFor.configure(text = "Force = " +str(f)+ "N")
    step = di/10
    
def gauche1():
    avance(0,-step,0)
    
def droite1():
    avance(0, step,0)
    
def haut1():
    avance(0,0,-step)
    
def bas1():
    avance(0,0,step)
    
def gauche2():
    avance(1,-step,0)
    
def droite2():
    avance(1,step,0)
    
def haut2():
    avance(1,0,-step)
    
def bas2():
    avance(1,0,step)
    
m1=6e24   #masse de la terre
m2=6e24
astre = [0]*2   #liste servant a modifier les references des dessisn
x =[50., 350.]
y = [100., 100.]
step = 10

#fenetre
fen = Tk()
fen.title("Gravitation universelle selon Newton")
#libellé
valM1 =Label(fen, text = "M1 =" +str(m1) + "kg")
valM2 = Label(fen, text = "M2 =" +str(m2) + "kg")
valM1.grid(row = 1, column = 0)
valM2.grid(row = 1, column = 1)
valDis = Label(fen, text = "Distance")
valFor = Label(fen, text = "Force")
valDis.grid(row = 3, column = 0)
valFor.grid(row = 3, column = 1)

#caneva avec les dessins
can = Canvas(fen, width= 400, height= 200, bg= "ivory")
can.grid(row = 2, column = 0, columnspan= 2)
astre[0] = can.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10, fill ="blue", width=2)
astre[1] = can.create_oval(x[1] -10, y[1]-10, x[1]+10, y[1]+10)
#creation de 4 boutons pour chacun des asrtres
fra1 = Frame(fen)
fra1.grid(row =4, column = 0, sticky = W, padx = 10)
Button(fra1, text = "<-", command= gauche1).pack(side = LEFT)
Button(fra1, text = "->", command = droite1).pack(side= LEFT)
Button(fra1, text = "^", command= haut1).pack(side = LEFT)
Button(fra1, text ="v", command = bas1).pack(side = LEFT)

fra2 = Frame(fen)
fra2.grid(row = 4, column = 1,sticky = E, padx =10)
Button(fra2, text = "Gauche", command = gauche2).pack(side = LEFT)
Button(fra2, text = "droit", command = droite2).pack(side = LEFT)
Button(fra2, text = "haut", command = haut2).pack(side = LEFT)
Button(fra2, text = "bas", command = bas2).pack(side = LEFT)

fen.mainloop()

