from tkinter import *
window = Tk()

class Application:

    def __init__(self, boss):
        self.big_frame = Frame(boss, relief=SUNKEN, width=200, height=100)
        self.big_frame.pack(side=TOP)
        self.create_starting_widget()


    def create_starting_widget(self):
        b_g = 'midnight blue'
        f_g = 'white'

        self.space = Label(self.big_frame)
        self.space.grid
        self.generate_button = Button(self.big_frame, font=('aerial', 10, 'bold'), bg=b_g, fg=f_g, border=0, text="Generate")
        self.generate_button.grid(row=2, column=2, columnspan=2)

        # x
        self.label_x = Label(self.big_frame, font=('aerial', 10, 'bold'), bg=b_g, fg=f_g, text="X")
        self.label_x.grid(row=1, column=1)

        self.field_x = Entry(self.big_frame, font=(10), bd=0)
        self.field_x.grid(row=1, column=2)


        # by
        self.label_y = Label(self.big_frame, font=('aerial', 10, 'bold'), bg=b_g, fg=f_g, text="By ")
        self.label_y.grid(row=1, column=3)


        # y
        self.label_y = Label(self.big_frame, font=('aerial', 10, 'bold'), bg=b_g, fg=f_g, text="Y")
        self.label_y.grid(row=1, column=4)

        self.field_y = Entry(self.big_frame, font=(10), bd=0)
        self.field_y.grid(row=1, column=5)

window.geometry("600x600")
window.configure(background='midnight blue')
window['bg']='midnight blue'
app = Application(window)
window.mainloop()

