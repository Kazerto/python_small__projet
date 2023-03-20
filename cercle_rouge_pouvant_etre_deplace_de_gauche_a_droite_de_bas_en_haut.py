from tkinter import *
#procedure general de deplacement
def avance(gd, hb):
    global x1, y1
    x1, y1= x1 + gd, y1 + hb
    can1.coords(oval1, x1, y1, x1 + 30, y1 + 30)
    
#getionnaire d'evennment
def depl_gauche():
    avance(-10,0)
    
def depl_droit():
    avance(10,0)
    
def depl_bas():
    avance(0,10)
    
def depl_haut():
    avance(0,-10)
    
#prog principal
x1, y1 = 10, 10
#creation de widget principal
fen1 = Tk()
fen1.title("Exercice d'animation avec Tkinter")

#creation de widget
can1=Canvas(fen1, width = 300, height = 300, bg="dark grey")
oval1=can1.create_oval(x1,y1,x1+30,y1+30, fill= "red", width= 2)
can1.pack(side = LEFT)
Button(fen1, text = "Gauche",bg = "dark grey", command = depl_gauche ).pack()
Button(fen1, text = "Droite", bg = "dark grey", command = depl_droit).pack()
Button(fen1, text= "Haut", bg="dark grey", command = depl_haut).pack()
Button(fen1, text = "Bas", command= depl_bas).pack()
Button(fen1, text = "Quitter", command = fen1.quit).pack(side = BOTTOM)

fen1.mainloop()

