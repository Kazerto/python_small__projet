import tkinter as tk

# Création de la fenêtre principale
root = tk.Tk()

# Création du canvas
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Dessiner le damier
size = 30 # Taille d'une case
for i in range(10):
    for j in range(10):
        x1 = i * size
        y1 = j * size
        x2 = x1 + size
        y2 = y1 + size
        if (i + j) % 2 == 0:
            canvas.create_rectangle(x1, y1, x2, y2, fill="white")
        else:
            canvas.create_rectangle(x1, y1, x2, y2, fill="black")

# Afficher la fenêtre
root.mainloop()
