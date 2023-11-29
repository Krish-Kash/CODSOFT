from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QListWidget, QPushButton, QMessageBox

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('To-Do List')

        # Entry for adding tasks
        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("Enter a task")

        # List widget to display tasks
        self.list_widget = QListWidget(self)

        # Buttons for adding and removing tasks
        add_button = QPushButton("Add Task", self)
        add_button.clicked.connect(self.add_task)

        remove_button = QPushButton("Remove Task", self)
        remove_button.clicked.connect(self.remove_task)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.entry)
        layout.addWidget(self.list_widget)
        layout.addWidget(add_button)
        layout.addWidget(remove_button)

        self.setLayout(layout)

    def add_task(self):
        task = self.entry.text()
        if task:
            self.list_widget.addItem(task)
            self.entry.clear()
        else:
            self.show_warning("Warning", "Please enter a task.")

    def remove_task(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            self.list_widget.takeItem(self.list_widget.row(selected_item))
        else:
            self.show_warning("Warning", "Please select a task to remove.")

    def show_warning(self, title, message):
        msg_box = QMessageBox.warning(self, title, message, QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication([])
    todo_app = ToDoApp()
    todo_app.show()
    app.exec_()



