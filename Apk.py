# Importy
from tkinter import *
from PIL import *
from PIL import ImageTk, Image
import easy
import medium
import medium_hard
import hard

okno = Tk()
okno.resizable(False, False)
okno.geometry("400x400")
okno.title("APK")

txt = Label(okno, text="Nauka języka Angielskiego", width=200).pack(side="top")
button1 = Button(okno, text = "Łatwy",bg = "green", command=easy.start).pack()
button2 = Button(okno, text = "Średni",bg = "blue", command=medium.start).pack()
button3 = Button(okno, text = "Średnio-Trudny",bg = "purple", command=medium_hard.start).pack()
button4 = Button(okno, text = "Trudny",bg = "red", command=hard.start).pack()

okno.mainloop()