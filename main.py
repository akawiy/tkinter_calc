# First 500 strings: 20.12.2021

import sys


import tkinter as tk
from tkinter import messagebox
# except ModuleNotFoundError:
#     import Tkinter as tk
#     from Tkinter import messagebox
import math
from time import sleep


run = True


class Main:
    def __init__(self):
        # Main label (root)
        self.root = tk.Tk()

        self.root.geometry("300x400")
        self.root.minsize(200, 330)
        self.root.update()
        self.root["bg"] = "#ffffff"
        self.root.title("Calculator")
        self.root.attributes('-alpha', 0.97)

        self.fullscreen_value = False
        self.calc_info = "Version: 1.4\nBy: Vladimir Polischuk\nRelease date: 22.12.2021\n\nWhat's new: fixed bugs, added exit and fullscreen buttons, optimised for different sizes."
        self.entry_font = ("Bold", 30)
        self.font = ("Bold", 20)
        self.font_mini = ("Arial", 17)
        self.cursor = "hand2"
        self.bd = 0
        self.pad = 3
        self.theme = "light"

        self.root.attributes('-fullscreen', self.fullscreen_value)
        self.win_size = [self.root.winfo_width(), self.root.winfo_height()]
        self.on_scale()

        self.root.bind("<Key>", self.on_press)
        self.root.bind("<F11>", self.fullscreen)

        self.entry = tk.Entry(self.root, bg="#ffffff", justify=tk.RIGHT, bd=0, font=self.entry_font, cursor="hand2")
        self.entry.insert(0, "0")
        self.entry.config(state=tk.DISABLED)
        self.entry.grid(row=1, column=0, columnspan=4, stick="wens")
        self.last_value = "0"
        self.memory = 0

        self.equals = False

        self.num_1 = tk.Button(text="1", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(1))
        self.num_2 = tk.Button(text="2", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(2))
        self.num_3 = tk.Button(text="3", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(3))
        self.num_4 = tk.Button(text="4", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(4))
        self.num_5 = tk.Button(text="5", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(5))
        self.num_6 = tk.Button(text="6", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(6))
        self.num_7 = tk.Button(text="7", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(7))
        self.num_8 = tk.Button(text="8", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(8))
        self.num_9 = tk.Button(text="9", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(9))
        self.num_0 = tk.Button(text="0", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_number(0))
        self.op_1 = tk.Button(text="+", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_operation("+"))
        self.op_2 = tk.Button(text="-", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_operation("-"))
        self.op_3 = tk.Button(text="×", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_operation("×"))
        self.op_4 = tk.Button(text="÷", bd=self.bd, font=self.font, cursor=self.cursor, command=lambda: self.add_operation("÷"))
        self.calc_btn = tk.Button(text="=", bd=self.bd, font=self.font, cursor=self.cursor, command=self.calculate)
        self.clear_btn = tk.Button(text="C", bd=self.bd, font=self.font, cursor=self.cursor, command=self.clear)
        self.change_sign_btn = tk.Button(text="±", bd=self.bd, font=self.font, cursor=self.cursor, command=self.change_sign)
        self.percent_btn = tk.Button(text="%", bd=self.bd, font=self.font, cursor=self.cursor, command=self.percent)
        self.coma_btn = tk.Button(text=",", bd=self.bd, font=self.font, cursor=self.cursor, command=self.add_coma)
        self.backspace_btn = tk.Button(text="←", bd=self.bd, font=self.font, cursor=self.cursor, command=self.backspace)
        self.close_menu_btn = tk.Button(text="<", bd=self.bd, font=self.font, cursor=self.cursor, command=self.more)

        self.num_1.grid(row=4, column=0, stick="wens", padx=self.pad, pady=self.pad)
        self.num_2.grid(row=4, column=1, stick="wens", padx=self.pad, pady=self.pad)
        self.num_3.grid(row=4, column=2, stick="wens", padx=self.pad, pady=self.pad)
        self.num_4.grid(row=5, column=0, stick="wens", padx=self.pad, pady=self.pad)
        self.num_5.grid(row=5, column=1, stick="wens", padx=self.pad, pady=self.pad)
        self.num_6.grid(row=5, column=2, stick="wens", padx=self.pad, pady=self.pad)
        self.num_7.grid(row=6, column=0, stick="wens", padx=self.pad, pady=self.pad)
        self.num_8.grid(row=6, column=1, stick="wens", padx=self.pad, pady=self.pad)
        self.num_9.grid(row=6, column=2, stick="wens", padx=self.pad, pady=self.pad)
        self.num_0.grid(row=7, column=1, stick="wens", padx=self.pad, pady=self.pad)
        self.op_1.grid(row=3, column=3, stick="wens", padx=self.pad, pady=self.pad)
        self.op_2.grid(row=4, column=3, stick="wens", padx=self.pad, pady=self.pad)
        self.op_3.grid(row=5, column=3, stick="wens", padx=self.pad, pady=self.pad)
        self.op_4.grid(row=6, column=3, stick="wens", padx=self.pad, pady=self.pad)
        self.calc_btn.grid(row=7, column=3, stick="wens", padx=self.pad, pady=self.pad)
        self.clear_btn.grid(row=3, column=0, stick="wens", padx=self.pad, pady=self.pad)
        self.change_sign_btn.grid(row=7, column=0, stick="wens", padx=self.pad, pady=self.pad)
        self.percent_btn.grid(row=3, column=1, stick="wens", padx=self.pad, pady=self.pad)
        self.coma_btn.grid(row=7, column=2, stick="wens", padx=self.pad, pady=self.pad)
        self.backspace_btn.grid(row=3, column=2, stick="wens", padx=self.pad, pady=self.pad)
        self.close_menu_btn.grid_forget()

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)

        self.root.grid_rowconfigure(0)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2)
        self.root.grid_rowconfigure(3, weight=1)
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_rowconfigure(5, weight=1)
        self.root.grid_rowconfigure(6, weight=1)
        self.root.grid_rowconfigure(7, weight=1)

        # Over entry label
        self.over_entry_label = tk.Label()
        self.over_entry_label.grid(row=0, column=0, stick="wens", columnspan=4)

        self.more_btn = tk.Button(self.over_entry_label, text="Menu ≡", bd=self.bd, font=self.font, cursor=self.cursor, command=self.more)

        self.more_btn.pack(side=tk.LEFT)

        # Under entry label
        self.under_entry_label = tk.Label()
        self.under_entry_label.grid(row=2, column=0, stick="wens", columnspan=4)

        self.mp_btn = tk.Button(self.under_entry_label, text="m+", bd=self.bd, font=self.font_mini, cursor=self.cursor, command=lambda: self.m("+"))
        self.mm_btn = tk.Button(self.under_entry_label, text="m-", bd=self.bd, font=self.font_mini, cursor=self.cursor, command=lambda: self.m("-"))
        self.mc_btn = tk.Button(self.under_entry_label, text="mc", bd=self.bd, font=self.font_mini, cursor=self.cursor, command=lambda: self.m("c"))
        self.mr_btn = tk.Button(self.under_entry_label, text="mr", bd=self.bd, font=self.font_mini, cursor=self.cursor, command=lambda: self.m("r"))

        self.mc_btn.grid(row=0, column=0, stick="wens", padx=self.pad, pady=self.pad)
        self.mp_btn.grid(row=0, column=1, stick="wens", padx=self.pad, pady=self.pad)
        self.mm_btn.grid(row=0, column=2, stick="wens", padx=self.pad, pady=self.pad)
        self.mr_btn.grid(row=0, column=3, stick="wens", padx=self.pad, pady=self.pad)

        self.under_entry_label.grid_rowconfigure(0, weight=1)
        self.under_entry_label.grid_columnconfigure(0, weight=1)
        self.under_entry_label.grid_columnconfigure(1, weight=1)
        self.under_entry_label.grid_columnconfigure(2, weight=1)
        self.under_entry_label.grid_columnconfigure(3, weight=1)

        # Menu label
        self.more_active = False

        self.more_label = tk.Label()
        self.more_label.grid_forget()

        self.sett_btn = tk.Button(self.more_label, text="Settings ⚙", bd=0, font=self.font, cursor=self.cursor, command=self.settings)
        self.mode_btn = tk.Button(self.more_label, text="Mode: 1", bd=0, font=self.font)
        self.fullscreen_btn = tk.Button(self.more_label, text="Fullscreen: off", bd=0, font=self.font, cursor=self.cursor, command=lambda: self.fullscreen(None))
        self.info_btn = tk.Button(self.more_label, text="Info i", bd=0, cursor=self.cursor, font=self.font,
                                  command=lambda: messagebox.showinfo(title="Calc info", message=self.calc_info))
        self.exit_btn = tk.Button(self.more_label, text="Exit ⮾", bd=0, font=self.font, cursor=self.cursor, command=self.exit)

        self.sett_btn.grid(row=0, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
        self.mode_btn.grid(row=1, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
        self.fullscreen_btn.grid(row=2, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
        self.info_btn.grid(row=3, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
        self.exit_btn.grid(row=4, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)

        self.more_label.grid_columnconfigure(0, weight=1)

        self.more_label.grid_rowconfigure(0, weight=1)
        self.more_label.grid_rowconfigure(1, weight=1)
        self.more_label.grid_rowconfigure(2, weight=1)
        self.more_label.grid_rowconfigure(3, weight=1)
        self.more_label.grid_rowconfigure(4, weight=1)

        # Settings label
        self.sett_label = tk.Label()
        self.sett_label.grid_forget()

        self.theme_btn = tk.Button(self.sett_label, text="Theme: " + self.theme, bd=0, font=("Bold", 17), cursor="hand2", command=self.change_theme)

        self.theme_btn.grid(row=0, column=0, stick="wens", columnspan=4, padx=self.pad, pady=self.pad)

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
        self.entry.config(state=tk.NORMAL)
        value = self.entry.get()
        if self.equals:
            value = "0"
            self.equals = False
        if value[0] == "0" and len(value) == 1:
            value = value[1:]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, value + str(num))
        self.entry.config(state=tk.DISABLED)

    def add_operation(self, operation):
        self.entry.config(state=tk.NORMAL)
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        for i in range(len(value)):
            if value[-1] == "0" and "." in value:
                value = value[:-1]
            elif value[-1] == ".":
                value = value[:-1]
        if value[-1] in "+-*/":
            value = value[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(0, str(self.translate(value, -1) + operation))
        self.entry.config(state=tk.DISABLED)

    def calculate(self, eq=True):
        self.entry.config(state=tk.NORMAL)
        value = self.translate(self.entry.get(), 1)
        if value[-1] in "+-*/" and ((value.count("+") + value.count("-") + value.count("*") + value.count("/")) == 1):
            value = value + value[:-1]
        self.entry.delete(0, tk.END)
        try:
            self.entry.insert(0, self.translate(self.debug(eval(self.translate(value, 1))), -1))
            if eq:
                # if "+" not in value and "*" not in value and "/" not in value and ("-" not in value or str(value).find("-") == 0):
                #     pass
                # else:
                self.equals = True
        except ZeroDivisionError:
            self.entry.insert(0, "0")
            messagebox.showerror("Error", "Error: \n\nCan't divide by zero.")
        except SyntaxError:
            self.entry.insert(0, "0")
            messagebox.showerror("Error", "Syntax error: \n\nPlease check syntax.")
        self.entry.config(state=tk.DISABLED)

    def clear(self):
        self.entry.config(state=tk.NORMAL)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "0")
        self.entry.config(state=tk.DISABLED)

    def change_sign(self):
        self.entry.config(state=tk.NORMAL)
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        if "+" not in value and "*" not in value and "/" not in value and ("-" not in value or str(value).find("-") == 0):
            value = self.debug(float(value))
            value = value * -1
        elif value[-1] in "+-*/":
            pass
        else:
            number = list([])
            value_2 = str(value)
            for i in range(len(value_2)):
                if value_2[i * -1] in "+-*/":
                    break
                else:
                    number.insert(0, value_2[(i + 1) * -1])
            number.pop(0)
            number = self.debug(float("".join(number)))
            print(number)
            self.entry.delete(len(self.entry.get()) - len(str(number)), tk.END)
            value = str(self.entry.get()) + str(number * -1)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))
        self.entry.config(state=tk.DISABLED)

    def percent(self):
        self.entry.config(state=tk.NORMAL)
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        if "+" not in value and "-" not in value and "*" not in value and "/" not in value:
            if value != "0" and value != "0.":
                value = self.debug(float(value))
                value = value / 100
            elif value == "0" or value == "0.":
                value = "0.01"
        elif value[-1] in "+-*/":
            value = value + "0.01"
        else:
            number = self.debug(float(self.find_last_number()))
            self.entry.delete(len(self.entry.get()) - len(str(self.debug(number))), tk.END)
            value = str(self.entry.get()) + str(number / 100)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))
        self.entry.config(state=tk.DISABLED)

    def on_press(self, event):
        if not self.more_active:
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
                pass  # print(repr(event.char))
        elif self.more_active:
            if event.char == "\x1b" and self.more_active:
                self.more()
            else:
                pass

    def add_coma(self):
        self.entry.config(state=tk.NORMAL)
        value = self.translate(self.entry.get(), 1)
        self.equals = False
        if "+" not in value and "-" not in value and "*" not in value and "/" not in value:
            if "." in value:
                pass
            else:
                value += "."
        elif value[-1] in "+-*/":
            value += "0."
        else:
            number = str(self.find_last_number())
            if number.find(".") > 0:
                pass
            else:
                value += "."
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(value, -1))
        self.entry.config(state=tk.DISABLED)

    def backspace(self):
        self.entry.config(state=tk.NORMAL)
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
        self.entry.config(state=tk.DISABLED)

    def more(self):
        self.entry.config(state=tk.NORMAL)
        if self.more_active:
            self.more_label.grid_forget()
            self.sett_label.grid_forget()
            self.close_menu_btn.grid_forget()
            self.entry.config(cursor="hand2")
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.last_value)
            self.more_active = False
        elif not self.more_active:
            self.more_label.grid(row=1, column=0, rowspan=7, columnspan=4, stick="wens", padx=0, pady=0)
            self.entry.config(cursor="arrow")
            self.close_menu_btn.grid(row=0, column=0, stick="wens", padx=3, pady=3)
            self.last_value = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, "Menu")
            self.more_active = True
        self.entry.config(state=tk.DISABLED)

    def settings(self):
        self.entry.config(state=tk.NORMAL)
        self.more_label.grid_forget()
        self.sett_label.grid(row=1, column=0, rowspan=7, columnspan=4, stick="wens", padx=0, pady=0)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, "Settings")
        self.entry.config(state=tk.DISABLED)

    def on_scale(self):
        if self.win_size[0] != self.root.winfo_width() or self.win_size[1] != self.root.winfo_height():
            self.win_size = [self.root.winfo_width(), self.root.winfo_height()]

            # Font size
            if self.win_size[0] > 1000 and self.win_size[1] > 1000:
                self.font = ("Bold", 35)
                self.font_mini = ("Bold", 30)
                self.entry_font = ("Bold", 45)
                self.buttons_reload()
            elif self.win_size[0] > 700 and self.win_size[1] > 700:
                self.font = ("Bold", 30)
                self.font_mini = ("Bold", 25)
                self.entry_font = ("Bold", 40)
                self.buttons_reload()
            elif self.win_size[0] > 500 and self.win_size[1] > 500:
                self.font = ("Bold", 25)
                self.font_mini = ("Bold", 21)
                self.entry_font = ("Bold", 35)
                self.pad = 3
                self.buttons_reload()
            elif self.win_size[0] > 400 and self.win_size[1] > 400:
                self.font = ("Bold", 20)
                self.font_mini = ("Bold", 17)
                self.entry_font = ("Bold", 30)
                self.pad = 2
                self.buttons_reload()
            elif self.win_size[0] > 200 and self.win_size[1] > 300:
                self.font = ("Bold", 17)
                self.entry_font = ("Bold", 25)
                self.pad = 1
                self.buttons_reload()
            else:
                self.font = ("Bold", 14)
                self.font_mini = ("Bold", 10)
                self.entry_font = ("Bold", 20)
                self.buttons_reload()

            # Under entry label
            if self.win_size[0] > 1000:
                self.mc_btn.grid_forget()
                self.mp_btn.grid_forget()
                self.mm_btn.grid_forget()
                self.mr_btn.grid_forget()
                self.mc_btn.pack(side=tk.RIGHT, padx=3, pady=3)
                self.mp_btn.pack(side=tk.RIGHT, padx=3, pady=3)
                self.mm_btn.pack(side=tk.RIGHT, padx=3, pady=3)
                self.mr_btn.pack(side=tk.RIGHT, padx=3, pady=3)
            elif self.win_size[0] > 700:
                self.under_entry_label.grid(row=2, column=2, stick="wens", columnspan=2)
                self.mc_btn.pack_forget()
                self.mp_btn.pack_forget()
                self.mm_btn.pack_forget()
                self.mr_btn.pack_forget()
                self.mc_btn.grid(row=0, column=0, stick="wens", padx=3, pady=3)
                self.mp_btn.grid(row=0, column=1, stick="wens", padx=3, pady=3)
                self.mm_btn.grid(row=0, column=2, stick="wens", padx=3, pady=3)
                self.mr_btn.grid(row=0, column=3, stick="wens", padx=3, pady=3)
            else:
                self.under_entry_label.grid(row=2, column=0, stick="wens", columnspan=4)

        self.root.after(1, func=self.on_scale)

    def change_theme(self):
        if self.theme == "light":
            self.root.config(bg="#2A2A2A")
            self.entry.config(bg="#2A2A2A", fg="#ffffff", disabledbackground="#2A2A2A", disabledforeground="#ffffff")
            self.over_entry_label.config(bg="#2A2A2A")
            self.under_entry_label.config(bg="#2A2A2A")
            self.more_label.config(bg="#2A2A2A")
            self.sett_label.config(bg="#2A2A2A")
            self.theme = "dark"
            self.theme_btn.config(text="Theme: dark")
        elif self.theme == "dark":
            self.root.config(bg="#DDDDDD")
            self.entry.config(bg="#DDDDDD", fg="#000000", disabledbackground="#DDDDDD", disabledforeground="#000000")
            self.over_entry_label.config(bg="#DDDDDD")
            self.under_entry_label.config(bg="#DDDDDD")
            self.more_label.config(bg="#DDDDDD")
            self.sett_label.config(bg="#DDDDDD")
            self.theme = "light"
            self.theme_btn.config(text="Theme: light")
        self.button_colors_reload()
        self.more()

    def button_colors(self, button, btn_type):
        if self.theme == "light":
            if btn_type == "number":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#ffffff'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#ffffff")
            elif btn_type == "main_operation":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#EAEAEA'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#EAEAEA")
            elif btn_type == "operation":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#EAEAEA'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#EAEAEA")
            elif btn_type == "equals":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#EAEAEA'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#EAEAEA")
            elif btn_type == "invisible":
                button.bind("<Enter>", lambda e: button.config(bg='#CFCFCF'))
                button.bind("<Leave>", lambda e: button.config(bg='#DDDDDD'))
                button.config(activebackground="#BEBEBE", activeforeground="#000000", fg="#000000", bg="#DDDDDD")
            elif btn_type == "attention":
                button.bind("<Enter>", lambda e: button.config(bg='#F78181'))
                button.bind("<Leave>", lambda e: button.config(bg='#ffffff'))
                button.config(activebackground="#FA5858", activeforeground="#000000", fg="#000000", bg="#ffffff")
        elif self.theme == "dark":
            if btn_type == "number":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#000000'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#000000")
            elif btn_type == "main_operation":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#1A1A1A'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#1A1A1A")
            elif btn_type == "operation":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#1A1A1A'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#1A1A1A")
            elif btn_type == "equals":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#1A1A1A'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#1A1A1A")
            elif btn_type == "invisible":
                button.bind("<Enter>", lambda e: button.config(bg='#424242'))
                button.bind("<Leave>", lambda e: button.config(bg='#2A2A2A'))
                button.config(activebackground="#585858", activeforeground="#ffffff", fg="#ffffff", bg="#2A2A2A")
            elif btn_type == "attention":
                button.bind("<Enter>", lambda e: button.config(bg='#610B0B'))
                button.bind("<Leave>", lambda e: button.config(bg='#000000'))
                button.config(activebackground="#770000", activeforeground="#ffffff", fg="#ffffff", bg="#000000")

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
        self.button_colors(self.op_1, "main_operation")
        self.button_colors(self.op_2, "main_operation")
        self.button_colors(self.op_3, "main_operation")
        self.button_colors(self.op_4, "main_operation")
        self.button_colors(self.calc_btn, "equals")
        self.button_colors(self.clear_btn, "operation")
        self.button_colors(self.change_sign_btn, "operation")
        self.button_colors(self.percent_btn, "operation")
        self.button_colors(self.coma_btn, "operation")
        self.button_colors(self.backspace_btn, "operation")
        self.button_colors(self.close_menu_btn, "operation")
        self.button_colors(self.mp_btn, "invisible")
        self.button_colors(self.mm_btn, "invisible")
        self.button_colors(self.mc_btn, "invisible")
        self.button_colors(self.mr_btn, "invisible")
        self.button_colors(self.more_btn, "invisible")

        self.button_colors(self.sett_btn, "number")
        self.button_colors(self.fullscreen_btn, "number")
        self.button_colors(self.info_btn, "number")
        self.button_colors(self.exit_btn, "attention")

        self.button_colors(self.theme_btn, "number")

    def buttons_reload(self):
        self.entry.config(font=self.entry_font)

        self.num_1.config(font=self.font)
        self.num_2.config(font=self.font)
        self.num_3.config(font=self.font)
        self.num_4.config(font=self.font)
        self.num_5.config(font=self.font)
        self.num_6.config(font=self.font)
        self.num_7.config(font=self.font)
        self.num_8.config(font=self.font)
        self.num_9.config(font=self.font)
        self.num_0.config(font=self.font)
        self.op_1.config(font=self.font)
        self.op_2.config(font=self.font)
        self.op_3.config(font=self.font)
        self.op_4.config(font=self.font)
        self.calc_btn.config(font=self.font)
        self.clear_btn.config(font=self.font)
        self.change_sign_btn.config(font=self.font)
        self.percent_btn.config(font=self.font)
        self.coma_btn.config(font=self.font)
        self.backspace_btn.config(font=self.font)
        self.close_menu_btn.config(font=self.font)
        self.mp_btn.config(font=self.font_mini)
        self.mm_btn.config(font=self.font_mini)
        self.mc_btn.config(font=self.font_mini)
        self.mr_btn.config(font=self.font_mini)
        self.more_btn.config(font=self.font)

        self.sett_btn.config(font=self.font)
        self.fullscreen_btn.config(font=self.font)
        self.info_btn.config(font=self.font)
        self.exit_btn.config(font=self.font)
        self.theme_btn.config(font=self.font)

        self.theme_btn.config(font=self.font)

    def reload(self):
        self.button_colors_reload()
        self.buttons_reload()
        if self.theme == "dark":
            self.root.config(bg="#2A2A2A")
            self.entry.config(bg="#2A2A2A", fg="#ffffff", disabledbackground="#2A2A2A", disabledforeground="#ffffff")
            self.over_entry_label.config(bg="#2A2A2A")
            self.under_entry_label.config(bg="#2A2A2A")
            self.more_label.config(bg="#2A2A2A")
            self.sett_label.config(bg="#2A2A2A")
            self.theme = "dark"
        elif self.theme == "light":
            self.root.config(bg="#DDDDDD")
            self.entry.config(bg="#DDDDDD", fg="#000000", disabledbackground="#DDDDDD", disabledforeground="#000000")
            self.over_entry_label.config(bg="#DDDDDD")
            self.under_entry_label.config(bg="#DDDDDD")
            self.more_label.config(bg="#DDDDDD")
            self.sett_label.config(bg="#DDDDDD")
            self.theme = "light"
        self.theme_btn.config(text="Theme: " + self.theme)

    def fullscreen(self, event):
        if event is None:
            if self.fullscreen_value:
                self.fullscreen_value = False
                self.fullscreen_btn.config(text="Fullscreen: off")
            elif not self.fullscreen_value:
                self.fullscreen_value = True
                self.fullscreen_btn.config(text="Fullscreen: on")
            self.root.attributes("-fullscreen", self.fullscreen_value)
            if not self.fullscreen_value:
                sleep(1)
        else:
            if self.fullscreen_value:
                self.fullscreen_value = False
                self.fullscreen_btn.config(text="Fullscreen: off")
            elif not self.fullscreen_value:
                self.fullscreen_value = True
                self.fullscreen_btn.config(text="Fullscreen: on")
            self.root.attributes("-fullscreen", self.fullscreen_value)
            if not self.fullscreen_value:
                sleep(1)

    def copy_entry_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(str(self.entry.get()))

    def find_last_number(self):
        self.entry.config(state=tk.NORMAL)
        value = self.translate(self.entry.get(), 1)
        number = list([])
        value_2 = str(value)
        for i in range(len(value_2)):
            if value_2[i * -1] in "+-*/":
                break
            else:
                number.insert(0, value_2[(i + 1) * -1])
        number.pop(0)
        number = "".join(number)
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.translate(str(value), -1))
        # self.entry.config(state=tk.DISABLED)
        print(number)
        if number == "":
            return None
        else:
            return str(number)

    def m(self, parameter):
        if parameter == "+":
            self.memory += float(self.entry.get())
            print(float(self.entry.get()))
            print(self.memory)
        elif parameter == "-":
            self.memory -= float(self.entry.get())
            print(float(self.entry.get()))
            print(self.memory)
        elif parameter == "c":
            self.memory = 0
            print(self.memory)
        elif parameter == "r":
            print(self.memory)

    @staticmethod
    def exit():
        sys.exit()

    @staticmethod
    def translate(text, value):
        text = str(text)
        if value > 0:
            text = str(text).replace("×", "*").replace("÷", "/").replace("^", "**").replace(",", ".").replace(" ", "")
        elif value < 0:
            text = str(text).replace("*", "×").replace("/", "÷").replace("**", "^").replace(".", ",")
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
