import sys
sys.setrecursionlimit(999999)
# Branje podatkov
velikost = [int(x) for x in input().split()]
# [0] = višina, [1] = širina
mapa = list()
# Mapi dodamo obrobo iz '0' kar predstavlja morje
mapa.append(list('0'*(velikost[1] + 2)))
for a in range(velikost[0]):
    mapa.append(list('0' + input() + '0'))
mapa.append(list('0'*(velikost[1] + 2)))
        
def floodFill(mapa, x, y, stara, nova):
    '''Rekurzivno zamenjamo vse zunanje('0') z novim znakom'''
    sirina = len(mapa)
    visina = len(mapa[0])
    if stara == None:
        stara = mapa[x][y]
    if mapa[x][y] != stara:
        # Če trenutni znak ni enak staremu, ne vrnemo nič
        return

    # Spremenimo stari znak v novega
    mapa[x][y] = nova 
    
    # Rekurzivno kličemo, dokler nismo na meji mape, katero bi sprožilo napako
    if x > 0: # levo
        floodFill(mapa, x-1, y, stara, nova)        
    if y > 0: # gor
        floodFill(mapa, x, y-1, stara, nova)
    if x < sirina-1: # desno
        floodFill(mapa, x+1, y, stara, nova)        
    if y < visina-1: # dol
        floodFill(mapa, x, y+1, stara, nova)
        
nova = 'x'
floodFill(mapa,0,0,'0',nova)
obala = 0
# Preštejemo dolžino obale 
for a in range(1,len(mapa)-1):
    vrsta = mapa[a]
    # sprehajamo po znakih v vrsti
    for b in range(1,len(vrsta)-1):
        stev = 0
        znak = vrsta[b]   
        # če je znak enak 1 preverjamo 'sosede'
        if znak == '1':
            if mapa[a-1][b] == nova: stev += 1
            if mapa[a][b-1] == nova: stev += 1
            if mapa[a][b+1] == nova: stev += 1
            if mapa[a+1][b] == nova: stev += 1
        # Odvisno koliko sosedov ima '1', tolko obale zasega tisti kos
        obala += stev
# Izpišemo rešitev
print(obala)

