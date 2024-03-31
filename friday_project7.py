import tkinter as tk
from tkinter import messagebox
import sqlite3

#function to create the database table
def create_table():
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, email TEXT UNIQUE, password TEXT)''')
    conn.commit()
    conn.close()

#function to insert a new user into the database
def insert_user(email, password):
    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
    conn.commit()
    conn.close()

#function to check if email is valid
def validate_email(email):
    return "@" in email and "." in email

#function to sign up a new user
def sign_up():
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()

    if not validate_email(email):
        messagebox.showerror("Error", "Invalid email format")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match")
        return

    insert_user(email, password)
    messagebox.showinfo("Success", "Account created successfully")

#function to log in an existing user
def sign_in():
    email = email_entry_sign_in.get()
    password = password_entry_sign_in.get()

    conn = sqlite3.connect('user_database.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    result = c.fetchone()
    conn.close()

    if result:
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error", "Email or password incorrect")

#create the main window
root = tk.Tk()
root.title("User Portal")

#create the sign-up window
sign_up_window = tk.Toplevel(root)
sign_up_window.title("Sign Up")

#create widgets for sign-up window
tk.Label(sign_up_window, text="Email:").pack()
email_entry = tk.Entry(sign_up_window)
email_entry.pack()

tk.Label(sign_up_window, text="Password:").pack()
password_entry = tk.Entry(sign_up_window, show="*")
password_entry.pack()

tk.Label(sign_up_window, text="Confirm Password:").pack()
confirm_password_entry = tk.Entry(sign_up_window, show="*")
confirm_password_entry.pack()

tk.Button(sign_up_window, text="Sign Up", command=sign_up).pack()

#create the sign-in window
sign_in_window = tk.Toplevel(root)
sign_in_window.title("Sign In")

#create widgets for sign-in window
tk.Label(sign_in_window, text="Email:").pack()
email_entry_sign_in = tk.Entry(sign_in_window)
email_entry_sign_in.pack()

tk.Label(sign_in_window, text="Password:").pack()
password_entry_sign_in = tk.Entry(sign_in_window, show="*")
password_entry_sign_in.pack()

tk.Button(sign_in_window, text="Sign In", command=sign_in).pack()

# Initialize database table
create_table()

root.mainloop()