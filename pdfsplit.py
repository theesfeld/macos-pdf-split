#!/usr/bin/env python3

import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(input_path):
    try:
        pdf_reader = PdfReader(input_path)
        num_pages = len(pdf_reader.pages)
        
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_dir = os.path.dirname(input_path)
        
        status_label.config(text=f"Splitting into {num_pages} pages...")
        root.update()
        
        for page_num in range(num_pages):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_num])
            
            output_file = os.path.join(output_dir, f"{base_name}_page{page_num + 1}.pdf")
            with open(output_file, 'wb') as out_file:
                pdf_writer.write(out_file)
        
        status_label.config(text=f"Done! Split {num_pages} pages")
        messagebox.showinfo("Success", f"PDF split into {num_pages} pages\nSaved in: {output_dir}")
        
    except Exception as e:
        status_label.config(text="Error occurred")
        messagebox.showerror("Error", str(e))

def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        file_label.config(text=f"Selected: {os.path.basename(file_path)}")
        split_pdf(file_path)

# Create GUI
root = tk.Tk()
root.title("PDF Splitter")
root.geometry("400x200")
root.configure(bg="#f0f0f0")

# Styling
frame = tk.Frame(root, bg="#f0f0f0", pady=20)
frame.pack(expand=True)

title = tk.Label(frame, text="PDF Splitter", font=("Helvetica", 20, "bold"), bg="#f0f0f0")
title.pack(pady=10)

select_button = tk.Button(frame, text="Select PDF File", command=select_file,
                         bg="#4CAF50", fg="white", font=("Helvetica", 12),
                         padx=10, pady=5, relief="flat")
select_button.pack(pady=10)

file_label = tk.Label(frame, text="No file selected", bg="#f0f0f0", font=("Helvetica", 10))
file_label.pack()

status_label = tk.Label(frame, text="", bg="#f0f0f0", font=("Helvetica", 10))
status_label.pack(pady=5)

root.mainloop()
