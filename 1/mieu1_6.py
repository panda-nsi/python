from tkinter import *

window = Tk()
window.title("Connexion")
window.config(bg = "#1e293b")
window.geometry("640x480")

window.maxsize(640,480)
window.minsize(640,480)

canvas1 = Canvas(window, width=400, height=300, bg = "#1e293b")
canvas1.pack()

identifiantLabel = Label(window, text = "Identifiant", bg = "#1e293b", fg = "#FF5733")
canvas1.pack()

identifiantEntry = Entry(window)
canvas1.create_window(200, 140, window=identifiantEntry)

def login():
    identifiant = identifiantEntry.get()

loginButton = Button(text= "Connexion")

window.mainloop()