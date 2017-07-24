from tkinter import *

window = Tk()

menu = Menu(window)

window.config(menu=menu)


def comon():
    """
    nothing
    """
    print ("We are dumb and doa whole lot of nothing")

fileMenu = Menu(menu)
fileMenu.add_command(label="New", command=comon)
fileMenu.add_command(label="New Folder", command=comon)
fileMenu.add_command(label="New Project", command=comon)
fileMenu.add_command(label="New python file", command=comon)
fileMenu.add_separator()

editMenu = Menu(menu)
editMenu.add_command(label="Undo", command=comon)
editMenu.add_command(label="Redo", command=comon)
editMenu.add_command(label="Comment", command=comon)

menu.add_cascade(label="File", menu=fileMenu)
menu.add_cascade(label="Edit", menu=editMenu)

window.mainloop()