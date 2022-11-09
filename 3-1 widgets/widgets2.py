import os
from tkinter import *   # importera alla metoder i Pythons inbyggda GUI-ramverk Tkinter
root = Tk()             # skapa ett rot-objekt
# här behandlas fönstret som ska visas
img = PhotoImage(file=os.getcwd()+'/bild.gif')
label = Label(image=img)
label.pack()
# visa fönstret och håll programmet vid liv tills man stänger fönstret
root.mainloop()
