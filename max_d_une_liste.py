
t2=[32,5,12,8,3,75,2,15]
maximum = 0
i =0
while i < len(t2):
    if t2[i] > maximum:
        maximum = t2[i]
        
    i=i+1
        
print("le plux grand élément de cette liste a la valeur 75")
"""Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. Par
#exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15], ce programme devrait
#afficher :
#le plus grand élément de cette liste a la valeur 75//"""