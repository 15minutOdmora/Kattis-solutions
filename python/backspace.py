vhod = input()[::-1] # Niz obrnemo
izhod = ''
izbrisati = 0
for a in range(len(vhod)):
    znak = vhod[a] # Se sprehajamo po znakih niza od odzadaj
    if izbrisati == 0: izbrisati += 1 # Prištejemo 1, zbrišemo kasneje če ni znak enak <
    if znak == '<': izbrisati += 1 # Prištejemo spremenljivki 1 če je znak <
    else: izbrisati -= 1 # Odštejemo če ni, tako se odšteje prej dodana 1
    if izbrisati < 0: izbrisati = 0 # če je negativno nastavimo nazaj na 0
    if izbrisati == 0: izhod += znak # Izhodu dodamo znak, katerega nismo izbrisali        
print(izhod[::-1]) # Izhod obrnemo nazaj na pravilni vrstni red

