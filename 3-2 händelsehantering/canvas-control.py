from tkinter import *
root = Tk()
canv = Canvas(root, height=250, width=300, bg="blue")
canv.pack()
id = canv.create_oval(0, 100, 50, 150, fill="red")
def move_left(e):
    if canv.coords(id)[0] >= 50:
        canv.move(id, -50, 0)
def move_right(e):
    if canv.coords(id)[0] < 250:
        canv.move(id, 50, 0)
def move_up(e):
    if canv.coords(id)[3] > 50:
        canv.move(id, 0, -50)
def move_down(e):
    if canv.coords(id)[3] < 250:
        canv.move(id, 0, 50)
canv.bind_all("<Left>", move_left)
canv.bind_all("<Right>", move_right)
canv.bind_all("<Up>", move_up)
canv.bind_all("<Down>", move_down)
root.mainloop()
