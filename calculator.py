from tkinter import *

root = Tk()
root.title("Calculator")

# Entry for number to the calculator
e = Entry(root, width=40, borderwidth=1)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Function for our buttons
def buttonClick(number):
    current = e.get()       # Getting the current number on the entry
    e.delete(0, END)        # Clear the entry
    e.insert(0, str(current) + str(number))

# Function to clear our entry
def clear():
    e.delete(0, END)

# Function to add a number
def add():
    firstNumber = e.get()
    global fnum
    global math 
    math = "add"
    fnum = float(firstNumber)
    e.delete(0, END)

# Function to subtract a number
def subtract():
    firstNumber = e.get()
    global fnum
    global math 
    math = "subtract"
    fnum = float(firstNumber)
    e.delete(0, END)

# Function to multiply a number
def multiply():
    firstNumber = e.get()
    global fnum
    global math 
    math = "multiply"
    fnum = float(firstNumber)
    e.delete(0, END)

# Function to divide a number
def divide():
    firstNumber = e.get()
    global fnum
    global math 
    math = "divide"
    fnum = float(firstNumber)
    e.delete(0, END)

# Function to mod a number
def mod():
    firstNumber = e.get()
    global fnum
    global math 
    math = "mod"
    fnum = float(firstNumber)
    e.delete(0, END)

# Function to make number a negative
def negative():
    current = str(e.get())
    e.delete(0, END)
    newCur = '-' + current
    e.insert(0, newCur)

# Function for backspace
def backspace():
    current = str(e.get())
    e.delete(0, END)
    e.insert(0, current[:-1])



# Function for eqaul sign
def equals():
    second_number = e.get()
    e.delete(0, END)
    # Check which math operation we are doing
    if math == "add":
        e.insert(0, fnum + float(second_number))
    if math == "subtract":
        e.insert(0, fnum - float(second_number))
    if math == "multiply":
        e.insert(0, fnum * float(second_number))
    if math == "divide":
        e.insert(0, fnum / float(second_number))
    if math == "mod":
        e.insert(0, fnum % float(second_number))


# All buttons that are numbers
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonClick(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonClick(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonClick(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonClick(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonClick(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonClick(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonClick(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonClick(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonClick(9))
button0 = Button(root, text="0", padx=40, pady=21, command=lambda: buttonClick(0))

# All buttons that are symbols
buttonBack = Button(root, text="Back", padx=32, pady=18, command=backspace)
buttonClear = Button(root, text="Clear", padx=76, pady=20, bg="#cd5c5c", command=clear)
buttonEquals = Button(root, text="=", padx=40, pady=21, bg="#dcdcdc", command=equals)
buttonNegative = Button(root, text="(-)", padx=36, pady=21, bg="#dcdcdc", command=negative)
buttonPeriod = Button(root, text=".", padx=41, pady=21, bg="#dcdcdc", command=lambda: buttonClick('.'))

# All operation buttons
buttonAdd = Button(root, text="+", padx=40, pady=20, bg="#dcdcdc", command=add)
buttonSubtract = Button(root, text="-", padx=41, pady=20, bg="#dcdcdc", command=subtract)
buttonMultiply = Button(root, text="x", padx=41, pady=20, bg="#dcdcdc", command=multiply)
buttonDivide = Button(root, text="/", padx=41, pady=20, bg="#dcdcdc", command=divide)
buttonMod = Button(root, text="%", padx=38, pady=20, bg="#dcdcdc", command=mod)


# Display buttons using grids
buttonBack.grid(row=0, column=3)

buttonClear.grid(row=1, column=0, columnspan=2) # Grid for Clear
buttonMod.grid(row=1, column=2) # Grid for %
buttonDivide.grid(row=1, column=3)  # Grid for /

button7.grid(row=2, column=0)   # Grid for button 7
button8.grid(row=2, column=1)   # Grid for button 8
button9.grid(row=2, column=2)   # Grid for button 9
buttonMultiply.grid(row=2, column=3)    # Grid for button x

button4.grid(row=3, column=0)   # Grid for button 4
button5.grid(row=3, column=1)   # Grid for button 5
button6.grid(row=3, column=2)   # Grid for button 6
buttonSubtract.grid(row=3, column=3) # Grid for button - 

button1.grid(row=4, column=0)   # Grid for button 1
button2.grid(row=4, column=1)   # Grid for button 2
button3.grid(row=4, column=2)   # Grid for button 2
buttonAdd.grid(row=4, column=3) # Grid for button +

buttonNegative.grid(row=5, column=0) # Grid for button (-)
button0.grid(row=5, column=1)   # Grid for button 0
buttonPeriod.grid(row=5, column=2)
buttonEquals.grid(row=5, column=3)  # Grid fro button Equals



root.mainloop()