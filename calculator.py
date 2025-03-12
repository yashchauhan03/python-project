import tkinter as tk
import math

# Create the main window
root = tk.Tk()
root.title("Scientific Calculator")

# Define a function for button click
def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

def on_clear():
    entry.delete(0, tk.END)

def on_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_sqrt():
    try:
        result = math.sqrt(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_sin():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_cos():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_tan():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_log():
    try:
        result = math.log(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def on_exp():
    try:
        result = math.exp(float(entry.get()))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the entry widget for displaying input/output
entry = tk.Entry(root, width=40, borderwidth=5, font=("Arial", 14), relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('sqrt', 5, 0), ('sin', 5, 1), ('cos', 5, 2), ('tan', 5, 3),
    ('log', 6, 0), ('exp', 6, 1), ('(', 6, 2), (')', 6, 3)
]

# Create buttons and add them to the grid
for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_equal)
    elif text == "sqrt":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_sqrt)
    elif text == "sin":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_sin)
    elif text == "cos":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_cos)
    elif text == "tan":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_tan)
    elif text == "log":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_log)
    elif text == "exp":
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=on_exp)
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 14), command=lambda value=text: on_button_click(value))
    
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", width=10, height=3, font=("Arial", 14), command=on_clear)
clear_button.grid(row=7, column=0, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
