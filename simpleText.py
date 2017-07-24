from tkinter import *

window = Tk()

# labels
textGreen = Label(text="Text Green", bg="black", fg="green")
textRed = Label(text="Text Red", bg="black", fg="red")

# pack
textGreen.pack(side=LEFT, fill=Y)
textRed.pack(fill=X)

window.mainloop()