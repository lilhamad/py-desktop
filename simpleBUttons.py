from tkinter import *

window = Tk()
# TopFrame
topFrame = Frame(window)
topFrame.pack()
# Bottom Frame
bottomFrame = Frame(window)
bottomFrame.pack(side=BOTTOM)
# Button
GreenButton = Button(topFrame, text="Green One", fg="green")
BlueButton = Button(topFrame, text="Blue One", fg="blue")
YellowButton = Button(topFrame, text="Yellow One", fg="yellow", bg="red")
PurpleButton = Button(bottomFrame, text="Purple One", fg="purple")

# Pack them
GreenButton.pack(side=LEFT)
BlueButton.pack(side=LEFT)
YellowButton.pack(side=LEFT)
PurpleButton.pack(side=LEFT)

window.mainloop()