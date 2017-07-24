from tkinter import *

window = Tk()
bigFrame = Frame(window, bg="black")
bigFrame.pack()

# texts & fields
textOne = Label(bigFrame, text="Username")
textTwo = Label(bigFrame, text="Password")
fieldOne = Entry(bigFrame)
fieldTwo = Entry(bigFrame)
checkBox = Checkbutton(bigFrame, text="Keep me logged in")
loginButton = Button(bigFrame, text="Log in", bg="black", fg="green")

# arrange
textOne.grid(row=0, sticky=E)
textTwo.grid(row=1, sticky=E)
fieldOne.grid(row=0, column=1)
fieldTwo.grid(row=1, column=1)
checkBox.grid(row=2, column=1)
loginButton.grid(row=3, column=1, sticky=E)
window.mainloop()
