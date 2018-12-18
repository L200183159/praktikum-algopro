document = open("L200183159", "w")
document.write("L200183159 \n")
document.write("03/08/2000 \n")
document.write("Naura Salsabila \n")
document.write("Bengkulu")
document.close()

import shelve
data = open("L200183159", "r")
NIM = data.readline()
TL = data.readline()
Nama = data.readline()
Kota = data.readline()
data.close

data = shelve.open("Naura")
data["newdata"] = [Nama, Kota, TL, NIM]
data.close()

data = shelve.open("Naura")
print(data["newdata"][0])
print(data["newdata"][1])
print(data["newdata"][2])
print(data["newdata"][3])
from tkinter import Tk, Label, Entry, Button, StringVar

my_app = Tk(className= "Kalkulator Sederhana")

L1 = Label(my_app, text= "Angka 1")
L1.grid(row=0, column=0)
str1 = StringVar()
E1 = Entry(my_app, textvariable= str1)
E1.grid(row=0, column=1, columnspan=3)
L2 = Label(my_app, text= "Angka 2")
str2 = StringVar()
L2.grid(row=1, column=0)
E2 = Entry(my_app, textvariable= str2)
E2.grid(row=1, column=1, columnspan=3)

def tambah():
    p = float(str1.get())
    q = float(str2.get())
    r = p+q
    L.config(text=r)

def kurang():
    p = float(str1.get())
    q = float(str2.get())
    r = p-q
    L.config(text=r)

def kali():
    p = float(str1.get())
    q = float(str2.get())
    r = p*q
    L.config(text=r)

def bagi():
    p = float(str1.get())
    q = float(str2.get())
    r = p/q
    L.config(text=r)

B1 = Button (my_app, text= "+", command = tambah)
B1.grid(row=2, column=0)
B2 = Button (my_app, text= "-", command = kurang)
B2.grid(row=2, column=1)
B3 = Button (my_app, text= "x", command = kali)
B3.grid(row=2, column=2)
B4 = Button (my_app, text= ":", command = bagi)
B4.grid(row=2, column=3)

L3 = Label (my_app, text= "Hasil")
L3.grid (row=3, column=1)
L = Label(my_app, text= "0")
L.grid(row=3, column=2)

my_app.mainloop()
