from tkinter import *
fen1 = Tk()
fen1.title("yesssssssss")
#creation de label et Entry
Label(fen1, text = "Premier champ :").grid(row = 0, sticky =E)
Label(fen1, text = "Second :").grid(row = 1,sticky = E)
Label(fen1, text = "Troisième :").grid(row = 2, sticky = E)
entr1 = Entry()
entr2 = Entry()
entr3 = Entry()
entr1.grid(row = 0, column = 1)
entr2.grid(row = 1, column = 1)
entr3.grid(row = 2, column = 1)
chek1 = Checkbutton(fen1, text ='Case à cocher, pour voir')
chek1.grid(columnspan =2)
#creation d'un widget canvas
can1 = Canvas(fen1, width=160, height= 160, bg = "white")
photo = PhotoImage(file = "aac.png")
can1.create_image(80,80, image = photo)
can1.grid(row = 0,column=2, rowspan=3, padx= 10, pady=5)

#mise en page


fen1.mainloop() 

