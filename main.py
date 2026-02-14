import tkinter as tk


def calculate():
    value = calc.get()
    if value[-1] in "+-x:*/":
        value = value + value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except ZeroDivisionError:
        calc.insert(0, "Error")


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, "0")


def add_digit(digit):
    value = calc.get()
    if value[0] == "0" and len(value) == 1:
        value = value[1:]
    elif value == "Error":
        value = value[5:]
    calc.delete(0, tk.END)
    calc.insert(0, value + str(digit))


def add_operation(operation):
    value = calc.get()
    if value[-1] in "+-x:*/":
        value = value[:-1]
    elif "+" in value or "-" in value or "*" in value or "/" in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)


def add_coma():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value + ".")


def make_operation_button(operation):
    return tk.Button(text=str(operation), bd=0, font=("Bold", 17), command=lambda: add_operation(operation))


def make_calc_button(operation):
    return tk.Button(text=str(operation), bd=0, font=("Bold", 17), command=calculate)


def make_clear_button(operation):
    return tk.Button(text=str(operation), bd=0, font=("Bold", 17), command=clear)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in "+-*/":
        add_operation(event.char)
    elif event.char == "\r" or event.char == "=":
        calculate()
    elif event.char == ".":
        add_coma()


win = tk.Tk()
win.geometry("250x300")
win.minsize(250, 300)
win.update()
win["bg"] = "#ffffff"
win.title("Calculator")
win.bind("<Key>", press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=("Arial", 30), bd=0)
calc.insert(0, "0")
calc.grid(row=0, column=0, columnspan=4, stick="wens")

num_1 = tk.Button(text=str(1), bd=0, font=("Bold", 20), command=lambda: add_digit(1))
num_1.grid(row=2, column=0, stick="wens", padx=3, pady=3)
num_2 = tk.Button(text=str(2), bd=0, font=("Bold", 20), command=lambda: add_digit(2))
num_2.grid(row=2, column=1, stick="wens", padx=3, pady=3)
num_3 = tk.Button(text=str(3), bd=0, font=("Bold", 20), command=lambda: add_digit(3))
num_3.grid(row=2, column=2, stick="wens", padx=3, pady=3)
num_4 = tk.Button(text=str(4), bd=0, font=("Bold", 20), command=lambda: add_digit(4))
num_4.grid(row=3, column=0, stick="wens", padx=3, pady=3)
num_5 = tk.Button(text=str(5), bd=0, font=("Bold", 20), command=lambda: add_digit(5))
num_5.grid(row=3, column=1, stick="wens", padx=3, pady=3)
num_6 = tk.Button(text=str(6), bd=0, font=("Bold", 20), command=lambda: add_digit(6))
num_6.grid(row=3, column=2, stick="wens", padx=3, pady=3)
num_7 = tk.Button(text=str(7), bd=0, font=("Bold", 20), command=lambda: add_digit(7))
num_7.grid(row=4, column=0, stick="wens", padx=3, pady=3)
num_8 = tk.Button(text=str(8), bd=0, font=("Bold", 20), command=lambda: add_digit(8))
num_8.grid(row=4, column=1, stick="wens", padx=3, pady=3)
num_9 = tk.Button(text=str(9), bd=0, font=("Bold", 20), command=lambda: add_digit(9))
num_9.grid(row=4, column=2, stick="wens", padx=3, pady=3)
num_0 = tk.Button(text=str(0), bd=0, font=("Bold", 20), command=lambda: add_digit(0))
num_0.grid(row=5, column=0, stick="wens", padx=3, pady=3, columnspan=2)

tk.Button(text=".", bd=0, font=("Bold", 17), command=add_coma).grid(row=5, column=2, stick="wens", padx=3, pady=3)

make_operation_button("+").grid(row=1, column=3, stick="wens", padx=3, pady=3)
make_operation_button("-").grid(row=2, column=3, stick="wens", padx=3, pady=3)
make_operation_button("*").grid(row=3, column=3, stick="wens", padx=3, pady=3)
make_operation_button("/").grid(row=4, column=3, stick="wens", padx=3, pady=3)

make_calc_button("=").grid(row=5, column=3, stick="wens", padx=3, pady=3)
make_clear_button("C").grid(row=1, column=0, stick="wens", padx=3, pady=3)

win.grid_columnconfigure(0, weight=1)
win.grid_columnconfigure(1, weight=1)
win.grid_columnconfigure(2, weight=1)
win.grid_columnconfigure(3, weight=1)

win.grid_rowconfigure(0, weight=1)
win.grid_rowconfigure(1, weight=1)
win.grid_rowconfigure(2, weight=1)
win.grid_rowconfigure(3, weight=1)
win.grid_rowconfigure(4, weight=1)
win.grid_rowconfigure(5, weight=1)

win.mainloop()
