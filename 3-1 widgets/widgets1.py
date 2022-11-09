from tkinter import *
root = Tk()
var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )
var.set("Hej världen!\nHur är läget?")
label.pack()
root.mainloop()
