import tkinter
import tkinter.messagebox
from turtle import bgcolor
class Average:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("350x250")
        self.main_window.configure(bg="light blue")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)
        
        
        self.cust = tkinter.Label(self.frame1, text="Please enter your name for the order: ")

        self.name = tkinter.Entry(self.frame1, width=10)

        self.cust.pack(side="left")
        self.name.pack(side="right")
        
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.frame2, text="Pepperoni $1.00", variable=self.cb_var1
        )

        self.cb2 = tkinter.Checkbutton(
            self.frame3, text="Ham $2.00", variable=self.cb_var2
        )

        self.cb3 = tkinter.Checkbutton(
            self.frame4, text="Sausage $3.00", variable=self.cb_var3
        )

        self.radio_var = tkinter.IntVar()

        self.radio_var.set(5)

        self.rb1 = tkinter.Radiobutton(
            self.frame4, text="Thin Crust $5.00", variable=self.radio_var, value=5
        )

        self.rb2 = tkinter.Radiobutton(
            self.frame4, text="Thick Crust $7.00", variable=self.radio_var, value=7
        )



        self.cb1.pack(side = "top")
        self.cb3.pack(side = "top")
        self.cb2.pack(side = "top")
        self.rb1.pack(side = "top")
        self.rb2.pack(side = "top")
        self.cb1.configure(bg="light blue")
        self.cb2.configure(bg="light blue")
        self.cb3.configure(bg="light blue")
        self.rb1.configure(bg="light blue")
        self.rb2.configure(bg="light blue")
        self.cust.configure(bg="light blue")
        
        

        

        self.avg_var = tkinter.StringVar()

        self.avg_label = tkinter.Label(self.frame4, textvariable=self.avg_var)

        
        self.avg_label.pack(side="right")

        self.frame1.pack(side="top")
        self.frame2.pack(side="top")
        self.frame3.pack(side="top")
        self.frame4.pack(side="top")

        self.frame2.configure(bg="light blue")
        self.frame3.configure(bg="light blue")
        self.frame4.configure(bg="light blue")

        self.calc_button = tkinter.Button(
            self.frame5, text="Calculate", command=self.calculate
        )

        self.quit_button = tkinter.Button(
            self.frame5, text="Quit", command=self.main_window.destroy
        )

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.frame5.pack(side = "bottom")
        self.frame5.configure(bg="light blue")

        

        tkinter.mainloop()

    def calculate(self):
        customer = self.name.get()

        total = 0

        if self.cb_var1.get() == 1:
            total += 1
        if self.cb_var2.get() == 1:
            total += 2
        if self.cb_var3.get() == 1:
            total += 3
        if self.radio_var.get() == 5:
            total += 5
        if self.radio_var.get() == 7:
            total += 7
        
        totalcost = "${:,.2f}".format(total)

        tkinter.messagebox.showinfo(
            "Order Summary", str(customer) + " your total is " + str(totalcost)
        )

        





my_gui = Average()

