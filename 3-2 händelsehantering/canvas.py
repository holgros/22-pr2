from tkinter import *
from time import *
root = Tk()
canv = Canvas(root, height=250, width=300, bg="blue")
canv.pack()
def update_circle():
    x0 = 0
    rightwards = True
    for i in range(1000):
        if x0 > 250 or x0 < 0:
            rightwards = not rightwards
        if rightwards:
            x0 = x0 + 10
        else:
            x0 = x0 - 10
        canv.delete("all")
        canv.create_oval(x0, 100, x0+50, 150, fill="red")
        canv.update()
        root.after(100)
    root.destroy()
update_circle()
root.mainloop()
