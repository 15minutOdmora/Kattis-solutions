import sys
liam = True
prva = True
while liam:
    n = int(input())
    #Prvi vhod, pri kateremu preverjamo začetek ali konec vhodov
    if n == 0:
        liam = False 
        break
    #Če je vhod enak 0 vstavimo zanko
    if prva:
        prva = not prva
    else:
        sys.stdout.write('\n')
    #Če je prva vrstica spustimo prvi presledek
    tab_tab = []
    pravilnostna = []
    pravilna = True
    while n > 0:
        vrstica = str(input()).split(" ")
        #Vhod razdeli pri presledkih ter jih da v tabelo
        tabela = []
        for a in vrstica:
            tabela.append(a)
            #Damo posamezen elt. v tabelo
        tab_tab.append(tabela[1:])
        #Damo v skupno tabelo vrstic za kasnejše preverjanje pravilnosti
        if tabela[0] in '#':
        #Če je prvi element '#'
            for a in range(1,len(tabela)):
                if a % 2 == 0:
                    print(int(tabela[a])*'.',end='')
                else:
                    print(int(tabela[a])*'#',end='')
                #Če je a liho bo prvi znak '#' čene pa '.', pomnoženo z ustreznim številom
        elif tabela[0] in '.':
        #Če je prvi element '#'
            for a in range(1,len(tabela)):
                if a % 2 == 0:
                    print(int(tabela[a])*'#',end='')
                else:
                    print(int(tabela[a])*'.',end='')
                #Če je a liho bo prvi znak '.' čene pa '#', pomnoženo z ustreznim številom
        if n == 1:
            pass
        else:
            print('',sep='\n')
        #Če je zadnja vrstica preskoči presledek (ga kasneje dodamo)    
        n -= 1
        
    for a in tab_tab:
        #Za vsako vrstico vhoda sešteje število znakov ter to shrani v tabelo
        sumacija = 0
        for b in a:
            sumacija += int(b)
        pravilnostna.append(sumacija)
        
    for a in range(1,len(pravilnostna)):
        #Gre skozi tabelo seštevkou znakov ter primerja sosednja dva.
        if pravilnostna[a-1] != pravilnostna[a]:
            #V primeru, da se katerakoli dva ne ujemata je vhod napačen
            pravilna = False
    
    if pravilna == True:
        #V primeru, da je pravilna dodamo presledek (katerega smo prej izpustili)
        sys.stdout.write('\n') 
    else:
        #Čene pa dodamo stavek, da je vhod napačen
        print('\n' + 'Error decoding image' )

        
        
    
    