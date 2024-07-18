import tkinter as tk

# Function to update the entry field when a button is pressed
def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

# Function to clear the entry field
def button_clear():
    entry.delete(0, tk.END)

# Function to perform the calculation
def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the entry field
entry = tk.Entry(root, width=16, borderwidth=5, font=('Arial', 24) , bg='light grey', fg='black')
entry.grid(row=0, column=0, columnspan=4)

# Define the buttons
button_1 = tk.Button(root, text="1", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(1) , bg='light pink', fg='black')
button_2 = tk.Button(root, text="2", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(2) , bg='light pink', fg='black')
button_3 = tk.Button(root, text="3", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(3) , bg='light pink', fg='black')
button_4 = tk.Button(root, text="4", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(4) , bg='light pink', fg='black')
button_5 = tk.Button(root, text="5", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(5) , bg='light pink', fg='black')
button_6 = tk.Button(root, text="6", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(6) , bg='light pink', fg='black')
button_7 = tk.Button(root, text="7", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(7) , bg='light pink', fg='black')
button_8 = tk.Button(root, text="8", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(8) , bg='light pink', fg='black')
button_9 = tk.Button(root, text="9", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(9) , bg='light pink', fg='black')
button_0 = tk.Button(root, text="0", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click(0) , bg='light pink', fg='black')

button_add = tk.Button(root, text="+", padx=20, pady=20, font=('Arial', 18), command=lambda: button_click('+') , bg='light pink', fg='black')
button_subtract = tk.Button(root, text="-", padx=22, pady=20, font=('Arial', 18), command=lambda: button_click('-') , bg='light pink', fg='black')
button_multiply = tk.Button(root, text="*", padx=21, pady=20, font=('Arial', 18), command=lambda: button_click('*') , bg='light pink', fg='black')
button_divide = tk.Button(root, text="/", padx=22, pady=20, font=('Arial', 18), command=lambda: button_click('/') , bg='light pink', fg='black')
button_equal = tk.Button(root, text="=", padx=20, pady=20, font=('Arial', 18), command=button_equal , bg='light pink', fg='black')
button_clear = tk.Button(root, text="C", padx=20, pady=20, font=('Arial', 18), command=button_clear , bg='light pink', fg='black')

# Place the buttons on the grid
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

button_equal.grid(row=4, column=2)
button_clear.grid(row=4, column=1)

# Run the main loop
root.mainloop()
