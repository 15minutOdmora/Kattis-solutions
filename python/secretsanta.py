import math
# Rezutat je enak Rez = 1 - (!n / n!)
# kjer je !n derangement
def derangement(n):
    ''' Vrne celo število katero je enako
        najbližjemu celemu številu rešitve enačbe !n = n! / e '''
    return round(math.factorial(n)/math.exp(1))

def rezultat(n):
    ''' Vrne zaokrožen rezultat 1 - (!n / n!) na 6 decimalk natančno'''
    return round(1 - (derangement(n)/math.factorial(n)), 8)

n = int(input())

if n < 11:
    print('%.8f' % rezultat(n))
# V primeru, da je n >= 11 bo rezultat pri 6 decimalnem zaokroževanju
# vedno enak 0.63212056
else:
    print('0.63212056')


