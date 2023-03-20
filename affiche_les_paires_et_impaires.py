t2=[32,5,12,8,3,75,2,15]
tpaire=[]
timpaire=[]
i=0
while i<len(t2):
    if t2[i]%2 == 0:
        tpaire.append(t2[i])
    else:
        timpaire.append(t2[i])
        
    i=i+1
    
print(tpaire,timpaire)
""" Écrivez un programme qui analyse un par un tous les éléments d’une liste de nombres (par
exemple celle de l’exercice précédent) pour générer deux nouvelles listes. L’une contiendra
seulement les nombres pairs de la liste initiale, et l’autre les nombres impairs. Par exemple, si la
liste initiale est celle de l’exercice précédent, le programme devra construire une liste pairs
qui contiendra [32, 12, 8, 2], et une liste impairs qui contiendra [5, 3, 75, 15]. Astuce :
pensez à utiliser l’opérateur modulo (%) déjà cité précédemment."""