from tkinter import *
#definition des gestionnaire d'evenement

def move():
    global x1, y1, dx, dy, flag, coul
    x1, y1 = x1 + dx, y1 + dy
    if x1 > 210:
        x1, dx, dy = 210, 0, 15
        coul ="green"
    if y1 >210:
        y1, dx , dy = 210, -15, -15
        coul = "black"
    if x1 < 10:
        x1, dx, dy = 10, 15, -15
        coul = "yellow"
    if y1 < 10:
        y1, dx, dy =10, -15, 15
        coul = "red"
        
    can1.itemconfigure(oval1, fill =coul)
    can1.coords(oval1,x1,y1,x1+30,y1+30)
    if flag >0:
        fen1.after(50,move)
        
def stop_it():
    "arret de l'animation"
    global flag
    flag =0
    
def start_it():
    "demarrage de l'animation"
    global flag
    if flag ==0:
        flag =1
        move()
        
#programme principal
x1,y1 = 10, 10
dx,dy =15,15
flag = 0
coul = "red"


#creation du widget principale
fen1=Tk()
fen1.title("Exercice d'animation avec Tkinter")

#ceation ds widgets enfant
can1 =Canvas(fen1, width= 250, height= 250, bg ="dark grey")
can1.pack(side =LEFT, padx = 5, pady =5)

oval1= can1.create_oval(x1,y1,x1+30,y1+30, fill = "red", width = 2)
bou1 = Button(fen1, text = "Démarrer", command = start_it).pack()
bou2 = Button(fen1, text = "Arreter", command = stop_it).pack()
bou3 = Button(fen1, text = "Quitter", command = fen1.quit).pack(side =BOTTOM)

fen1.mainloop()

