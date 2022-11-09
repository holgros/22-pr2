from tkinter import *
root = Tk()
b = Button(root, text ="Tryck mig!")
def click_handler(self):
    print("Någon klickade på knappen!")
b.bind("<Button-1>", click_handler)
b.pack()
root.mainloop()
