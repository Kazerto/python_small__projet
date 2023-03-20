from tkinter import *
def cercle(x,y,r,coul="black"):
    #tracé d'un cercle de centre (x,y) et de rayon r
    can.create_oval(x-r,y-r,x+r,y+r, outline = coul)
    
def figure_1():
        #eeffacer tout dessin
        can.delete(ALL)
        #tracer deux ligne horizontal et vertical
        can.create_line(100,0,100,200, fill ='blue')  #horizontal
        can.create_line(0,100,200,100, fill='blue')  #vertical
        #tracer de plusioeur cercles
        rayon = 15
        while rayon <100:
            cercle(100,100,rayon)
            rayon +=15
    

def figure_2():
    "dessiner un visage simplifié"
    #effacer d'abord tout dessin preexistant
    can.delete(ALL)
    # Les caractéristiques de chaque cercle sont
    # placées dans une liste de listes :
    cc =[[100, 100, 80, 'red'], # visage
         [70, 70, 15, 'blue'], # yeux
         [130, 70, 15, 'blue'], 
         [70, 70, 5, 'black'], 
         [130, 70, 5, 'black'],
         [44, 115, 20, 'red'], # joues
         [156, 115, 20, 'red'],
         [100, 95, 15, 'purple'], # nez
         [100, 145, 30, 'purple']] # bouche
    #on trace tous les cercles a l'aide d'une boucle
    i=0
    while i< len(cc):
        el = cc[i]
        cercle(el[0], el[1], el[2], el[3])
        i+=1
        
#programme principal
fen=Tk()
can=Canvas(fen, width = 200, height= 200, bg= 'ivory')
can.pack(side =TOP, padx = 5, pady =5)
b1=Button(fen, text= "dessin 1", command=figure_1)
b1.pack(side = LEFT, padx=3, pady=3)
b2=Button(fen, text= "dessin 2", command=figure_2)
b2.pack(side= RIGHT, padx=3, pady=3)
b3=Button(fen, text ="quitter", command=fen.quit)
b3.pack(side = BOTTOM, padx=3, pady =3)
fen.mainloop()

