import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, 
    QPushButton, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QSpinBox, QComboBox
)
from PySide6.QtGui import QIntValidator
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4

class TaxInvoiceApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tax Invoice")
        self.setGeometry(100, 100, 800, 600)

      
        main_layout = QVBoxLayout()

       
        self.shop_details = QFormLayout()
        self.shop_name = QLineEdit()
        self.shop_address = QLineEdit()
        self.shop_gstin = QLineEdit()
        self.shop_contact = QLineEdit()
        self.shop_details.addRow("Shop Name:", self.shop_name)
        self.shop_details.addRow("Shop Address:", self.shop_address)
        self.shop_details.addRow("Shop GSTIN:", self.shop_gstin)
        self.shop_details.addRow("Shop Contact:", self.shop_contact)

        # Customer details and databse connect
        self.customer_details = QFormLayout()
        self.customer_name = QLineEdit()
        self.customer_address = QLineEdit()
        self.customer_gstin = QLineEdit()
        self.customer_details.addRow("Customer Name:", self.customer_name)
        self.customer_details.addRow("Customer Address:", self.customer_address)
        self.customer_details.addRow("Customer GSTIN:", self.customer_gstin)

        # Add Table for Item Details
        self.item_table = QTableWidget(0, 6)  # 6 columns
        self.item_table.setHorizontalHeaderLabels(["Description", "HSN Code", "Quantity", "Rate", "GST Rate (%)", "Total"])
        self.add_item_button = QPushButton("Add Item")
        self.add_item_button.clicked.connect(self.add_item_row)

        # Save to PDF
        self.save_button = QPushButton("Save as PDF")
        self.save_button.clicked.connect(self.save_to_pdf)

        # Add widgets to main layout
        main_layout.addLayout(self.shop_details)
        main_layout.addLayout(self.customer_details)
        main_layout.addWidget(self.item_table)
        main_layout.addWidget(self.add_item_button)
        main_layout.addWidget(self.save_button)

        # Set central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def add_item_row(self):
        row_position = self.item_table.rowCount()
        self.item_table.insertRow(row_position)

        # Add input fields for the new row
        self.item_table.setCellWidget(row_position, 0, QLineEdit())  # Description
        self.item_table.setCellWidget(row_position, 1, QLineEdit())  # HSN Code
        self.item_table.setCellWidget(row_position, 2, QSpinBox())  # Quantity
        self.item_table.setCellWidget(row_position, 3, QLineEdit())  # Rate
        self.item_table.setCellWidget(row_position, 4, QComboBox())  # GST Rate
        gst_rates = self.item_table.cellWidget(row_position, 4)
        gst_rates.addItems(["0", "5", "12", "18", "28"])
        self.item_table.setItem(row_position, 5, QTableWidgetItem("0.0"))  # Total (auto-calculate placeholder)

    def save_to_pdf(self):
        # Prepare data for the PDF
        shop_details = [
            f"Shop Name: {self.shop_name.text()}",
            f"Shop Address: {self.shop_address.text()}",
            f"Shop GSTIN: {self.shop_gstin.text()}",
            f"Contact: {self.shop_contact.text()}",
        ]
        customer_details = [
            f"Customer Name: {self.customer_name.text()}",
            f"Customer Address: {self.customer_address.text()}",
            f"Customer GSTIN: {self.customer_gstin.text()}",
        ]

        # Table data for items
        table_data = [["S. No.", "Description", "HSN Code", "Quantity", "Rate", "GST Rate (%)", "Total"]]
        for row in range(self.item_table.rowCount()):
            description = self.item_table.cellWidget(row, 0).text()
            hsn_code = self.item_table.cellWidget(row, 1).text()
            quantity = self.item_table.cellWidget(row, 2).value()
            rate = self.item_table.cellWidget(row, 3).text()
            gst_rate = self.item_table.cellWidget(row, 4).currentText()
            total = float(quantity) * float(rate) * (1 + int(gst_rate) / 100)
            self.item_table.setItem(row, 5, QTableWidgetItem(f"{total:.2f}"))
            table_data.append([row + 1, description, hsn_code, quantity, rate, gst_rate, f"{total:.2f}"])

        # Generate PDF
        pdf = SimpleDocTemplate("Tax_Invoice.pdf", pagesize=A4)
        elements = []

        # Add shop and customer details
        elements.append(Table([shop_details], colWidths=[400]))
        elements.append(Table([[" "]]))  # Blank row
        elements.append(Table([customer_details], colWidths=[400]))
        elements.append(Table([[" "]]))  # Blank row

       
        item_table = Table(table_data, colWidths=[30, 150, 80, 60, 60, 80, 80])
        item_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ]))
        elements.append(item_table)

       
        pdf.build(elements)

        print("PDF saved as Tax_Invoice.pdf")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TaxInvoiceApp()
    window.show()
    sys.exit(app.exec())
