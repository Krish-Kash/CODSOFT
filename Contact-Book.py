import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QDialog, QFormLayout, QInputDialog


class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - Phone: {self.phone}"


class AddContactDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.name_lineedit = QLineEdit()
        self.phone_lineedit = QLineEdit()
        self.email_lineedit = QLineEdit()
        self.address_lineedit = QLineEdit()

        form_layout = QFormLayout()
        form_layout.addRow("Name:", self.name_lineedit)
        form_layout.addRow("Phone:", self.phone_lineedit)
        form_layout.addRow("Email:", self.email_lineedit)
        form_layout.addRow("Address:", self.address_lineedit)

        buttons_layout = QHBoxLayout()
        ok_button = QPushButton("OK")
        ok_button.clicked.connect(self.accept)
        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.reject)

        buttons_layout.addWidget(ok_button)
        buttons_layout.addWidget(cancel_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(buttons_layout)

        self.setLayout(main_layout)

    def get_contact_data(self):
        name = self.name_lineedit.text()
        phone = self.phone_lineedit.text()
        email = self.email_lineedit.text()
        address = self.address_lineedit.text()
        return Contact(name, phone, email, address)


class ContactManagementApp(QWidget):
    def __init__(self):
        super().__init__()

        self.contacts = []

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Contact Management System")

        self.name_label = QLabel("Name:")
        self.name_lineedit = QLineEdit()

        self.phone_label = QLabel("Phone:")
        self.phone_lineedit = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_lineedit = QLineEdit()

        self.address_label = QLabel("Address:")
        self.address_lineedit = QLineEdit()

        self.add_button = QPushButton("Add Contact")
        self.add_button.clicked.connect(self.show_add_contact_dialog)

        self.view_button = QPushButton("View Contacts")
        self.view_button.clicked.connect(self.view_contacts)

        self.search_button = QPushButton("Search Contact")
        self.search_button.clicked.connect(self.search_contact)

        self.update_button = QPushButton("Update Contact")
        self.update_button.clicked.connect(self.update_contact)

        self.delete_button = QPushButton("Delete Contact")
        self.delete_button.clicked.connect(self.delete_contact)

        self.list_widget = QListWidget()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.name_label)
        main_layout.addWidget(self.name_lineedit)
        main_layout.addWidget(self.phone_label)
        main_layout.addWidget(self.phone_lineedit)
        main_layout.addWidget(self.email_label)
        main_layout.addWidget(self.email_lineedit)
        main_layout.addWidget(self.address_label)
        main_layout.addWidget(self.address_lineedit)
        main_layout.addWidget(self.add_button)
        main_layout.addWidget(self.view_button)
        main_layout.addWidget(self.search_button)
        main_layout.addWidget(self.update_button)
        main_layout.addWidget(self.delete_button)
        main_layout.addWidget(self.list_widget)

        self.setLayout(main_layout)

    def show_add_contact_dialog(self):
        dialog = AddContactDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            new_contact = dialog.get_contact_data()
            self.contacts.append(new_contact)
            QMessageBox.information(self, "Success", "Contact added successfully!")
            self.clear_entries()
            self.update_list_widget()

    def view_contacts(self):
        self.list_widget.clear()
        for contact in self.contacts:
            self.list_widget.addItem(str(contact))

    def search_contact(self):
        search_query, ok = QInputDialog.getText(self, "Search Contact", "Enter name or phone number:")
        if ok and search_query:
            results = [str(contact) for contact in self.contacts if
                       search_query.lower() in contact.name.lower() or search_query in contact.phone]
            if results:
                QMessageBox.information(self, "Search Results", "\n".join(results))
            else:
                QMessageBox.information(self, "Search Results", "No contacts found.")

    def update_contact(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            selected_contact = next(contact for contact in self.contacts if str(contact) == selected_item.text())
            new_phone, ok = QInputDialog.getText(self, "Update Contact", f"Enter new phone number for {selected_contact.name}:")
            if ok and new_phone:
                selected_contact.phone = new_phone
                QMessageBox.information(self, "Success", "Contact updated successfully!")
                self.update_list_widget()
            else:
                QMessageBox.warning(self, "Warning", "Phone number cannot be empty.")
        else:
            QMessageBox.warning(self, "Warning", "Please select a contact from the list.")

    def delete_contact(self):
        selected_item = self.list_widget.currentItem()
        if selected_item:
            selected_contact = next(contact for contact in self.contacts if str(contact) == selected_item.text())
            confirmation = QMessageBox.question(self, "Delete Contact",
                                               f"Are you sure you want to delete {selected_contact.name}'s contact?",
                                               QMessageBox.Yes | QMessageBox.No)
            if confirmation == QMessageBox.Yes:
                self.contacts.remove(selected_contact)
                QMessageBox.information(self, "Success", "Contact deleted successfully!")
                self.update_list_widget()
        else:
            QMessageBox.warning(self, "Warning", "Please select a contact from the list.")

    def update_list_widget(self):
        self.list_widget.clear()
        for contact in self.contacts:
            self.list_widget.addItem(str(contact))

    def clear_entries(self):
        self.name_lineedit.clear()
        self.phone_lineedit.clear()
        self.email_lineedit.clear()
        self.address_lineedit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    contact_app = ContactManagementApp()
    contact_app.show()
    sys.exit(app.exec_())

