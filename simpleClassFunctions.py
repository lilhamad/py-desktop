from tkinter import *
window = Tk()
import tkinter.messagebox


class myClass:
    def __init__(self, baba):
        bigFrame = Frame(baba)
        bigFrame.pack()
        self.tex = "We are good bro!"

        self.myButton = Button(bigFrame, text="Print something", command=self.printMyText)
        self.myButton.pack()

        self.myQuitButton = Button(bigFrame, text="Quit now", command=bigFrame.quit)
        self.myQuitButton.pack(side=RIGHT)

    def printMyText(self):
        tkinter.messagebox.showinfo("dfdf", "dfdfdf")
        print(self.tex)


myclass = myClass(window)
window.mainloop()
