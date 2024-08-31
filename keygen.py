import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_random_key(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def on_generate():
    try:
        length = int(entry_length.get())
        count = int(entry_count.get())
        include_spaces = var_spaces.get()  # Check if spaces should be included
        
        if length <= 0 or count <= 0:
            raise ValueError("Length and count must be positive integers.")
        
        keys = [generate_random_key(length) for _ in range(count)]
        
        if include_spaces:
            keys_text = " ||| ".join(keys)  # Add ' ||| ' between keys
        else:
            keys_text = "\n".join(keys)
        
        keys_text = f" {keys_text} "  # Add spaces before and after
        
        pyperclip.copy(keys_text)  # Copy keys to clipboard
        messagebox.showinfo("Generated Keys", f"Generated {count} Keys:\n{keys_text}\n\nKeys copied to clipboard.")
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

# Set up the GUI
root = tk.Tk()
root.title("Random Key Generator")

tk.Label(root, text="Enter the length of each key:").pack(padx=10, pady=5)
entry_length = tk.Entry(root)
entry_length.pack(padx=10, pady=5)

tk.Label(root, text="Enter the number of keys to generate:").pack(padx=10, pady=5)
entry_count = tk.Entry(root)
entry_count.pack(padx=10, pady=5)

# Checkbox for including spaces
var_spaces = tk.BooleanVar()
chk_spaces = tk.Checkbutton(root, text="Include ' ||| ' between keys", variable=var_spaces)
chk_spaces.pack(padx=10, pady=5)

tk.Button(root, text="Generate Keys", command=on_generate).pack(padx=10, pady=10)

root.mainloop()
