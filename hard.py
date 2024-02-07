# Importy
from tkinter import *
from PIL import *
from PIL import ImageTk, Image
from random import *
import random as r


# Tablica z przedmiotami/osobami
tab1 = ["Apple","House","Mountain","Pencil","Window","Computer","Knife","Balloon","Scarecrow","Snake","Cardboard","Human","File","Poland","Cup","Tower","Bird","Plane","Chicken"]
tab2 = ["Jabłko","Dom","Góra","Ołówek","Okno","Komputer","Nóż","Balon","Strach Na Wróble","Wąż","Karton","Człowiek","Plik","Polska","Kubek","Wieża","Ptak","Samolot","Kurczak"]

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
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn
    
    okno2 = Tk()
    okno2.geometry("300x350")

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz1).pack()

    okno2.mainloop()

def odpowiedz1():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start2()
    else:
        dodajblad()
        start2()

def start2():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz2).pack()

def odpowiedz2():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start3()
    else:
        dodajblad()
        start3()

def start3():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz3).pack()

def odpowiedz3():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start4()
    else:
        dodajblad()
        start4()

def start4():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz4).pack()

def odpowiedz4():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start5()
    else:
        dodajblad()
        start5()

def start5():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz5).pack()

def odpowiedz5():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start6()
    else:
        dodajblad()
        start6()

def start6():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz6).pack()

def odpowiedz6():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start7()
    else:
        dodajblad()
        start7()

def start7():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz7).pack()

def odpowiedz7():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start8()
    else:
        dodajblad()
        start8()

def start8():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz8).pack()

def odpowiedz8():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start9()
    else:
        dodajblad()
        start9()

def start9():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz9).pack()

def odpowiedz9():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start10()
    else:
        dodajblad()
        start10()

def start10():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz10).pack()

def odpowiedz10():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start11()
    else:
        dodajblad()
        start11()

def start11():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz11).pack()

def odpowiedz11():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start12()
    else:
        dodajblad()
        start12()

def start12():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz12).pack()

def odpowiedz12():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start13()
    else:
        dodajblad()
        start13()

def start13():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz13).pack()

def odpowiedz13():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start14()
    else:
        dodajblad()
        start14()

def start14():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz14).pack()

def odpowiedz14():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start15()
    else:
        dodajblad()
        start15()

def start15():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz15).pack()

def odpowiedz15():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start16()
    else:
        dodajblad()
        start16()

def start16():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz16).pack()

def odpowiedz16():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start17()
    else:
        dodajblad()
        start17()

def start17():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz17).pack()

def odpowiedz17():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start18()
    else:
        dodajblad()
        start18()

def start18():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz18).pack()

def odpowiedz18():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start19()
    else:
        dodajblad()
        start19()

def start19():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz19).pack()

def odpowiedz19():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        start20()
    else:
        dodajblad()
        start20()

def start20():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    rn = r.randrange(0,len(tab1))
    tekst1 = tab1[rn]
    tekst2 = tab2[rn]

    zap = Label(okno2, text=tekst2)
    zap.pack()
    ent = Entry(okno2)
    ent.pack()
    b = Button(okno2, text="Odpowiedz",command=odpowiedz20).pack()

def odpowiedz20():
    odp = ent.get()
    if odp == tekst1:
        dodajpunkt()
        k4()
    else:
        dodajblad()
        k4()

def k4():
    global okno2, licznik_bledow, licznik_punktow, ent, los, tekst1, tekst2, rn

    clear()

    txt = Label(okno2, text="Twoja Łączna Ilość Punktów:")
    txt = Label(okno2, text=licznik_punktow)