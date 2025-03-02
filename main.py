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

main = Tk()
main.title("Calculator")
operator = ""
input_value = StringVar()

display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertwidth=4,
                     bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

# Buttons
digits = [
    (7, 1, 0), (8, 1, 1), (9, 1, 2),
    (4, 2, 0), (5, 2, 1), (6, 2, 2),
    (1, 3, 0), (2, 3, 1), (3, 3, 2),
    (0, 4, 0)
]

for num, r, c in digits:
    Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text=str(num),
           command=lambda n=num: buttonClick(n)).grid(row=r, column=c)

# Operations
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="+", command=lambda: buttonClick("+")).grid(row=1, column=3)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="-", command=lambda: buttonClick("-")).grid(row=2, column=3)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="*", command=lambda: buttonClick("*")).grid(row=3, column=3)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="/", command=lambda: buttonClick("/")).grid(row=4, column=3)

# Special functions
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="C", command=buttonClear).grid(row=4, column=1)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="=", command=buttonEqual).grid(row=4, column=2)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="x²", command=buttonSquare).grid(row=5, column=0)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="√", command=buttonSqrt).grid(row=5, column=1)
Button(main, padx=16, bd=8, fg="black", font=("arial", 20, "bold"), text="log", command=buttonLog).grid(row=5, column=2)

main.mainloop()
