from tkinter import *

window = Tk()

menu = Menu(window)

window.config(menu=menu)

# function that does nothing
def comon():
    """
    nothing
    """
    print ("We are dumb and doa whole lot of nothing")

# file menu
fileMenu = Menu(menu)
fileMenu.add_command(label="New", command=comon)
fileMenu.add_command(label="New Folder", command=comon)
fileMenu.add_command(label="New Project", command=comon)
fileMenu.add_command(label="New python file", command=comon)
fileMenu.add_separator()

# edit menu
editMenu = Menu(menu)
editMenu.add_command(label="Undo", command=comon)
editMenu.add_command(label="Redo", command=comon)
editMenu.add_command(label="Comment", command=comon)

# add both edit menu  and file menu to main menu
menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Edit", menu=editMenu)


# toolbar frame
toolbar = Frame(window, bg="grey")
addButton = Button(toolbar, text="Add new", command=comon)
addButton.pack(side=LEFT, padx=2, pady=2)
stopButton = Button(toolbar, text="Stop this", command=comon)
stopButton.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)


# status bar
status = Label(window, text="Something is about to happen..", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

window.mainloop()