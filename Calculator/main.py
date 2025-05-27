from tkinter import *

window = Tk()
window.geometry("500x500")

my_input = Entry(window, width=200 , borderwidth=5 )
my_input.place(x=10, y=10)

# creating a ideal number pad

def getValuefromButton(value):
    result = my_input.get() + str(value)
    my_input.delete(0, END)
    my_input.insert(0, str(result))
    
    
def addValue():
    result = my_input.get()
    global math
    math = "addition"
    global total
    total = int(result)
    my_input.delete(0, END)
    
def subValue():
    result = my_input.get()
    global math
    math = "subtraction"
    global total
    total = int(result)
    my_input.delete(0, END)
    
    
def multValue():
    result = my_input.get()
    global math
    math = "multiplication"
    global total
    total = int(result)
    my_input.delete(0, END)
    
    
def divValue():
    result = my_input.get()
    global math
    math = "division"
    global total
    total = int(result)
    my_input.delete(0, END)
    
    
def equalValue():
    input_value2 = my_input.get()
    my_input.delete(0, END)
    if math == "addition":
        my_input.insert(0, total + int(input_value2))
    elif math == "subtraction":
        my_input.insert(0, total - int(input_value2))
    elif math == "multiplication":
        my_input.insert(0, total * int(input_value2))
    elif math == "division":
        my_input.insert(0, total / int(input_value2))
        
def clearValue():
    my_input.delete(0, END)
    global total
    total = 0
    global math
    math = ""
    

buttons = Button(window,text='1' ,width=12 ,command=lambda: getValuefromButton(1))
buttons.place(x=20 ,y=140)
buttons = Button(window,text='2' ,width=12 ,command=lambda: getValuefromButton(2))
buttons.place(x=100 ,y=140)
buttons = Button(window,text='3' ,width=12 ,command=lambda: getValuefromButton(3))
buttons.place(x=190 ,y=140)
buttons = Button(window,text='+' ,width=12 ,command=addValue)
buttons.place(x=280 ,y=140)


buttons = Button(window,text='4' ,width=12 ,command=lambda: getValuefromButton(4))
buttons.place(x=20 ,y=160)
buttons = Button(window,text='5' ,width=12 ,command=lambda: getValuefromButton(5))
buttons.place(x=100 ,y=160)
buttons = Button(window,text='6' ,width=12 ,command=lambda: getValuefromButton(6))
buttons.place(x=190 ,y=160)
buttons = Button(window,text='-' ,width=12 ,command=subValue)
buttons.place(x=280 ,y=160)


buttons = Button(window, text='7' ,width=12 ,command=lambda: getValuefromButton(7))
buttons.place(x=20 ,y=180)
buttons = Button(window,text='8' ,width=12 ,command=lambda: getValuefromButton(8))
buttons.place(x=100 ,y=180)
buttons = Button(window,text='9' ,width=12 ,command=lambda: getValuefromButton(9))
buttons.place(x=190 ,y=180)
buttons = Button(window,text='*' ,width=12 ,command=multValue)
buttons.place(x=280 ,y=180)


buttons = Button(window,text='0' ,width=12 ,command=lambda: getValuefromButton(0))
buttons.place(x=20 ,y=200)
buttons = Button(window,text='=' ,width=12 ,command=equalValue)
buttons.place(x=100 ,y=200)
buttons = Button(window,text='Clear' ,width=12 ,command=clearValue)
buttons.place(x=190 ,y=200)
buttons = Button(window,text='/' ,width=12,command=divValue)
buttons.place(x=280 ,y=200)
    
    
# def getValuefrom
    


mainloop()