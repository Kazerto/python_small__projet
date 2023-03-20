note = []
enr = 1
while enr>=0:
    
    print("veuillez entrer la note : ")
    enr=int(input())
    if enr <0:
        print("vous avez saisi une note negative, recommencez")
    else:
        note.append(enr)
        note_basse = 0
        note_haute = 0
        note_moy = 0
        i=0
        while i <len(note):
            #iteration de la moyenne
            note_moy = note_moy + note[i]
            
            if i < len(note):
                note_basse = note[i]
            if i> len(note):
                note_haute = note[i]
        
        i=i+1    
        
    #moyenne    
        note_moy = note_moy/len(note)    
   
    
print(len(note),note_basse,note_haute,note_moy)
    
    
    
    """notes = []
n = 2 
while n >= 0 : 
    print("Entrez la note ") 
    n = float(input()) 
    if n < 0 : 
        print("OK. Terminé.") 
    else:
        notes.append(n) 
        max = 0
        tot = 0
        i = 0
        min = 100
        long = len(notes) 
        while i < long:
            if notes[i] > max:
                max = notes[i] 
            if notes[i] < min: 
                min = notes[i] 
            tot = tot + notes[i] 
            moy = tot/long 
            i = i + 1 
print(long, "notes entrées. Max =", max, "Min =", min, "Moy =", moy)"""