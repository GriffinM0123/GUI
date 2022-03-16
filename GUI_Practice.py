import tkinter
import tkinter.messagebox


class Average:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry("600x300")

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        self.score1 = tkinter.Label(self.frame1, text="Enter the Score of Test 1: ")

        self.score_entry1 = tkinter.Entry(self.frame1, width=10)

        self.score2 = tkinter.Label(self.frame2, text="Enter the Score of Test 2: ")

        self.score_entry2 = tkinter.Entry(self.frame2, width=10)

        self.score3 = tkinter.Label(self.frame3, text="Enter the Score of Test 3: ")

        self.score_entry3 = tkinter.Entry(self.frame3, width=10)

        self.score1.pack(side="left")
        self.score_entry1.pack(side="right")
        self.score2.pack(side="left")
        self.score_entry2.pack(side="right")
        self.score3.pack(side="left")
        self.score_entry3.pack(side="right")

        self.descr_label = tkinter.Label(self.frame4, text="Average: ")

        self.avg_var = tkinter.StringVar()

        self.avg_label = tkinter.Label(self.frame4, textvariable=self.avg_var)

        self.descr_label.pack(side="left")
        self.avg_label.pack(side="right")

        self.frame1.pack(side="top")
        self.frame2.pack(side="top")
        self.frame3.pack(side="top")
        self.frame4.pack(side="top")

        self.calc_button = tkinter.Button(
            self.frame5, text="Average", command=self.convert
        )

        self.quit_button = tkinter.Button(
            self.frame5, text="Quit", command=self.main_window.destroy
        )

        self.calc_button.pack(side="left")
        self.quit_button.pack(side="right")

        self.frame5.pack()

        tkinter.mainloop()

    def convert(self):
        score_1 = float(self.score_entry1.get())
        score_2 = float(self.score_entry2.get())
        score_3 = float(self.score_entry3.get())

        avg = (score_1 + score_2 + score_3) / 3

        self.avg_var.set(round(avg, 2))


my_gui = Average()


print("moving on......")
