from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from random import randint

import os;os.system('cls')

def generate_tax_invoice(self):
    output_path = "tax_invoice.pdf"
    # Create a PDF document
    pdf = SimpleDocTemplate(output_path, pagesize=A4)
    elements = []

    # Add a margin border
    def add_margin_border(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(colors.black)
        canvas.setLineWidth(1)
        canvas.rect(10, 10, A4[0] - 20, A4[1] - 20)
        canvas.restoreState()

    styles = getSampleStyleSheet()
    
    grand_total = 0
    total_cgst = 0
    total_sgst = 0

    # Company and Invoice Details
    elements.append(Paragraph("<b>ABC Private Limited</b>", styles['Normal']))
    elements.append(Paragraph("<b>INVOICE RECEIPT</b>", styles['Title']))
    elements.append(Spacer(1, 20))

    # Display shop and contact details as text
    elements.append(Paragraph(f"<b>Date:</b> {datetime.now().strftime('%d-%m-%Y')}}", styles['Normal']))
    elements.append(Paragraph(f"<b>Shop Name:</b> {self.form.lineEdit_shop_name.text()}", styles['Normal']))
    elements.append(Paragraph(f"<b>Shop Address:</b> {self.form.lineEdit_shop_address.text()}", styles['Normal']))
    elements.append(Paragraph(f"<b>Aadhaar Number:</b> 1234-5678-9876", styles['Normal']))
    elements.append(Paragraph(f"<b>Mobile Number:</b> 9876543210", styles['Normal']))
    elements.append(Paragraph(f"<b>Email:</b> abc@gmail.com", styles['Normal']))
    elements.append(Spacer(1, 20))

    # Section 2: Billing and Shipping Address
    billing_details = [
        ["Billing Address", "Shipping Address"],
        [f"{self.form.lineEdit_shop_address.text()}, City", "456, Another St, City"],
        [f"GSTIN: {self.form.lineEdit_shop_gstin.text()}", "GSTIN: GST987654321"]
    ]

    billing_table = Table(billing_details, colWidths=[280, 280])
    billing_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
    ]))
    elements.append(billing_table)
    elements.append(Spacer(1, 20))

    # Section 3: Items Table (Including CGST, SGST, and Total)
    item_data = [
                     ["Description"    ,"HSN CODE" ,"Qty", "Amount" , "Total" ,"GST Rate", "CGST" , "SGST","Total"]
    ]
    
    
    for row in range(self.form.table_item_table.rowCount()):
        description = self.form.table_item_table.cellWidget(row, 0).text()
        hsn = self.form.table_item_table.cellWidget(row, 1).text()
        quantity = self.form.table_item_table.cellWidget(row, 2).value()
        rate = float(self.form.table_item_table.cellWidget(row, 3).text() or 0)
        gst_rate = int(self.form.table_item_table.cellWidget(row, 4).currentText())
        cgst = float(self.form.table_item_table.item(row, 5).text())
        sgst = float(self.form.table_item_table.item(row, 6).text())
        total = float(self.form.table_item_table.item(row, 7).text())

        
        grand_total += total
        total_cgst += cgst
        total_sgst += sgst
    
    item_data.append([f'{description}'          ,hsn       ,quantity    , rate   , 843.23  , gst_rate  ,cgst  , sgst , total])

    items_table = Table(item_data, colWidths=[150, 70, 40, 50, 50, 50, 50, 50, 50])
    items_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    elements.append(items_table)

    # Section 4: Total GST and Invoice Amount
    total_cgst_sgst = grand_total  # Sum of CGST and SGST
    total_invoice = 11683.81

    elements.append(Spacer(1, 20))

    totals = [
        ["Total GST Amount:", "1748.95"],
        ["Total Invoice Amount:", "11683.81"],
        ["Total CGST + SGST:", f"{total_cgst_sgst:.2f}"]
    ]
    totals_table = Table(totals, colWidths=[460, 100])
    totals_table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT')
    ]))
    elements.append(totals_table)


    bank_name = self.form.lineEdit_bank_name.text()
    acc_no = self.form.lineEdit_account_number.text()
    ifsc = self.form.lineEdit_ifsc_code.text()
    branch = self.form.lineEdit_branch.text()
    
    # Section 5: Authorized Signatory and Bank Details
    elements.append(Spacer(1, 60))
    elements.append(Paragraph("<b>Authorized Signatory</b>", styles['Normal']))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(f"<i>Bank Details:</i> {bank_name}, A/C: {acc_no}, IFSC: {ifsc}, Branch: {branch}", styles['Normal']))
    elements.append(Paragraph("<i>Terms and Conditions:</i> Payment due within 30 days.", styles['Normal']))

    # Build PDF
    pdf.build(elements, onFirstPage=add_margin_border, onLaterPages=add_margin_border)

