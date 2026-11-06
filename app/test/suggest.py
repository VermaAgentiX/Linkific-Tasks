import sys
import pandas as pd
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PySide6.QtCore import QStringListModel
from PySide6.QtWidgets import QCompleter


class StockSearchApp(QWidget):
    def __init__(self):
        super().__init__()

        # Load stock data from CSV
        self.df = pd.read_csv('stock_data.csv')

        # Extract Item Names, Quantities, and Rates
        self.item_names = self.df['Item Name'].tolist()
        self.quantities = self.df['Quantity'].astype(str).tolist()
        self.rates = self.df['Rate (in Rs)'].astype(str).tolist()

        # Create UI elements
        self.line_edit_item = QLineEdit(self)
        self.line_edit_item.setPlaceholderText("Type item name...")

        self.line_edit_rate = QLineEdit(self)
        self.line_edit_rate.setPlaceholderText("Rate (in Rs)")
        self.line_edit_rate.setReadOnly(True)  # Make it read-only

        self.line_edit_quantity = QLineEdit(self)
        self.line_edit_quantity.setPlaceholderText("Type quantity...")

        self.update_button = QPushButton("Update Quantity", self)
        self.update_button.clicked.connect(self.update_quantity)

        # Create label to show available quantity
        self.label_available_quantity = QLabel("Available Quantity: N/A", self)

        # Setup completer for Item Name LineEdit
        self.model_item = QStringListModel(self.item_names)
        self.completer_item = QCompleter(self.model_item)
        self.line_edit_item.setCompleter(self.completer_item)

        # Setup completer for Quantity LineEdit
        self.model_quantity = QStringListModel(self.quantities)
        self.completer_quantity = QCompleter(self.model_quantity)
        self.line_edit_quantity.setCompleter(self.completer_quantity)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.line_edit_item)
        layout.addWidget(self.line_edit_rate)
        layout.addWidget(self.label_available_quantity)
        layout.addWidget(self.line_edit_quantity)
        layout.addWidget(self.update_button)
        self.setLayout(layout)

        self.setWindowTitle("Stock Item Update")
        self.setGeometry(300, 300, 400, 250)

        # Connect the item name field to update the available quantity and rate
        self.line_edit_item.textChanged.connect(self.update_item_details)

    def update_item_details(self):
        """Update the available quantity and rate based on item selection."""
        item_name = self.line_edit_item.text()

        # Check if the item exists in the stock data
        row = self.df[self.df['Item Name'] == item_name]

        if not row.empty:
            # Get the current quantity and rate from the CSV
            available_quantity = row['Quantity'].values[0]
            rate = row['Rate (in Rs)'].values[0]

            # Update the available quantity and rate fields
            self.label_available_quantity.setText(f"Available Quantity: {available_quantity}")
            self.line_edit_rate.setText(f"{rate}")
        else:
            self.label_available_quantity.setText("Available Quantity: N/A")
            self.line_edit_rate.clear()

    def update_quantity(self):
        # Get entered item name and quantity
        item_name = self.line_edit_item.text()
        quantity = self.line_edit_quantity.text()

        if item_name and quantity.isdigit():
            quantity = int(quantity)

            # Find the row matching the item name
            row = self.df[self.df['Item Name'] == item_name]

            if not row.empty:
                # Get the current quantity from the CSV
                current_quantity = row['Quantity'].values[0]

                # Check if entered quantity is smaller than the current quantity
                if quantity < current_quantity:
                    # Decrement the quantity
                    new_quantity = current_quantity - quantity

                    # Update the dataframe with the new quantity
                    self.df.loc[self.df['Item Name'] == item_name, 'Quantity'] = new_quantity

                    # Save the updated dataframe to CSV
                    self.df.to_csv('stock_data.csv', index=False)

                    # Clear the quantity field after updating
                    self.line_edit_quantity.clear()
                    print(f"Updated quantity for {item_name} to {new_quantity}.")
                else:
                    # Show message box if entered quantity is greater than available quantity
                    self.show_message("Error", "Entered quantity cannot be greater than available stock.")
            else:
                print(f"No item found with the name {item_name}.")
        else:
            print("Please enter a valid number for the quantity.")

    def show_message(self, title, message):
        """Shows a message box with the given title and message."""
        msg_box = QMessageBox(self)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = StockSearchApp()
    window.show()

    sys.exit(app.exec())
