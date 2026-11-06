import os;os.system('cls')
from fpdf import FPDF
from datetime import datetime

def save_as_pdf():
    """Save the invoice data as a PDF."""
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Header
    pdf.set_font("Arial", style="B", size=16)
    pdf.cell(200, 10, text="Tax Invoice", ln=True, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, text=f"Date: {datetime.now().strftime('%d-%m-%Y')}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Shop Name: {'Navjeevan Clinic'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Shop Address: {'shyam nagar bhopal'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Shop GSTIN: {46546}", ln=True, align="L")

    pdf.cell(100, 10, text=f"Customer Name: {'abhishek verma'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Customer Address: {'block c6'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Customer GSTIN: {'465465'}", ln=True, align="L")

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
    
    
    
    

    for row in range(5):
        description = 'cough syrup'
        hsn = 35465
        quantity = 3
        rate = float(120)
        gst_rate = int(12)
        cgst = float(21.60)
        sgst = float(23.67)
        total = float(403.20)

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
    pdf.cell(200, 10, text="Banking Details", ln=True, align="L")

    pdf.set_font("Arial", size=12)
    pdf.cell(100, 10, text=f"Bank Name: {'canara bank'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Account Number: {'15465121356'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"IFSC Code: {'CNRB09809809'}", ln=True, align="L")
    pdf.cell(100, 10, text=f"Branch: {'Arera Colony'}", ln=True, align="L")




    # Save the PDF
    file_name = f"Tax_Invoice_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(file_name)
    print(f"Invoice saved as {file_name}")
    
    
save_as_pdf()

