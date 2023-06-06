import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image

def convert_images_to_pdf(image_files, pdf_file):
    try:
        pdf = Image.open(image_files[0])
        pdf.save(pdf_file, "PDF", resolution=100.0, save_all=True, append_images=image_files[1:])
        messagebox.showinfo("Success", "PDF created successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create PDF.\nError: {e}")

def select_images():
    images = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=(("Image files", "*.jpg;*.jpeg;*.png"), ("All files", "*.*")),
        initialdir="C:/"
    )
    return images

def select_pdf():
    pdf_file = filedialog.asksaveasfilename(
        title="Save PDF As",
        defaultextension=".pdf",
        initialdir="C:/",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    return pdf_file

def convert_images_to_pdf_gui():
    root = tk.Tk()
    root.title("Image to PDF Converter")
    root.configure(bg="#292929")

    canvas = tk.Canvas(root, width=400, height=300, bg="#292929", highlightthickness=0)
    canvas.pack()

    title_label = tk.Label(canvas, text="Image to PDF Converter", font=("Arial", 20, "bold"), bg="#292929", fg="#00BFFF")
    title_label.pack(pady=20)

    select_images_btn = tk.Button(canvas, text="Choose Images", font=("Arial", 14), bg="#4C4C4C", fg="white", command=select_images)
    select_images_btn.pack(pady=10)

    select_pdf_btn = tk.Button(canvas, text="Choose PDF", font=("Arial", 14), bg="#4C4C4C", fg="white", command=select_pdf)
    select_pdf_btn.pack(pady=10)

    convert_btn = tk.Button(canvas, text="Convert to PDF", font=("Arial", 16, "bold"), bg="#00BFFF", fg="white",
                            command=lambda: convert_images_to_pdf(select_images(), select_pdf()))
    convert_btn.pack(pady=20)

    root.mainloop()

convert_images_to_pdf_gui()
