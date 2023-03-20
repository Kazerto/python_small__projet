from tkinter import *
from math import *

#distance
def distance(x1,y1,x2,y2):
    d= sqrt((x2-x1)**2+(y2-y1)**2)
    return d

#calcul de la force
def force(m1,m2, di ):
    return m1*m2*(6.67*10**-11)/di**2

def deplacer_astre(event):
    global selected_astre, x, y
    if selected_astre != -1:
        x[selected_astre], y[selected_astre] = event.x, event.y
        can.coords(astre[selected_astre], x[selected_astre]-10, y[selected_astre]-10, x[selected_astre]+10, y[selected_astre]+10)
        selected_astre = -1
        #calcul nouvel interdistance
        di = distance( x[0],y[0],x[1], y[1])
        #conversion de la distance ecran en distance astronomique
        diA = di*1e9
        #calcul de la force gravitationnelle
        f= force(m1, m2, diA)
        #affichage nouvelle valeur de distance
        valDis.configure(text= "Distance = " +str(diA)+"m")
        valFor.configure(text = "Force = " +str(f)+ "N")

def choisir_astre(n):
    global selected_astre
    for i in range(len(astre)):
        x1, y1, x2, y2 = can.coords(astre[n])
        if x1 <= x <= x2 and y1 <= y <= y2:
            selected_astre = i
            break

m1=6e24   #masse de la terre
m2=6e24
astre = [0]*2   #liste servant a modifier les references des dessins
x =[50., 350.]
y = [100., 100.]

#fenetre
fen = Tk()
fen.title("Gravitation universelle selon Newton")
selected_astre = -1

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
astre[1] = can.create_oval(x[1] -10, y[1]-10, x[1]+10, y[1]+10, fill ="red")

fra1 = Frame(fen)
fra1.grid(row =4, column = 0, sticky = W, padx =10)
Button(fra1, text ="astre 1", command = choisir_astre).pack(side = LEFT)

fra2 = Frame(fen)
fra2.grid(row =4, column = 0, sticky = E, padx =10)
Button(fra2, text ="astre 2", command = choisir_astre).pack(side = RIGHT)
# bind les événements du clic gauche sur le canevas pour le déplacement des astres
can.bind("<Button-1>", deplacer_astre)
can.bind("<Button-3>", choisir_astre)

fen.mainloop()
