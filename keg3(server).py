import socket
 def persegi(s=0):
    return s*s
s = oscket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 50020))
s.listen(5)
print "Server Penjawab Otomatis Sudah Siap"
data = ""
while data.lower() != "keluar":
    komm, addr = s.accept()
    while data.lower() != "keluar":
        data = komm.recv(1024)
        print "Pesan:", data
        if data.find("parameter") != -1:
            param, value = data.split("=")
            if param == "parameter sisi":
                s = float(value)
                b = value
                komm.send("parameter dicatat")
        elif data == "hitung":
            komm.send("Luas Persegi Dengan Sisi {} adalah {}".format(b,persegi(s)))
        else:
            komm.send("tidak ada")
