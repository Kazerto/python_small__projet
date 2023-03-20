from tkinter import *
from math import *

#calcul des distances
def distance(x1,y1,x2,y2):
    d = sqrt((x2-x1)**2+(y2-y1)**2)
    return d

#la froce
def force(m1, m2, di):
    return m1*m2*(6*10**-11)/di**2

#fonction selection astre
def selecte_astre(event):
    global choix
    #on a choisi l'astre 
    if event.x >= x[0]-10 and event.x <=[0]+10 and event.y >= y[0]-10 and event.y <= y[0]+10:
        choix = 0
    elif event.x >=x[1]-10 and event.x <=x[1]+10 and event.y >= y[1]-10 and event.y <=y[1]+10:
        choix = 1
        
    
def deplacement(event):
    global x,y, choix
    if choix != -1:
        x[choix] = event.x , y[choix] = event.y
        can.coords(astre[choix], x[choix]-10, y[choix]-10, x[choix]+10, y[choix]+10)
        di = distance(x[0],y[0],x[1],y[1])
        diA = di*1e9
        f = force(m1,m2,diA)
        
        valDis.configure(text = "Distance =" + str(diA)+"m" )
        valFor.configure( text = "Force =" +str(f)+"N")
        
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
valFor.grid(row = 3, column =1)

#canevas de dessin 
can = Canvas(fen, width= 400, height= 200, bg= "ivory")
can.grid(row = 2, column = 0, columnspan= 2)
astre[0] = can.create_oval(x[0]-10, y[0]-10, x[0]+10, y[0]+10, fill ="blue", width=2)
astre[1] = can.create_oval(x[1] -10, y[1]-10, x[1]+10, y[1]+10)

#creation de 4 boutons pour chacun des astres
fra1 = Frame(fen)
fra1.grid(row =4, column = 0, sticky = W, padx = 10)
Button(fra1, text = "astre 1", command= selecte_astre).pack(side = LEFT)
can.bind("<Button-1>",deplacement)



fra2 = Frame(fen)
fra2.grid(row = 4, column = 1,sticky = E, padx =10)
Button(fra2, text = "astre 2", command = selecte_astre).pack(side = LEFT)
can.bind("<Button-1>",deplacement)

fen.mainloop()