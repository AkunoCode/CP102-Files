from tkinter import *
from PIL import ImageTk, Image
import os

img_nav = 0
images_list = []
for filename in os.listdir("Analysis_Images"):
    images_list.append(f'Analysis_Images/{filename}')


def next_image():
    global img_nav
    if img_nav < len(images_list)-1:
        img_nav += 1
    elif img_nav == len(images_list)-1:
        img_nav = 0
    new_image = ImageTk.PhotoImage(Image.open(images_list[img_nav]))
    image_label.config(image=new_image)
    image_label.image = new_image


def prev_image():
    global img_nav
    if img_nav > 0:
        img_nav -= 1
    elif img_nav == 0:
        img_nav = len(images_list)-1
    new_image = ImageTk.PhotoImage(Image.open(images_list[img_nav]))
    image_label.config(image=new_image)
    image_label.image = new_image


root = Tk()
root.title("Analysis Image Viewer")

image = ImageTk.PhotoImage(Image.open(images_list[img_nav]))

# Create image label
image_label = Label(image=image)
prev_button = Button(root, text="< Previous", command=prev_image)
next_button = Button(root, text="Next >", command=next_image)
exit_button = Button(root, text="Exit", command=root.quit)

image_label.grid(row=0, column=0, columnspan=3)
prev_button.grid(row=1, column=0)
exit_button.grid(row=1, column=1)
next_button.grid(row=1, column=2)

root.mainloop()
