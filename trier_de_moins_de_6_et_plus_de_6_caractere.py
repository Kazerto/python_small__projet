liste =['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
t1=[]
t2=[]
i=0

while i<len(liste):
    if len(liste[i])<6:
        t1.append(liste[i])
    else:
        t2.append(liste[i])
        
    i=i+1
    
print(t1,t2)

""" Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots (par
exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']) pour
générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères,
l’autre les mots comportant 6 caractères ou davantage."""