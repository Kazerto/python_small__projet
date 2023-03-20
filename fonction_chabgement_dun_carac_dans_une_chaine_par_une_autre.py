"""Définissez une fonction changeCar(ch,ca1,ca2,debut,fin) qui remplace tous les caractères
ca1 par des caractères ca2 dans la chaîne de caractères ch, à partir de l’indice debut et jusqu’à
l’indice fin, ces deux derniers arguments pouvant être omis (et dans ce cas la chaîne est traitée
d’une extrémité à l’autre). Exemples de la fonctionnalité attendue :
>>> phrase = 'Ceci est une toute petite phrase.'
>>> print(changeCar(phrase, ' ', '*'))
Ceci*est*une*toute*petite*phrase.
>>> print(changeCar(phrase, ' ', '*', 8, 12"""

def changeCar(ch,ca1,ca2,debut=0,fin=-1):
    if fin ==-1:
        fin = len(ch)
    nch= ""
    i=0
    while i<len(ch):
        if i>=debut and i <=fin and ch[i]==ca1:
            nch= nch + ca2
        else:
            nch = nch + ch[i]
        i = i+1    
    return nch

phrase = "Ceci est une toute petite phrase"
print(changeCar(phrase, " ", "*"))

