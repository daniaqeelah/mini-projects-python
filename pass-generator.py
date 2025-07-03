import random
import string
import ttkbootstrap as tb
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Oops!", "Password should be at least 4 characters.")
            return

        chars = string.ascii_lowercase
        if upper_var.get():
            chars += string.ascii_uppercase
        if number_var.get():
            chars += string.digits
        if symbol_var.get():
            chars += string.punctuation

        if not chars:
            messagebox.showwarning("No character set", "Please select at least one character type.")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        password_entry.delete(0, "end")
        password_entry.insert(0, password)

        app.clipboard_clear()
        app.clipboard_append(password)
        status_label.config(text="🎉 Password copied to clipboard!", bootstyle="success")
    except ValueError:
        messagebox.showerror("Error", "Length must be a number.")

# App UI
app = tb.Window(themename="minty")
app.title("🌸 Password Generator")
app.geometry("450x400")
app.resizable(False, False)
app.configure(background="#ffe6f0")  # soft pink

# Label with background
tb.Label(app, text="Choose your password style 💖", font=("Comic Sans MS", 14), background="#ffe6f0").pack(pady=10)

# Frame with background
frame = tb.Frame(app)
frame.pack(pady=5)
frame.configure(style="TFrame")  # default style works with background

tb.Label(frame, text="Password Length:", background="#ffe6f0").grid(row=0, column=0, padx=5, pady=5)
length_entry = tb.Entry(frame, width=5)
length_entry.grid(row=0, column=1)
length_entry.insert(0, "12")

upper_var = tb.BooleanVar(value=True)
number_var = tb.BooleanVar(value=True)
symbol_var = tb.BooleanVar(value=True)

# Checkbox labels automatically pick up background from the theme, so no need to override
tb.Checkbutton(app, text="Include Uppercase", variable=upper_var).pack()
tb.Checkbutton(app, text="Include Numbers", variable=number_var).pack()
tb.Checkbutton(app, text="Include Symbols", variable=symbol_var).pack()

# Buttons and entries
tb.Button(app, text="✨ Generate Password ✨", bootstyle="info", command=generate_password).pack(pady=10)
password_entry = tb.Entry(app, font=("Courier", 14), justify="center", width=35)
password_entry.pack(pady=10)

# Status label
status_label = tb.Label(app, text="", font=("Arial", 10), background="#ffe6f0", bootstyle="success")
status_label.pack()

app.mainloop()
