from tkinter import *
import urllib.request

def fetch_def():

    response = urllib.request.urlopen('http://python.org/')
    html = response.read()

    fetchedText.set(html)

window = Tk()
fetchedText = StringVar()


fetchField = Label(window, textvariable=fetchedText).pack()
fetchButton = Button(window, text="fetch", command=fetch_def).pack()
window.mainloop()