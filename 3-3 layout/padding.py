from tkinter import *
root = Tk()
w = Label(root, text="Red Sun", bg="red", fg="white")
# extern padding i y-led
w.pack(fill=X, pady=10)
w = Label(root, text="Green Grass", bg="green", fg="black")
# extern padding i x-led
w.pack(fill=X, padx=10)
w = Label(root, text="Blue Sky", bg="blue", fg="white")
# intern padding i y-led
w.pack(fill=X, ipady=10)
mainloop()
