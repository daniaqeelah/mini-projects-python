from tkinter import *
from tkinter import filedialog

tasks = []

# Add a new task
def add_task():
    task_text = entry.get().strip()
    if task_text:
        var = BooleanVar()
        cb = Checkbutton(task_frame, text=task_text, variable=var, font=("Helvetica", 12),
                         bg="mistyrose", anchor="w", width=30, selectcolor="lightpink")
        cb.var = var
        cb.pack(anchor="w", padx=10, pady=3)
        tasks.append(cb)
        entry.delete(0, END)

# Delete selected (checked) tasks
def delete_selected():
    for task in tasks[:]:
        if task.var.get():
            task.destroy()
            tasks.remove(task)

# Save tasks to a .txt file
def save_tasks():
    if not tasks:
        return

    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")],
        title="Save Your Task List",
        initialfile="my_todo_list"
    )

    if file:
        with open(file, "w", encoding="utf-8") as f:
            for task in tasks:
                f.write(task.cget("text") + "\n")

# GUI setup
root = Tk()
root.title("🌸 Dania's To-Do List 🌸")
root.geometry("400x520")
root.config(bg="#ffeef2")

entry = Entry(root, font=("Helvetica", 14), width=25, bg="#ffe0ec", fg="#333")
entry.pack(pady=15)

# Buttons: Add, Delete, Save
btn_frame = Frame(root, bg="#ffeef2")
btn_frame.pack()

Button(btn_frame, text="Add Task", command=add_task, font=("Helvetica", 11),
       bg="#cce7ff", fg="#333", activebackground="#aadfff").pack(side=LEFT, padx=5)

Button(btn_frame, text="Delete Selected", command=delete_selected, font=("Helvetica", 11),
       bg="#ffb3c6", fg="#333", activebackground="#ff9eb3").pack(side=LEFT, padx=5)

Button(btn_frame, text="Save to File", command=save_tasks, font=("Helvetica", 11),
       bg="#d2ffe5", fg="#333", activebackground="#baffd5").pack(side=LEFT, padx=5)

# Task display area
task_frame = Frame(root, bg="#fff0f5", bd=2, relief=RIDGE)
task_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

root.mainloop()
