import tkinter as tk


class Calculator:
    def __init__(self) -> None:
        self.root = tk.Tk()

        self.root.geometry("500x600")
        self.root.title("Calculator")

        self.textline = tk.Entry(self.root, font=("Helvetica", "50"))
        self.textline.pack(fill='x')

        self.buttonframe = tk.Frame(self.root)

        self.buttonframe.columnconfigure(0, weight=1)
        self.buttonframe.columnconfigure(1, weight=1)
        self.buttonframe.columnconfigure(2, weight=1)
        self.buttonframe.columnconfigure(3, weight=1)

        self.button1 = tk.Button(
            self.buttonframe, text="1", height=4, font=("Helvetica", "10"))
        self.button2 = tk.Button(
            self.buttonframe, text="2", height=4, font=("Helvetica", "10"))
        self.button3 = tk.Button(
            self.buttonframe, text="3", height=4, font=("Helvetica", "10"))
        self.button4 = tk.Button(
            self.buttonframe, text="4", height=4, font=("Helvetica", "10"))
        self.button5 = tk.Button(
            self.buttonframe, text="5", height=4, font=("Helvetica", "10"))
        self.button6 = tk.Button(
            self.buttonframe, text="6", height=4, font=("Helvetica", "10"))
        self.button7 = tk.Button(
            self.buttonframe, text="7", height=4, font=("Helvetica", "10"))
        self.button8 = tk.Button(
            self.buttonframe, text="8", height=4, font=("Helvetica", "10"))
        self.button9 = tk.Button(
            self.buttonframe, text="9", height=4, font=("Helvetica", "10"))
        self.button0 = tk.Button(
            self.buttonframe, text="0", height=4, font=("Helvetica", "10"))
        self.button_plus = tk.Button(
            self.buttonframe, text="+", height=4, font=("Helvetica", "10"))
        self.button_minus = tk.Button(
            self.buttonframe, text="-", height=4, font=("Helvetica", "10"))
        self.button_mult = tk.Button(
            self.buttonframe, text="x", height=4, font=("Helvetica", "10"))
        self.button_div = tk.Button(
            self.buttonframe, text="/", height=4, font=("Helvetica", "10"))
        self.button_eq = tk.Button(
            self.buttonframe, text="=", height=4, font=("Helvetica", "10"))

        self.button1.grid(row=1, column=0, sticky=tk.W+tk.E)
        self.button2.grid(row=1, column=1, sticky=tk.W+tk.E)
        self.button3.grid(row=1, column=2, sticky=tk.W+tk.E)
        self.button4.grid(row=2, column=0, sticky=tk.W+tk.E)
        self.button5.grid(row=2, column=1, sticky=tk.W+tk.E)
        self.button6.grid(row=2, column=2, sticky=tk.W+tk.E)
        self.button7.grid(row=3, column=0, sticky=tk.W+tk.E)
        self.button8.grid(row=3, column=1, sticky=tk.W+tk.E)
        self.button9.grid(row=3, column=2, sticky=tk.W+tk.E)
        self.button0.grid(row=3, column=1, sticky=tk.W+tk.E)
        self.button_plus.grid(row=0, column=0, sticky=tk.W+tk.E)
        self.button_minus.grid(row=0, column=1, sticky=tk.W+tk.E)
        self.button_mult.grid(row=0, column=2, sticky=tk.W+tk.E)
        self.button_div.grid(row=0, column=3, sticky=tk.W+tk.E)
        self.button_eq.grid(row=3, column=3, sticky=tk.W+tk.E)

        self.buttonframe.pack(fill="x")

        self.root.mainloop()


Calculator()
