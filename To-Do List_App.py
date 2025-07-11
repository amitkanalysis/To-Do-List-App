import tkinter as tk
import pandas as pd
import os
from tkinter import messagebox, font

root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")
root.configure(bg='#f0f4f7')

tasks = []


def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)


def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")


def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
    except IndexError:
        messagebox.showwarning(
            "Selection Error", "Please select a task to delete")


def download_tasks():
    if tasks:
        df = pd.DataFrame(tasks, columns=['Tasks'])
        df.to_csv('tasks.csv', index=False)
        messagebox.showinfo("Download Successfull",
                            "Tasks have been downlaoded Successfully!")
    else:
        messagebox.showwaring("Download Error", "No Tasks to download")


title_font = font.Font(family='Helvetica', size=16, weight='bold')
button_font = font.Font(family='Helvetica', size=10)


title = tk.Label(root, text="My To-Do List",
                 font=title_font, bg="#f0f4f7", fg="#333")
title.pack(pady=10)


frame = tk.Frame(root, bg="#f0f4f7")
frame.pack(pady=10)

entry = tk.Entry(frame, width=25, font=("Helvetica", 12))
entry.grid(row=0, column=0, padx=5)


add_btn = tk.Button(frame, text="Add", font=button_font,
                    bg="#4CAF50", fg="white", width=8, command=add_task)
add_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(root, text="Delete Selected", font=button_font,
                       bg="#f44336", fg="white", width=20, command=delete_task)
delete_btn.pack(pady=10)

download_btn = tk.Button(root, text='Download Tasks', font=button_font,
                         bg='#2196F3', fg='white', width=20, command=download_tasks)
download_btn.pack(pady=10)

listbox = tk.Listbox(root, width=40, height=15, font=(
    "Helvetica", 12), bd=0, highlightthickness=0, selectbackground="#a6a6a6")
listbox.pack(pady=10)


def download_tasks_csv(event: object = None):
    download_path = os.path.join(os.path.expanduser("~"), "Downloads")
    file_path = os.path.join(download_path, 'tasks.csv')
    with open(file_path, "w") as file:
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Download Successful", f"Tasks saved to {file_path}")


download_btn.bind("<Return>", download_tasks_csv)

download_btn.focus_set()

root.mainloop()
