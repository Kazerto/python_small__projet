import tkinter as tk
import math

# Initialisation du canevas Tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

# Initialisation des cercles
x1, y1 = 100, 100
x2, y2 = 200, 200
r = 50
circle1 = canvas.create_oval(x1-r, y1-r, x1+r, y1+r, fill="blue")
circle2 = canvas.create_oval(x2-r, y2-r, x2+r, y2+r, fill="red")

# Initialisation des étiquettes de coordonnées
label1 = tk.Label(root, text=f"({x1}, {y1})", font=("Helvetica", 10))
label2 = tk.Label(root, text=f"({x2}, {y2})", font=("Helvetica", 10))
label1.place(x=x1+r, y=y1-r)
label2.place(x=x2+r, y=y2-r)

# Fonction de déplacement des cercles
def move_circle(event):
    global x1, y1, x2, y2
    dx = event.x - canvas.canvasx(0)  # Position x de la souris
    dy = event.y - canvas.canvasy(0)  # Position y de la souris
    if event.widget == canvas:  # Si l'événement vient du canevas
        # Déplacement du cercle 1
        if abs(dx-x1) <= r and abs(dy-y1) <= r:
            canvas.move(circle1, dx-x1, dy-y1)
            x1, y1 = dx, dy
            label1.place(x=x1+r, y=y1-r)
            label1.config(text=f"({x1}, {y1})")
        # Déplacement du cercle 2
        elif abs(dx-x2) <= r and abs(dy-y2) <= r:
            canvas.move(circle2, dx-x2, dy-y2)
            x2, y2 = dx, dy
            label2.place(x=x2+r, y=y2-r)
            label2.config(text=f"({x2}, {y2})")
    
# Ajout de l'écouteur d'événement de souris
canvas.bind("<Button-1>", move_circle)

root.mainloop()


