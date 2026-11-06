from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QLineEdit, QPushButton, QListWidget, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QCompleter
)
from PySide6.QtCore import Qt
import sys


class MedicalShopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Medical Shop Inventory")
        self.setGeometry(100, 100, 800, 500)

        self.stocks = {}  # Dictionary to store stock and items with rates and quantities

        self.init_ui()

    def init_ui(self):
        # Main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Stock Management Layout
        stock_layout = QHBoxLayout()
        self.stock_name_input = QLineEdit()
        self.stock_name_input.setPlaceholderText("Enter Stock Name")
        add_stock_button = QPushButton("Add Stock")
        add_stock_button.clicked.connect(self.add_stock)
        delete_stock_button = QPushButton("Delete Stock")
        delete_stock_button.clicked.connect(self.delete_stock)
        stock_layout.addWidget(QLabel("Stock Name:"))
        stock_layout.addWidget(self.stock_name_input)
        stock_layout.addWidget(add_stock_button)
        stock_layout.addWidget(delete_stock_button)

        # Search Stock Layout
        search_layout = QHBoxLayout()
        self.search_stock_input = QLineEdit()
        self.search_stock_input.setPlaceholderText("Search Stock")
        self.search_stock_input.textChanged.connect(self.update_stock_suggestions)
        self.search_stock_input.editingFinished.connect(self.select_stock_from_search)  # Add this line
        self.search_completer = QCompleter()
        self.search_completer.setCaseSensitivity(Qt.CaseInsensitive)  # Corrected here
        self.search_stock_input.setCompleter(self.search_completer)
        search_layout.addWidget(QLabel("Search Stock:"))
        search_layout.addWidget(self.search_stock_input)

        # Item Management Layout
        item_layout = QHBoxLayout()
        self.stock_selector = QComboBox()
        self.stock_selector.addItem("Select Stock")
        self.item_name_input = QLineEdit()
        self.item_name_input.setPlaceholderText("Enter Item Name")
        self.item_rate_input = QLineEdit()
        self.item_rate_input.setPlaceholderText("Enter Item Rate")
        self.item_quantity_input = QLineEdit()
        self.item_quantity_input.setPlaceholderText("Enter Quantity (Default: 1)")
        add_item_button = QPushButton("Add Item")
        add_item_button.clicked.connect(self.add_item)
        delete_item_button = QPushButton("Delete Item")
        delete_item_button.clicked.connect(self.delete_item)
        item_layout.addWidget(QLabel("Select Stock:"))
        item_layout.addWidget(self.stock_selector)
        item_layout.addWidget(QLabel("Item Name:"))
        item_layout.addWidget(self.item_name_input)
        item_layout.addWidget(QLabel("Rate:"))
        item_layout.addWidget(self.item_rate_input)
        item_layout.addWidget(QLabel("Quantity:"))
        item_layout.addWidget(self.item_quantity_input)
        item_layout.addWidget(add_item_button)
        item_layout.addWidget(delete_item_button)

        # Item Search Layout
        item_search_layout = QHBoxLayout()
        self.search_item_input = QLineEdit()
        self.search_item_input.setPlaceholderText("Search Item")
        self.search_item_input.textChanged.connect(self.filter_items)
        item_search_layout.addWidget(QLabel("Search Item:"))
        item_search_layout.addWidget(self.search_item_input)

        # Stock and Items Display
        display_layout = QHBoxLayout()
        self.stock_list = QListWidget()
        self.stock_list.itemClicked.connect(self.display_items)
        self.item_table = QTableWidget()
        self.item_table.setColumnCount(3)
        self.item_table.setHorizontalHeaderLabels(["Name", "Rate (in Rs)", "Quantity"])
        display_layout.addWidget(QLabel("Stocks"))
        display_layout.addWidget(self.stock_list)
        display_layout.addWidget(self.item_table)

        # Add layouts to main layout
        main_layout.addLayout(stock_layout)
        main_layout.addLayout(search_layout)
        main_layout.addLayout(item_layout)
        main_layout.addLayout(item_search_layout)
        main_layout.addLayout(display_layout)

    def add_stock(self):
        stock_name = self.stock_name_input.text().strip()
        if not stock_name:
            QMessageBox.warning(self, "Error", "Stock name cannot be empty!")
            return

        if stock_name in self.stocks:
            QMessageBox.warning(self, "Error", "Stock already exists!")
            return

        self.stocks[stock_name] = []  # Create an empty list for items
        self.stock_list.addItem(stock_name)
        self.stock_selector.addItem(stock_name)
        self.update_stock_suggestions()
        self.stock_name_input.clear()
        QMessageBox.information(self, "Success", f"Stock '{stock_name}' added!")

    def update_stock_suggestions(self):
        stock_names = list(self.stocks.keys())
        self.search_completer.setModel(self.stock_selector.model())
        self.stock_selector.clear()
        self.stock_selector.addItem("Select Stock")
        for stock in stock_names:
            self.stock_selector.addItem(stock)

    def select_stock_from_search(self):
        search_text = self.search_stock_input.text().strip()
        if search_text in self.stocks:
            index = self.stock_selector.findText(search_text)
            if index != -1:
                self.stock_selector.setCurrentIndex(index)
        else:
            QMessageBox.warning(self, "Error", "Stock not found!")

    def add_item(self):
        selected_stock = self.stock_selector.currentText()
        if selected_stock == "Select Stock":
            QMessageBox.warning(self, "Error", "Please select a stock!")
            return

        item_name = self.item_name_input.text().strip()
        item_rate = self.item_rate_input.text().strip()
        item_quantity = self.item_quantity_input.text().strip()

        if not item_name or not item_rate:
            QMessageBox.warning(self, "Error", "Item name and rate cannot be empty!")
            return

        try:
            item_rate = float(item_rate)
        except ValueError:
            QMessageBox.warning(self, "Error", "Item rate must be a valid number!")
            return

        try:
            item_quantity = int(item_quantity) if item_quantity else 1
            if item_quantity <= 0:
                raise ValueError
        except ValueError:
            QMessageBox.warning(self, "Error", "Quantity must be a positive integer!")
            return

        if item_name in [item['name'] for item in self.stocks[selected_stock]]:
            QMessageBox.warning(self, "Error", "Item already exists in this stock!")
            return

        self.stocks[selected_stock].append({
            "name": item_name,
            "rate": item_rate,
            "quantity": item_quantity
        })

        if self.stock_list.currentItem() and self.stock_list.currentItem().text() == selected_stock:
            self.add_item_to_table(item_name, item_rate, item_quantity)

        self.item_name_input.clear()
        self.item_rate_input.clear()
        self.item_quantity_input.clear()
        QMessageBox.information(self, "Success", f"Item '{item_name}' added to stock '{selected_stock}'!")

    def add_item_to_table(self, name, rate, quantity):
        row_position = self.item_table.rowCount()
        self.item_table.insertRow(row_position)
        self.item_table.setItem(row_position, 0, QTableWidgetItem(name))
        self.item_table.setItem(row_position, 1, QTableWidgetItem(f"{rate:.2f}"))
        self.item_table.setItem(row_position, 2, QTableWidgetItem(str(quantity)))

    def display_items(self, stock_item):
        stock_name = stock_item.text()
        self.item_table.setRowCount(0)  # Clear the table
        if stock_name in self.stocks:
            for item in self.stocks[stock_name]:
                self.add_item_to_table(item['name'], item['rate'], item['quantity'])

    def filter_items(self):
        search_term = self.search_item_input.text().lower()
        selected_stock = self.stock_selector.currentText()

        if selected_stock == "Select Stock":
            return

        self.item_table.setRowCount(0)  # Clear the table

        for item in self.stocks[selected_stock]:
            if search_term in item['name'].lower():  # Search based on item name
                self.add_item_to_table(item['name'], item['rate'], item['quantity'])

    def delete_stock(self):
        selected_stock_item = self.stock_list.currentItem()
        if not selected_stock_item:
            QMessageBox.warning(self, "Error", "Please select a stock to delete.")
            return

        selected_stock = selected_stock_item.text()
        if selected_stock not in self.stocks:
            QMessageBox.warning(self, "Error", "Stock not found!")
            return

        confirm = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the stock '{selected_stock}'?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if confirm == QMessageBox.Yes:
            # Remove stock from dictionary and list
            del self.stocks[selected_stock]
            self.stock_list.takeItem(self.stock_list.row(selected_stock_item))
            self.stock_selector.removeItem(self.stock_selector.findText(selected_stock))
            QMessageBox.information(self, "Success", f"Stock '{selected_stock}' deleted!")

    def delete_item(self):
        selected_row = self.item_table.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Error", "Please select an item to delete.")
            return

        selected_item_name = self.item_table.item(selected_row, 0).text()
        selected_stock = self.stock_selector.currentText()

        if selected_stock == "Select Stock":
            QMessageBox.warning(self, "Error", "Please select a stock to delete an item from.")
            return

        confirm = QMessageBox.question(self, "Confirm Deletion", f"Are you sure you want to delete the item '{selected_item_name}' from stock '{selected_stock}'?",
                                       QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if confirm == QMessageBox.Yes:
            # Remove item from stock
            self.stocks[selected_stock] = [item for item in self.stocks[selected_stock] if item['name'] != selected_item_name]
            self.item_table.removeRow(selected_row)
            QMessageBox.information(self, "Success", f"Item '{selected_item_name}' deleted from stock '{selected_stock}'!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MedicalShopApp()
    window.show()
    sys.exit(app.exec())
