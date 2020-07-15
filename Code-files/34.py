from tkinter import *
def click(num):
    global operator
    operator = operator + str(num)
    input_text.set(operator)
def clear():
    global operator
    operator = ""
    input_text.set("")
def equal():
    global operator
    eq = str(eval(operator))
    input_text.set(eq)
window = Tk()
window.title("Calculator")
operator = ""
input_text = StringVar()
text_disp = Entry(window, textvariable = input_text, bd = 10, insertwidth = 3,
                  bg = "#bbbbbb",fg = "#303030", justify = "right",
                  font = ("Arial", 60, 'bold')).grid(columnspan=4)
#First row.
bt_clear = Button(window, bd = 5, fg = "#303030", text = "Clear",
             font =("Arial", 30, 'bold'), command = clear
             ).grid(row = 1, column = 0)
bt_div = Button(window, bd = 5, fg = "#303030", text = "/", padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click("/")
             ).grid(row = 1, column = 3)
#Second row.
bt7 = Button(window, bd = 5, fg = "#303030", text = 7, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(7)
             ).grid(row = 2, column = 0)
bt8 = Button(window, bd = 5, fg = "#303030", text = 8, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(8)
             ).grid(row = 2, column = 1)
bt9 = Button(window, bd = 5, fg = "#303030", text = 9, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(9)
             ).grid(row = 2, column = 2)
bt_mult = Button(window, bd = 5, fg = "#303030", text = "*", padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click("*")
             ).grid(row = 2, column = 3)
#Third row.
bt4 = Button(window, bd = 5, fg = "#303030", text = 4, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(4)
             ).grid(row = 3, column = 0)
bt5 = Button(window, bd = 5, fg = "#303030", text = 5, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(5)
             ).grid(row = 3, column = 1)
bt6 = Button(window, bd = 5, fg = "#303030", text = 6, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(6)
             ).grid(row = 3, column = 2)
bt_add = Button(window, bd = 5, fg = "#303030", text = "+", padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click("+")
             ).grid(row = 3, column = 3)
#Third row.
bt1 = Button(window, bd = 5, fg = "#303030", text = 1, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(1)
             ).grid(row = 4, column = 0)
bt2 = Button(window, bd = 5, fg = "#303030", text = 2, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(2)
             ).grid(row = 4, column = 1)
bt3 = Button(window, bd = 5, fg = "#303030", text = 3, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(3)
             ).grid(row = 4, column = 2)
bt_sub = Button(window, bd = 5, fg = "#303030", text = "-", padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click("-")
             ).grid(row = 4, column = 3)
#Fourth row.
bt_dec = Button(window, bd = 5, fg = "#303030", text = ".", padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(".")
             ).grid(row = 5, column = 0)
bt0 = Button(window, bd = 5, fg = "#303030", text = 0, padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click(0)
             ).grid(row = 5, column = 1)
bt_perc = Button(window, bd = 5, fg = "#303030", text = "%", padx = 50,
             font =("Arial", 30, 'bold'), command = lambda:click("%")
             ).grid(row = 5, column = 2)
bt_eq = Button(window, bd = 5, fg = "#303030", text = "=", padx = 50,
             font =("Arial", 30, 'bold'), command = equal
             ).grid(row = 5, column = 3)
window.mainloop()