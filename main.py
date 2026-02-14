# First 500 strings: 20.12.2021

import tkinter as tk
import math
from tkinter import messagebox


class Main:
	class Button:
		@staticmethod
		def button(self, text: str, function):
			return tk.Button(text=text, bd=self.bd, font=self.font,
							 cursor=self.cursor, command=function)

		@staticmethod
		def number_button(self, num: int):
			return tk.Button(text=str(num), bd=self.bd, font=self.font,
							 cursor=self.cursor, command=lambda: self.add_number(num))

		@staticmethod
		def operation_button(self, operation: str):
			return tk.Button(text=operation, bd=self.bd, font=self.font,
							 cursor=self.cursor, command=lambda: self.add_operation(operation))

	def __init__(self):
		self.root = tk.Tk()
		self.fullscreen_value = False
		self.info = "Version: 1.5\nBy: Vladimir Polischuk\nRelease date: \n\nWhat's new: "
		self.entry_font = ("Bold", 30)
		self.font = ("Bold", 20)
		self.font_mini = ("Arial", 17)
		self.cursor = "hand2"
		self.bd = 0
		self.pad = 3
		self.theme = "light"
		self.minsize = [200, 350]

		self.root.geometry("300x400")
		self.root.minsize(self.minsize[0], self.minsize[1])
		self.root.update()
		self.root["bg"] = "#ffffff"
		self.root.title("Calculator")
		self.root.attributes('-alpha', 0.97)

		self.root.attributes('-fullscreen', self.fullscreen_value)
		self.win_size = [self.root.winfo_width(), self.root.winfo_height()]
		self.on_scale()

		self.root.bind("<Key>", self.on_press)
		self.root.bind("<F11>", self.fullscreen)

		self.entry = tk.Entry(self.root, justify=tk.RIGHT, bd=0, font=self.entry_font, cursor="hand2")
		self.entry.insert(0, "0")
		self.entry.config(state=tk.DISABLED)
		self.entry.grid(row=2, column=0, columnspan=4, stick="wens")
		self.last_value = "0"
		self.memory = 0

		self.entry_2 = tk.Entry(self.root, justify=tk.RIGHT, bd=0, font=self.font_mini, cursor="hand2")
		self.entry_2.grid(row=1, column=0, columnspan=4, stick="wens")
		self.last_value_2 = ""

		self.menu = tk.Menu(self.root, tearoff=0)
		self.menu.add_command(label="Copy text", command=self.copy_entry_text)
		self.entry.bind("<Button-3>", self.show_menu)
		self.entry_2.bind("<Button-3>", self.show_menu)

		self.new_enter = False
		self.equals = False

		self.num_0, self.num_1, self.num_2, self.num_3, self.num_4, \
		self.num_5, self.num_6, self.num_7, self.num_8, self.num_9 = \
			(self.Button.number_button(self, i) for i in range(10))

		self.op_1, self.op_2, self.op_3, self.op_4 = \
			(self.Button.operation_button(self, op) for op in ("+", "-", "×", "÷"))

		self.calc_btn = self.Button.button(self, "=", self.calculate)
		self.clear_btn = self.Button.button(self, "C", self.clear_all)
		self.change_sign_btn = self.Button.button(self, "±", self.change_sign)
		self.percent_btn = self.Button.button(self, "%", self.percent)
		self.coma_btn = self.Button.button(self, ",", self.add_coma)
		self.backspace_btn = self.Button.button(self, "←", self.backspace)
		self.close_menu_btn = self.Button.button(self, "<", self.more)

		self.num_1.grid(row=5, column=0, stick="wens", padx=self.pad, pady=self.pad)
		self.num_2.grid(row=5, column=1, stick="wens", padx=self.pad, pady=self.pad)
		self.num_3.grid(row=5, column=2, stick="wens", padx=self.pad, pady=self.pad)
		self.num_4.grid(row=6, column=0, stick="wens", padx=self.pad, pady=self.pad)
		self.num_5.grid(row=6, column=1, stick="wens", padx=self.pad, pady=self.pad)
		self.num_6.grid(row=6, column=2, stick="wens", padx=self.pad, pady=self.pad)
		self.num_7.grid(row=7, column=0, stick="wens", padx=self.pad, pady=self.pad)
		self.num_8.grid(row=7, column=1, stick="wens", padx=self.pad, pady=self.pad)
		self.num_9.grid(row=7, column=2, stick="wens", padx=self.pad, pady=self.pad)
		self.num_0.grid(row=8, column=1, stick="wens", padx=self.pad, pady=self.pad)
		self.op_1.grid(row=4, column=3, stick="wens", padx=self.pad, pady=self.pad)
		self.op_2.grid(row=5, column=3, stick="wens", padx=self.pad, pady=self.pad)
		self.op_3.grid(row=6, column=3, stick="wens", padx=self.pad, pady=self.pad)
		self.op_4.grid(row=7, column=3, stick="wens", padx=self.pad, pady=self.pad)
		self.calc_btn.grid(row=8, column=3, stick="wens", padx=self.pad, pady=self.pad)
		self.clear_btn.grid(row=4, column=0, stick="wens", padx=self.pad, pady=self.pad)
		self.change_sign_btn.grid(row=8, column=0, stick="wens", padx=self.pad, pady=self.pad)
		self.percent_btn.grid(row=4, column=1, stick="wens", padx=self.pad, pady=self.pad)
		self.coma_btn.grid(row=8, column=2, stick="wens", padx=self.pad, pady=self.pad)
		self.backspace_btn.grid(row=4, column=2, stick="wens", padx=self.pad, pady=self.pad)
		self.close_menu_btn.grid_forget()

		for i in range(4):
			self.root.grid_columnconfigure(i, weight=1)

		self.root.grid_rowconfigure(0)
		self.root.grid_rowconfigure(1, weight=1)
		self.root.grid_rowconfigure(2, weight=1)
		self.root.grid_rowconfigure(3)
		for i in range(4, 9):
			self.root.grid_rowconfigure(i, weight=1)

		# Over entry label
		self.over_entry_label = tk.Label()
		self.over_entry_label.grid(row=0, column=0, stick="wens", columnspan=4)

		self.more_btn = tk.Button(self.over_entry_label, text="Menu ≡", bd=self.bd, font=self.font, cursor=self.cursor, command=self.more)

		self.more_btn.pack(side=tk.LEFT)

		# Under entry label
		self.under_entry_label = tk.Label()
		self.under_entry_label.grid(row=3, column=0, stick="wens", columnspan=4)

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
		self.help_btn = tk.Button(self.more_label, text="Help", bd=0, font=self.font)
		self.fullscreen_btn = tk.Button(self.more_label, text="Fullscreen: off", bd=0, font=self.font, cursor=self.cursor, command=lambda: self.fullscreen(None))
		self.info_btn = tk.Button(self.more_label, text="Info i", bd=0, cursor=self.cursor, font=self.font,
								  command=lambda: messagebox.showinfo(title="Calc info", message=self.info))
		self.exit_btn = tk.Button(self.more_label, text="Exit ⮾", bd=0, font=self.font, cursor=self.cursor, command=self.exit)

		self.sett_btn.grid(row=0, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
		self.mode_btn.grid(row=1, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
		self.help_btn.grid(row=2, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
		self.fullscreen_btn.grid(row=3, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
		self.info_btn.grid(row=4, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)
		self.exit_btn.grid(row=5, column=0, columnspan=4, stick="wens", padx=self.pad, pady=self.pad)

		self.more_label.grid_columnconfigure(0, weight=1)

		self.more_label.grid_rowconfigure(0, weight=1)
		self.more_label.grid_rowconfigure(1, weight=1)
		self.more_label.grid_rowconfigure(2, weight=1)
		self.more_label.grid_rowconfigure(3, weight=1)
		self.more_label.grid_rowconfigure(4, weight=1)
		self.more_label.grid_rowconfigure(5, weight=1)

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

	# Count functions
	def add_number(self, num):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.entry.get()
		if self.equals:
			self.entry_2.delete(0, tk.END)
			value = "0"
			self.equals = False
		elif self.new_enter:
			value = "0"
			self.new_enter = False
		if value[0] == "0" and len(value) == 1:
			value = value[1:]
		if value == "-0":
			value = value[:-1]
		self.entry.delete(0, tk.END)
		self.entry.insert(0, value + str(num))
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def add_operation(self, operation):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		if self.equals:
			self.entry_2.delete(0, tk.END)
			self.equals = False
		value = self.translate(self.entry.get(), 1)
		value_2 = self.entry_2.get()
		add = True
		for i in range(len(value)):
			if value[-1] == "0" and "." in value or value[-1] == ".":
				value = value[:-1]
		if str(value) == "-0":
			value = "0"
		if len(value_2) > 3 and value_2[-2] in "+-×÷" and self.new_enter:
			value_2 = value_2[:-3]
			self.entry_2.delete(0, tk.END)
			self.entry_2.insert(0, str(value_2) + " " + operation + " ")
			add = False
		if add:
			self.entry.delete(0, tk.END)
			self.entry.insert(0, str(self.translate(value, -1)))
			if value[0] == "-" and len(value_2) != 0:
				self.entry_2.delete(0, tk.END)
				self.entry_2.insert(0, self.translate(value_2, -1) + "(" + str(self.translate(value, -1)) + ") " + operation + " ")
			else:
				self.entry_2.delete(0, tk.END)
				self.entry_2.insert(0, self.translate(value_2, -1) + str(self.translate(value, -1)) + " " + operation + " ")
		self.new_enter = True
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def calculate(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.translate(self.entry.get(), 1)
		value_2 = self.entry_2.get()
		do = True
		if self.equals:
			do = False
		elif self.new_enter:
			pass
		if do:
			for i in range(len(value)):
				if value[-1] == "0" and "." in value or value[-1] == ".":
					value = value[:-1]
			if str(value) == "-0":
				value = "0"
			if value[0] == "-" and len(value_2) != 0:
				value = value_2 + "(" + self.translate(value, -1) + ")"
			else:
				value = value_2 + self.translate(value, -1)
			self.entry_2.delete(0, tk.END)
			self.entry_2.insert(0, value + " =")
			self.entry.delete(0, tk.END)
			try:
				self.entry.insert(0, self.translate(self.debug(eval(self.translate(value, 1))), -1))
				self.equals = True
			except ZeroDivisionError:
				self.clear_all()
				messagebox.showerror("Error", "Error: \n\nCan't divide by zero.")
			except SyntaxError:
				self.clear_all()
				messagebox.showerror("Error", "Syntax error: \n\nPlease check syntax.")
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def ce(self):
		self.entry.config(state=tk.NORMAL)
		self.entry.delete(0, tk.END)
		self.entry.insert(0, "0")
		self.entry.config(state=tk.DISABLED)

	def clear_all(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		self.entry.delete(0, tk.END)
		self.entry_2.delete(0, tk.END)
		self.entry.insert(0, "0")
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def change_sign(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.debug(self.translate(self.entry.get(), 1))
		if self.equals:
			self.entry_2.delete(0, tk.END)
			self.equals = False
		elif self.new_enter:
			self.new_enter = False
		if str(self.entry.get()) == "-0":
			value = "0"
		elif value == 0 or value == 0.:
			value = "-" + str(value)
		else:
			value *= -1
		self.entry.delete(0, tk.END)
		self.entry.insert(0, self.translate(value, -1))
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def percent(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.debug(self.translate(self.entry.get(), 1))
		if self.equals:
			self.entry_2.delete(0, tk.END)
			self.equals = False
		elif self.new_enter:
			self.new_enter = False
		if value == 0:
			pass
		else:
			value /= 100
		self.entry.delete(0, tk.END)
		self.entry.insert(0, self.translate(value, -1))
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def on_press(self, event):
		if not self.more_active:
			if event.char.isdigit():
				self.add_number(event.char)
			elif event.char == "+" or event.char == "-" or event.char == "*" or event.char == "/":
				self.add_operation(self.translate(event.char, -1))
			elif event.char == "\r" or event.char == "=":
				self.calculate()
			elif event.char == "%":
				self.percent()
			elif event.char == "." or event.char == ",":
				self.add_coma()
			elif event.char == "\x08":
				self.backspace()
			elif event.char == "\x7f":
				self.clear_all()
			elif event.char == "\x03":
				self.copy_entry_text()
			else:
				pass  # print(repr(event.char))
		elif self.more_active:
			if event.char == "\x1b" and self.more_active:
				self.more()
			else:
				pass

	def add_coma(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.translate(self.entry.get(), 1)
		if self.equals:
			self.entry_2.delete(0, tk.END)
			self.equals = False
		elif self.new_enter:
			self.new_enter = False
		if "." not in value:
			value += "."
		self.entry.delete(0, tk.END)
		self.entry.insert(0, self.translate(value, -1))
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def backspace(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.translate(self.entry.get(), 1)
		if self.equals:
			self.entry_2.delete(0, tk.END)
			self.equals = False
		elif self.new_enter:
			self.new_enter = False
		if value == "0":
			pass
		elif len(value) == 2 and value[0] == "-":
			value = "-0"
		elif len(value) == 1 and value != "-":
			value = "0"
		else:
			value = value[:-1]
		self.entry.delete(0, tk.END)
		self.entry.insert(0, self.translate(value, -1))
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	# System functions
	def more(self):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		if self.more_active:
			self.more_label.grid_forget()
			self.sett_label.grid_forget()
			self.close_menu_btn.grid_forget()
			self.entry.config(cursor="hand2")
			self.entry.delete(0, tk.END)
			self.entry.insert(0, self.last_value)
			self.entry_2.insert(0, self.last_value_2)
			self.more_active = False
		elif not self.more_active:
			self.more_label.grid(row=2, column=0, rowspan=7, columnspan=4, stick="wens", padx=0, pady=0)
			self.entry.config(cursor="arrow")
			self.close_menu_btn.grid(row=0, column=0, stick="wens", padx=3, pady=3)
			self.last_value = self.entry.get()
			self.last_value_2 = self.entry_2.get()
			self.entry.delete(0, tk.END)
			self.entry_2.delete(0, tk.END)
			self.entry.insert(0, "Menu")
			self.more_active = True
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def settings(self):
		self.entry.config(state=tk.NORMAL)
		self.more_label.grid_forget()
		self.sett_label.grid(row=1, column=0, rowspan=8, columnspan=4, stick="wens", padx=0, pady=0)
		self.entry.delete(0, tk.END)
		self.entry.insert(0, "Settings")
		self.entry.config(state=tk.DISABLED)

	def on_scale(self):
		if self.win_size[0] != self.root.winfo_width() or self.win_size[1] != self.root.winfo_height():
			self.win_size = [self.root.winfo_width(), self.root.winfo_height()]

			# Font size and image size
			if self.win_size[0] > 1000 / 2 and self.win_size[1] > 1000:
				self.font = ("Bold", 35)
				self.font_mini = ("Bold", 30)
				self.entry_font = ("Bold", 45)
				self.buttons_reload()
			elif self.win_size[0] > 700 / 2 and self.win_size[1] > 700:
				self.font = ("Bold", 30)
				self.font_mini = ("Bold", 25)
				self.entry_font = ("Bold", 40)
				self.buttons_reload()
			elif self.win_size[0] > 500 / 2 and self.win_size[1] > 500:
				self.font = ("Bold", 25)
				self.font_mini = ("Bold", 21)
				self.entry_font = ("Bold", 35)
				self.pad = 3
				self.buttons_reload()
			elif self.win_size[0] >= 300 and self.win_size[1] >= 400:
				self.font = ("Bold", 20)
				self.font_mini = ("Bold", 17)
				self.entry_font = ("Bold", 30)
				self.pad = 2
				self.buttons_reload()
			elif self.win_size[0] > 200 / 2 and self.win_size[1] > 300:
				self.font = ("Bold", 17)
				self.font_mini = ("Bold", 14)
				self.entry_font = ("Bold", 25)
				self.pad = 1
				self.buttons_reload()
			else:
				self.font = ("Bold", 16)
				self.font_mini = ("Bold", 13)
				self.entry_font = ("Bold", 20)
				self.buttons_reload()

			# Under entry label
			if self.win_size[0] > 1000:
				self.mc_btn.grid_forget()
				self.mp_btn.grid_forget()
				self.mm_btn.grid_forget()
				self.mr_btn.grid_forget()
				self.mc_btn.config()
				self.mp_btn.config()
				self.mm_btn.config()
				self.mr_btn.config()
				self.mc_btn.pack(side=tk.RIGHT, padx=3, pady=3)
				self.mp_btn.pack(side=tk.RIGHT, padx=3, pady=3)
				self.mm_btn.pack(side=tk.RIGHT, padx=3, pady=3)
				self.mr_btn.pack(side=tk.RIGHT, padx=3, pady=3)
			elif self.win_size[0] > 700:
				self.under_entry_label.grid(row=3, column=2, stick="wens", columnspan=2)
				self.mc_btn.pack_forget()
				self.mp_btn.pack_forget()
				self.mm_btn.pack_forget()
				self.mr_btn.pack_forget()
				self.mc_btn.grid(row=0, column=0, stick="wens", padx=3, pady=3)
				self.mp_btn.grid(row=0, column=1, stick="wens", padx=3, pady=3)
				self.mm_btn.grid(row=0, column=2, stick="wens", padx=3, pady=3)
				self.mr_btn.grid(row=0, column=3, stick="wens", padx=3, pady=3)
			else:
				self.under_entry_label.grid(row=3, column=0, stick="wens", columnspan=4)

		self.root.after(1, func=self.on_scale)

	def change_theme(self):
		if self.theme == "light":
			self.root.config(bg="#2A2A2A")
			self.entry.config(bg="#2A2A2A", fg="#ffffff", disabledbackground="#2A2A2A", disabledforeground="#ffffff")
			self.entry_2.config(bg="#2A2A2A", fg="#DADADA", disabledbackground="#2A2A2A", disabledforeground="#DADADA")
			self.over_entry_label.config(bg="#2A2A2A")
			self.under_entry_label.config(bg="#2A2A2A")
			self.more_label.config(bg="#2A2A2A")
			self.sett_label.config(bg="#2A2A2A")
			self.theme = "dark"
			self.theme_btn.config(text="Theme: dark")
		elif self.theme == "dark":
			self.root.config(bg="#DDDDDD")
			self.entry.config(bg="#DDDDDD", fg="#000000", disabledbackground="#DDDDDD", disabledforeground="#000000")
			self.entry_2.config(bg="#DDDDDD", fg="#3C3D3C", disabledbackground="#DDDDDD", disabledforeground="#3C3D3C")
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
		self.entry_2.config(font=self.font_mini)

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
			self.entry_2.config(bg="#2A2A2A", fg="gray", disabledbackground="#2A2A2A", disabledforeground="gray")
			self.over_entry_label.config(bg="#2A2A2A")
			self.under_entry_label.config(bg="#2A2A2A")
			self.more_label.config(bg="#2A2A2A")
			self.sett_label.config(bg="#2A2A2A")
		elif self.theme == "light":
			self.root.config(bg="#DDDDDD")
			self.entry.config(bg="#DDDDDD", fg="#000000", disabledbackground="#DDDDDD", disabledforeground="#000000")
			self.entry_2.config(bg="#DDDDDD", fg="gray", disabledbackground="#DDDDDD", disabledforeground="#494949")
			self.over_entry_label.config(bg="#DDDDDD")
			self.under_entry_label.config(bg="#DDDDDD")
			self.more_label.config(bg="#DDDDDD")
			self.sett_label.config(bg="#DDDDDD")
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
		else:
			if self.fullscreen_value:
				self.fullscreen_value = False
				self.fullscreen_btn.config(text="Fullscreen: off")
			elif not self.fullscreen_value:
				self.fullscreen_value = True
				self.fullscreen_btn.config(text="Fullscreen: on")
			self.root.attributes("-fullscreen", self.fullscreen_value)

	def copy_entry_text(self):
		self.root.clipboard_clear()
		self.root.clipboard_append(str(self.entry_2.get()) + " " + str(self.entry.get()))

	def m(self, parameter):
		self.entry.config(state=tk.NORMAL)
		self.entry_2.config(state=tk.NORMAL)
		value = self.debug(self.entry.get())
		if parameter == "+":
			self.memory += value
		elif parameter == "-":
			self.memory -= value
		elif parameter == "c":
			self.memory = 0
		elif parameter == "r":
			self.entry.delete(0, tk.END)
			self.entry.insert(0, self.translate(self.memory, -1))
		self.entry.config(state=tk.DISABLED)
		self.entry_2.config(state=tk.DISABLED)

	def show_menu(self, e):
		self.menu.post(e.x_root, e.y_root)

	def img_resize(self, size):
		pass
		# self.backspace_image = self.backspace_image.subsample(size, size)
		# self.backspace_btn.config(image=self.backspace_image)

	@staticmethod
	def exit():
		exit(0)

	@staticmethod
	def translate(text, value):
		text = str(text)
		if value > 0:
			text = str(text).replace("×", "*").replace("÷", "/").replace("^", "**").replace(",", ".").replace(" ", "")
		elif value < 0:
			text = str(text).replace("*", "×").replace("/", "÷").replace("**", "^").replace(".", ",")
		return str(text)

	def debug(self, value):
		value = float(self.translate(value, 1))
		if math.modf(value)[0] == 0:
			value = int(value)
		elif math.modf(value)[0] != 0:
			value = float(value)
		return value


# Starting
if __name__ == "__main__":
	Main()
