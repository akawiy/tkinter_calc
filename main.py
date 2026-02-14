import tkinter as tk
import math


class Main:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("250x300")
        self.root.minsize(250, 300)
        self.root.update()
        self.root["bg"] = "#ffffff"
        self.root.title("Calculator")

        self.root.bind("<Key>", self.on_press)

        self.calc = tk.Entry(self.root, justify=tk.RIGHT, bd=0, font=("Bold", 17))
        self.calc.insert(0, "0")
        self.calc.grid(row=0, column=0, columnspan=4, stick="wens")

        self.num_1 = tk.Button(text="1", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(1))
        self.num_2 = tk.Button(text="2", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(2))
        self.num_3 = tk.Button(text="3", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(3))
        self.num_4 = tk.Button(text="4", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(4))
        self.num_5 = tk.Button(text="5", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(5))
        self.num_6 = tk.Button(text="6", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(6))
        self.num_7 = tk.Button(text="7", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(7))
        self.num_8 = tk.Button(text="8", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(8))
        self.num_9 = tk.Button(text="9", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(9))
        self.num_0 = tk.Button(text="0", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=lambda: self.add_number(0))
        self.op_1 = tk.Button(text="+", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation("+"))
        self.op_2 = tk.Button(text="-", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation("-"))
        self.op_3 = tk.Button(text="x", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation("x"))
        self.op_4 = tk.Button(text=":", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation(":"))
        self.calc_btn = tk.Button(text="=", bd=0, bg="#FCA75C", activebackground="#FC8A27", font=("Bold", 17), command=self.calculate)
        self.clear_btn = tk.Button(text="C", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=self.clear)
        self.change_sign_btn = tk.Button(text="+/-", bd=0, activebackground="#E7E4E4", font=("Bold", 13), command=self.change_sign)
        self.percent_btn = tk.Button(text="%", bd=0, activebackground="#E7E4E4", font=("Bold", 17), command=self.percent)

        self.num_1.grid(row=2, column=0, stick="wens", padx=3, pady=3)
        self.num_2.grid(row=2, column=1, stick="wens", padx=3, pady=3)
        self.num_3.grid(row=2, column=2, stick="wens", padx=3, pady=3)
        self.num_4.grid(row=3, column=0, stick="wens", padx=3, pady=3)
        self.num_5.grid(row=3, column=1, stick="wens", padx=3, pady=3)
        self.num_6.grid(row=3, column=2, stick="wens", padx=3, pady=3)
        self.num_7.grid(row=4, column=0, stick="wens", padx=3, pady=3)
        self.num_8.grid(row=4, column=1, stick="wens", padx=3, pady=3)
        self.num_9.grid(row=4, column=2, stick="wens", padx=3, pady=3)
        self.num_0.grid(row=5, column=0, stick="wens", padx=3, pady=3)
        self.op_1.grid(row=1, column=3, stick="wens", padx=3, pady=3)
        self.op_2.grid(row=2, column=3, stick="wens", padx=3, pady=3)
        self.op_3.grid(row=3, column=3, stick="wens", padx=3, pady=3)
        self.op_4.grid(row=4, column=3, stick="wens", padx=3, pady=3)
        self.calc_btn.grid(row=5, column=3, stick="wens", padx=3, pady=3)
        self.clear_btn.grid(row=1, column=0, stick="wens", padx=3, pady=3)
        self.change_sign_btn.grid(row=1, column=1, stick="wens", padx=3, pady=3)
        self.percent_btn.grid(row=1, column=2, stick="wens", padx=3, pady=3)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)

        self.root.mainloop()

    def add_number(self, num):
        value = self.calc.get()
        if value[0] == "0" and len(value) == 1:
            value = value[1:]
        elif value == "Error":
            value = value[5:]
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value + str(num))

    def add_operation(self, operation):
        value = self.calc.get()
        if value == "Error":
            value = "0"
        if value[-1] in "+-x:":
            value = value[:-1]
        elif "+" in value or "-" in value or "x" in value or ":" in value:
            self.calculate()
            value = self.calc.get()
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value + operation)

    def calculate(self):
        value = self.calc.get()
        if value[-1] in "+-x:":
            value = value + value[:-1]
        self.calc.delete(0, tk.END)
        try:
            self.calc.insert(0, self.debug(eval(str(value).replace("x", "*").replace(":", "/"))))
        except ZeroDivisionError:
            self.calc.insert(0, "Error")

    def clear(self):
        self.calc.delete(0, tk.END)
        self.calc.insert(0, "0")

    def change_sign(self):
        value = self.calc.get()
        if "+" not in value and "-" not in value and "x" not in value and ":" not in value:
            value = self.debug(value)
            value = value * -1
        elif value[-1] in "+-x:":
            pass
        elif value[-1] not in "+-x:" and "+" in value or "-" in value or "x" in value or ":" in value:
            pass
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value)

    def percent(self):
        value = self.calc.get()
        if "+" not in value and "-" not in value and "x" not in value and ":" not in value:
            value = self.debug(value)
            value = value / 100
        elif value[-1] in "+-x:":
            value = value + "0.01"
        elif value[-1] not in "+-x:" and "+" in value or "-" in value or "x" in value or ":" in value:
            operation_pos = 0
            for i in "+-x:":
                if str(value).find(i) == -1:
                    pass
                elif str(value).find(i) > 0:
                    operation_pos = str(value).find(i)
                    break
            self.calc.delete(0, operation_pos + 1)
            num = self.debug(float(self.calc.get()))
            self.calc.insert(0, value)
            self.calc.delete(operation_pos + 1, tk.END)
            v = str(self.calc.get())
            value = v + str(num / 100)
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value)

    def on_press(self, event):
        if event.char.isdigit():
            self.add_number(event.char)
        elif event.char in "+-*/":
            self.add_operation(event.char)
        elif event.char == "\r" or event.char == "=":
            self.calculate()

    def fontconfig(self):
        pass

    @staticmethod
    def debug(value):
        value = float(value)
        if math.modf(value)[0] == 0:
            return int(value)
        elif math.modf(value)[0] != 0:
            return float(value)


if __name__ == "__main__":
    Main()
