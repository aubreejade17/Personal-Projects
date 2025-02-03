import tkinter as tk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Function to generate PDF report
def generate_report(data):
    pdf_file = "inspection_report.pdf"
    c = canvas.Canvas(pdf_file, pagesize=letter)
    
    # Add content to the PDF
    c.drawString(100, 750, "Home Inspection Report")
    c.drawString(100, 730, f"Inspector: {data['inspector_name']}")
    c.drawString(100, 710, f"Property Address: {data['property_address']}")
    c.drawString(100, 690, f"Findings: {data['findings']}")
    
    # Save the PDF
    c.save()
    messagebox.showinfo("Success", f"Report saved as {pdf_file}")

# Function to handle form submission
def submit_form():
    # Collect data from the form
    data = {
        "inspector_name": entry_name.get(),
        "property_address": entry_address.get(),
        "findings": entry_findings.get("1.0", tk.END).strip()
    }
    
    # Generate the report
    generate_report(data)

# GUI Setup
root = tk.Tk()
root.title("Home Inspection Report Generator")

# Inspector Name
tk.Label(root, text="Inspector Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

# Property Address
tk.Label(root, text="Property Address:").grid(row=1, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=1, column=1)

# Findings
tk.Label(root, text="Findings:").grid(row=2, column=0)
entry_findings = tk.Text(root, height=5, width=30)
entry_findings.grid(row=2, column=1)

# Generate Report Button
tk.Button(root, text="Generate Report", command=submit_form).grid(row=3, column=1)

# Run the application
root.mainloop()
