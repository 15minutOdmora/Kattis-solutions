from sys import stdin, stdout
# Slovar elementov periodnega sistema, urejeni po abecedi
# kjer so ključi enaki začetnim črkam elementov
sez = {'a': ['ac', 'ag', 'al', 'am', 'ar', 'as', 'at', 'au'],
       'b': ['b', 'ba', 'be', 'bh', 'bi', 'bk', 'br'],
       'c': ['c', 'ca', 'cd', 'ce', 'cf', 'cl', 'cm',
             'cn', 'co', 'cr', 'cs', 'cu'],
       'd': ['db', 'ds', 'dy'],
       'e': ['er', 'es', 'eu'],
       'f': ['f', 'fe', 'fl', 'fm', 'fr'],
       'g': ['ga', 'gd', 'ge'],
       'h': ['h', 'he', 'hf', 'hg', 'ho', 'hs'],
       'i': ['i', 'in', 'ir'],
       'k': ['k', 'kr'],
       'l': ['la', 'li', 'lr', 'lu', 'lv'],
       'm': ['md', 'mg', 'mn', 'mo', 'mt'],
       'n': ['n', 'na', 'nb', 'nd', 'ne', 'ni', 'no', 'np'],
       'o': ['o', 'os'],
       'p': ['p', 'pa', 'pb', 'pd', 'pm', 'po', 'pr', 'pt', 'pu'],
       'r': ['ra', 'rb', 're', 'rf', 'rg', 'rh', 'rn', 'ru'],
       's': ['s', 'sb', 'sc', 'se', 'sg', 'si', 'sm', 'sn', 'sr'],
       't': ['ta', 'tb', 'tc', 'te', 'th', 'ti', 'tl', 'tm'],
       'u': ['u'],
       'v': ['v'],
       'w': ['w'],
       'x': ['xe'],
       'y': ['y', 'yb'],
       'z': ['zn', 'zr']}

    
def najdi_elemente(zacetek = 0):
    '''Rekurzivno pregleduje ali se niz, da sestaviti iz nizov v tabeli,
        začetek je enak 0, ker niz pregledujemo od 1. črke naprej'''
    if zacetek == len(niz):
        # Če je vrednost enaka dolžini niza pomeni, da smo prišli do konca
        # in se niz da sestaviti iz elementov. Vrnemo True
        return True
    
    if niz[zacetek] in sez:
        # Če je določena črka v slovarju kot niz
        for element in sez[niz[zacetek]]:
            # Se sprehajamo po elt.ih, ki se začnejo z ujemajoče se črko
            if element == niz[zacetek : zacetek + len(element)]:
                # V primeru, da se ujemajo rekurzivno kličemo funkcijo
                if najdi_elemente(zacetek + len(element)):
                    # Če rekurzivno klicana funk. vrne True
                    # pomeni, da smo prišli do konca niza
                    return True
    # Če pridemo do sm, se niz ne da sestaviti, vrnemo None             
    return None
    
# Branje vhodnih podatkov, klicanje funkcije in izpisovanje rezultata
st_vhodov = int(stdin.readline())
for a in range(st_vhodov):
    niz = stdin.readline().strip('\n')
    if najdi_elemente() == True:
        print('YES')
    else:
        print('NO')

