import tkinter as tk


class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Simple Calculator")

        # Entry for input and display
        self.input_display = tk.Entry(master, width=20, borderwidth=5)
        self.input_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons for digits
        for i in range(1, 10):
            tk.Button(master, text=str(i), command=lambda i=i: self.update_input(str(i))).grid(
                row=(i - 1) // 3 + 1, column=(i - 1) % 3, padx=5, pady=5
            )

        tk.Button(master, text="0", command=lambda: self.update_input("0")).grid(row=4, column=1, padx=5, pady=5)

        # Buttons for basic operations
        operations = ["+", "-", "*", "/"]
        for i, operation in enumerate(operations):
            tk.Button(master, text=operation, command=lambda op=operation: self.update_input(op)).grid(
                row=i + 1, column=3, padx=5, pady=5
            )

        # Equal button
        tk.Button(master, text="=", command=self.calculate_result).grid(row=4, column=2, padx=5, pady=5)

        # Clear button
        tk.Button(master, text="C", command=self.clear_input).grid(row=4, column=0, padx=5, pady=5)

    def update_input(self, value):
        current_text = self.input_display.get()
        new_text = current_text + value
        self.input_display.delete(0, tk.END)
        self.input_display.insert(0, new_text)

    def calculate_result(self):
        try:
            expression = self.input_display.get()
            result = eval(expression)
            self.input_display.delete(0, tk.END)
            self.input_display.insert(0, str(result))
        except Exception as e:
            self.input_display.delete(0, tk.END)
            self.input_display.insert(0, "Error")

    def clear_input(self):
        self.input_display.delete(0, tk.END)


if __name__ == '__main__':
    root = tk.Tk()
    calculator_app = CalculatorApp(root)
    root.mainloop()
