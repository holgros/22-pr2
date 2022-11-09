from tkinter import *
root = Tk()
e = Entry(root)
e.pack()
b = Button(root, text ="Tryck mig!")
def click_handler(self):
    print("Du skrev:", e.get())
b.bind("<Button-1>", click_handler)
b.pack()
root.mainloop()
