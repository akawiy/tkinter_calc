try:
    import tkinter as tk
    from tkinter import messagebox
except ModuleNotFoundError:
    import Tkinter as tk
    from Tkinter import messagebox
import math
from time import sleep


class Main:
    def __init__(self):
        # Main label (root)
        self.root = tk.Tk()

        self.root.geometry("500x500")
        self.root.minsize(400, 500)
        # Min (250, 300)
        self.root.update()
        self.root["bg"] = "#ffffff"
        self.root.title("Calculator")
        self.root.attributes('-alpha', 0.97)

        self.fullscreen_value = False
        self.root.attributes('-fullscreen', self.fullscreen_value)

        self.calc_info = "Version: 1.3\nBy: Vladimir Polischuk\nRelease date: 18.12.2021\n\nWhat's new: new design, added menu, information and settings buttons, added a new dark theme, " \
                         "added full-screen mode, fixed about 4 bugs."

        # EN: I started making this calculator to check if I am capable of it,
        # if I have enough programming knowledge. I didn't expect that he would become so cool (in my opinion).
        # If you see this message, I would like to personally thank you for downloading it and reading this message now.
        # Since this program is still in development, and does not yet have the coolest chips that I plan to add,
        # so if you find some error in the calculator, or you have ideas / suggestions for improving it, I ask you to report it by email.

        # RUS: Я начал делать этот калькулятор чтобы проверить, способен ли я на это, хватает ли у меня знаний программирования.
        # Я не ожидал то что он будет становиться настолько крутым (по моему мнению). Если вы видите это сообщение,
        # мне хочется лично поблагодарить вас за то, что вы его скачали, и сейчас читаете это сообщение.
        # Так как эта программа ещё находится в разработке, и ещё не имеет самых крутых фишек которые я планирую добавить,
        # поэтому если вы нашли какую-то ошибку в калькуляторе, или у вас есть идеи/предложения по его совершенствованию, прошу вас сообщить об этом на почту.

        self.root.bind("<Key>", self.on_press)
        self.root.bind("<F11>", self.fullscreen)

        self.entry = tk.Entry(self.root, bg="#ffffff", justify=tk.RIGHT, bd=0, font=("Bold", 30))
        self.entry.insert(0, "0")
        self.entry.grid(row=0, column=0, columnspan=4, stick="wens")

        self.equals = False

        self.num_1 = tk.Button(text="1", bd=0, font=("Bold", 20), command=lambda: self.add_number(1))
        self.num_2 = tk.Button(text="2", bd=0, font=("Bold", 20), command=lambda: self.add_number(2))
        self.num_3 = tk.Button(text="3", bd=0, font=("Bold", 20), command=lambda: self.add_number(3))
        self.num_4 = tk.Button(text="4", bd=0, font=("Bold", 20), command=lambda: self.add_number(4))
        self.num_5 = tk.Button(text="5", bd=0, font=("Bold", 20), command=lambda: self.add_number(5))
        self.num_6 = tk.Button(text="6", bd=0, font=("Bold", 20), command=lambda: self.add_number(6))
        self.num_7 = tk.Button(text="7", bd=0, font=("Bold", 20), command=lambda: self.add_number(7))
        self.num_8 = tk.Button(text="8", bd=0, font=("Bold", 20), command=lambda: self.add_number(8))
        self.num_9 = tk.Button(text="9", bd=0, font=("Bold", 20), command=lambda: self.add_number(9))
        self.num_0 = tk.Button(text="0", bd=0, font=("Bold", 20), command=lambda: self.add_number(0))
        self.op_1 = tk.Button(text="+", bd=0, font=("Bold", 20), command=lambda: self.add_operation("+"))
        self.op_2 = tk.Button(text="-", bd=0, font=("Bold", 20), command=lambda: self.add_operation("-"))
        self.op_3 = tk.Button(text="×", bd=0, font=("Bold", 20), command=lambda: self.add_operation("x"))
        self.op_4 = tk.Button(text="÷", bd=0, font=("Bold", 20), command=lambda: self.add_operation(":"))
        self.calc_btn = tk.Button(text="=", bd=0, bg="#008D3B", font=("Bold", 20), command=self.calculate)
        self.clear_btn = tk.Button(text="C", bd=0, font=("Bold", 20), bg='#ECECEC', command=self.clear)
        self.change_sign_btn = tk.Button(text="±", bd=0, font=("Bold", 20), bg='#ECECEC', command=self.change_sign)
        self.percent_btn = tk.Button(text="%", bd=0, font=("Bold", 20), bg='#ECECEC', command=self.percent)
        self.coma_btn = tk.Button(text=",", bd=0, font=("Bold", 20), bg='#ECECEC', command=self.add_coma)
        self.backspace_btn = tk.Button(text="←", bd=0, font=("Bold", 20), bg='#ECECEC', command=self.backspace)
        self.more_btn = tk.Button(text="≡", bd=0, font=("Bold", 20), bg='#ECECEC', command=self.more)

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
        self.more_btn.grid(row=0, column=0, stick="wens", padx=3, pady=3)

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

        # Menu label
        self.more_active = False

        self.more_label = tk.Label(bg="#ffffff")
        self.more_label.grid_forget()

        self.sett_btn = tk.Button(self.more_label, text="Settings ⚙", bd=0, font=("Bold", 20), command=self.settings)
        self.more_btn_2 = tk.Button(self.more_label, text="Test 2", bd=0, font=("Bold", 20))
        self.more_btn_3 = tk.Button(self.more_label, text="Test 3", bd=0, font=("Bold", 20))
        self.more_btn_4 = tk.Button(self.more_label, text="Test 4", bd=0, font=("Bold", 20))
        self.info_btn = tk.Button(self.more_label, text="Info i", bd=0, font=("Bold", 20),
                                  command=lambda: messagebox.showinfo(title="Calc info", message=self.calc_info))

        self.sett_btn.grid(row=0, column=0, columnspan=4, stick="wens", padx=3, pady=3)
        self.more_btn_2.grid(row=1, column=0, columnspan=4, stick="wens", padx=3, pady=3)
        self.more_btn_3.grid(row=2, column=0, columnspan=4, stick="wens", padx=3, pady=3)
        self.more_btn_4.grid(row=3, column=0, columnspan=4, stick="wens", padx=3, pady=3)
        self.info_btn.grid(row=4, column=0, columnspan=4, stick="wens", padx=3, pady=3)

        self.more_label.grid_columnconfigure(0, weight=1)

        self.more_label.grid_rowconfigure(0, weight=1)
        self.more_label.grid_rowconfigure(1, weight=1)
        self.more_label.grid_rowconfigure(2, weight=1)
        self.more_label.grid_rowconfigure(3, weight=1)
        self.more_label.grid_rowconfigure(4, weight=1)

        # Settings label
        self.sett_label = tk.Label(bg="#ffffff")
        self.sett_label.grid_forget()

        self.theme = "light"

        self.theme_btn = tk.Button(self.sett_label, text="Theme: " + self.theme, bd=0, font=("Bold", 20), command=self.change_theme)

        self.theme_btn.grid(row=0, column=0, stick="wens", columnspan=4, padx=3, pady=3)

        self.sett_label.grid_columnconfigure(0, weight=1)
        self.sett_label.grid_columnconfigure(1, weight=1)
        self.sett_label.grid_columnconfigure(2, weight=1)
        self.sett_label.grid_columnconfigure(3, weight=1)

        self.sett_label.grid_rowconfigure(0, weight=1)
        self.sett_label.grid_rowconfigure(1, weight=1)
        self.sett_label.grid_rowconfigure(2, weight=1)
        self.sett_label.grid_rowconfigure(3, weight=1)
        self.sett_label.grid_rowconfigure(4, weight=1)
        self.sett_label.grid_rowconfigure(5, weight=1)

        # Reload
        self.reload()

        # Mainloop
        self.root.mainloop()

    # Functions
    def add_number(self, num):
        value = self.entry.get()
        if self.equals:
            value = "0"
            self.equals = False
        if value[0] == "0" and len(value) == 1:
            value = value[1:]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value + str(num))

    def add_operation(self, operation):
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        for i in range(len(value)):
            if value[-1] == "0" and "." in value:
                value = value[:-1]
            elif value[-1] == ".":
                value = value[:-1]
        if value[-1] in "+-*/":
            value = value[:-1]
        elif "+" in value or "-" in value or "*" in value or "/" in value:
            self.calculate(eq=False)
            value = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1) + self.translate(operation, -1))

    def calculate(self, eq=True):
        value = self.translate(self.entry.get(), 1)
        if value[-1] in "+-*/":
            value = value + value[:-1]
        self.entry.delete(0, tk.END)
        try:
            self.entry.insert(0, self.translate(self.debug(eval(self.translate(value, 1))), -1))
            if eq:
                self.equals = True
        except ZeroDivisionError:
            self.entry.insert(0, "0")
            messagebox.showerror("Error", "Error: \n\nCan't divide by zero.")
        except SyntaxError:
            self.entry.insert(0, "0")
            messagebox.showerror("Error", "Unknown error: \n\nPlease check syntax.")

    def clear(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "0")

    def change_sign(self):
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        if "+" not in value and "*" not in value and "/" not in value and ("-" not in value or str(value).find("-") == 0):
            value = self.debug(float(value))
            value = value * -1
        elif value[-1] in "+-*/":
            pass
        elif value[-1] not in "+-*/" and "+" in value or "-" in value or "*" in value or "/" in value:
            pass
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))

    def percent(self):
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        if "+" not in value and "-" not in value and "*" not in value and "/" not in value:
            if value != "0" and value != "0.":
                value = self.debug(float(value))
                value = value / 100
        elif value[-1] in "+-*/":
            value = value + "0.01"
        elif value[-1] not in "+-*/" and "+" in value or "-" in value or "*" in value or "/" in value:
            operation_pos = 0
            for i in "+-*/":
                if str(value).find(i) == -1:
                    pass
                elif str(value).find(i) > 0:
                    operation_pos = str(value).find(i)
                    break
            self.entry.delete(0, operation_pos + 1)
            num = self.debug(float(self.translate(self.entry.get(), 1)))
            self.entry.insert(0, value)
            self.entry.delete(operation_pos + 1, tk.END)
            v = str(self.translate(self.entry.get(), 1))
            value = v + str(num / 100)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))

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
        elif event.char == "\x1b" and self.more_active:
            self.more()
        else:
            # print(repr(event.char))
            value = str(self.entry.get()).replace(event.char, "")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, value)

    def add_coma(self):
        value = self.translate(self.entry.get(), 1)
        self.equals = False
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
            self.entry.delete(0, operation_pos + 1)
            num = self.debug(float(self.translate(self.entry.get(), 1)))
            self.entry.insert(0, value)
            self.entry.delete(operation_pos + 1, tk.END)
            v = str(self.translate(self.entry.get(), 1))
            if str(num).count(".") > 0:
                pass
            elif str(num).count(".") == 0:
                value = v + str(num) + "."
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))

    def backspace(self):
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        if value == 0:
            pass
        elif (len(value) == 1 and value != "-") or (len(value) == 2 and value[0] == "-"):
            value = "0"
        else:
            value = value[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))

    def more(self):
        if self.more_active:
            self.more_label.grid_forget()
            self.sett_label.grid_forget()
            self.more_btn["text"] = "≡"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "0")
            self.more_active = False
        elif not self.more_active:
            self.more_label.grid(row=1, column=0, rowspan=5, columnspan=4, stick="wens", padx=0, pady=0)
            self.more_btn["text"] = "<"
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Menu")
            self.more_active = True

    def settings(self):
        self.more_label.grid_forget()
        self.sett_label.grid(row=1, column=0, rowspan=5, columnspan=4, stick="wens", padx=0, pady=0)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Settings")

    def fontconfig(self):
        pass

    def change_theme(self):
        if self.theme == "light":
            self.root["bg"] = "#2A2A2A"
            self.entry["bg"] = "#2A2A2A"
            self.more_label["bg"] = "#2A2A2A"
            self.sett_label["bg"] = "#2A2A2A"
            self.entry["fg"] = "#ffffff"
            self.theme = "dark"
            self.theme_btn["text"] = "Theme: dark"
            self.button_colors_reload()
            self.more()
        elif self.theme == "dark":
            self.root["bg"] = "#DDDDDD"
            self.entry["bg"] = "#DDDDDD"
            self.more_label["bg"] = "#DDDDDD"
            self.sett_label["bg"] = "#DDDDDD"
            self.entry["fg"] = "#000000"
            self.theme = "light"
            self.theme_btn["text"] = "Theme: light"
            self.button_colors_reload()
            self.more()

    def button_colors(self, button, btn_type):
        if self.theme == "light":
            if btn_type == "number":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#ffffff'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#ffffff")
            elif btn_type == "operation":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#EAEAEA'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#EAEAEA")
            elif btn_type == "equals":
                button.bind("<Enter>", lambda e: button.config(bg='#01A444'))
                button.bind("<Leave>", lambda e: button.config(bg='#008D3B'))
                button.config(activebackground="#00BE4F", activeforeground="#000000", fg="#000000", bg="#008D3B")
            elif btn_type == "attention":
                button.bind("<Enter>", lambda e: button.config(bg='#F78181'))
                button.bind("<Leave>", lambda e: button.config(bg='#ECECEC'))
                button.config(activebackground="#FA5858", activeforeground="#000000", fg="#000000", bg="#ECECEC")
        elif self.theme == "dark":
            if btn_type == "number":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#000000'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#000000")
            elif btn_type == "operation":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#1A1A1A'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#1A1A1A")
            elif btn_type == "equals":
                button.bind("<Enter>", lambda e: button.config(bg='#01A444'))
                button.bind("<Leave>", lambda e: button.config(bg='#008D3B'))
                button.config(activebackground="#00BE4F", activeforeground="#ffffff", fg="#ffffff", bg="#008D3B")
            elif btn_type == "attention":
                button.bind("<Enter>", lambda e: button.config(bg='#610B0B'))
                button.bind("<Leave>", lambda e: button.config(bg='#585858'))
                button.config(activebackground="#770000", activeforeground="#ffffff", fg="#ffffff", bg="#610B0B")

    def button_colors_reload(self):
        self.button_colors(self.num_1, "number")
        self.button_colors(self.num_2, "number")
        self.button_colors(self.num_3, "number")
        self.button_colors(self.num_4, "number")
        self.button_colors(self.num_5, "number")
        self.button_colors(self.num_6, "number")
        self.button_colors(self.num_7, "number")
        self.button_colors(self.num_8, "number")
        self.button_colors(self.num_9, "number")
        self.button_colors(self.num_0, "number")
        self.button_colors(self.op_1, "operation")
        self.button_colors(self.op_2, "operation")
        self.button_colors(self.op_3, "operation")
        self.button_colors(self.op_4, "operation")
        self.button_colors(self.calc_btn, "equals")
        self.button_colors(self.clear_btn, "operation")
        self.button_colors(self.change_sign_btn, "operation")
        self.button_colors(self.percent_btn, "operation")
        self.button_colors(self.coma_btn, "operation")
        self.button_colors(self.backspace_btn, "operation")
        self.button_colors(self.more_btn, "operation")

        self.button_colors(self.sett_btn, "number")
        self.button_colors(self.info_btn, "number")

        self.button_colors(self.theme_btn, "number")

    def reload(self):
        self.button_colors_reload()
        if self.theme == "dark":
            self.root["bg"] = "#2A2A2A"
            self.entry["bg"] = "#2A2A2A"
            self.more_label["bg"] = "#2A2A2A"
            self.sett_label["bg"] = "#2A2A2A"
            self.entry["fg"] = "#ffffff"
            self.theme = "dark"
            self.theme_btn["text"] = "Theme: dark"
        elif self.theme == "light":
            self.root["bg"] = "#DDDDDD"
            self.entry["bg"] = "#DDDDDD"
            self.more_label["bg"] = "#DDDDDD"
            self.sett_label["bg"] = "#DDDDDD"
            self.entry["fg"] = "#000000"
            self.theme = "light"
            self.theme_btn["text"] = "Theme: light"
        sleep(1)

    def fullscreen(self, event):
        if self.fullscreen_value:
            self.fullscreen_value = False
        elif not self.fullscreen_value:
            self.fullscreen_value = True
        self.root.attributes("-fullscreen", self.fullscreen_value)
        if not self.fullscreen_value:
            sleep(1)

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
            value = int(value)
        elif math.modf(value)[0] != 0:
            value = float(value)
        return value


# Starting
if __name__ == "__main__":
    Main()
