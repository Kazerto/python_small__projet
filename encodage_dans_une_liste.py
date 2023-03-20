liste = []
code = "ok" 
while code !="":
    print("veuillez entrer une valeur : ")
    code = int(input())
    if code != "":
        liste.append(code)       
    
              
print(liste) 
""" Écrivez un programme qui permette d’encoder des valeurs dans une liste. Ce programme
devrait fonctionner en boucle, l’utilisateur étant invité à entrer sans cesse de nouvelles
valeurs, jusqu’à ce qu’il décide de terminer en frappant <Enter> en guise d’entrée. Le
programme se terminerait alors par l’affichage de la liste. Exemple de fonctionnement :"""