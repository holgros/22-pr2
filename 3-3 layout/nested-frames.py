from tkinter import *
root = Tk()
topframe = Frame(root)
leftframe = Frame(topframe)
button1 = Button(leftframe, text="Button 1")
button1.pack()
button2 = Button(leftframe, text="Button 2")
button2.pack()
button3 = Button(leftframe, text="Button 3")
button3.pack()
leftframe.pack(side=LEFT)
text = Text(topframe, width=50, height=5)
text.pack(side=LEFT)
topframe.pack()
label = Label(root, text="Layout med Tkinter!")
label.pack()
mainloop()