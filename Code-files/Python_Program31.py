import tkinter as tk
font_def = ("Arial", 20, "bold")
window = tk.Tk()
window.title("Sum calc")
window.config(bg = "#aaaaaa")
window.geometry("400x400")
tk.Label(bg = "#aaaaaa").pack()
num1_lab = tk.Label(window, bg = "#aaa", text = "Enter number 1", font = font_def).pack()
num1_ent = tk.Entry(window, text = "Number 1", font = font_def)
num1_ent.pack()
num2_lab = tk.Label(window, bg = "#aaa", text = "Enter number 2", font = font_def).pack()
num2_ent = tk.Entry(window, text = "Number 2", font = font_def)
num2_ent.pack()


def display(num1, num2):
	summ = num1 + num2
	lab.configure(text = str(summ), font = font_def)

tk.Label(bg = "#aaaaaa").pack()

lab = tk.Label(window, bg = "#aaaaaa", fg = "#401010", font = font_def)
lab.pack()
tk.Label(bg = "#aaaaaa").pack()
button = tk.Button(window, text = "Calculate", bg = "#ffffff", font = font_def, command = display(num1_ent.get(), num2_ent.get()))
button.pack()

window.mainloop()