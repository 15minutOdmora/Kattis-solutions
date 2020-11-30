# Število testnih primerov
st_testov = int(input())

def vrni(n):
    '''Vrne rešitev formule'''
    return n * (n-1) // 2

# Zanka skozi vse primere
for i in range(st_testov):
    levo, desno = map(int,input().split())
    # Formulo sestavimo po formulah za aritmeticna zaporedja
    res = 1 + levo + 2 * desno + vrni(levo + desno)
    print(int(res))
   

    
    
