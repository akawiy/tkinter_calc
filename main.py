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
        self.root.attributes('-alpha', 0.95)

        self.root.bind("<Key>", self.on_press)

        self.fontconfig()

        self.calc = tk.Entry(self.root, bg="#ffffff", justify=tk.RIGHT, bd=0, font=("Bold", 17))
        self.calc.insert(0, "0")
        self.calc.grid(row=0, column=0, columnspan=4, stick="wens")

        self.num_1 = tk.Button(text="1", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(1))
        self.num_2 = tk.Button(text="2", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(2))
        self.num_3 = tk.Button(text="3", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(3))
        self.num_4 = tk.Button(text="4", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(4))
        self.num_5 = tk.Button(text="5", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(5))
        self.num_6 = tk.Button(text="6", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(6))
        self.num_7 = tk.Button(text="7", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(7))
        self.num_8 = tk.Button(text="8", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(8))
        self.num_9 = tk.Button(text="9", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(9))
        self.num_0 = tk.Button(text="0", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=lambda: self.add_number(0))
        self.op_1 = tk.Button(text="+", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation("+"))
        self.op_2 = tk.Button(text="-", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation("-"))
        self.op_3 = tk.Button(text="×", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation("x"))
        self.op_4 = tk.Button(text="÷", bd=0, bg="lightgray", activebackground="#A7A5A5", font=("Bold", 17), command=lambda: self.add_operation(":"))
        self.calc_btn = tk.Button(text="=", bd=0, bg="#FCA75C", activebackground="#EC8900", font=("Bold", 17), command=self.calculate)
        self.clear_btn = tk.Button(text="C", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=self.clear)
        self.change_sign_btn = tk.Button(text="±", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=self.change_sign)
        self.percent_btn = tk.Button(text="%", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=self.percent)
        self.coma_btn = tk.Button(text=",", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=self.add_coma)
        self.backspace_btn = tk.Button(text="←", bd=0, activebackground="lightgray", font=("Bold", 17), bg='#ECECEC', command=self.backspace)

        self.num_1.grid(row=2, column=0, stick="wens", padx=3, pady=3)
        self.num_2.grid(row=2, column=1, stick="wens", padx=3, pady=3)
        self.num_3.grid(row=2, column=2, stick="wens", padx=3, pady=3)
        self.num_4.grid(row=3, column=0, stick="wens", padx=3, pady=3)
        self.num_5.grid(row=3, column=1, stick="wens", padx=3, pady=3)
        self.num_6.grid(row=3, column=2, stick="wens", padx=3, pady=3)
        self.num_7.grid(row=4, column=0, stick="wens", padx=3, pady=3)
        self.num_8.grid(row=4, column=1, stick="wens", padx=3, pady=3)
        self.num_9.grid(row=4, column=2, stick="wens", padx=3, pady=3)
        self.num_0.grid(row=5, column=1, stick="wens", padx=3, pady=3)
        self.op_1.grid(row=1, column=3, stick="wens", padx=3, pady=3)
        self.op_2.grid(row=2, column=3, stick="wens", padx=3, pady=3)
        self.op_3.grid(row=3, column=3, stick="wens", padx=3, pady=3)
        self.op_4.grid(row=4, column=3, stick="wens", padx=3, pady=3)
        self.calc_btn.grid(row=5, column=3, stick="wens", padx=3, pady=3)
        self.clear_btn.grid(row=1, column=0, stick="wens", padx=3, pady=3)
        self.change_sign_btn.grid(row=5, column=0, stick="wens", padx=3, pady=3)
        self.percent_btn.grid(row=1, column=1, stick="wens", padx=3, pady=3)
        self.coma_btn.grid(row=5, column=2, stick="wens", padx=3, pady=3)
        self.backspace_btn.grid(row=1, column=2, stick="wens", padx=3, pady=3)

        self.on_target(self.num_1, "basic")
        self.on_target(self.num_2, "basic")
        self.on_target(self.num_3, "basic")
        self.on_target(self.num_4, "basic")
        self.on_target(self.num_5, "basic")
        self.on_target(self.num_6, "basic")
        self.on_target(self.num_7, "basic")
        self.on_target(self.num_8, "basic")
        self.on_target(self.num_9, "basic")
        self.on_target(self.num_0, "basic")
        self.on_target(self.op_1, "operation")
        self.on_target(self.op_2, "operation")
        self.on_target(self.op_3, "operation")
        self.on_target(self.op_4, "operation")
        self.on_target(self.calc_btn, "equals")
        self.on_target(self.clear_btn, "basic")
        self.on_target(self.change_sign_btn, "basic")
        self.on_target(self.percent_btn, "basic")
        self.on_target(self.coma_btn, "basic")
        self.on_target(self.backspace_btn, "basic")

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
        if value[-1] in "+-*/":
            value = value[:-1]
        elif "+" in value or "-" in value or "*" in value or "/" in value:
            self.calculate()
            value = self.calc.get()
        self.calc.delete(0, tk.END)
        self.calc.insert(0, value + operation)

    def calculate(self):
        value = self.translate(self.calc.get(), 1)
        if value[-1] in "+-*/":
            value = value + value[:-1]
        self.calc.delete(0, tk.END)
        try:
            self.calc.insert(0, self.translate(self.debug(eval(self.translate(value, 1))), -1))
        except ZeroDivisionError:
            self.calc.insert(0, "Error")
        except SyntaxError:
            self.calc.insert(0, "Error")

    def clear(self):
        self.calc.delete(0, tk.END)
        self.calc.insert(0, "0")

    def change_sign(self):
        value = self.translate(self.calc.get(), 1)
        if "+" not in value and "*" not in value and "/" not in value and ("-" not in value or str(value).find("-") == 0):
            value = self.debug(float(value))
            value = value * -1
        elif value[-1] in "+-*/":
            pass
        elif value[-1] not in "+-*/" and "+" in value or "-" in value or "*" in value or "/" in value:
            pass
        self.calc.delete(0, tk.END)
        self.calc.insert(0, self.translate(value, -1))

    def percent(self):
        value = self.translate(self.calc.get(), 1)
        if "+" not in value and "-" not in value and "*" not in value and "/" not in value:
            value = self.debug(float(value))
            value = value / 100
        elif value[-1] in "+-*/":
            value = value + "0,01"
        elif value[-1] not in "+-*/" and "+" in value or "-" in value or "*" in value or "/" in value:
            operation_pos = 0
            for i in "+-*/":
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
        self.calc.insert(0, self.translate(value, -1))

    def on_press(self, event):
        if event.char.isdigit():
            self.add_number(event.char)
        elif event.char in "+-*/":
            self.add_operation(event.char)
        elif event.char == "\r" or event.char == "=":
            self.calculate()
        elif event.char == "%":
            self.percent()
        elif event.char == "." or event.char == ",":
            self.add_coma()
        elif event.char == "\x08":
            self.backspace()
        elif event.char == "\x7f":
            self.clear()
        else:
            # print(repr(event.char))
            value = str(self.calc.get()).replace(event.char, "")
            self.calc.delete(0, tk.END)
            self.calc.insert(0, value)

    def add_coma(self):
        value = self.translate(self.calc.get(), 1)
        if ("+" not in value and "-" not in value and "*" not in value and "/" not in value) and "." in value:
            pass
        elif ("+" not in value and "-" not in value and "*" not in value and "/" not in value) and "." not in value:
            value += "."
        elif value[-1] in "+-*/":
            value += "0."
        elif value[-1] not in "+-*/" and "+" in value or "-" in value or "*" in value or "/" in value:
            operation_pos = 0
            for i in "+-*/":
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
            if str(num).count(".") > 0:
                pass
            elif str(num).count(".") == 0:
                value = v + str(num) + "."
        self.calc.delete(0, tk.END)
        self.calc.insert(0, self.translate(value, -1))

    def backspace(self):
        value = self.translate(self.calc.get(), 1)
        if value == 0:
            pass
        elif (len(value) == 1 and value != "-") or (len(value) == 2 and value[0] == "-") or value == "Error":
            value = "0"
        else:
            value = value[:-1]
        self.calc.delete(0, tk.END)
        self.calc.insert(0, self.translate(value, -1))

    def fontconfig(self):
        pass

    @staticmethod
    def on_target(button, btn_type):
        if btn_type == "basic":
            button.bind("<Enter>", lambda e: button.config(bg='#DDDDDD'))
            button.bind("<Leave>", lambda e: button.config(bg='#ECECEC'))
        elif btn_type == "operation":
            button.bind("<Enter>", lambda e: button.config(bg='#BBBBBB'))
            button.bind("<Leave>", lambda e: button.config(bg='lightgray'))
        elif btn_type == "equals":
            button.bind("<Enter>", lambda e: button.config(bg='#F89000'))
            button.bind("<Leave>", lambda e: button.config(bg='orange'))

    @staticmethod
    def translate(text, value):
        text = str(text)
        if value > 0:
            text = str(text).replace("x", "*").replace(":", "/").replace(",", ".").replace(" ", "")
        elif value < 0:
            text = str(text).replace("*", "x").replace("/", ":").replace(".", ",")
        return str(text)

    @staticmethod
    def debug(value):
        value = float(value)
        if math.modf(value)[0] == 0:
            return int(value)
        elif math.modf(value)[0] != 0:
            return float(value)


if __name__ == "__main__":
    Main()
