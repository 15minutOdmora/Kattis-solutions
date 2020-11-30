import bisect
# Branje in urejanje vh. podatkov
n, m = map(int, input().split())
stev = [int(i) for i in input().split()]
# Uredimo tabelo po velikosti
stev.sort()
sestevek = [0]
# Naredimo tabelo z seštevki višin dreves za kasnejšo uporabo
for i in stev:
    sestevek.append(sestevek[-1]+i)
# Določimo spodnjo(0) in zgornjo(max(stev)) mejo
min_, max_ = 0, stev[-1]

while min_ < max_ :
    sredina = (min_ + max_) / 2
    # Z bisekcijo najdemo index prvega elementa, ki je po vrednosti
    # večji od spremenljivke sredina
    neporezan = bisect.bisect_right(stev, sredina)
    # Izračunamo koliko metrov lesa smo odrezali
    zbrano = (sestevek[-1] - sestevek[neporezan]) - ((n - neporezan)* sredina)
    # Če se št. odrezanih metrov lesa ujema z želenim, prekinemo zanko
    if zbrano == m:
        break
    # Če smo porezali več, dvignemo spodnjo mejo
    elif zbrano > m:
        min_ = sredina
    # Če smo porezali premalo, spustimo zgornjo mejo
    elif zbrano < m:
        max_ = sredina

if max_ - min_ == 1:
    ans = min_
else:
    ans = (min_ + max_) / 2
    
# Izpišemo zaokroženo mejo   
print(int(ans))


