import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("EventGenie")

# The button frame is in grid layout but the overall is in pack layout
buttonframe = tk.Frame(root)

buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

button1 = tk.Button(buttonframe, text="Read")
button2 = tk.Button(buttonframe, text="Write")
button3 = tk.Button(buttonframe, text="Delete")

button1.grid(row=0, column=0, sticky=tk.W+tk.E)
button2.grid(row=0, column=1, sticky=tk.W+tk.E)
button3.grid(row=0, column=2, sticky=tk.W+tk.E)

# can also use button.place(x,y,h,w) for exact coordinates of widget

buttonframe.pack(fill='x')  # fill x means its gonna stretch to the sides
root.mainloop()
