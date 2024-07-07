import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tkinter import ttk

def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        animate_task_addition(task_listbox.size() - 1)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

def animate_task_addition(index):
    alpha = 0
    task_listbox.itemconfig(index, foreground=f"#{int(255*alpha):02x}{int(255*alpha):02x}{int(255*alpha):02x}")
    increment = 0.1

    def fade_in():
        nonlocal alpha
        alpha += increment
        if alpha <= 1:
            color = f"#{int(255*alpha):02x}{int(255*alpha):02x}{int(255*alpha):02x}"
            task_listbox.itemconfig(index, foreground=color)
            root.after(50, fade_in)
        else:
            task_listbox.itemconfig(index, foreground="black")

    fade_in()

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

def clear_tasks():
    task_listbox.delete(0, tk.END)

def save_tasks():
    tasks = task_listbox.get(0, tk.END)
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

def on_enter(e):
    e.widget['background'] = 'blue'

def on_leave(e):
    e.widget['background'] = 'SystemButtonFace'

root = ThemedTk(theme="equilux")
root.title("To-Do List")
root.geometry("400x400")

frame = ttk.Frame(root)
frame.pack(pady=10)

task_listbox = tk.Listbox(root, height=15, width=50, bd=0, selectbackground="#a6a6a6", activestyle="none")
task_listbox.pack(pady=10)

scrollbar = ttk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

task_entry = ttk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

add_button = ttk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

remove_button = ttk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack(pady=10)
remove_button.bind("<Enter>", on_enter)
remove_button.bind("<Leave>", on_leave)

clear_button = ttk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_button.pack(pady=10)
clear_button.bind("<Enter>", on_enter)
clear_button.bind("<Leave>", on_leave)

save_button = ttk.Button(root, text="Save Tasks", command=save_tasks)
save_button.pack(pady=10)
save_button.bind("<Enter>", on_enter)
save_button.bind("<Leave>", on_leave)

load_button = ttk.Button(root, text="Load Tasks", command=load_tasks)
load_button.pack(pady=10)
load_button.bind("<Enter>", on_enter)
load_button.bind("<Leave>", on_leave)

load_tasks()

root.mainloop()
