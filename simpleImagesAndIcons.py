from tkinter import *
from tkinter import messagebox

window = Tk()

photo = PhotoImage(file="ad.png", width=1000, height=500)
image = Label(window, image=photo)
image.pack()

def pressOne():
    messagebox.showinfo("", "list.count(x) Return the number of times x appears in the list.list.sort(cmp=None, key=None, reverse=False)Sort the items of he list in place (the arguments can be used for sort customization, see sorted() for their explanation).list.reverse() Reverse the elements of the list, in place.    An example that uses most of the list methods:[66.25, -1, 333, 1, 1234.5, 333]>>> a.reverse()>>> a[333, 1234.5, 1, 333, -1, 66.25]>>> a.sort()>>> a[-1, 1, 66.25, 333, 333, 1234.5]>>> a.pop()1234.5>>> a[-1, 1, 66.25, 333, 333]You might have noticed that methods like insert, remove or sort that only modify the list have no return value printed – they return the default None. [1] This is a design principle for all mutable data structures in Python.")

press = Button(window, text="Click me", command=pressOne)
press.pack()
window.mainloop()
