import tkinter as tk
window = tk.Tk()
window.geometry("500x200")
window.title("Counter")
window.configure(bg = "#aaaaaa")
title_label = tk.Label(text = "Counter", fg = "#404040", bg = "#aaaaaa", font = ("Arial", 20, "bold"))
title_label.pack()
sec = 1000
counter = 0
def counter_label(label):
	counter = 0
	def count():
		global counter
		counter += 1
		label.config(text = str(counter))
		label.after(sec, count)
	count()
label = tk.Label(window, fg = "#404040", bg = "#aaaaaa", font = ("Arial", 20, "bold"))
label.pack()
counter_label(label)
button = tk.Button(window, text = "Stop", fg = "#fff", bg = "#401010", font = ("Arial", 20, "bold"), command = window.destroy)
button.pack()
window.mainloop()