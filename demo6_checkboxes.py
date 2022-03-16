import tkinter
import tkinter.messagebox


class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("500x200")

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()

        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)

        self.cb1 = tkinter.Checkbutton(
            self.top_frame, text="Option1", variable=self.cb_var1
        )

        self.cb2 = tkinter.Checkbutton(
            self.top_frame, text="Option2", variable=self.cb_var2
        )

        self.cb3 = tkinter.Checkbutton(
            self.top_frame, text="Option3", variable=self.cb_var3
        )

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        # set the intvar object to 1

        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.okbutton = tkinter.Button(
            self.bottom_frame, text="OK", command=self.do_something
        )

        self.quit_button = tkinter.Button(
            self.bottom_frame, text="Quit", command=self.main_window.destroy
        )

        self.okbutton.pack(side="left")
        self.quit_button.pack(side="left")

        tkinter.mainloop()

    def do_something(self):
        self.message = "you have selected:\n"

        if self.cb_var1.get() == 1:
            self.message += "1\n"
        if self.cb_var2.get() == 1:
            self.message += "2\n"
        if self.cb_var3.get() == 1:
            self.message += "3\n"

        tkinter.messagebox.showinfo("Response", self.message)


my_gui = KiloConverterGUI()


print("moving on......")
