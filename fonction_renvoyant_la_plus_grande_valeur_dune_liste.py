def eleMax(liste,debut=0,fin=-1):
    if fin==-1:
        fin=len(liste)
    i=0; max=0
    while i<fin:
        if liste[i]>max and i>=debut and i<=fin:
            max = max + liste[i]
        i=i+1
    return max

serie = [9, 3, 6, 1, 7, 5, 4, 8, 2]
print(eleMax(serie, fin =3, debut =1))
