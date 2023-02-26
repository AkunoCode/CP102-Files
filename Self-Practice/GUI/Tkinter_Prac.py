import tkinter as tk
from tkinter import messagebox

class MyGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.menubar = tk.Menu(self.root)

        self.filemenu = tk.Menu(self.menubar, tearoff=0) # Needs to be in menubar
        self.filemenu.add_command(label="Close", command=exit)

        self.menubar.add_cascade(menu=self.filemenu,label="File") # Adds the file menu to menubar

        self.root.config(menu=self.menubar)

        self.label = tk.Label(self.root, text="Your Message")
        self.label.pack(padx=10, pady=10)

        self.textbox = tk.Text(self.root, height=5)
        self.textbox.bind("<KeyPress>", self.shortcut) # To see what is pressed inside the textbox
        self.textbox.pack(padx=10,pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", variable=self.check_state)
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root, text="Show Message", command=self.show_message)
        self.button.pack(padx=10,pady=10)

        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            # If not checked then itll print
            print(self.textbox.get('1.0',tk.END)) # '1.0 means at the start of the string in textbox
        else:
            # Else a popup will be created
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0',tk.END))
    
    def shortcut(self, event):
        # print(event.state) to get the number
        # print(event.keysym) to get the key symbol/name
        if event.state == 12 and event.keysym == "Return":
            self.show_message()

    def on_closing(self):
        print("Hello World")
        if messagebox.askyesno(title="Quit?", message="Do you reallw want to quit?"): #Yes/No prompt
            self.root.destroy() # Closes/Destroys the window



MyGUI()