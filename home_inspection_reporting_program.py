import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json
import os

current_file = None  # Variable to track the current file being used for saving

def save_data(filename):
    """Saves form data to a specified JSON file."""
    data = {
        "inspector_name": entry_name.get(),
        "property_address": entry_address.get(),
        "findings": entry_findings.get("1.0", tk.END).strip()
    }
    with open(filename, "w") as file:
        json.dump(data, file)
    messagebox.showinfo("Success", f"Changes saved successfully to {filename}")
    update_window_title(filename)  # Update window title with the current file name

def save_as():
    """Save the form data to a new file."""
    filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
    if filename:
        global current_file
        current_file = filename
        save_data(current_file)
        generate_report_button.config(state=tk.NORMAL)  # Enable the Generate Report button

def save():
    """Save the form data to the current file (if any)."""
    if current_file:
        save_data(current_file)
    else:
        save_as()  # If no file exists, prompt the user to use Save As

def generate_report():
    """Generates a PDF report with the provided data, using the same filename as the JSON file."""
    if not current_file:
        messagebox.showwarning("Warning", "Please save the data first before generating a report.")
        return

    # Get the base name of the JSON file (without extension)
    base_filename = os.path.splitext(os.path.basename(current_file))[0]
    pdf_file = f"{base_filename}.pdf"  # Use the same base name for the PDF

    data = {
        "inspector_name": entry_name.get(),
        "property_address": entry_address.get(),
        "findings": entry_findings.get("1.0", tk.END).strip()
    }
    
    c = canvas.Canvas(pdf_file, pagesize=letter)
    c.drawString(100, 750, "Home Inspection Report")
    c.drawString(100, 730, f"Inspector: {data['inspector_name']}")
    c.drawString(100, 710, f"Property Address: {data['property_address']}")
    c.drawString(100, 690, f"Findings: {data['findings']}")

    c.save()
    messagebox.showinfo("Success", f"Report saved as {pdf_file}")

def update_window_title(filename):
    """Updates the window title to the name of the saved file."""
    file_name_display = os.path.basename(filename)
    root.title(f"Home Inspection Report Generator - {file_name_display}")

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

# Buttons
generate_report_button = tk.Button(root, text="Generate Report", command=generate_report, state=tk.DISABLED)
generate_report_button.grid(row=3, column=1)

save_button = tk.Button(root, text="Save", command=save)
save_button.grid(row=4, column=0)

save_as_button = tk.Button(root, text="Save As", command=save_as)
save_as_button.grid(row=5, column=0)  # Positioned below the Save button

# Run the application
root.mainloop()
