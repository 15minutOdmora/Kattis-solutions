def pretvori_v_sec(cas_zadetka):
    #Pretvori čas v sekunde
    m, s = cas_zadetka.split(':')
    return int(m) * 60 + int(s)

def pretvori_nazaj(cas_sekunde):
    #Pretvori sekunde nazaj v ustrezen čas
    min = cas_sekunde // 60
    sec = cas_sekunde % 60
    if sec < 10:
        sec = '0' + str(sec)
    else:
        sec = str(sec)
    return str(min) + ':' + sec

n = int(input())
#Prvi vhod, ki nam pove število zadetih metov (število vhodnih vrstic)
vodstvo = 0
#Na začetku je izenačeno 
tabelatock = [[0,0]]
#V tabelo damo začetno stanje
while n > 0:
    zadetek = str(input()).split(' ')
    #Razdelimo pri presledkih
    zadetek[1] = int(zadetek[1])
    #Drugi elt. je število pik zato ga ustrezno pretvorimo
    zadetek[2] = pretvori_v_sec(zadetek[2])
    #Treti elt. je čas zadetega meta, pretvorimo v sekunde za lažje računanje
    cas = zadetek[2]
    if zadetek[0] in 'H':
        vodstvo += zadetek[1]
    if zadetek[0] in 'A':
        vodstvo -= zadetek[1]
    tabelatock.append([vodstvo,cas])
    #Preverimo katera ekipa je dosegla točke
    #Vodstvo nam pove katera ekipa vodi v določenem času
    #Vodstvo = 0 je izenačeno, < 0 vodi gostujoča ekipa (A), > 0 vodi domača ekipa (H)
    #V tabelo dodamo vodstvo ter takratni čas 
    n -= 1
zaccash = 0
zaccasa = 0
koncash = 0
koncasa = 0
#Spremenljivke za čas začetka in konca vodstva za posamezno ekipo
vodstvoh = 0
vodstvoa = 0
#Spremenljivke za seštevanje časa vodstva posamezne ekipe
for a in range(1,len(tabelatock)):
    #Preverjali bomo prejšnji čas z trenutnim ter prejšnje vodstvo z trenutnim
    #Zato zanko začnemo pri 1 
    prejkoef = tabelatock[a-1][0]
    koef = tabelatock[a][0]
    prejcas = tabelatock[a-1][1]
    cas = tabelatock[a][1]
    
    if prejkoef == 0:
        if koef > 0:
            zaccash = cas
        if koef < 0:
            zaccasa = cas
    #Če je bilo prej izenačeno bo zdej ena ekipa povedla, začnemo čas vodstva ustrezni ekipi
    
    elif prejkoef > 0:
        if koef < 0:
            zaccasa = cas
            koncash = cas
        #Če je prej vodila ekipa 'H'(preneha vodit) in zdej vodi ekipa 'A'(začne vodit)
        if koef == 0:
            koncash = cas
        #Če je izenačeno, ekipa 'H' preneha vodit 
            
    elif prejkoef < 0:
        if koef > 0:
            zaccash = cas
            koncasa = cas
        #Če je prej vodila ekipa 'A'(preneha vodit) in zdej vodi ekipa 'H'(začne vodit)
        if koef == 0:
            koncasa = cas
        #Če je izenačeno, ekipa 'A' preneha vodit
            
    if a == len(tabelatock)-1:
    #Če je to zadnji koš celotne tekme
        if prejkoef > 0:
            if koef < 0 or koef == 0:
                vodstvoh += koncash - zaccash
            if koef > 0:
                vodstvoh += cas - zaccash
        elif prejkoef < 0:
            if koef > 0 or koef == 0:
                vodstvoa += koncasa - zaccasa
            if koef < 0:
                vodstvoa += cas - zaccasa
        #preverimo če je prišlo do sprememb vodstva
        #In čase ustrezno seštejemo (cas = trenutni čas)
                
        if koef > 0:
            vodstvoh += 1920 - cas
        elif koef < 0:
            vodstvoa += 1920 - cas
        #Ekipa ki vodi po zadnjem zadetem metu vodi do konca tekme
        # zato ji dodamo čas, ki se še ni iztekel
        # 1920s = 32 min. kar je celoten čas tekme
        
    else:
        if prejkoef > 0:
            if koef < 0 or koef == 0:
                vodstvoh += koncash - zaccash
            
        elif prejkoef < 0:
            if koef > 0 or koef == 0:
                vodstvoa += koncasa - zaccasa
    #preverimo če je prišlo do sprememb vodstva
    #In čase ustrezno seštejemo
                
if koef > 0:
    print('H' + ' ' + pretvori_nazaj(vodstvoh)+ ' '  + pretvori_nazaj(vodstvoa))
elif koef < 0:
    print('A' +' '+ pretvori_nazaj(vodstvoh) + ' ' + pretvori_nazaj(vodstvoa))       
#Preverimo katera ekipa je zmagala in to ustrezno izpišemo    
