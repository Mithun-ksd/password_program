import tkinter as tk
import random
import string
import pyperclip

def generate():
    length = int(length_entry.get())
    chars = ""
    
    if lower.get():
        chars += string.ascii_lowercase
    if upper.get():
        chars += string.ascii_uppercase
    if nums.get():
        chars += string.digits
    if symbols.get():
        chars += string.punctuation
        
    if chars == "":
        result_label.config(text="Select options!")
        return
        
    password = "".join(random.choices(chars, k=length))
    result_label.config(text=password)

def check_strength():
    pwd = strength_entry.get()
    score = 0

    if not pwd:
        strength_label.config(text="Enter a password", fg="black")
        return
    if len(pwd)>= 8:
        score += 1
    if any(c.islower() for c in pwd):
        score += 1
    if any(c.isupper() for c in pwd):
        score += 1
    if any(c.isdigit() for c in pwd):
        score += 1
    if any(c in string.punctuation for c in pwd):
        score += 1

    if score <= 2:
        strength_label.config(text="Weak", fg="red")
    elif score <= 4:
        strength_label.config(text="Medium", fg="orange")
    else:
        strength_label.config(text="Strong", fg="green")

def clear_password():
    strength_entry.delete(0, tk.END)
    strength_label.config(text="")

def clear_generator():
    result_label.config(text="")  


def copy_to_clipboard():
    pyperclip.copy(result_label.cget("text"))
    
window = tk.Tk()
window.title("Password Tool")
window.geometry("400x600")
window.resizable(False, False)

#Password Generator
tk.Label(window, text="Generator", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(window, text="Length:").pack()
length_entry = tk.Entry(window, width=10)
length_entry.insert(0, "12")
length_entry.pack()

lower = tk.BooleanVar(value=True)
upper = tk.BooleanVar(value=True)
nums = tk.BooleanVar(value=False)
symbols = tk.BooleanVar(value=False)

tk.Checkbutton(window, text="Lowercase", variable=lower).pack(anchor="w", padx=100)
tk.Checkbutton(window, text="Uppercase", variable=upper).pack(anchor="w", padx=100)
tk.Checkbutton(window, text="Numbers", variable=nums).pack(anchor="w", padx=100)
tk.Checkbutton(window, text="Symbols", variable=symbols).pack(anchor="w", padx=100)

tk.Button(window, text="Generate", command=generate).pack(pady=10)

result_label = tk.Label(window, text="", font=("Courier", 14, "bold"), fg="blue")
result_label.pack(pady=10)
"""
tk.Button(window, text="Clear", command=clear_generator).pack(side="left", padx=10)
tk.Button(window, text="Copy", command=copy_to_clipboard).pack(side="left")
"""
button_frame = tk.Frame(window)
button_frame.pack(pady=10)
tk.Button(button_frame, text="Clear", command=clear_generator).pack(side="left", padx=15)
tk.Button(button_frame, text="Copy", command=copy_to_clipboard).pack(side="left", padx=15)

#Strength tester
tk.Frame(window, height=2, bg="gray").pack(fill="x", pady=10)
tk.Label(window, text="Strength Tester", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(window, text="Enter Password:").pack()
strength_entry = tk.Entry(window, width=30)
strength_entry.pack(pady=10)
"""
tk.Button(window, text="Check", command=check_strength).pack(side="left",padx=100)
tk.Button(window, text="Clear", command=clear_password).pack(side="left")
"""
strength_frame = tk.Frame(window)
strength_frame.pack(pady=10)
tk.Button(strength_frame, text="Check", command=check_strength).pack(side="left", padx=15)
tk.Button(strength_frame, text="Clear", command=clear_password).pack(side="left", padx=15)

strength_label = tk.Label(window, text="", font=("Arial", 16, "bold"))
strength_label.pack(side="top")

window.mainloop()
