n = int(input())
# Branje in urejanje podatkov
for a in range(n):
    stev = input()
    # Dodamo '+' na konec 'stev' kot nevrednosti element
    # za lažje branje podatkov
    stev += '+'
    stevilka = ''
    for b in range(len(stev)-1):
        # Se sprehodimo po 'številki'
        # In z pogoji 'lepše' zapišemo število
        if stev[b] != ',':
            stevilka += stev[b]
        else:
            if stev[b+1] == ',' or stev[b+1] == '+':
                stevilka += ',0'
            else:
                stevilka += ','
    # stev razdelimo pri ',' in števila spremenimo iz nizov v cela števila            
    tab = [int(x) for x in stevilka.split(',')][::-1]
    rez = 0
    for i in range(len(tab)):
        # Se sprehodimo po tabeli števil in rezultatu ustrezno prištevamo
        # vrednosti po 'seksagesimalnemu' sistemu
        rez += tab[i] * (60**i)
    print(rez)

