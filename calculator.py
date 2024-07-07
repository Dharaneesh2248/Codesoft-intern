import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk
def button_click(value):
    current_text = display.get()
    new_text = current_text + str(value)
    display.set(new_text)
def evaluate_expression():
    try:
        result = eval(display.get())
        display.set(result)
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        display.set("")
def clear_display():
    display.set("")
root = ThemedTk(theme="arc")
root.title("Calculator")
display = tk.StringVar()
entry = ttk.Entry(root, textvariable=display, font=("Arial", 24), justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '+', '=', '.'
]
row = 1
col = 0
for button in buttons:
    if button == "=":
        ttk.Button(root, text=button, command=evaluate_expression).grid(row=row, column=col, columnspan=2, sticky="nsew")
        col += 1
    else:
        ttk.Button(root, text=button, command=lambda value=button: button_click(value)).grid(row=row, column=col, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1
ttk.Button(root, text="C", command=clear_display).grid(row=row, column=0, columnspan=4, sticky="nsew")
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
root.mainloop()
