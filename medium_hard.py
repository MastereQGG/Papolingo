# Importy
from tkinter import *
from PIL import *
from PIL import ImageTk, Image
from random import *
import random as r


# Tablica z przedmiotami/osobami
tab1 = ["Apple","House","Mountain","Pencil","Window","Computer","Knife","Balloon","Scarecrow","Snake","Cardboard","Human","File","Poland","Cup","Tower","Bird","Plane","Chicken"]

# Liczniki
licznik_bledow = 0
licznik_punktow = 0

# Definicja dodania błędu
def dodajblad():
    global okno3
    def destroy():
        okno4.destroy()
        okno3.destroy()
        okno2.destroy()
    global licznik_bledow
    licznik_bledow += 1

    if licznik_bledow >= 4:
        okno4 = Tk()
        okno4.attributes("-fullscreen",True)
        txt = Label(okno4, text="Spróbuj ponownie...")
        b = Button(okno4, text="Try again", command=destroy).pack()
        okno4.mainloop()

def clear():
    widget_list = okno2.winfo_children()
    for item in widget_list:
        item.pack_forget()

# Definicja dodanie punktu
def dodajpunkt():
    global licznik_punktow
    licznik_punktow += 1

def start():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    
    okno2 = Tk()
    okno2.geometry("300x350")

    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz).pack()
    okno2.mainloop()

def odpowiedz():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start2()
    else:
        dodajblad()
        start2()

def start2():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz2).pack()

def odpowiedz2():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start3()
    else:
        dodajblad()
        start3()

def start3():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz3).pack()

def odpowiedz3():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start4()
    else:
        dodajblad()
        start4()

def start4():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz4).pack()

def odpowiedz4():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start5()
    else:
        dodajblad()
        start5()

def start5():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz5).pack()

def odpowiedz5():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start6()
    else:
        dodajblad()
        start6()

def start6():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz6).pack()

def odpowiedz6():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start7()
    else:
        dodajblad()
        start7()

def start7():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz7).pack()

def odpowiedz7():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start8()
    else:
        dodajblad()
        start8()

def start8():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz8).pack()

def odpowiedz8():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start9()
    else:
        dodajblad()
        start9()

def start9():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz9).pack()

def odpowiedz9():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start10()
    else:
        dodajblad()
        start10()

def start10():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz10).pack()

def odpowiedz10():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start11()
    else:
        dodajblad()
        start11()

def start11():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz11).pack()

def odpowiedz11():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start12()
    else:
        dodajblad()
        start12()

def start12():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz12).pack()

def odpowiedz12():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start13()
    else:
        dodajblad()
        start13()

def start13():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz13).pack()

def odpowiedz13():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start14()
    else:
        dodajblad()
        start14()

def start14():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz14).pack()

def odpowiedz14():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start15()
    else:
        dodajblad()
        start15()

def start15():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz15).pack()

def odpowiedz15():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start16()
    else:
        dodajblad()
        start16()

def start16():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz16).pack()

def odpowiedz16():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start17()
    else:
        dodajblad()
        start17()

def start17():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz17).pack()

def odpowiedz17():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start18()
    else:
        dodajblad()
        start18()

def start18():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz18).pack()

def odpowiedz18():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start19()
    else:
        dodajblad()
        start19()

def start19():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz19).pack()

def odpowiedz19():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        start20()
    else:
        dodajblad()
        start20()

def start20():
    global okno2, licznik_bledow, licznik_punktow, ent, los, odp
    clear()
    znak = "_"

    los = r.choice(tab1)
    tabpom = []
    tabpom = los.split()
    for x in range(3):
        i = 0
        odp = ""
        odp += tabpom[i]
        tabpom[i].replace([0],"_")
        i = i + 1

    zap = Label(okno2, text=tabpom)
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz20).pack()

def odpowiedz20():
    global ent, odp
    odp2 = ent.get()
    if odp2 == odp:
        dodajpunkt()
        k3()
    else:
        dodajblad()
        k3()

def k3():
    clear()
    txt = Label(okno2, text="Liczba twoich punktów: ")
    txt = Label(okno2, text=licznik_punktow)

