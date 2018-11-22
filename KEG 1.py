#kegiatan 1
a = {'nama':'naura',
     'nim':'L200183159',
     'alamat':'pesma kh masmansyur',
     'prodi':'informatika',
     'kota':'surakarta',
     'provinsi':'jawa tengah',
     'warganegara':'wni'}
def pilihan():
    print ('''pilihan yang tersedia:
p menampilkan nama
u menampilkan nim
h menampilkan alamat
g menampilkan prodi
f menampilkan kota
d menampilkan provinsi
w menampilkan warganegara
k kembali
q menampilkan pilihan ''')
pilihan()

def nama():
    print ('nama:', a['nama'])
def nim():
    print ('nim:', a['nim'])
def alamat():
    print ('alamat:', a['alamat'])
def prodi():
    print ('prodi:', a['prodi'])
def kota():
    print ('kota:', a['kota'])
def provinsi():
    print ('provinsi:', a['provinsi'])
def warga():
    print ('warganegara:' ,a['warganegara'])
def kembali():
    print ('pilihan()')
while True:
    c = input ('pilihan saudara:')
    if c == '1':
        nama()
    elif c == '2':
        nim()
    elif c == '3':
        alamat()
    elif c == '4':
        prodi()
    elif c == '5':
        kota()
    elif c == '6':
        provinsi()
    elif c == '7':
        warganegara()
    elif c == '...':
        nama()
        nim()
        alamat()
        prodi()
        kota()
        provinsi()
        warganegara()
    elif c == 'k':
        print ('terima kasih')
        break
    else:
        print ('perintah tidak di kenal')
        
