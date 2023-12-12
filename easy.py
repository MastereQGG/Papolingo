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
    def destroy():
        okno4.destroy()
    global licznik_bledow
    licznik_bledow += 1
    if licznik_bledow >= 4:
        okno4 = Tk()
        txt = Label(okno4, text="Spróbuj ponownie...")
        b = Button(okno4, text="Try again", command=destroy).pack()
        okno4.mainloop()

# Definicja dodanie punktu
def dodajpunkt():
    global licznik_punktow
    licznik_punktow += 1

# Definicja startu
def start():
    global okno2
    global okno3
    global licznik_bledow
    global licznik_punktow
    
    okno2 = Tk()
    okno2.geometry("300x350")

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start2).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    okno3 = Tk()
    tt = Label(okno3, text=textob).pack()
    okno3.mainloop()
    okno2.mainloop()

def clear():
    widget_list = okno2.winfo_children()
    for item in widget_list:
        item.pack_forget()

def clear2():
    widget_list = okno3.winfo_children()
    for item in widget_list:
        item.pack_forget()

def start2():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start3).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start3():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start4).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start4():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start5).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start5():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start6).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start6():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start7).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start7():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start8).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start8():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start9).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start9():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start10).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start10():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start11).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start11():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start12).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start12():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start13).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start13():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start14).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start14():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start15).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start15():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start16).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start16():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start17).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start17():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start18).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start18():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start19).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start19():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=start20).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def start20():
    clear()
    global licznik_bledow
    global licznik_punktow
    dodajpunkt()

    textp = r.choice(tab1)
    textob = textp
    textob += ".png"

    txt = Label(okno2, text = "Wybierz poprawny przycisk").pack()
    txt = Label(okno2, text = "Błędy: ").pack()
    txt = Label(okno2, text = licznik_bledow).pack()
    txt = Label(okno2, text = "Poprawne: ").pack()
    txt = Label(okno2, text = licznik_punktow).pack()

    b = Button(okno2, text=textp, command=k1).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()
    b = Button(okno2, text=r.choice(tab1), command=dodajblad).pack()

    clear2()
    tt = Label(okno3, text=textob).pack()

def k1():
    okno2.destroy()
    okno4 = Tk()
    okno4.mainloop()
    if licznik_punktow == 0:
        txt = Label(okno4, text="Spróbuj ponownie/Try again").pack()
    if licznik_punktow <= 5:
        txt = Label(okno4, text="Tekst1").pack()
    if licznik_punktow > 5 and licznik_punktow <= 10:
        txt = Label(okno4, text="Tekst2").pack()
    if licznik_punktow > 10 and licznik_punktow <= 15:
        txt = Label(okno4, text="Tekst3").pack()
    if licznik_punktow > 15 and licznik_punktow <= 20:
        txt = Label(okno4, text="Tekst4").pack()