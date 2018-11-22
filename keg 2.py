#KEG 2
def KonversiSuhu(C = 0, F = 0):
    if C !=0:
        F = int(9 / 5 * C + 32)
        print('suhu', C, 'celcius setara dengan', F, 'farenheit')
    elif F !=0:
        C = int(5/9* (F-32))
        print ('suhu', F, 'farenheit setara dengan', C, 'celcius')
    elif F !=0 and C !=0:
        F = (9/5*C+32)
        print ('suhu', C,'celcius setara dengan', F, 'farenheit')
    else:
        F = int('9/5*C+32')
        print ('suhu', C, 'celvius setara dengan' , F, 'farenheit')
        
