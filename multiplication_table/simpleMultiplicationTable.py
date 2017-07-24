from tkinter import *

# from .generate import *
window = Tk()


class Application:
    def __init__(self, boss):
        self.num = 0
        self.b_g = '#000033'
        self.top_b_g = 'midnight blue'
        self.f_g = 'white'
        self.top_frame = Frame(boss, relief=SUNKEN, bg=self.top_b_g)
        self.top_frame.pack(side=TOP, fill=X)

        self.big_frame = Frame(boss, relief=SUNKEN, bg=self.b_g)
        self.big_frame.pack(side=TOP)
        self.create_starting_widget()

    def generate_def(self, x, y, z):
        lis = []
        if z == 0:
            self.table1.destroy()
            self.big_frame.destroy()
        if z == 1:
            self.label_x.destroy()
            self.label_y.destroy()
            self.label_by.destroy()
            self.generate_button.destroy()
            self.generate_new_button.grid(row=1, column=3)
            self.field_x.destroy()
            self.field_y.destroy()
        for ln in range(x):
            var = globals()['label_text%s' % ln] = StringVar()
            lis.append(var)

        for xn in range(1, x):
            text = ""
            text += "Multiplication table " + str(xn) + "\n"
            for yn in range(1, y):
                text += str(xn) + " x " + str(yn) + " = " + str(xn * yn) + "\n"
            lis[xn].set(text)

            self.table1 = Label(self.big_frame, font=('aerial', 10, 'bold'), bg=self.b_g, fg=self.f_g,
                                textvariable=lis[xn])

            if xn >= 16:
                xn -= 15
                yn = x * 3
            if xn >= 11:
                xn -= 10
                yn = x * 2
            if xn >= 6:
                xn -= 5
                yn = x
            self.table1.grid(row=yn, column=xn)

    def create_starting_widget(self):
        b_g = "midnight blue"
        self.space = Label(self.top_frame, bg=self.top_b_g)
        self.space.grid(row=0)
        self.generate_button = Button(self.top_frame, font=('aerial', 12, 'bold'), bg=self.b_g, fg=self.f_g,
                                      command=lambda x=10, y=13, z=1: self.generate_def(x, y, z), text="Generate")
        self.generate_new_button = Button(self.top_frame, font=('aerial', 12, 'bold'), bg=self.b_g, fg=self.f_g,
                                          command=lambda x=10, y=13, z=0: self.generate_def(x, y, z),
                                          text="Generate new")
        self.generate_button.grid(row=3, column=9)
        self.space.grid(row=2)

        # x
        self.label_x = Label(self.top_frame, font=('aerial', 10, 'bold'), bg=self.top_b_g, fg=self.f_g, text="X")
        self.label_x.grid(row=1, column=1)
        self.field_x = Entry(self.top_frame, font=(8), width=8, justify="center", bd=0)
        self.field_x.grid(row=1, column=2)

        # by
        self.label_by = Label(self.top_frame, font=('aerial', 10, 'bold'), bg=self.top_b_g, fg=self.f_g, text=" By ")
        self.label_by.grid(row=1, column=3)

        # y
        self.label_y = Label(self.top_frame, bg=self.top_b_g, font=('aerial', 10, 'bold'), fg=self.f_g, text="Y")
        self.label_y.grid(row=1, column=4)
        self.field_y = Entry(self.top_frame, width=8, justify="center", font=(10), bd=0)
        self.field_y.grid(row=1, column=5)


window.geometry("600x600")
window['bg'] = '#000033'
window.title("Dynamic Multiplication table")
app = Application(window)
window.mainloop()
