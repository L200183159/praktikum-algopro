document = open("L200183159", "w")
document.write("L200183159" + "\n")
document.write("03-08-2000" + "\n")
document.write("Naura Salsabila")
document.close()
from tkinter import*

my_app = Tk(className="Data diri")

L1 = Label(my_app, text="Data diri", font=("Arial", 24))
L1.grid(row=0, column=0, sticky=W)
L2 = Label(my_app, text="Nama")
L2.grid(row=1, column=0, sticky=W)
L3 = Label(my_app, text="Naura Salsabila")
L3.grid(row=1, column=1, sticky=W)
L4 = Label(my_app, text="NIM")
L4.grid(row=2, column=0, sticky=W)
L5 = Label(my_app, text="L200183159")
L5.grid(row=2, column=1, sticky=W)
L6 = Label(my_app, text="Buku favorit")
L6.grid(row=3, column=0, sticky=W)
L7 = Label(my_app, text="Komik")
L7.grid(row=3, column=1, sticky=W)
L8 = Label(my_app, text="Idola di kalangan sahabat")
L8.grid(row=4, column=0, sticky=W)
L9 = Label(my_app, text="Umar Bin Khattab")
L9.grid(row=4, column=1, sticky=W)
L10 = Label(my_app, text="Motto")
L10.grid(row=5, column=0, sticky=W)
L11 = Label(my_app, text="Kerja keras,kerja ikhlas,kerja cerdas")
L11.grid(row=5, column=1, sticky=W)

def tutup():
    my_app.destroy()

B1 = Button(my_app, text="Tutup", command=tutup)
B1.grid(row=6, column=1)

my_app.mainloop()    
