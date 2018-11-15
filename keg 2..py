p = int(3)
while n > 0:
    y = str(raw_input ('Masukkan password:  ')
            if y =='naura':
                print ('Anda berhasil login')
                break
            if p!=0:
                print ('Maaf anda salah memasuki password.')
                continue
            elif p==0:
                print ('Anda telah mencoba 3x, akses di tolak')
