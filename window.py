from tkinter import *
import os

def btn_clicked():
    print("Button Clicked")
    os.system('python webcam.py')
    
window = Tk()
window.geometry("900x550")
window.configure(bg = "#ffffff")
window.title('Gesture Detection System')
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 599, y = 351,
    width = 120,
    height = 121)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    368.0, 228.5,
    image=background_img)

window.resizable(False, False)
window.mainloop()
