import pandas as pd
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton

class StockManager(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize table widget
        self.form = QWidget()
        self.form.table_item_table = QTableWidget(self)
        self.form.table_item_table.setRowCount(0)  # Initialize with 0 rows
        self.form.table_item_table.setColumnCount(4)  # Example number of columns

        # Set headers for the table (adjust according to your structure)
        self.form.table_item_table.setHorizontalHeaderLabels(['Stock', 'Item Name', 'Rate (in Rs)', 'Quantity'])

        # Example button to trigger the refresh
        self.button = QPushButton('Refresh Table', self)
        self.button.clicked.connect(self.refresh_table)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.form.table_item_table)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Initial load of data from CSV
        self.load_data_from_csv()

    def load_data_from_csv(self):
        # Load the CSV file into a DataFrame
        df = pd.read_csv('stock_data.csv')

        # Clear the existing rows in the table
        self.form.table_item_table.setRowCount(0)

        # Add new rows to the table based on the CSV data
        for row in range(len(df)):
            self.form.table_item_table.insertRow(row)  # Insert a new row

            # Populate the cells for each row with values from the CSV
            self.form.table_item_table.setItem(row, 0, QTableWidgetItem(str(df.iloc[row]['Stock'])))
            self.form.table_item_table.setItem(row, 1, QTableWidgetItem(str(df.iloc[row]['Item Name'])))
            self.form.table_item_table.setItem(row, 2, QTableWidgetItem(str(df.iloc[row]['Rate (in Rs)'])))
            self.form.table_item_table.setItem(row, 3, QTableWidgetItem(str(df.iloc[row]['Quantity'])))

    def refresh_table(self):
        # Reload and refresh the table with new data from CSV
        self.load_data_from_csv()

# Example usage
if __name__ == "__main__":
    app = QApplication([])
    window = StockManager()
    window.show()
    app.exec()
