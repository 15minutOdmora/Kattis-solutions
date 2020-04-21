# Branje podatkov
psi = input().split(' ')
pes1 = [int(psi[0]),int(psi[1])]
pes2 = [int(psi[2]),int(psi[3])]
ljudje = input().split(' ')
for a in range(len(ljudje)):
    ljudje[a] = int(ljudje[a])
tabp1 = []
tabp2 = []
# Zanka za zapisovanje stanja psov
for a in range(max(ljudje)):
    # Zanka do največjega časa pri ljudeh
    # Nepotrebno predolga
    if a % 2 != 0:
        # Ko pes miruje (ker je prvi indeks 0 je obratno kot bi po logiki sklepali) 
        for b in range(pes1[1]):
            tabp1.append(False)
        for b in range(pes2[1]):
            tabp2.append(False)
        # Toliko časa kot je pes miren tolikokrat se shrani 'False'
    elif a % 2 == 0:
        # Ko je pes agresiven
        for b in range(pes1[0]):
            tabp1.append(True)
        for b in range(pes2[0]):
            tabp2.append(True)
        # Toliko časa kot je pes agresiven tolikokrat se shrani 'True'
for c in ljudje:
    # Preverjamo koliko psov je agresivnih za določen čas prihoda
    # c zavzame vrednost, ki je enaka času prihoda
    # c = (c-1)-tem mestu v tabeli 
    # Ustrezno izpišemo
    if tabp1[c-1] and tabp2[c-1]:
        print('both')
    elif tabp1[c-1] or tabp2[c-1]:
        print('one')
    else:
        print('none')