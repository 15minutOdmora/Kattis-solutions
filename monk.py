def premica(p1, p2):
    '''Vrne '''
    return p1[1] - p2[1], p2[0] - p1[0], p2[0]*p1[1] -p1[0]*p2[1]

def presecisce(L1, L2):
    '''Vrne točko v katerih se premici L1 in L2 sekata''' 
    D = L1[0] * L2[1] - L1[1] * L2[0]
    if D != 0:
        return [(L1[2] * L2[1] - L1[1] * L2[2]) / D,(L1[0] * L2[2] - L1[2] * L2[0]) / D] 
    else:
        return False
#Branje podatkov 
x = input().split(' ')
if int(x[0]) > 5000: x[0] = 5000
if int(x[1]) > 5000: x[1] = 5000
# Tabeli gor dodamo prvi element [0,0] ker se tam začne pot navzgor
gor, dol = [[0,0]], []
for a in range(int(x[0])):
    neki = [int(x) for x in input().split(' ')]
    # Obrnemo v tabeli da postavimo čas na x-os višinsko razliko pa na y-os
    gor.append(neki[::-1])
for a in range(int(x[1])):
    nekaj = [int(x) for x in input().split(' ')]
    dol.append(nekaj[::-1])
# Seštevanje trenutnih sprememb časa in višine
# To naredimo zato, da dobimo točke na grafu skozi katere bi menih hodu
# S tem lahko skonstruiramo graf višine v odvisnosti od časa
skup = [0,0]
for a in range(0,len(gor)):
    # Zanka za seštevanje x in y koordinat poti gor
    skup = [skup[0] + gor[a][0], skup[1] + gor[a][1]]
    gor[a] = [skup[0],skup[1]]
# Tabeli novidol in skup1 dodamo prvi element, ki ima x = 0, y = zadnji višini, ki jo menih
# doseže na poti gor
# Pot navzdol 'zrcalimo' preko y-osi
skup1 = [0,gor[-1][1]]
novidol = [[0,gor[-1][1]]]
for a in range(0,len(dol)):
    # Čase(x-os) seštevamo, Višino(y-os) odštevamo, ker gre pot navzdol
    skup1 = [skup1[0] + dol[a][0],skup1[1] - dol[a][1]]
    # Dodajamo v tabelo v vsakem krogu zanke
    novidol.append([skup1[0],skup1[1]])
dol = novidol
# Se 'sprehodimo' po tabelah točk gor in dol
for a in range(len(gor)-1):
    for b in range(len(dol)-1):
        gorc = premica(gor[a],gor[a+1])
        dolc = premica(dol[b],dol[b+1])
        # Pod pogojem da je presečišče med premicami
        if presecisce(gorc,dolc):
            tes = presecisce(gorc,dolc)
            # Pogoj da je višina točke navzgor manjša od točke presečišča
            # ter da je višina naslednje točke večja
            # Nasprotno velja za dve točki navzdol
            if gor[a][1] <= tes[1] <= gor[a+1][1] and dol[b+1][1] <= tes[1] <= dol[b][1]:
                # Enako preverjamo za čas posameznih točk 
                if gor[a][0] <= tes[0] <= gor[a+1][0] and dol[b][0] <= tes[0] <= dol[b+1][0]:
                    # V primeru da oba pogoja veljata izpišemo x-koordinato presečišča in zaključimo zanko
                    print('{0:.6f}'.format(tes[0]))
                    break 