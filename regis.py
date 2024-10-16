import tkinter as tk
from tkinter import messagebox

import csv
def add(username, password):
    lst = []
    s = username + "," + password + '\n'
    lst.append(s)
    with open("users.csv", "a") as file:
        file.writelines(lst)


def register():
    username = entry_username.get()
    password = entry_password.get()
    confirm_password = entry_confirm_password.get()
    add(username, password)

    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "All fields must be filled")
    elif password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
    else:
        messagebox.showinfo("Success", "Registration successful for {}".format(username))
    add(username, password)
        # You can add code here to save the registration information to a database or file.

# Create the main window
root = tk.Tk()
root.title("Registration Page")

# Create and place widgets
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=10)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=10)

label_confirm_password = tk.Label(root, text="Confirm Password:")
label_confirm_password.pack(pady=10)
entry_confirm_password = tk.Entry(root, show="*")
entry_confirm_password.pack(pady=10)

button_register = tk.Button(root, text="Register", command=register)
button_register.pack(pady=20)


# Start the Tkinter main loop
root.mainloop()






