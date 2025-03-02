from tkinter import *
from PIL import Image, ImageTk
import math

def buttonClick(number):
    global operator
    operator += str(number)
    input_value.set(operator)

def buttonClear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual():
    global operator
    try:
        result = str(eval(operator))
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

def buttonSquare():
    global operator
    try:
        result = str(eval(operator) ** 2)
        input_value.set(result)
        operator = result
    except:
        input_value.set("Error")
        operator = ""

def buttonRoot():
    global operator
    try:
        result = str(math.sqrt(eval(operator)))
        input_value.set(result)
        operator = result
    except:
        input_value.set("Error")
        operator = ""

def buttonLog():
    global operator
    try:
        result = str(math.log10(eval(operator)))
        input_value.set(result)
        operator = result
    except:
        input_value.set("Error")
        operator = ""

def toggleHighContrast():
    if main.cget("bg") == "dark orange":
        main.config(bg="black")
        for button in buttons:
            button.config(bg="yellow", fg="black")
        display_text.config(bg="white", fg="black")
    else:
        main.config(bg="dark orange")
        for button in buttons:
            button.config(bg="orange", fg="black")
        display_text.config(bg="moccasin", fg="black")

main = Tk()
main.title("Calculator")
main.config(bg="dark orange")

operator = ""
input_value = StringVar()

title_frame = Frame(main, bg="dark orange")
title_frame.grid(row=0, column=0, columnspan=4, sticky="w")

contrast_btn = Button(title_frame, text="High Contrast", font=("arial", 12, "bold"), command=toggleHighContrast, bg="orange", fg="black")
contrast_btn.pack(side=LEFT)

# Load and display image with text
image = Image.open("photo/beluga_cat.png")
image = image.resize((50, 50), Image.LANCZOS)
img = ImageTk.PhotoImage(image)
image_label = Label(title_frame, image=img, bg="dark orange")
image_label.pack(side=RIGHT)
text_label = Label(title_frame, text="Simple Calculator", font=("arial", 12, "bold"), bg="dark orange", fg="black")
text_label.pack(side=RIGHT)

display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertwidth=4, bg="moccasin", justify=LEFT)
display_text.grid(row=1, column=0, columnspan=4)

buttons = []

button_layout =[
[("C", 2, 0, buttonClear),("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("+", 3, 3)],
[("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3)],
[("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("*", 5, 3)],
[("0", 6, 0), ("√", 6, 1, buttonRoot), ("/", 6, 2)],
[("x²", 7, 0, buttonSquare), ("log", 7, 1, buttonLog), ("=", 7, 3, buttonEqual)]]

for row in button_layout:
    for btn in row:
        text, r, c = btn[:3]
        cmd = btn[3] if len(btn) > 3 else lambda t=text: buttonClick(t)
        button = Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text=text, command=cmd, bg="orange")
        button.grid(row=r, column=c)
        buttons.append(button)

main.mainloop()