import math
def razdalja(a,b):
    '''Vrne razdaljo med dvema točkama'''
    rzd = math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)
    return rzd
def razdaljazkrogom(a,b):
    '''Vrne najblizjo razdaljo med točko a in krožnico točke b'''
    rzdk = razdalja(a,b) - b[2]
    return rzdk
# Branje vhodnih podatkov
x = [int(a) for a in input().split(' ')]
moj_polozaj,st_senzorjev = x[:2],x[2]
# Branje podatkov ostalih senzorjev
tabela_sen = []
for i in range(st_senzorjev):
    senzor = [int(a) for a in input().split(' ')]
    # V tab_sen shranimo razdaljo med najbližjo točko krožnice senzorja
    # in našim položajem 
    tabela_sen.append(round(razdaljazkrogom(moj_polozaj,senzor),2))
# Tabelo uredimo po velikosti
tabela_sen.sort()
# Kot rezultat izberemo tretjo največjo razdaljo 
radij = int(tabela_sen[2])
# Če je razdalja manjša od 0 izpišemo '0' namesto negativno število
if radij <= 0:
    print(0)
else:
    print(radij)