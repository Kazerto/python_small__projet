from tkinter import *
from random import randrange
#definition de fonction gestionnaire d'evenement
def drawline():
    #tracer d'une ligne dans le canevas
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    can1.update()
    #modifiaction des coordonnes
    y2,y1 = y2+10, y1-10
    
def changecolor():
    #changement de couleur
    global coul
    pal = ["purple","cyan","maroon","green","red","blue","orange","yellow"]
    c = randrange(8)
    coul=pal[c]
    
#programme principal
#variables utilisés de manière global
x1,y1,x2,y2 = 10, 190, 190, 10
coul='dark green'
fen1 = Tk()
can1=Canvas(fen1,bg='dark grey', height = 200, width = 200)
bou1=Button(fen1,text ="quitter" ,command = fen1.quit)
bou1.pack(side = BOTTOM)
bou2=Button(fen1, text = "Tracer une ligne", command = drawline)
bou2.pack()
bou3=Button(fen1, text ="Autre couleur", command = changecolor)
bou3.pack()

fen1.mainloop()
fen1.destroy()