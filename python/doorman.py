import math 
razlika = int(input())
x = str(input())
#Prejmemo vhodne podatke
vrsta = []
for a in x:
    if a in 'M':
       vrsta.append(-1) 
    elif a in 'W':
        vrsta.append(1)
    #Se "sprehodimo" po vrsti in spreminjamo znaka v števili (1 ali -1)
trenutno = 0
stevec = 0
for a in range(0,len(vrsta)-1):
    #Zadnji element preskočimo, da lahko preverjamo trenutni in naslednji elt.
    if abs(trenutno + vrsta[a]) > abs(trenutno + vrsta[a+1]):
        krneki = vrsta[a]
        vrsta[a]=vrsta[a+1]
        vrsta[a+1]= krneki
        #V primeru, da je naslednji elt. bolj primeren kot trenutni
        # ta dva zamenjamo 
    if abs(trenutno + vrsta[a]) > razlika:
        break
        #Če je razlika prevelika ustavimo zanko 
    trenutno += vrsta[a]
    stevec += 1
if abs(trenutno + vrsta[stevec]) <= razlika:
    stevec += 1
    #Ob končani zanki preverimo še naslednji (ali zadnji) elt. če bi bil primeren
print(stevec)


    
