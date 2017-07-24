from  tkinter import *
import tkinter.messagebox
window = Tk()

# canvas
canvas = Canvas(window, width=400, height=400)
canvas.pack()

def deleter():
    canvas.delete(ALL)


# line
blackLine = canvas.create_line(0, 0, 400, 400)
redLine = canvas.create_line(0, 400, 300, 300)
box = canvas.create_rectangle(25, 25, 200, 200, fill="black")

button = Button(window, text="Clear screen", command=deleter)
button.pack()
window.mainloop()

