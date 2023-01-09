import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import webcam

root = tk.Tk() 

canvas = tk.Canvas(root, width=300, height=200)
canvas.grid(columnspan=3, rowspan=6)
# logo
logo = Image.open("logo.jpeg")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)


instructions = tk.Label(root, text="\nCapture button below\n", font="Raleway", fg='blue')
instructions.grid(columnspan=3, column=0, row=1)


browse_text = tk.StringVar()
click_button = Image.open("newbutton.png")
root.click_buttton = ImageTk.PhotoImage(click_button)

def on_enter(event):
    button.config(image=root.click_buttton)


button = tk.Button(root, image=root.click_buttton, bg='white', bd=0, command=lambda: webcam)

canvas.create_window(10, 6, window=button)
button.grid(column=1, row=2)
canvas = tk.Canvas(root, width=200, height=50)
canvas.grid(columnspan=3)

root.mainloop() 

