import tkinter as tk
from tkinter import messagebox

def default(event, entry):
    if entry.get() == "Enter your task here":
        entry.delete(0, "end")
        entry.config(fg="black")

def event(event, entry):
    if entry.get() == "":
        entry.insert(0, "Enter your task here")
        entry.config(fg="grey")

def add_task():
    task = add_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        add_entry.delete(0, tk.END)
        add_window.destroy()

def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
        remove_window.destroy()
    else:
        messagebox.showerror("Error", "Select the task you want to remove.")

def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        updated_task = update_entry.get()
        task_listbox.delete(selected_task_index)
        task_listbox.insert(selected_task_index, updated_task)
        update_window.destroy()
    else:
        messagebox.showerror("Error", "Select a task to update.")

def open_add_window():
    global add_window
    add_window = tk.Toplevel(root)
    add_window.title("Add Task")

    global add_entry
    add_entry = tk.Entry(add_window, fg="grey", width=30)
    add_entry.insert(0, "Enter your task here")
    add_entry.bind('<FocusIn>', lambda event: default(event, add_entry))
    add_entry.bind('<FocusOut>', lambda event: event(event, add_entry))
    add_entry.pack(pady=10)

    add_button = tk.Button(add_window, text="Add Task", command=add_task, bg="green", fg="white")
    add_button.pack(side="left", padx=5, pady=5)

def open_remove_window():
    global remove_window
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Task")

    remove_button = tk.Button(remove_window, text="Remove Task", command=remove_task, bg="red", fg="white")
    remove_button.pack(side="left", padx=5, pady=5)

def open_update_window():
    global update_window
    update_window = tk.Toplevel(root)
    update_window.title("Update Task")

    global update_entry
    selected_task_index = task_listbox.curselection()
    update_entry = tk.Entry(update_window, fg="grey", width=30)
    update_entry.insert(0, task_listbox.get(selected_task_index))
    update_entry.pack(pady=10)

    update_button = tk.Button(update_window, text="Update Task", command=update_task, bg="blue", fg="white")
    update_button.pack(side="left", padx=5, pady=5)

# Create the main application window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x300")  # Set initial window size

# Create and configure the task listbox widget
task_listbox = tk.Listbox(root, width=30)
task_listbox.insert(0, "The to-do list:")
task_listbox.pack(pady=20, padx=20)

# Create and configure buttons to open different windows
add_button = tk.Button(root, text="Add Task", command=open_add_window, bg="green", fg="white")
add_button.pack(side="left", padx=10, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=open_remove_window, bg="red", fg="white")
remove_button.pack(side="left", padx=10, pady=10)

update_button = tk.Button(root, text="Update Task", command=open_update_window, bg="blue", fg="white")
update_button.pack(side="left", padx=10, pady=10)

# Main loop
root.mainloop()