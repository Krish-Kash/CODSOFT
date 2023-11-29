import tkinter as tk
from tkinter import Label, Entry, Button, StringVar
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        master.title("Password Generator")

        # Label and Entry for password length
        self.length_label = Label(master, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10)

        self.length_entry = Entry(master)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label to display generated password
        self.password_label = Label(master, text="Generated Password:")
        self.password_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # StringVar to store the generated password
        self.generated_password = StringVar()
        self.generated_password.set("")

        # Entry to display generated password
        self.password_entry = Entry(master, textvariable=self.generated_password, state='readonly')
        self.password_entry.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Button to generate password
        self.generate_button = Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=3, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            # Get password length from the entry
            password_length = int(self.length_entry.get())

            # Generate the password
            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))

            # Update the generated password in the Entry
            self.generated_password.set(password)
        except ValueError:
            self.generated_password.set("Invalid length")

if __name__ == '__main__':
    root = tk.Tk()
    password_generator_app = PasswordGeneratorApp(root)
    root.mainloop()
