x = [int(a) for a in input().split()]
visina, sirina = x[0], x[1]
# Naredimo mapo kjer je vsaka tabela en stoplec mape
mapa = ['' for b in range(sirina)] 
for i in range(visina):
    niz = list(input())
    for c in range(sirina):
        mapa[c] += niz[c]
# Sestavljamo novo mapo, z vsakim stolpom posebej
nova_mapa = []
for stolpec in mapa:
    nov_stolp = ''
    stolp = stolpec[::-1]  # Obrnemo, tako da so 'tla' pred indeksom 0
                           # 'gravitacija' torej vleče iz desne proti levi
    if '#' in stolp:
        # V primeru da je v stolpu ovira,
        # niz 'razbijemo' na dele katere ločuje ovira
        razbit = stolp.split('#')
        stevec = 0
        for delcek in razbit:
            stevec += 1
            # Če pregledujemo zadnji del ne dodamo znaka '#'
            # Ker smo tega dodali pri prejšnjem 
            if stevec == len(razbit): znak = ''
            else: znak = '#'
            # Preštejemo jabolke('a') v posameznem delu
            # Ter primerno ustvarimo del niza posameznega novega stolpa
            st_jab = delcek.count('a')
            nov_stolp += st_jab * 'a' + (len(delcek) - st_jab) * '.' + znak       
    else:
        # V primeru da znaka '#' ni v stolpu enostavno sestavimo nov stolp
        # Preštejemo jabolka('a') ter jih ustrezno izpišemo po vrstnem redu
        st_jab = stolp.count('a') 
        nov_stolp = st_jab * 'a' + (len(stolp) - st_jab) * '.'
        
    nova_mapa.append(nov_stolp[::-1])
    
# Izpis, upoštevamo, da smo mapo narobe 'zgradili' in jo zato ustrezno obrnemo
# in izpišemo.
for a in range(visina):
    for b in range(sirina):
        if b == sirina -1: pomoc = '\n'
        else: pomoc = ''
        print(nova_mapa[b][a], end = pomoc)
    
    
