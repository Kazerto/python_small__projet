#affichage d'un petit cercle rouge a chaque clique
from tkinter import *
#la fonction pointeur permet d'afficher les coordonnées de chaque clique gauche
#sans oublier de remplacer le Canvas par Frame
"""def pointeur(event):
    chaine.configure(text= "Clic detecté en X =" + str(event.x) +\
                        ", Y =" + str(event.y))"""
#creation du cercle

def petit_rond_rouge(event):
    cadre.delete(ALL) #permet de nettoyer après chaque clique pour eviter une accummulation de clique
    x=event.x
    y=event.y
    cadre.create_oval(x-10,y-10,x+10,y+10, fill= "red")
    
fen = Tk()
cadre = Canvas(fen,width = 200, height = 150, bg="light yellow")
cadre.bind("<Button-1>", petit_rond_rouge)
#pour le boutton droit de la souris c'est <Button-3>
cadre.pack()


fen.mainloop()

"""Button Un bouton classique, à utiliser pour provoquer l’exécution d’une commande
quelconque.
Canvas Un espace pour disposer divers éléments graphiques. Ce widget peut être
utilisé pour dessiner, créer des éditeurs graphiques, et aussi pour implémenter
des widgets personnalisés.
Checkbutton Une case à cocher qui peut prendre deux états distincts (la case est cochée ou
non). Un clic sur ce widget provoque le changement d’état.
Entry Un champ d’entrée, dans lequel l’utilisateur du programme pourra insérer un
texte quelconque à partir du clavier.
Frame Une surface rectangulaire dans la fenêtre, où l’on peut disposer d’autres
widgets. Cette surface peut être colorée. Elle peut aussi être décorée d’une
bordure. 
Label Un texte (ou libellé) quelconque (éventuellement une image).
Listbox Une liste de choix proposés à l’utilisateur, généralement présentés dans une
sorte de boîte. On peut également configurer la Listbox de telle manière
qu’elle se comporte comme une série de « boutons radio » ou de cases à
cocher.
Menu Un menu. Ce peut être un menu déroulant attaché à la barre de titre, ou bien
un menu « pop up » apparaissant n’importe où à la suite d’un clic.
Menubutton Un bouton-menu, à utiliser pour implémenter des menus déroulants.
Message Permet d’afficher un texte. Ce widget est une variante du widget Label, qui
permet d’adapter automatiquement le texte affiché à une certaine taille ou à
un certain rapport largeur/hauteur.
Radiobutton Représente (par un point noir dans un petit cercle) une des valeurs d’une
variable qui peut en posséder plusieurs. Cliquer sur un bouton radio donne la
valeur correspondante à la variable, et « vide » tous les autres boutons radio
associés à la même variable.
Scale Vous permet de faire varier de manière très visuelle la valeur d’une variable,
en déplaçant un curseur le long d’une règle.
Scrollbar Ascenseur ou barre de défilement que vous pouvez utiliser en association avec
les autres widgets : Canvas, Entry, Listbox, Text.
Text Affichage de texte formaté. Permet aussi à l’utilisateur d’éditer le texte affiché.
Des images peuvent également être insérées.
Toplevel Une fenêtre affichée séparément, au premier plan"""