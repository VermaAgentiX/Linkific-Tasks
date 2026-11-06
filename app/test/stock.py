import pandas as pd
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QLineEdit, QSpinBox, QVBoxLayout, QWidget, QPushButton, QMessageBox

class StockManager(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize table widget
        self.form = QWidget()
        self.form.table_item_table = QTableWidget(self)
        self.form.table_item_table.setRowCount(5)  # Example number of rows
        self.form.table_item_table.setColumnCount(8)  # Example number of columns

        # Set headers for the table (adjust according to your structure)
        self.form.table_item_table.setHorizontalHeaderLabels(
            ['Description', 'HSN', 'Quantity', 'Rate', 'GST Rate', 'CGST', 'SGST', 'Total']
        )

        # Add widgets to the first column (Description)
        for row in range(self.form.table_item_table.rowCount()):
            description_widget = QLineEdit()  # Create a QLineEdit widget for the Description column
            self.form.table_item_table.setCellWidget(row, 0, description_widget)

            # Add a QSpinBox widget to the "Quantity" column
            quantity_widget = QSpinBox()  # Create a QSpinBox widget for the Quantity column
            self.form.table_item_table.setCellWidget(row, 2, quantity_widget)

        # Example button to trigger the search and update logic
        self.button = QPushButton('Update Quantity', self)
        self.button.clicked.connect(self.update_quantity)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.form.table_item_table)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def update_quantity(self):
        # Load the CSV file
        df = pd.read_csv('stock_data.csv')

        # Loop through each row in the table
        for row in range(self.form.table_item_table.rowCount()):
            # Get the widget in the Description column
            widget_description = self.form.table_item_table.cellWidget(row, 0)
            description = widget_description.text() if widget_description is not None else ""

            # Get the widget in the Quantity column
            widget_quantity = self.form.table_item_table.cellWidget(row, 2)
            if widget_quantity is not None:
                quantity = widget_quantity.value()  # Get the value from the QSpinBox
            else:
                quantity = 0  # Handle the case when there's no widget

            # Check for matching description in CSV
            mask = df['Item Name'].str.lower() == description.lower()
            if mask.any():  # If the description is found
                # Get the quantity from the CSV
                csv_quantity = df.at[df[mask].index[0], 'Quantity']

                if quantity > csv_quantity:
                    # Show a message box if quantity entered is greater than the CSV quantity
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText(f"The quantity entered ({quantity}) exceeds the available quantity ({csv_quantity}) in stock.")
                    msg.setWindowTitle("Quantity Exceeded")
                    msg.exec()
                else:
                    # Decrement the quantity in the dataframe
                    idx = df[mask].index[0]  # Get the index of the matched item
                    df.at[idx, 'Quantity'] = max(0, csv_quantity - quantity)  # Decrement quantity

                    # Update the table cell with the new quantity
                    self.form.table_item_table.cellWidget(row, 2).setValue(df.at[idx, 'Quantity'])  # Update the table widget

                    # Optionally print the updated row for verification
                    print(f"Updated {description}: New Quantity = {df.at[idx, 'Quantity']}")

        # Save the updated dataframe back to the CSV
        df.to_csv('stock_data.csv', index=False)

# Example usage
if __name__ == "__main__":
    app = QApplication([])
    window = StockManager()
    window.show()
    app.exec()
