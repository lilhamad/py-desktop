from tkinter import *

window = Tk()


def printMyText():
    print("We are good")

myButton = Button(window, text="Click me", command=printMyText)
myButton.pack()

window.mainloop()

