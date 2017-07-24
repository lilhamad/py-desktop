from tkinter import *
import tkinter.messagebox
def showMessage():
    # tkinter.messagebox.showinfo("Nonesense", "We are dumb and doa whole lot of nothing")
    # tkinter.messagebox.showerror("Nonesense", "We are dumb and doa whole lot of nothing")
    # tkinter.messagebox.showwarning("Nonesense", "We are dumb and doa whole lot of nothing")
    answer = tkinter.messagebox.askquestion("Nonesense", "Do We do a whole lot of nothing?")
    if answer =='yes':
        tkinter.messagebox.showinfo("Good", "We are good and doa whole lot of nothing")
    else:
        tkinter.messagebox.showerror("Nonesense", "We are dumb and doa whole lot of nothing")


window = Tk()
button=Button(window, text="Click me", command=showMessage)
button.pack()

window.mainloop()