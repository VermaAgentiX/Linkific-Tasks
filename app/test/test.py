import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
)








from PySide6.QtWidgets import (QLabel,
    QMainWindow, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QTableWidget,
    QTableWidgetItem, QWidget, QSpinBox, QComboBox
)
from PySide6.QtGui import QDoubleValidator

from fpdf import FPDF
from datetime import datetime

class SaleBill(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sale Bill with GST")
        self.setGeometry(100, 100, 900, 600)

        # Main layout
        layout = QVBoxLayout()

        # Shop details
        shop_details = QFormLayout()
        self.shop_name = QLineEdit()
        self.shop_address = QLineEdit()
        self.shop_gstin = QLineEdit()
        shop_details.addRow("Shop Name:", self.shop_name)
        shop_details.addRow("Shop Address:", self.shop_address)
        shop_details.addRow("Shop GSTIN:", self.shop_gstin)

        # Customer details
        customer_details = QFormLayout()
        self.customer_name = QLineEdit()
        self.customer_address = QLineEdit()
        self.customer_gstin = QLineEdit()
        customer_details.addRow("Customer Name:", self.customer_name)
        customer_details.addRow("Customer Address:", self.customer_address)
        customer_details.addRow("Customer GSTIN:", self.customer_gstin)

        # Item table
        self.item_table = QTableWidget(0, 8)
        self.item_table.setHorizontalHeaderLabels([
            "Description", "HSN Code", "Quantity", "Rate", "GST Rate (%)",
            "CGST", "SGST", "Total"
        ])
        add_item_button = QPushButton("Add Item")
        add_item_button.clicked.connect(self.add_item_row)

        # Save as PDF
        save_button = QPushButton("Save Invoice as PDF")
        save_button.clicked.connect(self.save_as_pdf)

        # Add to layout
        layout.addLayout(shop_details)
        layout.addLayout(customer_details)
        layout.addWidget(self.item_table)
        layout.addWidget(add_item_button)
        layout.addWidget(save_button)
        
        
        self.bank_name = QLineEdit(self)
        self.account_number = QLineEdit(self)
        self.ifsc_code = QLineEdit(self)
        self.branch = QLineEdit(self)
        
        
                # Banking details fields
        layout.addWidget(QLabel("Bank Name:"))
        layout.addWidget(self.bank_name)
        layout.addWidget(QLabel("Account Number:"))
        layout.addWidget(self.account_number)
        layout.addWidget(QLabel("IFSC Code:"))
        layout.addWidget(self.ifsc_code)
        layout.addWidget(QLabel("Branch:"))
        layout.addWidget(self.branch)

        # Set layout to central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_item_row(self):
        """Add a new row to the item table."""
        row_position = self.item_table.rowCount()
        self.item_table.insertRow(row_position)

        # Add widgets to the row
        self.item_table.setCellWidget(row_position, 0, QLineEdit())  # Description
        self.item_table.setCellWidget(row_position, 1, QLineEdit())  # HSN Code
        self.item_table.setCellWidget(row_position, 2, QSpinBox())  # Quantity
        self.item_table.cellWidget(row_position, 2).setMaximum(99999)
        rate_input = QLineEdit()
        rate_input.setValidator(QDoubleValidator(0, 999999, 2))  # Only allow valid rates
        self.item_table.setCellWidget(row_position, 3, rate_input)  # Rate

        gst_rate_combo = QComboBox()
        gst_rate_combo.addItems(["0", "5", "12", "18", "28"])
        gst_rate_combo.currentIndexChanged.connect(
            lambda: self.update_row_totals(row_position)
        )
        self.item_table.setCellWidget(row_position, 4, gst_rate_combo)  # GST Rate

        self.item_table.setItem(row_position, 5, QTableWidgetItem("0.0"))  # CGST
        self.item_table.setItem(row_position, 6, QTableWidgetItem("0.0"))  # SGST
        self.item_table.setItem(row_position, 7, QTableWidgetItem("0.0"))  # Total

    def update_row_totals(self, row):
        """Update CGST, SGST, and total for a specific row."""
        try:
            quantity = self.item_table.cellWidget(row, 2).value()
            rate = float(self.item_table.cellWidget(row, 3).text() or 0)
            gst_rate = int(self.item_table.cellWidget(row, 4).currentText())

            # Calculate CGST and SGST
            taxable_value = quantity * rate
            cgst = taxable_value * (gst_rate / 2) / 100
            sgst = taxable_value * (gst_rate / 2) / 100
            total = taxable_value + cgst + sgst

            # Update table
            self.item_table.setItem(row, 5, QTableWidgetItem(f"{cgst:.2f}"))
            self.item_table.setItem(row, 6, QTableWidgetItem(f"{sgst:.2f}"))
            self.item_table.setItem(row, 7, QTableWidgetItem(f"{total:.2f}"))

        except ValueError:
            pass  # Gracefully handle invalid input


    

    def save_as_pdf(self):
        """Save the invoice data as a PDF."""
        pdf = FPDF(orientation='P', unit='mm', format='A4')
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Header
        pdf.set_font("Arial", style="B", size=16)
        pdf.cell(200, 10, txt="Tax Invoice", ln=True, align="C")
        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, txt=f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Shop Name: {self.shop_name.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Shop Address: {self.shop_address.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Shop GSTIN: {self.shop_gstin.text()}", ln=True, align="L")

        pdf.cell(100, 10, txt=f"Customer Name: {self.customer_name.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Customer Address: {self.customer_address.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Customer GSTIN: {self.customer_gstin.text()}", ln=True, align="L")

        pdf.ln(10)  # Add space

        # Table Header
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(50, 10, "Description", border=1, align="C")
        pdf.cell(30, 10, "HSN Code", border=1, align="C")
        pdf.cell(20, 10, "Quantity", border=1, align="C")
        pdf.cell(20, 10, "Rate", border=1, align="C")
        pdf.cell(20, 10, "GST%", border=1, align="C")
        pdf.cell(20, 10, "CGST", border=1, align="C")
        pdf.cell(20, 10, "SGST", border=1, align="C")
        pdf.cell(30, 10, "Total", border=1, align="C")
        pdf.ln()

        # Table Rows
        pdf.set_font("Arial", size=12)
        grand_total = 0
        total_cgst = 0
        total_sgst = 0
        
        
        
        

        for row in range(self.item_table.rowCount()):
            description = self.item_table.cellWidget(row, 0).text()
            hsn = self.item_table.cellWidget(row, 1).text()
            quantity = self.item_table.cellWidget(row, 2).value()
            rate = float(self.item_table.cellWidget(row, 3).text() or 0)
            gst_rate = int(self.item_table.cellWidget(row, 4).currentText())
            cgst = float(self.item_table.item(row, 5).text())
            sgst = float(self.item_table.item(row, 6).text())
            total = float(self.item_table.item(row, 7).text())

            # Add row to PDF
            pdf.cell(50, 10, description, border=1)
            pdf.cell(30, 10, hsn, border=1, align="C")
            pdf.cell(20, 10, str(quantity), border=1, align="C")
            pdf.cell(20, 10, f"{rate:.2f}", border=1, align="C")
            pdf.cell(20, 10, str(gst_rate), border=1, align="C")
            pdf.cell(20, 10, f"{cgst:.2f}", border=1, align="C")
            pdf.cell(20, 10, f"{sgst:.2f}", border=1, align="C")
            pdf.cell(30, 10, f"{total:.2f}", border=1, align="C")
            pdf.ln()

            # Update totals
            grand_total += total
            total_cgst += cgst
            total_sgst += sgst
            
            
        pdf.ln(10)  # Add space for banking details


        # Totals
        pdf.ln(5)
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(100, 10, "Grand Total", ln=True)
        pdf.cell(50, 10, f"Total CGST: {total_cgst:.2f}", ln=True)
        pdf.cell(50, 10, f"Total SGST: {total_sgst:.2f}", ln=True)
        pdf.cell(50, 10, f"Total: {grand_total:.2f}", ln=True)




        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(200, 10, txt="Banking Details", ln=True, align="L")

        pdf.set_font("Arial", size=12)
        pdf.cell(100, 10, txt=f"Bank Name: {self.bank_name.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Account Number: {self.account_number.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"IFSC Code: {self.ifsc_code.text()}", ln=True, align="L")
        pdf.cell(100, 10, txt=f"Branch: {self.branch.text()}", ln=True, align="L")




        # Save the PDF
        file_name = f"Tax_Invoice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        pdf.output(file_name)
        print(f"Invoice saved as {file_name}")



class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tax Invoice System")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QVBoxLayout()

        # Buttons for different modules
        self.sale_bill_button = QPushButton("Sale Bill with GST")
        self.purchase_bill_button = QPushButton("Purchase Bill with GST")
        self.stock_button = QPushButton("Stock Maintenance")
        self.banking_button = QPushButton("Banking")

        # Connect buttons to actions
        self.sale_bill_button.clicked.connect(self.open_sale_bill)
        self.purchase_bill_button.clicked.connect(self.open_purchase_bill)
        self.stock_button.clicked.connect(self.open_stock)
        self.banking_button.clicked.connect(self.open_banking)

        # Add buttons to layout
        layout.addWidget(self.sale_bill_button)
        layout.addWidget(self.purchase_bill_button)
        layout.addWidget(self.stock_button)
        layout.addWidget(self.banking_button)

        # Set layout to central widget
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_sale_bill(self):
        global k
        k = SaleBill()
        k.show()
        print("Open Sale Bill Module")  # Replace with actual functionality

    def open_purchase_bill(self):
        print("Open Purchase Bill Module")  # Replace with actual functionality

    def open_stock(self):
        print("Open Stock Maintenance Module")  # Replace with actual functionality

    def open_banking(self):
        print("Open Banking Module")  # Replace with actual functionality


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainApp()
    main_window.show()
    sys.exit(app.exec())
