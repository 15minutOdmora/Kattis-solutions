import fileinput
def pretvori_v_sec(cas_str):
    '''pretvori cas v sekunde'''
    h, m, s = cas_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def pretvori_v_hhmmss(sekunde):
    '''pretvori nazaj v format hh:mm:ss v obliki niza'''
    ure = sekunde // (60*60)
    sekunde %= (60*60)
    minute = sekunde // 60
    sekunde %= 60
    return "%02i:%02i:%02i" % (ure, minute, sekunde)

def kmh_v_ms(v):
    return round(v/3.6,5)

def ms_v_kmh(v):
    return round(v*3.6,5)

def m_v_km(metri):
    return round(metri/1000,2)

cas, hitrost, zeprevozeno = 0, 0, 0
liam = True
prejcas = 0
for vrstica in fileinput.input():
    x = vrstica.split(' ')
    if liam:
        if len(x) > 1:
            prejcas, prejhitrost = pretvori_v_sec(x[0]), kmh_v_ms(int(x[1]))
            liam = False 
    else:
        prejcas, prejhitrost = cas, hitrost
        
    if len(x) == 1:
        cas1 = pretvori_v_sec(x[0])
        prevozeno = (cas1 - prejcas) * hitrost
        skupaj = m_v_km(prevozeno + zeprevozeno)
        print(str(x[0]), '{0:.2f}'.format(skupaj), 'km', sep = ' ')
    else:
        cas, hitrost = pretvori_v_sec(x[0]), kmh_v_ms(int(x[1]))
        zeprevozeno += (cas - prejcas) * (prejhitrost)
        
    