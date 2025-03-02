from tkinter import *
import math

def buttonClick(number):
    global operator
    operator = operator + str(number)
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
        result = str(eval(operator + "**2"))
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

def buttonSqrt():
    global operator
    try:
        result = str(math.sqrt(eval(operator)))
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

def buttonLog():
    global operator
    try:
        result = str(math.log10(eval(operator)))
        input_value.set(result)
        operator = ""
    except:
        input_value.set("Error")
        operator = ""

def toggle_high_contrast():
    global high_contrast
    if high_contrast:
        main.configure(bg="blue")
        button_bg = "light blue"
    else:
        main.configure(bg="black")
        button_bg = "yellow"
    high_contrast = not high_contrast
    for btn in buttons:
        btn.configure(bg=button_bg)

main = Tk()
main.title("Calculator")
main.configure(bg="blue")
operator = ""
input_value = StringVar()
high_contrast = False

display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertwidth=4,
                     bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

# Buttons
buttons = []
digits = [
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (0, 4, 0)
]

for num, r, c in digits:
    btn = Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text=str(num),
                 command=lambda n=num: buttonClick(n), bg="light blue")
    btn.grid(row=r, column=c)
    buttons.append(btn)

# Operations
operations = [("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3)]
for op, r, c in operations:
    btn = Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text=op,
                 command=lambda o=op: buttonClick(o), bg="light blue")
    btn.grid(row=r, column=c)
    buttons.append(btn)

# Special functions
special_buttons = [
    ("C", buttonClear, 4, 1),
    ("=", buttonEqual, 4, 2),
    ("x²", buttonSquare, 5, 0),
    ("√", buttonSqrt, 5, 1),
    ("log", buttonLog, 5, 2)
]

for text, cmd, r, c in special_buttons:
    btn = Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text=text,
                 command=cmd, bg="light blue")
    btn.grid(row=r, column=c)
    buttons.append(btn)

# High contrast toggle button
btn_toggle = Button(main, padx=16, bd=10, fg="black", font=("arial", 12, "italic"), text="High Contrast",
                    command=toggle_high_contrast, bg="light blue")
btn_toggle.grid(row=0, column=1)
buttons.append(btn_toggle)

main.mainloop()
